# Design bake-off review — academic-pptx narrative rigor

Rubric: `skills/review/academic-pptx/SKILL.md` + `content_guidelines.md` + `slide_patterns.md`. Only its checks are applied: action-title test, ghost-deck test, exhibit discipline, structured-argument mode, citation standards, QA checklist. Subjects: 30 decks (5 tracks × brand/free × 3 messaging) + 30 `SCRIPT.md`. `impeccable-polish` is out of scope. Titles/exhibits/citations/type were extracted programmatically (`html.parser`); the mechanism, cover and close slides of all 30 were read.

**Mode.** Every deck is *structured argument* (product pitch to a finance-literate technical audience, evidence-evaluating) — Step 1 default applies, not visual/narrative.

**Split (a)/(b).** The three messaging contracts fix all 14 headline claims verbatim, and all ten track-modes render all 14 in order with no reorder, rewrite or drop. So the ghost-deck *wording* is inherited and design tools are scored only on: exhibit choice, whether the exhibit supports the claim, key-finding annotation, citation rendering, title treatment, text/type discipline, speaker support.

**Measurement basis.** A 1280×720 stage standing in for a 10″×5.625″ 16:9 slide gives 1 pt ≈ 1.778 px, so the rubric's floors are: title ≥ 43 px, body ≥ 36 px, citation 21–25 px. **No deck clears the body floor and only two clear the title floor** — a systemic result reported once here rather than ten times. Counts below are per 42 slides (3 messaging variants × 14).

---

## canvas-design / brand

| Check | Result |
|---|---|
| Action title dominant | PASS — `.claim` is the largest text; `PL. 03 · DIAGRAM · SERIES OF 14` is a breadcrumb, not a competing topic label |
| Contract fidelity | 42/42 slots, verbatim, in order |
| Exhibit present | **42/42** — a purpose-built SVG on every slide, `role="img"` + `aria-label` = the action title (13/14) |
| One exhibit per slide | PASS — the second SVG is an `aria-hidden` frame rule, not an exhibit |
| Key finding annotated | PASS — `~0 · EARLY 2025 / $620M+ · MAR 2026 / 87% UTILISATION` on the chart; `THE CONSTANT EDGE` on the payoff |
| In-slide citation | **42/42** — `SRC · canton-pitch-deck Sl. 3, 9 · rwa-redstone-2026 Part 2` (file + slide level) |
| Text / type | FAIL — median 94 body words (cap ~40), 0/42 slides at or under; title 30 px (17 pt), body 18 px (10 pt), citation 10.5 px (**6 pt**) |

**Ghost deck: PASS** (inherited spine, fully preserved and fully exhibited).

1. *Citations are the best in the field and the least legible in the field* — 10.5 px is under half the 21 px floor. Fix: raise `.prov` to 22 px and drop one bullet per slide to pay for it.
2. *94-word median* — the exhibit already carries the point, so the bullets duplicate it. Fix: cut body text to the ~40-word cap on every slide that has an annotated exhibit (all of them).
3. *17 pt claim* is the smallest title of any track-mode. Fix: `.claim` 30 px → 44 px, matching its own `.h1`, and let `text-wrap: balance` take three lines.

## canvas-design / free

| Check | Result |
|---|---|
| Action title dominant | PASS — `.claim.sm/md/lg` scales with claim length |
| Contract fidelity | 42/42 |
| Exhibit present | **42/42** — one large annotated plate SVG per slide |
| One exhibit per slide | PASS — 0/42 doubles |
| Key finding annotated | **BEST-IN-BRAND-MODE-PEER** — the payoff plate carries `where a lending market / would put its threshold` pointed at the axis: a genuine "so what" callout, exactly §3's prescription |
| In-slide citation | **FAIL — 4/42** (only where the claim text itself names a source) |
| Text / type | FAIL — median 86 words, 0/42 under cap; title 31–41 px (17–23 pt), body 18 px (10 pt) |

**Ghost deck: PASS.**

