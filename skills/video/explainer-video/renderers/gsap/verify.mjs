#!/usr/bin/env node
// verify.mjs — behavioural checks for the GSAP renderer adapter.
//
//   node verify.mjs            # or: npm test
//
// Every case drives the REAL runtime (src/gsap-explainer.js) in a real
// Chromium via Playwright and asserts on measured numbers — timeline spans,
// computed styles, the done signal. Nothing here is a mock.
//
// There is deliberately NO skip path. If `gsap` or `playwright` is missing the
// suite EXITS 1 with instructions rather than reporting green, because a green
// run that silently skipped the browser proves nothing about a renderer.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const GSAP = path.join(HERE, 'node_modules', 'gsap', 'dist', 'gsap.min.js');
const DRAWSVG = path.join(HERE, 'node_modules', 'gsap', 'dist', 'DrawSVGPlugin.min.js');
const RUNTIME = path.join(HERE, 'src', 'gsap-explainer.js');

function die(msg) {
  console.error('verify: ' + msg);
  process.exit(1);
}

for (const [label, p] of [['gsap core', GSAP], ['DrawSVGPlugin', DRAWSVG], ['runtime', RUNTIME]]) {
  if (!fs.existsSync(p)) die(`${label} not found at ${p} — run \`npm install\` in ${HERE}.`);
}

let chromium;
try {
  ({ chromium } = await import('playwright'));
} catch {
  die('playwright is not installed — run `npm install && npx playwright install chromium` in '
    + path.resolve(HERE, '..', '..') + '.');
}

const url = (p) => 'file://' + p;

/** Build a self-contained fixture page around the real runtime. */
function fixture({ body, boot, durations }) {
  const inject = durations == null ? '[]' : JSON.stringify(durations);
  return `<!doctype html><html><head><meta charset="utf-8"><style>
    html,body{margin:0;background:#fff;width:1920px;height:1080px;font-family:system-ui}
    [data-scene]{position:absolute;inset:0;opacity:0;visibility:hidden}
  </style></head><body>
${body}
<script src="${url(GSAP)}"></script>
<script src="${url(DRAWSVG)}"></script>
<script src="${url(RUNTIME)}"></script>
<script>window.SCENE_DURATIONS = ${inject};</script>
<script>
window.__warnings = []; window.__errors = [];
var _w = console.warn, _e = console.error;
console.warn = function(){ window.__warnings.push(Array.prototype.join.call(arguments,' ')); _w.apply(console, arguments); };
console.error = function(){ window.__errors.push(Array.prototype.join.call(arguments,' ')); _e.apply(console, arguments); };
window.addEventListener('load', function () {
  try { window.__result = (${boot})(); window.__booted = true; }
  catch (err) { window.__bootError = String(err && err.message || err); window.__booted = true; }
});
</script></body></html>`;
}

const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'gsap-verify-'));
const browser = await chromium.launch();

const results = [];
async function check(name, spec, assertFn) {
  const file = path.join(tmp, name.replace(/[^a-z0-9]+/gi, '-') + '.html');
  fs.writeFileSync(file, fixture(spec));
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  const failures = [];
  try {
    await page.goto(url(file));
    await page.waitForFunction('window.__booted === true', null, { timeout: 15000 });
    const problems = await assertFn(page);
    if (problems && problems.length) failures.push(...problems);
  } catch (err) {
    failures.push('threw: ' + (err && err.message ? err.message.split('\n')[0] : String(err)));
  } finally {
    await page.close();
  }
  results.push({ name, failures });
  const tag = failures.length ? 'FAIL' : 'ok  ';
  console.log(`${tag}  ${name}`);
  for (const f of failures) console.log(`        ${f}`);
}

const near = (a, b, tol) => Math.abs(a - b) <= tol;

// A scene body with three stroked paths under one [data-draw] container.
const DIAGRAM = `<section data-scene="diagram">
  <h1 data-enter>Diagram</h1>
  <svg width="600" height="200" viewBox="0 0 600 200" data-draw>
    <path d="M20,100 L200,100" stroke="#111" stroke-width="3" fill="none"/>
    <path d="M200,100 L380,100" stroke="#111" stroke-width="3" fill="none"/>
    <path d="M380,100 L560,100" stroke="#111" stroke-width="3" fill="none"/>
  </svg>
</section>`;

