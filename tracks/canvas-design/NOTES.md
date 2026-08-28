# NOTES — design contender `canvas-design`

One file per design contender, shared by both brand modes.

## brand

Contender `canvas-design`, mode `brand`. Session 2026-08-27 23:41Z → 2026-08-28 00:20Z
(~39 min wall clock, single session, no prior state).

### The tool, and how its process was actually run

`skills/design/canvas-design/SKILL.md` is a two-step process: (1) write a design
philosophy / art-movement manifesto as a `.md`, (2) express it on a canvas as a
single-page `.pdf`/`.png`, then a refine-don't-add second pass. Both steps were run
faithfully; only the output medium was substituted (HTML deck + HTML film, per the
design-contender task).

1. **Philosophy** — `brand/PHILOSOPHY.md`, written before any artifact, 6 paragraphs,
   movement named **Conservation Plate**. Written to the skill's own rules: kept generic
   (it never names Medici, RWA or the deck), organised by the headings the skill asks for
   (space/form, colour/material, scale/rhythm, composition/hierarchy, craft), and it
   repeats the craftsmanship demand the skill insists on.
2. **Deducing the subtle reference** — the skill's `DEDUCING THE SUBTLE REFERENCE` step
   was run and is what gave the movement its spine: the brief's real subject is a
   *conserved quantity* (`P + N ≡ collateral`) whose consequence is an *absence* (no
   liquidation threshold). So the movement's two devices are **the constant edge** (one
   unbroken white rule at 1.00 that recurs plate to plate) and **the refused line** (a
   gesture that begins and does not complete). Neither device is captioned as a metaphor;
   the jazz-quote rule was kept.
3. **Canvas creation** — the skill's "scientific bible / imaginary discipline" instruction
   is the single most useful thing it says, and it drove the whole system: dense hairline
   tick fields, plate numbering (`PL. 07 · DIAGRAM · SERIES OF 14`), a registration frame
   with corner ticks, an index rail, and a provenance strip at the foot of every plate
   (`SRC · canton-pitch-deck Sl. 3, 5`). That last one is the happy accident of the whole
   exercise: the skill's "systematic reference markers" instruction and the brief's
   "every figure must trace to a source file" requirement turn out to be the same
   instruction, so fact-tracing became a design element rather than a compliance tax.
4. **Refine, don't add** (the skill's FINAL STEP) — run as nine measured passes in a real
   browser (see "Render and look" below). Every pass subtracted or aligned; no pass added
   a figure. Examples: the payoff plot lost its duplicate `1.00` label, the built-vs-not
   plate lost a colliding second rule, the split plate's brace was redrawn from two
   overlapping paths to one bracket, the P-decline plate moved two labels off each other.
5. **Fonts** — the skill says to search `./canvas-fonts` and "use different fonts". In
   brand mode this is overridden: IBM Plex Sans + IBM Plex Mono only, self-hosted woff2
   copied beside each HTML (brand §3.1, "self-host, never a CDN"). See "Brand fights".

### Artifacts and time-to-artifact

The six artifacts are generated from one shared plate library, so they do not have
separable build times — the honest unit is the library, not the artifact.

| phase | wall clock |
|---|---|
| read brief + all three staging contracts + brand guide §2/§3/§7/§9/§10 + the linter's rule table | ~7 min |
| `PHILOSOPHY.md` (step 1) | ~4 min |
| plate library (`_build/plates.py`, 20 figures) + content map (`_build/content.py`, 42 slots + 25 scenes) + builder (`_build/build.py`) | ~13 min |
| first full build → all six artifacts | 2.1 s (and every rebuild after) |
| render-and-look refine loop: 9 fix rounds, 14 browser screenshots, 2 measured overflow audits | ~13 min |
| notes | ~2 min |

Per artifact, from the generator: `staging` deck 14 plates + film 9 scenes/120s;
`presentation-writing` deck 14 + film 8/132s; `pitch-deck-mastery` deck 14 + film 8/143s.

### Render and look (the gate the linter cannot do)

