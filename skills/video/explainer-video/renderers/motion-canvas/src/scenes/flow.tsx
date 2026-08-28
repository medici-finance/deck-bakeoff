/**
 * Scene 2 — animated 2D diagram.
 *
 * Nominal 8s. Three labelled boxes with flows between them: each box fades and
 * rises in, each connector draws itself left-to-right, then a return flow draws
 * beneath the row and the final box takes the single accent.
 *
 * This is the scene that exists to answer "is Motion Canvas worth it?" — the
 * same choreography in the HTML/CSS recorder path costs a hand-written keyframe
 * timeline plus a `stroke-dashoffset` hack for the draw-on.
 */
import {Layout, Line, Rect, Txt, makeScene2D} from '@motion-canvas/2d';
import type {Reference} from '@motion-canvas/core';
import {all, createRef, waitFor} from '@motion-canvas/core';
import {
  FONT,
  LowerThird,
  type Stage,
  applyStage,
  beat,
  ease,
  type as typeScale,
  weight,
  whiteStage,
} from '../brand';
import {pipelineScene} from '../pipeline-scene';

const BOX_W = 400;
const BOX_H = 180;
const ROW_Y = -30;
const COLS = [-620, 0, 620];

interface Box {
  node: Layout;
  rect: Reference<Rect>;
  root: Reference<Layout>;
}

function FlowBox(stage: Stage, x: number, label: string, caption: string): Box {
  const root = createRef<Layout>();
  const rect = createRef<Rect>();
  const node = (
    <Layout ref={root} x={x} y={ROW_Y + 18} opacity={0}>
      <Rect
        ref={rect}
        width={BOX_W}
        height={BOX_H}
        radius={10}
        fill={stage.isDark ? stage.panel : stage.background}
        stroke={stage.hairline}
        lineWidth={1.5}
        layout
        direction="column"
        justifyContent="center"
        alignItems="center"
        gap={12}
      >
        <Txt
          text={label}
          fontFamily={FONT}
          fontSize={typeScale.heading}
          fontWeight={weight.semibold}
          fill={stage.ink}
        />
        <Txt
          text={caption}
          fontFamily={FONT}
          fontSize={typeScale.label}
          fontWeight={weight.regular}
          fill={stage.inkMuted}
        />
      </Rect>
    </Layout>
  ) as Layout;
  return {node, rect, root};
}

function Connector(
  stage: Stage,
  points: [number, number][],
  ref: Reference<Line>,
  radius = 0,
) {
  return (
    <Line
      ref={ref}
      points={points}
      stroke={stage.hairline}
      lineWidth={3}
      radius={radius}
      endArrow
      arrowSize={13}
      end={0}
    />
  );
}

export default makeScene2D(
  pipelineScene('flow', 8, function* (view, t) {
    const stage = applyStage(view, whiteStage);

    const heading = LowerThird({
      title: 'How a scene reaches the encoder',
      subtitle: 'narration measured first, picture stretched to match',
      stage,
      x: -820,
      y: -380,
    });
    view.add(heading.node);

    const boxes = [
      FlowBox(stage, COLS[0], 'SCRIPT.md', 'one row per scene'),
      FlowBox(stage, COLS[1], 'Narration', 'measured, per scene'),
      FlowBox(stage, COLS[2], 'Render', 'scaled to fit'),
    ];
    boxes.forEach(box => view.add(box.node));

    const edgeR = BOX_W / 2;
    const a1 = createRef<Line>();
    const a2 = createRef<Line>();
    const back = createRef<Line>();
    view.add(
      <>
        {Connector(stage, [[COLS[0] + edgeR + 24, ROW_Y], [COLS[1] - edgeR - 24, ROW_Y]], a1)}
        {Connector(stage, [[COLS[1] + edgeR + 24, ROW_Y], [COLS[2] - edgeR - 24, ROW_Y]], a2)}
        {Connector(
          stage,
          [
            [COLS[2], ROW_Y + BOX_H / 2 + 24],
            [COLS[2], ROW_Y + 300],
            [COLS[0], ROW_Y + 300],
            [COLS[0], ROW_Y + BOX_H / 2 + 24],
          ],
          back,
          40,
        )}
      </>,
    );

    const caption = createRef<Txt>();
    view.add(
      <Txt
        ref={caption}
        y={ROW_Y + 390}
        text="drift is corrected once, at the source"
        fontFamily={FONT}
        fontSize={typeScale.label}
        fontWeight={weight.regular}
        fill={stage.inkMuted}
        opacity={0}
      />,
    );

    function* enter(box: Box) {
      yield* all(
        box.root().opacity(1, t(beat.quick), ease.enter),
        box.root().y(ROW_Y, t(beat.quick), ease.enter),
      );
    }

    yield* heading.reveal(t(beat.base));
    yield* enter(boxes[0]);
    yield* a1().end(1, t(beat.quick), ease.reveal);
    yield* enter(boxes[1]);
    yield* a2().end(1, t(beat.quick), ease.reveal);
    yield* enter(boxes[2]);
    yield* waitFor(t(beat.snap));

    // The single accent lands on the box the scene is about.
    yield* all(
      boxes[2].rect().stroke(stage.accent, t(beat.quick), ease.move),
      boxes[2].rect().lineWidth(3, t(beat.quick), ease.move),
      boxes[2].rect().fill(stage.accentWash, t(beat.quick), ease.move),
    );

    yield* all(
      back().end(1, t(beat.slow), ease.reveal),
      back().stroke(stage.accentMuted, t(beat.slow), ease.move),
    );
    yield* caption().opacity(1, t(beat.quick), ease.fade);
    yield* waitFor(t(beat.hold));
  }),
);
