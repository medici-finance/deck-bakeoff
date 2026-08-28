#!/usr/bin/env python3
"""Stdlib-only tests for the YouTube-description feature (## Description).

Run from the tool venv (PyYAML — the tool's only Python dep — installed):

    cd tools/explainer-video
    python3 tests/test_description.py

Not CI-wired (repo CI is lint-only); run before touching parse_description,
RunContext.out_description, or the orchestrator's post-encode publish tail.

Covers:
  a. parse_description returns the VERBATIM section body — boundaries
     respected (stops at the next `## ` H2, keeps `### ` subheadings and
     interior blank lines, strips leading/trailing blanks), heading matched
     case-insensitively, first section wins;
  b. a script without the section (or with an empty-bodied one) parses to ''
     and the render skips description emission gracefully — no .txt, no
     failure, and a stale .description.txt from a prior render is removed;
  c. the emission path: a successful run() writes out/<name>.description.txt
     with the verbatim body, and hands the same text to
     encode.sh as --description AFTER the script path (the R1 argv rule);
  d. RunContext.out_description shares the mp4's stem, and build_context
     actually wires parse_description into the context.
"""
from __future__ import annotations

import importlib.machinery
import importlib.util
import subprocess
import sys
import tempfile
import types
import unittest
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOL / "pipeline"))

from lib import (  # noqa: E402
    Profile,
    RunContext,
    Scene,
    build_context,
    parse_description,
)

SCENES = [Scene(id="s1", narration="n", subtitle="s")]

VTT = "WEBVTT\n\n1\n00:00:00.350 --> 00:00:02.000\nHello.\n"

DESCRIPTION_BODY = (
    "Assay is the assay office for agent-fleet software work.\n"
    "\n"
    "Learn more: https://assay.finance"
)

SCRIPT_WITH_DESCRIPTION = (
    "# Assay explainer\n"
    "\n"
    "| # | id | narration | subtitle |\n"
    "|---|----|-----------|----------|\n"
    "| 1 | s1 | \"n\"     | s        |\n"
    "\n"
    "## Description\n"
    "\n" + DESCRIPTION_BODY + "\n"
    "\n"
    "## Notes\n"
    "\n"
    "production notes that must NOT leak into the description\n"
)


def write(root: Path, body: str) -> Path:
    p = root / "SCRIPT.md"
    p.write_text(body)
    return p


def make_ctx(root: Path, name: str = "fixture", description: str = "") -> RunContext:
    out_dir = (root / "out").resolve()
    return RunContext(
        script=Path("unused"), slides=Path("unused"),
        profile=Profile(name="testprof", engine="qwen", model=""),
        out_dir=out_dir, name=name, scenes=SCENES,
        work=out_dir / f".work-{name}-testprof",
        description=description,
    )


class ParseDescriptionTest(unittest.TestCase):
    def test_verbatim_body_bounded_by_next_h2(self):
        with tempfile.TemporaryDirectory() as td:
            p = write(Path(td), SCRIPT_WITH_DESCRIPTION)
            body = parse_description(p)
        self.assertEqual(body, DESCRIPTION_BODY)
        self.assertNotIn("production notes", body)

    def test_runs_to_eof_when_last_section(self):
        with tempfile.TemporaryDirectory() as td:
            p = write(Path(td), "# T\n\n## Description\n\nlast section body\n\n\n")
            self.assertEqual(parse_description(p), "last section body")

    def test_keeps_interior_blanks_and_h3_subheadings(self):
        """`### ` does not match a `## ` boundary — it stays in the body."""
        body = "para one\n\n### Links\n\nhttps://assay.finance"
        with tempfile.TemporaryDirectory() as td:
            p = write(Path(td), "# T\n\n## Description\n" + body + "\n## Next\n")
            self.assertEqual(parse_description(p), body)

    def test_heading_matched_case_insensitively(self):
        for heading in ("## description", "## DESCRIPTION", "##   Description  "):
            with self.subTest(heading=heading), tempfile.TemporaryDirectory() as td:
                p = write(Path(td), f"# T\n\n{heading}\nbody\n")
                self.assertEqual(parse_description(p), "body")

    def test_first_section_wins(self):
        with tempfile.TemporaryDirectory() as td:
            p = write(Path(td),
                      "## Description\nfirst\n## Description\nsecond\n")
            self.assertEqual(parse_description(p), "first")

    def test_missing_section_returns_empty(self):
        for body in (
            "# T\n\n| id | narration |\n|---|---|\n| s1 | n |\n",   # no section
            "# T\n\n## Description\n\n\n## Next\nx\n",              # empty body
            "# T\n\n### Description\nnot an H2\n",                  # wrong level
            "# T\n\n## Description of scenes\nnot the section\n",   # wrong name
        ):
            with self.subTest(body=body), tempfile.TemporaryDirectory() as td:
                self.assertEqual(parse_description(write(Path(td), body)), "")


