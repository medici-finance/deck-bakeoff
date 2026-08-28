---
name: video-design
description: Use when authoring, storyboarding, or reviewing a house explainer video — writing the SCRIPT.md scenes, choosing a renderer, designing a chart or maths scene, or checking pacing, VO sync, on-screen copy, and brand fit before a render. Not for the renderer/pipeline contract itself (that is a separate layer).
---

# video-design

The narrative video-direction layer for the house explainer program: the
mission → script → storyboard → scene-grammar → VO-sync judgment that decides
whether an explainer lands. It sits where `frontend-design` sits for pages —
above the tooling, below the content. The engine, the renderer adapters, and
the durations contract live in `tools/explainer-video/`; this skill teaches how
to *direct* a video that runs on them. It is deliberately renderer-agnostic in
its core and carries one appendix per adapter that exists.

Every rule below is authored **from** the 2026-08-06 pilot — two missions (the
Assay office explainer, "the maths behind the P/N split") rendered in four
treatments each (current HTML, GSAP, Motion Canvas, Manim) and judged
side-by-side — or from a standing house brand rule. A rule with no citation is
speculation and gets cut; the `[cite: …]` on each rule is what makes "cut it"
mechanical rather than a matter of taste. The pilot's human verdict selected
**GSAP across both missions** (`assay-decks#4`, `medici-decks#14`); the two
other adapters were evaluated and not selected. Their retirement is a separate
ruling (see the appendices and the stream README) — this layer does not delete
them, it records what won.

## Mission