No puppeteer/playwright is installed, so the check was done in a real Chrome via the
browser tools, against a local static server. Two things it caught that no static check
would have:

* **Slide-content overflow.** `pitch-deck-mastery` plate 02 has four supporting points;
  my annotation-height estimator assumed a single row of three columns, so the fourth
  wrapped underneath and pushed the provenance strip through the footer. Fixed by making
  the grid 1–4 columns and folding row count into the height budget, then re-verified by
  measuring every element's bottom/right edge in all 42 plates and all 25 scenes
  (`0` slides over the 664px content-bottom, `0` over the 1226px content-right;
  scenes `0`/`0` against 992px/1828px).
* **Duplicate SVG `<pattern>` ids.** The `pitch-deck-mastery` film uses the payoff plate
  twice (scenes 4 and 5). Two `<pattern id="hx7">` in one document silently killed the N
  leg's hatch in the second scene — the plate still rendered, just without the texture
  that distinguishes N from ground. Paint-server ids are now minted per figure instance.

Screenshots also confirmed the two motion moments actually read: the rupture (every
proceeds mark drops to the zero baseline in 320 ms and the frame goes still) and the
arrest (the seizure gesture travels the price axis and stops mid-motion under a slashed
terminator, with the label `LIQUIDATION THRESHOLD — NO PRICE TO PUT IT AT`).

### Linter results

`python3 skills/deck-author/tools/check_deck.py <deck>/index.html --quiet`

| deck | result |
|---|---|
| `staging/deck/index.html` | **PASS** — 14 slides, brand Medici, footer class external, 0 errors, 3 notices |
| `presentation-writing/deck/index.html` | **PASS** — 14 slides, same |
| `pitch-deck-mastery/deck/index.html` | **PASS** — 14 slides, same |

The three notices are identical and expected on every deck: `C-PURE-BLACK` and
`C-PURE-WHITE` (the brand contract *pins* `#000000` and `#FFFFFF`, and the linter's own
message says so), and `P-DECKMD-COUNT` (no sibling `deck.md`; the task's deliverable list
does not include one, so story parity is checked against `staging.yaml` instead — see
below).

Plus a stdlib structural gate of my own, `_build/validate.py`, which asserts what the deck
linter does not cover and covers the films at all: doctype, slide count == slot count,
`deck-footer` meta and the per-slide print footer on both media, folio per slide,
`@page{size:1280px 720px}`, film scene count, **per-scene `data-dur` identical to the
contract's `vo_seconds` list**, `window.__player` export, `?scene=` override, the
1920×1080 stage, SCRIPT.md row count == scene count, zero remote assets, and the four
woff2 files present in all six directories. `PASS: all six artifacts structurally clean`.

### Slots and scenes: nothing dropped

Every slot and every scene of all three contracts is rendered, in contract order, with the
headline claim verbatim. Two things worth recording rather than burying:

1. **`pitch-deck-mastery` has 13 slots plus an `appendix` block (A1).** The appendix is
   outside the numbered `slots:` list in the contract. It is rendered as plate 14 with
   layout `L-SEQUENCE` rather than dropped, so the pdm deck is 14 plates for 13 slots + A1.
2. **Supporting points are rendered as plate annotations, not as bullets.** The brief asks
   for 90% visual / 10% text, so each supporting point becomes a `LABEL / value` pair on
   the plate's foot rule (18px body, ≥4.5:1 on `#000`), and the numbers themselves are
   drawn into the figure where the figure can carry them (`$620M+`, `$8M → $0`,
   `$0.895 ON $1.00`, `54` filled marks and `5` hollow ones). No supporting point was
   deleted; two were shortened for line-breaks only (never re-worded into a new claim):
   pdm slot 6's two holder lines and staging slot 12's audit line.
3. **Transitions are not rendered anywhere.** All three contracts carry a `transitions:`
   block; those are speaker lines between slots, not slots, and there is no slot to hang
   them on. Recorded here rather than silently dropped.

### Brand fights

