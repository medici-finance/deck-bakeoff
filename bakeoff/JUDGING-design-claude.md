# JUDGING — design leg (Claude)

Judge: Claude, 2026-08-27. Independent; written before Ian's verdict and without reference to it. Read: `BRIEF.md`, `DESIGN-TASK.md`, `bakeoff/PROTOCOL.md`, `bakeoff/JUDGING-messaging-claude.md`, all six `tracks/*/NOTES.md`, all five reviews under `reviews/design/` incl. their `impeccable-polish` addenda, and the three `staging.yaml` contracts. **Looked at:** 44 frames from `shots/_reviewer-frames/` and `shots/impeccable-polish/` — the mechanism slide (staging `d8`) and the bold-moment scene (staging `s4`) of all twelve track-modes, plus cover / `d6` / `d11` / `d14` / `s6` spot frames. No new frames rendered; `_reviewer-frames/` already carries 6 tools × 2 modes × 9 frames.

**Scoring convention.** (a) *tool difficulty* is **inverse** — 10 = the tool fit the job, low = heavy adaptation. **No tool scores above 7, because all six had to build the timed-explainer engine themselves.** The clock, `data-dur`, `?scene=N`, the progress bar and `window.__player` are outside every one of the six skills; the eight motion verbs (`hold / accumulate / strain / rupture / assemble / arrest / divest / cadence`) come from the *messaging* contracts' `motion_role` field. (b) is representation quality against the brief's three educational goals. (c) is the per-tool brand→free delta.

---

## 1. Per-tool scorecards

| tool | brand (a)/(b) | free (a)/(b) | (c) delta | does `free` still read as Medici? |
|---|---|---|---|---|
| canvas-design | **3 / 9** | 3 / 7 | **−1.5** | structurally yes (same conserved-line system); reads as a maths monograph |
| algorithmic-art | 3 / 3 | 4 / 4 | +1 | no |
| impeccable | 5 / 7 | 5 / 7 | +0.5 | **more than its brand mode** — the name is the concept |
| impeccable-polish | **7** / 5 | **7** / 5 | +1.4 (inherited, flattened) | no |
| visual-explainer | 5 / 6 | 5 / 7 | +1 | family-adjacent, not this house |
| html-ppt | 4 / 4 | 6 / 7 | **+3** (largest) | no — a light surface with a crimson accent inverts §2.1 |

### canvas-design

**brand (3/9).** The worst fit and the best result. The skill's model is one page ("Output only .md, .pdf, .png", stated three times); no sequence, no motion vocabulary, no HTML, and an ethic — *"never explain, let the composition tell the story"* — that inverts an educational brief. What saved it is one instruction: "systematic reference markers from an imaginary discipline" is the same instruction as the brief's *every figure must trace to a source*, so provenance became a design element rather than a compliance tax — 42/42 exhibits, 42/42 file-level citations, alt-text on every SVG. `d8` is the one payoff diagram a viewer could redraw unaided: stacked P and N, the constant edge at 1.00, the strike marked, **both branches written as arithmetic under the axis** (`x ≤ S → P 1.00 · N 0.00` / `x > S → P S/x · N 1 − S/x`). `d6` and `s4` are the only genuine visual peaks anywhere — 54 hairline marks falling to a zero baseline under one enormous `$0` — and `d14` draws a *non-existence* (seven ⊘ marks, `NO SUCH PRICE EXISTS`), which nothing else attempted. Against that: the least legible deck measured (123/221 strings under 4.5:1; the `SRC ·` line at **1.85:1**) and the only track in 30 decks that **dropped a fact** — d11's roll-cost line, the only contract numbers missing from the entire bake-off, and the *driver* of the −1.25%/yr shown on the same slide. *Best: turned a fact-tracing requirement into the visual system. Worst: set it below the threshold of sight, and lost a fact while reporting "nothing dropped".*

