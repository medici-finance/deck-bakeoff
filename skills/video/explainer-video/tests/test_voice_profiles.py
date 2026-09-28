#!/usr/bin/env python3
"""Voice-profile resolution and MLX command tests.

Run from the tool venv (PyYAML — the tool's only Python dep — installed):

    cd skills/video/explainer-video
    python3 tests/test_voice_profiles.py
"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOL / "pipeline"))

from gen_tts import _mlx_cmd  # noqa: E402
from lib import (  # noqa: E402
    Profile,
    RunContext,
    Scene,
    load_profile,
    us_qwen_steered_profile,
)


def make_ctx(profile: Profile) -> RunContext:
    return RunContext(
        script=Path("SCRIPT.md"),
        slides=Path("explainer.html"),
        profile=profile,
        out_dir=Path("out").resolve(),
        name="fixture",
        scenes=[Scene(id="title", narration="This is the narration.", subtitle="")],
        work=Path("out").resolve() / f".work-fixture-{profile.name}",
    )


class QwenCustomCommandTest(unittest.TestCase):
    def test_custom_voice_carries_speaker_language_instruction_and_cap(self):
        profile = us_qwen_steered_profile("AIDEN")
        ctx = make_ctx(profile)
        cmd = _mlx_cmd(ctx, ctx.scenes[0], ctx.scenes[0].id)

        self.assertEqual(cmd[cmd.index("--model") + 1], profile.model)
        self.assertEqual(cmd[cmd.index("--voice") + 1], "aiden")
        self.assertEqual(cmd[cmd.index("--lang_code") + 1], "english")
        self.assertEqual(cmd[cmd.index("--instruct") + 1],
                         profile.params["instruct"])
        self.assertEqual(cmd[cmd.index("--max_tokens") + 1], "4096")
        self.assertNotIn("--ref_audio", cmd)

    def test_registry_custom_voice_without_speaker_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            registry = Path(td) / "registry.yaml"
            registry.write_text(
                "profiles:\n"
                "  bad:\n"
                "    engine: qwen_custom\n"
                "    model: example-model\n"
            )
            with self.assertRaises(SystemExit) as raised:
                load_profile("bad", registry=registry)
            self.assertIn("no preset voice", str(raised.exception))

    def test_registry_custom_voice_with_speaker_resolves(self):
        with tempfile.TemporaryDirectory() as td:
            registry = Path(td) / "registry.yaml"
            registry.write_text(
                "profiles:\n"
                "  steered:\n"
                "    engine: qwen_custom\n"
                "    model: example-custom-model\n"
                "    voice: aiden\n"
                "    params:\n"
                "      lang_code: english\n"
                "      instruct: Calm narrator.\n"
            )
            profile = load_profile("steered", registry=registry)
            ctx = make_ctx(profile)
            cmd = _mlx_cmd(ctx, ctx.scenes[0], ctx.scenes[0].id)
            self.assertEqual(cmd[cmd.index("--voice") + 1], "aiden")
            self.assertEqual(cmd[cmd.index("--lang_code") + 1], "english")
            self.assertEqual(cmd[cmd.index("--instruct") + 1], "Calm narrator.")

    def test_unknown_built_in_speaker_is_rejected(self):
        with self.assertRaises(SystemExit) as raised:
            us_qwen_steered_profile("zac")
        self.assertIn("unknown Qwen US voice", str(raised.exception))


if __name__ == "__main__":
    unittest.main(verbosity=2)
