"""Medici brand style module for the Manim renderer.

Manim's defaults are wrong for this house in three ways: the canvas is black,
the default text colour is white, and the default animation vocabulary leans on
bouncy rate functions. This module flips all three and exposes the small set of
primitives a scene is allowed to use.

Source of truth: `option-index-tracker/docs/brand-guide.md` (canonical brand
reference). The tokens below are transcribed from it, not invented:

  §2.4 light-surface palette   Ink #1A1D26, Ink Muted #5B6472, Ink Faint #8A93A3,
                               Rule #E4E7EC, Accent (Electric Blue) #3366FF
  §2.1/§2.3                    Gold #D4A843, Danger #FF4444, Success #00CC66
  §3.1/§3.4                    IBM Plex Sans (600 headings / 400 body, sentence
                               case, never all-caps display), IBM Plex Mono for data
  §7.2                         chart rules (2px series lines, no dots, dashed
                               reference lines, no title, legend only at 3+ series)
  §9.1                         "No spring animations. No bounce. No overshoot.
                               Springs feel playful. Fintech is not playful."

Explainer *video* surfaces are WHITE (a light document surface, §2.4 / §10.6),
not the dark app surface — so the light palette applies and the colour ratios
invert: white dominates, ink for text, Electric Blue as the one accent.
"""

from __future__ import annotations

import warnings

import manimpango
from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    Line,
    ManimColor,
    Text,
    VGroup,
    config,
)
from manim.utils.rate_functions import ease_out_cubic, linear, smooth

# --- Colour tokens -----------------------------------------------------------

PAGE = ManimColor("#FFFFFF")  # explainer surfaces are white (§2.4 light surface)
INK = ManimColor("#1A1D26")  # body + heading text; near-black, never pure #000
INK_MUTED = ManimColor("#5B6472")  # subtitles, standfirst, secondary text
INK_FAINT = ManimColor("#8A93A3")  # axis labels, fine print, footnotes
RULE = ManimColor("#E4E7EC")  # hairlines, grid lines, table borders
ACCENT = ManimColor("#3366FF")  # Electric Blue — the one accent, used sparingly

GOLD = ManimColor("#D4A843")  # §7.2 P Token series line
DANGER = ManimColor("#FF4444")  # §7.2 N Token series line
SUCCESS = ManimColor("#00CC66")

# Series roles, so scenes never hardcode a hex (§7.2).
P_SERIES = GOLD
N_SERIES = DANGER
SUM_SERIES = ACCENT

# --- Type -------------------------------------------------------------------

_SANS_STACK = ("IBM Plex Sans", "Helvetica Neue", "Helvetica", "Arial")
_MONO_STACK = ("IBM Plex Mono", "Menlo", "Monaco", "Courier New")

# Type scale (§3.3) expressed in Manim font_size units. Manim sizes are in
# "scene units * 100"-ish rather than px; these are the calibrated equivalents
# for a 1920x1080 frame and keep the guide's *ratios* (h1 : h2 : body ≈
# 48 : 30 : 14 → widened for video legibility, where 14px body is unreadable).
SIZE_H1 = 60
SIZE_H2 = 42
SIZE_H3 = 32
SIZE_BODY = 28
SIZE_LABEL = 22
SIZE_FINE = 18

_warned: set[str] = set()


def _resolve(stack: tuple[str, ...], kind: str) -> str:
    """Pick the first installed font in a stack; warn once if the brand face is
    missing. A silent fallback is the classic 'wrong fonts' failure (§3.1)."""
    available = set(manimpango.list_fonts())
    for name in stack:
        if name in available:
            if name != stack[0] and kind not in _warned:
                _warned.add(kind)
                warnings.warn(
                    f"medici_brand: {stack[0]} is not installed; falling back to "
                    f"{name!r} for {kind}. Output is OFF-BRAND typographically. "
                    "Install with: brew install --cask font-ibm-plex-sans font-ibm-plex-mono",
                    stacklevel=2,
                )
            return name
    if kind not in _warned:
        _warned.add(kind)
        warnings.warn(f"medici_brand: no font from {stack} installed; using Manim default.", stacklevel=2)
    return ""


