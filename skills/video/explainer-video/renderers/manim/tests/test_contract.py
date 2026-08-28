"""Unit tests for the Manim adapter's pipeline timing contract.

Stdlib only, by design. Manim needs Python 3.12/3.13, cairo, pango and ffmpeg;
gating the arithmetic on that install means the arithmetic is never checked in
CI, and the arithmetic is the part that has to be right — a frame-budget bug
produces a video that plays perfectly and drifts against its own narration.

Run:  python3 -m unittest discover -s tools/explainer-video/renderers/manim/tests
"""

from __future__ import annotations

import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

ADAPTER = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ADAPTER))

import contract  # noqa: E402


class ContractTestCase(unittest.TestCase):
    def write(self, payload, name: str = "scene-durations.json") -> Path:
        d = Path(tempfile.mkdtemp())
        p = d / name
        p.write_text(payload if isinstance(payload, str) else json.dumps(payload))
        return p

    def load(self, payload) -> contract.Contract:
        return contract.load_contract(self.write(payload))


class TestPipelineConstants(ContractTestCase):
    """The lead-in is a copy of a pipeline constant; copies drift."""

    def test_lead_in_matches_assemble_audio(self):
        src = (ADAPTER.parent.parent / "pipeline" / "assemble_audio.py").read_text()
        self.assertIn(
            f"LEAD_S = {contract.LEAD_IN_DEFAULT}", src,
            "contract.LEAD_IN_DEFAULT no longer matches pipeline/assemble_audio.py LEAD_S — "
            "every rendered video would be out of sync with its narration by the difference",
        )

    def test_lead_in_matches_gen_subs(self):
        src = (ADAPTER.parent.parent / "pipeline" / "gen_subs.py").read_text()
        self.assertIn(f"LEAD_S = {contract.LEAD_IN_DEFAULT}", src)

    def test_positive_control_for_the_greps_above(self):
        """If the constant were 0.0 the assertions above must fail, not pass."""
        src = (ADAPTER.parent.parent / "pipeline" / "assemble_audio.py").read_text()
        self.assertNotIn("LEAD_S = 0.0", src)


class TestLoading(ContractTestCase):
    def test_bare_array(self):
        c = self.load([4.0, 10.0, 4.0])
        self.assertEqual(c.durations, [4.0, 10.0, 4.0])
        self.assertIsNone(c.scenes)
        self.assertEqual(c.lead_in, contract.LEAD_IN_DEFAULT)

    def test_object_form(self):
        c = self.load({"scene_durations": [4.0, 10.0], "scenes": ["A", "B"], "fps": 30})
        self.assertEqual(c.scenes, ["A", "B"])
        self.assertEqual(c.fps, 30.0)
        self.assertEqual(c.lead_in, contract.LEAD_IN_DEFAULT)

    def test_explicit_zero_lead_in_is_honoured(self):
        c = self.load({"scene_durations": [4.0], "lead_in": 0})
        self.assertEqual(c.lead_in, 0.0)

    def test_camel_case_lead_in_accepted(self):
        c = self.load({"scene_durations": [4.0], "leadIn": 0.5})
        self.assertEqual(c.lead_in, 0.5)

    def test_missing_file_is_empty_not_an_error(self):
        os.environ.pop(contract.DURATIONS_ENV, None)
        c = contract.load_contract(Path(tempfile.mkdtemp()) / "nope.json")
        self.assertFalse(c)

    def test_object_without_durations_key_fails_loudly(self):
        with self.assertRaises(SystemExit) as cm:
            self.load({"scenes": [{"id": "title", "duration": 5.9}], "leadIn": 0.35})
        self.assertIn("scene_durations", str(cm.exception))

    def test_motion_canvas_scenes_shape_is_rejected(self):
        """The sibling adapter's file uses the same key for a different type."""
        with self.assertRaises(SystemExit) as cm:
            self.load({"scene_durations": [5.9], "scenes": [{"id": "title"}]})
        self.assertIn("class NAMES", str(cm.exception))

    def test_scenes_length_mismatch_fails(self):
        with self.assertRaises(SystemExit):
            self.load({"scene_durations": [4.0, 10.0], "scenes": ["A"]})

    def test_non_positive_duration_fails(self):
        for bad in ([0.0], [-1.0], ["x"], [None]):
            with self.subTest(bad=bad), self.assertRaises(SystemExit):
                self.load(bad)

    def test_invalid_json_fails_loudly(self):
        with self.assertRaises(SystemExit) as cm:
            self.load("{not json")
        self.assertIn("not valid JSON", str(cm.exception))

    def test_negative_lead_in_fails(self):
        with self.assertRaises(SystemExit):
            self.load({"scene_durations": [4.0], "lead_in": -0.1})