1. *Citation collapse.* The same tool cites 42/42 in brand mode and 4/42 here — releasing the brand constraint deleted the source line. Fix: port the brand `SRC ·` footer into the free stylesheet; it is a footer slot that already exists (it holds only the confidentiality string).
2. *Cover carries an as-of date but no source* (`Material as-of July 2026`). Fix: append the two source files, as the brand cover does.
3. *No exhibit is alt-texted below the cover* despite `role="img"` on all 14 — the labels repeat the claim rather than describing the graphic. Fix: describe the shape, not the headline.

## algorithmic-art / brand

| Check | Result |
|---|---|
| Action title dominant | PASS — `h2` 33 px over a `kicker` topic label |
| Contract fidelity | 42/42 |
| Exhibit present | **FAIL — 0/42 representational exhibits.** Every slide is backed by a seeded p5 particle field (`plate`), a background, not an exhibit |
| One exhibit per slide | n/a |
| Key finding annotated | **FAIL** — on the payoff slide, `N`, `P`, `price x →`, `strike S` are `<span class="annot">` labels pinned at `left:92.5%; top:24%` over an emergent field. Cover the title and the exhibit says nothing; the labels assert a geometry the generative system does not guarantee |
| In-slide citation | **FAIL — 4/42** |
| Text / type | Best text discipline in the field (median 65 words, 5/42 under cap); title 33 px (19 pt), body 18 px (10 pt) |

**Ghost deck: PASS on titles, FAIL on evidence** — the titles carry the argument alone because nothing under them corroborates it.

1. **Fabricated-figure risk (highest-severity finding in this review).** A mono readout `census · P 0.617 · N 0.383 · Σ 1.000` sits in the position a data readout occupies, on every slide. `0.617` appears nowhere in `source/medici/` — it is a live particle count from the art system, rendered as if it were a measurement. Fix: delete the readout, or relabel it unambiguously as a render statistic and move it out of the evidence zone.
2. *No exhibit supports any claim.* Fix: on the four claims that have a shape (payoff, deposit climb, comparison, decline curve), draw the shape deterministically and let the field stay behind it.
3. *Zero citations* while its own free-mode twin cites 41/42. Fix: reuse the free-mode `.src` footer.

## algorithmic-art / free

| Check | Result |
|---|---|
| Action title dominant | PASS — `h1.claim` 33–60 px, longest claims auto-downshift |
| Contract fidelity | 42/42 |
| Exhibit present | **FAIL — 0/42 representational**; same generative field, driven by p5 |
| One exhibit per slide | n/a |
| Key finding annotated | FAIL — same label-over-field pattern |
| In-slide citation | **41/42** — `<span class="src">canton-pitch-deck.md Slides 4, 7</span>` in the footer |
| Text / type | median 76 words, 3/42 under cap; title 33–60 px (19–34 pt), body 19–21 px (11–12 pt) |

**Ghost deck: PASS on titles, FAIL on evidence** (as brand).

1. *Same structural failure as its brand twin* — the argument is entirely in the titles. Fix as above.
2. *Better than brand on provenance* (41/42 vs 4/42) but `.src` is a single line with no per-figure attribution, because there are no figures to attribute. Fix follows from finding 1.
3. *The `censusRec` sampler is now measured off the drawn payoff*, which is defensible, but the film script still describes the payoff as "emergent, not drawn". Fix: state in-deck which numbers are measured from the corpus and which from the render.

## impeccable / brand

| Check | Result |
|---|---|
| Action title dominant | PASS — `h2` 33 px, `h2.big` 44 px on statement slides |
| Contract fidelity | 42/42 |
| Exhibit present | 14/42 (≈ 5 of 14 slides) — payoff SVG, comparison `<table>`, otherwise typographic |
| One exhibit per slide | 5/42 doubles |
| Key finding annotated | PARTIAL — payoff SVG labels `P + N = 1.00 at every price`; no callout on the deposit-growth claim |
| In-slide citation | **41/42, best placement in the field** — a slide-head mast: `Notice 03 / 14 · Collateral use · RedStone, as of March 2026`, i.e. source *and* as-of at the top where the audience reads it |
| Text / type | median 79 words, 2/42 under cap; title 33 px (19 pt), body **17.5 px (10 pt) — smallest body type in the field** |

**Ghost deck: PASS.**

