---
name: video-author
description: >
  Author the explainer video: turn a locked staging.yaml into SCRIPT.md +
  a self-contained explainer.html that the house pipeline can render. Use when
  someone asks to author the explainer video, build the film or its scenes,
  render the staged video, write SCRIPT.md and explainer.html, or do any
  storyboard-to-film work downstream of staging. Consumes the staging skill's
  contract (skills/staging, video lane); supersedes the house video-design
  skill for AUTHORING — the pipeline README (tools/explainer-video) stays
  authoritative for render mechanics. Not for deciding what the film says or
  in what order — that is staging's job, and this skill is forbidden to touch it.
---

# video-author

The design-and-authoring layer for a staged film. Input: a `staging.yaml`
emitted by `skills/staging` (v2, video lane) with its per-scene motion fields,
`motion_budget`, and derived bold-moment window. Output: `SCRIPT.md`,
`explainer.html`, a locked-then-audited `motion-spec.md` instance, a
`seams.json` ledger with a passing seam gate, a passing render-and-look check
with screenshots — and nothing else. The mp4 is not this skill's output (§9).

This skill is the packaging of the bake-off's winning hybrid process
(`bakeoff/JUDGING-video-claude.md`): the house pipeline + staging's arithmetic
and gates + the vendored seam gate + the one-choice-per-row motion spec + the
motion-role governor. Worked example: §10.

## 1. The composition contract (hard)

```
staging       owns WHAT is said and IN WHAT ORDER   → emits staging.yaml
video-author  owns HOW IT LOOKS AND MOVES           → consumes staging.yaml
```

- **Never reorder beats or scenes, and never rewrite a headline claim.** You
  may reword a claim's *phrasing* for the ear or for line-breaking, split one
  scene's claim across an on-screen line and a narration sentence, and refuse
  a scene as unrenderable — but a refusal **returns to staging**; it does not
  get fixed in the timeline.
- The per-scene `motion_role`, `energy`, `peak`, `motion_turn` and `figures`
  fields are allocation, and allocation is staging's. You spend the budget;
  you do not re-budget. If choreography wants a peak the contract does not
  grant (or wants to skip one it does), that is a staging conversation,
  recorded in `staging.yaml`, not a quiet deviation.
- A failed gate never gets patched at the gate: it names the upstream step
  (staging, the motion spec, the seam ledger) and you go back there.

## 2. The pipeline contract — verbatim-precise

The renderer is `tools/explainer-video` (see its README for mechanics; the
narration is TTS'd per scene, measured, and the measured durations are
injected before recording). The authored artifacts must satisfy, exactly:

**`SCRIPT.md`**
- A first `# ` title heading — it slugifies to the output filename (≤100
  chars).
- One Markdown table, one row per scene, in play order. The pipeline matches
  `id`, `narration`, and (optionally) `subtitle` columns case-insensitively;
  house-added columns (`~sec (est)`, `words`, `act`, `motion role`,
  `on-screen text`) are legal and ignored by the parser.
- **No `subtitle` column** is the sanctioned default: the narration is reused
  as the subtitle (the accessible answer). On-screen text stays 2–5 words —
  it is what the viewer *reads* while the voice says the sentence, never a
  transcript.
- Optionally a `## Description` H2 section — its verbatim body becomes the
  YouTube description `.txt` and mp4 metadata.
- The "8-scene table" in older house prose is a **description, not a
  contract**. Scene count comes from one-idea-per-scene against the staged
  arc; hold scenes to roughly 9–30 s each, none over 30.

**Words per second — the pacing unit.** "Author at a natural pace" has a
unit, and it is *words*:

- conversational / explainer register: **150 wpm** → 1 s = 2.5 words
- technical / deep-dive register: **140 wpm** → 1 s = 2.333 words

Write every narration cell to a word budget; `~sec = words ÷ rate`. Recount
the declared word counts against the narration text before shipping. Every
`~sec` is an **ESTIMATE, and must be labelled as one** in `SCRIPT.md` — no
TTS take exists yet, and the measured take overwrites it. Sanity-check the
ceiling against a take that runs 10 % slow. A film that mixes registers
(a relay) runs each act at its own rate; a single blended rate makes one
register silently wrong.

