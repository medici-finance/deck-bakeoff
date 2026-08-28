// record.mjs <html-path> <out-dir>
// Records explainer.html to webm at 1920x1080 using Playwright, real-time,
// stopping when document.body.dataset.done === "1" (+ ~1s pad).
import { chromium } from 'playwright';
import path from 'node:path';
import fs from 'node:fs';

const [, , htmlPath, outDir] = process.argv;
if (!htmlPath || !outDir) {
  console.error('usage: node record.mjs <html-path> <out-dir>');
  process.exit(1);
}
fs.mkdirSync(outDir, { recursive: true });

const absHtml = path.resolve(htmlPath);
const absOut = path.resolve(outDir);

const browser = await chromium.launch();
const context = await browser.newContext({
  viewport: { width: 1920, height: 1080 },
  recordVideo: { dir: absOut, size: { width: 1920, height: 1080 } },
});
const page = await context.newPage();

// A deck that adopts the GSAP renderer calls window.GsapExplainer.boot() and
// carries the bundler's inline markers. Reading that from the source lets the
// boot watchdog below tell a genuinely long render apart from a GSAP deck whose
// runtime never loaded — the un-bundled case, where GsapExplainer is undefined,
// boot() threw at parse, and nothing will ever raise data-done. A hand-rolled
// deck that never mentions the runtime matches neither and is left untouched.
const deckSrc = fs.readFileSync(absHtml, 'utf8');
const wantsGsap = /gsap-explainer:inline|GsapExplainer\s*\.\s*boot/.test(deckSrc);

await page.goto('file://' + absHtml);

// Poll for completion (real-time, no timer throttling issue since page is foregrounded).
const start = Date.now();
// The watchdog must outlast the film. A fixed 5-minute cap truncated the first
// 7-minute render, so derive the budget from the page's injected
// SCENE_DURATIONS when present (sum + 60s margin); keep 5 minutes as the floor
// for pages with no durations, and allow EXPLAINER_MAX_WAIT_S to override.
const declaredS = await page.evaluate(() =>
  Array.isArray(window.SCENE_DURATIONS)
    ? window.SCENE_DURATIONS.reduce((a, b) => a + (Number(b) || 0), 0)
    : 0);
// EXPLAINER_MAX_WAIT_S overrides the derived budget, but only when it parses to
// a finite number of seconds. A non-numeric value ("600s", "10m") yields NaN,
// which propagates through Math.max below and would disable the watchdog
// entirely (Date.now() - start > NaN is always false, so the loop never times
// out and the render hangs forever). Fall back to 0 on a non-finite value so
// the 5-minute floor / SCENE_DURATIONS budget still applies and the watchdog
// always fires.
const parsedEnvS = Number(process.env.EXPLAINER_MAX_WAIT_S);
const envS = Number.isFinite(parsedEnvS) ? parsedEnvS : 0;
const maxWaitMs = Math.max(5 * 60, envS, declaredS + 60) * 1000;
// A short boot watchdog, separate from the film-length ceiling above: a GSAP
// deck whose runtime never loaded can never raise data-done, so waiting the full
// ceiling only delays an inevitable failure and ships a video of a dead page.
// EXPLAINER_BOOT_GRACE_S overrides it, falling back to 8s on a non-finite value.
const parsedBootS = Number(process.env.EXPLAINER_BOOT_GRACE_S);
const bootGraceMs = (Number.isFinite(parsedBootS) ? parsedBootS : 8) * 1000;
let timedOut = false;
let bootFailed = false;
while (true) {
  const st = await page.evaluate(() => ({
    done: document.body.dataset.done === '1',
    // "The runtime got as far as executing." GsapExplainer is defined once the
    // runtime script ran; __explainer once run() reached the end; a doneReason
    // once it signalled either way. Any one means the deck is NOT the dead
    // un-bundled page — leave it to the full budget (it may be mid-render).
    started: typeof window.GsapExplainer !== 'undefined'
      || !!window.__explainer
      || !!document.body.dataset.doneReason,
  }));
  if (st.done) break;
  const elapsed = Date.now() - start;
  // Fast-fail backstop: an un-bundled GSAP deck (empty inline slots, so no
  // runtime on the page) never started and never will — fail in seconds with a
  // precise remedy instead of at the 5-minute ceiling.
  if (wantsGsap && !st.started && elapsed > bootGraceMs) {
    bootFailed = true;
    break;
  }
  if (elapsed > maxWaitMs) {
    console.error('timeout waiting for data-done=1');
    timedOut = true;
    break;
  }
  await page.waitForTimeout(200);
}
// ~1s pad after done
await page.waitForTimeout(1000);

// A renderer may report HOW it finished. `complete` is the only success value;
// anything else (a build that threw, a watchdog that fired) means the capture is
// broken or partial. Pages that set no reason are not judged, so hand-rolled
// explainer.html decks keep working unchanged.
const status = await page.evaluate(() => ({
  reason: document.body.dataset.doneReason || null,
  error: document.body.dataset.error || null,
}));

const videoPath = await page.video().path();
await context.close();
await browser.close();

console.log('RECORDED:' + videoPath);

// Exit non-zero rather than let a broken or truncated capture pass as a
// finished render: the caller runs this with check=True.
if (bootFailed) {
  console.error('FAILED: window.GsapExplainer never initialized within '
    + bootGraceMs / 1000 + 's — the deck is un-bundled or GsapExplainer failed to '
    + 'boot, so it can never signal data-done. Inline the GSAP runtime by running '
    + 'renderers/gsap/bundle.mjs on the deck\'s explainer.html '
    + '(the explainer-video pipeline auto-bundles a work copy; a deck passed '
    + 'straight to record.mjs must already be bundled).');
  process.exit(1);
}
if (timedOut) {
  console.error('FAILED: the page never signalled data-done=1 within '
    + maxWaitMs / 1000 + 's — the recording is truncated, not a finished render.');
  process.exit(1);
}
if (status.reason && status.reason !== 'complete') {
  console.error('FAILED: renderer reported data-done-reason="' + status.reason + '"'
    + (status.error ? ' — ' + status.error : ''));
  process.exit(1);
}
