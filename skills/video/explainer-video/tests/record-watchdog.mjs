#!/usr/bin/env node
// record-watchdog.mjs — end-to-end proof of the un-bundled-deck fix, driving the
// REAL pipeline/record.mjs in a real Chromium.
//
//   cd tools/explainer-video
//   npm install && npx playwright install chromium          # once
//   (cd renderers/gsap && npm install)                      # the bundler's gsap
//   node tests/record-watchdog.mjs
//
// Not CI-wired (repo CI is lint-only). Two cases, the before/after of the fix:
//
//   1. An UN-BUNDLED deck (empty inline slots — window.GsapExplainer undefined)
//      handed straight to record.mjs fails in SECONDS with the remedy, instead
//      of burning the 5-minute ceiling. This is the incident.
//   2. The SAME deck, once auto-bundled (what the orchestrator now does to the
//      work copy) and injected with durations, records to a webm and record.mjs
//      exits 0 — which, because record.mjs exits non-zero on any doneReason but
//      `complete`, proves the render reached doneReason=complete.
//
// There is deliberately no skip path: a green run that silently skipped the
// browser would prove nothing. Missing deps exit 1 with install instructions.
import { execFileSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const TOOL = path.resolve(HERE, '..');
const RECORD = path.join(TOOL, 'pipeline', 'record.mjs');
const BUNDLE = path.join(TOOL, 'renderers', 'gsap', 'bundle.mjs');
const TEMPLATE = path.join(TOOL, 'renderers', 'gsap', 'template.html');
const GSAP_MIN = path.join(TOOL, 'renderers', 'gsap', 'node_modules', 'gsap', 'dist', 'gsap.min.js');

function die(msg) {
  console.error('record-watchdog: ' + msg);
  process.exit(1);
}
if (!fs.existsSync(path.join(TOOL, 'node_modules', 'playwright'))) {
  die('playwright is not installed — run `npm install && npx playwright install chromium` in ' + TOOL);
}
if (!fs.existsSync(GSAP_MIN)) {
  die('the bundler\'s gsap sources are missing — run `npm install` in ' + path.join(TOOL, 'renderers', 'gsap'));
}

const SD_RE = /window\.SCENE_DURATIONS\s*=\s*\[[^\]]*\]\s*;?/;
function injectDurations(file, seconds) {
  const html = fs.readFileSync(file, 'utf8');
  fs.writeFileSync(file, html.replace(SD_RE, `window.SCENE_DURATIONS=[${seconds.join(', ')}];`));
}

// Run record.mjs; never throw on non-zero exit. Returns { code, output, ms }.
function record(html, outDir, env) {
  const started = Date.now();
  try {
    const out = execFileSync(process.execPath, [RECORD, html, outDir], {
      encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'], timeout: 120000,
      env: { ...process.env, ...env },
    });
    return { code: 0, output: out, ms: Date.now() - started };
  } catch (err) {
    if (err.killed) die('record.mjs did not exit within 120s — the watchdog never fired (this is the bug).');
    return { code: err.status == null ? 1 : err.status, output: `${err.stdout || ''}${err.stderr || ''}`, ms: Date.now() - started };
  }
}

const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'record-watchdog-'));
const results = [];
function check(name, fn) {
  let failures = [];
  try { failures = fn() || []; } catch (err) { failures = ['threw: ' + ((err && err.message) || err)]; }
  results.push({ name, failures });
  console.log(`${failures.length ? 'FAIL' : 'ok  '}  ${name}`);
  for (const f of failures) console.log(`        ${f}`);
}

// --- 1. an un-bundled deck fails fast with the remedy, not at 300s ------------
check('an un-bundled deck fails in seconds with the bundle remedy', () => {
  const deck = path.join(tmp, 'unbundled.html');
  fs.copyFileSync(TEMPLATE, deck);          // template ships UN-bundled
  injectDurations(deck, [0.3, 0.3]);        // durations present, runtime absent
  const out = path.join(tmp, 'rec-unbundled');
  // 3s boot grace keeps the test snappy; the point is it is nowhere near 300s.
  const r = record(deck, out, { EXPLAINER_BOOT_GRACE_S: '3' });
  const problems = [];
  if (r.code === 0) problems.push('record.mjs exited 0 on a deck that never initialized');
  if (r.ms > 60000) problems.push(`took ${(r.ms / 1000).toFixed(1)}s — the fast-fail did not fire (ceiling is 300s)`);
  if (!/un-bundled or GsapExplainer failed to boot/.test(r.output)) {
    problems.push('remedy message missing from output: ' + r.output.trim().split('\n').slice(-3).join(' | '));
  }
  if (!/bundle\.mjs/.test(r.output)) problems.push('remedy does not point at bundle.mjs');
  return problems;
});

// --- 2. the same deck, auto-bundled, records to completion -------------------
check('an auto-bundled deck records and record.mjs exits 0 (doneReason=complete)', () => {
  const deck = path.join(tmp, 'bundled.html');
  fs.copyFileSync(TEMPLATE, deck);
  // This is exactly what the orchestrator's maybe_bundle_slides does to the work
  // copy: inline the runtime in place, then the pipeline injects durations.
  execFileSync(process.execPath, [BUNDLE, deck], { stdio: 'ignore' });
  injectDurations(deck, [0.3, 0.3]);
  const out = path.join(tmp, 'rec-bundled');
  const r = record(deck, out);
  const problems = [];
  if (r.code !== 0) problems.push(`record.mjs exited ${r.code}; output: ${r.output.trim().split('\n').slice(-3).join(' | ')}`);
  const webms = fs.existsSync(out) ? fs.readdirSync(out).filter((f) => f.endsWith('.webm')) : [];
  if (!webms.length) problems.push('no webm was produced');
  if (!/RECORDED:/.test(r.output)) problems.push('record.mjs did not report RECORDED:');
  return problems;
});

fs.rmSync(tmp, { recursive: true, force: true });
const failed = results.filter((r) => r.failures.length);
console.log(`\n${results.length - failed.length}/${results.length} record-watchdog checks passed`);
if (failed.length) {
  console.error('FAILED: ' + failed.map((f) => f.name).join(', '));
  process.exit(1);
}