1. *Nine of fourteen slides carry no exhibit.* Fix: the comparison, cost and status slots already have table-shaped content — promote them from prose to the `<table>` treatment already in the deck.
2. *17.5 px body*. Fix: `.cl.tight p` → 20 px, absorbed by cutting the 79-word median.
3. *The mast is the citation, so a reader who prints the deck loses the as-of on figure captions.* Fix: repeat the as-of beneath the payoff and growth figures, per §5 "attribution caption directly beneath the figure".

## impeccable / free

| Check | Result |
|---|---|
| Action title dominant | PASS — serif `.claim` 37–57 px (21–32 pt), best title scale in the field |
| Contract fidelity | 42/42 |
| Exhibit present | 11/42 (≈ 4 of 14) |
| One exhibit per slide | PASS — 0/42 doubles |
| Key finding annotated | **WEAKEST of the tools that drew a chart** — the payoff SVG's text is `1.00 / 0.50 / 0 / strike S / reference price x →`: axis furniture only, no `P`, no `N`, no invariant callout |
| In-slide citation | 41/42, `.src` italic 18 px |
| Text / type | median 80 words, 0/42 under cap; body 19 px (11 pt) |

**Ghost deck: PASS.**

1. *The mechanism exhibit fails the cover-the-title test* — cover the claim and the chart is an unlabelled pair of regions. Fix: label the P and N regions and add `P + N ≡ 1.00 at every x` on the flat edge.
2. *Four exhibits across fourteen slides* in a deck whose whole argument is a payoff shape. Fix: give the two maturity cases their own drawn exhibit rather than a prose pair.
3. *`.src` at 18 px sits below the citation floor while the claim runs at 57 px* — the largest title-to-citation ratio here. Fix: 22 px `.src`.

## visual-explainer / brand

| Check | Result |
|---|---|
| Action title dominant | PASS — `h2` 33 px over a muted kicker |
| Contract fidelity | 42/42 |
| Exhibit present | **25/42 (≈ 8 of 14) — highest rate after canvas-design** |
| One exhibit per slide | **8/42 doubles — most in the field** (chart + table on the same claim) |
| Key finding annotated | PASS — payoff SVG carries `P + N = collateral, at every price` on the flat edge |
| In-slide citation | 41/42 — `<span class="src">Medici Canton briefing, slides 4 · 7 · July 2026</span>`: carries the as-of, but renames the file to a prose title, so it is less traceable than the file-level citations elsewhere |
| Text / type | median 76 words, 4/42 under cap; title 33 px (19 pt), body 18 px (10 pt), `.cmp li` **16 px (9 pt)** |

**Ghost deck: PASS.**

1. *Eight double-exhibit slides.* §3: two charts are either one comparison (combine) or two points (split). Fix: on each, keep the chart and demote the table to the appendix — or drop the chart and keep the table where the exact values are the point.
2. *Citations name "Medici Canton briefing" rather than `canton-pitch-deck.md`.* Fix: cite the file, keep the as-of.
3. *9 pt comparison text* on precisely the slides asking the audience to read across two columns. Fix: `.cmp li` 16 → 20 px and cut a row.

## visual-explainer / free

| Check | Result |
|---|---|
| Action title dominant | PASS — `.claim` 46 px = **26 pt, the only track-mode clearing the 24 pt title floor on every slide** |
| Contract fidelity | 42/42 |
| Exhibit present | 16/42 (≈ 5 of 14) |
| One exhibit per slide | 4/42 doubles (`<figure>` + `<svg>` + `<table>` on the maturity claim) |
| Key finding annotated | PASS — `P + N ≡ collateral` on the chart, cases in the paired table |
| In-slide citation | 41/42 — rail `statement / canton-pitch-deck.md Slides 4, 7` (file level) |
| Text / type | median 72 words (max 140), 3/42 under cap; body 20–21 px (11–12 pt), **best body scale in the field**; `.rail .foot` 12 px (7 pt) |

**Ghost deck: PASS.**

1. *The maturity slide runs a chart and a table of the same two cases.* Fix: keep the table (the exact values are the point) and move the curve to the adjacent mechanism slide, which has room.
2. *140-word maximum* on the slide that most needs to be read at a glance. Fix: the table already states both cases — delete the prose restating them.
3. *`.overlay li` at 15 px (8 pt)* is unreadable at any projection distance. Fix: 20 px, or move the overlay content to speaker notes, which this deck does not yet have.

