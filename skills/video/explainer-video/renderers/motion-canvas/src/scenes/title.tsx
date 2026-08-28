/**
 * Scene 1 — title card.
 *
 * Nominal 4s. `pipelineScene` spends the audio lead-in (0.35s) on this scene's
 * initial state — a bare white frame — so the first frame of motion coincides
 * with the first word of narration rather than preceding it.
 */
import {makeScene2D, Rect} from '@motion-canvas/2d';
import {createRef, waitFor} from '@motion-canvas/core';
import {TitleCard, applyStage, beat, ease, whiteStage} from '../brand';
import {pipelineScene} from '../pipeline-scene';

export default makeScene2D(
  pipelineScene('title', 4, function* (view, t) {
    const stage = applyStage(view, whiteStage);

    // A single hairline under the card — the only other mark on the frame.
    const hairline = createRef<Rect>();
    view.add(<Rect ref={hairline} y={260} width={0} height={1} fill={stage.hairline} />);

    const card = TitleCard({
      kicker: 'Explainer',
      title: 'Deterministic motion, measured to the narration',
      subtitle: 'A Motion Canvas render path for the explainer-video pipeline',
      stage,
      y: -20,
    });
    view.add(card.node);

    yield* card.reveal(t(beat.base));
    yield* hairline().width(1100, t(beat.slow), ease.reveal);
    yield* waitFor(t(beat.hold));
  }),
);