**free (3/7).** Same plate library, warmer skin. It keeps the conserved-line device and gains the field's best "so what" callout (`where a lending market would put its threshold`, pointed at the axis) — then **collides that callout with `P PROTECTED` on D8**, the one slide that must be redrawable. Citations collapse 42/42 → 4/42 the moment the brand stops requiring them. Two contradictory numbering systems (`D3`/`PLATE 04`), all body copy in mono, `Black Thursday` dropped as a name in the pdm lane, zero `prefers-reduced-motion` in either medium. *Best: a device that survives a palette change. Worst: freedom deleted the source line.* **Delta −1.5 — the constraint made the better work.**

### algorithmic-art

**brand (3/3).** A generator with no opinion on type, layout, hierarchy or copy, so the deck tool had to be written around it; p5 instance-mode init order was the biggest single bug in the bake-off; a living canvas cannot print. First-run linter PASS is real credit. The representation is the weakest here. **Slide 08 — the mechanism — is a horizontal noise field with 12px `P`/`N` labels, no 1.00 line, no strike, no axis values.** I looked at it: it reads as a rendering artifact. Goal 3 is unmet. `s4` is a near-black frame with barely-visible wisps, and the measured film barely moves at all (every scene ≤0.28% in-scene pixel change — an `assemble` that does not assemble); its own NOTES concede *"not done: an actual pixel look-pass"*. 0/42 representational exhibits, 4/42 citations, and the contract's `function · beat` vocabulary as every slide's kicker. One finding outranks all of it: `census · P 0.617 · N 0.383 · Σ 1.000` sits where a data readout sits, and **0.617 appears nowhere in `source/medici/`** — a live particle count rendered as a measurement, to a room whose stated distrust is "numbers whose provenance is not named". *Best: the census as a live proof of the invariant — the most argument-serving invention in the bake-off. Worst: it put a render statistic in the evidence zone.*

**free (4/4).** Citations recover to 41/42 and the ledger bar is a strong idea (a bar whose length is a *count*, so the invariant is watched, not asserted). The payoff figure gains visible stacked regions and a flat top edge — still no axis values, no strike label, no numbers. `s4` collides at 1280×720 (header over scene label, footer over the second bullet), prints `SEED 3441…` on every slide, renders the contract's `figures[].name` strings as viewer-facing bullets, and **ships the entire staging contract verbatim as `window.SHOW_DATA` inside a file stamped "Proprietary & Confidential"**. *Best: motion is the only medium in which an absence is legible, and it proved that. Worst: design metadata staged as content, inside a confidential artifact.* **Delta +1; not Medici.**

### impeccable

**brand (5/7).** The best-behaved artifact in the field. `craft-floor.md` drove real checks; the linter's *source* was read rather than its `--help`, which is why it passed first run; and the clearing-house-circular device earns itself on this brief specifically — the audience distrusts unnamed provenance, and a circular makes provenance structural. An `AUTHORITY` line on every slide at 4.89:1 is **the best citation placement in the bake-off** (source *and* as-of at the top, where it is read). Only 2 strings under 4.5:1 across the deck. Zero insider vocabulary reaches the screen (`THE BREACH`, not `RUPTURE`) — the only track that renamed the contract's fields. Costs: a third of the skill's flow is an interview this harness cannot hold, and `visualize.md` — the step the skill names as its own best lever — was unavailable. Nine of fourteen slides carry no exhibit, eight sit over a 180–220px dead band, and the explainer's mechanism is the weakest drawing of any tool that drew one: `s4` is a descending line, a dotted rule and an empty box clipped to `ollateral`. The cover's gold shield says "security product" on a deck arguing that no liquidation exists. *Best: made provenance structural, legibly. Worst: a beautifully set text document, not an explained mechanism.*