// --- 1. injected durations are honoured exactly -----------------------------
await check('injected SCENE_DURATIONS drive the master total', {
  durations: [3.21, 11.87, 5.04],
  body: `<section data-scene="a"><h1 data-enter>A</h1></section>
         <section data-scene="b"><h1 data-enter>B</h1></section>
         <section data-scene="c"><h1 data-enter>C</h1></section>`,
  boot: `function(){ return GsapExplainer.run({ autostart: false }); }`,
}, async (page) => {
  const r = await page.evaluate(() => ({
    total: window.__result.total,
    durations: window.__result.durations,
    warnings: window.__warnings,
    bootError: window.__bootError || null,
  }));
  const out = [];
  if (r.bootError) out.push('boot threw: ' + r.bootError);
  if (!near(r.total, 20.12, 1e-6)) out.push(`master total ${r.total} != 20.12`);
  if (JSON.stringify(r.durations) !== JSON.stringify([3.21, 11.87, 5.04])) {
    out.push('durations ' + JSON.stringify(r.durations));
  }
  if (r.warnings.length) out.push('unexpected warnings: ' + JSON.stringify(r.warnings));
  return out;
});

// --- 2. no injection => fallback + a loud warning ----------------------------
await check('uninjected page falls back and warns', {
  durations: null,
  body: `<section data-scene="a"><h1 data-enter>A</h1></section>
         <section data-scene="b"><h1 data-enter>B</h1></section>`,
  boot: `function(){ return GsapExplainer.run({ autostart: false, fallback: [4, 8] }); }`,
}, async (page) => {
  const r = await page.evaluate(() => ({
    total: window.__result.total, warnings: window.__warnings,
  }));
  const out = [];
  if (!near(r.total, 12, 1e-6)) out.push(`fallback total ${r.total} != 12`);
  if (!r.warnings.some((w) => /no window\.SCENE_DURATIONS injected/.test(w))) {
    out.push('no fallback warning emitted; saw ' + JSON.stringify(r.warnings));
  }
  return out;
});

// --- 3. a flexible draw fills the measured scene -----------------------------
await check('flexible draw stretches to fill the scene', {
  durations: [10],
  body: DIAGRAM,
  boot: `function(){ return GsapExplainer.run({ autostart: false, scenes: [
      { id: 'diagram', build: function (tl, ctx) { ctx.enter('h1'); ctx.draw('svg'); } },
    ] }); }`,
}, async (page) => {
  const r = await page.evaluate(() => ({
    span: window.__result.timelines[0].duration(),
    scale: window.__result.timelines[0].timeScale(),
    warnings: window.__warnings,
  }));
  const out = [];
  // available = 10 - 0.2 crossfade
  if (!near(r.span, 9.8, 0.05)) out.push(`scene span ${r.span} != ~9.8`);
  if (!near(r.scale, 1, 1e-9)) out.push(`scene timeScale ${r.scale} != 1 (it should not need compressing)`);
  if (r.warnings.length) out.push('unexpected warnings: ' + JSON.stringify(r.warnings));
  return out;
});

// --- 4. ctx.flex(ctx.hold(...)) flexes the HOLD, not the whole timeline -------
// Regression: field report from assay-decks#4. `tl.to()` / `tl.fromTo()` return
// the TIMELINE for chaining, so registering that return value as flexible
// time-scaled the entire scene.
await check('flex(hold) flexes only the held span', {
  durations: [10],
  body: `<section data-scene="a"><h1 data-enter>A</h1><p data-enter>b</p></section>`,
  boot: `function(){ return GsapExplainer.run({ autostart: false, scenes: [
      { id: 'a', build: function (tl, ctx) {
          window.__enter = ctx.enter('h1');
          window.__held = ctx.flex(ctx.hold(1));
        } },
    ] }); }`,
}, async (page) => {
  const r = await page.evaluate(() => {
    const tl = window.__result.timelines[0];
    const kids = tl.getChildren(false);
    return {
      span: tl.duration(),
      scale: tl.timeScale(),
      kidCount: kids.length,
      kidDurations: kids.map((k) => k.duration()),
      enterIsTimeline: typeof window.__enter.getChildren === 'function',
      holdIsTimeline: typeof window.__held.getChildren === 'function',
    };
  });
  const out = [];
  if (r.enterIsTimeline) out.push('ctx.enter returned the scene TIMELINE, not the tween');
  if (r.holdIsTimeline) out.push('ctx.hold returned the scene TIMELINE, not the tween');
  if (!near(r.scale, 1, 1e-9)) out.push(`scene timeScale ${r.scale} != 1 — the whole timeline was flexed`);
  if (!near(r.span, 9.8, 0.05)) out.push(`scene span ${r.span} != ~9.8`);
  if (r.kidCount !== 2) out.push(`expected 2 children, got ${r.kidCount}`);
  if (r.kidDurations[0] != null && !near(r.kidDurations[0], 0.2, 1e-6)) {
    out.push(`enter duration ${r.kidDurations[0]} != 0.2 — the fixed enter was stretched`);
  }
  return out;
});

