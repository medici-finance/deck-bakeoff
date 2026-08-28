#!/usr/bin/env python3
"""Prepare any audio file as a reference voice for Qwen3-TTS voice cloning.

Converts to 24kHz mono 16-bit WAV, trims silence, normalizes volume.

Usage:
    .venv/bin/python prep_voice.py input.mp3 -o audio/aussie_voice.wav
    .venv/bin/python prep_voice.py input.m4a --trim 30   # take first 30s
    .venv/bin/python prep_voice.py input.wav --trim 10:40 # take from 10s to 40s
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

SAMPLE_RATE = 24000

# silenceremove start stage: seconds of CONTINUOUS non-silence required before
# the filter stops trimming — the buffered audio is DISCARDED, so every output
# loses exactly this much from the head of its window when the window opens on
# speech (measured: sd=1 -> exactly 1.000s, review 4848044222 R2; sd=0.05 ->
# exactly 50ms, review 4848258041). MUST stay small, and the Realized report
# below shares this constant so the two cannot drift.
START_DURATION = 0.05


def main():
    parser = argparse.ArgumentParser(
        description="Prepare a voice sample for Qwen3-TTS voice cloning"
    )
    parser.add_argument("input", help="Input audio file (any format ffmpeg can read)")
    parser.add_argument("--output", "-o", default="audio/aussie_voice.wav",
                        help="Output WAV path (default: audio/aussie_voice.wav)")
    parser.add_argument("--trim", default=None,
                        help="Trim audio: '30' (first 30s), '10:40' (10s to 40s)")
    parser.add_argument("--no-silence-trim", action="store_true",
                        help="Skip silence trimming")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        sys.exit(f"Error: input file not found: {args.input}")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not shutil.which("ffmpeg"):
        sys.exit("Error: ffmpeg is required. Install with: brew install ffmpeg")

    # Build ffmpeg filters
    filters = []

    # Trim
    if args.trim:
        if ":" in args.trim:
            start, end = args.trim.split(":")
            filters.append(f"atrim={start}:{end}")
        else:
            filters.append(f"atrim=0:{args.trim}")

    # Silence trim (remove leading/trailing silence). See START_DURATION above:
    # the start stage discards its buffer, so this costs exactly START_DURATION
    # from the head of every window that opens on speech.
    if not args.no_silence_trim:
        filters.append(
            f"silenceremove=start_periods=1:start_duration={START_DURATION}:"
            "start_threshold=-50dB:detection=peak:"
            "stop_periods=-1:stop_duration=0.5:stop_threshold=-50dB"
        )

    # Normalize
    filters.append("loudnorm=I=-16:TP=-1.5:LRA=11")

    filter_chain = ",".join(filters)

    cmd = [
        "ffmpeg", "-y",
        "-i", str(input_path),
        "-af", filter_chain,
        "-ar", str(SAMPLE_RATE),
        "-ac", "1",
        "-sample_fmt", "s16",
        str(output_path),
    ]

    print(f"Converting: {args.input} -> {output_path}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print("ffmpeg error:")
        print(result.stderr)
        sys.exit(1)

    # Report
    duration = float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(output_path)],
        text=True,
    ).strip())

    size_kb = output_path.stat().st_size / 1024

    print(f"✅ Done!")
    print(f"   Output:   {output_path}")
    print(f"   Duration: {duration:.1f}s")
    print(f"   Size:     {size_kb:.0f} KB")
    print(f"   Format:   {SAMPLE_RATE}Hz mono 16-bit WAV")

    # Report the REALIZED window. silenceremove's start stage discards its
    # buffer, shifting the head by exactly START_DURATION when the window opens
    # on speech (review 4848258041 R1: the prior report ignored this and was
    # off by exactly start_duration at both ends). Any transcript written
    # against source timestamps must use the realized ones.
    if args.trim and ":" in args.trim:
        t0, t1 = (float(x) for x in args.trim.split(":"))
        head = 0.0 if args.no_silence_trim else START_DURATION
        realized_start = t0 + head
        realized_end = realized_start + duration
        print(f"   Realized: {realized_start:.3f}s -> {realized_end:.3f}s of source"
              f" (requested {t0:g}:{t1:g}; head trim {head:.3f}s)")
    print()

    if duration < 5:
        print("⚠️  Clip is under 5 seconds — voice cloning works best with 10-30+ seconds.")
    elif duration < 10:
        print("💡 10-30+ seconds of speech gives better voice cloning results.")
    else:
        print("💡 Good duration for voice cloning.")

    print()
    print("Now add it to voices/registry.yaml and use it with ./explainer-video --profile <name>.")


if __name__ == "__main__":
    main()
