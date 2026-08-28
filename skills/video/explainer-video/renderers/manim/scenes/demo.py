"""Demo storyboard — "the maths behind the P/N split".

Three scenes, matching a three-row `SCRIPT.md`:

  0  TitleCard    4s   title card
  1  SplitMaths  10s   S = P + N decomposing into the payoff identity, then the
                       two payoff curves drawn and *morphed* as the strike moves
  2  ClosingCard  4s   closing card

Scene 1 is the reason this adapter exists. Redrawing two piecewise payoff curves
and their sum, sixty times a second, off a single moving parameter, is three
lines of Manim and a genuinely awkward afternoon in HTML/GSAP.

Standalone dev (no pipeline run, uses the fallback durations):

    manim render -ql scenes/demo.py SplitMaths

Pipeline render (durations from the measured narration):

    MEDICI_SCENE_DURATIONS=/path/scene-durations.json ./render.sh
"""

from __future__ import annotations

import sys
from pathlib import Path

# The adapter root, so `import medici_brand` works however manim was invoked.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from manim import (  # noqa: E402
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    Axes,
    Create,
    DashedVMobject,
    FadeIn,
    Line,
    TransformMatchingShapes,
    ValueTracker,
    VGroup,
    Write,
    always_redraw,
)

import medici_brand as brand  # noqa: E402
from pipeline_contract import BrandScene  # noqa: E402

#: Storyboard order — `render.sh` reads this to know which classes to render and
#: in what order. One entry per SCRIPT.md row.
SCENE_ORDER = ["TitleCard", "SplitMaths", "ClosingCard"]

#: Durations used when no `scene-durations.json` is present (standalone dev).
#: These are also the scaling denominators — see pipeline_contract.
FALLBACK_DURATIONS = [4.0, 10.0, 4.0]

# Fail the import if a bouncy rate function ever creeps into this file.
brand.assert_restrained(brand.EASE, brand.EASE_OUT, brand.LINEAR)


class TitleCard(BrandScene):
    scene_index = 0
    fallback_duration = FALLBACK_DURATIONS[0]

    def construct(self) -> None:
        card = brand.title_card(
            title="The maths behind the P/N split",
            subtitle="Index exposure without liquidation risk",
            kicker="Medici",
        )
        rule = card.title_rule
        rule.save_state()
        rule.stretch_to_fit_width(0.01).align_to(card, LEFT)

        self.play(FadeIn(card[0], shift=UP * 0.15), run_time=self.t(0.5), rate_func=brand.EASE)
        self.play(FadeIn(card[1], shift=UP * 0.15), run_time=self.t(0.7), rate_func=brand.EASE)
        self.play(rule.animate.restore(), run_time=self.t(0.5), rate_func=brand.EASE_OUT)
        self.play(FadeIn(card[3]), run_time=self.t(0.6), rate_func=brand.EASE)
        self.hold_to_end()