// --- 5. an authored dash pattern survives ctx.draw ---------------------------
// Regression: field report from medici-decks#14. Stroke draw-on (DrawSVG or the
// dashoffset fallback) OWNS stroke-dasharray, so drawing a dashed reference
// line silently turned it solid.
await check('authored stroke-dasharray survives ctx.draw', {
  durations: [3],
  body: `<section data-scene="a">
    <svg width="600" height="200" viewBox="0 0 600 200" data-draw>
      <path id="dashed" d="M20,60 L560,60" stroke="#888" stroke-width="2" fill="none" stroke-dasharray="8 6"/>
      <path id="solid" d="M20,140 L560,140" stroke="#111" stroke-width="3" fill="none"/>
    </svg></section>`,
  boot: `function(){ return GsapExplainer.run({ autostart: false, scenes: [
      { id: 'a', build: function (tl, ctx) { ctx.draw('svg'); } },
    ] }); }`,
}, async (page) => {
  const r = await page.evaluate(() => {
    // Jump to the end without burning wall-clock.
    window.__result.master.progress(1, true);
    const d = document.getElementById('dashed');
    const s = document.getElementById('solid');
    const cs = (el) => getComputedStyle(el);
    return {
      dashArray: cs(d).strokeDasharray,
      dashOpacity: cs(d).opacity,
      dashOffset: cs(d).strokeDashoffset,
      solidOffset: cs(s).strokeDashoffset,
      solidArray: cs(s).strokeDasharray,
    };
  });
  const out = [];
  const nums = (r.dashArray || '').match(/[\d.]+/g) || [];
  if (nums.length !== 2 || Math.round(+nums[0]) !== 8 || Math.round(+nums[1]) !== 6) {
    out.push(`dashed path stroke-dasharray is "${r.dashArray}" — the authored 8 6 pattern was destroyed`);
  }
  if (Math.round(parseFloat(r.dashOffset)) !== 0) {
    out.push(`dashed path stroke-dashoffset ${r.dashOffset} != 0 — it is left partly hidden`);
  }
  if (parseFloat(r.dashOpacity) < 0.99) out.push(`dashed path never became visible (opacity ${r.dashOpacity})`);
  // The solid path must still be genuinely drawn on, not silently skipped.
  if (Math.round(parseFloat(r.solidOffset)) !== 0) out.push(`solid path not fully drawn (offset ${r.solidOffset})`);
  if (!/[\d.]/.test(r.solidArray || '')) out.push('solid path was never dash-seeded — it was not drawn on at all');
  return out;
});

// --- 6. a healthy run reports doneReason=complete ----------------------------
await check('healthy run signals done with reason=complete', {
  durations: [1, 1],
  body: `<section data-scene="a"><h1 data-enter>A</h1></section>
         <section data-scene="b"><h1 data-enter>B</h1></section>`,
  boot: `function(){ return GsapExplainer.run({}); }`,
}, async (page) => {
  await page.waitForFunction("document.body.dataset.done === '1'", null, { timeout: 20000 });
  const r = await page.evaluate(() => ({
    reason: document.body.dataset.doneReason,
    error: document.body.dataset.error || null,
    errors: window.__errors,
  }));
  const out = [];
  if (r.reason !== 'complete') out.push(`doneReason "${r.reason}" != complete`);
  if (r.error) out.push('dataset.error set on a healthy run: ' + r.error);
  if (r.errors.length) out.push('console errors: ' + JSON.stringify(r.errors));
  return out;
});

// --- 7. a failing render must NOT look like a success ------------------------
// The done flag is the ONLY channel the recorder reads. A scene build that
// throws must therefore still raise it (so the recorder fails in seconds rather
// than burning its 5-minute ceiling) but must mark the run as failed, so
// record.mjs can exit non-zero instead of shipping a broken video as success.
await check('a throwing scene build is reported as a failure, not success', {
  durations: [1],
  body: `<section data-scene="a"><h1 data-enter>A</h1></section>`,
  boot: `function(){ return GsapExplainer.run({ scenes: [
      { id: 'a', build: function () { throw new Error('deliberate build failure'); } },
    ] }); }`,
}, async (page) => {
  await page.waitForFunction("document.body.dataset.done === '1'", null, { timeout: 20000 });
  const r = await page.evaluate(() => ({
    done: document.body.dataset.done,
    reason: document.body.dataset.doneReason,
    error: document.body.dataset.error || null,
    errors: window.__errors,
  }));
  const out = [];
  if (r.done !== '1') out.push('done flag never raised — the recorder would hang for 5 minutes');
  if (r.reason === 'complete') out.push('FAILED RENDER REPORTED AS COMPLETE');
  if (r.reason !== 'error') out.push(`doneReason "${r.reason}" != error`);
  if (!r.error || !/deliberate build failure/.test(r.error)) {
    out.push(`dataset.error does not name the cause: ${r.error}`);
  }
  if (!r.errors.some((e) => /deliberate build failure/.test(e))) out.push('nothing logged to console.error');
  return out;
});

