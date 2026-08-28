#!/usr/bin/env python3
"""Write work/subtitles.srt and .vtt from the measured per-scene clip durations
(via ffprobe) and the subtitle text of each scene in the RunContext.

Same timing formula as the audio assembly: start_i = cum, end_i = cum + raw_i,
cum = end_i + gap, with a lead-in before scene 1. Generalized from the winning
ad-hoc `gen_subs.py`.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import RunContext  # noqa: E402

LEAD_S = 0.35
GAP_S = 0.15


def _ffprobe_duration(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        check=True, capture_output=True, text=True,
    )
    return float(out.stdout.strip())


def _fmt_srt(t: float) -> str:
    # Round to whole milliseconds first, then decompose h/m/s/ms from that
    # integer — rounding the fractional part in isolation (e.g. 999.5ms ->
    # 1000) can produce an out-of-range ms field like "00:00:42,1000".
    total_ms = int(round(t * 1000))
    h, rem_ms = divmod(total_ms, 3600_000)
    m, rem_ms = divmod(rem_ms, 60_000)
    s, ms = divmod(rem_ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def _fmt_vtt(t: float) -> str:
    return _fmt_srt(t).replace(",", ".")


def _vtt_escape(text: str) -> str:
    # WebVTT cue text: "<" opens a cue span tag, so escape & < > ("&" first,
    # so the escapes themselves aren't re-escaped). The .srt branch stays RAW
    # — mov_text is plain text, escaping it would show entities verbatim.
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def write_subs(ctx: RunContext) -> None:
    raw = [round(_ffprobe_duration(ctx.scene_wav(s)), 3) for s in ctx.scenes]

    entries = []
    cum = LEAD_S
    for scene, d in zip(ctx.scenes, raw):
        start = cum
        end = cum + d
        entries.append((start, end, scene.subtitle))
        cum = end + GAP_S

    srt_lines = []
    vtt_lines = ["WEBVTT", ""]
    for i, (start, end, text) in enumerate(entries, 1):
        srt_lines += [str(i), f"{_fmt_srt(start)} --> {_fmt_srt(end)}", text, ""]
        vtt_lines += [str(i), f"{_fmt_vtt(start)} --> {_fmt_vtt(end)}", _vtt_escape(text), ""]

    ctx.subtitles_srt.write_text("\n".join(srt_lines).rstrip() + "\n")
    ctx.subtitles_vtt.write_text("\n".join(vtt_lines).rstrip() + "\n")
    print("wrote", ctx.subtitles_srt.name, ctx.subtitles_vtt.name)


def publish_vtt(ctx: RunContext) -> Path:
    """Copy the run's .vtt alongside the final mp4 (same stem), for web
    players' <track> elements. Call only AFTER a successful encode so a
    failed run never leaves a stray .vtt in out/."""
    src = ctx.subtitles_vtt
    valid = src.exists() and src.read_text(errors="replace").startswith("WEBVTT")
    if not valid:
        raise SystemExit(
            f"encode succeeded — mp4 is complete at {ctx.out_mp4} — but the "
            f"subtitles .vtt is missing or invalid (no WEBVTT header): {src}. "
            f"Nothing published to {ctx.out_vtt}."
        )
    shutil.copyfile(src, ctx.out_vtt)
    return ctx.out_vtt


if __name__ == "__main__":
    from lib import build_context

    if len(sys.argv) != 5:
        raise SystemExit("usage: gen_subs.py <script.md> <slides.html> <profile> <out_dir>")
    ctx = build_context(Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3], Path(sys.argv[4]), None)
    write_subs(ctx)
