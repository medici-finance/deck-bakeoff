"""Manim-side of the pipeline↔renderer contract: `BrandScene`.

The arithmetic lives in `contract.py`, which imports nothing but the standard
library and is unit-tested without Manim (`tests/test_contract.py`). This module
adds the Manim-dependent parts: the `BrandScene` base class and the `render.sh`
`--scene-order` helper, and re-exports the pure API so existing imports
(`from pipeline_contract import BrandScene, load_contract, ...`) keep working.

Contract
--------
* One pipeline scene == one Manim `Scene` subclass, in the same order as the
  rows of the deck's `SCRIPT.md`, declared in the module's `SCENE_ORDER`.
* Each scene class declares `scene_index` (0-based) and `fallback_duration`.
* At render time the scene resolves its budget from the durations array. The
  whole storyboard is then *scaled* by `budget / fallback_duration`, so a scene
  authored against a 10s fallback still fits when the measured narration comes
  in at 11.4s — every beat stretches proportionally rather than the tail growing
  a dead pause. Beats go through `self.t()`.
* The FIRST scene additionally holds `contract.LEAD_IN_DEFAULT` (0.35s, the
  pipeline's `LEAD_S`) *before* its storyboard, because the narration WAV starts
  with that much silence and `encode.sh` muxes at a common t=0. `BrandScene`
  spends it automatically — see `__init_subclass__` — so no storyboard has to
  remember, and forgetting cannot silently desynchronise the whole video.
* `hold_to_end()` absorbs the rounding remainder so the rendered clip lands on
  the budget to within one frame. It runs automatically after `construct()`;
  calling it explicitly at the end of a storyboard (as the demo does) stays
  correct and is a no-op the second time.

See `contract.py`'s module docstring for the audio timeline this is derived
from, the accepted JSON shapes, and the durations-file lookup order.
"""

from __future__ import annotations

import functools
import sys
import warnings

from manim import Scene, config

import medici_brand as brand
from contract import (  # noqa: F401 — re-exported for existing importers
    DURATIONS_ENV,
    DURATIONS_FILENAME,
    LEAD_IN_DEFAULT,
    Contract,
    build_parser,
    durations_from_log,
    load_contract,
    resolve_budget,
    resolve_index,
    run,
    total_length,
    write_contract,
)


# --- the base scene ----------------------------------------------------------


