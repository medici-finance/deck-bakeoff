import {makeProject} from '@motion-canvas/core';

import closing from './scenes/closing?scene';
import flow from './scenes/flow?scene';
import title from './scenes/title?scene';
import {SCENE_ORDER} from './scene-order';
import {timing, totalDuration} from './timing';

/**
 * Scene registration order MUST match `SCENE_ORDER`, which in turn matches the
 * row order of the deck repo's `video/SCRIPT.md`. The assertion below is cheap
 * insurance: a mismatch here plays the right animation under the wrong words.
 */
const scenes = [title, flow, closing];

if (scenes.length !== SCENE_ORDER.length) {
  throw new Error(
    `project.ts registers ${scenes.length} scenes but src/scene-order.ts ` +
      `declares ${SCENE_ORDER.length} ([${SCENE_ORDER.join(', ')}])`,
  );
}

// Surfaced in the editor console and in render.mjs's log scrape. Reported at
// the default fps; render.mjs re-quantizes via setRenderFps() before rendering.
const plan = timing();
// eslint-disable-next-line no-console
console.log(
  `[explainer] timing: ${plan.measured ? 'measured' : 'DEV_FALLBACK'} ` +
    `leadIn=${plan.leadIn}s fps=${plan.fps} ` +
    `scenes=[${plan.scenes.map(s => `${s.id}:${s.total.toFixed(3)}`).join(' ')}] ` +
    `total=${totalDuration().toFixed(3)}s`,
);

export default makeProject({
  scenes,
});
