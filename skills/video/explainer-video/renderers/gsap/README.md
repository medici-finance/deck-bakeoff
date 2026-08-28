# renderers/gsap — GSAP renderer adapter

A drop-in replacement for the hand-rolled animation JS inside an
`explainer.html`. It reads the durations the pipeline measured from the real
narration, builds **one GSAP timeline per scene** scaled to fit, advances the
scenes itself, and raises the done signal `pipeline/record.mjs` waits for.

**The engine is untouched.** Nothing under `pipeline/` changes; this renderer is
additive and opt-in, one deck at a time. A deck that adopts it is still just a
self-contained `explainer.html` passed to `--slides`.

What it buys over hand-rolled per-deck JS:

- **Sync is declarative.** You author a scene at a natural pace; the runtime
  stretches or compresses it to the seconds the voice actually took.
- **SVG draw-on is first-class.** The house diagrams are SVG/mermaid exports —
  `ctx.draw()` walks an inline SVG in reading order, drawing strokes and
  revealing labels, spread across the scene's measured duration.
- **The done signal is not your problem.** One implementation, correct once,
  plus a watchdog so a broken build fails in seconds instead of burning the
  recorder's 5-minute timeout.

```
renderers/gsap/
├── package.json        # local npm project; vendors gsap (free, incl. plugins)
├── bundle.mjs          # inlines gsap + runtime into an explainer.html, in place
├── src/gsap-explainer.js   # the runtime (classic script, global GsapExplainer)
├── template.html       # starting point to copy into a deck repo's video/
└── demo/demo.html      # self-contained 3-scene demo (bundled, ready to record)
```

## Contract with the pipeline

Both directions of the contract are narrow and already implemented by the
engine — this renderer just implements the slide side of it.

### In — `window.SCENE_DURATIONS`

`assemble_audio` measures each narration clip; `inject_durations`
(`tools/explainer-video/explainer-video`) then writes an array of seconds — one
entry per scene, in `SCRIPT.md` row order — into a **copy** of the slides
(`RunContext.slides_rendered`, `<out>/.work-*/slides.html`) before recording.

It does this with a regex substitution, `count=1`:

```python
re.compile(r"window\.SCENE_DURATIONS\s*=\s*\[[^\]]*\]\s*;?")
```

Three consequences the renderer is built around:

1. **Keep exactly one such assignment in the whole file** — including inside
   HTML comments and JS strings. The pipeline rewrites the *first* match; a
   second one silently steals the injection and the video renders at fallback
   timings, drifting off the voice-over with nothing in the logs. `bundle.mjs`
   makes that a build error. (This is not hypothetical — the first draft of
   `demo.html` had a comment that matched, and the injected durations went into
   the comment.)
2. **The slides are copied to a work dir**, so relative `<script src>` and any
   other external reference breaks. The file must be genuinely self-contained;
   `bundle.mjs` is how you get there.
3. **Scene count must equal `SCRIPT.md` row count.** A mismatch is a console
   warning and missing entries default to 4s.

The declared literal is left empty (`window.SCENE_DURATIONS = [];`) so the
uninjected case is unambiguous: empty means "no pipeline", and the runtime falls
back to the timings passed to `boot({ fallback: [...] })` with a warning.

### Out — the done signal

`record.mjs` polls `document.body.dataset.done === '1'` every 200ms, pads ~1s,
and stops. The runtime sets it `tail` seconds (default 0.5) after the master
timeline completes, so the last frame is held rather than cut on the final tween.

It also sets `document.body.dataset.doneReason`, which is how a finished render
is told apart from a broken one:

| `data-done-reason` | Meaning | `record.mjs` |
|---|---|---|
| `complete` | the master timeline ran to the end | exit 0 |
| `error` | a scene build threw, or the page had no scenes — `data-error` carries the message | **exit 1** |
| `watchdog` | the master never completed within `total + tail + 5s` | **exit 1** |