**free (5/7).** The boldest swing and the highest ceiling. `concept-seed.mjs` refused the build thread's own ranking and landed on the Medici *libro segreto* — the double-entry codex whose two sides must balance, which is what `P + N ≡ collateral` is. Lapis, gold-leaf P, vermilion N, verdigris for the sum that holds. `d8` **states the invariant and draws it** in one gesture ("the top edge is flat at 1.00 at every price" as a legend line beside a flat-topped stack) — the strongest show-don't-tell artifact here. The fresh-context finish reviewer found four things the build thread was confident and wrong about. Against that, the largest evidence gap in the bake-off: **no human or model ever looked at a rendered frame of these six artifacts** — its own NOTES says so, and it shows. Folio 1 ships a visible collision (the citation line running through `AAA Flowers S.A. (Panama), operating as Medici`), pdm folio 5 renders words out of reading order, vermilion — established as N *and* as the threshold — is spent on the incumbent's win on folio 9, and the `divest` scene whose job is to give up the apparatus is the loudest scene in the film. *Best: a design that cannot be resold to another client. Worst: shipped unlooked-at, and it shows on the cover.* **Delta +0.5 — uniquely, `free` reads more Medici than `brand`.**

### impeccable-polish

**brand (7/5).** The best tool fit in the bake-off — `polish.md` + `craft-floor.md` + `animate.md` are written for exactly this job — and the method is exemplary: 227 substitutions across six files in one batch, *every replacement asserting its expected hit count so nothing silently no-ops.* It bought the entire craft floor: a real `--sp-1…12` scale where nine arbitrary values had been, the mandated confidentiality footer **3.4:1 → 6.1:1**, thirteen of fourteen slides out of the screen-reader tree, the presenter legend (1.55:1, sitting on the footer, in *every recorded frame*) auto-hidden, a `:focus-visible` ring the brand pins and the incumbent omitted. Detector 30 → 3. And it moved **not one** representation finding: 8/42 citations, no "so what" on the payoff, the explainer's second bar still undrawn, `.eyebrow` still 3.66:1 on every slide despite the notes claiming otherwise. I compared `slide-08` and `scene-04` against the html-ppt baseline directly: near pixel-identical. *Best: fixed the two highest-value defects in the field (the a11y tree, the mandated footer) — both found by looking, neither visible to its own detector. Worst: installed a spacing system under a composition that never used it.*

**free (7/5).** 40,026 bytes of unreachable CSS removed, with correct reachability analysis through the player's runtime `'anim-'+data-anim` construction that a class grep misses; gradient-filled text made solid (from *no measurable contrast at all* to 5.09:1); two render-only occlusion bugs fixed. Settled render pixel-identical to the baseline; every rubric returns ~zero. *Best: proved a detector result is defect evidence, not proof of quality. Worst: nothing left to buy — html-ppt/free had already banked the whole craft floor.* **Delta: it inherits html-ppt's +2.2 brand→free gradient and flattens it to +1.4, by moving the brand arm and not the free one.**

### visual-explainer

**brand (5/6).** The best *teaching* in brand mode. Its invariants — "depict the mechanism, not its name", "one figure, one claim; the caption states it" — are exactly right here, and its design-judgment audit produced the one real layout idea in the field: *the payoff axis is the deck's spine*, recurring on the mechanism, cost and proof slides, with the argument told by what gets drawn onto it. 25/42 exhibits, second-highest. But its routing table has no row for a continuous mathematical function, its slide engine is a `100dvh` scroll-snap container that had to be rewritten, and `slide-patterns.md`'s "18–25 slides, add slides rather than drop content" is actively wrong against a fixed slot count. Three real defects: `d8`'s plot rect clips at x≈696 with the curve running into the right column; the provenance line runs at **1.85:1 on every slide**; and **`s4` states the opposite of the fact** — `collateral posted` and `auction proceeds` drawn as comparable bars when the source is $8M cleared for $0. I looked at that frame. Any recording taken there is wrong. *Best: the mechanism, drawn properly, by a tool that knows why. Worst: a bold-moment scene that contradicts its own claim.*

