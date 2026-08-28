# Motion Canvas renderer adapter

A **spike**: an alternative video track for `tools/explainer-video`, rendered
offline and deterministically by [Motion Canvas](https://motioncanvas.io) (MIT)
instead of recorded in real time by Playwright.

It exists to answer one question — *does Motion Canvas earn a place in this
pipeline?* — so read the [Limits and DX](#limits-and-dx-the-honest-part) section
before adopting it. Nothing under `pipeline/` is modified, and the default
`explainer-video` flow is untouched.

---

## What it replaces, and what it does not

The engine is six steps; this adapter swaps **exactly one**:

| # | Step | Owner |
|---|------|-------|
| 1 | `gen_tts` — per-scene narration clips | unchanged |
| 2 | `assemble_audio` — concat + loudnorm, emits `SCENE_DURATIONS` | unchanged |
| 3 | `inject` — `window.SCENE_DURATIONS` into the slides | **not used** (see below) |
| 4 | `record.mjs` — Playwright real-time recording → webm | **replaced** by `render.mjs` |
| 5 | `gen_subs` — `.srt` / `.vtt` from measured clip lengths | unchanged |
| 6 | `encode.sh` — `h264_videotoolbox` mux | unchanged |

Step 3 disappears because there is no HTML page to inject into: the scenes are
TypeScript, and the measured durations reach them through the
[scene-duration contract](#scene-duration-contract) instead.

### Why deviate from `record.mjs`

`record.mjs` opens `explainer.html` in Chromium and records it **in real time**,
stopping when the page sets `data-done="1"`. That has four costs this adapter
does not pay:

1. **Wall clock in the loop.** A 2-minute video takes 2 minutes to record, every
   time, and a busy machine can drop frames mid-record. Motion Canvas renders
   frame-by-frame as fast as the CPU allows — the 16.4s demo renders in ~7s, and
   the output does not depend on how loaded the machine was.
2. **Non-determinism.** Two recordings of the same page are not byte-identical:
   frame pacing, `requestAnimationFrame` jitter and the WebM encoder all vary.
   Two runs of this adapter produce **byte-identical PNG sequences** (verified —
   see [Smoke run](#smoke-run)). That makes "did my change alter the picture?" a
   `shasum` away, and makes a regression diff meaningful.
3. **Choreography cost.** Draw-on strokes, staged reveals and timeline scaling
   are hand-rolled CSS keyframes plus a `stroke-dashoffset` trick in the HTML
   path. Here they are `line.end(1, seconds, easing)` and a generator that reads
   top-to-bottom in the order the viewer sees it.
4. **Frame rate is implicit.** The recorder's fps is whatever Playwright chose
   (25). Here it is an argument, and it is quantized against the audio (below).

What is *lost*: the slides stop being a self-contained, openable
`explainer.html`. There is no "open it in a browser and look" artefact and no
CSS; a designer who is comfortable in HTML now needs TypeScript. That is the
real trade, and it is the thing to weigh.

---

## Scene-duration contract

The pipeline measures narration **first**, then the picture is stretched to fit.
One `SCRIPT.md` row = one narration clip = one Motion Canvas scene.

### The pipeline's numbers

From `pipeline/assemble_audio.py` and `pipeline/gen_subs.py`:

```
LEAD_S = 0.35   silence before scene 1's narration
GAP_S  = 0.15   silence after every scene except the last
TAIL_S = 1.00   silence after the last scene

SCENE_DURATIONS[i] = raw_clip_i + (i is last ? TAIL_S : GAP_S)
total audio        = LEAD_S + sum(SCENE_DURATIONS)
```

`LEAD_S` is **not** part of any `SCENE_DURATIONS` entry. The rendered video must
therefore be `leadIn + sum(durations)` long, and `pipelineScene()` spends the
lead-in holding scene 1's initial state so the first frame of motion coincides
with the first word of narration.

### The file

`render.mjs --durations <file>` (or a `scene-durations.json` sitting in this
directory) is read at Vite **config** time and frozen into the bundle as
`__PIPELINE_TIMING__` — scenes run in a browser and cannot read the filesystem.

```json
{
  "leadIn": 0.35,
  "fps": 30,
  "scenes": [
    {"id": "title",   "duration": 5.912},
    {"id": "flow",    "duration": 11.204},
    {"id": "closing", "duration": 6.331}
  ]
}
```

A bare array (`[4.0, 8.0, 4.0]`) is also accepted and matched **positionally**
against `src/scene-order.ts`. When ids *are* present they are authoritative:
they are reordered into `SCENE_ORDER`, and a mismatch is a hard error, because
a silently-shifted scene plays the right picture under the wrong words.

Guardrails, all of which fail the render immediately with a named cause:

- ids present but not equal to `SCENE_ORDER` → `ids do not match src/scene-order.ts`
- wrong number of durations → `got N durations but src/scene-order.ts declares M`
- a non-positive / non-numeric duration → `entry N has no usable positive duration`
- `--durations` path missing → `--durations file not found`

This also means the Manim adapter's `scene-durations.json` (same filename, but
`scenes` is an array of scene *names* alongside a parallel `durations` array) is
rejected here rather than half-read: it trips the third guardrail with
`entry 0 has no usable positive duration (got "TitleCard")`. Verified by feeding
one in. See "Limits" for the schema divergence itself.

### Output guardrails (no green exit on a short video)

The two ways a render can *succeed* and still hand `encode.sh` something wrong,
both checked before `RENDERED:` is printed:

- **A gap in the PNG sequence.** ffmpeg's image2 demuxer walks `%06d.png` from
  `-start_number`, stops at the first missing index, **and still exits 0**.
  Measured: deleting frame `000250` of a 492-frame sequence yields an ffmpeg exit
  code of 0 and an 8.333s / 250-frame mp4 — half a video, from a green run, which
  would then be muxed against full-length narration. `render.mjs` asserts the
  sequence is contiguous and names the missing frame.
- **A frame count that does not survive the encode.** After ffmpeg, `ffprobe
  -count_frames` reads the count back out of the file that actually leaves this
  script and requires it to equal the number of PNGs rendered. The `frames=` and
  `duration=` lines in the banner are that verified count, not the on-disk tally.

Both exit 1 and leave no output file. The rule they encode: **this adapter never
reports success on work it did not do.**

**Standalone dev fallback:** with no file resolved, `src/timing.ts` uses
`DEV_FALLBACK = [4, 8, 4]`, so `npm run dev` and a bare `node render.mjs` both
work with nothing but this directory. The render log always states which source
it used (`measured (pipeline)` vs `DEV_FALLBACK`) — never guess.

### Building the file from a pipeline run

`make-durations.mjs` scrapes the `SCENE_DURATIONS [...]` line the pipeline
already prints. It reads the pipeline's *output*; it imports nothing from
`pipeline/`.

```bash
./explainer-video --script …/video/SCRIPT.md --slides …/video/explainer.html \
  --profile australian-medici --out ./out 2>&1 | tee run.log

node renderers/motion-canvas/make-durations.mjs \
  --log run.log --script …/video/SCRIPT.md \
  --out renderers/motion-canvas/scene-durations.json
```

### Writing a scene against it

```ts
export default makeScene2D(
  pipelineScene('title', 4, function* (view, t) {
    //                ^id   ^nominal seconds the choreography was authored for
    yield* card.reveal(t(beat.base));
    yield* waitFor(t(beat.hold));
  }),
);
```

`t(x)` scales a nominal second into a real one (`x * measured / nominal`), so a
scene authored at 4s plays correctly when the narration comes back at 6.3s.
`pipelineScene` then pads to the exact frame budget, and **warns** (in the
render log) if the body overran it.

> **Rule:** every duration inside the body goes through `t()`. A raw
> `waitFor(2)` does not stretch — the scene's internal proportions drift as
> narration length changes, and the trailing pad silently swallows the
> difference.

### Frame quantization

A renderer can only end a scene on a frame boundary. Rounding each scene
independently lets the error *accumulate* — twelve scenes rounded up is twelve
frames the narration never paid for. `src/timing.ts` instead rounds the
**cumulative boundary** (the absolute timestamp at which each scene ends) and
takes each scene's budget as the difference between consecutive rounded
boundaries. Per-scene error stays under half a frame and never compounds.

`render.mjs` reports the residual as `drift` and warns above ±2 frames.

---

## Headless render path

**One path, and it is the one that works here:** Vite dev server in-process →
headless Chromium → `@motion-canvas/core`'s `Renderer` driven directly →
PNG sequence → ffmpeg.

Why this and not the alternatives:

- **Not `@motion-canvas/ffmpeg`.** It would remove the ffmpeg step, but it adds
  an `ffmpeg-static` binary download to a repo that already requires
  `brew install ffmpeg`, and it hands back an opaque mp4 instead of the frames.
  The PNG sequence is worth keeping: it is what makes the byte-identical
  determinism check possible, and `--keep-frames` gives you a still of any
  moment for free.
- **Not the editor UI.** Motion Canvas's render button lives in a preact
  component. Clicking it with Playwright means automating someone else's DOM.
  `Renderer` is the class that button drives, so `src/render-entry.ts` drives it
  directly and exposes `window.__mc.render()`.
- **Dev server, not `vite build`.** Motion Canvas's `ImageExporter` ships each
  frame over Vite's HMR socket (`motion-canvas:export`); the vite-plugin writes
  it to disk. The exporter is gated on `import.meta.hot`, which only exists in
  dev. This is a real constraint of the library, not a preference.

### Handoff contract

`render.mjs` writes **one video file, video only** — no audio, no subtitles:

| Property | Value |
|----------|-------|
| Container / codec | `.mp4` / H.264 `libx264 -crf 10 -preset veryfast -pix_fmt yuv420p` (default) |
| Alternative | `--codec prores` → `prores_ks -profile:v 3 -pix_fmt yuv422p10le` |
| Frame rate | `--fps`, default 30, or the `fps` pinned in the durations file |
| Size | `--width`/`--height`, default 1920×1080 |
| Path | `--out`, default `./out/video.mp4` |
| Intermediate frames | `output/explainer/%06d.png`, zero-padded to 6, starting at `000000` (deleted unless `--keep-frames`) |

It goes into `encode.sh` in the slot that used to hold the recorder's webm —
`encode.sh` takes any container ffmpeg can read and does not pass `-r`, so the
final mp4 **inherits this file's fps**:

```bash
bash pipeline/encode.sh \
  renderers/motion-canvas/out/video.mp4 \
  out/.work-…/narration_full.wav \
  out/.work-…/subtitles.srt \
  out/medici-decks-australian-medici.mp4
```

Verified end-to-end (see below): the resulting mp4 carries h264 @ 30fps + aac +
`mov_text`, exactly as the recorder path produces.

---

## Smoke run

Prerequisites: Node 20+, `ffmpeg` on PATH, and Playwright's Chromium
(`npx playwright install chromium`).

```bash
cd tools/explainer-video/renderers/motion-canvas
npm install

# 1. Render the 3-scene demo on the [4, 8, 4] fallback (~7s)
node render.mjs --out ./out/demo.mp4 --keep-frames
#   → [render] timing source: DEV_FALLBACK; expected 16.350s
#   → [render] 492 frames on disk (expected ~491, drift +1)
#   → RENDERED: …/out/demo.mp4   fps=30 size=1920x1080 frames=492

# 2. Render against measured durations
node render.mjs --durations ./scene-durations.example.json --out ./out/measured.mp4

# 3. Prove determinism — two runs, identical bytes
node render.mjs --out ./out/a.mp4 --keep-frames && (cd output/explainer && cat *.png | shasum -a 256)
rm -rf output
node render.mjs --out ./out/b.mp4 --keep-frames && (cd output/explainer && cat *.png | shasum -a 256)
shasum -a 256 out/a.mp4 out/b.mp4      # both hashes match

# 4. Prove the handoff — mux with silence + stub subs through the real encoder
ffmpeg -y -f lavfi -i "anullsrc=r=48000:cl=stereo" -t 16.35 /tmp/silence.wav
printf '1\n00:00:00,350 --> 00:00:04,350\nhello\n' > /tmp/stub.srt
bash ../../pipeline/encode.sh ./out/demo.mp4 /tmp/silence.wav /tmp/stub.srt /tmp/final.mp4
ffprobe -v error -show_entries stream=codec_name,avg_frame_rate /tmp/final.mp4

# 5. Interactive authoring (Motion Canvas editor, scrubbable timeline)
npm run dev            # → http://localhost:9000

# 6. Typecheck
npm run typecheck
```

---

## Adopting it in a deck repo

A deck repo's `video/` dir today holds `SCRIPT.md` + `explainer.html`. To render
that video through Motion Canvas instead:

1. **Keep `SCRIPT.md` exactly as it is.** It is still the source of narration,
   subtitles and scene order. `explainer.html` becomes unused for this render.
2. **List the scene ids** in `src/scene-order.ts`, in `SCRIPT.md` row order.
   The ids must be the `id` column values.
3. **Write one scene per row** in `src/scenes/<id>.tsx`, each wrapped in
   `pipelineScene('<id>', <nominal seconds>, …)`, and register them in
   `src/project.ts` in the same order. `project.ts` asserts the counts agree.
4. **Style from `src/brand.tsx` only.** Import `whiteStage`, `ease`, `beat`,
   `type`, `TitleCard`, `LowerThird` — do not hand-pick hex values in a scene.
   Product brand facts live in `option-index-tracker/docs/brand-guide.md`
   (Medici), `reconciler/docs/brand.md` (Plumb),
   `assay-toolkit/docs/brand/brand.md` (Assay).
5. **Run the pipeline to get durations**, build `scene-durations.json` with
   `make-durations.mjs`, render, and mux with `encode.sh` (recipe above).

Open question for adoption (see the PR): this directory currently holds **one**
project. Three products means either three `src/` trees behind a
`--project` switch, or one renderer directory per deck repo importing a shared
`brand.tsx`. The spike does not decide that.

### Brand rules this encodes

- **One accent, `#3366FF`, sparingly.** `brand.tsx` exposes a single `accent`
  plus a wash and a muted variant; a scene that wants a second accent is doing
  something the brand does not allow.
- **White surfaces.** `whiteStage` is the default and all three demo scenes use
  it. `darkStage` exists for a deliberate inverted card; the demo does not spend
  it.
- **No spring, bounce, elastic or overshoot.** `ease` is the only easing surface
  scenes import, and it exposes exactly `enter / exit / move / reveal / fade /
  linear` (cubic and quad, plus `linear`). `FORBIDDEN_EASINGS` names the banned
  set as data so a reviewer can grep for it:
  `grep -rE 'Back|Elastic|Bounce|spring' src/scenes/` must come back empty.
- **Small travel.** `RISE = 24px`. Things fade and settle; they do not fly.

---

## Layout

```
renderers/motion-canvas/
├── render.mjs                 # headless render driver (vite + playwright + ffmpeg)
├── make-durations.mjs         # pipeline log -> scene-durations.json
├── render-entry.html          # headless entry page (NOT the editor)
├── vite.config.ts             # motion-canvas plugin + __PIPELINE_TIMING__ define
├── scene-durations.example.json
├── env.d.ts                   # ambient decls for ?scene / ?project / __PIPELINE_TIMING__
└── src/
    ├── project.ts             # scene registration (+ order assertion)
    ├── scene-order.ts         # the join key: SCRIPT.md <-> durations <-> scenes
    ├── timing.ts              # duration contract, frame-boundary quantization
    ├── pipeline-scene.ts      # pipelineScene() — lead-in, t() scaling, pad/warn
    ├── brand.tsx              # tokens, stages, easings, TitleCard, LowerThird
    ├── render-entry.ts        # drives core's Renderer; window.__mc
    ├── *.meta                 # project settings — COMMITTED
    └── scenes/
        ├── title.tsx          # title card
        ├── flow.tsx           # three labelled boxes + drawn flows
        └── closing.tsx        # closing card
```

`src/*.meta` and `src/scenes/*.meta` are generated by the vite plugin on first
run and **are committed on purpose**: they carry each scene's random seed, which
is what makes `useRandom()` reproduce across machines.

---

## Limits and DX (the honest part)

**What was actually rendered.** All numbers in this README come from real runs
on an Apple-Silicon Mac (Node 26.5.1, ffmpeg 8.1.2, Motion Canvas 3.17.2,
Playwright Chromium): the 3-scene demo at 30fps on the fallback durations
(492 frames, 16.4s, ~7s wall), the same demo at 30 and 60fps against a measured
durations file (715 / 1428 frames), two byte-identical repeat runs, and a mux of
the result through the **unmodified** `pipeline/encode.sh` producing a valid
h264+aac+mov_text mp4. No full product video has been rendered through this path
— no deck repo has Motion Canvas scenes yet.

**Limits, in the order they will bite:**

1. **Not wired into the `explainer-video` CLI.** Deliberate — the spike is not
   allowed to edit `pipeline/*` or the orchestrator. Today the handoff is three
   manual commands (`tee` the run, `make-durations.mjs`, `render.mjs`, then
   `encode.sh`). Adoption means adding a `--renderer motion-canvas` branch to
   `explainer-video`, which is a follow-up, not this PR.
2. **Content moves from HTML to TypeScript.** The self-contained
   `explainer.html` artefact goes away. Anyone who can edit the slides today
   needs to learn a generator-based animation API to edit them tomorrow. This is
   the single biggest adoption cost and it is not technical.
3. **±1 frame tail.** The render lands one frame long at 30fps (33ms) and
   exactly on the mark at 60fps. Cause is Motion Canvas's own per-scene frame
   rounding; a quarter-frame epsilon on the pad was tried and overshot the other
   way (−2 frames), so it was reverted rather than papered over. The residual is
   reported every run, and 33ms of frozen final frame is invisible after the
   mux. It is not fixed.
4. **Fonts are a system stack, not a brand font.** Chromium has no network
   access during the render and no brand webfont is bundled, so `brand.tsx` uses
   `"Inter", "Helvetica Neue", Helvetica, Arial, …`. The render is byte-identical
   **on the same machine**; a machine with a different set of installed fonts
   will pick a different first-available family and produce different (still
   correct-looking) frames. Cross-machine byte-determinism needs a bundled woff2
   loaded via `@font-face` — **still not done**; the assay-decks field report
   closed this deck-side in ~20 lines and it is worth pulling in here. Half of
   that fix *is* in: `render-entry.ts` gates `window.__mc.ready` on
   `document.fonts.ready`, so the moment a woff2 is bundled the render cannot
   start on fallback glyphs and rasterize its opening frames non-deterministically.
   The other half — actually shipping the font file — is a deliberate omission,
   not an oversight.
5. **The dev server is load-bearing.** Rendering requires Vite's HMR socket
   (`import.meta.hot` gates the exporter). A production `vite build` cannot
   render. That is upstream's design; if it changes, this driver changes.
6. **`@motion-canvas/vite-plugin` is CommonJS.** Depending on how Vite loads the
   config, the default import arrives as the function or as `{default: fn}` —
   `vite.config.ts` normalizes both. Without that, config loading fails with
   `motionCanvas is not a function`.
7. **esbuild's postinstall must run.** This environment's npm gates install
   scripts; `package.json` carries an `allowScripts` entry for `esbuild`. If
   `npm install` reports esbuild as un-approved, Vite will not start.
8. **Cost of the dependency.** 74 packages (measured: `npm ci` → "added 74
   packages") plus a Chromium download, for a tool whose current job is one video
   per product per quarter. The Playwright dependency does *not* go away — it
   just moves from recording to driving.
9. **No automated test covers any of this.** CI for this repo is
   `.github/workflows/lint.yml` → `statusgen --lint`, which validates the stream
   registers and never touches this directory. `npm run typecheck` is real but is
   not wired to CI, and everything else above was verified by running it by hand
   on one machine. A render smoke test needs Chromium + ffmpeg on the runner;
   until a deck actually adopts this, that cost is not paid. **Read every claim
   in this file as hand-verified, not as continuously enforced** — there is no
   green check anywhere that would catch a regression in this directory.
10. **Schema divergence with the Manim adapter.** Both write a file called
    `scene-durations.json` with a `scenes` key, and the two shapes are not
    compatible: here `scenes` is `[{id, duration}]` alongside a `leadIn`; there it
    is `["SceneName", …]` with a parallel `durations` array and no lead-in.
    Feeding either to the other fails loudly rather than mis-rendering (verified
    in both directions), but one house schema would be better than two. The
    lead-in is the substantive half: `assemble_audio.py` puts `LEAD_S = 0.35` of
    silence before scene 1 and excludes it from every `SCENE_DURATIONS` entry, so
    the video owes `leadIn + sum(durations)`. This adapter renders that; a
    renderer that ignores it runs 0.35s short against the same narration. Flagged
    for the stream, not decided here.

**Verdict input, not a verdict.** What Motion Canvas buys is determinism, speed,
and cheap choreography. What it costs is the HTML artefact and a TypeScript
authoring surface. If explainer videos stay rare and are edited by whoever has
the deck open, the HTML path is fine. If they become routine, get iterated on,
and need diffable output, this path pays for itself quickly.
