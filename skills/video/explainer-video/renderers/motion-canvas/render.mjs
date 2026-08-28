#!/usr/bin/env node
/**
 * render.mjs — headless Motion Canvas render for the explainer-video pipeline.
 *
 * Replaces `pipeline/record.mjs` for the VIDEO TRACK ONLY. Everything else in
 * the pipeline (gen_tts, assemble_audio, gen_subs, encode.sh) is untouched.
 *
 *   record.mjs   : Playwright records an HTML page in REAL TIME -> webm
 *   render.mjs   : Motion Canvas renders frame-by-frame, as fast as the machine
 *                  allows, with no wall clock in the loop -> PNG sequence -> mp4
 *
 * How it works
 *   1. Resolve the measured scene durations (a JSON file from the pipeline) and
 *      export them as $SCENE_DURATIONS_FILE, which `vite.config.ts` freezes into
 *      the bundle as `__PIPELINE_TIMING__`.
 *   2. Start a Vite DEV server in this process. Dev, not build: Motion Canvas's
 *      image exporter ships frames over Vite's HMR socket, and the vite-plugin
 *      writes them to disk. `import.meta.hot` only exists in dev.
 *   3. Open `render-entry.html` in headless Chromium and drive
 *      `@motion-canvas/core`'s `Renderer` directly (not the editor UI).
 *   4. Assemble the PNG sequence into a single video file with ffmpeg.
 *
 * Handoff to the pipeline
 *   The output file is a plain H.264 mp4 (or ProRes mov) at the requested fps,
 *   video only, no audio, no subtitles. It is handed to `pipeline/encode.sh` in
 *   the slot that used to hold the recorder's webm:
 *
 *     bash pipeline/encode.sh <this-output> <narration.wav> <subtitles.srt> <final.mp4>
 *
 *   encode.sh does not pass `-r`, so the final mp4 inherits this file's fps.
 *
 * usage:
 *   node render.mjs [--durations scene-durations.json] [--out out/video.mp4]
 *                   [--fps 30] [--width 1920] [--height 1080]
 *                   [--codec x264|prores] [--keep-frames] [--port 9000]
 */
import {spawn} from 'node:child_process';
import {existsSync, mkdirSync, readFileSync, readdirSync, rmSync} from 'node:fs';
import {dirname, resolve} from 'node:path';
import {fileURLToPath} from 'node:url';
import {chromium} from 'playwright';
import {createServer} from 'vite';

const HERE = dirname(fileURLToPath(import.meta.url));
const PROJECT_NAME = 'explainer';

function parseArgs(argv) {
  const opts = {
    durations: null,
    out: resolve(HERE, 'out', 'video.mp4'),
    fps: 30,
    width: 1920,
    height: 1080,
    codec: 'x264',
    fpsExplicit: false,
    keepFrames: false,
    port: 9000,
    timeoutMs: 15 * 60 * 1000,
  };
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    const next = () => {
      const value = argv[++i];
      if (value === undefined) throw new Error(`${arg} needs a value`);
      return value;
    };
    switch (arg) {
      case '--durations': opts.durations = resolve(next()); break;
      case '--out': opts.out = resolve(next()); break;
      case '--fps': opts.fps = Number(next()); opts.fpsExplicit = true; break;
      case '--width': opts.width = Number(next()); break;
      case '--height': opts.height = Number(next()); break;
      case '--codec': opts.codec = next(); break;
      case '--port': opts.port = Number(next()); break;
      case '--keep-frames': opts.keepFrames = true; break;
      case '--timeout': opts.timeoutMs = Number(next()) * 1000; break;
      case '-h':
      case '--help':
        process.stdout.write(readHelp());
        process.exit(0);
        break;
      default:
        throw new Error(`unknown argument: ${arg}`);
    }
  }
  if (!['x264', 'prores'].includes(opts.codec)) {
    throw new Error(`--codec must be x264 or prores, got '${opts.codec}'`);
  }
  if (!Number.isFinite(opts.fps) || opts.fps <= 0) {
    throw new Error(`--fps must be a positive number`);
  }
  return opts;
}

function readHelp() {
  return `render.mjs — headless Motion Canvas render

  --durations <file>  measured scene durations JSON from the pipeline
                      (default: ./scene-durations.json if present, else the
                      DEV_FALLBACK baked into src/timing.ts)
  --out <file>        output video (default ./out/video.mp4)
  --fps <n>           frame rate (default 30) — the final mp4 inherits this
  --width/--height    frame size (default 1920x1080)
  --codec x264|prores intermediate codec (default x264, CRF 10)
  --keep-frames       leave the PNG sequence in ./output/${PROJECT_NAME}/
  --port <n>          vite dev-server port (default 9000)
  --timeout <sec>     abort the render after this long (default 900)
`;
}

