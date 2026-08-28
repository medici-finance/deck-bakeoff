# Manim renderer adapter — the animated-maths render path

An alternative **video track** for the `explainer-video` pipeline. Everything
else in the pipeline is unchanged: narration, audio assembly, subtitles and the
final mux stay exactly where they are. This adapter replaces one step —
recording — with an offline, deterministic render from
[Manim Community Edition](https://www.manim.community/) (MIT, Python).

```
gen_tts ─► assemble_audio ─┬─► SCENE_DURATIONS ─► [ HTML: inject + record.mjs ] ─┐
                           │                                                     ├─► encode.sh ─► .mp4
                           └─► SCENE_DURATIONS ─► [ THIS: scene-durations.json ] ─┘
                                                     render.sh → manim.mp4
```

## Why this exists

This is a **spike**, and it is meant to be judged, not adopted by default. The
question it answers is narrow: does a second, Python-based renderer earn the
setup cost it imposes? The case for it is one specific capability — **animated
mathematics**. Equations that transform term-by-term into other equations,
curves that morph continuously as a parameter moves, geometry that stays
correct because it is computed rather than hand-tweened. The house needs a
"maths behind the P/N split" video; `scenes/demo.py` is that scene, built.

Everything else Manim can do, the existing HTML/GSAP path already does at least
as well and usually faster. Read §Strengths and limits before adopting.

## Setup

Apple Silicon Mac. **Python 3.12 or 3.13** — Manim 0.20 publishes no wheels for
3.14, which is the current Homebrew `python3`.

```bash
cd tools/explainer-video/renderers/manim

brew install cairo pango pkgconf ffmpeg     # pycairo/manimpango build + link against these
python3.12 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt             # manim==0.20.1 + its stack

# On-brand typography (optional but strongly recommended — see below)
brew install --cask font-ibm-plex-sans font-ibm-plex-mono
```

The venv is local and gitignored, and it is deliberately **separate** from the
parent tool's `.venv`: Manim drags in numpy, scipy, moderngl, pycairo,
manimpango, skia-pathops and av — 336 MB of venv, none of which the TTS engine needs.

`medici_brand.py` warns, loudly and once, if IBM Plex is not installed and it
has to fall back to Helvetica Neue — a silent font fallback is the classic
"wrong fonts" failure, so this one is not silent. Rendering still works; the
output is just off-brand typographically.

**No LaTeX.** Manim's `MathTex` needs a TeX distribution and renders Computer
Modern, a serif — which breaks the brand's single-family rule (brand-guide
§3.1) as well as adding a multi-hundred-MB dependency. Formulas here are Pango
text in IBM Plex Mono, coloured per term (`medici_brand.formula`). Nothing in
this adapter requires TeX.

## Render

```bash
# Smoke render — 854x480 @ 15fps, ~5s
./render.sh -q l

# Deliverable — 1920x1080 @ 30fps
./render.sh -q h -d /path/to/scene-durations.json

# One scene, standalone, no pipeline run (uses the fallback durations)
. .venv/bin/activate && manim render -ql scenes/demo.py SplitMaths
```

`render.sh` prints a per-scene frame/second table and the concatenated total, so
a drift regression is visible in the run output rather than in the finished
video.

## The handoff contract

`render.sh` writes **one** file for the pipeline to consume:

| | |
|---|---|
| Path | `out/manim.mp4` (`-o` to change) |
| Container | MP4 |
| Video codec | H.264 (High profile), `yuv420p` — Manim's libx264 output, stream-copied |
| Resolution | 1920×1080 (`-q h`) / 854×480 (`-q l`) |
| Frame rate | 30 (`-q h`) / 15 (`-q l`), constant |
| Audio | **none** — the pipeline owns the audio track |
| Per-scene clips | `out/media/videos/<module>/<H>p<FPS>/NN-<SceneName>.mp4`, `NN` = 0-based scene index |
| Concat list | `out/manim-scenes.txt` (ffmpeg concat demuxer format) |

Hand it to the pipeline's existing encoder, unmodified:

```bash
bash ../../pipeline/encode.sh \
  out/manim.mp4 \
  <work>/narration_full.wav \
  <work>/subtitles.srt \
  <out>/<name>.mp4
```

`encode.sh`'s first parameter is named `WEBM` because the HTML path produces
webm, but it is only ever `ffmpeg -i`'d — an H.264 MP4 is accepted with no
change. The final mux re-encodes video with `h264_videotoolbox` regardless, so
the intermediate codec costs nothing downstream. Verified end-to-end: see
§What was actually rendered.

Scenes are concatenated with `-c copy`. Every clip comes out of the same encoder
with the same parameters, so the join is exact — no generation loss, no
re-timing.

## Scene-duration contract

The pipeline is authoritative about time. `pipeline/assemble_audio.py` measures
the rendered narration and prints

