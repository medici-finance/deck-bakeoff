#!/usr/bin/env python3
"""Stdlib-only tests for the .vtt-alongside-mp4 feature (PR #10 review, N2).

Run from the tool venv (PyYAML — the tool's only Python dep — installed):

    cd tools/explainer-video
    python3 tests/test_subs.py

Not CI-wired (repo CI is lint-only); run before touching pipeline/gen_subs.py
or the explainer-video orchestrator's encode/publish tail.

Covers:
  a. write_subs escapes & < > in WebVTT cue text, leaves the .srt raw
     (mov_text is plain text — escaping it would show entities verbatim);
  b. publish_vtt copies a valid .vtt byte-identically, and raises SystemExit
     (naming the completed mp4) on a missing or zero-length/invalid source;
  c. RunContext.out_vtt has the same stem as out_mp4;
  d. a failed encode (genuine non-zero exit from encode.sh) propagates out of
     the orchestrator's run() and leaves no .vtt/.mp4 in out/.
"""
from __future__ import annotations

import importlib.machinery
import importlib.util
import os
import subprocess
import sys
import tempfile
import types
import unittest
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOL / "pipeline"))

import gen_subs  # noqa: E402
from lib import Profile, RunContext, Scene  # noqa: E402

SCENES = [
    Scene(id="s1", narration="narration one", subtitle="P < N when vol is high"),
    Scene(id="s2", narration="narration two", subtitle="P (Protected) & N (Amplified)"),
]

VTT = "WEBVTT\n\n1\n00:00:00.350 --> 00:00:02.000\nHello.\n"


def make_ctx(root: Path, name: str = "fixture") -> RunContext:
    # work lives *under* out_dir, exactly as build_context computes it
    # (out_dir / f".work-{name}-{profile.name}"); run() refuses to clean a
    # work dir that is not a '.work-*' child of --out.
    out_dir = (root / "out").resolve()
    return RunContext(
        script=Path("unused"), slides=Path("unused"),
        profile=Profile(name="testprof", engine="qwen", model=""),
        out_dir=out_dir, name=name, scenes=SCENES,
        work=out_dir / f".work-{name}-testprof",
    )


class WriteSubsEscapeTest(unittest.TestCase):
    def test_vtt_escaped_srt_raw(self):
        with tempfile.TemporaryDirectory() as td:
            ctx = make_ctx(Path(td))
            ctx.work.mkdir(parents=True)
            orig = gen_subs._ffprobe_duration
            gen_subs._ffprobe_duration = lambda p: 1.25
            try:
                gen_subs.write_subs(ctx)
            finally:
                gen_subs._ffprobe_duration = orig
            vtt = ctx.subtitles_vtt.read_text()
            srt = ctx.subtitles_srt.read_text()
        self.assertTrue(vtt.startswith("WEBVTT"))
        # vtt cue text is escaped
        self.assertIn("P &lt; N when vol is high", vtt)
        self.assertIn("P (Protected) &amp; N (Amplified)", vtt)
        self.assertNotIn("P < N when vol is high", vtt)
        # srt cue text stays raw (muxed as mov_text plain text)
        self.assertIn("P < N when vol is high", srt)
        self.assertIn("P (Protected) & N (Amplified)", srt)
        self.assertNotIn("&lt;", srt)
        self.assertNotIn("&amp;", srt)


class PublishVttTest(unittest.TestCase):
    def test_success_byte_identical(self):
        with tempfile.TemporaryDirectory() as td:
            ctx = make_ctx(Path(td))
            ctx.work.mkdir(parents=True)
            # run() creates this before encode; work/ already nests inside it
            ctx.out_dir.mkdir(parents=True, exist_ok=True)
            ctx.subtitles_vtt.write_text(VTT)
            result = gen_subs.publish_vtt(ctx)
            # delivered name is the clean base — no `-<profile>` voice suffix
            expected = ctx.out_dir / "fixture.vtt"
            self.assertEqual(result, expected)
            self.assertEqual(expected.read_bytes(), VTT.encode())

    def test_missing_source_raises(self):
        with tempfile.TemporaryDirectory() as td:
            ctx = make_ctx(Path(td))
            ctx.work.mkdir(parents=True)  # work dir exists, subtitles.vtt does not
            with self.assertRaises(SystemExit) as cm:
                gen_subs.publish_vtt(ctx)
            self.assertIn("fixture.mp4", str(cm.exception))
            self.assertFalse(ctx.out_vtt.exists())

    def test_zero_length_source_raises(self):
        with tempfile.TemporaryDirectory() as td:
            ctx = make_ctx(Path(td))
            ctx.work.mkdir(parents=True)
            ctx.subtitles_vtt.write_bytes(b"")  # 0-byte: no WEBVTT magic
            with self.assertRaises(SystemExit) as cm:
                gen_subs.publish_vtt(ctx)
            self.assertIn("fixture.mp4", str(cm.exception))
            self.assertFalse(ctx.out_vtt.exists())

    def test_out_vtt_stem_matches_out_mp4(self):
        with tempfile.TemporaryDirectory() as td:
            ctx = make_ctx(Path(td))
            self.assertEqual(ctx.out_vtt.stem, ctx.out_mp4.stem)
            self.assertEqual(ctx.out_vtt.parent, ctx.out_mp4.parent)
            self.assertEqual(ctx.out_vtt.suffix, ".vtt")
            self.assertEqual(ctx.out_mp4.suffix, ".mp4")