**A failed render must never look like a successful one.** The done flag is the
only channel `record.mjs` polls, so a broken run still raises it — otherwise the
recorder burns its 5-minute ceiling and then ships a five-minute video of a
broken page, exiting 0. Raising it with `doneReason=error` instead means the
recorder stops in seconds *and* exits non-zero, which the CLI runs under
`check=True`. A build failure also skips playback entirely: there is no reason
to spend the narration's wall-clock recording something already known bad.

Pages that set no `data-done-reason` at all are not judged, so hand-rolled
`explainer.html` decks that predate this adapter keep working unchanged.

`window.__explainer` is exposed for debugging:
`{ master, durations, total, scenes, timelines, failure }` — `timelines[i]` is
scene *i*'s timeline, which is what the checks in `verify.mjs` measure.

## The timing model

For each scene, `available = measured_duration − handoff`, where the handoff is
the named boundary the scene is entered through (the default is a 0.2s
crossfade — see below). Content is built into a paused timeline, then
reconciled against `available`:

| Case | What happens |
|------|--------------|
| Content shorter, with a flexible segment | The flexible segment absorbs **all** the slack (`tween.duration()` / nested `timeScale()`, then `timeline.shiftChildren()` to keep siblings in order) |
| Content shorter, nothing flexible | The scene plays at its authored pace and **holds** the final frame — the right answer for a title card |
| Content longer than the scene | Compressed via `timeScale`, with a console warning naming the scene and both durations |

The master timeline's length is anchored to the sum of the measured durations,
not to whatever the last scene's animation happened to need, so scene *k* always
starts at `sum(durations[0..k-1])`.

`gsap.ticker.lagSmoothing(0)` is set at load. GSAP's default lag smoothing
freezes animation time through a jank spike, which makes wall-clock elapsed time
run ahead of the timeline — harmless on a website, fatal when the frames have to
line up with a pre-rendered narration track.

### Scene handoffs — `data-exit`

The boundary between two scenes is a named, per-boundary storyboard choice,
authored on the **outgoing** scene ("how this scene hands off to the next"):

```html
<section class="scene" data-scene="split" data-exit="push">…</section>
```

| Name | What it does | Duration |
|------|--------------|----------|
| `fade` | The brand crossfade — the **default**, no attribute needed | 0.2s (`crossfade`) |
| `cut` | A one-frame swap; the strongest punctuation available | 0s |
| `push` | Outgoing shifts up 24px and fades; incoming rises 24px into place | 0.3s (`pushDuration`) |
| `zoom` | Outgoing scales to 1.02 and fades; incoming settles from 0.98 | 0.35s (`zoomDuration`) |

The handoff's duration is charged to the **incoming** scene's measured budget
(exactly as the crossfade always was), capped at half that scene's duration, so
the narration stays the clock. An unknown name warns loudly and falls back to
`fade` — a typo must never fail a render. `data-exit` on the final scene has no
effect (the film ends on the tail hold) and warns.

Both moves stay inside the house motion vocabulary — small travel, `power2.inOut`,
no spring or overshoot. The vocabulary is deliberately closed: a fifth name is a
design ruling for the video-design skill, not a runtime patch. Since one
continuous timeline owns both scenes, a **carried motif** (an element that
travels through a boundary) still needs no handoff machinery at all — build it
in the master's coordinate space; the handoff only governs the scene roots.

## Authoring

### Declarative (no JS per scene)

Mark up elements and let the default build run: enter everything marked
`[data-enter]`, then draw everything marked `[data-draw]` (flexible, so it fills
the scene).

```html
<section class="scene" data-scene="intro">
  <h1 data-enter>Headline.</h1>
  <svg viewBox="0 0 1000 300" data-draw>…</svg>
</section>
…
<script>GsapExplainer.boot({ fallback: [5, 9] });</script>
```

### Imperative (per-scene choreography)

