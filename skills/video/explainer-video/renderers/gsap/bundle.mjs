#!/usr/bin/env node
// bundle.mjs — inline the GSAP runtime into an explainer HTML file, in place,
// and (optionally) compose the file's scenes from per-scene fragment files.
//
// The pipeline copies the slides to a work dir before recording
// (`RunContext.slides_rendered`), so relative <script src> references break.
// A deck's explainer.html must therefore be SELF-CONTAINED. This tool keeps
// that honest: author against the markers, run `bundle`, commit the result.
//
//   <!-- gsap-explainer:inline gsap -->
//   <script>/* replaced */</script>
//   <!-- /gsap-explainer:inline -->
//
// Sources: `gsap` (core), `drawsvg` (DrawSVGPlugin), `runtime` (gsap-explainer.js).
//
// Scene composition (opt-in): author each scene as its own fragment file and
// let the bundler assemble them, so scenes can be written, diffed, and
// reviewed in isolation while the COMMITTED artifact stays one self-contained
// page (decomposed at source, monolithic at artifact):
//
//   <!-- gsap-explainer:compose scenes -->
//   …generated: every scenes/*.html fragment, sorted by filename…
//   <!-- /gsap-explainer:compose -->
//
// The dir is resolved relative to the HTML file. Each fragment is exactly one
// scene — one element carrying data-scene — and fragment order (by filename,
// so prefix them 01-, 02-, …) must match the SCRIPT.md row order.
//
//   node bundle.mjs demo/demo.html [more.html ...]
//   node bundle.mjs --check demo/demo.html      # exit 1 if the file is stale
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));

const SOURCES = {
  gsap: path.join(HERE, 'node_modules', 'gsap', 'dist', 'gsap.min.js'),
  drawsvg: path.join(HERE, 'node_modules', 'gsap', 'dist', 'DrawSVGPlugin.min.js'),
  runtime: path.join(HERE, 'src', 'gsap-explainer.js'),
};

const BLOCK = /([ \t]*)<!--\s*gsap-explainer:inline\s+([a-zA-Z0-9_-]+)\s*-->[\s\S]*?<!--\s*\/gsap-explainer:inline\s*-->/g;
const COMPOSE = /([ \t]*)<!--\s*gsap-explainer:compose\s+([^\s>]+)\s*-->[\s\S]*?<!--\s*\/gsap-explainer:compose\s*-->/g;

// Byte-for-byte the pattern `inject_durations` (tools/explainer-video/explainer-video)
// substitutes, with `count=1`. It rewrites the FIRST match in the file — so a
// second occurrence ANYWHERE, including in a comment or a JS string, silently
// steals the injection and the slides render at their fallback timings.
// That failure is invisible until the finished video drifts off the voice-over,
// so it is a build error here rather than a README warning.
const INJECT_TARGET = /window\.SCENE_DURATIONS\s*=\s*\[[^\]]*\]\s*;?/g;

function assertOneInjectTarget(html, file) {
  const hits = html.match(INJECT_TARGET) || [];
  if (hits.length === 1) return;
  const detail = hits.map((h) => `    ${h.slice(0, 60)}`).join('\n');
  throw new Error(
    `${file}: found ${hits.length} \`window.SCENE_DURATIONS = [...]\` assignments; ` +
    `the pipeline needs exactly one (it rewrites the first match).\n${detail}`
  );
}

function readSource(name, file) {
  const src = SOURCES[name];
  if (!src) {
    throw new Error(`${file}: unknown inline source "${name}" (known: ${Object.keys(SOURCES).join(', ')})`);
  }
  if (!fs.existsSync(src)) {
    throw new Error(`${src} not found — run \`npm install\` in ${HERE} first.`);
  }
  // A literal </script> inside inlined JS would close the host tag early.
  return fs.readFileSync(src, 'utf8').replace(/<\/script/gi, '<\\/script');
}

/** Regenerate one compose block's body from its fragment dir. Deterministic:
 *  fragments are read fresh and sorted by filename, so re-running is
 *  idempotent and `--check` catches a stale artifact after a fragment edit. */
function composeScenes(dirRel, file, indent) {
  const dir = path.resolve(path.dirname(file), dirRel);
  if (!fs.existsSync(dir) || !fs.statSync(dir).isDirectory()) {
    throw new Error(`${file}: compose dir "${dirRel}" not found (resolved to ${dir})`);
  }
  const frags = fs.readdirSync(dir).filter((f) => f.endsWith('.html')).sort();
  if (!frags.length) {
    throw new Error(`${file}: compose dir "${dirRel}" contains no .html fragments`);
  }
  const parts = [];
  for (const name of frags) {
    const raw = fs.readFileSync(path.join(dir, name), 'utf8').replace(/\s+$/, '');
    if (!/data-scene\s*=/.test(raw)) {
      throw new Error(
        `${dirRel}/${name}: fragment has no data-scene element — every fragment is exactly one scene`);
    }
    parts.push(`${indent}<!-- GENERATED from ${dirRel}/${name} — edit the fragment, then re-run \`npm run bundle\` -->`);
    parts.push(raw.split('\n').map((l) => (l.trim() ? indent + l : '')).join('\n'));
  }
  return parts.join('\n');
}

function bundle(file) {
  const original = fs.readFileSync(file, 'utf8');
  let found = 0;
  // Compose first, then inline, so a fragment smuggling a second
  // SCENE_DURATIONS assignment is caught by the assertion on the final output.
  let out = original.replace(COMPOSE, (_m, indent, dirRel) => {
    found += 1;
    return [
      `${indent}<!-- gsap-explainer:compose ${dirRel} -->`,
      composeScenes(dirRel, file, indent),
      `${indent}<!-- /gsap-explainer:compose -->`,
    ].join('\n');
  });
  out = out.replace(BLOCK, (_m, indent, name) => {
    found += 1;
    const body = readSource(name, file);
    return [
      `${indent}<!-- gsap-explainer:inline ${name} -->`,
      `${indent}<script>${body}</script>`,
      `${indent}<!-- /gsap-explainer:inline -->`,
    ].join('\n');
  });
  if (!found) throw new Error(`${file}: no <!-- gsap-explainer:inline/compose … --> blocks found`);
  assertOneInjectTarget(out, file);
  return { original, out, found };
}

const args = process.argv.slice(2);
const check = args.includes('--check');
const files = args.filter((a) => a !== '--check');
if (!files.length) {
  console.error('usage: node bundle.mjs [--check] <html> [<html> ...]');
  process.exit(1);
}

let stale = 0;
for (const f of files) {
  const file = path.resolve(f);
  const { original, out, found } = bundle(file);
  if (check) {
    if (original !== out) {
      console.error(`STALE: ${f} — re-run \`npm run bundle\``);
      stale += 1;
    } else {
      console.log(`ok: ${f} (${found} block${found === 1 ? '' : 's'})`);
    }
  } else if (original === out) {
    console.log(`unchanged: ${f} (${found} block${found === 1 ? '' : 's'})`);
  } else {
    fs.writeFileSync(file, out);
    console.log(`inlined: ${f} (${found} block${found === 1 ? '' : 's'}, ${out.length} bytes)`);
  }
}
process.exit(stale ? 1 : 0);