def sans() -> str:
    return _resolve(_SANS_STACK, "sans")


def mono() -> str:
    return _resolve(_MONO_STACK, "mono")


# --- Motion ------------------------------------------------------------------
#
# §9.1: no springs, no bounce, no overshoot. Only these three rate functions are
# sanctioned. EASE for enter/exit and transforms, EASE_OUT for a move that
# settles, LINEAR for a value sweep (a parameter changing at a constant rate
# reads as measurement, not performance).

EASE = smooth  # sigmoid ease-in-out, no overshoot
EASE_OUT = ease_out_cubic
LINEAR = linear

#: Rate functions that overshoot, bounce, or reverse — banned by §9.1.
BANNED_RATE_FUNCS = frozenset(
    {
        "there_and_back",
        "there_and_back_with_pause",
        "wiggle",
        "running_start",
        "ease_in_back",
        "ease_out_back",
        "ease_in_out_back",
        "ease_in_bounce",
        "ease_out_bounce",
        "ease_in_out_bounce",
        "ease_in_elastic",
        "ease_out_elastic",
        "ease_in_out_elastic",
        "not_quite_there",
        "lingering",
    }
)


def assert_restrained(*rate_funcs) -> None:
    """Raise if any rate function is on the banned list. Call it at module
    import in a scenes file to keep a stray `there_and_back` from shipping."""
    for fn in rate_funcs:
        name = getattr(fn, "__name__", str(fn))
        if name in BANNED_RATE_FUNCS:
            raise ValueError(
                f"medici_brand: rate function {name!r} overshoots/bounces — banned by "
                "brand-guide §9.1 (no springs, no bounce, no overshoot)."
            )


# --- Canvas ------------------------------------------------------------------


def apply_brand() -> None:
    """Flip Manim's defaults to the brand: white canvas, ink text.

    Called at import time by this module so any scene that imports it inherits
    the canvas — Manim reads `config.background_color` when the Camera is
    constructed, i.e. at scene instantiation, so import-time is early enough.
    """
    config.background_color = PAGE


apply_brand()


# --- Text primitives ---------------------------------------------------------


def heading(text: str, size: float = SIZE_H1, color: ManimColor = INK) -> Text:
    """Sentence-case heading, SemiBold (§3.4 rule 1: never all-caps display)."""
    return Text(text, font=sans(), weight="SEMIBOLD", font_size=size, color=color)


def body(text: str, size: float = SIZE_BODY, color: ManimColor = INK) -> Text:
    """Body copy, Regular (§3.4 rule 2: never 600+ for body)."""
    return Text(text, font=sans(), weight="NORMAL", font_size=size, color=color)


def subtle(text: str, size: float = SIZE_BODY) -> Text:
    return body(text, size=size, color=INK_MUTED)


def data(text: str, size: float = SIZE_BODY, color: ManimColor = INK) -> Text:
    """Numeric / formula text in the mono face (§3.4 rule 3). Never italic (rule 4)."""
    return Text(text, font=mono(), weight="MEDIUM", font_size=size, color=color)


def eyebrow(text: str) -> Text:
    """Small tracked caps kicker — the one place caps are allowed (§3.3 label,
    ~0.1em tracking). Pango has no tracking knob through Manim's `Text`, so the
    tracking is applied as thin spaces between glyphs."""
    tracked = " ".join(text.upper())
    return Text(tracked, font=sans(), weight="SEMIBOLD", font_size=SIZE_LABEL, color=INK_FAINT)


def formula(text: str, colors: dict[str, ManimColor] | None = None,
            size: float = SIZE_H2) -> Text:
    """A formula as a single mono `Text`, with per-term colouring.

    Manim's LaTeX path (`MathTex`) renders Computer Modern — a serif, which
    breaks the single-family rule (§3.1) — and drags a whole TeX distribution
    into the setup cost. Formulas here are Pango text in the data face instead,
    coloured per term via Manim's `t2c` substring map:

        formula("S = P + N", {"P": P_SERIES, "N": N_SERIES})
        formula("S = min(S, K) + max(S - K, 0)", {"min(S, K)": P_SERIES})

    One `Text` keeps the typographic spacing and a common baseline (a VGroup of
    per-term mobjects aligns bounding boxes, so parentheses sink the terms
    around them). `TransformMatchingShapes` morphs one formula into the next
    glyph-by-glyph, which is the transform this renderer exists to do.
    """
    return Text(
        text,
        font=mono(),
        weight="MEDIUM",
        font_size=size,
        color=INK,
        t2c=dict(colors or {}),
    )