// --- 8. a page with no scenes is a failure, not an empty success -------------
await check('a page with no scenes fails loudly', {
  durations: [1],
  body: `<div>no scenes here</div>`,
  boot: `function(){ return GsapExplainer.run({}); }`,
}, async (page) => {
  await page.waitForFunction("document.body.dataset.done === '1'", null, { timeout: 20000 });
  const r = await page.evaluate(() => ({
    reason: document.body.dataset.doneReason,
    error: document.body.dataset.error || null,
  }));
  const out = [];
  if (r.reason === 'complete') out.push('EMPTY PAGE REPORTED AS COMPLETE');
  if (r.reason !== 'error') out.push(`doneReason "${r.reason}" != error`);
  if (!r.error) out.push('dataset.error not set');
  return out;
});

// --- 9. over-long content compresses and says so -----------------------------
await check('over-long content compresses with a named warning', {
  durations: [0.7],
  body: DIAGRAM,
  boot: `function(){ return GsapExplainer.run({ autostart: false, scenes: [
      { id: 'diagram', build: function (tl, ctx) { ctx.enter('h1'); ctx.draw('svg', { duration: 3 }); } },
    ] }); }`,
}, async (page) => {
  const r = await page.evaluate(() => ({
    scale: window.__result.timelines[0].timeScale(),
    warnings: window.__warnings,
  }));
  const out = [];
  if (r.scale <= 1) out.push(`timeScale ${r.scale} — content was not compressed`);
  if (!r.warnings.some((w) => /compressing/.test(w) && /diagram/.test(w))) {
    out.push('no compression warning naming the scene: ' + JSON.stringify(r.warnings));
  }
  return out;
});

// --- 10. off-brand easing warns ----------------------------------------------
await check('off-brand ease warns', {
  durations: [2],
  body: `<section data-scene="a"><h1 data-enter>A</h1></section>`,
  boot: `function(){ return GsapExplainer.run({ autostart: false, scenes: [
      { id: 'a', build: function (tl, ctx) { ctx.enter('h1', { ease: 'back.out(1.7)' }); } },
    ] }); }`,
}, async (page) => {
  const warnings = await page.evaluate(() => window.__warnings);
  return warnings.some((w) => /off-brand ease/.test(w))
    ? [] : ['no off-brand-ease warning: ' + JSON.stringify(warnings)];
});

// --- 11. data-exit="cut" hands the next scene its full measured duration -----
// The handoff into a scene is charged to that scene's budget; a hard cut costs
// nothing, so the incoming scene keeps all of its narration time.
await check('data-exit=cut is a one-frame swap and costs the incoming scene nothing', {
  durations: [4, 4],
  body: `<section data-scene="a" data-exit="cut"><h1 data-enter>A</h1></section>
         <section data-scene="b">
           <svg width="600" height="200" viewBox="0 0 600 200" data-draw>
             <path d="M20,100 L560,100" stroke="#111" stroke-width="3" fill="none"/>
           </svg>
         </section>`,
  boot: `function(){ return GsapExplainer.run({ autostart: false }); }`,
}, async (page) => {
  const r = await page.evaluate(() => {
    const m = window.__result.master;
    const a = document.querySelector('[data-scene="a"]');
    const b = document.querySelector('[data-scene="b"]');
    m.time(3.99, true);
    const before = { aOp: +getComputedStyle(a).opacity, bVis: getComputedStyle(b).visibility };
    m.time(4.02, true);
    const after = {
      aOp: +getComputedStyle(a).opacity, aVis: getComputedStyle(a).visibility,
      bOp: +getComputedStyle(b).opacity,
    };
    return { before, after, spanB: window.__result.timelines[1].duration(), warnings: window.__warnings };
  });
  const out = [];
  if (!near(r.spanB, 4.0, 0.05)) out.push(`incoming scene span ${r.spanB} != ~4.0 — the cut was charged like a fade`);
  if (r.before.aOp < 0.99) out.push(`outgoing scene already fading before the cut (opacity ${r.before.aOp})`);
  if (r.after.aOp > 0.01 || r.after.aVis !== 'hidden') {
    out.push(`outgoing scene still visible after the cut (opacity ${r.after.aOp}, visibility ${r.after.aVis})`);
  }
  if (r.after.bOp < 0.99) out.push(`incoming scene not fully on after the cut (opacity ${r.after.bOp})`);
  if (r.warnings.length) out.push('unexpected warnings: ' + JSON.stringify(r.warnings));
  return out;
});