## html-ppt / brand

| Check | Result |
|---|---|
| Action title dominant | PARTIAL — the claim is the largest text, but three headings stack above it: `Medici` / `What changed` (eyebrows) + `Collateral use, at scale` (kicker). Two of the three are topic labels the rubric replaces with action titles |
| Contract fidelity | 42/42 |
| Exhibit present | 15/42 (≈ 5 of 14) |
| One exhibit per slide | 3/42 doubles (payoff SVG + case table) |
| Key finding annotated | PARTIAL — the payoff SVG labels `P + N = 1.00`, `P = S/x`, `N = 1 − S/x` but carries no callout naming the consequence |
| In-slide citation | **FAIL — 8/42, worst in the field** (`Source: RedStone RWA lending report 2026, Part 2 addendum` where present, and it is well-formed) |
| Text / type | median 67 words, 3/42 under cap; title 34 px (19 pt), body 18 px (10 pt) |
| Speaker support | PASS — `.notes` per slide with a presenter overlay (4 slides populated) |

**Ghost deck: PASS.**

1. *Citations on 8 of 42 slides* while its free twin manages 39. Every `$620M`, `$344B`, `−1.25%/yr` on an uncited slide is a §5 violation. Fix: the `Source:` line already exists — emit it on all 14.
2. *Three headings above the action title* dilute it. Fix: drop the `What changed` eyebrow; keep `Medici` and the claim.
3. *Speaker notes on 4 of 14 slides* while the deck carries 67 body words per slide. Fix: fill all 14 and move the orientation prose off the slide into them.

## html-ppt / free

| Check | Result |
|---|---|
| Action title dominant | PASS — `.h2` 42–54 px (24–30 pt), clears the title floor |
| Contract fidelity | 42/42 |
| Exhibit present | **FAIL — 6/42 (≈ 2 of 14), lowest in the field**; twelve of fourteen slides are kicker + claim + bullets |
| One exhibit per slide | 3/42 doubles |
| Key finding annotated | **BEST IN THE BAKE-OFF** — the payoff SVG carries `no liquidation line fits anywhere on this axis` alongside `P — Protected`, `N — Amplified`, `P + N = 1.00 collateral, at every price`. This is the one exhibit in 30 decks that states its own "so what" on the chart |
| In-slide citation | **39/42** — `Source: canton-pitch-deck.md Slide 2 ("liquidation is the mechanism"); rwa-redstone-2026.md Part 2`, with the quoted phrase: the most traceable citations in the field |
| Text / type | **FAIL — median 89 words, max 150**, 2/42 under cap; body 19 px (11 pt), `.src` 16 px (9 pt) |
| Speaker support | PASS — `.notes` on every slide (52 references) plus a print stylesheet pair |

**Ghost deck: PASS.**

1. *It proved it can build the field's best exhibit, then built two.* Fix: apply the payoff slide's treatment to the deposit-growth, comparison, cost-of-P and status claims — four slides, four shapes already implied by the copy.
2. *89-word median on a deck that has speaker notes on all 14 slides* — the mechanism to carry that prose already exists and is unused. Fix: move everything past the first three bullets into `.notes`.
3. *`.src` at 9 pt* undercuts the best citation content in the bake-off. Fix: 22 px.

---

## Secondary — inherited from the messaging contract (scored per messaging, not per design tool)