**free (5/7).** The `AT MATURITY / P RECEIVES / N RECEIVES` case table beside the chart is the most redrawable rendering of the arithmetic in the bake-off, and `.claim` at 46px is the only track clearing the title floor on every slide. Undone by chrome: the presenter widget (`← outline ? →` plus `← → move · O outline · ? help`) is **baked into the stage**, overlaps the source citation, and would be recorded and printed with it; the same frame reads `08/14` in the folio and `1 / 14 · 7%` in the widget; and the rail prints `BOLD MOMENT` and `fact · accumulate` — `staging.yaml` field names, in front of an asset manager. *Best: the case table. Worst: shipped its own reader UI into the deliverable.* **Delta +1.**

### html-ppt

**brand (4/4).** The pinned brand cost this tool everything it is for: all 23 tokyo-night tokens replaced, 20 of 27 animations and all 20 canvas FX modules cut as decoration-by-construction, and presenter mode / theme cycling / the overview grid — its headline features — lost to self-containment. What survived is the primitive layer and the token discipline, which is real and paid. The result is hollow: 150–200px voids on five slides, three headings stacked above every action title, **8/42 citations (worst in the field)**, notes on 4 of 14 slides while carrying 67 body words a slide, and an `s4` that is one unlabelled navy rectangle with the "auctioned for zero" half of the claim never drawn. *Best: `d8`'s payoff chart beside a case table — proof the tool can carry. Worst: vertical placement was never resolved on any slide.*

**free (6/7).** Off the leash it becomes the most professionally resolved deck here: swiss-grid / nord / pitch-deck-vc, one per messaging register. It owns **the best-annotated exhibit in 30 decks** (`no liquidation line fits anywhere on this axis` beside `P — Protected`, `N — Amplified`, `P + N = 1.00 collateral, at every price` — the one exhibit that states its own "so what"), the most traceable citations (39/42, quoting the source phrase), `.notes` on all 14 carrying the contracts' `transitions`, and **zero strings under 4.5:1 and zero under the 28px floor** — the most accessible artifact measured. Its friction is the most instructive in the bake-off: the skill's `counter-up` idiom rendered **$296B where the contract says $344B**, and `color-mix()` fell back to solid black and turned the payoff into a black box — two silent-failure idioms caught only because every pass was screenshotted. Then: 6/42 exhibits (lowest in the field), an 89-word median against an unused notes mechanism, a mechanism chart whose pink fill spans both legs so P and N are indistinguishable at speed, and a theme swap between messaging lanes, so the track has no single identity. *Best: proved it could build the field's best exhibit. Worst: then built two, in fourteen slides.* **Delta +3 — the house brand was costing this tool ~2 points, and its free deck is still the best-made one in the field, which is the uncomfortable finding.**

---

## 2. Cross-review matrix

Rank per rubric, 1 = best. `—` = not scored. Rank sums over the four rubrics that scored all six.

**brand**

| rubric (its bias) | canvas | algo | impec | imp-pol | vis-exp | html-ppt |
|---|---|---|---|---|---|---|
| huashu-critique (concept) | **1** | 2 | 3 | 5 | 4 | 6 |
| open-design-review (a11y) | **1** | 5 | 2 | 4 | 3 | 6 |
| academic-pptx (evidence) | **1** | 6 | 3 | 4 | 2 | 5 |
| impeccable-critique (craft floor) | **1** | 4 | 2 | 3 | 5 | 6 |
| messaging-rubrics (fidelity) | 4 | 5 | **1** | — | 2 | 3 |
| **rank sum** | **4** | 17 | 10 | 16 | 14 | 23 |

**free**

| rubric | canvas | algo | impec | imp-pol | vis-exp | html-ppt |
|---|---|---|---|---|---|---|
| huashu-critique | 2 | 3 | **1** | 5 | 4 | 6 |
| open-design-review | 6 | 4 | 5 | **1=** | 3 | **1=** |
| academic-pptx | 2 | 6 | 5 | 4 | **1** | 3 |
| impeccable-critique | 5 | 3 | **1=** | 4 | **1=** | 6 |
| messaging-rubrics | 4 | 5 | **1** | — | 3 | 2 |
| **rank sum** | 15 | 16 | 12.5 | 14.5 | **9.5** | 16.5 |