The house brand and the canvas-design skill disagree in four places. Each was resolved in
the brand's favour, because that is what `brand` mode means:

1. **"Use different fonts. Search `./canvas-fonts`."** The skill ships 20-odd display
   faces and explicitly wants typographic variety, plus "generally the font should be
   thin". The brand pins one family for everything and forbids a CDN. Resolved: IBM Plex
   Sans + IBM Plex Mono, self-hosted, hierarchy from weight/size/air only. The skill's
   instinct is not wasted — it is spent on *scale* contrast instead of *face* contrast
   (11px tracked mono labels against 30px SemiBold claims against a 34px numeral).
2. **"Bring the font onto the canvas, not typeset digitally."** Unimplementable in HTML
   without images, and images are the wrong medium for a deck that must print and stay
   selectable. Not attempted; the closest legitimate move — type as drawn element — shows
   up as the in-figure `P`, `N`, `S`, `1.00` labels, which live inside the SVG in the
   drawing's coordinate space rather than in the HTML flow.
3. **Chart colour.** Brand §7.2 pins chart lines as P = Gold `#D4A843`, N = Danger
   `#FF4444`; `brand.toml`'s `[marks].usage` says "Gold appears ONLY inside the mark", and
   §2.3 says the functional reds/greens are "used only functionally (pass/fail/warn),
   never decoration". Those three rules cannot all hold on a P/N payoff chart. **Override,
   deliberate:** P is Electric Blue (§2.1 names Electric Blue "P Token representation") and
   N is white hatch on black. Rationale: red/green on the two legs would read as bad/good,
   which is exactly the wrong message about a payoff identity; gold stays inside the mark.
   Electric Blue use stays inside the ≤2/slide budget — on the payoff plate it is the P
   region (1) and the strike marker (2), and nothing else.
4. **The mark.** The shipped `deck-skeleton-external.html` symbol library is the *Assay*
   octagonal/shield marks, not Medici's. Rather than put another product's mark on a Medici
   deck, the Medici mark was drawn from brand-guide §1.1's element table (solid Electric
   Blue left stem = the whole; the split point; upper blue stem = P; lower green stem = N;
   gold value dot). It appears once, on the cover.

### What the tool refused, or could not express

* **The skill has no concept of a sequence.** Its entire model is one page ("Create one
  single page, highly visual, design-forward PDF"), with a bolted-on MULTI-PAGE OPTION that
  says the extra pages should be "unique twists and memories of the original" and "almost
  tell a story in a very tasteful way". That is a coffee-table-book instruction, and it is
  actively wrong for a 14-slot argument where slot order is contractually fixed and each
  plate must turn one specific value. **This was the main fight, and I logged it in detail
  below.**
* **No motion vocabulary at all.** Nothing in the skill addresses time, and the explainer
  is half the deliverable. The motion system (hold / accumulate / strain / rupture /
  assemble / arrest / divest / cadence) comes entirely from the messaging contracts'
  `motion_role`, not from the design skill. What the skill *did* usefully constrain was
  restraint: "if the instinct is to draw a new shape, STOP" translates cleanly into "quiet
  scenes stay quiet", which is also what the contracts demand.
* **No output format but PNG/PDF.** "Output only .md files, .pdf files, and .png files" is
  stated twice. The task's medium is HTML, so this was overridden wholesale. The cost is
  real: the skill's craft advice assumes a fixed canvas it can inspect, and HTML text
  reflows — which is why the overflow bug above existed at all and why the browser audit
  was necessary.
* **Accent budget is invisible to the linter.** `check_deck.py` counts accent uses by CSS
  class (`kicker` / `accent`), so Electric Blue carried inside inline SVG is not counted;
  all three decks report 0 accent uses. The ≤2/slide rule was therefore held by hand and
  by construction (blue appears only as the P region and the strike marker), not by the
  gate. Worth fixing in the linter, not here.

### How much the poster-art framing fought the slide medium

A lot, and in three specific ways — this is the honest answer to the question.

1. **One page vs fourteen.** The skill's craft standard is *per canvas*: "one single page",
   balanced, self-contained, nothing else on it. A deck's craft standard is *per series*:
   the container must become invisible so the eye reads only what changed. Followed
   literally, the skill produces fourteen beautiful unrelated posters. The resolution was
   to move the skill's compositional ambition down one level — the *system* (frame, rail,
   margins, plate numbering, provenance strip) is invariant across every plate and every
   deck, and the artistry is spent inside a fixed window. The MULTI-PAGE OPTION's advice
   ("unique twists and memories of the original") was explicitly ignored; a variation-set
   would have destroyed the argument's legibility. Cost of the fight: the shared library
   had to be designed before any plate was drawn, which is the opposite of the skill's
   "make the masterpiece first, then extend it" order.
