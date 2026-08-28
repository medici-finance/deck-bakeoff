/**
 * Brand module for explainer-video Motion Canvas scenes.
 *
 * Binding brand facts this encodes (see the product brand guides — Medici:
 * `option-index-tracker/docs/brand-guide.md`, Plumb: `reconciler/docs/brand.md`,
 * Assay: `assay-toolkit/docs/brand/brand.md`):
 *
 *   - ONE accent, #3366FF, used sparingly — never as a large field, never two
 *     accents competing in a frame.
 *   - Explainer surfaces are WHITE with the blue accent. `darkStage` exists for
 *     the occasional inverted card; it is the exception, not the default.
 *   - Motion is minimal and functional. NO spring, bounce, elastic or overshoot
 *     easing anywhere — see `ease` below.
 *   - Fintech-restrained: things fade, rise a little, and draw. They do not pop.
 */
import {Layout, Node, Rect, Txt} from '@motion-canvas/2d';
import type {View2D} from '@motion-canvas/2d';
import {
  all,
  createRef,
  easeInCubic,
  easeInOutCubic,
  easeInOutSine,
  easeOutCubic,
  easeOutQuad,
  linear,
  type Reference,
  type ThreadGenerator,
} from '@motion-canvas/core';

// ---------------------------------------------------------------------------
// Colour tokens
// ---------------------------------------------------------------------------

export const color = {
  /** The single accent. Sparing use only: rules, one keyword, one active edge. */
  accent: '#3366FF',
  /** Tinted accent for fills that must stay quiet behind text. */
  accentWash: '#EDF2FF',
  /** Accent at reduced weight, for a secondary stroke on a white surface. */
  accentMuted: '#7A99FF',

  surface: '#FFFFFF',
  surfaceSunken: '#F6F7F9',
  ink: '#0E1116',
  inkMuted: '#5B6573',
  hairline: '#DCE0E6',

  surfaceDark: '#0E1116',
  surfaceDarkRaised: '#171C24',
  inkDark: '#FFFFFF',
  inkMutedDark: '#9BA5B4',
  hairlineDark: '#2A313B',
} as const;

// ---------------------------------------------------------------------------
// Stage presets
// ---------------------------------------------------------------------------

export interface Stage {
  name: 'white' | 'dark';
  isDark: boolean;
  background: string;
  /** Raised/sunken surface for a card sitting on the background. */
  panel: string;
  ink: string;
  inkMuted: string;
  hairline: string;
  accent: string;
  /** Accent at reduced weight — a secondary stroke that must not shout. */
  accentMuted: string;
  /** Quiet accent fill, safe behind text. */
  accentWash: string;
}

/** The default. Explainer surfaces are white. */
export const whiteStage: Stage = {
  name: 'white',
  isDark: false,
  background: color.surface,
  panel: color.surfaceSunken,
  ink: color.ink,
  inkMuted: color.inkMuted,
  hairline: color.hairline,
  accent: color.accent,
  accentMuted: color.accentMuted,
  accentWash: color.accentWash,
};

/** The exception — an inverted card, used at most once per video. */
export const darkStage: Stage = {
  name: 'dark',
  isDark: true,
  background: color.surfaceDark,
  panel: color.surfaceDarkRaised,
  ink: color.inkDark,
  inkMuted: color.inkMutedDark,
  hairline: color.hairlineDark,
  accent: color.accent,
  accentMuted: color.accentMuted,
  accentWash: color.surfaceDarkRaised,
};

/** Paint a view with a stage's background. Call once at the top of a scene. */
export function applyStage(view: View2D, stage: Stage = whiteStage): Stage {
  view.fill(stage.background);
  return stage;
}

// ---------------------------------------------------------------------------
// Motion: easings and beats
// ---------------------------------------------------------------------------

