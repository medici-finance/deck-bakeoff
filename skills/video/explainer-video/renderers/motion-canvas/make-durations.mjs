#!/usr/bin/env node
/**
 * make-durations.mjs — turn a pipeline run's measured durations into the JSON
 * this renderer consumes.
 *
 * `pipeline/assemble_audio.py` prints, on stdout:
 *
 *     RAW_DURATIONS [3.912, 9.204, 4.331]
 *     SCENE_DURATIONS [4.062, 9.354, 5.331]
 *     OUT /.../narration_full.wav
 *
 * This script scrapes the `SCENE_DURATIONS` line and pairs it with the scene
 * ids — either given explicitly or parsed out of the deck repo's `SCRIPT.md`
 * (the same `id` column `pipeline/lib.py` reads) — and writes
 * `scene-durations.json`.
 *
 * It reads the pipeline's OUTPUT. It does not import, patch or otherwise touch
 * anything under `pipeline/`.
 *
 * usage:
 *   explainer-video ... 2>&1 | tee run.log
 *   node make-durations.mjs --log run.log --script ../../../medici-decks/video/SCRIPT.md
 *
 *   # or pipe it, with explicit ids
 *   cat run.log | node make-durations.mjs --ids title,flow,closing
 */
import {readFileSync, writeFileSync} from 'node:fs';
import {resolve} from 'node:path';

const LEAD_IN = 0.35; // pipeline/assemble_audio.py LEAD_S

function parseArgs(argv) {
  const opts = {log: null, script: null, ids: null, out: 'scene-durations.json', fps: 30};
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    const next = () => {
      const value = argv[++i];
      if (value === undefined) throw new Error(`${arg} needs a value`);
      return value;
    };
    switch (arg) {
      case '--log': opts.log = resolve(next()); break;
      case '--script': opts.script = resolve(next()); break;
      case '--ids': opts.ids = next().split(',').map(s => s.trim()).filter(Boolean); break;
      case '--out': opts.out = resolve(next()); break;
      case '--fps': opts.fps = Number(next()); break;
      case '--lead-in': opts.leadIn = Number(next()); break;
      case '-h':
      case '--help':
        process.stdout.write(
          'usage: make-durations.mjs [--log run.log] [--script SCRIPT.md | --ids a,b,c]\n' +
            '                          [--out scene-durations.json] [--fps 30] [--lead-in 0.35]\n' +
            'Reads the pipeline log from --log or stdin.\n',
        );
        process.exit(0);
        break;
      default:
        throw new Error(`unknown argument: ${arg}`);
    }
  }
  return opts;
}

function readLog(path) {
  if (path) return readFileSync(path, 'utf8');
  try {
    return readFileSync(0, 'utf8');
  } catch {
    throw new Error('no --log given and nothing on stdin');
  }
}

function scrapeDurations(log) {
  // Last occurrence wins — a log may contain more than one run.
  const matches = [...log.matchAll(/^SCENE_DURATIONS\s+\[([^\]]*)\]/gm)];
  if (matches.length === 0) {
    throw new Error(
      "no 'SCENE_DURATIONS [...]' line in the log. Run the pipeline through " +
        '`assemble_audio` first (step 2 of explainer-video).',
    );
  }
  const durations = matches[matches.length - 1][1]
    .split(',')
    .map(s => Number(s.trim()))
    .filter(n => Number.isFinite(n));
  if (durations.length === 0) throw new Error('SCENE_DURATIONS line parsed to zero entries');
  return durations;
}

/**
 * Parse scene ids out of a SCRIPT.md scenes table. Mirrors the column matching
 * in pipeline/lib.py `parse_script` (case-insensitive substring on 'id' /
 * 'narration'), but only far enough to recover the ordered id list.
 */
function scrapeIds(scriptPath) {
  const lines = readFileSync(scriptPath, 'utf8').split(/\r?\n/);
  let idCol = null;
  let narrationCol = null;
  const ids = [];
  for (const line of lines) {
    if (!line.includes('|')) {
      if (idCol !== null && ids.length) break;
      continue;
    }
    const cells = line
      .trim()
      .replace(/^\|/, '')
      .replace(/\|$/, '')
      .split('|')
      .map(c => c.trim());
    if (cells.every(c => c.length > 0 && /^[-: ]+$/.test(c))) continue;
    if (idCol === null) {
      const lower = cells.map(c => c.toLowerCase());
      const i = lower.findIndex(h => h.includes('id'));
      const n = lower.findIndex(h => h.includes('narration'));
      if (i === -1 || n === -1) continue;
      idCol = i;
      narrationCol = n;
      continue;
    }
    const id = (cells[idCol] ?? '').replace(/\*\*/g, '').replace(/^["']|["']$/g, '').trim();
    const narration = (cells[narrationCol] ?? '').trim();
    if (id && narration) ids.push(id);
  }
  if (!ids.length) throw new Error(`no scene ids found in ${scriptPath}`);
  return ids;
}

function main() {
  const opts = parseArgs(process.argv.slice(2));
  const durations = scrapeDurations(readLog(opts.log));
  const ids = opts.ids ?? (opts.script ? scrapeIds(opts.script) : null);

  if (ids && ids.length !== durations.length) {
    throw new Error(
      `${ids.length} scene ids but ${durations.length} measured durations — ` +
        'the SCRIPT.md rows and the narration clips disagree.',
    );
  }

  const payload = {
    leadIn: opts.leadIn ?? LEAD_IN,
    fps: opts.fps,
    scenes: durations.map((duration, i) => (ids ? {id: ids[i], duration} : duration)),
  };

  writeFileSync(opts.out, JSON.stringify(payload, null, 2) + '\n');
  const total = opts.leadIn ?? LEAD_IN;
  console.error(
    `wrote ${opts.out}: ${durations.length} scenes, ` +
      `${(durations.reduce((a, b) => a + b, total)).toFixed(3)}s total ` +
      `(incl. ${payload.leadIn}s lead-in)`,
  );
  if (!ids) {
    console.error(
      'note: no ids (pass --script or --ids) — the durations will be matched ' +
        'positionally against src/scene-order.ts.',
    );
  }
}

try {
  main();
} catch (err) {
  console.error(`make-durations.mjs: ${err.message}`);
  process.exit(1);
}
