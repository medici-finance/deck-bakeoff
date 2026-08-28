/**
 * Scene-duration contract (runtime half).
 *
 * `vite.config.ts` resolves the pipeline's measured narration lengths at config
 * time and freezes them into the bundle as `__PIPELINE_TIMING__`. This module
 * normalizes that payload, validates it against `SCENE_ORDER`, and exposes the
 * per-scene timing that `pipelineScene()` uses to stretch each scene to exactly
 * the length of its narration clip.
 *
 * The pipeline numbers this mirrors (see `pipeline/assemble_audio.py` and
 * `pipeline/gen_subs.py`):
 *
 *   LEAD_S = 0.35   silence before scene 1's narration
 *   GAP_S  = 0.15   silence after every scene except the last
 *   TAIL_S = 1.00   silence after the last scene
 *
 *   SCENE_DURATIONS[i] = raw_clip_i + (i is last ? TAIL_S : GAP_S)
 *
 * so LEAD_S is NOT part of any SCENE_DURATIONS entry, and
 *
 *   total audio = LEAD_S + sum(SCENE_DURATIONS)
 *
 * The rendered video must therefore be `leadIn + sum(durations)` long, with the
 * lead-in spent holding scene 1's opening frame. `pipelineScene()` does that.
 */
import {SCENE_ORDER, type SceneId} from './scene-order';

/** Matches `LEAD_S` in pipeline/assemble_audio.py and pipeline/gen_subs.py. */
export const DEFAULT_LEAD_IN = 0.35;

/** Frame rate used when the timing payload does not pin one. Must match render.mjs. */
export const DEFAULT_FPS = 30;

/**
 * Durations used when no scene-durations file is present — i.e. `npm run dev`
 * with no pipeline run behind it. Deliberately the brief's [4, 8, 4] so the
 * demo is watchable standalone.
 */
export const DEV_FALLBACK: readonly number[] = [4, 8, 4];

export interface SceneTiming {
  id: SceneId;
  index: number;
  /** Measured narration length + trailing gap/tail, in seconds. */
  duration: number;
  /** Seconds of static hold before the choreography starts (scene 0 only). */
  leadIn: number;
  /** Total wall time this Motion Canvas scene must occupy. */
  total: number;
}

export interface PipelineTiming {
  leadIn: number;
  fps: number;
  /** True when the durations came from a real pipeline run, false for DEV_FALLBACK. */
  measured: boolean;
  scenes: SceneTiming[];
}

interface RawSceneEntry {
  id?: string;
  duration?: number;
  seconds?: number;
}

interface RawTimingObject {
  leadIn?: number;
  lead_in?: number;
  fps?: number;
  scenes?: (RawSceneEntry | number)[];
  durations?: number[];
}

function entryDuration(entry: RawSceneEntry | number, at: number): number {
  const value = typeof entry === 'number' ? entry : (entry.duration ?? entry.seconds);
  if (typeof value !== 'number' || !Number.isFinite(value) || value <= 0) {
    throw new Error(
      `scene-durations: entry ${at} has no usable positive duration (got ${JSON.stringify(entry)})`,
    );
  }
  return value;
}

