/**
 * `pipelineScene()` — the scene-duration contract, enforced.
 *
 * One pipeline scene (one `SCRIPT.md` row, one narration clip) == one Motion
 * Canvas scene. The author choreographs against a *nominal* length; this
 * wrapper stretches that choreography so the scene occupies exactly the
 * measured narration length, and pads or warns if the body under/overruns.
 *
 *     export default makeScene2D(
 *       pipelineScene('title', 4, function* (view, t) {
 *         yield* card().opacity(1, t(0.6), ease.enter);
 *         yield* waitFor(t(2.2));
 *       }),
 *     );
 *
 * `t(x)` scales a nominal second into a real one (`x * measured / nominal`).
 * Every duration inside the body should go through `t()` — a raw `waitFor(2)`
 * does not stretch, so the scene's proportions drift as narration length
 * changes and the trailing pad silently absorbs the difference.
 */
import type {View2D} from '@motion-canvas/2d';
import type {ThreadGenerator} from '@motion-canvas/core';
import {useScene, useThread, waitFor} from '@motion-canvas/core';
import type {SceneId} from './scene-order';
import {sceneTiming} from './timing';

export interface Beat {
  /** Scale a nominal duration (seconds) into a real one. */
  (nominal: number): number;
  /** measured / nominal. 1.0 means the narration matched the authored length. */
  readonly scale: number;
  /** The measured narration length (excluding this scene's lead-in hold). */
  readonly measured: number;
  /** Seconds consumed so far, measured from the start of the scene. */
  elapsed(): number;
  /** Seconds left before the scene must end. Negative means overrun. */
  remaining(): number;
}

export type PipelineSceneBody = (view: View2D, t: Beat) => ThreadGenerator;

function warn(message: string): void {
  try {
    useScene().logger.warn(message);
  } catch {
    // Outside a scene context (unit test / import-time) — fall back to console.
    // eslint-disable-next-line no-console
    console.warn(message);
  }
}

export function pipelineScene(
  id: SceneId,
  nominalSeconds: number,
  body: PipelineSceneBody,
): (view: View2D) => ThreadGenerator {
  if (!(nominalSeconds > 0)) {
    throw new Error(`pipelineScene('${id}'): nominalSeconds must be > 0`);
  }

  return function* (view: View2D): ThreadGenerator {
    const timing = sceneTiming(id);
    const scale = timing.duration / nominalSeconds;
    const start = useThread().time();

    const t = ((nominal: number) => nominal * scale) as {
      (nominal: number): number;
      scale: number;
      measured: number;
      elapsed(): number;
      remaining(): number;
    };
    t.scale = scale;
    t.measured = timing.duration;
    t.elapsed = () => useThread().time() - start;
    t.remaining = () => timing.total - t.elapsed();

    // Scene 1 holds its opening frame through the audio's lead-in silence.
    if (timing.leadIn > 0) {
      yield* waitFor(timing.leadIn);
    }

    yield* body(view, t);

    const left = timing.total - (useThread().time() - start);
    if (left > 1e-6) {
      yield* waitFor(left);
    } else if (left < -1e-3) {
      warn(
        `scene '${id}' overran its measured slot by ${(-left).toFixed(3)}s ` +
          `(budget ${timing.total.toFixed(3)}s). Everything after it will drift ` +
          'against the narration — shorten the choreography or route more of it ' +
          'through t().',
      );
    }
  };
}
