## free

**Contender:** `algorithmic-art` (Anthropic's algorithmic-art skill, p5.js + seeded randomness).
**Movement authored for this brief:** **INVARIANT DRIFT** — `free/PHILOSOPHY.md`.
**Artifacts:** 3 decks × 14 slides, 3 explainers (120 s / 132 s / 143 s) + 3 SCRIPT.md,
plus the skill's own interactive viewer artifact at `free/viewer.html`.

### The one-line idea

The whole design is a single generative system: a **closed population of collateral quanta**
that may migrate between two basins (P and N) but may never be created or destroyed. Basin
*area* is proportional to share, so `area(P) + area(N)` is constant by construction; the
hairline **ledger bar** and the **payoff census curve** are both *counted from the live
population every frame*, never computed from the closed form the population happens to obey.
Which means: if `P + N ≡ collateral` ever broke, the drawing would show it break. The deck's
backplates and the explainer's motion are the same algorithm at different parameter settings.

The four things the parent brief asked to be emergent, and the parameter each one is:

| Message | Emergent from | Not drawn as |
|---|---|---|
| the P/N split | `split: 0→1` — one body separates into two basins whose areas are `S/x` and `1−S/x` | a two-box diagram |
| `P + N ≡ collateral` | the ledger bar's length = `count(alive)/count`, measured each frame | a labelled equation |
| the payoff at maturity | `x` sweeps; the census **counts** the population at each price and stamps it; the curve draws itself, flat-topped at 1.00 | a plotted `S/x` line |
| the refused liquidation | `scanMode:'seek'` sweeps the axis testing the measured census for a shortfall, finds none, dissolves | a red X over a threshold |
| **and the counter-example** | `conserve:false` — one boolean. The same scan latches, quanta are annihilated top-of-stack down, the ledger collapses to zero | a second, different picture |

That last row is the design's actual argument: Black Thursday and the Medici payoff are the
**same algorithm one parameter apart**. Nothing else in the deck is asked to carry it.

### Time to artifact (wall clock, single session 18:37 → 19:10)

| Step | Elapsed |
|---|---|
| Read BRIEF + DESIGN-TASK + 3 staging.yaml + SKILL.md | 3 min |
| `curl` p5.js 1.9.4 → `vendor/` (the one permitted fetch) | 20 s |
| **Step 1 of the skill — PHILOSOPHY.md** (movement + conceptual seed) | 4 min |
| **Step 2 — `_src/engine.js`**, the generative system (~330 lines) | 6 min |
| Content transcription, 3 × `_src/content/*.json` (claims verbatim + per-slide seeds + per-scene motion trajectories) | 9 min |
| Deck + explainer CSS/JS/build.py | 5 min |
| **First build of all 6 artifacts** | **0.03 s** |
| Verification (4 harnesses) + 2 layout fixes found by them | 8 min |
| `viewer.html` (skill's own template artifact) | 3 min |
| NOTES | 4 min |

Marginal cost of the 2nd and 3rd deck+explainer pair: **essentially zero** — one shared
engine, three content files. That is the strongest practical property of this approach and
the reason the per-artifact number is meaningless on its own.

### The tool's process, as actually run

The skill prescribes: (1) write an algorithmic philosophy → .md; (2) deduce a conceptual seed;
(3) express it in p5.js from `templates/viewer.html`. All three were run, in order, and the
philosophy was written **before** any code — which mattered: the "census is the only chart"
and "nothing may be respawned or culled" clauses in the manifesto are what forced the payoff
curve to be *measured* rather than plotted, and that measurement is the whole design.

- `templates/viewer.html` was used as the literal starting point for `free/viewer.html`:
  layout, Anthropic palette/Poppins+Lora, the Seed block and the Actions block are the
  template's, unchanged. Replaced: the algorithm, the 14 parameters and their controls.
- `templates/generator_template.js` was used for structure (one `params` object, seeded init,
  `updateParam`/`regenerate`/`reset`, palette-from-hex helper) — not for the flow-field example.
- Seeded randomness per the skill's Art Blocks pattern, but hardened: structure comes from a
  local **mulberry32** PRNG rather than p5's global `randomSeed`, so the composition survives
  any other code touching p5's global state. `noiseSeed()` is set once at init.
- Deck determinism: seed = `seedBase + slot number` (staging 3441–3454, presentation-writing
  1321–1334, pitch-deck-mastery 1431–1444). Slide 8 of the staging deck is byte-identical on
  every load, forever. The seed is printed on every slide, top right.
- Default population = **344 quanta** (Canton's $344B). Quiet, not announced — the skill's
  "conceptual seed" instruction taken literally.

### What freedom bought (free mode)

- **Palette:** ink `#06080C`, P cyan `#6FD6FF`, N amber `#FFA94D`, annihilation `#FF4D5E`.
  Colour is *derived*, never chosen: hue from allegiance, luminance from speed, alpha from
  density. Nothing in the palette responds to time, which is why a churning field reads as
  still.
- **Type:** Instrument Serif (display) / Inter (body) / JetBrains Mono (data + eyebrows), via
  the one Google Fonts link `free` permits. Editorial-technical, not deck-template.
- **Layout:** one rule, "type left, algorithm right", with three variants (`full` for cover
  and end, `left`, `figure` where the census needs room). Slides never fight the field: a
  left-to-right CSS scrim carries the type, so the canvas veil can stay low (0.40–0.58) and
  the art stays vivid on the right third instead of being greyed to wallpaper.
- **Motion vocabulary** mapped 1:1 onto the contracts' own `motion_role`s — `hold`,
  `accumulate`, `strain`, `rupture`, `assemble`, `divest`, `arrest`, `cadence` — so quiet
  scenes are genuinely quiet (drift ≈ 0.1, turbulence ≈ 0.12) and the two peaks per film are
  the only places the population or the scan changes state.

### Verification — 4 harnesses, no browser

No puppeteer/playwright is installed, so per the DESIGN-TASK fallback I built the checks in
node + python3. All four are re-runnable.

1. **`harness.js`** — stubs p5 + DOM, `eval`s the real `engine.js` / `deck.js` / `explainer.js`,
   walks all 42 slides and all 25 scenes. *Result: no runtime errors; `max|P+N−1| = 0` over 61
   prices before and after 400 frames; `conserve:false` collapses the measured total to 0.003;
   same seed → identical census.*
2. **`geom.js`** — captures every crisp overlay primitive (census polygons, ledger, scan line)
   per slide and per explainer frame at 12 fps, and tests each against the type box.
   *Result: 0 collisions across 42 slides and 25 scenes.* This found two real layout bugs
   (the ledger bar ran under the text column on the `left` layout; the census panel clipped
   the explainer's caption block) that reading the code had not.
3. **`motion.js`** — plays every scene through the real clock and **measures the live
   population every frame**. *Result: 22 of 25 scenes hold `P+N = 1.000000` for every frame;
   the 3 annihilation scenes (staging s4, presentation-writing s3, pitch-deck-mastery s2)
   collapse to 0.003.* This is the check that proves the motion carries the meaning rather
   than depicting it.
4. **`validate.py`** — structure per the quality floor: slide count == slot count, footer on
   every slide, `<meta name="deck-footer">` exact, `@page {size:1280px 720px}`, keyboard +
   click nav, counter, `window.__player`, `?scene=N`, per-scene `data-dur` == the contract's
   `vo_seconds` and their sum == runtime, SCRIPT.md row count == scene count, VO verbatim,
   every headline claim and every supporting point present verbatim, slot order preserved, no
   remote resource refs except Google Fonts, body ≥ 19 px / explainer ≥ 26 px.
   *Result: ALL CHECKS PASSED — 0 failures.*

**Not done:** an actual pixel look-pass. A Chrome browser was connected, but the browser tool
requires the user to pick the browser through a consent prompt this sub-agent cannot raise, so
I did not drive it. The visuals are verified by geometry and by execution, not by eye — that
is the single real gap in this contender's evidence and it should be read as such.

### Linter (`skills/deck-author/tools/check_deck.py`)

The linter is a **brand-contract** checker; `free` mode is defined as having no brand. Run
anyway, for information, on all three decks: **40 errors each**, and they decompose cleanly:

- **Deliberate, licensed by `free`** (36): `H-FONT-PIN` × 8 (Instrument Serif / Inter /
  JetBrains Mono / Georgia / Segoe UI fallbacks vs the pinned IBM Plex set), `H-LAYOUT-POOL`
  × 14 (my `full` / `left` / `figure` pool vs the house's `L-*` pool), `H-GEOMETRY` (the house
  wants the letterbox scale in CSS; mine is a JS `transform` on a fixed 1280×720 stage,
  which is what DESIGN-TASK actually asks for), plus the rest of the brand surface.
- **Fixed after the first run** (1): `H-FOLIO` wanted `.folio` / `.slide-no` on the slide
  number. Free costs me nothing to interoperate — the counter now carries
  `class="count folio slide-no"`.
- **Genuinely wrong about my deck** (1): `H-FOOTER-PRINT` demands a `.slide::after` print
  rule. My footer is a real `<footer>` element *inside every slide*, so it prints on every
  page by construction; the linter tests for one mechanism rather than for the outcome.
- **Linter defects** (2): `H-ASSET-EXISTS` reports two "missing local assets" named
  `.concat(e,` and `+ url + ` — its asset regex is matching JavaScript string fragments
  inside the inlined p5.js. Any deck that inlines a minified library will trip this.

Its `GHOST DECK` output (headlines read as one paragraph) is the most useful thing it printed
and all three decks read as a coherent argument in that form.

### Slots rendered, and the one judgement call

**Every slot and every scene in all three contracts is rendered.** Nothing dropped.

- `pitch-deck-mastery` carries a 14th deck item under `deck.appendix` (`A1`, roadmap /
  compliance / identity), outside its 13-slot `slots` list. **Rendered as slide 14**, marked
  `APPENDIX` in the eyebrow, after slot 13 — order preserved, nothing reordered. Dropping it
  silently was not an option; renumbering the 13 would have been worse. Flagging the call
  here per the contract's instruction.
- `pitch-deck-mastery` slot 4 carries a `diagram:` field — a prose spec for exactly the figure
  this design produces generatively (P flat to the strike then `S/x`, N stacked above, flat
  top edge, "annotate the absence" where a lending market would draw its threshold). It is
  implemented as the measured census + the seeking line, not printed as text; slots 4 and 5
  carry a one-line `figNote` naming what the figure is doing.
- `presentation-writing`'s deck has a `transitions` block of spoken bridge lines. Those are
  presenter script, not slide content, so they are not on the slides. They are in the
  contract and recoverable; noted rather than dropped.

### Where generative art HELPED the message

1. **The invariant.** A bar whose length is a *count* is the strongest possible rendering of
   `P + N ≡ collateral`, because the viewer watches the joint slide across the whole price
   sweep and the ends never move. A drawn equation asks for belief; a measured bar doesn't.
2. **The payoff at maturity.** Letting the curve accumulate out of a census — one stamped
   sample per price — makes `S/x` feel *observed*. It also delivers brief goal 3 (a diagram
   they could redraw) better than a chart would, because the viewer sees it being built.
3. **Black Thursday vs. Medici as one parameter.** This is the thing no static design can do.
   The rupture scene and the mechanism scene are the same code, the same population, the same
   colours; `conserve` is the only difference. The film argues by A/B on itself.
4. **The arrest.** `pitch-deck-mastery` scene 5 asks for a gesture that *begins and does not
   complete*. A generative system does that natively — the same strain build, the same mark
   at 0.66, and then nothing latches because there is nothing to latch on. Motion is the only
   medium in which an *absence* is legible.
5. **Deck coherence for free.** Fourteen backplates that are provably the same system in
   different states give the deck a family resemblance that no template library produces, at
   ~1 KB of per-slide configuration.

### Where it OBSCURED, or nearly did

1. **The backplate wants to be looked at.** First pass had veil ≈ 0.42 across the whole
   1280×720 and the field genuinely competed with the headline. The fix was not "turn the art
   down" but "give the art its own third": type left under a CSS scrim, algorithm right. If
   the layout had stayed full-bleed this contender would have lost on legibility.
2. **Quiet scenes are hard to keep quiet.** A living field always moves. `s5` (staging),
   `s4` (presentation-writing) and `s6` (pitch-deck-mastery) are contractually the *payment*
   for the peaks, and drift had to be pushed to 0.10–0.32 — nearly frozen — before they read
   as still rather than as idling. Generative motion has a floor that a static frame does not,
   and the contracts' motion budgets are written assuming that floor is zero.
3. **The census panel is not a chart and should not be mistaken for one.** It has no tick
   labels, no axis numbers, no units — deliberately, because inventing any would breach "no
   figure that doesn't trace to the contract". A reader who wants to read `S/x` off it at a
   specific price cannot. The slide text carries the arithmetic; the figure carries the shape.
   That is the right split for this audience, but it is a real limit and a reviewer should
   decide whether the deck needs a labelled table somewhere.
4. **Two slides where the field adds nothing.** `d12` / slot 12 ("nothing is on mainnet") and
   slot 12 ("five to ten basis points, no token") are register-of-record slides with no
   mechanism in them. The field there is dimmed almost to nothing (bloom 0.65–0.70, drift
   0.26–0.28) because anything livelier would be decoration — which the brief forbids. Honest
   answer: on those slides the generative system is doing nothing the message needs.
5. **Print is a compromise.** A living canvas cannot print. On `beforeprint` the deck walks
   all 14 slides, settles each one deterministically, and stamps a PNG snapshot into that
   slide's background — so the PDF is the real art, but it is one frozen frame of it, and the
   ~14 canvas renders make printing take a beat. If the snapshot path fails the slides fall
   back to flat ink, which is safe but plain.

### Friction and overrides

- **The skill's default output is one artwork, not six documents.** Its shape ("a single
  self-contained HTML artifact with a sidebar") had to be *inverted*: the sidebar viewer became
  the by-product (`free/viewer.html`, built faithfully from the template) and the real
  deliverables are decks/explainers that embed the same engine headlessly. The skill has
  nothing to say about slides, timelines or narration; everything above the engine layer is
  outside its scope and had to be invented. That is the honest cost of using an art skill as a
  design system.
- **p5 CDN vs self-contained.** The skill's template loads p5 from cdnjs; DESIGN-TASK forbids
  remote assets. p5.js 1.9.4 was fetched once to `tracks/algorithmic-art/vendor/` and is
  **inlined** into all seven HTML files (≈1.03 MB each, ≈1.1 MB per artifact). Fully offline,
  at the cost of file size.
- **p5's global state.** `randomSeed`/`noiseSeed` are global; with several sketches alive at
  once (the viewer recreates one per parameter change) determinism would rot. Overridden with
  a per-field mulberry32 and an explicit `field.p5.remove()` on rebuild.
- **Trails vs overlays.** Accumulating trails and crisp figures cannot share one buffer. Split
  into a p5 `createGraphics` layer for the field (trail decay per frame) composited under a
  veil, with census/ledger/scan drawn crisply on the main canvas. Without this the census
  curve smears.
- **Contract fidelity is manual.** Nothing in the toolchain enforces "claims verbatim, slots
  in order" — I added those assertions to `validate.py` myself (all 45/39/63 supporting points
  and all 42 headline claims are checked byte-for-byte against the YAML).

### What the tool refused / could not express

- **Nothing refused.** The skill has no guardrails that fired.
- **Could not express, natively:** typography, slide layout, a scene timeline, narration
  timing, print pagination, contract fidelity. All six were built around it. The skill is a
  generative-art skill; treating it as a deck tool means writing the deck tool.
- **Could not express, in principle:** a *labelled* quantitative figure. The system's honesty
  rule ("the census counts, it never computes") is also its limit — the curve is real but
  unannotated, and any axis labels would have to be drawn by hand outside the algorithm.
- **A comparison table.** `d4`, `d9`, slot 9, slot 11 are comparisons; the field can hold two
  climates side by side but it cannot make a table. Those slides are carried by the text and
  the split-basin backplate, which is weaker than a real two-column table would be.

### Reproducing

```
python3 /Users/iholsman/jojig/Lending/rwa-bakeoff/tracks/algorithmic-art/free/_src/build.py
```
Rebuilds all six artifacts (0.03 s) from `_src/engine.js` + `_src/content/*.json`.
`free/viewer.html` is built by the same inline step documented at the top of `_src/viewer_src.html`.

---

## brand

**Contender:** `algorithmic-art` (Anthropic's algorithmic-art skill, p5.js + seeded randomness).
**Mode:** `brand` — house pin (true-black canvas, Electric Blue #3366FF as the one frequent
colour, greys, self-hosted IBM Plex Sans/Mono, external footer on every surface).
**Movement authored for this mode:** **CONSERVED ENTRY** — `brand/PHILOSOPHY.md`.
**Artifacts:** 3 decks × 14 slides, 3 explainers (120 s / 132 s / 143 s) + 3 `SCRIPT.md`,
plus the skill's interactive viewer artifact re-skinned to the house brand at `brand/PLATES.html`.

*(Written by the brand-mode agent. The `## free` section above was authored independently
and concurrently by the free-mode agent; the two converged on a conserved-population idea
without coordination, which is itself a finding about this skill — see "What the tool did"
below.)*

### The one-line idea

One law, enforced in code, carries the whole argument: **the population is fixed at 1000
particles before the first frame, and nothing is ever created or respawned.** Particles are
*returned* at the boundary, never re-seeded; a fade is a fade of luminance, never of
population. The `census · P … · N … · Σ …` readout on every slide and every scene is
**counted from the live particle population**, not printed from the closed form — so if
`P + N ≡ collateral` ever failed, the readout would say so. Exactly one scene per film is
permitted to break the law, and it is the March-2020 scene.

Two geometries share the one solver:

| Geometry | What it is | What it renders |
|---|---|---|
| `basin` | two-well potential over three-octave Perlin noise; the population settles between the wells in the ratio `min(1, S/x)` | the split, the strain, the rupture, the scoped lenses, the recombination |
| `ledger` | the frame's vertical extent **is** one unit of collateral; every particle holds a stable rank `u ∈ [0,1)` as its row, and is P if `u < min(1, S/x)` **at its own x** | the payoff. The blue/grey boundary *is* the `S/x` curve; the flat top edge *is* the invariant. Nobody draws either. |

The four things the parent brief required to be emergent, and the parameter each one is:

| Message | Emergent from | Explicitly **not** |
|---|---|---|
| the P/N split | `split` 0→1 separating one basin into two of unequal density | two labelled boxes with an arrow |
| `P + N ≡ collateral` | a conserved particle **count**; the census is a trial balance struck every frame; in `ledger` the top edge is flat because the count cannot change | a caption asserting an identity |
| the payoff at maturity | `drive = x/S` sweeping; particles change allegiance in rank order, so the colour boundary traces `S/x` | a plotted chart with axes |
| the refused liquidation | `seek` — a scan that traverses every price looking for a column summing to less than one, decelerates, and dissolves *without arriving* | a red line with a cross through it |

Seeds: `seed_of(slot_id)` (FNV-1a over the slot/scene id) → the deck is byte-deterministic;
the same slide is the same plate on every open, in the browser and in the PDF.

### Time to artifact (wall clock, one agent)

| Stage | Elapsed | Note |
|---|---|---|
| Read brief + 3 contracts + brand guide + skeleton + linter source | 0:00 → 0:05 | reading `check_deck.py`'s rule table first paid for itself: zero linter errors on the first run |
| `PHILOSOPHY.md` (skill step 1) | 0:05 → 0:08 | 6 paragraphs + the conceptual seed |
| `build/ce-engine.js` — the p5 engine (skill step 2) | 0:08 → 0:12 | conservation solver, two geometries, the four registers |
| `build/build.py` + `build/content.py` — contracts transcribed, all 6 artifacts | 0:12 → 0:14 | **first complete set of six at 0:14** |
| `check_deck.py` on all three decks | 0:15 | PASS ×3, first run, no fixes |
| Render-and-look loop (headless Chrome, ~40 screenshots) | 0:15 → 0:33 | the real cost — see friction |
| `brand/PLATES.html` (skill's viewer artifact, re-skinned) | 0:33 → 0:36 | |
| Notes | 0:36 → 0:42 | |

Rebuild of all six artifacts from source: **0.2 s** (`python3 build/content.py`).

### The tool's process, as actually run

The skill prescribes two steps and a template. I ran all three, in order:

1. **ALGORITHMIC PHILOSOPHY CREATION** — `brand/PHILOSOPHY.md`, six paragraphs, named
   movement, the craftsmanship framing the skill demands repeatedly, ending with the
   skill's **DEDUCING THE CONCEPTUAL SEED** step: the seed is Renaissance *double entry* —
   the population is the ledger total, the two basins are the two columns, the census is the
   trial balance, and the rupture is what a bank looks like when its books stop balancing.
   Nothing on any slide says any of that.
2. **STEP 0: READ THE TEMPLATE FIRST** — read `templates/viewer.html` and
   `templates/generator_template.js` before writing a line of p5. `generator_template.js`'s
   structure was followed literally: one `params` object, `randomSeed(seed)` +
   `noiseSeed(seed)` at construction, entity class with `update`/`display` split,
   `noLoop()` for the static plates, live `draw()` for the film.
3. **P5.JS IMPLEMENTATION** — `build/ce-engine.js`, p5 **instance mode** (14 canvases on one
   deck page; global mode cannot do that). `CE.plate()` = a static deterministic backplate,
   205 accumulation passes then still. `CE.film()` = one live 1920×1080 field driven by the
   player clock.
4. **INTERACTIVE ARTIFACT** — `brand/PLATES.html`, keeping every FIXED feature the skill
   lists (seed display, prev/next/random/jump, parameter sliders, regenerate, reset,
   download PNG) and replacing the branding (see brand fights).

References used: the skill's `SKILL.md` end-to-end, both templates, `house-brand-guide.md`
§2/§3/§9/§10, `brands/medici/brand.toml`, `deck-skeleton-external.html` (the deck's CSS,
stage geometry, nav and print rules are the skeleton's, unchanged), and
`tools/check_deck.py`'s rule table read as source.

### Where the generative art HELPED the message

- **The mechanism slide is the strongest artifact in the set.** In `ledger` geometry the
  colour boundary *is* `S/x` and the top edge *is* the invariant, so slide 8 (staging) /
  7 (presentation-writing) / 4 (pitch-deck-mastery) satisfies brief goal 3 — "one diagram
  they could redraw" — without a diagram existing anywhere in the code. A viewer can read
  the two branches off the picture and check them against the census in the corner.
- **The census made the deck honest.** Because the readout is a particle count, every number
  on those plates is checkable: at `x/S = 1.56` the plate reads `P 0.641 · N 0.359 · Σ 1.000`,
  and 0.641 is 1/1.56. The build script precomputes the same value from the closed form and
  the JS overwrites it from the live count; a disagreement would be visible.
- **The refused liquidation.** An absence is the hardest thing to draw. Rendering it as a
  *motion that does not complete* — a scan that decelerates and dissolves mid-axis, in the
  same visual vocabulary the rupture used — is something a static diagram cannot do at all,
  and it is exactly what two of the three contracts stage as their bold moment.
- **The one broken law.** Spending 100+ frames proving nothing is ever lost, then annihilating
  the population once, buys the March-2020 beat a reaction no headline gets. The census
  falling to `Σ 0.000 · conservation off` under the sentence is the whole point of having
  built a conservation solver rather than a flow field.
- **Quiet stayed quiet, cheaply.** `energy 0.11` on the pivot scenes produces a field that is
  present and almost motionless, which is what the contracts' `hold` / `divest` roles ask for.
  Motion budget compliance fell out of the parameters instead of needing discipline.

### Where it OBSCURED the message — and what was done

- **First pass was unreadable.** At the tuned-for-print alpha the plates were near-invisible
  at slide scale, and at the first legible setting the `ledger` field ran under the body text
  and cut its contrast. Fixed structurally, not by dimming: every plate declares a `box`
  (the region the field may occupy) and a `mask` (a gradient that drives the field to true
  black where words live), plus a `veil`. The diagram slides got a `left-tight` mask and a
  narrower text column so the field and the text never overlap at all.
- **`ledger` legibility was a real fight.** Three iterations: particles born off their rows
  drew vertical strikes across the payoff; a stiff row-spring turned the field into
  scanlines; too much travel smeared the colour boundary. Landed on: seed particles *on*
  their rows at construction, a clamped soft spring, low turbulence, low energy.
- **Basin plates on dense slides read as texture, not as meaning.** On `L-TABLE` /
  `L-STAT-ROW` slides with five long bullets, the field is decoration — it carries no clause
  of the claim. Kept deliberately faint there and treated as a backplate; the honest note is
  that on those six or seven slides the generative layer is atmosphere, not argument.
- **The `strain` register is ambiguous.** "Turbulence rising, wells shallow, population not
  settling" reads as *unrest* but a viewer will not decode it as "this collateral cannot be
  sold in one transaction" without the headline. It supports the sentence; it does not carry it.
- **Colour ratio tension, declared.** Brand §2.6 puts Electric Blue at 3–5 % of a surface. But
  §2.1 makes blue the P-token colour, and on several plates P is the *majority* leg, so blue
  is the dominant hue in the field region. Resolved by pulling blue's render multiplier down
  to 1.15 and grey's up to 0.92, and by keeping the field to a boxed region behind a veil —
  blue is roughly 5–8 % of a diagram slide. That is over the letter of §2.6 and is called
  out here rather than hidden; the alternative (P in grey) would break the §2.1 semantic pin.

### Brand fights

1. **The skill's template is the fight.** `templates/viewer.html` is a hard pin: Anthropic
   palette, Poppins + Lora from the Google Fonts CDN, p5 from cdnjs, light gradient
   background — and the skill says "use it as the LITERAL STARTING POINT", "avoid dark
   themes". Every one of those is forbidden in brand mode (§3.1 "self-host, never a CDN";
   §10.3 dark external surface; the linter errors on any remote `src`). **Override:** kept
   the template's *structure and required features* (sidebar order Seed → Parameters →
   Actions, the exact seed controls, sliders, regenerate/reset/download) and replaced its
   *branding* wholesale. `brand/PLATES.html` is that artifact. Logged as an override, not a
   silent deviation.
2. **p5 from a CDN.** Not permitted. `p5.min.js` v1.9.4 was fetched **once** to
   `vendor/p5.min.js` (the one network call the task allows) and every HTML references it
   relatively (`../../../vendor/p5.min.js`). The six artifacts are otherwise fully
   self-contained: engine inlined, fonts copied beside each HTML, no other external asset.
   Cost: an artifact moved out of the tree without `vendor/` beside it will not run.
3. **Gold is out.** Brand §7.2 makes gold `#D4A843` the P-token *chart* line, but the
   contract's `[marks] exempt_colors` limits gold to the mark, and the mode brief pins the
   palette to black/blue/grey. P is Electric Blue, N is grey. Red `#FF4444` appears exactly
   twice in the whole track, both functional: the rupture hairline and the one VO figure
   line under the March-2020 headline.
4. **Source citations could not go on the slides.** The linter's `PROCESS_LEAK` list contains
   `"deck.md"`, and every source string in the contracts is of the form
   `canton-pitch-deck.md Slide 5` — which contains `deck.md` as a substring and hard-fails
   `H-PROCESS-LEAK`. Provenance therefore lives in `staging.yaml` and in this file, not on
   the slide face. Every figure still traces; none is printed with its filename.

### What the tool refused / could not express

- **Nothing typographic.** The skill has no opinion on type, layout, hierarchy or copy — it
  is a *generator*, not a design system. All 14-slide composition, the type scale, the
  masks, the grid and the print rules came from the house skeleton and the brand guide.
  On its own the skill would have produced a beautiful square canvas and no deck.
- **No text rendering in the field.** Deliberately: p5 text on the canvas would not be
  IBM Plex-metric-consistent with the DOM. The four annotation labels on the diagram slides
  (`N`, `P`, `price x →`, `strike S`, `Σ = 1.000`) are DOM spans positioned over the canvas.
  A tool-honest note: those five labels are the one place the artifact *tells* rather than
  *emerges*, and without them the payoff plate is legible but unlabelled.
- **The contracts' spoken transitions are not on any slide.** `transitions:` in all three
  contracts are presenter lines between slots, not slot content; rendering them would have
  put narration on the slide face. They are not dropped — they are the spoken track, and
  they are reproduced in the contracts.
- **`motion_spec_locked`, `seams_declared` and `render_and_look` (staging's design-lane
  gates) were NOT formally run.** No `references/motion-spec.md` or `tools/seam-gate.mjs`
  exists in this bake-off tree. `render_and_look` was run in substance — headless Chrome,
  ~40 screenshots including mid-animation frames at absolute times, zero page errors, scene
  count == script row count, and a model actually looking at every frame — but not against
  that named harness.

### Slots and scenes: all rendered, one override

- **Every slot and every scene of all three contracts is rendered, in contract order, with
  headline claims verbatim.** Deck slide counts: staging 14/14, presentation-writing 14/14,
  pitch-deck-mastery **14** = its 13 slots **plus its `appendix: A1`**, rendered as slide 14
  rather than dropped. Scene counts: 9 / 8 / 8, durations exactly the contracts'
  `vo_seconds` (120 s / 132 s / 143 s).
- **One declared motion override.** `presentation-writing` scene 6 is staged
  `motion_role: rupture, energy 5.0` for "the liquidation line has nowhere to sit". In this
  movement `rupture` means the conservation law is broken and the population is destroyed —
  and that law may break only once per sequence (it breaks in that film at scene 3, Black
  Thursday). Scene 6 is therefore rendered as **threshold-then-seek**: the line is drawn onto
  the payoff, the scan crosses every price, and both dissolve while the census holds
  `Σ 1.000`. Highest *charge*, not highest amplitude — which is the resolution
  `pitch-deck-mastery`'s own `note_on_arrest_at_ceiling` reaches for its scene 5.
- Supporting bullets are transcribed verbatim; the only edits are line-break-level
  (`**bold**` on figures, `mono` on symbols). Two slides per deck lift a figure out of a
  supporting line into a stat tile — the line's own words become the tile caption.

### Friction, in order of cost

1. **p5 instance-mode initialisation order (~10 min, the single biggest bug).** p5 defers
   `setup()` to the `load` event when the document is still parsing, but the sketch function
   runs synchronously — so `film.set()` called on the next line touched a canvas that did not
   exist yet, threw *inside* `p5.min.js`, and surfaced as an opaque cross-origin
   `"Script error."` that killed the rest of the player script. Symptom: the explainer showed
   the wrong scene, no progress bar and a default field. Fixed with a `ready` hook fired at
   the end of `setup()`; everything the player does now starts from there.
2. **Verifying a live film in headless Chrome.** `--virtual-time-budget` advances the clock
   far faster than it runs `requestAnimationFrame`, so a screenshot caught ~1 frame of
   animation and the eased parameters had barely moved off their scene-start values. Fixed
   properly rather than around: added `?t=<seconds>` absolute seeking, and `seedFrame()` —
   push the exact parameters for that instant, re-home the population, settle 70 steps
   silently, then warm 46 painted passes. Any absolute time now renders correctly in one
   frame. Side benefit: seeking in a real browser lands instantly instead of on an empty field.
3. **Live-frame density vs static-plate density.** A deck plate accumulates 205 passes; a
   live frame reaches equilibrium at ~13 passes against the trail decay, so the film was
   about a third as dense as the deck at identical parameters. Added a render `gain` (4.3 in
   the film, 1 in the plates) so one parameter set reads the same in both media.
4. **The `check_deck.py` static-parser rule.** The linter cannot see script-built slides
   (`S-SLIDES` reports 0 and everything downstream is noise). Every slide is therefore static
   markup with the canvas as a backplate — which is the right architecture anyway, because
   it is also what makes `@media print` work.
5. **Deck load cost.** 14 canvases × 1000 particles × 205 passes ≈ 2.9 M line segments. Plates
   render progressively (active slide first, then one per animation frame), and a
   `beforeprint` handler forces the remainder synchronously so PDF export is complete.

### Linter results

`python3 skills/deck-author/tools/check_deck.py <deck>/index.html --brand
skills/deck-author/brands/medici/brand.toml --config skills/deck-author/.deckcheck.json`

| Deck | Result |
|---|---|
| `brand/staging/deck/index.html` | **PASS** — 14 slides, footer class external, 0 errors, 1 notice |
| `brand/presentation-writing/deck/index.html` | **PASS** — 14 slides, footer class external, 0 errors, 1 notice |
| `brand/pitch-deck-mastery/deck/index.html` | **PASS** — 14 slides, footer class external, 0 errors, 1 notice |

The single notice on each is `P-DECKMD-COUNT` (no sibling `deck.md`; story parity not
checked — there is no `deck.md` in this contract, the `staging.yaml` is the story). Two
findings suppressed per deck by the shipped `.deckcheck.json`: `C-PURE-BLACK` / `C-PURE-WHITE`,
both deliberate brand pins. Clean on the **first** run, before any of the visual tuning.

Independent structural check (python3, no browser): 14/14 slides per deck, footer `<meta>`
present, one `.slide::after` print footer matching it exactly, 14 folio markers per deck,
scene count == `SCRIPT.md` row count (9/9, 8/8, 8/8), `window.__player` exposed, footer
string on the explainer stage, **zero `http(s)://` references anywhere in the six artifacts**.

Render-and-look: 14/14 staging slides, 9/9 staging scenes, plus spot frames from both other
tracks and mid-animation frames at absolute times (t = 26 s, 39 s, 72 s, 88 s, 92 s, 100 s),
screenshotted in headless Chrome at 1280×720 and 1920×1080 and inspected. Zero page errors
in the final build.

### Reproducing

```
python3 /Users/iholsman/jojig/Lending/rwa-bakeoff/tracks/algorithmic-art/build/content.py   # the six artifacts
python3 /Users/iholsman/jojig/Lending/rwa-bakeoff/tracks/algorithmic-art/build/viewer.py    # brand/PLATES.html
```

`build/ce-engine.js` is the movement; `build/content.py` is the three contracts transcribed
plus the per-slot parameter mapping; `build/build.py` is the templates and the renderer. The
engine is inlined into each artifact at build time, so the outputs need nothing but
`vendor/p5.min.js` and their own `fonts/`.