function run(cmd, args) {
  return new Promise((res, rej) => {
    const child = spawn(cmd, args, {stdio: ['ignore', 'inherit', 'inherit']});
    child.on('error', rej);
    child.on('close', code =>
      code === 0 ? res() : rej(new Error(`${cmd} exited with ${code}`)),
    );
  });
}

/** Like `run`, but returns the child's stdout. */
function capture(cmd, args) {
  return new Promise((res, rej) => {
    const child = spawn(cmd, args, {stdio: ['ignore', 'pipe', 'inherit']});
    let out = '';
    child.stdout.setEncoding('utf8');
    child.stdout.on('data', chunk => {
      out += chunk;
    });
    child.on('error', rej);
    child.on('close', code =>
      code === 0 ? res(out) : rej(new Error(`${cmd} exited with ${code}`)),
    );
  });
}

/**
 * ffmpeg's image2 demuxer walks `%06d.png` from `-start_number` and STOPS at the
 * first missing index — and still exits 0. A single dropped frame (the exporter
 * ships frames over the HMR socket, so a dropped write is a real failure mode)
 * would therefore produce a short video from a successful-looking run: the
 * frame count on disk still reads 492, ffmpeg reports success, and the truncated
 * file gets muxed against full-length narration.
 *
 * Verified: deleting frame 000250 of a 492-frame sequence yields `FFMPEG_EXIT=0`
 * and an 8.333s / 250-frame mp4. So the sequence is checked before encoding.
 */
function assertContiguous(frames, framesDir) {
  const numbers = frames.map(name => Number(name.replace('.png', '')));
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] !== numbers[i - 1] + 1) {
      const missing = numbers[i - 1] + 1;
      throw new Error(
        `PNG sequence in ${framesDir} has a gap: frame ${String(missing).padStart(6, '0')} ` +
          `is missing (jumps ${frames[i - 1]} -> ${frames[i]}, ${frames.length} files on disk). ` +
          "ffmpeg would stop at the gap and still exit 0, shipping a silently truncated video.",
      );
    }
  }
}

/** Frames actually present in an encoded file, or null if ffprobe cannot say. */
async function encodedFrameCount(file) {
  const out = await capture('ffprobe', [
    '-v', 'error',
    '-count_frames',
    '-select_streams', 'v:0',
    '-show_entries', 'stream=nb_read_frames',
    '-of', 'default=nw=1:nk=1',
    file,
  ]);
  const count = Number(out.trim());
  return Number.isFinite(count) && count > 0 ? count : null;
}

