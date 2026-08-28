# Alternate engines (reference only)

The productized tool drives TTS through `pipeline/gen_tts.py`, which selects the
engine from the voice profile in `voices/registry.yaml`. The scripts here are
**preserved standalone references** for the two non-default engines and for the
original winning run. They are not on the tool's code path.

| File | What it is |
|------|-----------|
| `gen_qwen_aussie.py` | The original winning generator, verbatim — Qwen3-TTS-12Hz-1.7B, Aussie voice clone, with the 8 medici scene texts embedded. `gen_tts.py` is its parameterized generalization (scenes come from the product `SCRIPT.md` instead of being baked in). Kept for provenance. |
| `gen_orpheus.py` | Orpheus-3b, built-in `leo` voice, no reference clip. Equivalent to a `engine: orpheus` profile. |

## Kokoro (no-reference neural fallback)

There is no standalone Kokoro script — it runs through the same
`mlx_audio.tts.generate` path as the others, so `gen_tts.py` handles it directly
when a profile sets `engine: kokoro`. All 7 current profiles in
`voices/registry.yaml` are populated `qwen` voice clones, so no profile uses
`kokoro` today; it (along with `orpheus`) remains available as a no-reference
fallback for a future profile added before a real reference clip is recorded,
e.g. `voice: bm_george` (British male).

```bash
python -m mlx_audio.tts.generate \
  --model mlx-community/Kokoro-82M-bf16 --voice bm_george \
  --text "..." --output_path ./out
```
