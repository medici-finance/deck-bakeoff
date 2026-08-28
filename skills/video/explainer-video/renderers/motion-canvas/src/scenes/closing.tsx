/**
 * Scene 3 — closing card.
 *
 * Nominal 4s. The last measured duration carries the pipeline's 1.0s TAIL_S,
 * so this scene deliberately ends on a still frame with nothing moving.
 *
 * Stays on `whiteStage`: the brand fact is that explainer surfaces are white.
 * `darkStage` is available in `brand.tsx` for a deliberate inverted card, but
 * the demo does not spend it.
 */
import {Rect, Txt, makeScene2D} from '@motion-canvas/2d';
import {createRef, waitFor} from '@motion-canvas/core';
import {
  FONT,
  TitleCard,
  applyStage,
  beat,
  ease,
  type as typeScale,
  weight,
  whiteStage,
} from '../brand';
import {pipelineScene} from '../pipeline-scene';

export default makeScene2D(
  pipelineScene('closing', 4, function* (view, t) {
    const stage = applyStage(view, whiteStage);

    const card = TitleCard({
      title: 'One render, byte-identical every time',
      subtitle: 'No wall-clock recorder in the loop',
      stage,
      y: -60,
    });
    view.add(card.node);

    // A hairline, not a second accent: the card's rule already spends the one
    // accent this frame is allowed.
    const footer = createRef<Txt>();
    const tick = createRef<Rect>();
    view.add(
      <>
        <Rect ref={tick} y={200} width={0} height={1} fill={stage.hairline} />
        <Txt
          ref={footer}
          y={280}
          text="tools/explainer-video/renderers/motion-canvas"
          fontFamily={FONT}
          fontSize={typeScale.label}
          fontWeight={weight.regular}
          fill={stage.inkMuted}
          opacity={0}
        />
      </>,
    );

    yield* card.reveal(t(beat.base));
    yield* tick().width(560, t(beat.quick), ease.reveal);
    yield* footer().opacity(1, t(beat.quick), ease.fade);
    yield* waitFor(t(beat.hold));
  }),
);