```js
GsapExplainer.boot({
  fallback: [4, 8, 4],
  scenes: [
    { id: 'title', build: function (tl, ctx) {
        ctx.enter('.eyebrow, h1');
        ctx.draw('.rule', { duration: 0.6 });  // fixed => draws, then holds
        ctx.enter('.lede', { at: '-=0.3' });
      } },
    { id: 'diagram', build: function (tl, ctx) {
        ctx.enter('h2');
        ctx.draw('svg');                       // flexible => fills the scene
      } },
  ],
});
```

`tl` is the scene's GSAP timeline — anything GSAP can do is available. `ctx` adds:

| | |
|---|---|
| `ctx.duration` | seconds of content time this scene has |
| `ctx.el`, `ctx.$(sel)`, `ctx.$$(sel)` | the scene element and scoped selectors |
| `ctx.enter(sel, opts)` | fade + 8px rise, 200ms ease-in-out, staggered. Defaults to `[data-enter]` |
| `ctx.exit(sel, opts)` | the mirror of `enter` |
| `ctx.draw(sel, opts)` | SVG draw-on (below). Defaults to `[data-draw]` |
| `ctx.flex(child, {weight, min})` | mark any tween/timeline as the scene's flexible segment |
| `ctx.hold(seconds, opts)` | an explicit pause in the sequence |

`opts.duration` on `draw` is `'fill'` by default (flexible); pass a number for a
fixed one. With several flexible segments, slack splits by `weight`. Flexing
works on **direct children of the scene timeline** — a tween nested inside a
timeline you built yourself is not reachable.

**Every helper returns the thing it just made** — `enter`, `exit` and `hold`
return their tween, `draw` returns its nested timeline — so the return value can
be handed straight to `ctx.flex`:

```js
ctx.flex(ctx.hold(1));            // the HOLD absorbs the scene's slack
ctx.flex(ctx.draw('svg'), { weight: 2 });
```

This is worth stating because GSAP's own `tl.to()` / `tl.fromTo()` return the
**timeline**, for chaining — not the tween. An earlier cut of these helpers
passed that return value straight through, so `ctx.flex(ctx.hold(1))` registered
the whole scene as flexible and time-scaled every tween in it. `ctx.flex` now
also refuses the scene timeline outright, with a warning naming the mistake.

### SVG draw-on

`ctx.draw(target)` expands a container to its drawable descendants and orders
them by **document order**, which is why authoring the SVG in reading order is
all most diagrams need. Override selectively with `data-draw-order="N"`.

Each element is then classified:

- **stroked geometry** (`path`, `line`, `polyline`, `polygon`, `circle`,
  `ellipse`, `rect` with a stroke) — drawn on. Uses `DrawSVGPlugin` when it is
  present, otherwise an equivalent `stroke-dasharray`/`stroke-dashoffset`
  implementation, so the renderer works with or without the plugin.
- **an element that already carries its own `stroke-dasharray`** — a dashed
  reference line, a dotted boundary — is **revealed, not drawn on** (see below).
- **a shape that also has a fill** — the fill washes in behind its own outline
  at 60% of the draw. `data-draw-fill="off"` opts out.
- **everything else** (`text`, labels, `data-draw="reveal"`) — fade + 8px rise.

Dash patterns are seeded at init, while the whole document still has layout, so
nothing flashes fully-drawn for one frame as its scene becomes visible. This is
also why scenes are hidden with `opacity`/`visibility` and never `display:none` —
`getTotalLength()` needs the geometry to be live.

#### Dashed strokes

Stroke draw-on **owns `stroke-dasharray`** — DrawSVGPlugin and the dashoffset
fallback both work by rewriting it. So drawing a deliberately dashed element
silently renders it solid, and an authored dashed reference line comes out of the
video looking like a solid one. (Found in the field, on `medici-decks#14`.)