**`explainer.html`**
- **Self-contained**: inline CSS/JS, all fonts base64-embedded
  (`document.fonts.check` must resolve them), inline/data-URI images, zero
  external `src`/`href`/`url()` references. The pipeline copies the file to a
  work dir before recording; any external reference breaks there.
- **Exactly ONE `window.SCENE_DURATIONS` assignment** in the whole file —
  comments and JS strings included. The pipeline rewrites the *first* match
  of `window\.SCENE_DURATIONS\s*=\s*\[[^\]]*\]\s*;?`; a second assignment
  silently steals the injection and drifts the film off the voice with
  nothing in the logs. Make a duplicate a build error.
- Declare it **empty** (`window.SCENE_DURATIONS = [];`) and carry the
  authored estimates in a separate `FALLBACK` array the runtime uses with a
  console warning — so which duration path ran is never ambiguous, and both
  paths are testable (§8).
- **`document.body.dataset.done = "1"`** when the timeline finishes, plus
  `dataset.doneReason = complete | error | watchdog` — a failed render must
  never look like a successful one. A broken build (no scenes, a thrown
  boot) reports `error` in seconds; a watchdog bounds the recording.
- **Scene count == `SCRIPT.md` row count**, always. Give every scene
  `<section class="scene" data-scene="<id>">` with the SCRIPT row's id.
- The narration is the clock and the visuals follow — author each scene's
  beats at natural pace and let the runtime reconcile the authored span
  against the measured slot (§6). Never hard-code a timing that assumes a
  narration length.

## 3. The motion governor, applied

The allocation rules live in `../staging/references/motion-roles.md` (the
eight roles, R1–R6). What authoring does with them:

- **Peaks land only on EVENT claims.** `rupture` and `arrest` are legal only
  on a claim with a before and an after; the event walk in `staging.yaml` is
  the peak budget and there is no other number. Choreograph the peaks the
  contract grants and nothing else at peak amplitude.