class BrandScene(Scene):
    """A pipeline-timed, brand-styled Manim scene.

    Subclasses set `scene_index` and `fallback_duration`, then express every
    beat through `self.t(nominal_seconds)` so the storyboard scales to the
    measured narration.
    """

    #: 0-based position in the deck's SCRIPT.md scene table.
    scene_index: int = 0
    #: Storyboard length this scene was authored against, in seconds. Used both
    #: as the standalone-dev duration and as the scaling denominator.
    fallback_duration: float = 5.0

    def __init_subclass__(cls, **kwargs) -> None:
        """Wrap the subclass's `construct` so the lead-in hold and the tail hold
        happen whether or not the storyboard remembers them.

        The pipeline's 0.35s of lead silence is a property of the *contract*,
        not of any one storyboard, and a scene that forgets it renders a video
        that is 0.35s ahead of its own narration and subtitles from the first
        frame to the last — a defect that looks fine in the rendered clip and
        only shows up after the mux. Making it opt-out rather than opt-in is the
        difference between a wrong video and a loud one.
        """
        super().__init_subclass__(**kwargs)
        fn = cls.__dict__.get("construct")
        if fn is None or getattr(fn, "_brandscene_wrapped", False):
            return

        @functools.wraps(fn)
        def construct(self, *args, **kwargs):  # type: ignore[no-untyped-def]
            self.spend_lead_in()
            result = fn(self, *args, **kwargs)
            self.hold_to_end()
            return result

        construct._brandscene_wrapped = True  # type: ignore[attr-defined]
        cls.construct = construct  # type: ignore[assignment]

    def setup(self) -> None:
        super().setup()
        if self.fallback_duration <= 0:
            raise SystemExit(
                f"{type(self).__name__}: fallback_duration must be > 0 — it is the "
                "denominator every beat is scaled against."
            )
        self.budget, self.lead_in, provenance = resolve_budget(
            type(self).__name__, self.scene_index, self.fallback_duration,
            float(config.frame_rate),
        )
        #: Total length of the clip this scene must emit: the lead-in hold plus
        #: the narration window. `hold_to_end()` targets this, not `budget`.
        self.clip_length = self.lead_in + self.budget
        self.time_scale = self.budget / self.fallback_duration
        self._lead_spent = False
        self._held = False
        print(
            f"[contract] {type(self).__name__}: budget={self.budget:.3f}s "
            f"lead_in={self.lead_in:.3f}s clip={self.clip_length:.3f}s "
            f"scale={self.time_scale:.3f}x source={provenance}",
            file=sys.stderr,
        )

    # -- timing helpers --

    def quantize(self, seconds: float) -> float:
        """Snap a duration to a whole number of frames.

        Manim emits a whole number of frames per animation, so a `run_time` of
        0.5s at 15fps (7.5 frames) loses the half frame — and four such
        animations leave the clip a frame short of its budget, which the
        concatenated video pays for as creeping audio drift. Quantising every
        beat makes the clip land on the budget exactly.
        """
        fps = float(config.frame_rate)
        return max(1, int(seconds * fps + 0.5)) / fps

    def t(self, nominal_seconds: float) -> float:
        """Scale a storyboard beat to the measured narration, frame-quantised."""
        return self.quantize(nominal_seconds * self.time_scale)

    @property
    def elapsed(self) -> float:
        """Seconds of animation emitted so far."""
        t = getattr(self.renderer, "time", None)
        if t is None:  # pragma: no cover - renderer API drift
            warnings.warn("BrandScene: renderer exposes no .time; hold_to_end() is a no-op")
            return self.clip_length
        return float(t)

    def spend_lead_in(self) -> None:
        """Hold for the pipeline's lead silence before the storyboard starts.

        Called automatically at the top of `construct()`; idempotent, so a
        storyboard may also call it explicitly without paying twice.
        """
        if self._lead_spent:
            return
        self._lead_spent = True
        if self.lead_in > 0:
            self.wait(self.quantize(self.lead_in))

    def hold_to_end(self, min_hold: float = 0.0) -> None:
        """Wait out the remainder of the clip so it lands on the narration
        length to the frame. Over-run is a loud warning, never a silent
        truncation — a long scene desynchronises every scene after it, and
        `render.sh` fails the run on the resulting total-length mismatch."""
        frame = 1.0 / float(config.frame_rate)
        # The clip length itself is only realisable to the frame.
        remaining = self.quantize(self.clip_length) - self.elapsed
        if remaining > max(min_hold, frame / 2):
            self.wait(self.quantize(remaining))
        elif remaining < -frame and not self._held:
            warnings.warn(
                f"{type(self).__name__}: storyboard ran {abs(remaining):.3f}s OVER its "
                f"{self.clip_length:.3f}s clip budget — the concatenated video will drift "
                "out of sync with the narration. Shorten the beats or raise "
                "fallback_duration.",
                stacklevel=2,
            )
        self._held = True

    # -- convenience so scenes import one module --

    brand = brand


# --- scene-order helper (needs Manim: it imports the storyboard) -------------


def scene_order(module_path: str) -> list[str]:
    """Import a scenes module and return its declared SCENE_ORDER.

    `render.sh` calls this to learn which classes to render and in what order —
    the storyboard declares its order rather than the shell guessing it from
    class names, because scene N of the video must line up with narration
    clip N.
    """
    import importlib.util
    from pathlib import Path

    path = Path(module_path).resolve()
    sys.path.insert(0, str(path.parent.parent))
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    order = getattr(mod, "SCENE_ORDER", None)
    if not order:
        raise SystemExit(f"{path}: no SCENE_ORDER list — the renderer needs the scene order")
    return list(order)


def main() -> None:
    args = build_parser(prog="pipeline_contract.py").parse_args()
    if args.scene_order:
        print("\n".join(scene_order(args.scene_order)))
        return
    run(args)


if __name__ == "__main__":
    main()
