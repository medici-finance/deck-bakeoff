# Design review — impeccable `critique` over all 10 track-modes

⚠️ DEGRADED: single-context (this reviewer is itself a sub-agent under a
no-re-delegation instruction, so Assessment A and B ran in one thread rather than
as two isolated sub-agents — critique.md's fallback path).

Rubric: `reference/critique.md` (Nielsen 0–4) + `reference/craft-floor.md` (Refuse
list) + `scripts/detect.mjs`. Mode = **Persuade**, so **7 (Flexibility)** and
**10 (Help)** are `n/a` everywhere — a linear pitch surface has no expert path and
no help system. **Applicable maximum = 32.** Bands: 90% Excellent, 70% Good, 50%
Acceptable. Columns below: 1 Status · 2 Match real world · 3 Control ·
4 Consistency · 5 Error prevention · 6 Recognition · 8 Aesthetic · 9 Error recovery.

Evidence: `detect.mjs --no-config` on `staging/{deck/index.html,explainer/explainer.html}`
per track-mode, `pitch-deck-mastery` spot-checked as the second messaging variant
(same pattern, ±2 findings). No `shots/` directory exists, so frames were rendered
with headless Chromium: `--print-to-pdf` for decks (all 10 print 14 pages, one
slide per page, as the brief requires) and `--screenshot` at 1280×720 for explainer
scenes 1 and 4, plus scene 6 and 1920×1080 re-renders where a frame looked wrong.

| Track-mode | 1 | 2 | 3 | 4 | 5 | 6 | 8 | 9 | Total | Band | detect hard / adv |
|---|--|--|--|--|--|--|--|--|--|---|---|
| canvas-design · brand | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 2 | **28/32** (88%) | Good | 1 / 1 |
| impeccable · brand | 4 | 4 | 4 | 4 | 2 | 4 | 2 | 3 | **27/32** (84%) | Good | 1 / 1 |
| algorithmic-art · brand | 3 | 3 | 3 | 4 | 2 | 1 | 2 | 2 | **20/32** (63%) | Acceptable | 1 / 0 |
| visual-explainer · brand | 3 | 3 | 3 | 3 | 1 | 3 | 1 | 2 | **19/32** (59%) | Acceptable | 5 / 0 |
| html-ppt · brand | 3 | 3 | 3 | 2 | 1 | 3 | 1 | 2 | **18/32** (56%) | Acceptable | 9 / 1 |
| impeccable · free | 3 | 4 | 3 | 3 | 1 | 4 | 2 | 3 | **23/32** (72%) | Good | 0 / 2 |
| visual-explainer · free | 3 | 2 | 3 | 3 | 3 | 4 | 2 | 3 | **23/32** (72%) | Good | 8 / 2 |
| algorithmic-art · free | 3 | 3 | 3 | 4 | 2 | 2 | 1 | 2 | **20/32** (63%) | Acceptable | 6 / 2 |
| canvas-design · free | 3 | 3 | 3 | 2 | 1 | 3 | 2 | 2 | **19/32** (59%) | Acceptable | 0 / 1 |
| html-ppt · free | 3 | 3 | 3 | 3 | 1 | 2 | 1 | 2 | **18/32** (56%) | Acceptable | 15 / 2 |

Every advisory is `em-dash-overuse` (11–31 per file); advisories never count as
failures and are held against no one.

## canvas-design · brand — 28/32 · "Conservation Plate"

Bans: **eyebrow/kicker** (`PL. 02 DIAGRAM SERIES OF 14` above every heading — the
one ban craft-floor says no brief earns back); **border-left > 1px** (3px blue on
the pl.05 pull-quote); **monospace as costume** (mostly defensible — it labels
measurement). Detector 1 hard (`layout-transition` on `transition: width`).

1. **P0 — the plate rail is an eyebrow.** Drop `DIAGRAM`/`COMPARE`/`STATEMENT`;
   keep `PL. 07 · SERIES OF 14`, which is sequence the reader uses.
2. **P1 — pl.05's 3px blue quote rule.** Take it to 1px or use the plate's indent.
3. **P2 — that quote runs at ~2.0 line-height** against ~1.4 everywhere else, and
   over the 65–75ch measure. Set it on the plate's own leading.

The `SRC ·` strip turns don't-invent-numbers into a device, not a compliance tax;
pl.08 is the one payoff diagram a viewer could redraw; no collision or clipping
anywhere.

## impeccable · brand — 27/32 · "clearing-house circular"

Bans: **border-left > 1px** (`[side-tab] border-left:3px solid var(--blue)`, deck
line 101 — impeccable's own detector catching impeccable's own build); **section
numbers** (7.1/7.2/7.3 — defensible, clauses are cited as `<notice>.<n>`).
Detector 1 hard.

1. **P0 — clipped label in the explainer.** Scene 4 renders `ollateral`: the
   collateral box overprints its own label. Pad the box or move the label out.
2. **P1 — eight of fourteen notices are heading + ruled rows over a 180–220px dead
   band.** Fill it with the figure that notice implies, or move the space above the
   heading where the floor wants it. Only two notices carry a real figure.
3. **P2 — the cover's gold shield and the ghost hexagon watermark.** The palette is
   black + Electric Blue; the shield adds a third hue and the hexagon bleeds off
   the top of notice 02. Cut both.

## algorithmic-art · brand — 20/32 · "Invariant Drift"

Bans: **eyebrow** (`CHANGE`/`PIVOT`/`MOVE`/`EVIDENCE`); **hero-metric template**
(slide 03's two big-number cards). Detector 1 hard.

1. **P0 — the mechanism slide has no readable diagram.** Slide 08 is a horizontal
   noise field with 12px `N`/`P` labels, no 1.00 line, no strike, no axis values.
   The brief's goal 3 ("one diagram they could redraw") is unmet.
2. **P1 — the art is decoration on 10 of 14 slides.** On 03, 04, 07 it fills the
   bottom 60% carrying no per-slide meaning; only the `census · P · N · Σ` readout
   does argumentative work. Bind each slide's parameters to its claim, or crop.
3. **P2 — one layout, fourteen times;** one authored exception at the turn would
   carry it.

## visual-explainer · brand — 19/32

Bans, densely: **same-size cards as page structure** (07, 10); **hero-metric
template** (02, 10); **eyebrow** on every slide; **border-left > 1px** ×4.
Detector 5 hard (`side-tab` at lines 76/77/78/100, `layout-transition`).

1. **P0 — slide 08's payoff plot is clipped.** The plot rect stops at x≈696 while
   the curve and `reference price x at maturity` run off into the right column.
2. **P0 — the explainer's Black-Thursday scene states the opposite of the fact.**
   At scene 4 `collateral posted` and `auction proceeds` are equal-height bars;
   the source is $8M cleared for $0. Any frame recorded here is wrong. Start
   proceeds at zero, or hold the collapsed state.
3. **P1 — the card grid is the page.** Replace the 3-card rows on 07 and 10 with a
   composition each; cards are the floor's named lazy container. Scenes 4 and 6
   also rendered with no headline text under two time budgets.

## html-ppt · brand — 18/32

Bans: **hero-metric template** ×3 (02, 03, 10 are the same component); **eyebrow**,
doubled (`MEDICI` + `WHERE WE ARE` + `COMMON GROUND`); **border-left > 1px** ×8;
**monospace as costume** (`stated yield`, `stakeholder-scoped`, `one transaction`
as display words). Detector 9 hard — worst in brand mode.

1. **P0 — vertical placement is unresolved.** Cover, 02, 03, 07 and 10 leave
   150–200px of void between heading and body and more below. Fix a baseline.
2. **P1 — three identical metric rows;** the deck has one layout idea, used thrice.
3. **P1 — the mono display words.** Mono is for code, data or measurement. Slide 08
   is the salvage: a correctly labelled payoff chart beside a case table.

## impeccable · free — 23/32 · "Libro Segreto"

Bans: **none named** — no cards, no hero-metric, no eyebrow (the folio number is a
folio), no gradient text, no glyph icons. Detector 0 hard.

1. **P0 — text collision on the cover.** `canton-pitch-deck.md Slides 1, 3` runs
   through `AAA Flowers S.A. (Panama), operating as Medici.` The folio rail sits
   over a body block that grew; reserve its height in the flow.
2. **P1 — the bottom 45% is empty on folios 2, 3, 7, 10** — a committed grid, and
   the most product-specific world here, used for a third of its height.
3. **P1 — vermilion for the incumbent's win (folio 9).** Vermilion is established
   as the N leg and the threshold; spending it on "$620M+ of live RWA deposits"
   inverts the colour argument exactly where honesty matters most.

## visual-explainer · free — 23/32

Bans: **border-left > 1px** ×3; **same-size cards** (02, 10); **hero-metric
template** (02); **eyebrow + decorative rule** on every slide;
**codex-grid-background** ×2. Detector 8 hard.

1. **P0 — pipeline vocabulary on the surface.** The explainer rail reads
   `04 FACT · RUPTURE · BOLD MOMENT`; `BOLD MOMENT` is a `staging.yaml` field name,
   not language for an asset manager.
2. **P1 — grid background plus three side-tab cards.** Both are named AI-tells;
   together they make slide 10 read as a template.
3. **P2 — slide 03's chart is five bars with no y-axis** under a claim about a
   year of growth, over an empty lower half. Slide 08 is the reverse: the best
   mechanism slide in free mode — table, annotated chart, legend, plain-words caption.

## algorithmic-art · free — 20/32

Bans: **eyebrow** (`FACT · CHANGE`); **overused-font** — the detector flags `Inter`
and `Instrument Serif` six times, the most recognisable free-mode default pairing.
Detector 6 hard.

1. **P0 — the generative layer does not survive the print path.** In the
   brief-required print-to-PDF the p5 field on 02, 03, 04, 10 is a faint smudge:
   the deck's whole visual argument sits on a canvas the deliverable can't carry.
   Rasterise a still per slide at build time.
2. **P1 — the payoff figure has no numbers.** Slides 08/09 are a flat two-tone
   block: no 1.00 line, no strike label, no axis values.
3. **P2 — the source line truncates** with `…` on 04 and 09, defeating this
   track's best idea. Fourteen slides share one layout with no authored exception:
   the strongest engine in the bake-off spent on the weakest composition.

## canvas-design · free — 19/32 · "Invariant Field"

Bans: **monospace as costume** — all body copy is mono, which is the ban rather
than the exception; **eyebrow**, doubled (`D5` + `QUOTE` + `PLATE 06 · …`).
Detector 0 hard.

1. **P0 — collision on the mechanism slide.** On D8 `P PROTECTED` overprints the
   red annotation `where a lending market would put its threshold`. The one slide
   that must be redrawable is the one that breaks.
2. **P0 — two contradictory numbering systems.** `D3`/`PLATE 04`, `D9`/`PLATE 10`,
   `D10`/`PLATE 09` — disagreeing in both directions. Pick one sequence.
3. **P1 — D3's chart clips at the right edge** (`… RWA COLLATERAL DEPOS`) and its
   `the collateral arrives` label crowds the `$620M+` figure.

## html-ppt · free — 18/32

Bans: **gradient text** ×2; **hero-metric template** (02, 03, 10); **bounce easing**
(`cubic-bezier(.22, 1.3, .36, 1)`); **zero-offset glow** (`dark-glow #3b6cff`);
**marquee** ×2 infinite loops; **overused-font** (`Inter`). Detector **15 hard** —
the worst mechanical score in the bake-off.

1. **P0 — the explainer does not render its own copy.** At scenes 4 and 6, under
   two time budgets, headlines sit at near-zero opacity and overprint the `Medici`
   lockup; figures are plain grey placeholder rectangles; `MakerDAO collateral,
   auctioned` overlaps the footer; the stage letterboxes at 1280×720.
2. **P0 — slide 08's payoff chart.** Right edge clipped mid-curve, a stray vertical
   rule at x≈660, pink fill spanning both legs so P and N are indistinguishable,
   and `no liquidation line fits anywhere on this axis` printed across the plot.
3. **P1 — infinite marquee and bounce easing** in a Persuade surface: motion that
   never resolves, on a curve the floor names. The Swiss editorial system on 02,
   03, 07, 09, 10 is genuinely good; the mechanism slide and explainer are not.

## Rankings

**brand** — 1. canvas-design (28) · 2. impeccable (27) · 3. algorithmic-art (20)
· 4. visual-explainer (19) · 5. html-ppt (18)

**free** — 1. impeccable (23) · 2. visual-explainer (23) · 3. algorithmic-art (20)
· 4. canvas-design (19) · 5. html-ppt (18)

The free tie broke on the rubric's own instruments: ban categories hit
(impeccable/free 0, visual-explainer/free 5) and detector hard findings (0 vs 8).
Under a defect-severity tie-break — impeccable/free ships a cover-slide collision,
visual-explainer/free ships none — the order flips. Read them as tied; I have
named my tie-break because it favours the tool I am not neutral about.

## Brand → free delta

| Tool | brand | free | Δ | What the constraint was doing |
|---|--|--|--|---|
| canvas-design | 28 | 19 | **−9** | The brand held its type discipline. Freed, it set all body in mono and shipped two collisions and a numbering contradiction. |
| impeccable | 27 | 23 | **−4** | Freedom bought the most distinctive world and cost composition: half-empty grid, colliding cover. |
| algorithmic-art | 20 | 20 | **0** | Same engine, same 14-slide template either way; the brand only changed the palette. |
| html-ppt | 18 | 18 | **0** | Equal on paper only: brand mode is mis-centred, free mode is mechanically broken. |
| visual-explainer | 19 | 23 | **+4** | The one tool freedom helped. Its brand deck is a card grid; its free deck earns a real mechanism slide. |

The brand raised the floor for two tools, lowered the ceiling for one, and did
nothing for the two whose weakness is composition rather than palette.

## Blind spots — including mine

I am impeccable's `critique` scoring impeccable's own tracks: it placed 2nd in
brand and 1st-equal in free under a rubric it authored.

**The rubric is impeccable's home turf.** The craft-floor bans are the checklist
impeccable's own build runs before shipping; tracks that never read that file are
penalised for habits they had no notice of. `visual-explainer` and `html-ppt` lose
most of their aesthetic points to bans a viewer might not notice; `algorithmic-art`
and `canvas-design` lose theirs to legibility failures a viewer certainly would.
Weight those differently and the middle of both tables reshuffles; top and bottom
do not.

**The detector is not neutral either.** impeccable/free was the only track with a
local `.impeccable/` directory that could suppress findings, so every scan ran
`--no-config` and that track was run both ways: identical counts (0 hard). It is a
design-system description, not detector ignores, and no track uses inline
`impeccable-disable` comments. But the detector finds side-tabs and fonts, not
clipped charts or collisions — every P0 above came from a rendered frame.

**I over-corrected once.** My first pass tied impeccable/brand with
canvas-design/brand at 28; I dropped it to 27 on the dead-space finding, which is
real — but I went looking for it because the tie made me uncomfortable. The
opposite pressure applies in free mode, where a ban count decided a tie in
impeccable's favour. Both calls are inside the noise: treat canvas-design/brand ≈
impeccable/brand and impeccable/free ≈ visual-explainer/free.

**The evidence is uneven across media.** Decks were inspected through their own
print path — the brief's requirement, and deterministic. Explainers were stills
under headless virtual time, which punishes motion driven by a real clock. `html-ppt/free` and `visual-explainer/brand` rendered headline-less or
opacity-stuck frames there; those findings are observed rather than proven, and a
live-browser pass could partly exonerate both. No other explainer failed the same
harness, which is why I did not discount them.

---

# Addendum — impeccable-polish (brand, free)

⚠️ **COMPOUNDED CONFLICT OF INTEREST — read this before the scores.** The main review already
carried one: impeccable's `critique` scoring impeccable's own tracks. This addendum stacks a
second one on top of it. `impeccable-polish` is `tracks/html-ppt/{brand,free}/` copied verbatim
and put through **impeccable's own `polish` and `animate` commands**, and I am now scoring that
output using **impeccable's own `reference/critique.md`, impeccable's own
`reference/craft-floor.md`, and impeccable's own `scripts/detect.mjs`** — the same
`craft-floor.md` the pass loaded immediately before its first edit, and the same detector the
pass ran as its before/after instrument. The refinement arm was optimising directly against the
rubric I am grading it with. Treat every number below as a self-report with a stopwatch on it,
and read the "What polish bought" section, where I try to separate what the pass fixed from
what it merely satisfied.

Same frame as the main review: Mode = **Persuade**, so **7 (Flexibility)** and **10 (Help)**
stay `n/a`; applicable maximum **32**; bands 90% Excellent, 70% Good, 50% Acceptable.

**Evidence.** `detect.mjs --no-config` on `staging/{deck/index.html,explainer/explainer.html}`
per mode, `pitch-deck-mastery` spot-checked as the second messaging variant. **I re-ran the
detector over the `html-ppt` baseline in the same pass and through the same code path**, so the
before/after column below is mine, not the track's own reported figure — and it reproduces the
main review's published `9 / 1` and `15 / 2` exactly, which is the check that lets the delta be
trusted. Frames: no `shots/impeccable-polish` exists, so one headless Chrome (Playwright +
installed Chrome) rendered deck slides 1 / 6 / 11 at 1280×720 and explainer scenes 4 and 6 at
1920×1080, frozen at 85% of each scene's `data-dur` through the artifacts' own
`?scene=N&still=T` / `?scene=N&at=T` hooks, plus a 1280×720 explainer pass to test stage fit.
24 frames.

| Track-mode | 1 | 2 | 3 | 4 | 5 | 6 | 8 | 9 | Total | Band | detect hard / adv |
|---|--|--|--|--|--|--|--|--|--|---|---|
| **impeccable-polish · brand** | 4 | 3 | 3 | 4 | 2 | 4 | 2 | 2 | **24/32** (75%) | **Good** | **0 / 1** |
| html-ppt · brand *(baseline)* | 3 | 3 | 3 | 2 | 1 | 3 | 1 | 2 | 18/32 (56%) | Acceptable | 9 / 1 |
| **impeccable-polish · free** | 3 | 3 | 3 | 3 | 1 | 2 | 2 | 2 | **19/32** (59%) | Acceptable | **3 / 2** |
| html-ppt · free *(baseline)* | 3 | 3 | 3 | 3 | 1 | 2 | 1 | 2 | 18/32 (56%) | Acceptable | 15 / 2 |

Detector, measured by me, staging deck + explainer, `--no-config`:

| mode | baseline hard | polish hard | what cleared | what survives |
|---|---|---|---|---|
| brand | **9** (`side-tab` ×8, `layout-transition` ×1) | **0** | every one | `em-dash-overuse` ×1 (advisory, contract copy) |
| free | **15** (`marquee` ×4, `overused-font` ×3, `gradient-text` ×2, `bounce-easing` ×2, `layout-transition` ×2, `dark-glow` ×2) | **3** | marquee, gradient-text, bounce-easing, layout-transition, one dark-glow | `overused-font` ×3 (Inter, the incumbent identity), `dark-glow` ×1 (light-page offset shadow, a documented false positive) |

## impeccable-polish · brand — 24/32 · "the circular, correctly set"

Bans: **eyebrow/kicker, doubled** (`MEDICI` + `WHO HOLDS EACH LEG` + `TWO HOLDERS` — three
labels above one headline, on every content slide; the track's notes name this as the ban it
cannot clear because clearing it is copy removal); **hero-metric template** ×3 (02, 03, 10 are
still the same component); **monospace as costume** (`stated yield`, `stakeholder-scoped`, `one
transaction` still set as display words). Bans **cleared**: `border-left > 1px` ×8 — the 3px
coloured rails on `.card-accent`/`.card-bad`/`.card-good`/`.quote` are gone, replaced by a 1px
tinted hairline plus a faint wash of the same hue, verified in frame; and, invisibly to the
detector, seven hand-drawn 6px SVG side rails thinned to 2px and inset past the parent card's
`rx=14` corners. Detector **0 hard** — from 9, the largest mechanical movement in the bake-off.

1. **P0 — vertical placement is still unresolved, and this is the finding.** My P0 against
   html-ppt/brand was "Cover, 02, 03, 07 and 10 leave 150–200px of void between heading and
   body and more below. Fix a baseline." The pass built the baseline — a real `--sp-1…12` 4px
   scale with 21 declarations snapped onto it, replacing 18/22/26/34/15/14/9/7/6px of nothing —
   and then did not re-flow a single slide onto it. Verified in frame: cover, headline ends
   y≈185, lede at y≈411; slide 06, `$0` + two bullets floating between 45% and 70% with ~200px
   empty above and ~160px below; `pitch-deck-mastery` 06 the same. A spacing system installed
   under a composition that does not use it is the exact shape of what a refinement arm can and
   cannot do.
2. **P1 — the eyebrow ban is unclearable here and the pass says so out loud.** craft-floor is
   absolute on this one (*"no brief earns it back"*), every content slide carries three stacked
   labels, and removing them is copy removal, which `polish.md` forbids without asking. The
   pass fixed the *consequence* instead — the kicker was 8px under the header rule and 16px
   above its own headline, i.e. grouped with the wrong thing; it is now 20px above / 8px below,
   a genuine proximity repair — and escalated the cause into its notes. That is the correct
   handling of a rule collision, and it still leaves the ban standing on 14 slides.
3. **P1 — three fixes the detector could not see, which is the honest part of this result.**
   Thirteen of fourteen slides were in the accessibility tree at once (`opacity:0` with no
   `visibility`); the mandated confidentiality footer ran at 3.4:1 and the presenter key legend
   at 1.6:1 — a dead state sitting on top of the footer at 1280×720, and in every recorded
   frame. All three are now fixed (footer 6.1:1 at 12px, legend auto-hides at 2.4s, one slide in
   the tree), and none of them is a detector rule. The `:focus-visible` ring the brand guide
   pins in §9.3 and the incumbent omitted now exists. Set against that, one recorded deviation:
   §9.1's *named* `ease-in-out` replaced by `cubic-bezier(.16,1,.3,1)` at the pinned 200ms.

Column movements, briefly. **1 Status 3→4**: slide counter, progress fill and scene id are all
legible now, and the progress fill drives `transform:scaleX()` instead of `width`, so stepping
the deck no longer re-lays-out the stage. **4 Consistency 2→4**: the largest single jump in
this addendum — one spacing scale, one semantic-colour idiom where there were two, header and
footer insets equalised at 24px, `.g1` given the rule the markup was already assuming, six
declared-and-unreachable tokens removed, a type ladder without a 1px step. **5 Error prevention
1→2**: `prefers-reduced-motion` extended to cover the motion the pass itself added, print block
likewise, focus ring added; the print/record hazard of baked-in chrome is gone. **6 Recognition
3→4**: dead state resolved, a11y tree resolved, the kicker labels the right thing. **8 Aesthetic
1→2**: one of four ban categories cleared, three standing.

## impeccable-polish · free — 19/32

Bans: **hero-metric template** (02, 03, 10); **section numbers** (`.section-num` watermarks on 8
`pitch-deck-mastery` slides at 1.1:1 — explicitly kept and flagged, on the reasoning that they
are load-bearing identity carrying nothing a reader must decode); **overused-font** (`Inter`,
the incumbent identity across all three themes — the one finding a from-scratch arm can fix and
this arm cannot). Bans **cleared**: **gradient text** ×2 (`-webkit-text-fill-color:transparent`
made the template's later `color:` override inert, so every kicker and the `$344B` / `never
liquidate` display type rendered as gradient fill and had *no measurable contrast at all*; now
solid at 5.09:1 and 5.06:1); **bounce easing** (`cubic-bezier(.22,1.3,.36,1)` with a
`scale(1.04)` overshoot → a clean `.72→1` ease-out); **marquee** ×4 infinite loops; **zero-offset
glow** on the staging pair. Detector **3 hard**, from 15.

1. **P0 — the explainer still does not survive the brief's own stage, and this was my P0.** At
   1280×720, verified in frame: the stage letterboxes, and `MakerDAO collateral, auctioned`
   overprints the confidentiality footer and its rule. At 1920×1080 it resolves cleanly — so
   this is stage-fit geometry rather than a layout bug, and I am naming that explicitly because
   the main review very nearly filed three false blockers on exactly this class. It is still an
   unfixed P0 against the brief as written.
2. **P0 — slide 08's payoff chart is untouched.** Right edge clipped mid-curve, the stray
   vertical rule at x≈660, pink fill spanning both legs so P and N remain indistinguishable.
   That was my second P0 and it is a figure defect; a pass that may not redraw a figure cannot
   reach it. The explainer's collateral figure is the same story from the other end — at 85% of
   scene 4 it is two bare black rules and a dotted red one, unlabelled, at both stage sizes.
3. **P1 — 40,026 bytes of dead CSS removed, and it changed nothing a viewer sees.** The
   baseline inlined html-ppt's entire 67-rule animation library into every artifact while using
   3–9 effects; the pass rebuilt each block from the effects actually referenced — including the
   ones reached through the player's runtime `'anim-'+data-anim` construction, which a class
   grep misses — and took marquee, shimmer, neon-glow, gradient-flow, confetti, typewriter,
   glitch, ken-burns and the four 3D flips with it. Genuine, careful, load-bearing maintenance
   work; worth +1 on Aesthetic for the bans it cleared and nothing at all on the seven other
   columns, because the settled render is pixel-identical.

## Revised rankings

**brand (6)** — 1. canvas-design (28) · 2. impeccable (27) · **3. impeccable-polish (24)** ·
4. algorithmic-art (20) · 5. visual-explainer (19) · 6. html-ppt (18)

**free (6)** — 1. impeccable (23) · 2. visual-explainer (23) · 3. algorithmic-art (20) ·
**4. impeccable-polish (19)** · 5. canvas-design (19) · 6. html-ppt (18)

The free tie at 19 breaks on the same instruments the main review used, and in the same
uncomfortable direction. Ban categories: canvas-design/free hits two (mono-as-costume across
all body copy, doubled eyebrow), impeccable-polish/free hits three. Detector hard findings:
canvas-design 0, impeccable-polish 3. Both of those favour canvas-design. The defect-severity
tie-break is what flips it: canvas-design/free ships a collision at its own native size (`P
PROTECTED` overprinting the red annotation on D8, the one slide that must be redrawable) plus
two contradictory numbering systems, while impeccable-polish/free's surviving P0 resolves at
1920 and its three detector hits are a font choice and a documented false positive. **I have
put impeccable-polish 4th on that reading and I want it read as a tie**, exactly as the main
review asked for canvas-design/brand ≈ impeccable/brand. Note also that my own tie-break
instruments — ban count and detector count — are the two things this arm was tuned against, so
the fact that they came out *against* it here is the only reassuring thing in this paragraph.

## What polish bought

**+6 in brand (18 → 24, Acceptable → Good), +1 in free (18 → 19, Acceptable → Acceptable).**
The brand arm posts the largest single improvement in the bake-off and the free arm posts the
smallest measurable one, from the same tool, in the same 17-and-38-minute passes, on the same
day. That spread is the actual finding.

The honest decomposition of the +6, because the conflict of interest demands one:

- **Two points are craft repair the rubric would have credited from any tool** — Consistency
  2→4 for a spacing scale, a unified colour idiom, equalised insets and a type ladder. This is
  real work on the deck the main review called "one layout idea, used thrice, mis-centred".
- **Two points are defects the detector cannot see and no rule made it look for** — the
  accessibility tree, the mandated footer at 3.4:1, the presenter legend that was both a dead
  state and a recording artifact, the kicker grouped with the wrong element. Every one came
  from reading and looking. The pass's own notes say so plainly ("the detector went 30 → 3, but
  the two highest-value fixes and the two render-only fixes came from reading and looking, not
  from scanning"), and my frames agree.
- **One point is the ban list, scored on a rubric the pass had open in front of it.** Aesthetic
  1→2 is `border-left > 1px` ×8 cleared in brand, gradient-text + bounce + marquee cleared in
  free. This is the component a neutral reader should discount hardest: the arm was editing
  against my checklist. I have capped it at +1 in both modes for precisely that reason — and
  note it stays at 2, not 4, because the *structural* bans (eyebrow, hero-metric template,
  mono-as-costume, section numbers) all survive, and those are the ones a viewer would feel.
- **One point is status and recognition legibility**, which is downstream of the contrast work.

And what it demonstrably did **not** buy, in either mode: **not one P0 from the main review is
closed.** html-ppt/brand's was unresolved vertical placement — still unresolved, on a scale
built for it. html-ppt/free's two were the explainer's stage and the clipped payoff chart —
both still there. Nine of the eleven P0/P1 items I filed against these two artifacts are
composition or copy, and composition and copy are the two things `polish.md` forbids touching.

So: **polish bought the entire craft floor and none of the composition.** It moved
html-ppt/brand from the worst mechanical score in brand mode to third overall and left it
finishing behind two artifacts with more defects and better ideas; it moved html-ppt/free by
one point and 40KB. The sharpest way to say it is the pass's own: *"a from-scratch impeccable
contender would not have shipped these; this arm cannot remove them."* A finish pass raises the
floor of the artifact it is given. It does not raise the ceiling, and on this rubric the
ceiling was set by composition in both modes.

## Blind spots — including the two that are mine

Everything in the main review's blind-spot section still holds. Three more here.

**The conflict is not just that I authored the rubric — it is that the subject optimised
against it.** In the main review the other tracks were "penalised for habits they had no notice
of"; here the arm had the notice, had `craft-floor.md` open before its first edit, and used my
detector as its own before/after instrument. A detector score going 9→0 and 15→3 under those
conditions is a measure of compliance, not of quality, and I have deliberately let it move only
the Aesthetic column by 1. A reviewer who weighted the detector the way its headline numbers
invite would score this arm several points higher, and would be measuring the wrong thing.

**My detector is still blind exactly where this arm did its best work, and that cuts in the
arm's favour this time.** `detect.mjs` found 24 CSS `border-left` side-tabs in the brand
baseline and zero of the seven hand-drawn 6px SVG rails that are the same anti-pattern in a
different syntax; it cannot see contrast, proximity, a dead state, an accessibility tree, or a
class used in markup but never defined in CSS — six of the roughly fourteen defect classes the
brand pass actually fixed. So the instrument that flatters this arm on ban compliance
simultaneously under-reports its most valuable work, and both errors are mine.

**Evidence coverage is thinner than the main review's and asymmetric between the modes.** I
read 24 frames across two modes — staging plus one spot-check — and I did not re-run the
print-to-PDF path that the main review used as its deterministic deck evidence, so a pagination
regression from the pass's `visibility:hidden` and print-block edits would have escaped me
(the pass reports adding `visibility:visible!important` to the print block for exactly that
reason; I have taken that on trust rather than verifying 14 pages × 6 decks). I also graded
motion from frozen frames again, which under-credits the brand arm specifically: a 200ms
dissolve replacing a hard cut, a film progress bar taken off per-frame layout, and one arrival
per scene instead of two are all changes a viewer feels on a recording and a still cannot show.
If any part of the +6 is understated, it is there.