- **The bold-moment window is DERIVED from the lane's `runtime_shares`**, by
  time, never inherited from a deck figure. `staging.yaml` shows the
  derivation (the hybrid's deep-dive act: 72–85 % by time); verify the built
  film's cumulative clock actually places the peak inside it. When the first
  cut misses the window, the rule's own consequence applies: **cut the tail
  beats to the bone** — arithmetic writes content, it is not satisfied by
  relabelling.
- **Spend the energy budget as ordered**: the staged bold moment holds the
  single highest amplitude (R3), every peak buys a quiet neighbour ≤1.5
  (R2), mean energy ≤3.0 with ≥⅓ of scenes at ≤1.5 (R5), rhymes only to
  answer (R4).
- **The ornament gate (R6)**: ≤2 animated figures per scene, 3 at the bold
  moment, every figure naming the clause of the claim it renders. A figure
  that renders the same clause as another, or a clause the narration already
  carries, is decoration — cut it even if it is built and you like it.
- **Absences are decisions and are recorded as such.** `divest` scenes carry
  zero figures by design; a `hold` after the peak is what the peak was paid
  with. Write a restraint pass (what *could* have moved and does not, with
  reasons) into the motion-spec instance, and an honest per-scene
  helped / half / decorated / **helped-by-absence** ledger into your NOTES.
  Roughly half the motion doing real work is the observed honest ratio; a
  ledger with no "decorated" rows was not written honestly.

## 4. The motion-spec ritual — lock before, audit after

Fill in one instance of the one-choice-per-row form
(`../staging/references/motion-spec.md`) — easing, base unit, transition
family, stagger, intensity, hold discipline, budget — **before the first
scene is authored**, dated and marked LOCKED. Every distance is a percentage
of frame height (pixel equivalents in brackets only). After the scenes are
finished, re-run every row against the built film and publish the audit
table; failures are written **FAIL → FIXED** with the fix, or FAIL with the
reason — never quietly deleted.

**This skill amends the donor form's easing row**, resolving the defect the
hybrid run found (recorded there as FAIL — NOT FIXED: the two-curve lock
governs entrances and exits and has no slot for state change, so any film
with a subtractive beat breaks it — an `out` curve on a disappearance makes
a thing that is going look like a thing that is arriving). The row to lock,
in this skill's versions of the form:

> **Easing family** — exactly **two** curves for entrances and exits (one
> OUT for entrances, landings and draws; one IN for exits), **plus a
> declared closed set of at most three** for state change and continuous
> motion (drains, shuttles, strain builds, sanctioned collapses), each
> printed in the instance with what it governs. `linear` is legal only on a
> single declared continuous ambient or accumulation. Overshoot **0 %** —
> no spring, bounce, back or elastic. No default ease anywhere: every tween
> names its curve.

Two counting units the audit needs stated in advance, or the rows cannot be
checked at all:

- An intensity-budget **event is a perceptual beat, not a tween** — a
  three-phase erasure (drain + collapse + ghost) is one event to a viewer
  and four to a timeline. ≤3 events per scene; the bold moment may spend 5.
- **One hero per frame** is checked at an instant: two figures may share a
  scene only strictly sequenced or with one authored at support tier.

Known recurring audit failures, named in advance: the **terminal-hold
pile-up** (all choreography in the first seconds, then stillness — flex
every inter-event gap, §6) and **two heroes in one frame** (fix by demotion,
not by a shorter duration).

## 5. The seam ritual

Every scene boundary is designed, declared, and numerically verified. The
wiring reference is `../staging/references/seam-gate.md`; the tool is
`../staging/tools/seam-gate.mjs` (vendored Apache-2.0, licence file beside
it; node ≥22 + local Chrome, zero npm).

1. **Declare ALL boundaries** in `seams.json` beside the film, **before**
   the master timeline exists — the ledger is what forces the seam design.
   A 22-cut film with 4 declared seams has 18 unaudited cuts. Opt a boundary
   out only when it is genuinely not a cut, with the reason in `_doc`.
2. **`crossfade: 0` is not a taste.** The gate's `zero-overlap` row fails
   any frame showing both sides, and a 0.2 s crossfade puts both sides up
   for six frames at every cut. The film is cut, not dissolved — so each
   side of every cut must carry its own motion (no settled exits, no
   from-rest entries).
3. Pick one **current** (e.g. every ordinary seam a cut-the-curve LEFT, the
   entry ≈120 % of the exit rate so the vector is picked up mid-flight) and
   reserve **≤3 Z vectors** for boundaries the narration itself marks — a
   register handoff, an arrival. Spending a reserved vector on an ordinary
   cut is the "everything is dramatic" failure.
4. Expose the **~15-line `__player` shim** in the shipped file — bridge the
   runtime's master timeline to `window.__player` (`pause`/`play`/`seek`/
   `duration`) plus `window.__playerReady` and `window.__renderReady` — so
   the gate is re-runnable by anyone against the delivered artifact. The
   render check (§8) reuses the same shim. Verbatim pattern in
   `../staging/references/seam-gate.md`.
5. **Run the gate** from the repo root, and require exit 0:

   ```bash
   node skills/staging/tools/seam-gate.mjs verify \
     --ledger <film>/seams.json \
     --url http://127.0.0.1:1 \
     --comp-url "file://$PWD/<film>/explainer.html"
   ```

   `--url` is required-but-unused (the dead address skips the server-spawn
   branch); `--comp-url` is what is navigated. **Never pass `--project`** —
   that branch runs `npx --yes hyperframes preview` and installs from the
   network.
6. Cut times are the cumulative durations **the page is actually running**;
   if those are estimates, the ledger is in estimate time and says so. Any
   edit to a scene's first/last ~1 s, or to any duration, invalidates every
   later boundary's audit — re-derive and re-run, and note it in `_doc`.

## 6. Renderer reality — GSAP may not be installable

The house pilot selected the GSAP adapter, but `renderers/gsap/` ships
without `node_modules` in most snapshots and npm installs are usually out of
scope. The renderer contract survives the adapter; take the first of:

1. **Vendored GSAP, no npm** — verbatim copies of `gsap.js`, `drawsvg.js`
   and the pipeline's `gsap-explainer.js` runtime already extracted from
   the platform repo's committed bundle live at
   `<loom-bakeoff sandbox>/tracks/video/hyperframes/tools/vendor/` (local sandbox); inline them at
   build time as the hybrid's `build.mjs` does. Gotchas that carry:
   `ctx.flex(ctx.hold(...))` smears the choreography (use a `flexHold`
   helper); `ctx.draw` destroys dash patterns (`data-draw="reveal"`); and
   **GSAP suppresses `onUpdate` callbacks on a seek** — a counter or figure
   driven by `onUpdate` plays live but freezes under both gates, and an
   unverifiable ornament is the easiest kind to keep. Don't build one.
2. **The hand-rolled driver** — the sanctioned fallback, proven on two runs:
   a ~90-line dependency-free script that reproduces the adapter's timing
   model exactly (injected-else-fallback durations, natural-pace authoring
   via `data-at` cues, hold-or-compress reconciliation with a named warning,
   `done`/`doneReason` discipline, watchdog). Full annotated pattern and the
   timing model it must reproduce: `references/driver-pattern.md`.

Either way, **flex the slack**: a measured take that runs long buys longer
*holds distributed across the scene's rests*, never a slower diagram and
never one terminal freeze — the render check's front-load probe (§8)
enforces this.

## 7. Diagram and code-on-screen grammar

Explainer subjects are mostly *record shapes* (a JSON fact, a YAML warrant,
a table, a chain, a cell diagram), not chart data, and no donor skill ships
a grammar for them. This skill does: size floors (mono ≥23 px at 1080p),
line budgets (≤11 lines, one record per scene), syntax colouring inside the
brand contract's accent rule, and **build-in-narration-order** — every
progressive reveal follows the sentence being spoken, and code blocks appear
as blocks, never typed. Full grammar: `references/screen-grammar.md`.

**Brand.** This skill carries no hard brand gates of its own: a film inherits
its brand through the film's design and — when one resolves (the deck-author
skill's resolution order: an explicit path, `brand.toml` at the consuming
repo's root, or the shipped default instance at
`../deck-author/brands/medici/brand.toml`) — through the same `brand.toml`
contract: its marks, its palette, its accent as the emphasis colour. Schema:
`../deck-author/references/brand-contract.md`. With no contract, the film is
brand-neutral by the same honesty rule deck-author states. For genuine chart
scenes (a curve, a plotted formula) the house dataviz discipline applies
unchanged: validated palette, direct labels in text tokens, one axis, and
the renderer as a clock over a hand-written sampler, not a maths engine.

## 8. The render-and-look gate — mandatory

Headless render check plus a human or model **actually looking at frames**.
Automated assertions catch overflow and contract breaks; the defects that
survive them — an illegible soft-wrap reading as a second command, a stamp
landing on legible text, a scene that plays out in three seconds and sits
still for seventeen — are invisible to measurement and obvious to an eye.
*An overflow measurement tests whether pixels are inside the frame, not
whether the frame is legible.*

Required, all of it: zero page/console errors, zero off-`file://` requests,
fonts resolved, scenes == SCRIPT rows, one `SCENE_DURATIONS` assignment,
nothing overflowing the 1920×1080 stage (measured per element, seeked —
off-frame elements can be clipped invisible by their own container), the
front-load probe (visible content at 85 % of each slot ≥ at 15 %),
**both duration paths** (injected through the pipeline's own regex, and
fallback) reaching `done=1 reason=complete` on the right array, ≥6
screenshots **including mid-animation ones**, and a **negative control
proven to actually be negative** — a deliberately broken build must report
`doneReason=error`, and you must confirm the breakage is real (two of three
naive controls in the exemplar run passed because the film was fine, not
because the control worked). Playwright recipe, the exact assertions, and
the negative-control lore: `references/render-check.md`.

Then look: open the screenshots, mid-animation ones first, and read every
frame as a viewer. Record what the looking found.

## 8b. Wall-clock discipline under the recorder — mandatory

