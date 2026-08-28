#!/usr/bin/env bash
# render.sh — render every scene of a Manim storyboard and concatenate them into
# ONE video stream that `pipeline/encode.sh` can mux with the pipeline's
# narration and subtitles.
#
# This replaces step 4 of the pipeline (`inject` + `record.mjs`). Everything
# else — gen_tts, assemble_audio, gen_subs, encode.sh — is unchanged.
#
# usage:
#   ./render.sh [options]
#     -m, --module FILE      scenes module (default: scenes/demo.py)
#     -d, --durations FILE   scene-durations.json from the pipeline
#                            (default: $MEDICI_SCENE_DURATIONS, else the module's
#                            fallback durations)
#     -o, --out DIR          output directory (default: ./out)
#     -q, --quality l|h      l = 854x480@15 smoke render, h = 1920x1080@30
#                            deliverable (default: h)
#         --keep-media       keep the per-scene media dir (default: kept anyway,
#                            flag retained for symmetry/scripting)
#
# output:
#   <out>/manim.mp4          H.264 / yuv420p / <fps> / 1920x1080, no audio
#   <out>/manim-scenes.txt   the ffmpeg concat list (per-scene provenance)
#
# handoff to the pipeline:
#   bash ../../pipeline/encode.sh <out>/manim.mp4 <work>/narration_full.wav \
#        <work>/subtitles.srt out/<name>.mp4
#
# encode.sh's first argument is named WEBM because the HTML path produces webm;
# it is only ever `ffmpeg -i`'d, so an H.264 mp4 is accepted unchanged. The final
# mux re-encodes video with h264_videotoolbox regardless, so the intermediate
# codec choice here costs nothing downstream.
#
# When --durations is supplied, the concatenated video's length is CHECKED
# against the contract (lead-in + every scene) and a mismatch fails the run.
# A renderer that hands `encode.sh` a short or long video produces a file that
# plays but drifts against its own narration, which is worse than no file.
set -euo pipefail

ADAPTER_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Adapter-relative, so the default storyboard resolves from any cwd (a deck repo
# drives this script from its own directory). A user-supplied -m stays
# cwd-relative, which is what a relative path on a command line should mean.
MODULE="$ADAPTER_DIR/scenes/demo.py"
DURATIONS="${MEDICI_SCENE_DURATIONS:-}"
OUT="$ADAPTER_DIR/out"
QUALITY="h"

while [[ $# -gt 0 ]]; do
  case "$1" in
    -m|--module)    MODULE="$2"; shift 2 ;;
    -d|--durations) DURATIONS="$2"; shift 2 ;;
    -o|--out)       OUT="$2"; shift 2 ;;
    -q|--quality)   QUALITY="$2"; shift 2 ;;
    --keep-media)   shift ;;
    # Print the header block itself rather than a hardcoded line range, which
    # silently starts printing the code the moment the header grows a line.
    -h|--help)      awk 'NR>1 && /^#/ {print; next} NR>1 {exit}' "${BASH_SOURCE[0]}"; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
done

case "$QUALITY" in
  l) WIDTH=854;  HEIGHT=480;  FPS=15 ;;
  h) WIDTH=1920; HEIGHT=1080; FPS=30 ;;
  *) echo "--quality must be 'l' (smoke) or 'h' (deliverable)" >&2; exit 2 ;;
esac

PY="$ADAPTER_DIR/.venv/bin/python"
[[ -x "$PY" ]] || { echo "no venv at $ADAPTER_DIR/.venv — see README §Setup" >&2; exit 1; }
command -v ffmpeg >/dev/null || { echo "ffmpeg not on PATH (brew install ffmpeg)" >&2; exit 1; }
command -v ffprobe >/dev/null || { echo "ffprobe not on PATH (brew install ffmpeg)" >&2; exit 1; }

MODULE_ABS="$(cd "$(dirname "$MODULE")" && pwd)/$(basename "$MODULE")"
[[ -f "$MODULE_ABS" ]] || { echo "scenes module not found: $MODULE" >&2; exit 1; }

if [[ -n "$DURATIONS" ]]; then
  [[ -f "$DURATIONS" ]] || { echo "durations file not found: $DURATIONS" >&2; exit 1; }
  DURATIONS="$(cd "$(dirname "$DURATIONS")" && pwd)/$(basename "$DURATIONS")"
  export MEDICI_SCENE_DURATIONS="$DURATIONS"
  echo "durations : $DURATIONS"
else
  # Unset rather than empty: an empty env var would still be preferred over the
  # module fallbacks by pipeline_contract's lookup order.
  unset MEDICI_SCENE_DURATIONS || true
  echo "durations : (none — using each scene's fallback_duration)"
fi