class ContextWiringTest(unittest.TestCase):
    def test_out_description_stem_matches_out_mp4(self):
        with tempfile.TemporaryDirectory() as td:
            ctx = make_ctx(Path(td))
            self.assertEqual(ctx.out_description.parent, ctx.out_mp4.parent)
            # delivered name is the clean base — no `-<profile>` voice suffix
            self.assertEqual(ctx.out_description.name, "fixture.description.txt")
            self.assertTrue(ctx.out_description.name.startswith(ctx.out_mp4.stem + "."))

    def test_build_context_parses_the_description(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            script = write(root, SCRIPT_WITH_DESCRIPTION)
            slides = root / "explainer.html"
            slides.write_text("<body></body>")
            ctx = build_context(
                script, slides, None, root / "out", None,
                profile_override=Profile(name="testprof", engine="qwen", model=""),
            )
            self.assertEqual(ctx.description, DESCRIPTION_BODY)


def _load_cli():
    """Import the extension-less ./explainer-video orchestrator as a module."""
    loader = importlib.machinery.SourceFileLoader(
        "explainer_video_cli", str(TOOL / "explainer-video"))
    spec = importlib.util.spec_from_loader("explainer_video_cli", loader)
    ev = importlib.util.module_from_spec(spec)
    loader.exec_module(ev)
    return ev


def _run_orchestrator(ctx: RunContext):
    """Drive ev.run(ctx) with every heavy step stubbed except the publish
    tail, mirroring test_subs.EncodeCmdOrderTest. Returns the encode argv."""
    ev = _load_cli()
    saved = {
        "tts": ev.gen_tts.generate,
        "asm": ev.assemble_audio.assemble,
        "subs": ev.gen_subs.write_subs,
    }
    ev.gen_tts.generate = lambda c: None
    ev.assemble_audio.assemble = lambda c: [1.0] * len(c.scenes)
    ev.inject_durations = lambda c, d: None
    ev.maybe_bundle_slides = lambda c: None  # new pipeline step; not under test here
    ev.gen_subs.write_subs = lambda c: (
        c.subtitles_srt.write_text("1\n00:00:00,350 --> 00:00:02,000\nHi.\n"),
        c.subtitles_vtt.write_text(VTT),
    )
    captured = {}

    def fake_subprocess_run(cmd, check=False, **kw):
        joined = [str(x) for x in cmd]
        if any("record.mjs" in x for x in joined):
            rec = Path(joined[-1])
            rec.mkdir(parents=True, exist_ok=True)
            (rec / "clip.webm").write_bytes(b"stand-in")
            return subprocess.CompletedProcess(cmd, 0)
        if any("encode.sh" in x for x in joined):
            captured["cmd"] = joined
            return subprocess.CompletedProcess(cmd, 0)
        raise AssertionError(f"unexpected subprocess.run: {joined}")

    ev.subprocess = types.SimpleNamespace(
        run=fake_subprocess_run,
        CalledProcessError=subprocess.CalledProcessError,
    )
    try:
        ev.run(ctx)
    finally:
        ev.gen_tts.generate = saved["tts"]
        ev.assemble_audio.assemble = saved["asm"]
        ev.gen_subs.write_subs = saved["subs"]
    return captured["cmd"]


class EmissionTest(unittest.TestCase):
    def test_successful_run_writes_the_txt_and_passes_the_flag(self):
        with tempfile.TemporaryDirectory() as td:
            ctx = make_ctx(Path(td), name="descase", description=DESCRIPTION_BODY)
            cmd = _run_orchestrator(ctx)

            out_txt = ctx.out_dir / "descase.description.txt"
            self.assertTrue(out_txt.exists())
            self.assertEqual(out_txt.read_text(), DESCRIPTION_BODY + "\n")

            # --description reaches encode.sh with the verbatim body, and
            # lands AFTER the script path (R1: bash rejects flags placed
            # between 'bash' and the script argument)
            self.assertTrue(cmd[1].endswith("encode.sh"), cmd[1])
            self.assertIn("--description", cmd)
            i = cmd.index("--description")
            self.assertGreater(i, 1)
            self.assertEqual(cmd[i + 1], DESCRIPTION_BODY)

    def test_no_description_skips_gracefully_and_drops_stale_txt(self):
        with tempfile.TemporaryDirectory() as td:
            ctx = make_ctx(Path(td), name="nodesc", description="")
            stale = ctx.out_dir / "nodesc.description.txt"
            stale.parent.mkdir(parents=True, exist_ok=True)
            stale.write_text("from a previous render whose script had one\n")

            cmd = _run_orchestrator(ctx)  # must not raise

            self.assertNotIn("--description", cmd)
            self.assertFalse(stale.exists(),
                             "stale .description.txt survived a render "
                             "whose script no longer has ## Description")


if __name__ == "__main__":
    unittest.main(verbosity=2)