// --- 12. data-exit="push" moves both scenes and cleans up after itself -------
await check('data-exit=push moves both scenes through the boundary and clears its transform', {
  durations: [2, 2],
  body: `<section data-scene="a" data-exit="push"><h1 data-enter>A</h1></section>
         <section data-scene="b"><h1 data-enter>B</h1></section>`,
  boot: `function(){ return GsapExplainer.run({ autostart: false }); }`,
}, async (page) => {
  const r = await page.evaluate(() => {
    const m = window.__result.master;
    const a = document.querySelector('[data-scene="a"]');
    const b = document.querySelector('[data-scene="b"]');
    const ty = (el) => {
      const t = getComputedStyle(el).transform;
      return t === 'none' ? 0 : new DOMMatrixReadOnly(t).m42;
    };
    m.time(2.15, true); // mid-boundary: push runs 2.0 → 2.3
    const mid = { aY: ty(a), bY: ty(b), bOp: +getComputedStyle(b).opacity };
    m.progress(1, true);
    const end = {
      aVis: getComputedStyle(a).visibility,
      aTransform: getComputedStyle(a).transform,
      bOp: +getComputedStyle(b).opacity,
      bY: ty(b),
    };
    return { mid, end, warnings: window.__warnings };
  });
  const out = [];
  if (!(r.mid.bY > 1)) out.push(`incoming scene is not rising mid-boundary (y=${r.mid.bY})`);
  if (!(r.mid.aY < -1)) out.push(`outgoing scene is not pushed away mid-boundary (y=${r.mid.aY})`);
  if (!(r.mid.bOp > 0.01 && r.mid.bOp < 0.99)) out.push(`incoming opacity ${r.mid.bOp} not mid-fade`);
  if (r.end.aVis !== 'hidden') out.push(`outgoing scene not hidden at the end (visibility ${r.end.aVis})`);
  if (r.end.aTransform !== 'none') out.push(`outgoing scene's push transform was not cleared: ${r.end.aTransform}`);
  if (r.end.bOp < 0.99 || Math.abs(r.end.bY) > 0.01) {
    out.push(`incoming scene did not settle (opacity ${r.end.bOp}, y ${r.end.bY})`);
  }
  if (r.warnings.length) out.push('unexpected warnings: ' + JSON.stringify(r.warnings));
  return out;
});

// --- 13. unknown / final-scene data-exit warn instead of failing --------------
await check('unknown data-exit warns and falls back to fade; final-scene data-exit warns', {
  durations: [4, 4],
  body: `<section data-scene="a" data-exit="wipe"><h1 data-enter>A</h1></section>
         <section data-scene="b" data-exit="cut">
           <svg width="600" height="200" viewBox="0 0 600 200" data-draw>
             <path d="M20,100 L560,100" stroke="#111" stroke-width="3" fill="none"/>
           </svg>
         </section>`,
  boot: `function(){ return GsapExplainer.run({ autostart: false }); }`,
}, async (page) => {
  const r = await page.evaluate(() => ({
    spanB: window.__result.timelines[1].duration(),
    warnings: window.__warnings,
    reason: document.body.dataset.doneReason || null,
  }));
  const out = [];
  if (!r.warnings.some((w) => /unknown data-exit="wipe"/.test(w))) {
    out.push('no unknown-data-exit warning: ' + JSON.stringify(r.warnings));
  }
  if (!near(r.spanB, 3.8, 0.05)) out.push(`incoming scene span ${r.spanB} != ~3.8 — the fallback is not a fade`);
  if (!r.warnings.some((w) => /data-exit on the final scene/.test(w))) {
    out.push('no final-scene data-exit warning: ' + JSON.stringify(r.warnings));
  }
  if (r.reason === 'error') out.push('a typo\'d data-exit failed the render — it must warn and fall back');
  return out;
});

await browser.close();
fs.rmSync(tmp, { recursive: true, force: true });

const failed = results.filter((r) => r.failures.length);
console.log(`\n${results.length - failed.length}/${results.length} checks passed`);
if (failed.length) {
  console.error('FAILED: ' + failed.map((f) => f.name).join(', '));
  process.exit(1);
}