**The dispersion is the result.** In brand mode canvas-design takes four of five firsts and a rank sum of 4 out of a possible 4 — the only consensus in the bake-off. In free mode every tool except algorithmic-art places first on at least one rubric and last-or-next-to-last on another; the sums span 9.5–16.5 with four tools inside 2.0. There is no free-mode consensus, and reporting one would be manufacturing it.

**Why they disagree, traced to each rubric.** `huashu` is **concept-led by construction**: Concept carries 0.30 *and* a hard veto — score ≤5 and the total caps at 6.0 regardless of execution. That one rule caps four artifacts scoring 7–8 on hierarchy and craft, puts algorithmic-art/brand second (strong idea, ambient execution) and the best-built free deck last. `open-design` is nominally .4/.2/.2/.2 but **a11y-led in practice**: its brand column sits at 8.5–9.5 for everyone while a11y spans 2.5–9.0, so a .2 axis behaves as the discriminator — which is why canvas-design/free finishes *last* there at 6.5 despite critic 7.5 (it sets its content in 1.7:1 grey) and html-ppt/free wins outright. `academic-pptx` is **evidence-led** — exhibit rate, whether the exhibit carries its "so what", citation rendering — the only rubric putting algorithmic-art last in *both* modes (0/42 representational exhibits) and the only one ranking visual-explainer/free first; it states outright that it has no vocabulary for motion, so it systematically undersells the tool whose whole argument is kinetic. `impeccable-critique` is **craft-floor-led**, and is the rubric the polish arm was optimising against with the file open in front of it — which is why it alone lifts impeccable-polish/brand from sixth to third (+6/32), and why its bans (kicker, coloured `border-left`, section numbers, hero-metric) penalise four tracks for habits they had no notice of. `messaging-rubrics` is **fidelity- and comprehension-led**, and the only rubric that measured motion empirically (820 sampled frames) or diffed claims against extracted DOM text — which is why it inverts nearly everything: impeccable first in both modes for keeping insider vocabulary off screen, canvas-design fourth in both for the dropped fact and the `RUPTURE` eyebrow, algorithmic-art last for a film that does not move. The sharpest single disagreement: **canvas-design/brand is first on four rubrics and fourth on the fifth — because the fifth is the only one that checked whether a fact went missing.**

---

## 3. Consensus findings

