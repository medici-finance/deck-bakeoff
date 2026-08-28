import {readFileSync, existsSync} from 'node:fs';
import {dirname, resolve} from 'node:path';
import {fileURLToPath} from 'node:url';
import motionCanvas from '@motion-canvas/vite-plugin';
import {defineConfig} from 'vite';

const HERE = dirname(fileURLToPath(import.meta.url));

// @motion-canvas/vite-plugin is published as CommonJS. Depending on how Vite
// loads this config (ESM vs the CJS fallback) the default import can arrive as
// the function itself or as `{default: fn}` — normalize both.
const motionCanvasPlugin = (
  typeof motionCanvas === 'function'
    ? motionCanvas
    : (motionCanvas as {default: typeof motionCanvas}).default
) as typeof motionCanvas;

/**
 * Scene-duration contract (build-time half).
 *
 * Motion Canvas scenes run in the browser, so they cannot read the pipeline's
 * measured narration lengths from the filesystem. This config resolves the
 * timing payload at config time and freezes it into the bundle as the global
 * `__PIPELINE_TIMING__`; `src/timing.ts` is the runtime half that reads it.
 *
 * Resolution order:
 *   1. $SCENE_DURATIONS_FILE  — path to a JSON file (what render.mjs passes)
 *   2. ./scene-durations.json — if present in this directory
 *   3. built-in fallback      — standalone dev, see src/timing.ts DEV_FALLBACK
 *
 * Accepted JSON shapes:
 *   {"leadIn": 0.35, "fps": 30, "scenes": [{"id": "title", "duration": 4.0}, ...]}
 *   [4.0, 8.0, 4.0]            (positional, mapped against src/scene-order.ts)
 */
function loadTiming(): unknown {
  const fromEnv = process.env.SCENE_DURATIONS_FILE;
  const candidates = [
    fromEnv ? resolve(fromEnv) : null,
    resolve(HERE, 'scene-durations.json'),
  ].filter((p): p is string => p !== null);

  for (const path of candidates) {
    if (!existsSync(path)) {
      if (path === fromEnv) {
        throw new Error(`SCENE_DURATIONS_FILE does not exist: ${path}`);
      }
      continue;
    }
    const parsed = JSON.parse(readFileSync(path, 'utf8'));
    // eslint-disable-next-line no-console
    console.log(`[motion-canvas] scene durations: ${path}`);
    return parsed;
  }
  // eslint-disable-next-line no-console
  console.log('[motion-canvas] scene durations: none found — using DEV_FALLBACK');
  return null;
}

export default defineConfig({
  plugins: [
    motionCanvasPlugin({
      project: './src/project.ts',
      output: process.env.MC_OUTPUT ?? './output',
    }),
  ],
  define: {
    __PIPELINE_TIMING__: JSON.stringify(loadTiming()),
  },
  server: {
    port: Number(process.env.MC_PORT ?? 9000),
    strictPort: true,
    host: '127.0.0.1',
  },
});