```
SCENE_DURATIONS [4.212, 10.017, 3.981]
```

one entry per scene in `SCRIPT.md` order, already including the inter-scene gap
(and the 1.0s tail on the last scene). The HTML path injects that array as
`window.SCENE_DURATIONS`; this path reads the same array as JSON.

**The lead-in.** `assemble_audio.py` also prepends `LEAD_S = 0.35` of silence
before scene 0's narration, and that lead is **not** part of any
`SCENE_DURATIONS` entry:

```
narration WAV = 0.35s silence | clip_0 | 0.15s | clip_1 | … | clip_n | 1.0s
total         = LEAD_S + sum(SCENE_DURATIONS)
```

`gen_subs.py` agrees — its first cue starts at 0.35s — and `encode.sh` muxes
video and audio at a common t=0 with no offset. So the video the renderer hands
over must be `lead_in + sum(durations)` long, with the first 0.35s spent holding
before scene 0's storyboard begins. A renderer that emits `sum(durations)` puts
every picture 0.35s ahead of its own narration and subtitles, from the first
frame to the last: a video that plays perfectly and is wrong throughout.

`BrandScene` spends the lead-in automatically at the top of the first scene's
`construct()` (see `pipeline_contract.BrandScene.__init_subclass__`) — it is a
property of the contract, not something each storyboard is asked to remember.
Override it per-run with `"lead_in"` in the durations file (`0` disables it);
the standalone-dev fallback path, which is never muxed, has no lead-in.

**Rules**

1. One `SCRIPT.md` row = one Manim `Scene` subclass = one entry in the module's
   `SCENE_ORDER` list, all in the same order.
2. Each scene declares `scene_index` (0-based) and `fallback_duration`.
3. The scene's budget is derived from the **cumulative** timeline: scene *i*
   owns frames `round((lead + T_i) · fps)` … `round((lead + T_{i+1}) · fps)` of
   the running sum. Each scene absorbs the previous scenes' rounding residue, so
   total error against the narration stays under half a frame however many
   scenes there are, instead of accumulating up to a frame per scene.
4. Every beat goes through `self.t(nominal_seconds)`, which scales the
   storyboard by `budget / fallback_duration` and snaps to whole frames. A
   scene authored against 10s still fits when the narration lands at 11.9s —
   every beat stretches proportionally rather than the tail growing a dead
   pause. `budget` is the narration window; the lead-in hold is *not* scaled
   into the storyboard.
5. `self.hold_to_end()` closes the scene, absorbing the remainder. It runs
   automatically after `construct()`, and calling it explicitly (as the demo
   does) stays correct. Over-run is a loud warning, never a silent truncation.
6. `render.sh` **asserts the concatenated length against the contract** and
   exits non-zero on a mismatch. A dropped clip, a truncated scene or a missing
   lead-in all produce a playable MP4 and would otherwise exit 0.

**Where the durations come from** (first hit wins):

1. `MEDICI_SCENE_DURATIONS` — a path, which `render.sh -d` sets.
2. `scene-durations.json` in the working directory.
3. `scene-durations.json` beside `contract.py`.
4. Nothing → each scene's `fallback_duration`, and no lead-in. This is the
   documented standalone-development path: `manim render -ql scenes/demo.py
   SplitMaths` works with no pipeline run at all.

**Writing the file** without touching anything under `pipeline/` — and without
a Manim install, since `contract.py` is stdlib-only:

```bash
# from a captured pipeline run
explainer-video --script … --slides … --profile … 2>&1 | tee assemble.log
python3 contract.py --from-log assemble.log \
  --scenes TitleCard,SplitMaths,ClosingCard --fps 30 --out scene-durations.json

# or by hand
python3 contract.py --durations 3.412,11.874,4.905 \
  --scenes TitleCard,SplitMaths,ClosingCard --fps 30
```

`pipeline_contract.py` accepts the same flags (it re-exports the CLI) and is
what you need for `--scene-order`, which imports the storyboard and therefore
needs Manim.

Accepted shapes: a bare array, or the object form in
`scene-durations.example.json`. When the object carries `scenes`, a scene
resolves **by name** first — so a reordered storyboard fails loudly with an
unknown name instead of quietly rendering against the wrong narration slot.

> **Not interchangeable with the Motion Canvas adapter's file.** Both renderers
> read a `scene-durations.json`, but this one's `scenes` key is an array of
> Manim `Scene` class *names* alongside a parallel `scene_durations` array,
> while `renderers/motion-canvas/` uses an array of `{id, duration}` objects and
> spells the lead-in `leadIn`. Cross-feeding fails closed on both sides (tested
> — each rejects the other with a named error rather than mis-timing a render),
> but the collision is a trap for whoever adopts the second renderer. If the
> orchestrator ever grows a `--renderer` flag, one shared shape is the fix.