| Messaging | Action titles | Ghost deck — deck | Ghost deck — film | Inherited defects |
|---|---|---|---|---|
| `staging` | 14/14 claim sentences (slides 8, 13 imperative but still state a takeaway) | **PASS** — SCR spine intact: situation 2–3, complication 4–6, pivot 7, mechanism 8, comparison 9, venue 10, cost 11, status 12, ask 13, close 14 | **PASS** — 9 scenes, 120 s, same spine | Slides 2 and 3 both hold the situation beat and slightly collide ("assets sitting idle" then "$620M in a year"); slide 8 opens with an imperative where a finding would be sharper |
| `presentation-writing` | 14/14; slide 14 is a fragment, not a sentence | **PASS — strongest of the three.** Complication lands at 3–4, resolution at 5, mechanism 6–8, positioning 9–11, honest status 12, ask 13, close 14. No slide could be moved without loss | **PASS** — 8 scenes, 132 s | Only the fragment close; nothing structural |
| `pitch-deck-mastery` | **11/14** — slides 6 ("Two legs, two holders, each with an intrinsic reason"), 11 ("Every risk we removed, and every risk we did not") and 14 ("Roadmap, compliance path and identity control plane — as of July 2026") are noun-phrase topic labels | **FAIL** — answer-first order is legitimate (§1 Option C), but the deck ends on a roadmap slide *after* the ask. §6 and the QA checklist require conclusions last, on screen during Q&A | **PASS** — 8 scenes, 143 s, ends on the ask; the film's ghost deck is better than its own deck's | Deck lane says "54 DAML templates", video lane VO says "fifty-four DAML contracts" — a template is not a contract; internal inconsistency in the contract itself |

**Citation accuracy (all three): PASS.** Every figure carried on a slide traces to `source/medici/` — `$620M+`/`87%` and `$423.5M`/`$106M`/`269 addresses` to `rwa-redstone-2026.md`, `$344B` and `5-10bps` and `−1.25%/yr` (9-yr Hypercall/ETH backtest) to `canton-pitch-deck.md`, Black Thursday `$8M → $0` to `asset-manager-pitch-deck.md`. The one number I could not trace — `0.617` — is design-authored, not inherited (algorithmic-art/brand, above).

**Shared inherited QA failures, not attributable to any design tool:** no References slide, no contact line or QR on the closing slide, no appendix and no labelled cut-slides. The 14-slot contract has no room for any of them; every tool that logged the gap logged it in NOTES.md rather than dropping a slot.

---

## Rankings — design tools, on (a) only

**brand**

1. **canvas-design** — 42/42 annotated, alt-texted exhibits and 42/42 file-level citations. Nothing else is close on evidence; it loses only on type scale and word count, both cheap to fix.
2. **visual-explainer** — the best exhibit rate after canvas-design and the invariant annotated on the payoff; docked for eight double-exhibit slides and 9 pt comparison text.
3. **impeccable** — best citation *placement* anywhere in the bake-off (source + as-of in the slide head), but nine of fourteen slides carry no exhibit and the body type is the smallest measured.
4. **html-ppt** — clean claim treatment and real speaker notes, undone by 8/42 citations and a three-deep heading stack above the action title.
5. **algorithmic-art** — no exhibit supports any claim, no citations, and a generative particle count rendered in data position with no corpus trace.

**free**

1. **visual-explainer** — the only track-mode clearing the title floor on every slide, best body scale, file-level citations, real chart-plus-table evidence; docked for four double-exhibit slides.
2. **canvas-design** — 42/42 exhibits and the best "so what" callout of the brand-mode peers (`where a lending market would put its threshold`), but its citations collapse from 42/42 to 4/42 against its own brand mode; that regression is what keeps it off the top.
3. **html-ppt** — owns the single best exhibit and the most traceable citations in 30 decks, and then ships only two exhibits in fourteen slides with the highest word counts in the field.
4. **impeccable** — best title scale and 41/42 citations, but four exhibits and the least-annotated payoff chart of any tool that drew one.
5. **algorithmic-art** — citations recovered to 41/42; the evidence layer is still absent.

---

## Blind spot

This rubric was written for a projector in a lecture hall and a `.pptx` file, and I applied it to a 1280×720 CSS stage. The px→pt conversion above is *my* extrapolation, not the rubric's: at a 27″ desk monitor or in a PDF the reader scrolls, an 18 px body is comfortable and a 10.5 px citation is merely small — so the "no deck clears the body floor" result reads as much as a genre mismatch as a defect, and I have weighted it lightly in the rankings for that reason. Three further limits. First, the rubric has no vocabulary for motion, so the explainers were tested only on their `SCRIPT.md` title sequence; whether the animation carries the P/N split meaningfully — the brief's actual test — is invisible to every check I ran, which is why algorithmic-art, whose entire argument is kinetic, may be systematically undersold here. Second, I read the DOM, not rendered pixels: a slide can pass "one exhibit, annotated, cited" in markup and still be an unreadable overlap on screen, and I cannot see collisions, contrast or the actual p5 output. Third, the academic rubric prizes the References slide, the appendix and the citation apparatus — machinery a ten-minute product pitch to asset managers would be wrong to carry — so its verdicts on citation density are genre-blind, and the three tools I penalised most for thin citations would likely be *more* effective decks in the room than the two I ranked first for citing everything. 
---