function normalize(raw: unknown): {leadIn: number; fps: number; measured: boolean; durations: number[]} {
  if (raw === null || raw === undefined) {
    return {
      leadIn: DEFAULT_LEAD_IN,
      fps: DEFAULT_FPS,
      measured: false,
      durations: [...DEV_FALLBACK],
    };
  }

  if (Array.isArray(raw)) {
    return {
      leadIn: DEFAULT_LEAD_IN,
      fps: DEFAULT_FPS,
      measured: true,
      durations: raw.map((entry, i) => entryDuration(entry as RawSceneEntry | number, i)),
    };
  }

  if (typeof raw !== 'object') {
    throw new Error(`scene-durations: expected an object or array, got ${typeof raw}`);
  }

  const obj = raw as RawTimingObject;
  const list = obj.scenes ?? obj.durations;
  if (!Array.isArray(list)) {
    throw new Error("scene-durations: object form needs a 'scenes' (or 'durations') array");
  }

  const durations = list.map((entry, i) => entryDuration(entry, i));

  // When ids are supplied, they are authoritative: reorder to SCENE_ORDER so a
  // reordered SCRIPT.md cannot silently shift narration onto the wrong picture.
  const ided = list.filter(
    (entry): entry is RawSceneEntry => typeof entry !== 'number' && typeof entry.id === 'string',
  );
  if (ided.length === list.length) {
    const byId = new Map(ided.map(entry => [entry.id as string, entry]));
    const missing = SCENE_ORDER.filter(id => !byId.has(id));
    const extra = ided.map(e => e.id as string).filter(id => !SCENE_ORDER.includes(id as SceneId));
    if (missing.length || extra.length) {
      throw new Error(
        `scene-durations: ids do not match src/scene-order.ts. ` +
          `missing=[${missing.join(', ')}] unexpected=[${extra.join(', ')}]`,
      );
    }
    return {
      leadIn: obj.leadIn ?? obj.lead_in ?? DEFAULT_LEAD_IN,
      fps: obj.fps ?? DEFAULT_FPS,
      measured: true,
      durations: SCENE_ORDER.map((id, i) => entryDuration(byId.get(id) as RawSceneEntry, i)),
    };
  }

  return {
    leadIn: obj.leadIn ?? obj.lead_in ?? DEFAULT_LEAD_IN,
    fps: obj.fps ?? DEFAULT_FPS,
    measured: true,
    durations,
  };
}

const RAW = normalize(typeof __PIPELINE_TIMING__ === 'undefined' ? null : __PIPELINE_TIMING__);

if (RAW.durations.length !== SCENE_ORDER.length) {
  throw new Error(
    `scene-durations: got ${RAW.durations.length} durations but src/scene-order.ts ` +
      `declares ${SCENE_ORDER.length} scenes ([${SCENE_ORDER.join(', ')}]). ` +
      'The SCRIPT.md row count and the registered scenes must agree.',
  );
}

/**
 * Quantize the scene boundaries to whole frames.
 *
 * A renderer can only end a scene on a frame boundary, so every scene's length
 * gets rounded. Rounding each duration independently lets the error ACCUMULATE:
 * twelve scenes rounded up is up to twelve frames of picture that the narration
 * never paid for, and by the closing card the words are visibly early.
 *
 * Instead, round the cumulative boundary — the absolute timestamp at which each
 * scene ends — and take each scene's frame budget as the difference between
 * consecutive rounded boundaries. Per-scene error stays under half a frame and
 * never compounds, and the total lands on `round(totalSeconds * fps)` exactly.
 */
function compute(fps: number): PipelineTiming {
  if (!Number.isFinite(fps) || fps <= 0) {
    throw new Error(`scene-durations: fps must be a positive number, got ${fps}`);
  }

  const scenes: SceneTiming[] = [];
  let seconds = RAW.leadIn;
  let previousFrame = 0;

  RAW.durations.forEach((duration, index) => {
    seconds += duration;
    const boundary = Math.round(seconds * fps);
    const total = (boundary - previousFrame) / fps;
    previousFrame = boundary;
    const leadIn = index === 0 ? RAW.leadIn : 0;
    scenes.push({
      id: SCENE_ORDER[index],
      index,
      duration: total - leadIn,
      leadIn,
      total,
    });
  });

  return {leadIn: RAW.leadIn, fps, measured: RAW.measured, scenes};
}

let active: PipelineTiming = compute(RAW.fps);

/**
 * Re-quantize for the fps the renderer is actually going to use. Call BEFORE
 * the render starts (see `src/render-entry.ts`); scenes read `sceneTiming()`
 * while their generators run.
 */
export function setRenderFps(fps: number): PipelineTiming {
  active = compute(fps);
  return active;
}

/** The active timing table. */
export function timing(): PipelineTiming {
  return active;
}

export function sceneTiming(id: SceneId): SceneTiming {
  const found = active.scenes.find(scene => scene.id === id);
  if (!found) {
    throw new Error(`unknown scene id '${id}' — add it to src/scene-order.ts`);
  }
  return found;
}

/** Total length of the rendered video, in seconds: leadIn + sum(durations). */
export function totalDuration(): number {
  return active.scenes.reduce((sum, scene) => sum + scene.total, 0);
}