2. **"Text as rare, powerful gesture" vs a contract that fixes the words.** The skill wants
   text minimal and subordinate; the staging contract supplies a mandatory verbatim
   headline claim per slot plus 2–5 supporting points, and the read-fallback lane requires
   the claims to stand alone. Straight conflict. Resolution: the claim gets one line at
   30px (the second-largest thing on the plate, never the largest — the figure is), and the
   supporting points are demoted to clinical annotations at the foot, which is the only
   place the skill's aesthetic would tolerate them. The 90/10 target is met by area, not by
   word count; on a plate like `staging` 08 the figure owns roughly two thirds of the field
   and the text is a claim, three annotations and a source line.
3. **"Never explain, let the composition tell the story" vs an educational brief.** The
   skill's ethic is that information lives in design and the viewer does the work. Brief
   goal 3 is that a finance-literate non-DeFi audience must be able to *redraw* the P/N
   payoff tomorrow. A poster can be enigmatic; a teaching diagram cannot. The payoff plate
   is where this was resolved and it is the plate the whole design is built around: it
   carries the constant edge, both regions, the strike, both cases written as arithmetic
   (`x ≤ S → P 1.00 · N 0.00`, `x > S → P S/x · N 1 − S/x`), and the axis names — which is
   more text than the skill would ever sanction on an art object, and exactly the amount
   the brief requires. Where the skill *won* was the negative space around it: no legend,
   no callout boxes, no arrows-and-labels clutter.

Two places the poster framing helped rather than hurt, for balance: the bold moment
(`staging` 06 / `pw` 04, Black Thursday) is a genuine poster — one dated event, 64 hairline
marks, one numeral — and it is the strongest plate in the set precisely because the skill's
instinct applies unmodified. And the closing plate is a pure absence composition (the
constant edge, a surveyed empty field, seven refused attempts to place a liquidation
price), which no slide-deck convention would have produced.

### Files

```
brand/PHILOSOPHY.md                          the movement (step 1, written first)
brand/<messaging>/deck/index.html            + 4 woff2
brand/<messaging>/explainer/explainer.html   + SCRIPT.md + 4 woff2
brand/_build/plates.py                       20-figure SVG library, one vocabulary
brand/_build/content.py                      slot/scene content, claims verbatim
brand/_build/build.py                        emits all six artifacts (2.1 s)
brand/_build/validate.py                     structural gate over all six
```

`_build/` is process, not deliverable; it is kept because it is the honest record of how
the six artifacts were made and because a fix to one plate has to propagate to all of them.

---

## free

Design contender **canvas-design**, mode **free**. Movement invented for this run:
**INVARIANT FIELD** (`free/PHILOSOPHY.md`). Total wall clock **≈ 95 min**, one session.

### Artifacts