# Absolute, always. ffmpeg's concat demuxer resolves a relative `file '...'`
# entry against the LIST FILE's own directory, not the cwd — so a relative
# --out wrote a list whose paths only resolved by accident with the default
# ./out, and failed on every other value (field-reported from medici-decks#14).
mkdir -p "$OUT"
OUT="$(cd "$OUT" && pwd)"
MEDIA_DIR="$OUT/media"
mkdir -p "$MEDIA_DIR"

# SCENE_ORDER is the storyboard's own declaration of scene classes, in SCRIPT.md
# order. Reading it (rather than globbing class names) is what keeps scene N of
# the video aligned with narration clip N.
# (No `mapfile` — macOS ships bash 3.2.)
SCENES=()
while IFS= read -r line; do
  [[ -n "$line" ]] && SCENES+=("$line")
done < <("$PY" "$ADAPTER_DIR/pipeline_contract.py" --scene-order "$MODULE_ABS")
[[ ${#SCENES[@]} -gt 0 ]] || { echo "no scenes declared in $MODULE_ABS" >&2; exit 1; }

echo "module    : $MODULE_ABS"
echo "scenes    : ${SCENES[*]}"
echo "format    : ${WIDTH}x${HEIGHT} @ ${FPS}fps, H.264 / yuv420p, no audio"
echo

CONCAT_LIST="$OUT/manim-scenes.txt"
: > "$CONCAT_LIST"

i=0
for SCENE in "${SCENES[@]}"; do
  NAME=$(printf '%02d-%s' "$i" "$SCENE")
  echo "[render] $NAME"
  "$PY" -m manim render \
    --renderer cairo \
    --format mp4 \
    --resolution "${WIDTH},${HEIGHT}" \
    --fps "$FPS" \
    --disable_caching \
    --media_dir "$MEDIA_DIR" \
    --output_file "$NAME" \
    "$MODULE_ABS" "$SCENE"

  CLIP=$(find "$MEDIA_DIR" -name "${NAME}.mp4" -type f -print -quit)
  [[ -n "$CLIP" ]] || { echo "render produced no ${NAME}.mp4 under $MEDIA_DIR" >&2; exit 1; }
  # Paths are adapter-local, never user content; single quotes are safe here for
  # the same reason pipeline/assemble_audio.py documents for its concat list.
  printf "file '%s'\n" "$CLIP" >> "$CONCAT_LIST"
  i=$((i + 1))
done

echo
echo "[concat] $CONCAT_LIST -> $OUT/manim.mp4"
# Every clip comes out of the same encoder with the same parameters, so a stream
# copy is exact: no generation loss, no re-timing.
ffmpeg -y -loglevel error -f concat -safe 0 -i "$CONCAT_LIST" -c copy "$OUT/manim.mp4"

echo
echo "scene         frames   seconds"
TOTAL=0
while read -r _ CLIP; do
  CLIP=${CLIP//\'/}
  # ffprobe emits csv fields in its own stream-entry order: duration, then packets.
  read -r DUR FRAMES < <(ffprobe -v error -select_streams v -count_packets \
    -show_entries stream=duration,nb_read_packets -of csv=p=0 "$CLIP" | tr ',' ' ')
  printf '%-14s %6s  %8.3f\n' "$(basename "$CLIP" .mp4)" "$FRAMES" "$DUR"
  TOTAL=$(awk -v a="$TOTAL" -v b="$DUR" 'BEGIN{printf "%.3f", a+b}')
done < "$CONCAT_LIST"

FULL=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT/manim.mp4")
printf '%-14s %6s  %8.3f\n' "(concatenated)" "-" "$FULL"

# The contract check. Without it the failure mode is a video that plays fine and
# drifts against its own narration — a dropped clip, a truncated scene or a
# missing lead-in all produce a valid MP4 and exit 0. Only meaningful when a
# durations file was supplied; the fallback path has nothing to check against.
if [[ -n "$DURATIONS" ]]; then
  EXPECTED=$("$PY" "$ADAPTER_DIR/contract.py" --total-length --fps "$FPS")
  echo
  printf '%-14s %6s  %8.3f\n' "(contract)" "-" "$EXPECTED"
  # One frame of tolerance: the mp4 container stores duration in a timescale
  # that need not divide evenly by the frame rate.
  if ! awk -v a="$FULL" -v e="$EXPECTED" -v f="$FPS" \
       'BEGIN{d=a-e; if(d<0)d=-d; exit (d <= 1.0/f + 0.002) ? 0 : 1}'; then
    echo >&2
    echo "FAIL: rendered ${FULL}s but the contract demands ${EXPECTED}s (lead-in + all scenes)." >&2
    echo "      The video would drift against the narration and the subtitles." >&2
    echo "      Check the per-scene table above for the scene that missed its budget." >&2
    exit 1
  fi
fi

echo
echo "MANIM_VIDEO: $OUT/manim.mp4"
echo "Next: bash ../../pipeline/encode.sh $OUT/manim.mp4 <work>/narration_full.wav <work>/subtitles.srt <out>.mp4"