class TestBudgets(ContractTestCase):
    FPS = 30.0

    def budgets(self, c: contract.Contract, names: list[str]):
        return [contract.resolve_budget(n, i, 5.0, self.FPS, c) for i, n in enumerate(names)]

    def test_first_scene_carries_the_lead_in(self):
        c = self.load([4.0, 10.0, 4.0])
        (b0, l0, _), (b1, l1, _), (b2, l2, _) = self.budgets(c, ["A", "B", "C"])
        # 0.35s is 10.5 frames at 30fps, so the hold quantises to 10 frames.
        # What must hold is that it is within half a frame of LEAD_S and is a
        # whole number of frames — not that it equals 0.35 exactly.
        self.assertAlmostEqual(l0, 0.35, delta=0.5 / self.FPS)
        self.assertEqual(l0 * self.FPS, round(l0 * self.FPS))
        self.assertGreater(l0, 0.0)
        self.assertEqual(l1, 0.0)
        self.assertEqual(l2, 0.0)
        self.assertAlmostEqual(b0, 4.0, places=6)
        self.assertAlmostEqual(b1, 10.0, places=6)
        self.assertAlmostEqual(b2, 4.0, places=6)

    def test_clips_tile_the_full_narration_without_gap_or_overlap(self):
        durations = [3.412, 11.874, 4.905]
        c = self.load(durations)
        clips = [lead + budget for budget, lead, _ in self.budgets(c, ["A", "B", "C"])]
        total = sum(clips)
        expected = contract.total_length(self.FPS, c)
        self.assertAlmostEqual(total, expected, places=9)
        # …and the contract's total is the narration plus the lead-in, to within
        # half a frame (inclusive — an x.5-frame boundary hits the bound exactly).
        self.assertLessEqual(abs(expected - (0.35 + sum(durations))), 0.5 / self.FPS + 1e-9)

    def test_total_error_stays_under_half_a_frame_for_many_scenes(self):
        """Cumulative boundaries, not per-scene rounding: residue must not stack."""
        durations = [1.0 / 7.0] * 40  # deliberately unrepresentable at 30fps
        c = self.load(durations)
        names = [f"S{i}" for i in range(len(durations))]
        clips = [lead + budget for budget, lead, _ in self.budgets(c, names)]
        self.assertLessEqual(abs(sum(clips) - (0.35 + sum(durations))), 0.5 / self.FPS + 1e-9)

    def test_every_boundary_is_a_whole_number_of_frames(self):
        c = self.load([3.412, 11.874, 4.905])
        for budget, lead, _ in self.budgets(c, ["A", "B", "C"]):
            for value in (budget, lead):
                frames = value * self.FPS
                self.assertAlmostEqual(frames, round(frames), places=6)

    def test_zero_lead_in_contract_gives_no_hold(self):
        c = self.load({"scene_durations": [4.0, 10.0], "lead_in": 0})
        (_, l0, _), (_, l1, _) = self.budgets(c, ["A", "B"])
        self.assertEqual((l0, l1), (0.0, 0.0))

    def test_fallback_when_no_contract_has_no_lead_in(self):
        """Standalone dev renders are never muxed, so they must not gain 0.35s."""
        os.environ.pop(contract.DURATIONS_ENV, None)
        budget, lead, prov = contract.resolve_budget("A", 0, 7.5, self.FPS, contract.EMPTY)
        self.assertEqual((budget, lead), (7.5, 0.0))
        self.assertIn("fallback", prov)

    def test_name_resolution_beats_index(self):
        c = self.load({"scene_durations": [4.0, 10.0, 4.0],
                       "scenes": ["A", "B", "C"]})
        # Declared scene_index is deliberately wrong; the name must win.
        budget, lead, prov = contract.resolve_budget("C", 0, 5.0, self.FPS, c)
        self.assertAlmostEqual(budget, 4.0, places=6)
        self.assertEqual(lead, 0.0)
        self.assertIn("by name", prov)

    def test_unknown_name_fails_loudly(self):
        c = self.load({"scene_durations": [4.0], "scenes": ["A"]})
        with self.assertRaises(SystemExit) as cm:
            contract.resolve_budget("Ghost", 0, 5.0, self.FPS, c)
        self.assertIn("not in 'scenes'", str(cm.exception))

    def test_index_past_the_end_fails_loudly(self):
        c = self.load([4.0, 10.0])
        with self.assertRaises(SystemExit) as cm:
            contract.resolve_budget("C", 2, 5.0, self.FPS, c)
        self.assertIn("diverged", str(cm.exception))

    def test_total_length_without_a_contract_fails(self):
        with self.assertRaises(SystemExit):
            contract.total_length(self.FPS, contract.EMPTY)

    def test_total_length_is_the_narration_plus_lead_to_within_half_a_frame(self):
        c = self.load([4.0, 10.0, 4.0])
        for fps in (15.0, 24.0, 30.0, 60.0):
            with self.subTest(fps=fps):
                total = contract.total_length(fps, c)
                # A quantised length can be exactly half a frame off when the
                # boundary lands on x.5 frames (0.35s is 10.5 frames at 30fps),
                # so the bound is inclusive.
                self.assertLessEqual(abs(total - 18.35), 0.5 / fps + 1e-9)
                self.assertAlmostEqual(total * fps, round(total * fps), places=6)