/**
 * The sanctioned easing set.
 *
 * Motion Canvas ships `easeOutBack`, `easeOutElastic`, `easeOutBounce` and
 * `spring()`. NONE of them may be used here: overshoot reads as playful, and
 * the brand is restrained. This object is deliberately the only easing surface
 * scenes import, so a springy easing cannot arrive by autocomplete.
 */
export const ease = {
  /** Something arrives: fade + small rise. */
  enter: easeOutCubic,
  /** Something leaves. */
  exit: easeInCubic,
  /** Something already on screen moves or resizes. */
  move: easeInOutCubic,
  /** A stroke draws itself, a bar grows. */
  reveal: easeOutQuad,
  /** Pure opacity cross-fades. */
  fade: easeInOutSine,
  /** Constant rate — progress bars, sweeps, anything metronomic. */
  linear,
} as const;

/**
 * Names that must never appear in a scene. Kept as data so a reviewer can grep
 * for them (`grep -rE 'Back|Elastic|Bounce|spring' src/scenes/`).
 */
export const FORBIDDEN_EASINGS = [
  'easeInBack',
  'easeOutBack',
  'easeInOutBack',
  'easeInElastic',
  'easeOutElastic',
  'easeInOutElastic',
  'easeInBounce',
  'easeOutBounce',
  'easeInOutBounce',
  'spring',
] as const;

/**
 * Nominal beat lengths in seconds, used as the `t()` argument in scenes.
 * They describe proportion, not wall time — `pipelineScene()` scales them.
 */
export const beat = {
  /** A hairline appearing, a label switching. */
  snap: 0.18,
  /** A small element entering. */
  quick: 0.3,
  /** The default: a card entering, a box drawing. */
  base: 0.5,
  /** A long stroke travelling across the frame. */
  slow: 0.9,
  /** Dead air so the viewer can read what just landed. */
  hold: 1.2,
} as const;

/** Vertical travel for an "enter" — small on purpose. */
export const RISE = 24;

// ---------------------------------------------------------------------------
// Typography
// ---------------------------------------------------------------------------

/**
 * System stack. Scenes render in headless Chromium, which has no network
 * access to a webfont and no bundled brand font; a stack keeps the render
 * reproducible on the machine that runs it. See README "Limits" for the
 * cross-machine caveat.
 */
export const FONT =
  '"Inter", "Helvetica Neue", "Helvetica", "Arial", "Liberation Sans", sans-serif';
export const FONT_MONO = '"SF Mono", "Menlo", "DejaVu Sans Mono", "Consolas", monospace';

/** Type scale in px, authored against a 1920x1080 stage. */
export const type = {
  display: 104,
  title: 72,
  heading: 48,
  subtitle: 38,
  body: 32,
  label: 26,
  kicker: 22,
} as const;

export const weight = {
  regular: 400,
  medium: 500,
  semibold: 600,
} as const;

// ---------------------------------------------------------------------------
// Components
// ---------------------------------------------------------------------------

export interface TitleCardProps {
  /** Small tracked, uppercase line above the title. Accent-coloured. */
  kicker?: string;
  title: string;
  subtitle?: string;
  stage?: Stage;
  /** Centre position of the card on the stage. */
  x?: number;
  y?: number;
  /** Max text width before wrapping. */
  width?: number;
}

export interface CardHandle<T extends Node = Layout> {
  node: T;
  /** Fade + rise in. `seconds` is real time — pass `t(beat.base)`. */
  reveal(seconds: number): ThreadGenerator;
  /** Fade + settle out. */
  dismiss(seconds: number): ThreadGenerator;
}

/**
 * Centred title card: optional accent kicker, title, accent rule, subtitle.
 * Starts hidden (opacity 0, offset down by RISE) — call `reveal()`.
 */
