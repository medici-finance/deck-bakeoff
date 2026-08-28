#!/usr/bin/env node
// verify-bundle.mjs — node-side checks for bundle.mjs (no browser needed).
//
// verify.mjs owns the runtime behaviour in a real Chromium; this file owns the
// build tool: scene composition from fragments, idempotency/--check, and the
// failure modes that must stay loud (missing dir, non-scene fragment, a second
// SCENE_DURATIONS assignment smuggled in via a fragment).
import { execFileSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const BUNDLE = path.join(HERE, 'bundle.mjs');

const results = [];
function check(name, fn) {
  try {
    const problems = fn() || [];
    results.push({ name, failures: problems });
  } catch (err) {
    results.push({ name, failures: ['threw: ' + (err.message || err).split('\n')[0]] });
  }
  const r = results[results.length - 1];
  console.log(`${r.failures.length ? 'FAIL' : 'ok  '}  ${name}`);
  for (const f of r.failures) console.log(`        ${f}`);
}

function run(args, cwd) {
  // Returns { code, output } — never throws on non-zero exit.
  try {
    const out = execFileSync(process.execPath, [BUNDLE, ...args], {
      cwd, encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'],
    });
    return { code: 0, output: out };
  } catch (err) {
    return { code: err.status == null ? 1 : err.status, output: `${err.stdout || ''}${err.stderr || ''}` };
  }
}

function fixtureDir() {
  return fs.mkdtempSync(path.join(os.tmpdir(), 'gsap-bundle-verify-'));
}

// A minimal host page: one compose block, one SCENE_DURATIONS assignment.
// No inline blocks, so the fixture does not depend on node_modules content.
const HOST = `<!doctype html><html><body>
  <div class="stage">
  <!-- gsap-explainer:compose scenes -->
  <!-- /gsap-explainer:compose -->
  </div>
<script>window.SCENE_DURATIONS = [];</script>
</body></html>
`;

check('compose assembles fragments sorted by filename', () => {
  const dir = fixtureDir();
  fs.mkdirSync(path.join(dir, 'scenes'));
  fs.writeFileSync(path.join(dir, 'scenes', '02-second.html'),
    '<section class="scene" data-scene="second"><h1 data-enter>Two</h1></section>\n');
  fs.writeFileSync(path.join(dir, 'scenes', '01-first.html'),
    '<section class="scene" data-scene="first" data-exit="push"><h1 data-enter>One</h1></section>\n');
  fs.writeFileSync(path.join(dir, 'page.html'), HOST);
  const out = [];
  const r = run(['page.html'], dir);
  if (r.code !== 0) out.push('bundle exited ' + r.code + ': ' + r.output.trim());
  const html = fs.readFileSync(path.join(dir, 'page.html'), 'utf8');
  const first = html.indexOf('data-scene="first"');
  const second = html.indexOf('data-scene="second"');
  if (first < 0 || second < 0) out.push('fragments were not composed into the page');
  if (first > second) out.push('fragments are out of filename order');
  if (!/GENERATED from scenes\/01-first\.html/.test(html)) out.push('no provenance comment on the fragment');
  if (!/data-exit="push"/.test(html)) out.push('fragment attributes did not survive composition');
  fs.rmSync(dir, { recursive: true, force: true });
  return out;
});

check('compose is idempotent and --check passes when fresh, fails when stale', () => {
  const dir = fixtureDir();
  fs.mkdirSync(path.join(dir, 'scenes'));
  const frag = path.join(dir, 'scenes', '01-a.html');
  fs.writeFileSync(frag, '<section data-scene="a"><h1 data-enter>A</h1></section>\n');
  fs.writeFileSync(path.join(dir, 'page.html'), HOST);
  const out = [];
  run(['page.html'], dir);
  const once = fs.readFileSync(path.join(dir, 'page.html'), 'utf8');
  run(['page.html'], dir);
  const twice = fs.readFileSync(path.join(dir, 'page.html'), 'utf8');
  if (once !== twice) out.push('second bundle run changed the file — compose is not idempotent');
  if (run(['--check', 'page.html'], dir).code !== 0) out.push('--check failed on a fresh artifact');
  fs.writeFileSync(frag, '<section data-scene="a"><h1 data-enter>A, edited</h1></section>\n');
  if (run(['--check', 'page.html'], dir).code === 0) out.push('--check passed on a STALE artifact after a fragment edit');
  fs.rmSync(dir, { recursive: true, force: true });
  return out;
});

check('a fragment with no data-scene is a build error naming the fragment', () => {
  const dir = fixtureDir();
  fs.mkdirSync(path.join(dir, 'scenes'));
  fs.writeFileSync(path.join(dir, 'scenes', '01-a.html'), '<div>not a scene</div>\n');
  fs.writeFileSync(path.join(dir, 'page.html'), HOST);
  const r = run(['page.html'], dir);
  const out = [];
  if (r.code === 0) out.push('bundle exited 0 on a scene-less fragment');
  if (!/scenes\/01-a\.html/.test(r.output)) out.push('error does not name the fragment: ' + r.output.trim());
  fs.rmSync(dir, { recursive: true, force: true });
  return out;
});

check('a missing compose dir is a build error', () => {
  const dir = fixtureDir();
  fs.writeFileSync(path.join(dir, 'page.html'), HOST);
  const r = run(['page.html'], dir);
  fs.rmSync(dir, { recursive: true, force: true });
  return r.code === 0 ? ['bundle exited 0 with no scenes/ dir'] : [];
});

check('a fragment smuggling a second SCENE_DURATIONS assignment is a build error', () => {
  const dir = fixtureDir();
  fs.mkdirSync(path.join(dir, 'scenes'));
  fs.writeFileSync(path.join(dir, 'scenes', '01-a.html'),
    '<section data-scene="a"><script>window.SCENE_DURATIONS = [9];</script></section>\n');
  fs.writeFileSync(path.join(dir, 'page.html'), HOST);
  const r = run(['page.html'], dir);
  fs.rmSync(dir, { recursive: true, force: true });
  const out = [];
  if (r.code === 0) out.push('bundle exited 0 with two SCENE_DURATIONS assignments in the composed output');
  if (!/SCENE_DURATIONS/.test(r.output)) out.push('error does not name the duplicate assignment: ' + r.output.trim());
  return out;
});

const failed = results.filter((r) => r.failures.length);
console.log(`\n${results.length - failed.length}/${results.length} bundle checks passed`);
if (failed.length) {
  console.error('FAILED: ' + failed.map((f) => f.name).join(', '));
  process.exit(1);
}