class TestLogScraping(ContractTestCase):
    def test_reads_the_last_line(self):
        log = ("SCENE_DURATIONS [1.0, 2.0]\n"
               "noise\n"
               "SCENE_DURATIONS [4.212, 10.017, 3.981]\n")
        self.assertEqual(contract.durations_from_log(log), [4.212, 10.017, 3.981])

    def test_missing_line_fails_loudly(self):
        with self.assertRaises(SystemExit) as cm:
            contract.durations_from_log("nothing to see here")
        self.assertIn("SCENE_DURATIONS", str(cm.exception))

    def test_empty_array_fails_loudly(self):
        with self.assertRaises(SystemExit):
            contract.durations_from_log("SCENE_DURATIONS []\n")

    def test_raw_durations_line_is_not_mistaken_for_the_contract(self):
        """assemble_audio prints RAW_DURATIONS too; those exclude the gaps."""
        log = "RAW_DURATIONS [3.0, 9.0]\nSCENE_DURATIONS [3.15, 10.0]\n"
        self.assertEqual(contract.durations_from_log(log), [3.15, 10.0])


class TestWriting(ContractTestCase):
    def write_quietly(self, *args, **kwargs) -> None:
        with contextlib.redirect_stdout(io.StringIO()):
            contract.write_contract(*args, **kwargs)

    def test_round_trip_carries_the_lead_in(self):
        out = Path(tempfile.mkdtemp()) / "scene-durations.json"
        self.write_quietly([4.2124, 10.0], out, ["A", "B"], 30)
        c = contract.load_contract(out)
        self.assertEqual(c.durations, [4.212, 10.0])
        self.assertEqual(c.scenes, ["A", "B"])
        self.assertEqual(c.lead_in, contract.LEAD_IN_DEFAULT)
        self.assertEqual(c.fps, 30.0)

    def test_lead_in_is_always_written(self):
        out = Path(tempfile.mkdtemp()) / "scene-durations.json"
        self.write_quietly([4.0], out)
        self.assertIn("lead_in", json.loads(out.read_text()))

    def test_shipped_example_file_parses(self):
        c = contract.load_contract(ADAPTER / "scene-durations.example.json")
        self.assertEqual(len(c.durations), len(c.scenes or []))
        self.assertEqual(c.lead_in, contract.LEAD_IN_DEFAULT)


class TestCli(ContractTestCase):
    def parse(self, argv: list[str]):
        return contract.build_parser().parse_args(argv)

    def test_total_length_requires_fps(self):
        with self.assertRaises(SystemExit):
            contract.run(self.parse(["--total-length"]))

    def test_total_length_prints_seconds(self):
        path = self.write([4.0, 10.0, 4.0])
        os.environ[contract.DURATIONS_ENV] = str(path)
        try:
            import io
            from contextlib import redirect_stdout

            buf = io.StringIO()
            with redirect_stdout(buf):
                contract.run(self.parse(["--total-length", "--fps", "30"]))
            self.assertLessEqual(abs(float(buf.getvalue().strip()) - 18.35), 0.5 / 30.0 + 1e-6)
        finally:
            os.environ.pop(contract.DURATIONS_ENV, None)

    def test_scene_order_is_refused_without_manim(self):
        """contract.py cannot import a storyboard; it must say so, not crash."""
        argv = ["--scene-order", "scenes/demo.py"]
        sys.argv = ["contract.py", *argv]
        with self.assertRaises(SystemExit) as cm:
            contract.main()
        self.assertIn("pipeline_contract.py", str(cm.exception))

    def test_durations_and_from_log_are_mutually_exclusive(self):
        with self.assertRaises(SystemExit):
            self.parse(["--durations", "1,2", "--from-log", "x.log"])


if __name__ == "__main__":
    unittest.main()
