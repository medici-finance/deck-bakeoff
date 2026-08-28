# The render-and-look gate — recipe

Two halves, both mandatory: a headless assertion pass, and a human or model
**looking at the frames**. The worked implementation is
`<loom-bakeoff sandbox>/tracks/video/hybrid/build/render-check.mjs` (~226 lines, node builtins +
Playwright only) with its transcript in `<loom-bakeoff sandbox>/tracks/video/hybrid/build/out/`;
copy it and adjust paths rather than rewriting it.

## Playwright without npm install

Import Playwright by absolute path from the house pipeline's own install —
no npm in the working repo:

```js
import { chromium } from
  "file://<repo-root>/tools/explainer-video/node_modules/playwright/index.mjs (this repo)";
```

Viewport 1920×1080, `file://` navigation, collect every `pageerror`,
`console` error/warning, and any request that is not `file:`/`data:`.
Seeking uses the same `window.__player` shim the seam gate requires
(`../../staging/references/seam-gate.md`) — one shim serves both gates.

## Pass A — LOAD (static + seeked assertions)

- scene count == `window.SCENE_DURATIONS` length == `SCRIPT.md` table rows
- exactly one `SCENE_DURATIONS` assignment matches the pipeline regex
  `window\.SCENE_DURATIONS\s*=\s*\[[^\]]*\]\s*;?` in the file source
- no external references: `src`/`href` that is not `data:` fails
- `document.fonts.check(...)` true for every embedded face
- shim exposed: `__player`, `__playerReady`, `__renderReady`
- zero page errors, zero console errors/warnings (allow only the runtime's
  own named fallback/compression warnings), zero off-`file://` requests
- no scene compressed by the runtime (grep the compression warning)
- **overflow, measured per element, seeked**: seek to ~60 % of every scene,
  force layout, walk `.scene, .scene *`, skip invisible elements (computed
  visibility/display and *effective* opacity through ancestors), and fail
  anything whose rect leaves the 1920×1080 stage by >2 px. This is the only
  check that catches an element clipped invisible by its own container
  (the exemplar found one at x −1273 this way).

## Pass B — SHOTS + the front-load probe

- **Front-load probe**: for every scene, count visible inked elements at
  15 % and at 85 % of its slot; fail any scene with *less* at 85 %. This is
  the executable form of the terminal-hold pile-up check — a scene that
  plays its whole choreography in three seconds and freezes.
- **≥6 screenshots, including mid-animation ones** — seek into the middle
  of the bold moment, the arrest, each assemble — plus each act's final
  image. Name them for what they should show.

## Pass C — DONE, both duration paths

- **Injected path**: rewrite the file through the pipeline's *own* regex
  with short durations (e.g. 0.6 s per scene), load, wait for
  `dataset.done === "1"`, assert `doneReason === "complete"` and that the
  runtime actually used the injected array.
- **Fallback path**: empty the declaration (and shrink the authored
  fallback), assert the same on the fallback array.
- **Negative control** — a green check that cannot go red proves nothing.
  Break the build for real and assert `doneReason === "error"`. The
  exemplar's lesson: the control must be *proven negative*. Renaming the
  `.scene` CSS class did nothing (the runtime selects on `[data-scene]`);
  renaming `data-scene` everywhere also rewrote the runtime's own selector
  string, so the page rebuilt itself perfectly. Only renaming the attribute
  **on the `<section>` tags alone** actually broke it. If your control
  passes on the first try, suspect the control before celebrating.

Write the full PASS/FAIL transcript to a file beside the build and exit
non-zero on any failure.

## Pass D — WALL CLOCK under the recorder (SKILL §8b)

The 12:14-against-7:06 incident (2026-08): a runaway TTS take (327.68 s wav
for a 25.71 s row) was measured and injected into `SCENE_DURATIONS`, and
every downstream guard trusted it — `doneReason=complete`, green gates, film
1.72× long. The injected array is a measurement, not ground truth. Assert:

- **Take-sanity gate fires.** Inject the authored array with one scene
  multiplied ~12× through the pipeline's own regex; the page must reach
  `done=1` with `doneReason=error` naming that scene in **well under a
  second** (measured: 0.06 s hybrid adapter, 0.2 s hand-rolled driver).
  Then inject authored × 1.15 (a real pacing drift) and assert it does
  *not* fire — a gate that trips on honest pacing is a broken gate.
- **Sync telemetry under recordVideo.** Run the film through the
  `record.mjs` conditions — `chromium.launch()`, viewport 1920×1080,
  `recordVideo: { size: { width: 1920, height: 1080 } }` — and read the
  `[sync]` boundary lines / `__explainer.syncMarks`. Every scene boundary's
  wall-clock drift must be within ~2 % of elapsed timeline time (measured
  2026-08-18: the hybrid exemplar holds every boundary within ±0.03 s over
  7 min *while recording*; the hand-rolled animated driver within +0.26 s
  over 3 min, 0.14 %). A drift that grows scene-over-scene means the live ticker is
  not tracking the wall clock (lag smoothing re-enabled, a frame-counting
  driver) or a scene cannot hold real time at 1080p — fix the ticker or
  cheapen the frame; never ship the drift.
- **Webm duration proof.** The recorded webm must decode to
  sum(`SCENE_DURATIONS`) + tail + ~1.5 s (recorder pad + page-load skew),
  within 2 %. Probe with `ffmpeg -i <webm> -f null -` (Playwright webms
  carry no duration header). The webm is the render test; the mp4 encode
  stays the human's.

Run both duration paths' sync numbers on the FALLBACK array too — a plain
(no-recording) run and a recorded run should produce the same boundary
timings; a gap between them is load-proportional slip and fails the gate.

## Then LOOK

Open the screenshots — mid-animation first — and read each frame as a
viewer:

- Is every line legible, or did something soft-wrap into a false second
  line?
- Did anything land on top of anything (a stamp over text passes every
  overflow check)?
- Does the mid-slot frame of each scene look *mid-motion*, or already
  finished?
- Is the bold moment visibly the loudest frame in the piece, and the
  arrest visibly stopped short?

Record what the looking found (even "nothing") in NOTES. The class of
defect this catches — illegible, overlapping, pace-dead frames — survived
every automated assertion on every bake-off run.