| artifact | path | size | time-to-artifact |
|---|---|---|---|
| philosophy | `free/PHILOSOPHY.md` | 8 KB | 12 min (after ~20 min reading the 3 contracts + brief) |
| plate library | `_build/plates.py` (23 plates, shared by all 3 decks) | — | 30 min |
| deck · staging | `free/staging/deck/index.html` | 908 KB | 14 min (first deck; +2 min each after) |
| deck · presentation-writing | `free/presentation-writing/deck/index.html` | 872 KB | 4 min |
| deck · pitch-deck-mastery | `free/pitch-deck-mastery/deck/index.html` | 872 KB | 6 min (+2 new plates) |
| motion engine + scene vocabulary | `_build/ex.py`, `_build/scenes.py` (17 scene constructors) | — | 25 min |
| explainer · staging | `…/staging/explainer/{explainer.html,SCRIPT.md}` | 933 KB | 8 min |
| explainer · presentation-writing | `…/presentation-writing/explainer/…` | 794 KB | 3 min |
| explainer · pitch-deck-mastery | `…/pitch-deck-mastery/explainer/…` | 798 KB | 3 min |
| render-and-look passes | 26 headless Chrome screenshots, read and fixed | — | 20 min |

All six artifacts are single self-contained files; the four typefaces
(**Gloock**, **Jura Light/Medium**, **GeistMono Regular/Bold** — all from the skill's own
`canvas-fonts/`) are base64-embedded, so there is not one `http(s)://` reference in any file
(validator confirms; only the SVG namespace URI appears).

### The tool's process, as actually run

The canvas-design SKILL.md prescribes exactly two steps, and both were run literally:

1. **DESIGN PHILOSOPHY CREATION** — wrote a named movement (1–2 words: *Invariant Field*),
   six paragraphs covering space/form, colour/material, scale/rhythm, composition/balance,
   visual hierarchy, and a craftsmanship paragraph; kept generic per the skill's instruction
   ("without mentioning the intention of the art"). Saved as `.md` before any pixel existed.
2. **DEDUCING THE SUBTLE REFERENCE** — the skill's mandatory middle step. Deduced thread:
   *a conservation law*. That became the one device the whole series is built on — a constant
   line at a fixed height on every plate and every scene, and a progress indicator made of two
   segments (warm elapsed / cold remaining) whose **total width never changes**. On the payoff
   plate the stacked P+N top edge is that same dead-flat line. Someone who knows the mechanism
   sees `P + N ≡ collateral` on slides that contain no chart at all; everyone else just reads
   a series that feels unaccountably level.
3. **CANVAS CREATION** — followed its stated visual programme: "borrow the visual language of
   systematic observation — dense accumulation of marks, repeated elements… sparse, clinical
   typography and systematic reference markers that suggest a diagram from an imaginary
   discipline." Concretely: the recurring **344-mark grid** (each mark = $1B represented on
   Canton, a sourced figure), plate catalogue numbers, unit captions, tick rules, and a
   two-body-plus-one-alarm palette.
4. **FINAL STEP** ("it isn't perfect enough… refine, don't add") — ran as a real second pass:
   26 headless-Chrome screenshots read back and fixed, and the rule *"if the instinct is to
   draw a new shape, STOP"* was obeyed twice — the `risk_register` and `no_such_x` plates were
   **rebuilt from the same elements** rather than decorated (three columns → three full-width
   bands; 37 overlapping "NO" labels → 37 counted dots with one caption).
5. **MULTI-PAGE OPTION** was the bridge to the deck: "treat the first page as a single page in
   a coffee-table book… the next pages unique twists and memories of the original." That is the
   only part of the skill that anticipates a sequence at all, and it is what made a 14-slot deck
   expressible as a *plate series* rather than as slides.

References used from the skill package: `SKILL.md` (all sections), `canvas-fonts/` (chose 4 of
the 40 faces). Nothing else ships with it — no layout system, no grid, no colour tooling, no
animation guidance, no HTML anything.

### How much the poster-art framing fought the slide medium

Honestly: **it fought hard on structure, and it won on look.** Itemised —

1. **Output format is hard-coded to the wrong thing.** SKILL.md says, three separate times,
   "Output only .md files, .pdf files, and .png files" and "one single page… PDF or PNG output".
   HTML, keyboard nav, print CSS, a 1920×1080 timeline and `window.__player` are all outside
   what it will admit exists. Every mechanical requirement of this brief had to be supplied from
   outside the skill. **Override:** treated its "canvas" as an abstract 1136×H drawing box and
   wrote my own deck shell, print pagination and motion engine around it.