# Addendum — impeccable-polish (brand, free)

Two late track-modes, scored under the same rubric and the same extraction method. `impeccable-polish`
is `tracks/html-ppt/{brand,free}/` copied verbatim and put through impeccable v4.0.4's `polish`
(+`animate`) refine pass — a finish arm, not a design arm. Subjects: 6 decks (2 modes × 3 messaging)
+ 6 `SCRIPT.md`. Mode is unchanged (*structured argument*), the messaging contracts are unchanged, so
the (a)/(b) split above applies identically: the ghost-deck wording is inherited and this arm is
scored only on exhibit choice, exhibit support, key-finding annotation, citation rendering, title
treatment, text/type discipline, and speaker support.

**Extraction.** Same method as the main review — `html.parser` over all six decks, slides walked as
`<section class="slide">`, exhibits counted as `<svg>`/`<table>`/`<figure>` inside the slide,
citations matched on `.src`/`.prov` and on the citation string forms actually used, body words
counted off the stripped stage text, type sizes read out of the stylesheet. **I ran the identical
extractor over the `html-ppt` baseline in the same pass**, so every line below is a measured delta
rather than a comparison against numbers reported earlier. The measurement basis is unchanged:
1 pt ≈ 1.778 px, floors title ≥ 43 px, body ≥ 36 px, citation 21–25 px.

## The whole result, in one table

| check | html-ppt/brand | impeccable-polish/brand | html-ppt/free | impeccable-polish/free |
|---|---|---|---|---|
| slides | 42 | **42** | 42 | **42** |
| exhibit present | 15/42 | **15/42** | 6/42 | **6/42** |
| one exhibit per slide (doubles) | 3/42 | **3/42** | 3/42 | **3/42** |
| in-slide citation | 8/42 | **8/42** | 39/42 | **39/42** |
| speaker notes | 4/14 per lane | **4/14 per lane** | 14/14 | **14/14** |
| body words, median / max | 67 / 132 | **67 / 132** | 89 / 150 | **89 / 150** |
| action title px (`.h1` / `.h2`) | 46 / 34 | **46 / 34** | 72 / 54 | **72 / 54** |
| body px | 18 | **18** | 19 | **19** |
| citation px | 11 (`.conf`) | **12** | 16 (`.src`) | **16** |
| `h3` / `h4` px | 19 / 15 | **21 / 16** | 32 / 22 | **32 / 22** |

*Reconciliation note.* The word-count and citation-count rows above are quoted at the values the main
review reports, for continuity. My re-extraction uses a slightly different tokeniser and slide walk
and returns 78/132 words and 8/42 citations in brand, 100/157 words and 37/37 citations in free —
**and returns those same values for the baseline and the polish tree alike, digit for digit**. The
absolute numbers differ from the main review by method; the delta, which is what this addendum is
for, is exactly zero either way.

**Every check this rubric runs returns the same verdict on the polish arm as on its baseline, in both
modes.** The only measured movement in the entire extraction is three font sizes in brand mode — the
confidentiality footer 11→12 px, `h3` 19→21 px, `h4` 15→16 px — and not one of them crosses a floor.
Copy fidelity is 42/42 verbatim in order, as before; the three `SCRIPT.md` files are byte-identical
to the baseline's, so the film's ghost deck is the same ghost deck.

## impeccable-polish / brand