class SplitMaths(BrandScene):
    """The differentiator scene: an equation transform driving a curve morph."""

    scene_index = 1
    fallback_duration = FALLBACK_DURATIONS[1]

    X_MAX = 8.0
    Y_MAX = 8.0
    K_START = 3.4
    K_END = 5.4

    def construct(self) -> None:
        # --- 1. the identity ------------------------------------------------
        identity = brand.formula(
            "S = P + N",
            {"P": brand.P_SERIES, "N": brand.N_SERIES},
            size=brand.SIZE_H1,
        )
        identity.move_to(ORIGIN)
        self.play(FadeIn(identity), run_time=self.t(0.6), rate_func=brand.EASE)
        self.wait(self.t(0.5))

        # --- 2. …becomes the payoff decomposition ---------------------------
        payoff = brand.formula(
            "S = min(S, K) + max(S - K, 0)",
            {"min(S, K)": brand.P_SERIES, "max(S - K, 0)": brand.N_SERIES},
            size=brand.SIZE_H2,
        )
        payoff.move_to(ORIGIN)
        self.play(
            TransformMatchingShapes(identity, payoff),
            run_time=self.t(1.1),
            rate_func=brand.EASE,
        )
        self.wait(self.t(0.4))
        self.play(
            payoff.animate.scale(0.8).to_edge(UP, buff=0.55),
            run_time=self.t(0.6),
            rate_func=brand.EASE_OUT,
        )

        # --- 3. the axes ----------------------------------------------------
        # Shifted right of centre so the lower-third caption has the bottom-left
        # corner to itself.
        axes = Axes(
            x_range=[0, self.X_MAX, 1],
            y_range=[0, self.Y_MAX, 1],
            x_length=7.4,
            y_length=4.0,
            axis_config=dict(brand.AXIS_CONFIG),
        ).shift(RIGHT * 2.15 + DOWN * 0.35)
        x_label = brand.axis_label("index price  S").next_to(axes.x_axis, DOWN, buff=0.25).align_to(axes, RIGHT)
        y_label = brand.axis_label("payoff").next_to(axes.y_axis, UP, buff=0.2)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label),
                  run_time=self.t(0.7), rate_func=brand.EASE)

        # --- 4. the two payoff curves, bound to a moving strike -------------
        k = ValueTracker(self.K_START)

        def p_payoff(s: float) -> float:
            return min(s, k.get_value())

        def n_payoff(s: float) -> float:
            return max(s - k.get_value(), 0.0)

        p_curve = always_redraw(
            lambda: axes.plot(p_payoff, color=brand.P_SERIES,
                              stroke_width=brand.SERIES_STROKE, use_smoothing=False)
        )
        n_curve = always_redraw(
            lambda: axes.plot(n_payoff, color=brand.N_SERIES,
                              stroke_width=brand.SERIES_STROKE, use_smoothing=False)
        )
        strike = always_redraw(
            lambda: DashedVMobject(
                Line(
                    axes.c2p(k.get_value(), 0),
                    axes.c2p(k.get_value(), self.Y_MAX),
                    color=brand.INK_FAINT,
                    stroke_width=brand.REFERENCE_STROKE,
                ),
                num_dashes=18,
            )
        )
        strike_label = always_redraw(
            lambda: brand.series_label("K", brand.INK_FAINT)
            .scale(0.8)
            .next_to(axes.c2p(k.get_value(), self.Y_MAX), UP, buff=0.12)
        )

        # Three series (P, N, and their sum) is where §7.2 allows a legend. It
        # sits in the empty upper-left block rather than riding the curves —
        # the curves move, and a label chasing a moving curve is exactly the
        # restless motion the brand rules out.
        key = brand.legend(
            [
                ("P  protected", brand.P_SERIES, False),
                ("N  amplified", brand.N_SERIES, False),
                ("P + N = S", brand.SUM_SERIES, True),
            ]
        )
        key.to_corner(UP + LEFT, buff=0.9).shift(DOWN * 0.9)

        self.play(Create(p_curve), FadeIn(strike), FadeIn(strike_label),
                  run_time=self.t(0.8), rate_func=brand.EASE)
        self.play(FadeIn(key[0]), run_time=self.t(0.25), rate_func=brand.EASE)
        self.play(Create(n_curve), run_time=self.t(0.7), rate_func=brand.EASE)
        self.play(FadeIn(key[1]), run_time=self.t(0.25), rate_func=brand.EASE)

        # --- 5. their sum is the index itself -------------------------------
        total = DashedVMobject(
            axes.plot(lambda s: s, color=brand.SUM_SERIES, stroke_width=brand.REFERENCE_STROKE),
            num_dashes=42,
        )
        caption = brand.lower_third("Move the strike. The sum holds.",
                                    "P + N = S at every price")
        self.play(Write(total), FadeIn(key[2]), run_time=self.t(0.7), rate_func=brand.EASE)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=self.t(0.4), rate_func=brand.EASE)

        # --- 6. move the strike; both curves morph, the sum does not ---------
        # One ValueTracker drives two piecewise curves, a reference line and its
        # label. This is the scene the adapter exists to make cheap.
        self.play(k.animate.set_value(self.K_END), run_time=self.t(2.2), rate_func=brand.LINEAR)
        self.hold_to_end()


class ClosingCard(BrandScene):
    scene_index = 2
    fallback_duration = FALLBACK_DURATIONS[2]

    def construct(self) -> None:
        equation = brand.formula(
            "P + N = 1",
            {"P": brand.P_SERIES, "N": brand.N_SERIES},
            size=brand.SIZE_H1,
        )
        line = brand.subtle("At every state, by construction.", size=brand.SIZE_H3)
        rule = brand.accent_rule(width=3.0)
        block = VGroup(equation, rule, line).arrange(DOWN, buff=0.5)
        block.move_to(ORIGIN)

        self.play(FadeIn(equation), run_time=self.t(0.7), rate_func=brand.EASE)
        self.play(Create(rule), run_time=self.t(0.4), rate_func=brand.EASE_OUT)
        self.play(FadeIn(line, shift=UP * 0.1), run_time=self.t(0.6), rate_func=brand.EASE)
        self.hold_to_end()