Start from one sentence: who is watching, and what one thing must they believe
by the end? An explainer is an argument, not a feature tour. The mission fixes
the single claim the whole video serves (the Assay explainer sells "an office
for agent-fleet software work"; the P/N explainer proves "P + N = 1, proven not
promised"). Everything downstream — scene count, the one bold moment, the
palette — is spent in service of that claim, and anything that does not serve it
is cut before it reaches a storyboard.

- RULE: Give each video exactly one mission claim and sequence every scene as a step toward it; a scene that does not advance the claim is cut, not kept for interest. [cite: https://github.com/medici-finance/medici-decks/pull/14#issuecomment-5308442362]

## Script

The script is the house `SCRIPT.md`: a first `# ` title heading (which slugifies
to the output filename) and an **8-scene table**, one row per scene, columns
`# | id | ~sec | narration | on-screen text`. The narration column is the
spoken voice-over; `~sec` is the estimated length until a real take exists; the
on-screen-text column is the literal words that appear on the canvas that scene.
The table row order is load-bearing: it is the order the pipeline measures
durations in, injects them in, and the renderer plays scenes in. An optional
`## Description` section becomes the YouTube description at encode time.

Timing discipline is **measured, not guessed**. The pipeline speaks each scene
with the real voice profile, measures it, and emits one `SCENE_DURATIONS` float
per scene (gap included, a longer tail on the last). Author the visuals to those
measured numbers; until a take exists, the `~sec` estimates stand in and must be
labelled as estimates.

- RULE: One idea per scene, in argument order — give each row exactly one claim and sequence the table as a proof (the P/N explainer runs title → split → morph → invariant → sides → recombine → cost → close). [cite: https://github.com/medici-finance/medici-decks/pull/14#issuecomment-5308442362]
- RULE: Trace every scene duration to a measured narration take; when no TTS run exists yet, wire the estimate in as the renderer's native SCENE_DURATIONS fallback and label it an estimate, never a measurement. [cite: https://github.com/medici-finance/assay-decks/pull/4#issuecomment-5308433641]

## Storyboard

Before any renderer opens, block the video shot-by-shot against the script rows:
what is on the canvas at the start of each scene, what enters, what the eye is
meant to rest on, and how the scene hands off to the next. The storyboard is
where the *one bold moment* is placed and everywhere else is kept quiet, and
where recurring motifs are planned so the video reads as one piece rather than
eight slides. Because the deliverable is copied to a work directory before
recording, the storyboard also fixes the rule that the artifact is entirely
self-contained — nothing it references may live outside the file.

- RULE: Keep the slides genuinely self-contained — fonts embedded, no relative script or asset references — because the pipeline copies the file to a work dir before recording and any external reference breaks there. [cite: https://github.com/medici-finance/assay-decks/pull/4#issuecomment-5308433641]

## Scene grammar

One idea per scene; one bold moment per video. The signature element is the
single place the motion is allowed to be loud — the Assay explainer spends it on
scene 6's stamp sting, the P/N explainer on scene 3's morph — and every other
scene stays quiet so the bold moment reads. Distinctiveness cannot come from
colour, because the house palette is pinned and identical across videos; it
comes from recurring **motifs** (the octagonal assay mark, the App-avatar
marks) carried scene to scene. A scene that tries to be memorable on its own
steals from the one moment that is supposed to be.

- RULE: Spend exactly one bold moment per video and keep everything else quiet — the signature element (the assay explainer's scene-6 stamp sting, the P/N explainer's scene-3 morph) is the only place the motion goes loud. [cite: https://github.com/medici-finance/assay-decks/pull/4#issuecomment-5308433641]
- RULE: Carry distinctiveness in recurring motifs (the octagonal assay mark and the App-avatar marks), not in colour, because the pinned house palette cannot vary from one video to the next. [cite: https://github.com/medici-finance/assay-decks/pull/4#issuecomment-5308433641]

## Pacing & VO sync

The narration leads and the visuals follow — never the reverse. The pipeline
measures each narration clip and hands the renderer a `SCENE_DURATIONS` array;
the renderer's job is to scale an authored-at-natural-pace scene to fit the
seconds the voice actually took. This is precisely why the pilot chose the GSAP
adapter: its duration-reconciliation absorbs narration drift without re-timing
by hand. Do not author to a stopwatch of frames; author to the beats of the
sentence and let the runtime stretch or compress to the measured take.

- RULE: Author each scene at a natural pace and let the runtime scale it to the measured SCENE_DURATIONS; never hard-code timings that assume a narration length, because the voice-over is the clock and the visuals follow it. [cite: https://github.com/medici-finance/assay-decks/pull/4#issuecomment-5308433641]

## Chart scenes

When a scene *is* the data — a curve, a morph, a plotted formula — the dataviz
discipline applies in full: form first, one axis per chart, a validated palette
checked against the actual canvas (not eyeballed), direct labels, and all text
in text tokens rather than in a series colour. The P/N pilot is the worked
example: the settlement curves `P = min(1, S/x)` and `N = max(0, 1 − S/x)` are
sampled point-by-point and the morph is constructed so `P + N = 1` holds at
every frame. The renderer draws them; it does not compute them for you.

- RULE: Validate every chart palette against the actual canvas with the dataviz validator before use, never by eye — in the pilot N could not stay #99BBFF (outside the dark-mode lightness band) and the validated pair was P #3366FF / N #7B90D9. [cite: https://github.com/medici-finance/medici-decks/pull/14#issuecomment-5308442362]
- RULE: Label curves directly in text tokens (white or #AAAAAA), never in the series colour, and keep one axis per chart with a recessive grid. [cite: https://github.com/medici-finance/medici-decks/pull/14#issuecomment-5308442362]
- RULE: Treat the renderer as a clock, not a maths engine — carry ordinary scenes as declarative markup but build any chart, curve, or morph scene as an imperative timeline over a hand-written sampler. [cite: https://github.com/medici-finance/medici-decks/pull/14#issuecomment-5308442362]

## On-screen copy

On-screen text is not the narration transcript. It is the two or three words the
viewer should read while the voice says the sentence — plain verbs, one job per
element, no decoration. The subtitle track is held to the same discipline: it is
on-screen text, not a second script. If an element is doing two jobs, split it;
if a word is not earning its place on the canvas, it belongs in the narration
only.

- RULE: Write on-screen text in plain verbs with one job per element, and hold the subtitle to the same discipline as the on-screen text. [cite: brand-guide]

## Brand

Brand authority is the house guide (`../option-index-tracker/docs/brand-guide.md`)
plus the per-product overlays; this skill **cites** those rules and never
restates or forks them — if a rule below and the guide ever disagree, the guide
wins. The canvas is the pinned house dark surface, the accent is the house blue
only, copy is set in the embedded house typeface, there is no mascot, and the
audio follows the house voice-and-loudness policy.

- RULE: Render on the house dark canvas; it is the pinned brand surface, not a per-video choice. [cite: brand-guide §Video]
- RULE: Use the house blue as the only accent and do not introduce new hues for emphasis. [cite: brand-guide §Palette]
- RULE: No mascot — the marks are motifs, never characters; do not animate them into personas or give them agency. [cite: brand-guide §Video]
- RULE: Set all copy in the house typeface (IBM Plex) embedded in the artifact, and never rely on a system font stack. [cite: brand-guide §Typography]
- RULE: Follow the house audio policy — a house voice profile normalized to the house loudness spec (−16 LUFS / −1.5 dBTP) — and never ship a raw or differently-normalized track. [cite: brand-guide §Audio]
- RULE: The rendered mp4 is generated output — never commit it to the engine repo or a deck repo. [cite: brand-guide §Video]

## Renderer appendices

The core above is renderer-agnostic. Each adapter directory that exists under
`tools/explainer-video/renderers/` gets one appendix here describing it **as
built**. The pilot verdict selected `gsap`; `manim` and `motion-canvas` were
evaluated and not selected, and are documented here as what they are — evaluated
alternatives kept pending a separate retirement ruling (owed from Ian at verdict
time, per the stream README). This layer does not specify the adapter/pipeline
contract; that is brief 02, authored against the surviving renderers.

### Renderer: gsap

**The selected adapter.** A drop-in replacement for hand-rolled per-deck
animation JS inside an `explainer.html`: it reads the measured
`window.SCENE_DURATIONS`, builds one GSAP timeline per scene scaled to fit,
advances the scenes itself, and raises the `document.body.dataset.done` signal
`record.mjs` waits for. It buys declarative sync (author at a natural pace, the
runtime fits it to the voice), first-class SVG draw-on (`ctx.draw()` walks an
inline SVG in reading order), and a correct-once done signal with a watchdog.

Direction notes for authoring on it:
- Keep exactly one `window.SCENE_DURATIONS = [...]` assignment in the whole file
  (comments and JS strings included) — the pipeline rewrites the *first* match,
  and a second one silently steals the injection and drifts the video off the
  voice with nothing in the logs. `bundle.mjs` makes that a build error.
- Ordinary scenes are declarative `[data-enter]` markup; chart/maths scenes are
  imperative builds over a hand-written sampler — GSAP is a better clock, not a
  maths engine.
- Pilot gotchas found and worth carrying: `ctx.hold()` returns the scene
  timeline, so `ctx.flex(ctx.hold(...))` smears the choreography (use the
  `flexHold()` helper); `ctx.draw` on a dashed reference line destroys its dash
  pattern (use `data-draw="reveal"`).
- Scene handoffs are a named per-boundary choice: `data-exit="cut|fade|push|zoom"`
  on the outgoing scene (default fade, the brand crossfade). Direct them from
  the storyboard's hand-off row, not ad hoc — a cut is punctuation and spends
  like a bold moment; the vocabulary is deliberately closed, and a new name is
  a design ruling, not a runtime patch.
- Scenes can be authored as one fragment file each (`video/scenes/NN-id.html`)
  and composed by `bundle.mjs` into the committed self-contained artifact —
  decomposed at source, monolithic at artifact. The storyboard's
  self-containment rule is unchanged: it binds the composed output.
- The recorder path emits 25fps (Playwright's recorder rate); the offline
  adapters emit 30fps — pin one rate if treatments are ever intercut.

### Renderer: manim

An offline, deterministic **animated-maths** render path
([Manim CE](https://www.manim.community/), Python) that replaces the recording
step only; narration, audio assembly, subtitles and mux are unchanged. It reads
the measured durations from a `scene-durations.json` file (`--durations <file>`)
and emits its own mp4 with per-scene budgets resolved by name; it has no
`data-done` signal because it renders offline to a known duration. Its one
genuine advantage is term-by-term equation transforms and computed-geometry
morphs (`TransformMatchingShapes`, `ValueTracker`); its tax is
layout-by-scene-units on talking slides. **Evaluated, not selected** by the
pilot verdict. If ever authored against: fonts need repo-embedded woff2→TTF
registration with Pango (no system install), and the adapter's `render.sh`
concat-list path bug requires absolute paths as a workaround.

### Renderer: motion-canvas

An offline, deterministic **frame-by-frame** render path
([Motion Canvas](https://motioncanvas.io), TypeScript), ~3× faster than
real-time recording; scenes are TypeScript and durations reach them through the
scene-duration contract rather than an HTML injection (the `inject`/`record.mjs`
steps are skipped). It is strong on dense, loop-heavy scenes (claim grids,
board tables) and on chart signals expressed as functions of a morph/strike
parameter. Its cost is that the artifact stops being an openable HTML page.
**Evaluated, not selected** by the pilot verdict. If ever authored against: the
adapter's `brand.tsx` is white-surface, so the house dark canvas needs a
`trueBlack` stage override, and the render entry must embed the house woff2s and
gate readiness on `document.fonts.load`.