async function main() {
  const opts = parseArgs(process.argv.slice(2));

  const framesDir = resolve(HERE, 'output', PROJECT_NAME);
  rmSync(framesDir, {recursive: true, force: true});
  mkdirSync(dirname(opts.out), {recursive: true});

  if (opts.durations) {
    if (!existsSync(opts.durations)) {
      throw new Error(`--durations file not found: ${opts.durations}`);
    }
    process.env.SCENE_DURATIONS_FILE = opts.durations;
    // The durations file may pin an fps; an explicit --fps still wins.
    if (!opts.fpsExplicit) {
      const pinned = JSON.parse(readFileSync(opts.durations, 'utf8'))?.fps;
      if (typeof pinned === 'number' && pinned > 0) {
        opts.fps = pinned;
        console.error(`[render] fps ${pinned} taken from ${opts.durations}`);
      }
    }
  }
  process.env.MC_OUTPUT = resolve(HERE, 'output');
  process.env.MC_PORT = String(opts.port);

  console.error(`[render] starting vite dev server on 127.0.0.1:${opts.port} ...`);
  const server = await createServer({
    root: HERE,
    configFile: resolve(HERE, 'vite.config.ts'),
    logLevel: 'warn',
    server: {port: opts.port, strictPort: true, host: '127.0.0.1'},
  });
  await server.listen();

  const browser = await chromium.launch({
    args: [
      // Deterministic text/vector rasterization: no GPU in the loop.
      '--disable-gpu',
      '--force-color-profile=srgb',
      '--disable-lcd-text',
      '--font-render-hinting=none',
      '--hide-scrollbars',
    ],
  });

  let report;
  try {
    const context = await browser.newContext({
      viewport: {width: 1280, height: 720},
      deviceScaleFactor: 1,
    });
    const page = await context.newPage();
    // The scene-duration contract throws at module scope on a bad payload, so a
    // page exception is a hard failure — surface it instead of waiting out the
    // readiness timeout.
    let firstPageError = null;
    page.on('console', msg => {
      const text = msg.text();
      if (text.startsWith('[motion-canvas]') || text.startsWith('[explainer]')) {
        console.error(`  ${text}`);
      } else if (msg.type() === 'error') {
        console.error(`  page error: ${text}`);
      }
    });
    page.on('pageerror', err => {
      firstPageError ??= err;
      console.error(`  page exception: ${err.message}`);
    });

    await page.goto(`http://127.0.0.1:${opts.port}/render-entry.html`, {
      waitUntil: 'domcontentloaded',
    });

    const readyBy = Date.now() + 60_000;
    for (;;) {
      if (firstPageError) {
        throw new Error(`render entry failed to load: ${firstPageError.message}`);
      }
      if (await page.evaluate(() => window.__mc?.ready === true)) break;
      if (Date.now() > readyBy) {
        throw new Error('timed out waiting for the render entry to become ready');
      }
      await page.waitForTimeout(100);
    }

    const plan = await page.evaluate(fps => window.__mc.plan(fps), opts.fps);
    const expectedSeconds = plan.scenes.reduce((sum, scene) => sum + scene.total, 0);
    console.error(
      `[render] timing source: ${plan.measured ? 'measured (pipeline)' : 'DEV_FALLBACK'}; ` +
        `expected ${expectedSeconds.toFixed(3)}s ` +
        `[${plan.scenes.map(s => `${s.id}:${s.total.toFixed(3)}`).join(' ')}]`,
    );

    console.error(`[render] rendering ${opts.width}x${opts.height} @ ${opts.fps}fps ...`);
    let watchdog;
    const timeout = new Promise((_, reject) => {
      watchdog = setTimeout(
        () => reject(new Error(`render exceeded --timeout (${opts.timeoutMs / 1000}s)`)),
        opts.timeoutMs,
      );
    });
    try {
      report = await Promise.race([
        page.evaluate(request => window.__mc.render(request), {
          fps: opts.fps,
          width: opts.width,
          height: opts.height,
          name: PROJECT_NAME,
        }),
        timeout,
      ]);
    } finally {
      clearTimeout(watchdog);
    }
  } finally {
    await browser.close();
    await server.close();
  }

  for (const entry of report.logs) {
    console.error(`  [${entry.level}] ${entry.message}`);
  }
  if (report.result !== 'success') {
    throw new Error(`render finished with result '${report.result}' — see log above`);
  }

  const frames = existsSync(framesDir)
    ? readdirSync(framesDir).filter(f => f.endsWith('.png')).sort()
    : [];
  if (frames.length === 0) {
    throw new Error(`no PNG frames were written to ${framesDir}`);
  }
  assertContiguous(frames, framesDir);

  const expectedFrames = Math.round(report.expectedSeconds * opts.fps);
  const drift = frames.length - expectedFrames;
  console.error(
    `[render] ${frames.length} frames on disk (expected ~${expectedFrames}, drift ${drift >= 0 ? '+' : ''}${drift})`,
  );
  // One frame of slack each way is rounding on the scene boundaries; more than
  // that means picture and narration will visibly separate.
  if (Math.abs(drift) > 2) {
    console.error(
      `[render] WARNING: frame count is ${drift} off the measured narration length. ` +
        'Audio and picture will drift — check for a scene that overran its slot.',
    );
  }

  const codecArgs =
    opts.codec === 'prores'
      ? ['-c:v', 'prores_ks', '-profile:v', '3', '-pix_fmt', 'yuv422p10le']
      : ['-c:v', 'libx264', '-crf', '10', '-preset', 'veryfast', '-pix_fmt', 'yuv420p'];

  console.error(`[render] assembling ${opts.codec} -> ${opts.out}`);
  await run('ffmpeg', [
    '-y',
    '-framerate', String(opts.fps),
    '-start_number', frames[0].replace('.png', ''),
    '-i', resolve(framesDir, '%06d.png'),
    ...codecArgs,
    '-r', String(opts.fps),
    '-movflags', '+faststart',
    opts.out,
  ]);

  // Never report success on a file we have not counted. The contiguity check
  // above covers the known truncation path; this one is the belt-and-braces
  // assertion on the artefact that actually leaves this script, so no encoder
  // fault can reach `encode.sh` behind a green exit code.
  const encoded = await encodedFrameCount(opts.out);
  if (encoded === null) {
    throw new Error(`could not read a frame count back from ${opts.out} — refusing to report success`);
  }
  if (encoded !== frames.length) {
    throw new Error(
      `${opts.out} holds ${encoded} frames but ${frames.length} PNGs were rendered ` +
        `(${((frames.length - encoded) / opts.fps).toFixed(3)}s missing). ` +
        'The video would run short against its narration — refusing to report success.',
    );
  }

  if (!opts.keepFrames) {
    rmSync(framesDir, {recursive: true, force: true});
  }

  console.error('');
  console.error(`RENDERED: ${opts.out}`);
  console.error(`  fps=${opts.fps} size=${opts.width}x${opts.height} frames=${encoded} (verified in the file)`);
  console.error(`  duration=${(encoded / opts.fps).toFixed(3)}s (video only, no audio)`);
  console.error('');
  console.error('Hand to the pipeline encoder:');
  console.error(`  bash ../../pipeline/encode.sh ${opts.out} <narration.wav> <subtitles.srt> <final.mp4>`);
}

main().catch(err => {
  console.error(`render.mjs: ${err.message}`);
  process.exit(1);
});
