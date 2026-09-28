#!/usr/bin/env python3
"""Generate one narration clip per scene with MLX-Audio, driven by a voice
profile from voices/registry.yaml.

This is the parameterized generalization of the winning `gen_qwen_aussie.py`
(preserved verbatim under pipeline/alternates/ for reference). Engine is chosen
by the profile:

  qwen    voice-CLONED from ref_audio + ref_text (the winning path; all 7
          current profiles in voices/registry.yaml use this). CRITICAL:
          --max_tokens 4096 — the mlx_audio default (1200 ~= 14.6s) silently
          truncates long scenes.
  qwen_custom
          Qwen3-TTS CustomVoice preset speaker, optionally steered by a
          natural-language `instruct`. No reference clip.
  orpheus built-in `voice` preset, no reference. Not used by any current
          profile; available for a future no-reference profile.
  kokoro  built-in neural `voice` preset, no reference. Not used by any
          current profile; available for a future no-reference profile.

Writes work/<scene.id>.wav for every scene in the RunContext.
"""
from __future__ import annotations

import subprocess
import sys
import wave
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import RunContext, Scene  # noqa: E402


def _mlx_cmd(ctx: RunContext, scene: Scene, prefix: str) -> list[str]:
    p = ctx.profile
    cmd = [
        sys.executable, "-m", "mlx_audio.tts.generate",
        "--model", p.model,
        "--text", scene.narration,
        "--file_prefix", prefix,
        "--output_path", str(ctx.work),
    ]
    if p.engine == "qwen":
        cmd += ["--ref_audio", str(p.ref_audio), "--ref_text", p.ref_text or ""]
        cmd += ["--max_tokens", str(p.params.get("max_tokens", 4096))]
    elif p.engine == "qwen_custom":
        if not p.voice:
            raise SystemExit("engine=qwen_custom requires a preset voice")
        cmd += ["--voice", p.voice]
        cmd += ["--lang_code", p.params.get("lang_code", "english")]
        instruct = p.params.get("instruct")
        if instruct:
            cmd += ["--instruct", instruct]
        cmd += ["--max_tokens", str(p.params.get("max_tokens", 4096))]
    elif p.engine in ("orpheus", "kokoro"):
        if p.voice:
            cmd += ["--voice", p.voice]
        if "max_tokens" in p.params:
            cmd += ["--max_tokens", str(p.params["max_tokens"])]
    else:
        raise SystemExit(f"unsupported engine: {p.engine}")
    return cmd


def _wav_seconds(path: Path) -> float:
    with wave.open(str(path), "rb") as w:
        return w.getnframes() / w.getframerate()


def _plausible_bounds(narration: str) -> tuple[float, float]:
    """Duration window a take must land in, from word count alone.

    Speech slower than ~100 wpm or faster than ~240 wpm is not a take, it is a
    failure mode: Qwen occasionally misses its end-of-speech and generates
    until max_tokens (a 28s scene once came back as 327s of degenerate audio),
    and the inverse cap-truncation cuts a scene short. Generous margins so no
    legitimate delivery is ever rejected.
    """
    words = max(1, len(narration.split()))
    lo = words / 4.0          # 240 wpm — nothing real is faster
    hi = words / 1.5 + 6.0    # 90 wpm + pause allowance — nothing real is slower
    return lo, hi


def generate(ctx: RunContext) -> None:
    ctx.work.mkdir(parents=True, exist_ok=True)
    for scene in ctx.scenes:
        prefix = scene.id
        lo, hi = _plausible_bounds(scene.narration)
        attempts = 3
        for attempt in range(1, attempts + 1):
            print(f"=== {ctx.profile.name}: {prefix} (take {attempt}) ===", file=sys.stderr)
            subprocess.run(_mlx_cmd(ctx, scene, prefix), check=True, cwd=ctx.work)
            # mlx_audio writes "<prefix>_000.wav"
            src = ctx.work / f"{prefix}_000.wav"
            dst = ctx.scene_wav(scene)
            if not src.exists():
                raise SystemExit(f"expected TTS output missing: {src}")
            src.replace(dst)
            dur = _wav_seconds(dst)
            # sanity: warn on the ~14.6s truncation signature
            flag = "  <-- SUSPICIOUS (near max_tokens cap?)" if 14.0 < dur < 15.2 else ""
            print(f"-> {dst.name}  {dur:.2f}s{flag}", file=sys.stderr)
            if lo <= dur <= hi:
                break
            kind = "runaway" if dur > hi else "truncated"
            print(f"!! {prefix}: {kind} take ({dur:.2f}s for "
                  f"{len(scene.narration.split())} words; plausible {lo:.1f}-{hi:.1f}s)"
                  + ("" if attempt == attempts else " — retrying"), file=sys.stderr)
        else:
            raise SystemExit(
                f"{prefix}: no plausible take in {attempts} attempts — "
                f"last was {dur:.2f}s for a {lo:.1f}-{hi:.1f}s window. "
                f"Check the narration for pathological tokens, or re-run.")


if __name__ == "__main__":
    # Standalone: `gen_tts.py <script.md> <slides.html> <profile> <out_dir>`
    from lib import build_context

    if len(sys.argv) != 5:
        raise SystemExit("usage: gen_tts.py <script.md> <slides.html> <profile> <out_dir>")
    ctx = build_context(Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3], Path(sys.argv[4]), None)
    generate(ctx)
