/**
 * The scene ids, in pipeline order.
 *
 * This list is the join key between three things that must agree:
 *   - the rows of the deck repo's `video/SCRIPT.md` (one row per scene, same order),
 *   - the entries of the pipeline's measured SCENE_DURATIONS,
 *   - the scenes registered in `src/project.ts`.
 *
 * It is a plain string array with no imports so both `timing.ts` and
 * `project.ts` can depend on it without a cycle. `timing.ts` validates the
 * counts at load and throws loudly on a mismatch — a silent off-by-one here
 * would desync narration from picture for the whole video.
 */
export const SCENE_ORDER = ['title', 'flow', 'closing'] as const;

export type SceneId = (typeof SCENE_ORDER)[number];