## Testing

The timing arithmetic — the part that has to be right, because a frame-budget
bug yields a video that plays perfectly and drifts against its narration — lives
in `contract.py`, which imports nothing outside the standard library:

```bash
python3 -m unittest discover -s tools/explainer-video/renderers/manim/tests
```

No Manim, no cairo/pango, no ffmpeg, no venv. That is deliberate: gating these
checks on the heavy toolchain means they never run in CI, and a suite that skips
when its dependency is absent reports green while proving nothing. The
`lint / renderer-contract` job runs exactly this command.

What these tests do **not** cover, and nothing in CI does: the Manim render
itself, the brand module (fonts, colours, rate functions), scene layout, the
ffmpeg concat, and the `encode.sh` mux. Those need the full toolchain and are
verified by hand — see §What was actually rendered.

## Adopting it in a deck repo

Product content still lives in the deck repo (`medici-decks/video/`,
`reconciler-decks/video/`, `assay-decks/video/`); this repo stays tooling-only.
For a Manim-rendered video the deck repo supplies:

1. `video/SCRIPT.md` — unchanged, the same narration table the HTML path uses.
2. `video/scenes.py` (instead of `video/explainer.html`) — one `BrandScene`
   subclass per script row, plus `SCENE_ORDER` and `FALLBACK_DURATIONS`.
   Copy `scenes/demo.py` as the starting point.

Then:

```bash
# 1. narration + measured durations (unchanged pipeline, dry of the record step)
explainer-video --script ../../../medici-decks/video/SCRIPT.md \
                --slides  ../../../medici-decks/video/explainer.html \
                --profile australian-medici --out ./out 2>&1 | tee assemble.log

# 2. durations -> contract file
python pipeline_contract.py --from-log assemble.log --fps 30

# 3. video track
./render.sh -q h -m ../../../medici-decks/video/scenes.py -d scene-durations.json

# 4. mux with the pipeline's own encoder
bash ../../pipeline/encode.sh out/manim.mp4 \
     ./out/.work-medici-decks-australian-medici/narration_full.wav \
     ./out/.work-medici-decks-australian-medici/subtitles.srt \
     ./out/medici-decks-australian-medici.mp4
```

Steps 2–4 are what a `--renderer manim` flag on the `explainer-video` CLI would
automate. **That flag is not in this spike** — wiring it means editing the
orchestrator, and the point of the spike is to decide whether the toolchain is
worth keeping before touching the engine.

## What was actually rendered

Everything below was run on this machine (M-series Mac, macOS 26.5, ffmpeg
8.1.2, Python 3.12.13, manim 0.20.1) and the numbers are measured, not
estimated. IBM Plex was **not** installed, so the frames rendered in the
Helvetica Neue fallback with the warning firing as designed.

> **These figures predate the lead-in fix** and were measured against a video
> that started at scene 0 frame 0. The mux proof used synthetic silence cut to
> `sum(durations)` — which is exactly the audio file that *cannot* expose the
> 0.35s lead-in defect, since a real `narration_full.wav` is `LEAD_S` longer.
> The row that reads "+8ms total timing error" was true of the video against
> that stand-in and false of the video against a pipeline narration, where the
> error was 0.35s throughout. Re-measurement on a machine with the toolchain is
> owed; the arithmetic itself is now unit-tested (§Testing).

| Check | Result |
|---|---|
| `./render.sh -q l` (854×480@15) | 3/3 scenes, 18.000s total against 4+10+4 fallbacks |
| `./render.sh -q h -d scene-durations.json` (1920×1080@30) | 3/3 scenes, 606 frames, 20.199s, 727 KB, **13.6s wall** |
| Contract scaling | budgets 3.412/11.874/4.905 → 3.400/11.900/4.900 (frames 0–102, 102–459, 459–606) |
| Total timing error | +8ms on 20.191s of narration — under half a frame at 30fps |
| Stream params | `h264 (High) / yuv420p / 1920x1080 / 30fps`, no audio track |
| `pipeline/encode.sh` handoff | ran **unmodified** on `out/manim.mp4` + a 20.191s 48kHz stereo WAV + a 3-cue SRT → 3.3 MB MP4, `h264_videotoolbox` video + `aac` audio + `mov_text` soft subs, 1.5s |
| Over-budget guard | a deliberately over-running scene emitted `storyboard ran 1.533s OVER its 2.000s budget` and was **not** truncated |
| Font fallback guard | warned once per face: "IBM Plex Sans is not installed … Output is OFF-BRAND typographically" |

Not done, and not claimed: no run against real TTS narration (the audio used for
the mux proof was synthetic silence of the contract length), no `explainer-video
--renderer manim` CLI flag, no render on a machine that actually has IBM Plex
installed.

Verified without the toolchain (stdlib Python + ffmpeg only), after the fixes:

| Check | Result |
|---|---|
| `python3 -m unittest discover -s .../manim/tests` | 36 tests, exit 0 |
| Suite catches the defect it was written for | forcing `LEAD_IN_DEFAULT = 0.0` → 11 failures, exit 1 |
| `render.sh -o ./relative-dir` | exit 0 (pre-fix: exit 254, `Impossible to open 'out-pn/./out-pn/media/…'`) |
| Contract-length assertion | scene 0 rendered without its lead-in → `FAIL: rendered 18.000000s but the contract demands 18.333333s`, exit 1 |
| Frame partition | 130 + 300 + 120 = 550 frames = 18.333s for `[4.0, 10.0, 4.0]` + 0.35s lead at 30fps |

(The render step in those runs is an ffmpeg stand-in emitting clips of the
contracted length — it exercises `render.sh`'s plumbing and the assertion, not
Manim itself.)

## Strengths and limits vs the HTML/GSAP path

**Where Manim wins**

- *Animated mathematics.* `scenes/demo.py::SplitMaths` drives two piecewise
  payoff curves, a dashed reference line and its label off one `ValueTracker`.
  Move the strike, everything re-derives. In HTML that is a hand-written
  interpolation per element and a standing invitation for the curves to
  disagree with the caption.
- *Term-level equation transforms.* `TransformMatchingShapes` morphs
  `S = P + N` into `S = min(S, K) + max(S − K, 0)` glyph-by-glyph. The DOM
  equivalent is a per-glyph FLIP animation someone has to maintain.
- *Determinism.* Frame-accurate, offline, no browser. The same input renders the
  same bytes; the recorder path is subject to real-time browser scheduling.
- *Faster than real time.* 20.2s of 1080p30 rendered in 13.6s. `record.mjs` is
  1× real time by construction, plus browser launch — a five-minute video costs
  five minutes every take.
- *Exact per-scene lengths.* Each scene is its own clip cut to its own frame
  budget, so a narration re-record only re-renders the scenes that changed.

**Where it loses**

- *A second toolchain.* Python 3.12 pin, a second venv, `brew` deps for cairo
  and pango, 336 MB installed. That is real, permanent maintenance surface for
  a repo whose slides are otherwise HTML.
- *No visual iteration loop.* HTML slides open in a browser and reload. Manim
  compiles to video; a preview of one scene at `-ql` is ~2–5 seconds, which is
  fast for a renderer and slow next to a page refresh.
- *Layout is code.* No flexbox, no grid, no devtools. Collisions between a
  legend, a caption and a plot are solved by nudging scene-unit offsets and
  re-rendering — the exact thing CSS is good at. Two of the three layout fixes
  in this spike were of that kind.
- *Typography is thinner.* Pango via `Text`, no tracking control (the eyebrow's
  letter-spacing is faked with thin spaces), no OpenType feature access, no
  `tabular-nums`. `MathTex` would help, at the cost of LaTeX and an off-brand
  serif.
- *Brand assets do not transfer.* The logo SVG, the whitepaper CSS and the deck
  components are all HTML/CSS. `medici_brand.py` is a **re-implementation** of
  the brand for a second engine — a second place for the brand to drift.
- *Narrow payoff.* For a title card, a bullet build or a screenshot walkthrough,
  Manim is strictly more work than HTML for a worse result.

**The honest read.** Manim earns its keep for maths-heavy scenes and nothing
else. The strongest adoption shape is a **hybrid** — HTML for the talking
slides, Manim for the two or three scenes that animate an equation or a curve,
concatenated at the video-track level (both paths already hand `encode.sh` a
single video file, so this costs one more concat). Adopting Manim as *the*
renderer would trade a good tool for slides for a great tool for graphs.

## Layout

```
renderers/manim/
├── README.md                     # this file
├── requirements.txt              # manim==0.20.1 (own venv, gitignored)
├── render.sh                     # render all scenes -> out/manim.mp4
├── medici_brand.py               # white canvas, #3366FF accent, type, motion, chart tokens
├── contract.py                   # timing arithmetic + scene-durations CLI (stdlib only)
├── pipeline_contract.py          # BrandScene base, on top of contract.py (needs Manim)
├── scene-durations.example.json  # the contract file's shape
├── scenes/
│   └── demo.py                   # 3-scene demo: title / P-N maths / closing
└── tests/
    └── test_contract.py          # unit tests for contract.py — no Manim, CI-gated
```

The `contract.py` / `pipeline_contract.py` split is what makes the timing
testable: everything that can be checked without rendering a frame lives on the
stdlib side of the line.

`medici_brand.py` transcribes the canonical brand reference
(`option-index-tracker/docs/brand-guide.md`) — §2.4 light-surface palette, §3
typography, §7.2 chart rules, §9.1 motion. Section numbers are cited inline next
to each token so the two can be diffed when the guide moves.