| Check | Result | Δ |
|---|---|---|
| Action title dominant | PARTIAL — the claim is still the largest text, and **three headings still stack above it**: `Medici` / `Where it stands` (eyebrows) + `The cost` (kicker). The pass moved the kicker down to group with the headline it labels (20 px above / 8 px below, was 8/16) — a proximity fix, not a count fix | proximity improved, count unchanged |
| Contract fidelity | 42/42 slots, verbatim, in order | 0 |
| Exhibit present | 15/42 (≈ 5 of 14) | 0 |
| One exhibit per slide | 3/42 doubles | 0 |
| Key finding annotated | PARTIAL — the payoff SVG still labels `P + N = 1.00`, `P = S/x`, `N = 1 − S/x` and still carries no callout naming the consequence | 0 |
| In-slide citation | **FAIL — 8/42, still the worst in the field.** The `Source:` line is still emitted on 8 slides of 42 | 0 |
| Text / type | median 67 words, 3/42 under cap; title 34 px (19 pt), body 18 px (10 pt), citation **12 px (6.75 pt)** | citation 11→12 px |
| Speaker support | PASS — `.notes` per slide, 4 of 14 lanes populated | 0 |

**Ghost deck: PASS** (inherited, preserved).

1. *All three of my findings against html-ppt/brand stand unchanged.* Citations on 8 of 42 slides
   while its free twin manages 39; three headings above the action title; speaker notes on 4 of 14
   while the deck carries 67 body words a slide. A refinement pass cannot emit a citation that is not
   in the source, cannot delete an eyebrow (that is copy), and cannot write speaker notes (that is
   authorship) — so the three cheapest, highest-value fixes on this deck are all outside its reach.
   Fixes: unchanged from the main entry.
2. *The one thing it did move is the citation, and it moved it 1 px.* `.conf` 11 → 12 px lifts the
   line from 6.2 pt to 6.75 pt against a 21–25 px (12–14 pt) floor — the correct direction, roughly
   3% of the distance. The pass's own recorded reason was contrast (3.4:1 → 6.1:1), which this
   rubric does not score and which is the right fix for a different problem. Fix: `.conf` → 22 px,
   which needs a slide with room, which needs the body word count cut, which needs copy.
3. *The type ladder tightened where the rubric was not looking.* `h3` 19 → 21 px removed a 1 px step
   against an 18 px body; `h4` 15 → 16 px. Both are real craft repairs and neither touches the title
   or body floors, which are the two this rubric fails every deck on. Fix: the ladder is now
   46/34/21/18/16/14 — moving it up one whole step is the change that would matter, and the pass
   explicitly declined it as a composition change.

## impeccable-polish / free

| Check | Result | Δ |
|---|---|---|
| Action title dominant | PASS — `.h2` 42–54 px (24–30 pt), clears the title floor | 0 |
| Contract fidelity | 42/42 | 0 |
| Exhibit present | **FAIL — 6/42 (≈ 2 of 14), still the lowest in the field** | 0 |
| One exhibit per slide | 3/42 doubles | 0 |
| Key finding annotated | **STILL BEST IN THE BAKE-OFF** — `no liquidation line fits anywhere on this axis` alongside `P — Protected`, `N — Amplified`, `P + N = 1.00 collateral, at every price` | 0 |
| In-slide citation | 39/42, still the most traceable in the field | 0 |
| Text / type | **FAIL — median 89 words, max 150**, 2/42 under cap; body 19 px (11 pt), `.src` **16 px (9 pt)** | 0 |
| Speaker support | PASS — `.notes` on every slide plus a print stylesheet pair | 0 |

**Ghost deck: PASS.**

1. *Zero delta on every check, including the type sizes.* The free pass changed no font size at all;
   its work was dead-CSS removal (40,026 bytes), easing, a bounce curve, gradient-filled text made
   solid, and two render-only defects in one explainer scene. Not one of those is a check in this
   rubric, which is the honest result rather than a gap in my extraction.
2. *It proved it can build the field's best exhibit, then built two — and the finish pass built
   none.* The recommendation stands verbatim: apply the payoff slide's treatment to the
   deposit-growth, comparison, cost-of-P and status claims. Four slides, four shapes already implied
   by the copy, and four exhibits a refinement arm is structurally forbidden from drawing.
3. *`.src` at 16 px (9 pt) still undercuts the best citation content in 30 decks.* The one place the
   pass did touch a citation-adjacent property was contrast in a different lane; the size floor is
   untouched. Fix: 22 px.

## Revised rankings — design tools, on (a) only

**brand (6)**

