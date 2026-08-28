#!/usr/bin/env node
// qa.mjs — the render-and-look gate for GSAP explainer decks.
//
// Gates catch broken; they have never caught bad. This tool makes LOOKING
// cheap, at the two places looking matters:
//
//   stills     three frames per scene — entry / payload / resolve — captured
//              by seeking the master timeline in a real Chromium. Seconds per
//              deck, no real-time playback, no render. Run it after every
//              scene edit, before spending a TTS take.
//
//   delivered  the same three moments per scene extracted from the SHIPPED
//              mp4 with ffmpeg. The file you deliver is the only artifact
//              whose behaviour is not an inference — sample it at the beats
//              you changed before calling a fix landed.
//
// One frame per scene is not a review: a mid-slot sample misses the built
// card row and the settled end-state alike (both shipped, both were caught
// by a human). Entry / payload / resolve is the floor.
//
//   node qa.mjs stills <explainer.html> [--out dir] [--durations 8,15,…]
//   node qa.mjs delivered <video.mp4> --durations 10.31,16.63,… [--out dir]
//                [--scenes 3,9] [--tail 0.5]
//
// stills reads durations from the booted page (its fallback timings) unless
// --durations overrides them — pass the render log's SCENE_DURATIONS to
// preview the film at the measured take. delivered needs --durations (from
// the render log) and auto-corrects for load skew by comparing the probed
// video length against durations + tail.
import { execFileSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';

const MOMENTS = [['entry', 0.15], ['payload', 0.55], ['resolve', 0.92]];

function die(msg) { console.error('qa: ' + msg); process.exit(1); }

function parseArgs(argv) {
  const args = { _: [] };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--out' || a === '--durations' || a === '--scenes' || a === '--tail') {
      args[a.slice(2)] = argv[++i];
    } else if (a.startsWith('--')) {
      die(`unknown flag ${a}`);
    } else {
      args._.push(a);
    }
  }
  return args;
}

function durationsFrom(str) {
  const d = str.split(',').map(Number);
  if (!d.length || d.some((n) => !isFinite(n) || n <= 0)) die(`bad --durations "${str}"`);
  return d;
}

function starts(durations) {
  const s = [];
  let at = 0;
  for (const d of durations) { s.push(at); at += d; }
  return s;
}

function sceneFilter(str, n) {
  if (!str) return null;
  const set = new Set(str.split(',').map((x) => parseInt(x, 10)));
  for (const i of set) if (!(i >= 1 && i <= n)) die(`--scenes entry ${i} out of range 1..${n}`);
  return set;
}

const args = parseArgs(process.argv.slice(2));
const mode = args._[0];
const target = args._[1];
if (!mode || !target) die('usage: qa.mjs stills <explainer.html> | delivered <video.mp4> [flags]');
if (!fs.existsSync(target)) die(`${target} not found`);
const outDir = path.resolve(args.out || `qa-${mode}`);
fs.mkdirSync(outDir, { recursive: true });