A 2026-08 render shipped a 12:14 film against a 7:06 script with every gate
green. The mechanism was **not** recorder lag: the per-scene TTS produced one
runaway take (327.68 s of continuous speech for a 25.71 s row), the pipeline
measured it and injected it into `SCENE_DURATIONS`, and every downstream
guard — the scene scaling, the film's watchdog, `record.mjs`'s wait budget —
**trusted the poisoned number**, so the film obediently held one scene for
five and a half minutes and reported `doneReason=complete`. The injected
array is a *measurement*, and a measurement can be wrong; nothing downstream
of the injection may treat it as ground truth against the authored script.

Four rules, all mandatory:

1. **Take-sanity gate in the film.** On the injected path, compare every
   injected duration against the authored estimate (`FALLBACK`). Real TTS
   pacing drifts ~1.0–1.4× off a wpm estimate; it never explodes past it.
   Fail the render (`doneReason=error`, naming the scene) when a scene's
   measured duration exceeds `max(authored × 1.8, authored + 8 s)` or the
   total exceeds authored × 1.3 — a runaway take must produce a **red
   render**, never a long one. (Patched into the hybrid and animated
   exemplar films 2026-08-18; poisoned-injection test fails in <1 s.)
2. **lagSmoothing(0) on the LIVE ticker.** GSAP's default lag smoothing
   (`500ms/33ms`) freezes timeline time during jank, stretching wall clock
   under load. Call `gsap.ticker.lagSmoothing(0)` on the gsap instance that
   actually drives the master timeline — and *prove* it executes with the
   sync telemetry below, because a call sitting in dead adapter code passes
   every grep. Hand-rolled drivers must sequence on **elapsed time**
   (`performance.now()` deltas), never by counting rAF frames.
3. **Per-frame cost budget.** Every scene must hold real time at 1920×1080
   *with `recordVideo` on* — the recorder is part of the load. If a scene's
   sync drift exceeds ~2 % under recording conditions, cheapen the frame
   (canvas-bake grain/atmosphere as the staged-animated film does, reduce
   filter/blur/glow work) until it holds; do not accept the drift.
4. **Sync telemetry + webm proof in the render gate.** The film logs
   `[sync] scene N timeline=Xs wall=Ys drift=Zs` at every scene boundary
   (and exposes `__explainer.syncMarks`). Verification runs `record.mjs`
   (or an equivalent `recordVideo` run) for real and asserts: every
   boundary drift within ~2 % of elapsed, `doneReason=complete`, and
   **webm duration within 2 % of sum(SCENE_DURATIONS) + tail + ~1.5 s
   pad**. The webm is the test; the mp4 encode stays the human's (§9).

Recipe and measured exemplar numbers: `references/render-check.md`.

> **Flag — packaged copy out of date:** the video-author skill copy packaged
> on medici-platform **PR #109** predates this section and needs the same
> patch (take-sanity gate + wall-clock discipline + webm verification). Do
> not edit that PR's worktree from here — a sibling session owns it; carry
> this section over there.

## 9. The human render boundary

This skill's deliverables end at **`SCRIPT.md` + `explainer.html`** (with
`staging.yaml`, the motion-spec instance, `seams.json`, `frames/` and NOTES
beside them). The human runs the mp4 render through the house
`explainer-video` tool — TTS, audio assembly, injection, recording, encode
are theirs. Never run the TTS/render pipeline yourself, never pick the voice
profile unilaterally (name the candidates; write the script so either
renders without an edit), and never commit an mp4 anywhere.

## 10. Worked example

`<loom-bakeoff sandbox>/tracks/video/hybrid/loom/` (the local loom-bakeoff sandbox) is the exemplar run of this exact
process end to end: `staging.yaml` (the relay classification, derived
windows, full `motion_budget`), `SCRIPT.md` (two registers at two wpm),
`motion-spec.md` (locked, audited, the easing FAIL that §4 resolves),
`seams.json` (all 22 boundaries, 2 reserved Z vectors, 0 fail),
`explainer.html` (self-contained, shimmed), `frames/` (15 shots), and
`NOTES.md` — read its register-fork decision, its ornament-gate cuts, and
its honest ledger before authoring your first film. Build tooling worth
copying: `<loom-bakeoff sandbox>/tracks/video/hybrid/build/` (`build.mjs`, `render-check.mjs`).