2. **"One single page" vs. 14 slots.** The skill's whole gravity is the single masterpiece
   plate. The multi-page paragraph is one sentence long and is framed as an *exception*. Framing
   a 14-slot argument as a plate series is a reading of the skill, not an instruction in it.
3. **"90 % visual / 10 % text" vs. a contract with up to six supporting facts per slot.** This
   was the sharpest fight. The messaging contracts are text-dense by construction, and the
   quality floor demands ≥ 18 px body. Resolution: an explicit two-tier text system — *apparatus*
   (plate numbers, units, axis labels, tick captions: 10–15 px, deliberately at the edge of
   visibility, carrying no unique fact) and *register* (18 px mono, carrying every contract fact
   that the drawing does not itself carry). Nothing was dropped; see the accounting below.
4. **"Most of the time, font should be thin" and "bring the font onto the canvas, not typeset
   digitally".** Second half is unrunnable in HTML — text has to be typeset. First half is
   actively wrong for a 1280×720 projected headline claim; Jura Light is used for inscriptions
   and quotes only, and headline claims are set in Gloock, a high-contrast display serif, at
   31–41 px. **Override recorded.**
5. **"Keep the design philosophy generic without mentioning the intention of the art"** is in
   direct tension with a brief whose whole point is teaching one specific mechanism. Followed
   it literally in `PHILOSOPHY.md` (the movement never mentions collateral, options or finance)
   and put the deduced subject in a clearly-marked *Working note* underneath.
6. **Silence on motion.** The skill has no vocabulary for time. The eight motion verbs
   (`hold / accumulate / strain / rupture / assemble / arrest / divest / cadence`) are taken
   from the *messaging contracts'* `motion_role` fields, not from the design tool — and then
   mapped onto a declarative `data-a / data-t0 / data-t1` engine of my own. The one place the
   skill helped was negative space discipline: `arrest` (pdm s5) is 2.5 s in which *nothing on
   screen moves*, which is a very canvas-design idea applied to film.

Where it earned its keep: the "scientific-bible / systematic observation" paragraph is a genuinely
good generator. The 344-mark field, the counted 54-template grid (9 rows of 6 = 9 modules), the
falling marks in the Black Thursday plate and the 37 tested prices are all *honest encodings of
sourced numbers* that arrived because the skill told me to accumulate marks rather than draw
icons. And "the alarm colour is spent once" produced a real dynamic: vermilion appears on exactly
one plate per deck, then returns only as an **absence** (the liquidation line that is drawn and
withdrawn).

### What the tool did with freedom

- **Palette**: deep plate ground `#06080B`; cream ink `#EDE7DA`; a two-body chromatic system —
  warm brass `#E9B24C` = P (the part kept), cold cyan `#59D2E0` = N (the part given away) — used
  *only* semantically, never for emphasis; one alarm `#FF4A2E`, spent once per series. Body text
  contrast ≈ 13:1, dimmed register ≈ 8:1, both well over 4.5:1.
- **Type**: Gloock (display serif, monumental numerals) / Jura Light (thin inscriptions) /
  GeistMono (all apparatus). No Inter, no system stack, no default-deck look.
- **Structure**: full-bleed constant line at a fixed y on all 42 slides and all 25 scenes;
  the conserved progress bar; plate catalogue numbering; the payoff drawn as a *stacked* area
  whose top edge is dead flat, with the liquidation line annotated as an absence.
- **Motion**: meaning-only. The bold moment of each film is the only scene permitted to break;
  quiet scenes are genuinely quiet; the `divest` scenes delete their own apparatus on screen.

### Slots and supporting points — full accounting (nothing dropped)

Every slot and every scene of all three contracts is rendered, in contract order, with headline
claims verbatim. **41 deck slots + 1 appendix = 42 slides; 25 scenes.**

- `pitch-deck-mastery` has 13 slots **plus an `appendix` block (A1)**. A1 is rendered as slide 14
  (the roadmap plate) rather than dropped, so that deck is 14 slides.
