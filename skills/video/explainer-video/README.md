# explainer-video

Productized pipeline for rendering branded ~2-minute explainer videos with a
local neural voice-over on Apple Silicon. **This directory is the tooling/engine
only** — it contains no product scripts or slides.

The per-product content (the narration `SCRIPT.md` and the self-contained,
branded `explainer.html` slides) lives in each product's **deck repo**, under a
`video/` dir, and is passed to the tool as input paths:

| Product | Deck repo | Content dir |
|---------|-----------|-------------|
| Medici  | `medici-decks`    | `video/` |
| Plumb   | `reconciler-decks`| `video/` |
| Assay   | `assay-decks`     | `video/` |

The rendered `.mp4` is generated output — it is **not committed** to this repo or
the deck repos; it is uploaded wherever the video is published.

**Designing the video** (mission → script → storyboard → scene grammar → VO sync
→ chart/brand judgment) is the narrative layer above this engine: see the
`video-design` skill (`.claude/skills/video-design/SKILL.md`). This README covers
the pipeline mechanics; the skill covers the direction.

## What it does

`explainer-video --script … --slides … --profile …` runs, as a thin wrapper over
`pipeline/*`:

1. **gen_tts** — one narration clip per scene via MLX-Audio, using the chosen
   voice profile (Qwen3-TTS voice-clone / Orpheus / Kokoro).
2. **assemble_audio** — concat with lead-in + inter-scene gaps + tail, then
   loudness-normalize to 48kHz stereo / −16 LUFS; emits `SCENE_DURATIONS`.
3. **inject** — writes `window.SCENE_DURATIONS` into a copy of the slides so the
   animation timeline stays synced to the measured narration.
4. **record.mjs** — Playwright records the slides to 1920×1080 webm in real time
   (stops on `document.body.dataset.done === "1"`).
5. **gen_subs** — soft subtitles (`.srt` + `.vtt`) from the measured clip lengths.
6. **encode.sh** — hardware H.264 mux (`h264_videotoolbox`) → `out/<name>.mp4`,
   plus a YouTube-ready `out/<name>.description.txt` when the
   `SCRIPT.md` carries a `## Description` section.

Output: `out/<name>.mp4` (e.g.
`out/the-assay-office-for-agent-fleet-software-work.mp4`).
On a successful encode, the `.vtt` subtitles land alongside it (`out/<name>.vtt`, same stem) for web players' `<track>` elements, and — when the
`SCRIPT.md` has a `## Description` section — so does
`out/<name>.description.txt` (same stem): the verbatim section body,
ready to paste into the YouTube description field. A script without the
section renders exactly as before; the tool prints a one-line notice and emits
no `.txt`.

The delivered filenames carry `<name>` **only** — the voice/profile is *not* in
the name. The voice lives on the internal scratch dir instead
(`out/.work-<name>-<profile>/`), which keeps concurrent renders of the same
article in different voices from colliding mid-render. Two voices written into
the **same** `--out`, though, resolve to the same delivered `<name>.mp4` and so
overwrite (last render wins) — exactly as re-running one profile already
overwrites its own output. To keep both, give each voice its own `--out`.

`<name>` defaults to the **slugified first `# ` heading of the `SCRIPT.md`**,
capped at 100 characters. It used to default to the deck repo's directory name
(`medici-decks`, `assay-decks`), so output paths changed — anything pinning the
old filename (a docs link, a publish step, a cached artifact) needs updating, or
pass `--name medici-decks` to keep the previous name. `--name` must be a single
filename component: no `/` and no `..`, since it also names the work directory
that each run deletes recursively. A script with no `# ` heading, or one whose
title slugifies to nothing (`# !!!`), falls back to the deck directory name.

The MP4 also carries metadata: `title` (the raw heading), `comment` (whatever
`--url` is given, e.g. `--url https://assay.finance`), and `date` (the run's UTC
timestamp). When a `## Description` is present its body is additionally
embedded as the mp4's `description`/`synopsis` metadata — best-effort (players
vary in how they surface multi-line metadata); the `.description.txt` is the
canonical cut-and-paste artifact.

## Setup

Apple-Silicon Mac (M-series). One-time:

```bash
cd tools/explainer-video

# Python: venv + MLX-Audio (Qwen3-TTS / Orpheus / Kokoro) + PyYAML
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# espeak-ng (phonemizer backend some MLX-Audio models need) + ffmpeg
brew install espeak-ng ffmpeg

# Node + Playwright (Chromium) for the recorder
npm install
npx playwright install chromium
```

Model weights download to the Hugging Face cache on first run (gitignored, never
committed).

## Generate

Regenerate the **Medici** video with the populated **australian-medici** profile:

```bash
. .venv/bin/activate
./explainer-video \
  --script ../../../medici-decks/video/SCRIPT.md \
  --slides ../../../medici-decks/video/explainer.html \
  --profile australian-medici \
  --out ./out
```

(Adjust the `../medici-decks` path to wherever the deck repo is checked out.)

Preview the plan without running anything (parses the script, resolves the
profile, prints the scene list + output path):

```bash
./explainer-video --script … --slides … --profile australian-medici --dry-run
```

Or skip the registry and use a US-accent **Orpheus** built-in voice
(`tara`, `leah`, `jess`, `leo`, `dan`, `mia`, `zac`, `zoe` — bare `--us-voice`
selects `leo`):

```bash
./explainer-video \
  --script ../../../medici-decks/video/SCRIPT.md \
  --slides ../../../medici-decks/video/explainer.html \
  --us-voice leo \
  --out ./out
```

### The exact hardware-encode

The final mux uses the Apple-Silicon hardware encoder — **seconds**, not the
>1hr `libx264 -preset slow` path. `encode.sh` runs, verbatim:

```bash
ffmpeg -y -i <webm> -i <narration.wav> -i <subtitles.srt> \
  -map 0:v:0 -map 1:a:0 -map 2:s:0 \
  -c:v h264_videotoolbox -b:v 10M -pix_fmt yuv420p \
  -c:a aac -b:a 192k -c:s mov_text -movflags +faststart \
  out/<name>.mp4
```

## Voice profiles — the `<accent>-<product>[-<gender>]` scheme

Profiles live in [`voices/registry.yaml`](voices/registry.yaml), named
`<accent>-<product>` with an optional trailing `-<gender>` qualifier (e.g.
`australian-medici`, `english-medici-female`; no suffix means
male/unspecified). Each maps to an engine, model, voice-clone reference clip,
and params.

| Profile | Status | Engine | Reference |
|---------|--------|--------|-----------|
| `australian-medici`     | **populated** | qwen (Qwen3-TTS clone) | `voices/australian-medici/assay-au-us.wav` |
| `english-medici`        | **populated** | qwen (Qwen3-TTS clone) | `voices/english-medici/medici-british-male.wav` |
| `english-medici-female` | **populated** | qwen (Qwen3-TTS clone) | `voices/english-medici-female/medici-british-female.wav` |
| `australian-plumb`      | **populated** | qwen (Qwen3-TTS clone) | `voices/australian-plumb/reconciler-australian.wav` (Plumb == reconciler) |
| `english-plumb`         | **populated** | qwen (Qwen3-TTS clone) | `voices/english-plumb/reconciler-british.wav` |
| `australian-assay`      | **populated** | qwen (Qwen3-TTS clone) | `voices/australian-assay/assay-australian.wav` |
| `english-assay`         | **populated** | qwen (Qwen3-TTS clone) | `voices/english-assay/assay-british.wav` |

All 7 profiles are populated Qwen3-TTS voice clones: MLX-Audio + Qwen3-TTS-12Hz-1.7B
(`mlx-community/Qwen3-TTS-12Hz-1.7B-Base-bf16`), each cloned from a committed
reference `.wav` + transcript, `--max_tokens 4096`. `gen_tts.py` also supports
`orpheus` and `kokoro` engines (built-in presets, no reference clip needed);
none of the current profiles use them, but they remain available for future
no-reference profiles — see `pipeline/alternates/README.md`.

The `--us-voice <name>` flag renders via the Orpheus-3b built-in voices with
**no registry entry** — the profile is synthesized in memory as
`us-orpheus-<name>` (engine `orpheus`, model
`mlx-community/orpheus-3b-0.1-ft-bf16`); output is
`out/<name>-us-orpheus-<voice>.mp4`.

> **Gotcha:** `mlx_audio.tts.generate` defaults to `--max_tokens 1200` (~14.6s),
> which silently truncates long scenes. The qwen profiles set `max_tokens: 4096`;
> `gen_tts.py` flags any clip whose duration lands suspiciously near the cap.

## Voice provenance & licence

All 7 voice-clone reference clips are sourced from **Mozilla Common Voice**
(commonvoice.mozilla.org) — CC0 / public domain — per project-owner
confirmation. Each is a **single CC0-dedicated speaker clip**: a voice-clone
reference carries one speaker's timbre, so it cannot be (and none of these
are) a blend of multiple speakers; there is no individual-consent concern
because the source dedication is CC0.