def _load_cli():
    """Import the extension-less ./explainer-video orchestrator as a module."""
    loader = importlib.machinery.SourceFileLoader(
        "explainer_video_cli", str(TOOL / "explainer-video"))
    spec = importlib.util.spec_from_loader("explainer_video_cli", loader)
    ev = importlib.util.module_from_spec(spec)
    loader.exec_module(ev)
    return ev


class FailedEncodeTest(unittest.TestCase):
    def test_failed_encode_leaves_no_vtt_or_mp4(self):
        with tempfile.TemporaryDirectory() as td:
            ctx = make_ctx(Path(td), name="failcase")
            ev = _load_cli()
            # ev.gen_tts / ev.assemble_audio / ev.gen_subs are the SAME module
            # objects this test imported — snapshot and restore so the patches
            # don't leak into the other test classes.
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
            real_run = subprocess.run
            # Force /bin first on PATH for the encode.sh invocation, same as
            # the review's own repro ("forcing bash 3.2 first on PATH"): the
            # tool's target platform is macOS, where /bin/bash is still 3.2,
            # but a dev machine's PATH commonly resolves the bare "bash" run()
            # invokes to a Homebrew bash >=4.4 that never had the empty-array
            # unbound-variable bug — so without this, the mutation this test
            # exists to catch is invisible on such a machine.
            forced_env = dict(os.environ)
            if Path("/bin/bash").exists():
                forced_env["PATH"] = "/bin:" + forced_env.get("PATH", "")

            def fake_subprocess_run(cmd, check=False, **kw):
                joined = [str(x) for x in cmd]
                if any("record.mjs" in x for x in joined):
                    rec = Path(joined[-1])
                    rec.mkdir(parents=True, exist_ok=True)
                    (rec / "clip.webm").write_bytes(b"not a real webm")
                    return subprocess.CompletedProcess(cmd, 0)
                # encode.sh runs for real: ffmpeg rejects the bogus webm
                return real_run(cmd, check=check, capture_output=True,
                                 env=forced_env, **kw)

            ev.subprocess = types.SimpleNamespace(
                run=fake_subprocess_run,
                CalledProcessError=subprocess.CalledProcessError,
            )
            try:
                with self.assertRaises(subprocess.CalledProcessError) as cm:
                    ev.run(ctx)
            finally:
                ev.gen_tts.generate = saved["tts"]
                ev.assemble_audio.assemble = saved["asm"]
                ev.gen_subs.write_subs = saved["subs"]
            self.assertFalse((ctx.out_dir / "failcase.vtt").exists())
            self.assertFalse((ctx.out_dir / "failcase.mp4").exists())
            # Required-2 (review 4850520385 revisited, mp14 review 2): a bare
            # "did it fail?" assertion passes on every failure mode, including
            # the two bugs this PR fixed — a shell arg-parsing crash presents
            # as a CalledProcessError too. Pin the REASON: this must be ffmpeg
            # rejecting the bogus webm, not encode.sh's own argv handling
            # falling over first.
            stderr = (cm.exception.stderr or b"").decode(errors="replace")
            self.assertNotIn("unbound variable", stderr,
                              "encode.sh's own bash-3.2 empty-array bug, not ffmpeg")
            self.assertNotIn("invalid option", stderr,
                              "the R1 argv-ordering bug (flags landed before the "
                              "script path and bash rejected them), not ffmpeg")
            self.assertTrue(
                "Invalid data found" in stderr or "Error opening input" in stderr,
                f"failure doesn't look like ffmpeg rejecting the bogus webm: {stderr!r}",
            )


class EncodeCmdOrderTest(unittest.TestCase):
    """Required-1 (review 4850520385 revisited, mp14 review 2): the metadata
    flags must land AFTER the encode.sh script path in the constructed argv,
    not between 'bash' and the script — the exact defect the first review
    found (bash rejects a flag in that position before encode.sh ever runs),
    and `dry_run` cannot catch it because it never builds `encode_cmd`.
    Capture the real argv `run()` hands to subprocess.run and assert on it
    directly, so reverting the insertion index turns this test red."""

    def test_flags_inserted_after_script_path_not_before(self):
        with tempfile.TemporaryDirectory() as td:
            ctx = make_ctx(Path(td), name="metacase")
            ctx.title_raw = "A Title"
            ctx.url = "https://example.test"
            ctx.generated_at = "2026-08-08T00:00:00Z"
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
                    # don't actually run ffmpeg here — EncodeCmdOrderTest is
                    # about argv shape, FailedEncodeTest above already covers
                    # the real encode.sh/ffmpeg path
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

            cmd = captured["cmd"]
            self.assertEqual(cmd[0], "bash")
            # R1: index 1 must be the encode.sh path, not a flag — reverting
            # to `encode_cmd[1:1] = [...]` lands "--date" (last inserted)
            # here instead, and bash rejects it before encode.sh ever runs.
            self.assertTrue(cmd[1].endswith("encode.sh"), cmd[1])
            self.assertNotIn(cmd[1], ("--title", "--url", "--date"))
            for flag in ("--title", "--url", "--date"):
                self.assertIn(flag, cmd)
                self.assertGreater(cmd.index(flag), 1,
                                    f"{flag} landed at/before index 1 (before the script path)")
            # the four positionals still trail, in order, untouched by the
            # flag insertion
            webm = sorted(ctx.rec_dir.glob("*.webm"))[-1]
            self.assertEqual(
                cmd[-4:],
                [str(webm), str(ctx.narration_wav), str(ctx.subtitles_srt), str(ctx.out_mp4)],
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