- Supporting points are never deleted, but some are **rendered inside the drawing instead of as a
  register line** — that is the 90/10 rule doing its job. The cases: staging d8's two payoff
  branches (drawn as `P = 1.00 / N = 0` and `S/x / 1 − S/x` on the plate, plus stated in full in
  the register); staging d11's first two objection points (drawn as `P = S/x`, "no floor · never a
  cliff", "continuous · computable · the income"); presentation-writing s01's P/N description
  (drawn as the two bar captions); pitch-deck-mastery slot 02's threshold line and $8M/$0 figures
  (drawn), slot 04's three payoff rows (drawn), slot 05's two absence points (drawn). In every one
  of those cases the *number* is on screen at ≥ 17 px inside the plate.
- **Nothing was un-renderable.** No slot was logged out.

### Linter

Brand mode's `check_deck.py` is a **brand contract** checker (IBM Plex pin, `data-layout` pool,
house geometry, Electric Blue budget), so it is not the right instrument for `free`. Run anyway
on `free/staging/deck/index.html` for the record: **exit 0 with 28 findings**, of which 27 are
by-design brand deviations that free mode explicitly licenses (`H-FONT-PIN` ×8 for
Gloock/Jura/GeistMono, `H-LAYOUT-POOL` ×14 for no `data-layout`, `H-GEOMETRY` for a different
scale-to-fit transform). The 28th, `H-FOOTER-PRINT` ("no `.slide::after` print rule"), is a
false positive against this construction: the footer is a real `<footer>` element inside every
`.slide`, and each `.slide` is one printed page, so it lands on all 14 pages.

Free mode was instead validated by `_build/validate.py` (stdlib only) — **ALL PASS**, 66 checks:
slide count == slot count on all three decks, `<footer>` on every slide, `<meta name="deck-footer">`,
`@media print` with `size:1280px 720px`, 1280×720 stage, ←/→ + click nav, slide counter, register
body ≥ 18 px, no remote refs; explainers: scene count == contract scene count, **durations sum to
exactly 120 / 132 / 143 s (the contracts' own `vo_seconds` totals, unaltered)**, 1920×1080 stage,
`window.__player = {scene, t, total, seek}`, `?scene=N`, Space/→, progress bar, footer, no
audio/video/TTS, smallest SVG type 18 px; and `SCRIPT.md` row count == scene count.

No puppeteer/playwright is installed, so the **render-and-look** gate was run with headless
Chrome (`--headless=new --screenshot`) directly: 26 frames across all six artifacts, including
mid-animation frames via a `?scene=N&p=0.0–1.0&paused=1` tooling hook added to the player. Bugs
found and fixed *only* by looking: solid-cream fills where an animated opacity target was missing
(three scenes), a payoff annotation colliding with the plate apparatus, a register overrunning the
footer, two plates that did not fill their box, an off-canvas annotation, and a threshold line that
was "erased" by overpainting (replaced with a `flash` verb that draws it and then withdraws it —
better motion *and* better meaning).

### Friction, in order of cost

1. **The skill's PNG/PDF framing** — every structural requirement of the brief had to be built
   from scratch (deck shell, print pagination, timeline engine, seek API). ~40 % of the session.
2. **Text density vs. "90 % visual"** — reconciling six supporting points per slot with a
   philosophy that treats a sentence as an intrusion. Solved with the apparatus/register split
   plus per-slot auto-fitting (register height is measured, the plate takes what's left).
3. **No headless renderer installed** — the first four screenshots were silently stale because
   the capture script broke early on a pre-existing file; two rounds of "fixes" were evaluated
   against old images before the bug was found. Lesson recorded: always `rm` the target first.
4. **A plate coordinate inset.** Plates are drawn in a 152…986 box inside a 1136-wide column, so
   figures sit inset from the headline/register margin. Considered a full re-coordinate, decided
   against it under time — the constant line runs the full width and ties the composition, so the
   inset reads as a figure set within the page. Logged as the one thing I would change next.