1. **The bold moment is a visual peak in exactly one track-mode.** Measured in-scene motion puts `s6` (`assemble`) above `s4` (`rupture`) in six films, and a *contractually quiet* scene above `s4` in three more. Only **canvas-design/brand** orders the film as the contract requires (ρ=+0.85, `s4` 3.35 = the maximum). My frame reading agrees: it is the only `s4` that is a composition rather than a caught-early state.
2. **algorithmic-art's census number is untraceable.** `census · P 0.617 · N 0.383 · Σ 1.000` is a live particle count printed where a measurement goes; `0.617` is nowhere in `source/`. Two reviews reach it independently; `academic-pptx` calls it its highest-severity finding. Same class: on-screen `SEED 3441…` / `SEED 12004`.
3. **`check_deck.py`'s `deck.md` false-error is the most-reported tool defect in the bake-off.** `PROCESS_LEAK` contains `deck.md`, a substring of every real citation (`canton-pitch-deck.md`), so honest sourcing hard-fails the linter. **Five of six NOTES.md report it as top-tier friction.** It pushed provenance into prose (fine — better, even) or off the slide face entirely: algorithmic-art/brand's 4/42 citation rate is this rule's doing.
4. **No design tool has a timeline concept — all six built the explainer engine themselves.** Named in every NOTES: *"no motion vocabulary at all"* (canvas-design), *"could not express: a scene timeline, narration timing"* (algorithmic-art), *"`animate.md` covers interaction motion, not a fixed-duration film with a seek API"* (impeccable), *"no scene/timeline concept at all"* (visual-explainer), *"html-ppt has no timeline"*. The motion vocabulary came from the messaging layer. This is the bake-off's clearest tooling gap.
5. **Provenance lines fail contrast, everywhere.** canvas-design/brand `SRC` 1.85:1; visual-explainer/brand provenance 1.85:1 on every slide; canvas-design/free captions 1.99:1; impeccable-polish/brand's `.eyebrow` still 3.66:1 after the pass claimed it. The brief made traceability mandatory and the field set it below the threshold of sight — `open-design` calls one token change here "the highest-value fix in the review".
6. **Polish bought the craft floor and none of the composition.** Four rubrics, one answer: +6/32, +0.8, +0.7, 1px in brand; +1/32, 0.0, +0.1, 0 in free. **Not one P0 closed in either mode.** The ceiling on a refinement pass is the concept it inherits.
7. **Contract fidelity is perfect across the whole design layer.** 30/30 decks and 30/30 explainers render every slot and scene, in order, claims verbatim, footer on every surface, durations equal to `vo_seconds`. The messaging contract as transport works — a finding, not a given.
8. **Internal contract vocabulary is leaking onto the screen** in four of six tools (`RUPTURE`, `ACCUMULATE`, `STRAIN`, `BOLD MOMENT`, `COVER · COMMON-GROUND`, and `figures[].name` printed as viewer bullets). Only impeccable renamed them. One line in `DESIGN-TASK.md` fixes it.
9. **Raw internal filenames are on client-facing slide faces** — `canton-pitch-deck.md`, `asset-manager-pitch-deck.md`, and `house-brand-guide.md §0.5` on two covers, across five of twelve track-modes. No review filed this as a class. The linter rule everyone routed around was, badly, trying to catch exactly this.

---

## 4. Verdicts

**Brand winner — `canvas-design / brand`.** First on four of five rubrics, rank sum 4/4. The only artifact with an idea a viewer can restate, the only redrawable mechanism diagram, the only film whose bold moment measurably is its peak, 42/42 exhibits and 42/42 citations.

**Free winner — `impeccable / free`, on ceiling.** No rank-sum consensus exists in free mode, so I pick on the mode's own stated purpose: *"this mode exists to show the tool's ceiling."* impeccable/free is the only free artifact whose world could not be resold to another client and whose mechanism slide both states and draws the invariant. It also carries the most shipped defects, and it was **never looked at**. If the question were "which free artifact would survive contact with a projector", the answer is `html-ppt / free`, and I would say so.

**Overall winner — `canvas-design`.** Rank sum 19 across both modes (impeccable 22.5, visual-explainer 23.5 — inside the noise the reviews themselves declare, so read the top three as close). It wins on the thing the brief actually asked for: goal 3, one diagram they could redraw.

**The artifact I would put in front of a real RWA prospect tomorrow: `tracks/canvas-design/brand/staging/` — `deck/index.html` + `explainer/`.** Brand mode because it is the external surface the house ships; `staging` because it is the contract the messaging leg recommends adopting. Fix first, in order:

1. **Restore d11's roll-cost line** (`−1.2%/yr at 10bps across ~12.2 rolls/yr`). One line. It is the only dropped fact in 30 decks and the driver of the −1.25%/yr on that same slide.
2. **Lift the provenance ramp**: `.prov` from `#3A3A3A`/10.5px (1.85:1) to `#AAA`/13px; in-plate SVG labels off `#333` (1.66:1). 123 of 221 strings are currently under 4.5:1.
3. **Reword citations for a reader**: `SRC · CANTON-PITCH-DECK SL. 1, 3 · HOUSE-BRAND-GUIDE §0.5` → "Medici Canton briefing, slides 1 · 3 · July 2026". An internal style-guide section number does not belong on a prospect's cover.
4. **Rename the film's scene eyebrow**: `SC. 04 / 09 RUPTURE` → `SC. 04 / 09 · MARCH 2020`.
5. **Fix the two explainer collisions**: `s6`'s axis label clipping `P` off `P + N ≡ 1.00`; `s4`'s `CLEARED FOR` sitting under the bar field.
6. **Raise the film type ramp to the 28px floor** (min is 16px; 7 of 10 strings under it).
7. **Claim 30px → 44px**, paid for by cutting the 94-word body median toward 40.