The committed `.txt` alongside each `.wav` is the Qwen `ref_text`
conditioning string used to drive the clone — **not** a claim that its
content is itself a Common Voice sentence (one profile's `.txt`, for
example, mixes Snips-NLU and Flickr-caption style lines; that's expected
for a `ref_text` string and doesn't bear on the CC0 status of the audio).

Per-profile detail lives in each `voices/<profile>/README.md` and in
`voices/registry.yaml` `notes:`.

The ~19 MB of reference `.wav` files are committed **directly to git** (they
are write-once CC0 references, not generated output). Git-LFS is a future
option if the voice-profile library grows significantly; not needed today.

### Add a voice profile

1. Record a clean **20–40s** reference clip of the target speaker.
2. Prep it (24kHz mono, trim, normalize):
   ```bash
   python pipeline/prep_voice.py input.m4a -o voices/<accent>-<product>/ref.wav
   ```
3. Save the exact transcript as `voices/<accent>-<product>/ref.txt`.
4. Add an entry to `voices/registry.yaml`:
   ```yaml
   <accent>-<product>:
     engine: qwen
     model: mlx-community/Qwen3-TTS-12Hz-1.7B-Base-bf16
     ref_audio: ref.wav
     ref_text_file: ref.txt
     params: { max_tokens: 4096 }
   ```

All current profiles use `qwen` voice clones. For a new profile without a
reference clip yet, `kokoro`/`orpheus` built-in presets (e.g. Kokoro's
`bm_george` British-male neural voice) remain available as a no-reference
fallback — usable immediately, upgrade to a `qwen` clone once a reference
clip exists.

## Add a product (video)

Products are pluggable: a product's video is just a `SCRIPT.md` + a branded
`explainer.html`, authored in that product's **deck repo** under `video/`. To
add one, create `video/SCRIPT.md` and `video/explainer.html` in the deck repo,
then point the tool at them. Nothing product-specific is added here.

### `SCRIPT.md` format (the tool's input contract)

A Markdown table with a header row containing **`id`**, **`narration`**, and
optionally **`subtitle`** columns (matched case-insensitively). One row per
scene, in order. Surrounding quotes and `**bold**` are stripped. When there is
no `subtitle` column, the narration is reused as the subtitle.

```markdown
| # | id    | narration                                   | subtitle                     |
|---|-------|---------------------------------------------|------------------------------|
| 1 | title | "Every DeFi platform shares one flaw …"     | No liquidations. By design.  |
| 2 | …     | …                                           | …                            |
```

Optionally, a `## Description` H2 section anywhere in the same file. Its
verbatim body — everything until the next `## ` heading or EOF, stripped of
leading/trailing blank lines — becomes `out/<name>.description.txt`
and the mp4's `description`/`synopsis` metadata. It is authored prose (the
YouTube description), never generated from the scenes table:

```markdown
## Description

Assay is the assay office for agent-fleet software work: every claim is
weighed before it ships.

Learn more: https://assay.finance
```

Omitting the section is fine — the render is unchanged and no `.txt` is
emitted (`--dry-run` reports which case you're in, with a character count).

### `explainer.html` requirements

Self-contained (inline CSS/JS, base64 fonts, inline logo — no external fetches).
It must:
- read `window.SCENE_DURATIONS` (an array, one entry per scene) to drive its
  animation timeline — the tool injects this before recording;
- set `document.body.dataset.done = "1"` when the timeline finishes, so
  `record.mjs` knows when to stop;
- have exactly as many scenes as the `SCRIPT.md` table has rows.

Brand references for building product slides: Medici →
`option-index-tracker/docs/brand-guide.md`, Plumb → `reconciler/docs/brand.md`,
Assay → `assay-toolkit/docs/brand/brand.md`.

## Layout

```
tools/explainer-video/
├── explainer-video          # CLI orchestrator (thin wrapper) — the render ENGINE
├── fetch-and-render         # pull bundles from PR(s) — SCRIPT.md/explainer.html + optional index.html/cover.png — + fire the engine; renders default to ~/Downloads/videos (see fetch-and-render.md)
├── fetch-and-render.md      # docs for the above
├── requirements.txt         # PyYAML + mlx-audio
├── package.json             # playwright (recorder)
├── pipeline/
│   ├── lib.py               # registry load + SCRIPT.md parse + run context
│   ├── gen_tts.py           # parameterized generator (qwen/orpheus/kokoro)
│   ├── assemble_audio.py    # concat + loudnorm, emits SCENE_DURATIONS
│   ├── gen_subs.py          # srt/vtt from measured clip lengths
│   ├── record.mjs           # Playwright recorder -> webm
│   ├── encode.sh            # hardware h264_videotoolbox mux
│   ├── prep_voice.py        # prep a new reference clip for cloning
│   └── alternates/          # standalone reference scripts (orpheus, the original winning qwen)
└── voices/
    ├── registry.yaml        # <accent>-<product>[-<gender>] profiles, all 7 POPULATED
    └── {australian-medici,english-medici,english-medici-female,
        australian-plumb,english-plumb,australian-assay,english-assay}/
        # each: cloned ref .wav + .txt + README.md (provenance + regen command)
```