Elements with an authored dash pattern are therefore classified as **reveal**
(fade + rise), keeping the pattern intact. The classification is made once, on
pristine geometry, before anything has been seeded.

To draw a dashed element on anyway — accepting that its pattern is consumed —
opt in explicitly:

```html
<path d="…" stroke-dasharray="8 6" data-draw="stroke"/>
```

### Brand

The demo and template are white-surface, near-black ink, a single `#3366FF`
accent used sparingly. Motion is 200ms ease-in-out enters/exits with an 8px
rise, and functional stroke draws — no spring, bounce or overshoot. Passing an
ease from the `back` / `elastic` / `bounce` families logs an off-brand warning
rather than quietly shipping a bouncy frame into a product video.

## Adopting it in a deck repo

1. Copy `template.html` to `<deck-repo>/video/explainer.html`; replace the
   palette and write one `<section data-scene>` per `SCRIPT.md` row.
2. Inline the runtime (this is what makes the file self-contained):
   ```bash
   cd tools/explainer-video/renderers/gsap
   npm install
   node bundle.mjs ../../../<deck-repo>/video/explainer.html
   ```
3. Commit the bundled `explainer.html` to the deck repo and render as usual:
   ```bash
   ./explainer-video --script ../<deck-repo>/video/SCRIPT.md \
                     --slides ../<deck-repo>/video/explainer.html \
                     --profile english-medici
   ```

Re-run `bundle.mjs` after any change to the runtime or a GSAP upgrade;
`node bundle.mjs --check <file>` reports staleness without writing.

### Composing scenes from fragments (opt-in)

A long or multi-author deck can decompose its scenes into one fragment file per
scene and let the bundler assemble them — decomposed at **source**, monolithic
at **artifact**, so the committed `explainer.html` stays the one self-contained
page the pipeline contract requires:

```
video/
├── explainer.html      # the committed artifact (generated block inside)
└── scenes/
    ├── 01-title.html   # exactly one <section data-scene="…"> each
    ├── 02-split.html
    └── …
```

In `explainer.html`, mark where the scenes go:

```html
<!-- gsap-explainer:compose scenes -->
<!-- /gsap-explainer:compose -->
```

`bundle.mjs` fills the block with every `scenes/*.html` fragment in filename
order (prefix them `01-`, `02-`, … to match the `SCRIPT.md` rows), stamps each
with a provenance comment, and regenerates it on every run — edit the fragment,
never the generated block. `--check` fails when a fragment edit has not been
re-bundled, a fragment without a `data-scene` element is a build error, and the
one-`SCENE_DURATIONS`-assignment rule is enforced on the composed output, so a
fragment cannot smuggle in a second assignment. Hand-authored single-file decks
are untouched — a page with no compose block bundles exactly as before.

