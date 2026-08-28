#!/usr/bin/env python3
"""Concatenate the per-scene narration clips into work/narration_full.wav with
a lead-in, inter-scene gaps and a tail, then loudness-normalize to the
deliverable spec (48kHz stereo, -16 LUFS).

Returns SCENE_DURATIONS (raw clip duration + inter-scene gap, one per scene) to
inject into the slides' `window.SCENE_DURATIONS`. Generalized from the winning
ad-hoc `assemble_audio.py`; operates on a RunContext instead of hardcoded paths.
"""
from __future__ import annotations

import subprocess
import sys
import wave
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import RunContext  # noqa: E402

LEAD_S = 0.35
GAP_S = 0.15
TAIL_S = 1.0


def _params(path: Path):
    with wave.open(str(path), "rb") as w:
        return w.getframerate(), w.getnchannels(), w.getsampwidth()


def _duration(path: Path) -> float:
    with wave.open(str(path), "rb") as w:
        return w.getnframes() / w.getframerate()


def _silence(path: Path, seconds: float, rate: int, channels: int, sampwidth: int) -> None:
    n = int(seconds * rate)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(channels)
        w.setsampwidth(sampwidth)
        w.setframerate(rate)
        w.writeframes(b"\x00" * n * channels * sampwidth)


def assemble(ctx: RunContext) -> list[float]:
    scene_paths = [ctx.scene_wav(s) for s in ctx.scenes]
    for p in scene_paths:
        if not p.exists():
            raise SystemExit(f"missing scene clip {p} (run gen_tts first)")

    rate, channels, sampwidth = _params(scene_paths[0])
    durs = [_duration(p) for p in scene_paths]

    silences = ctx.work / "silences"
    silences.mkdir(exist_ok=True)
    lead = silences / "lead.wav"
    gap = silences / "gap.wav"
    tail = silences / "tail.wav"
    _silence(lead, LEAD_S, rate, channels, sampwidth)
    _silence(gap, GAP_S, rate, channels, sampwidth)
    _silence(tail, TAIL_S, rate, channels, sampwidth)

    # Paths here are first-party (repo-relative work-dir paths), never
    # user-supplied, so this isn't exploitable — but the ffmpeg concat demuxer
    # parses `file '...'` as a single-quoted string, so a literal `'` in a
    # path would break parsing. If work-dir paths ever become configurable,
    # escape `'` as `'\''` before writing this list.
    list_path = ctx.work / "concat_list.txt"
    lines = [f"file '{lead}'"]
    for i, p in enumerate(scene_paths):
        lines.append(f"file '{p}'")
        lines.append(f"file '{tail if i == len(scene_paths) - 1 else gap}'")
    list_path.write_text("\n".join(lines) + "\n")

    raw = ctx.work / "narration_raw.wav"
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(list_path),
         "-c", "copy", str(raw)],
        check=True,
    )
    # resample + loudness-normalize to the deliverable spec
    subprocess.run(
        ["ffmpeg", "-y", "-i", str(raw), "-ar", "48000", "-ac", "2",
         "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", str(ctx.narration_wav)],
        check=True,
    )

    # The last scene is followed by TAIL_S of trailing silence in the concat
    # (not GAP_S like every other scene) — the injected duration must match.
    scene_durations = [
        round(d + (TAIL_S if i == len(durs) - 1 else GAP_S), 3)
        for i, d in enumerate(durs)
    ]
    print("RAW_DURATIONS", [round(d, 3) for d in durs])
    print("SCENE_DURATIONS", scene_durations)
    print("OUT", ctx.narration_wav)
    return scene_durations


if __name__ == "__main__":
    from lib import build_context

    if len(sys.argv) != 5:
        raise SystemExit("usage: assemble_audio.py <script.md> <slides.html> <profile> <out_dir>")
    ctx = build_context(Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3], Path(sys.argv[4]), None)
    assemble(ctx)