if (mode === 'stills') {
  let chromium;
  try { ({ chromium } = await import('playwright')); }
  catch { die('playwright is not installed — run `npm install && npx playwright install chromium` in tools/explainer-video.'); }

  // Overridden clock: rewrite the SCENE_DURATIONS literal in a temp copy,
  // exactly the way the pipeline's inject step does. An init-script cannot do
  // this — the page's own `window.SCENE_DURATIONS = []` contract literal runs
  // after it and wins. Safe because the contract requires the artifact to be
  // self-contained, so the copy loads without its original directory.
  let pageFile = path.resolve(target);
  let tmpFile = null;
  const wanted = args.durations ? durationsFrom(args.durations) : null;
  if (wanted) {
    const html = fs.readFileSync(pageFile, 'utf8');
    const RE = /window\.SCENE_DURATIONS\s*=\s*\[[^\]]*\]\s*;?/;
    if (!RE.test(html)) die(`${target} has no window.SCENE_DURATIONS assignment to inject into`);
    tmpFile = path.join(outDir, '.qa-injected.html');
    fs.writeFileSync(tmpFile, html.replace(RE, `window.SCENE_DURATIONS = [${wanted.join(', ')}];`));
    pageFile = tmpFile;
  }

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  const errors = [];
  page.on('pageerror', (e) => errors.push('pageerror: ' + e.message));
  page.on('console', (m) => { if (m.type() === 'error') errors.push('console.error: ' + m.text()); });
  await page.goto('file://' + pageFile);

  // boot() waits for load; poll rather than waitForFunction (heavy pages have
  // starved its rAF-based polling in practice).
  let booted = false;
  for (let i = 0; i < 100 && !booted; i++) {
    await page.waitForTimeout(200);
    booted = await page.evaluate(() => !!(window.__explainer && window.__explainer.master));
  }
  if (!booted) { await browser.close(); die('page never booted (no window.__explainer after 20s) — is the runtime inlined?'); }

  const info = await page.evaluate(() => ({
    durations: window.__explainer.durations,
    ids: window.__explainer.scenes.map((s) => s.dataset.scene || s.id || '?'),
  }));
  const durations = info.durations; // what the master timeline actually runs on
  if (wanted && (durations.length !== wanted.length ||
      durations.some((d, i) => Math.abs(d - wanted[i]) > 1e-6))) {
    await browser.close();
    die('injected durations did not reach the timeline — the page is not honouring the contract literal');
  }
  if (wanted && wanted.length !== info.ids.length) {
    die(`--durations has ${wanted.length} entries but the page has ${info.ids.length} scenes`);
  }
  await page.evaluate(() => { window.__explainer.master.pause(); });

  // Seek FORWARD only, with events firing, so one-way .call() state changes
  // (class flips, text swaps) land exactly as they would in playback.
  const st = starts(durations);
  const only = sceneFilter(args.scenes, durations.length);
  let shots = 0;
  for (let i = 0; i < durations.length; i++) {
    if (only && !only.has(i + 1)) continue;
    for (const [name, f] of MOMENTS) {
      const t = st[i] + durations[i] * f;
      await page.evaluate((tt) => { window.__explainer.master.time(tt, false); }, t);
      await page.waitForTimeout(120);
      const file = path.join(outDir,
        `scene-${String(i + 1).padStart(2, '0')}-${info.ids[i]}-${name}.png`);
      await page.screenshot({ path: file });
      shots++;
    }
    console.log(`scene ${i + 1} (${info.ids[i]}): entry/payload/resolve captured`);
  }
  await browser.close();
  if (tmpFile) fs.rmSync(tmpFile, { force: true });
  for (const e of errors) console.error('  ' + e);
  console.log(`\n${shots} stills in ${outDir}${errors.length ? ` — ${errors.length} PAGE ERRORS above` : ''}`);
  console.log('Now LOOK at them at full resolution — that is the gate.');
  if (errors.length) process.exit(1);

} else if (mode === 'delivered') {
  if (!args.durations) die('delivered mode needs --durations (copy SCENE_DURATIONS from the render log)');
  const durations = durationsFrom(args.durations);
  const tail = args.tail == null ? 0.5 : Number(args.tail);
  const sum = durations.reduce((a, b) => a + b, 0);

  let videoLen;
  try {
    videoLen = parseFloat(execFileSync('ffprobe',
      ['-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', target],
      { encoding: 'utf8' }));
  } catch { die('ffprobe not found — install ffmpeg'); }

  // The recording starts before scene 1 (page load + boot), so timeline zero
  // sits a little into the file. Estimate that skew and shift every sample.
  const skew = Math.max(0, videoLen - (sum + tail));
  if (videoLen + 0.5 < sum + tail) {
    die(`video is ${videoLen.toFixed(2)}s but durations+tail is ${(sum + tail).toFixed(2)}s — wrong --durations for this file?`);
  }
  console.log(`video ${videoLen.toFixed(2)}s, take ${sum.toFixed(2)}s + ${tail}s tail, load skew ~${skew.toFixed(2)}s`);

  const st = starts(durations);
  const only = sceneFilter(args.scenes, durations.length);
  let shots = 0;
  for (let i = 0; i < durations.length; i++) {
    if (only && !only.has(i + 1)) continue;
    for (const [name, f] of MOMENTS) {
      const t = (skew + st[i] + durations[i] * f).toFixed(2);
      const file = path.join(outDir, `scene-${String(i + 1).padStart(2, '0')}-${name}-t${t}.png`);
      execFileSync('ffmpeg', ['-v', 'error', '-ss', String(t), '-i', target, '-frames:v', '1', file, '-y']);
      shots++;
    }
    console.log(`scene ${i + 1}: entry/payload/resolve extracted`);
  }
  console.log(`\n${shots} frames from the DELIVERED file in ${outDir}`);
  console.log('Now LOOK at them at full resolution — that is the gate.');

} else {
  die(`unknown mode "${mode}" — use stills or delivered`);
}