# --- Furniture ---------------------------------------------------------------


def accent_rule(width: float = 2.0, thickness: float = 5.0) -> Line:
    """The short Electric Blue rule that anchors a title card."""
    return Line(LEFT * width / 2, RIGHT * width / 2, color=ACCENT, stroke_width=thickness)


def title_card(title: str, subtitle: str | None = None, kicker: str | None = None) -> VGroup:
    """Centred title card: optional kicker, heading, accent rule, optional
    subtitle. Returns a VGroup laid out and centred; the caller animates it.

    Layout is left-aligned as a block and centred on the frame — a centred
    *block* of left-aligned text reads as published, fully-centred text reads
    as a slide template.
    """
    rows = VGroup()
    if kicker:
        rows.add(eyebrow(kicker))
    rows.add(heading(title, size=SIZE_H1))
    rule = accent_rule(width=2.2)
    rows.add(rule)
    if subtitle:
        rows.add(subtle(subtitle, size=SIZE_H3))
    rows.arrange(DOWN, buff=0.45, aligned_edge=LEFT)
    rows.move_to(ORIGIN)
    rows.title_rule = rule  # type: ignore[attr-defined]
    return rows


def lower_third(text: str, sub: str | None = None) -> VGroup:
    """Bottom-left caption block with a vertical accent rule — the standing
    label for whatever is on screen. Positioned in frame; the caller animates."""
    bar = Line(UP * 0.28, DOWN * 0.28, color=ACCENT, stroke_width=5)
    rows = VGroup(body(text, size=SIZE_H3))
    if sub:
        rows.add(subtle(sub, size=SIZE_LABEL))
    rows.arrange(DOWN, buff=0.16, aligned_edge=LEFT)
    bar.set_height(max(rows.height, 0.5))
    group = VGroup(bar, rows).arrange(RIGHT, buff=0.32, aligned_edge=UP)
    group.to_corner(DOWN + LEFT, buff=0.7)
    return group


# --- Chart styling (§7.2, adapted to the light surface) ----------------------

#: Kwargs for `manim.Axes` that match the chart rules: hairline axes, faint
#: labels, no decoration. Grid/axis colour is the light-surface Rule token
#: (#E4E7EC) rather than the dark-surface Surface Light (#1A1A1A).
AXIS_CONFIG = {
    "color": RULE,
    "stroke_width": 2,
    "include_ticks": False,
    "tip_width": 0.18,
    "tip_height": 0.18,
}

SERIES_STROKE = 5  # §7.2 "2px, no dots" at 1080p scene units
REFERENCE_STROKE = 3  # dashed reference lines (strike, spot)


def legend(entries: list[tuple[str, ManimColor, bool]]) -> VGroup:
    """A small series legend: `[(label, colour, dashed), ...]`.

    §7.2 allows a legend only at three or more series — with just P and N the
    pairing is self-explanatory. Each row is a short swatch line plus a mono
    label, left-aligned; the caller positions the group.
    """
    rows = VGroup()
    for label, color, dashed in entries:
        swatch = Line(ORIGIN, RIGHT * 0.55, color=color, stroke_width=SERIES_STROKE)
        if dashed:
            from manim import DashedVMobject  # local: keeps the import surface small

            swatch = DashedVMobject(swatch, num_dashes=4)
        rows.add(VGroup(swatch, data(label, size=SIZE_LABEL, color=color)).arrange(RIGHT, buff=0.22))
    rows.arrange(DOWN, buff=0.24, aligned_edge=LEFT)
    return rows


def axis_label(text: str) -> Text:
    return body(text, size=SIZE_LABEL, color=INK_FAINT)


def series_label(text: str, color: ManimColor) -> Text:
    return data(text, size=SIZE_H3, color=color)
