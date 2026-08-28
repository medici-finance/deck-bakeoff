#!/usr/bin/env bash
# Hardware-encode the final MP4 on Apple Silicon (h264_videotoolbox — seconds,
# not the >1hr libx264 -preset slow path). Muxes: recorded webm video + the
# normalized narration + a soft subtitle track.
#
# usage: encode.sh [--title T] [--url U] [--date D] [--description TEXT] <input.webm> <narration.wav> <subtitles.srt> <output.mp4>
set -euo pipefail

TITLE=""
URL=""
DATE=""
DESCRIPTION=""
while [[ $# -gt 4 ]]; do
  case "$1" in
    --title)       TITLE="$2";       shift 2 ;;
    --url)         URL="$2";         shift 2 ;;
    --date)        DATE="$2";        shift 2 ;;
    --description) DESCRIPTION="$2"; shift 2 ;;
    *) echo "encode.sh: unknown flag: $1" >&2; exit 1 ;;
  esac
done

WEBM=${1:?input webm required}
AUDIO=${2:?narration wav required}
SUBS=${3:?subtitles srt required}
OUT=${4:?output mp4 required}

# Expanded below as ${META[@]+"${META[@]}"}: under `set -u`, bash 3.2 (what
# /bin/bash still is on macOS, this tool's target) treats "${META[@]}" on an
# EMPTY array as an unbound variable and aborts — so a bare
# `encode.sh <webm> <wav> <srt> <mp4>` with no metadata flags would die here.
META=()
[ -n "$TITLE" ] && META+=(-metadata title="$TITLE")
[ -n "$URL" ]   && META+=(-metadata comment="$URL")
[ -n "$DATE" ]  && META+=(-metadata date="$DATE")
# Best-effort: the canonical description artifact is the .description.txt the
# orchestrator writes next to the mp4. The value arrives as a single argv
# element (never re-parsed by a shell), so newlines and quotes reach ffmpeg
# intact; how faithfully players surface multi-line MP4 metadata varies.
[ -n "$DESCRIPTION" ] && META+=(-metadata description="$DESCRIPTION" -metadata synopsis="$DESCRIPTION")

ffmpeg -y \
  -i "$WEBM" \
  -i "$AUDIO" \
  -i "$SUBS" \
  -map 0:v:0 -map 1:a:0 -map 2:s:0 \
  -c:v h264_videotoolbox -b:v 10M -pix_fmt yuv420p \
  -c:a aac -b:a 192k \
  -c:s mov_text \
  -movflags +faststart \
  ${META[@]+"${META[@]}"} \
  "$OUT"

echo "ENCODED: $OUT"