Then the six human rulings the messaging leg logged — 54-vs-36 templates, the unsourced $344B claim, MMF-vs-gold, the Panama entity on the cover, whether the fee gets a slot, and the implied theta — none of which a design tool can settle, and the first two of which are on slide 3.

**Recommended house pipeline**

| stage | pick | why |
|---|---|---|
| messaging | `staging` as transport + `house-guide` as content gate | per the messaging verdict; carry `pitch-deck-mastery` slot 4's `diagram:` key onto d8 as a redraw spec |
| design | `canvas-design`, run under the house brand | the only tool whose signature instruction turns the brief's hardest constraint into a design element |
| finish | `impeccable polish` (+`animate`), mandatory pass on top | it measurably cannot author and reliably clears the craft floor — and canvas-design's two worst defects (provenance contrast, film type ramp) are exactly that class |
| review | `open-design-review` gating · `academic-pptx` second · `huashu-critique` **before any pixels** | a11y from computed styles caught the field's commonest defect; the concept test is a go/no-go, not a post-hoc score |

Plus the two five-line checks this bake-off proved missing, run by the contender before NOTES.md is written: the **R3 motion assertion** (`max(s_bold) > max(all others)`, any frame-diff harness — it would have caught nine films) and the **fidelity differ** (claims + supporting points against extracted DOM text — canvas-design and algorithmic-art both reported "nothing dropped", both wrong).

**Borrow from the non-winners**

- **html-ppt/free** — the annotated exhibit (`no liquidation line fits anywhere on this axis`: the one exhibit in 30 decks that states its own "so what"); `.notes` as the home for the contracts' `transitions`; the citation form that quotes the source phrase.
- **impeccable/brand** — the `AUTHORITY` mast (source *and* as-of at the top of the slide, at 4.89:1) and the numbered clause id (`8.1`) as a speaking aid across a room and across a forward.
- **impeccable/free** — the catchword (next slide's first words at the foot: functional, not whimsy), and the **fresh-context finish reviewer with no forked history**, which found four things its own build thread was confident and wrong about.
- **visual-explainer/free** — the `AT MATURITY / P RECEIVES / N RECEIVES` case table beside the chart: the most redrawable rendering of the arithmetic in the field.
- **algorithmic-art** — the live census (`census · Σ 1.000 · at every x`, flipping to `conservation off`), relabelled so it cannot be read as a corpus figure. The one thing here no static design can do.
- **impeccable-polish** — the method: batched edits where every replacement asserts its expected hit count, so nothing silently no-ops on a six-file simultaneous change.

---

## 5. Blind spots in this judgement

I read 44 frames, all stills, most of them scene-*entry* or 85%-freeze states — so I judged motion from frozen frames and from source, and the two tracks that invested most in motion (algorithmic-art, canvas-design) are the two I am least equipped to score. Treat every explainer number as a floor. I looked at one messaging lane (`staging`); a lane-specific failure would have escaped me, and three tracks differ in CSS between messagings while html-ppt/free differs in *theme*. I did not independently re-verify any figure against `source/medici/` — I took the reviews' fact-checks, which agree with each other; my one independent correctness observation (visual-explainer/brand's `s4` bars contradicting their own claim) came from looking at a frame, not from checking a number. Finally, four of the five rubrics I aggregate carry a declared conflict or a substituted scaffold: `impeccable-critique` scored its own tool under its own rules with the subject optimising against them, `open-design-review`'s weights are the seat's invention because the skill is a catalogue stub, and `academic-pptx` is a lecture-hall rubric applied to a 1280×720 CSS stage. My rank sums inherit all of it, and the free-mode sums in particular should be read as evidence that the rubrics disagree, not as a ranking.