GSAP is vendored as a normal npm dependency. It is free for all uses including
every plugin (Webflow's acquisition removed the club licence), so
`DrawSVGPlugin` ships inlined alongside the core.

## Checks

```bash
cd tools/explainer-video && npm install && npx playwright install chromium   # once
cd renderers/gsap && npm install
npm test          # bundle staleness + verify-bundle.mjs + verify.mjs
```

`verify.mjs` drives the real runtime in a real Chromium and asserts on measured
numbers — timeline spans, `timeScale`, computed `stroke-dasharray`, the done
signal. It covers the injected and fallback duration paths, flexing (including
`flex(hold)`), dash preservation, compression, the off-brand-ease guard, the
named handoffs (`cut` costs the incoming scene nothing; `push` moves both scene
roots and clears its transform; an unknown `data-exit` warns and falls back to
`fade`), and — most importantly — that a throwing build and a page with no
scenes are reported as `error` rather than as a completed render.

`verify-bundle.mjs` covers the build tool node-side: fragment composition order
and provenance, idempotency, `--check` staleness after a fragment edit, and the
loud failures (missing dir, scene-less fragment, a smuggled second
`SCENE_DURATIONS` assignment).

### The render-and-look gate — `qa.mjs`

The checks above catch **broken**; they have never caught **bad**. `qa.mjs`
makes looking cheap, at the two places looking matters:

```bash
# three frames per scene — entry / payload / resolve — by seeking the master
# timeline in Chromium. Seconds per deck; run after every scene edit, before
# spending a TTS take. --durations previews the film at a measured take.
node qa.mjs stills path/to/explainer.html --out /tmp/qa \
    [--durations 10.31,16.63,…] [--scenes 3,9]

# the same three moments per scene extracted from the SHIPPED mp4 (ffmpeg).
# Sample the delivered file at the beats you changed before calling a fix
# landed — the delivered file is the only artifact whose behaviour is not an
# inference. Load skew is auto-corrected from the probed video length.
node qa.mjs delivered renders/video.mp4 --durations 10.31,16.63,… \
    [--scenes 3,9] [--tail 0.5]
```

One frame per scene is not a review: a single mid-slot sample misses the built
card row and the settled end-state alike (both classes shipped past exactly
that sampling and were caught by a human). Entry / payload / resolve per scene
is the floor, and the tool prints its own last word: **now look at them at
full resolution — that is the gate.** Seeks run forward-only with events
firing, so one-way `.call()` state changes (class flips, text swaps) land
exactly as they would in playback; with `--durations` the literal is rewritten
in a temp copy exactly the way the pipeline's inject step does it (an
init-script cannot win against the page's own contract literal).

There is deliberately **no skip path**: if `gsap` or `playwright` is missing the
suite exits 1 with install instructions. A green run that quietly skipped the
browser would prove nothing about a renderer, which is the whole point of having
it. `npm test` also fails on a stale `demo/demo.html` bundle, so a runtime change
cannot silently leave the committed bundle behind.

Nothing in CI runs this yet — the repo's only workflow is `statusgen --lint`.

## Smoke run

```bash
cd tools/explainer-video
npm install && npx playwright install chromium     # once
node pipeline/record.mjs renderers/gsap/demo/demo.html /tmp/gsap-demo-out
```

Expected: `RECORDED:/tmp/gsap-demo-out/page@….webm` — a 1920×1080 VP8 file of
~17.5s (16s of fallback timeline + 0.5s tail + record.mjs's ~1s pad).

To exercise the injected path without generating audio, substitute durations
with the same regex the pipeline uses and record the result:

```bash
python3 - <<'PY'
import re, pathlib
p = pathlib.Path('renderers/gsap/demo/demo.html')
out = re.sub(r"window\.SCENE_DURATIONS\s*=\s*\[[^\]]*\]\s*;?",
             "window.SCENE_DURATIONS=[3.21, 11.87, 5.04];", p.read_text(), count=1)
pathlib.Path('/tmp/injected.html').write_text(out)
PY
node pipeline/record.mjs /tmp/injected.html /tmp/gsap-inject-out   # ~21.6s webm
```

## Limits

- Flexing reaches direct children of the scene timeline only.
- A very long scene with a single flexible draw stretches that draw across the
  whole scene. That is usually what you want for a big diagram; for a short
  accent rule, give it a fixed `duration` and let the scene hold.
- No audio in the page: sync is to the measured durations, not to playback.
  That is the engine's model — audio is muxed at encode time.
- **Lead-in silence is not accounted for.** `assemble_audio.LEAD_S` prepends
  0.35s of silence to the narration and deliberately excludes it from every
  `SCENE_DURATIONS` entry; `encode.sh` muxes video and audio both from t=0. This
  runtime starts scene 1 at t=0, so the visuals lead the narration by that 0.35s
  for the whole video — unless recorder start-up latency is what the lead-in was
  meant to absorb, in which case it is already correct. The Motion Canvas
  adapter (#20) takes an explicit `--lead-in 0.35`. Worth settling across all
  three adapters rather than per-renderer; see the note on PR #17.
