"""Lifecycle tests for `BrandScene` against a stubbed Manim.

`pipeline_contract` imports Manim, which needs Python 3.12/3.13 plus cairo and
pango — so the class that actually spends the lead-in would otherwise be the one
piece of the fix with no test at all. Manim's `Scene` contract that `BrandScene`
depends on is small (a `setup()` hook, `wait(seconds)`, and a renderer exposing
elapsed `time`), so it is stubbed here and the real behaviour under test is
`BrandScene`'s own: that the lead-in is spent exactly once, before the
storyboard, and that the clip lands on its contracted length.

This does NOT prove `BrandScene` composes correctly with real Manim — see the
README's §What was actually rendered for what remains hand-verified.
"""

from __future__ import annotations

import sys
import tempfile
import types
import unittest
from pathlib import Path

ADAPTER = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ADAPTER))

import contract  # noqa: E402


# --- the stub, installed before `pipeline_contract` is imported --------------


class FakeRenderer:
    def __init__(self) -> None:
        self.time = 0.0


class FakeScene:
    """The slice of `manim.Scene` that `BrandScene` relies on."""

    def __init__(self) -> None:
        self.renderer = FakeRenderer()
        self.waits: list[float] = []

    def setup(self) -> None:  # manim calls this before construct()
        pass

    def wait(self, seconds: float = 1.0) -> None:
        self.waits.append(seconds)
        self.renderer.time += seconds

    def play(self, *_args, run_time: float = 1.0, **_kwargs) -> None:
        self.renderer.time += run_time


class FakeConfig:
    frame_rate = 30.0


def _install_stubs() -> None:
    manim = types.ModuleType("manim")
    manim.Scene = FakeScene
    manim.config = FakeConfig
    sys.modules.setdefault("manim", manim)

    # medici_brand pulls in manimpango and the real manim colour API; BrandScene
    # only re-exports it as an attribute, so a placeholder is enough.
    sys.modules.setdefault("medici_brand", types.ModuleType("medici_brand"))


_install_stubs()

import pipeline_contract  # noqa: E402


def durations_file(payload: str) -> Path:
    p = Path(tempfile.mkdtemp()) / "scene-durations.json"
    p.write_text(payload)
    return p


CONTRACT = '{"scene_durations": [4.0, 10.0, 4.0], "lead_in": 0.35, "fps": 30}'


class BrandSceneTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.path = durations_file(CONTRACT)
        self._orig = pipeline_contract.resolve_budget

        def patched(name, index, fallback, fps, c=None):
            return contract.resolve_budget(name, index, fallback, fps,
                                           contract.load_contract(self.path))

        pipeline_contract.resolve_budget = patched

    def tearDown(self) -> None:
        pipeline_contract.resolve_budget = self._orig

    def run_scene(self, cls):
        scene = cls()
        scene.setup()
        scene.construct()
        return scene


# --- storyboards ------------------------------------------------------------


class Explicit(pipeline_contract.BrandScene):
    """Ends with an explicit hold_to_end(), as the shipped demo does."""

    scene_index = 0
    fallback_duration = 4.0

    def construct(self) -> None:
        self.play(run_time=self.t(1.0))
        self.hold_to_end()


class Implicit(pipeline_contract.BrandScene):
    """No explicit hold — the wrapper must still land it on the budget."""

    scene_index = 0
    fallback_duration = 4.0

    def construct(self) -> None:
        self.play(run_time=self.t(1.0))


class SecondScene(pipeline_contract.BrandScene):
    scene_index = 1
    fallback_duration = 10.0

    def construct(self) -> None:
        self.play(run_time=self.t(2.0))


class Overrunning(pipeline_contract.BrandScene):
    scene_index = 0
    fallback_duration = 4.0

    def construct(self) -> None:
        self.play(run_time=99.0)


class TestLeadIn(BrandSceneTestCase):
    def test_first_scene_holds_the_lead_before_anything_else(self):
        scene = self.run_scene(Explicit)
        self.assertGreater(scene.lead_in, 0.0)
        # The very first thing the scene emitted is the lead-in hold.
        self.assertEqual(scene.waits[0], scene.quantize(scene.lead_in))

    def test_clip_lands_on_lead_plus_budget(self):
        for cls in (Explicit, Implicit):
            with self.subTest(cls=cls.__name__):
                scene = self.run_scene(cls)
                self.assertAlmostEqual(scene.renderer.time, 4.0 + 10.0 / 30.0, places=6)
                self.assertAlmostEqual(scene.renderer.time, scene.clip_length, places=6)

    def test_later_scenes_get_no_lead_in(self):
        scene = self.run_scene(SecondScene)
        self.assertEqual(scene.lead_in, 0.0)
        self.assertAlmostEqual(scene.renderer.time, 10.0, places=6)

    def test_lead_in_is_spent_once_even_if_called_explicitly(self):
        scene = SecondScene()
        scene.scene_index = 0
        scene.setup()
        scene.spend_lead_in()
        scene.spend_lead_in()
        scene.construct()
        self.assertAlmostEqual(scene.renderer.time, scene.clip_length, places=6)

    def test_storyboard_beats_scale_off_the_narration_window_not_the_lead(self):
        scene = self.run_scene(Implicit)
        # budget 4.0 / fallback 4.0 == 1x, so a nominal 1.0s beat stays 1.0s
        # even though the clip is 4.333s long.
        self.assertAlmostEqual(scene.time_scale, 1.0, places=6)
        self.assertAlmostEqual(scene.t(1.0), 1.0, places=6)

    def test_overrun_warns_once_and_does_not_truncate(self):
        with self.assertWarns(UserWarning) as cm:
            scene = self.run_scene(Overrunning)
        self.assertEqual(len(cm.warnings), 1)
        self.assertIn("OVER", str(cm.warnings[0].message))
        # Not truncated: the emitted time still reflects the full storyboard.
        self.assertGreater(scene.renderer.time, scene.clip_length)

    def test_wrapping_is_not_applied_twice_to_an_inherited_construct(self):
        class Child(Explicit):
            pass

        scene = self.run_scene(Child)
        self.assertAlmostEqual(scene.renderer.time, scene.clip_length, places=6)

    def test_wrapper_preserves_the_original_for_introspection(self):
        """Manim's caching hashes construct's source; wraps must stay followable."""
        self.assertTrue(hasattr(Explicit.construct, "__wrapped__"))
        self.assertEqual(Explicit.construct.__name__, "construct")

    def test_zero_fallback_duration_is_rejected(self):
        class Bad(pipeline_contract.BrandScene):
            scene_index = 0
            fallback_duration = 0.0

            def construct(self) -> None:
                pass

        with self.assertRaises(SystemExit):
            Bad().setup()


if __name__ == "__main__":
    unittest.main()