export function TitleCard(props: TitleCardProps): CardHandle {
  const stage = props.stage ?? whiteStage;
  const root: Reference<Layout> = createRef<Layout>();
  const rule: Reference<Rect> = createRef<Rect>();
  const width = props.width ?? 1280;
  const baseY = props.y ?? 0;

  const node = (
    <Layout
      ref={root}
      layout
      direction="column"
      alignItems="center"
      gap={28}
      width={width}
      x={props.x ?? 0}
      y={baseY + RISE}
      opacity={0}
    >
      {props.kicker ? (
        <Txt
          text={props.kicker.toUpperCase()}
          fontFamily={FONT}
          fontSize={type.kicker}
          fontWeight={weight.semibold}
          letterSpacing={4}
          fill={stage.accent}
        />
      ) : null}
      <Txt
        text={props.title}
        fontFamily={FONT}
        fontSize={type.title}
        fontWeight={weight.semibold}
        fill={stage.ink}
        textAlign="center"
        textWrap
        width={width}
      />
      <Rect ref={rule} width={0} height={4} radius={2} fill={stage.accent} />
      {props.subtitle ? (
        <Txt
          text={props.subtitle}
          fontFamily={FONT}
          fontSize={type.subtitle}
          fontWeight={weight.regular}
          fill={stage.inkMuted}
          textAlign="center"
          textWrap
          width={width}
        />
      ) : null}
    </Layout>
  ) as Layout;

  return {
    node,
    *reveal(seconds: number) {
      yield* all(
        root().opacity(1, seconds, ease.enter),
        root().y(baseY, seconds, ease.enter),
      );
      yield* rule().width(96, seconds * 0.6, ease.reveal);
    },
    *dismiss(seconds: number) {
      yield* all(
        root().opacity(0, seconds, ease.exit),
        root().y(baseY - RISE * 0.5, seconds, ease.exit),
      );
    },
  };
}

export interface LowerThirdProps {
  title: string;
  subtitle?: string;
  stage?: Stage;
  /**
   * X of the component's LEFT edge (the root is left-anchored via `offsetX`),
   * so a long title grows rightwards instead of off the left of the stage.
   * Stage x runs -960..960; -820 leaves a 140px margin.
   */
  x?: number;
  /** Y of the vertical centre of the bar. */
  y?: number;
}

/**
 * Left-aligned lower third: a vertical accent bar, a title and an optional
 * caption. Starts hidden; the bar wipes down, then the text fades in.
 */
export function LowerThird(props: LowerThirdProps): CardHandle {
  const stage = props.stage ?? whiteStage;
  const root = createRef<Layout>();
  const bar = createRef<Rect>();
  const text = createRef<Layout>();
  const baseX = props.x ?? -820;
  const baseY = props.y ?? 300;
  const BAR_HEIGHT = 96;

  const node = (
    <Layout
      ref={root}
      layout
      direction="row"
      alignItems="center"
      gap={28}
      x={baseX}
      y={baseY}
      offsetX={-1}
      opacity={1}
    >
      <Rect ref={bar} width={5} height={0} radius={2.5} fill={stage.accent} />
      <Layout ref={text} layout direction="column" gap={10} opacity={0} y={RISE / 2}>
        <Txt
          text={props.title}
          fontFamily={FONT}
          fontSize={type.heading}
          fontWeight={weight.semibold}
          fill={stage.ink}
        />
        {props.subtitle ? (
          <Txt
            text={props.subtitle}
            fontFamily={FONT}
            fontSize={type.label}
            fontWeight={weight.regular}
            fill={stage.inkMuted}
          />
        ) : null}
      </Layout>
    </Layout>
  ) as Layout;

  return {
    node,
    *reveal(seconds: number) {
      yield* bar().height(BAR_HEIGHT, seconds * 0.45, ease.reveal);
      yield* all(
        text().opacity(1, seconds * 0.55, ease.enter),
        text().y(0, seconds * 0.55, ease.enter),
      );
    },
    *dismiss(seconds: number) {
      yield* all(
        root().opacity(0, seconds, ease.exit),
        text().y(-RISE / 2, seconds, ease.exit),
      );
    },
  };
}