1. **canvas-design** — 42/42 annotated, alt-texted exhibits and 42/42 file-level citations.
2. **visual-explainer** — best exhibit rate after canvas-design; docked for eight double-exhibit
   slides and 9 pt comparison text.
3. **impeccable** — best citation *placement* in the bake-off; nine of fourteen slides carry no
   exhibit.
4. **impeccable-polish** — identical to html-ppt on every check that decides this ranking, and ahead
   of it by the only measurable movement in the extraction: the citation line 11→12 px and a repaired
   type ladder. A 1 px tie-break is a thin thing to rank on and I am naming it as such.
5. **html-ppt** — clean claim treatment and real speaker notes, undone by 8/42 citations and a
   three-deep heading stack above the action title.
6. **algorithmic-art** — no exhibit supports any claim, no citations, and a generative particle count
   rendered in data position with no corpus trace.

**free (6)**

1. **visual-explainer** — the only track-mode clearing the title floor on every slide, best body
   scale, file-level citations, real chart-plus-table evidence.
2. **canvas-design** — 42/42 exhibits and the best "so what" callout of the brand-mode peers; its
   citations collapse from 42/42 to 4/42.
3. **html-ppt** — owns the single best exhibit and the most traceable citations in 30 decks, then
   ships only two exhibits in fourteen slides with the highest word counts in the field.
4. **impeccable-polish** — **an exact tie with html-ppt on all nine checks and on all four type
   measurements**, so the incumbent holds the place and the challenger sits immediately behind it. A
   pass that changes nothing this rubric measures does not overtake the artifact it was copied from.
5. **impeccable** — best title scale and 41/42 citations, but four exhibits and the least-annotated
   payoff chart of any tool that drew one.
6. **algorithmic-art** — citations recovered to 41/42; the evidence layer is still absent.

## What polish bought — under this rubric

**Nothing, in free mode. One pixel, in brand mode.**

That is not a slight on the pass — it is what this rubric is for. Every check here is about *the
argument*: does a claim have evidence under it, does the evidence carry a "so what", does a figure
trace to a source, can a reader at the back of the room read the source when it does. Those
properties are decided when the deck is composed, and the refinement arm's own contract forbids it
from composing. The three findings I filed against html-ppt/brand — 8/42 citations, three headings
above the action title, notes on 4 of 14 slides — are all copy-and-structure findings, and all three
are on screen unchanged. The three against html-ppt/free — two exhibits in fourteen slides, an
89-word median with an unused notes mechanism, a 9 pt source line — likewise.

Two things are worth saying in the pass's favour, both invisible here. First, the brand arm moved its
citation in the right direction for the right reason: it lifted `.conf` from 3.4:1 to 6.1:1 because
the *mandated* confidentiality line was set below the threshold of sight, which is the same class of
defect as my "citations are the best in the field and the least legible in the field" finding against
canvas-design — this rubric measures citation legibility in points and would have scored that fix at
zero. Second, both arms provably preserved what this rubric cares most about: 42/42 verbatim slots in
contract order and byte-identical `SCRIPT.md` files, which is not a given for any pass that touches
a deck at all.

The generalisable finding: **a finish pass and a narrative rubric have almost no overlapping surface.**
If this bake-off is choosing a tool on argument quality, `polish` is not the lever; if it is choosing
on whether the argument survives contact with a projector, it moved one of my four type floors by 1
px and left the other three where it found them.

## Blind spot

The main review's blind spots all still apply, and this addendum adds one that cuts specifically
against the polish arm. **This rubric has no vocabulary for finish**, in exactly the way it has none
for motion. Contrast, spacing systems, focus rings, accessibility trees, dead stylesheet weight,
compositor-driven progress bars, easing curves — the entire content of both passes — appear nowhere
in the action-title test, the ghost-deck test, exhibit discipline or citation standards, so a genuine
zero here is compatible with a substantial improvement on any seat that grades the rendered artifact.
I have reported the zero as a zero because that is what the checks return, and a reader should not
read it as "the pass did nothing" but as "the pass did nothing *this rubric can see*". The reverse
also holds and is the sharper caution: the 1 px citation bump that decides my brand-mode tie-break is
a genuinely trivial difference, and had the pass moved that line the other way by 1 px I would have
had no principled basis for ordering these two at all.
