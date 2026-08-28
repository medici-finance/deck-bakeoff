# Design review — `open-design-review` seat

Reviewer: independent design seat, local bake-off. Read-only pass; nothing outside this file written.
Subjects: 10 finished track-modes under `tracks/{canvas-design,algorithmic-art,impeccable,visual-explainer,html-ppt}/{brand,free}/`.

## Rubric provenance (read this before the scores)

`skills/review/open-design-review/SKILL.md` is a **catalogue stub**, not a rubric: 43 lines of
OpenDesign frontmatter pointing at `github.com/garrytan/gstack`, carrying no jury weighting, no seat
definitions, no typed codes, no severity ladder, and no references. What survives is its *method* —
*"visual audit … before/after screenshots"*, i.e. **grade the rendered pixels, not the source**. I
applied that literally and took the missing scaffolding from the seat brief: **critic .4 / brand .2 /
a11y .2 / copy .2**, 0–10. The `CRIT-`/`BRAND-`/`A11Y-`/`COPY-` codes and `blocker`/`major`/`minor`
ladder are mine, not gstack's.

**Evidence base.** `shots/` held 0 PNGs, so I rendered my own: 30 CDP frames (deck slide 1, a
mid-deck slide, explainer scene 4 per track-mode) with animations seeked to 85% of their duration
and paused, 10 `pitch-deck-mastery` spot-checks, 8 verification re-renders. A11y figures are
**computed styles from the live DOM**, not greps — every visible text node, SVG resolved through
`fill`/`fill-opacity` not `color`, alpha composited onto the nearest opaque ancestor, WCAG 2.x
contrast. Floors: deck ≥18px at 1280×720, explainer ≥28px at 1920×1080.
## Measured a11y table (the shared evidence for every A11Y finding)

| track · mode | deck min px | deck items <18px | deck items <4.5:1 | worst deck CR | expl min px | expl items <28px | expl worst CR | `prefers-reduced-motion` blocks (deck/expl) |
|---|---|---|---|---|---|---|---|---|
| canvas-design · brand | 10 | 167/221 | **123** | 1.35 | 16 | 7/10 | 1.66 | 1 / 1 |
| canvas-design · free | 10 | 129/205 | **91** | 1.72 | 18 | 6/8 | 1.99 | **0 / 0** |
| algorithmic-art · brand | 11 | 36/127 | 29 | 1.55 | 16 | 11/24 | 3.66 | **0 / 0** |
| algorithmic-art · free | 12 | 6/9 | **1** | 2.65 | 28 | **0/8** | — | **0 / 0** |
| impeccable · brand | 11 | 186/186 | **2** | 1.85 | 22 | 6/10 | 1.85 | 1 / 1 |
| impeccable · free | 14 | 4/19 | **1** | 2.50 | 28 | **0/6** | — | 2 / 1 |
| visual-explainer · brand | 10.5 | 137/179 | **61** | 1.46 | 17 | 5/9 | 1.66 | 1 / 1 |
| visual-explainer · free | 12 | 13/16 | **1** | 4.14 | 20 | 5/10 | 3.33 | 1 / 1 |
| html-ppt · brand | 11 | 88/148 | 40 | 1.55 | 20 | 2/6 | 1.55 | 1 / 2 |
| html-ppt · free | 13 | 74/176 | **0** | — | 28 | **0/8** | — | 1 / 2 |

Decks keeping all 14 slides in the DOM are sampled whole; those mounting only the active slide give
floors. **Every** deck fails an 18px floor once chrome and citations count, so the discriminator is
the contrast column, not the size column.
### canvas-design · brand — **7.8** (critic 9.0 · brand 9.0 · a11y 3.5 · copy 8.5)

The best information design in the field: plate numbering, a hairline rule as the structural spine,
annotation as label-over-value pairs, and a payoff plot (plate 11) drawing the flat-then-`S/x`
decline with the strike marked, one callout at `$0.895` and a tick axis — a diagram an issuer could
redraw. Negative space is deliberate, not leftover. It is also the least legible deck here.

| code | sev | evidence | fix |
|---|---|---|---|
| A11Y-CONTRAST-01 | blocker | The brief's traceability line — `SRC · CANTON-PITCH-DECK SL. 1, 3 · HOUSE-BRAND-GUIDE §0.5` — renders `rgb(58,58,58)` on `#000` at 10.5px: **1.85:1**. Required content set below the threshold of sight. | Lift provenance to `#666` minimum (3.66:1) at 12px; it is content, not chrome. |
| A11Y-CONTRAST-02 | major | In-plate SVG labels carry the same fault: `ISSUED`, `HELD · 4 OF 72 POSTED AS COLLATERAL` at 13px `fill:#333` = **1.66:1**. 123 of 221 sampled strings are under 4.5:1. | Raise the plate-label token to `#AAA`; reserve `#333` for hairlines only. |
| COPY-OVERFLOW-01 | major | `pitch-deck-mastery` plate 07 clips two lines at the right panel edge: `$840M+ OF TOKENIZED RWA ALREADY DEPOSITED INTO LENDING PROTOC…` and `NO NO-LIQUIDATION DESIGN APPEARS IN THE 2026 LANDSCAPE`. NOTES.md claims a measured overflow audit; this survived it. | Constrain the stat-panel to the column and wrap; re-run the audit on all three messaging lanes. |
| A11Y-SIZE-01 | major | Explainer min 16px against a 28px floor; 7 of 10 strings under it, including the scene counter at 1.85:1. | Set the explainer type ramp from 28px up; it is a video canvas, not a page. |
| BRAND-MARK-01 | minor | The cover "M" mark renders blue **and green**. Brand §2.6 makes green functional-only and `brand.toml` says gold appears only inside the mark. | Use the plate-stripped `#assay-mark` symbol from the skeleton. |

### canvas-design · free — **6.5** (critic 7.5 · brand 8.5 · a11y 2.5 · copy 6.5)

A Didone display over mono annotation on near-black, amber/teal coded to P/N; self-hosted base64
faces make it the only free contender with no network dependency. It is also the dimmest artifact
here, and it drops motion accessibility entirely.

| code | sev | evidence | fix |
|---|---|---|---|
| A11Y-MOTION-01 | blocker | **Zero** `prefers-reduced-motion` blocks in either the deck or the explainer — the only contender failing this in both media. | Wrap the scene timeline in a reduced-motion branch that cuts rather than tweens. |
| A11Y-CONTRAST-03 | blocker | 91 of 205 deck strings under 4.5:1. Plate captions `PLATE 01 · THE SPLIT`, `one unit of collateral` at 10px `rgba(237,231,218,.26)` = **1.99:1**. Explainer `P + N ≡ 1.00` at 18px = 1.99:1, `SCENE 04 / 09 · RUPTURE` at 22px = 2.64:1. | Raise the annotation alpha floor from `.26` to `.62`; the restraint is costing the content. |
| CRIT-VOID-01 | major | Plate 07 (`the pathway, deleted`) leaves the bottom ~40% of the 1280×720 stage empty below the struck-through list; the composition stops mid-frame. | Either raise the plate into the void or let the deleted list occupy the full measure. |
| COPY-CASE-01 | minor | `P PROTECTED` / `N AMPLIFIED` set as letterspaced all-caps mono. Reads slowly and fights the Didone headline register. | Sentence case in the display face; keep mono for the numbers. |
| CRIT-SCALE-01 | minor | The 1920×1080 stage does not fit-scale: at 1280×720 the frame is pinned at (320,180) and the headline is cut off mid-word. Correct at 1080p, so screen-recording is safe. | Add a `transform: scale(min(vw/1920, vh/1080))` fit so the artifact previews anywhere. |

### algorithmic-art · brand — **6.4** (critic 6.0 · brand 9.0 · a11y 3.5 · copy 7.5)

Brand compliance is clean and the cover backplate — a dark seeded flow-field with a blue filament —
is genuinely lovely. The problem is that the generative layer stops being figure and becomes noise.

| code | sev | evidence | fix |
|---|---|---|---|
| CRIT-FIGURE-01 | major | Slide 11's backplate is a dense band of horizontal streaks that begins immediately under the last bullet and fills the lower half. It reads as a rendering artifact, not a field, and carries no meaning about roll cost. | Either bind the plate's parameter to the slide's number (as the cover's census strip does) or drop it to a watermark opacity. |
| CRIT-EMPTY-01 | major | Explainer scene 04 leaves the top two-thirds of the frame to an almost-invisible blob while all content sits in the bottom quarter. NOTES.md concedes "no actual pixel look-pass" was done — this is what that cost. | Do the look-pass; rebalance the scene so the rupture reads as motion, not a dark patch. |
| A11Y-MOTION-02 | blocker | **Zero** `prefers-reduced-motion` blocks in either medium — on the most motion-dependent contender in the field. | Gate the p5 draw loop on the media query and render the final frame statically. |
| A11Y-CONTRAST-04 | major | Slide numbers `01`…`14` at 12px `#3A3A3A` = 1.85:1; explainer section labels (`Medici`, `Pivot`, `The cost`) at 20px `#666` = 3.66:1. | `#666` → `#AAA` for the eyebrow row; slide numbers to `#666`. |
| A11Y-SIZE-02 | major | Explainer min 16px; 11 of 24 strings under the 28px floor, including the footer. | Rebuild the film type ramp at 1920-native sizes. |

### algorithmic-art · free — **7.0** (critic 6.5 · brand 8.0 · a11y 6.0 · copy 8.0)

Instrument Serif over JetBrains Mono, seeded backplates announced honestly (`SEED 3441`), and the
`pitch-deck-mastery` payoff chart is the strongest generative figure either mode produced. It also
posts the cleanest deck contrast of the whole free field.

| code | sev | evidence | fix |
|---|---|---|---|
| CRIT-COLLIDE-01 | major | Explainer scene 04 at 1280×720 collides twice: the header `MEDICI · COLLATERAL SPLITTING FOR TOKENIZED RWA` overruns `SCENE 4 / 9`, and the footer sits on top of the second bullet (`…sold for nothing"`). The stage max-widths without scaling the type, so it breaks at every width between 1280 and 1920. | Fit-scale the whole stage with one transform instead of constraining widths. |
| CRIT-EMPTY-02 | major | Even at a correct 1920×1080 the same scene leaves the middle ~500px to one small blue tuft and a red line. | Give the rupture the centre of the frame; it is the deck's bold moment. |
| A11Y-MOTION-03 | blocker | **Zero** `prefers-reduced-motion` blocks. | As above. |
| A11Y-CONTRAST-05 | minor | One string under 4.5:1 — the nav hint at 12px `rgba(226,236,242,.34)` = 2.65:1. Everything content-bearing clears. | Raise to `.55` or drop the hint from the printed/recorded frame. |

### impeccable · brand — **7.7** (critic 6.5 · brand 9.5 · a11y 7.0 · copy 9.0)

The best-behaved artifact here — a "notice" system of numbered sub-claims (`11.1`, `11.2`),
right-aligned mono figures against left-aligned prose, and an `AUTHORITY` citation line that is
actually legible (11px, 4.89:1). Gold only inside the shield mark, restrained accent, print CSS, no
remote assets, and just **2** strings under 4.5:1 across the whole deck (both keyboard chrome): cite
this as the brand reference.

| code | sev | evidence | fix |
|---|---|---|---|
| CRIT-DIAGRAM-01 | major | It is a beautifully set text document, not an explained mechanism. Explainer scene 04 is one descending line, a dotted "liquidation threshold" and an empty box labelled `collateral` — the weakest mechanism drawing here against the brief's third educational goal ("one diagram they could redraw"). | Borrow visual-explainer's move: draw the P/N payoff with axes at least once. |
| CRIT-VOID-02 | minor | Slide 11 ends its content at ~75% height and leaves the remainder blank; slide 01 has a similar gap between mark and headline. | Tighten the vertical rhythm or let the figure column fill it. |
| A11Y-SIZE-03 | major | Explainer min 22px; 6 of 10 strings below the 28px floor, incl. the footer at 3.66:1 and the `?scene=N` hint at 1.85:1. | Raise the film ramp; the deck ramp is already correct. |

### impeccable · free — **6.7** (critic 6.0 · brand 8.5 · a11y 7.5 · copy 5.5)

The boldest swing: deep navy, Cardo over Alegreya Sans, a folio/catchword book metaphor, gold and
coral. Where it lands (folio 7, the gilt-bar explainer scene) it is the most memorable thing here,
and its explainer clears the 28px floor with zero contrast failures. It is also the one artifact
with genuinely broken text.

| code | sev | evidence | fix |
|---|---|---|---|
| COPY-FLOW-01 | blocker | `pitch-deck-mastery` folio 5, right column, renders words out of reading order: *"'No forced liquidation' **theorem** , not a risk parameter. is a"*. The sentence is unreadable as set. | The inline drop/float treatment is reordering the run — set the emphasis as a span in normal flow. |
| CRIT-OVERLAP-01 | major | `staging` folio 1: the source line `canton-pitch-deck.md Slides 1, 3; house-brand-guide.md §0.5` sits **on top of** the second body bullet, and the footer rule cuts through both. | Reserve the footer band; push the bullet block up by its height. |
| A11Y-CONTRAST-07 | minor | One string under 4.5:1: `catchword ·` at 18px `#7E8AB6` at .55 opacity = 2.50:1. | Raise the opacity to .8. |

### visual-explainer · brand — **7.2** (critic 8.0 · brand 9.0 · a11y 3.5 · copy 7.5)

The best *teaching* in brand mode, and the artifact to reuse whichever tool wins. Slide 11 pairs a
properly drawn payoff curve — axes labelled `strike S` and `reference price x →`, the flat-to-`S/x`
transition marked, `1.00` and `0` on the ordinate — with stat cards carrying `−1.25%/yr` and
`$0.895`. Scene 04 sets collateral posted against auction proceeds as two bars and lets the red one
argue. Then it sets its sources at 1.85:1.

| code | sev | evidence | fix |
|---|---|---|---|
| A11Y-CONTRAST-08 | blocker | The provenance line runs the width of every slide at 10.5px `#3A3A3A` = **1.85:1** (`Medici Canton briefing, slides 1 · 3 · July 2026`, `RedStone with Credora, Gauntlet and Dune…`). 61 of 179 strings under 4.5:1. The brief's "every figure must trace to a source" is satisfied in the DOM and defeated on screen. | `#3A3A3A` → `#AAA` at 12px. This single token change is the highest-value fix in the review. |
| CRIT-VOID-03 | major | `pitch-deck-mastery` slide 07 leaves roughly the bottom half of the stage empty below a single quoted line; slide 11 leaves ~25%. | Rebalance the two-column grid, or promote the figure. |
| A11Y-SIZE-04 | major | Explainer min 17px (scene counter at 1.66:1); 5 of 9 strings under 28px. | Raise the film ramp. |
| BRAND-MARK-02 | minor | Same blue-and-green "M" as canvas-design/brand on the cover. | Use `#assay-mark`. |

### visual-explainer · free — **7.2** (critic 7.0 · brand 8.5 · a11y 6.5 · copy 7.0)

Bricolage Grotesque display, amber on ink-black, a faint blueprint grid, and the phrase-level amber
highlight inside the headline (`that **cannot be liquidated**`) — the sharpest typographic device
anyone used. The mini payoff chart repeats as a persistent corner reference. Not the house palette,
but a coherent tokenised system carrying the footer on all 14 slides.

| code | sev | evidence | fix |
|---|---|---|---|
| CRIT-CHROME-01 | major | Presenter chrome is baked into the frame: a button row (`←  outline  ?  →`) plus `← → move · O outline · ? help`, and it **overlaps the source citation** on both slides sampled — `canton-pitch-deck.md Slides 1, 3; house-brand-guide.md §0.5` is half-hidden on slide 1, and the slide-11 citation is cut by the same bar. Recurs on the `pitch-deck-mastery` lane. | Hide chrome under `@media print` and behind an idle timeout; move citations above the band. |
| A11Y-SIZE-05 | major | Explainer min 20px; 5 of 10 strings under the 28px floor incl. the timecode at 3.33:1. | Raise the film ramp. |
| A11Y-CONTRAST-09 | minor | Single deck offender is the nav hint at 4.14:1 — otherwise clean, and the best free-mode deck after html-ppt. | Raise the hint or hide it. |

### html-ppt · brand — **6.0** (critic 5.0 · brand 9.0 · a11y 4.5 · copy 6.5)

The template shows through. Brand compliance is fine — Plex, true black, footer, print CSS, gold in
the mark only — but the compositions are hollow: tokyo-night's primitives were re-skinned without
being re-proportioned.

| code | sev | evidence | fix |
|---|---|---|---|
| CRIT-RHYTHM-01 | major | Slide 01 leaves ~200px of dead space between the headline and the lede, which then floats at mid-slide above two pills; slide 06 clusters `$0` plus two bullets in a band between 45% and 70% height with empty thirds above and below. Reading order becomes ambiguous. | Anchor the content block to a baseline grid instead of centring it in the remaining space. |
| CRIT-CLIP-01 | major | The shield watermark bleeds off the bottom-right and is cut by the stage edge, so it reads as a stray polygon rather than a mark. | Inset it, or clip it deliberately at a rule. |
| CRIT-EMPTY-03 | major | Explainer scene 04 is a single unlabelled navy rectangle under the headline — `~$8M of collateral` is stated but the "auctioned for zero" half of the claim is never drawn. | Draw the second bar. visual-explainer/brand's scene 04 is the model. |
| A11Y-CONTRAST-10 | major | 40 strings under 4.5:1; the footer itself at 11px `#666` = 3.66:1, the nav hint at 1.55:1, and the explainer scene counter `s4 4/9` at 1.55:1. | `#666` → `#AAA` for footer and counters. |
| CRIT-OK-02 | — | The `pitch-deck-mastery` lane's slide 04 (P/N payoff table beside the annotated chart, `nowhere to put it` labelled on the threshold) is the strongest slide this contender made — the tool can carry, the staging lane just didn't ask it to. | — |

### html-ppt · free — **8.2** (critic 7.5 · brand 8.5 · a11y 9.0 · copy 8.5)

Off the brand leash this becomes the most professionally resolved deck here: a light Swiss editorial
surface, a visible column grid used as structure not decoration, Inter at heavy display weights,
crimson as the single accent, three-up stat rows, and an explainer scene 04 that is a confident
full-bleed `$8,000,000`. Also the most accessible artifact measured — **zero** strings under 4.5:1
across 176 sampled, **zero** under the 28px floor, reduced-motion in both media.

| code | sev | evidence | fix |
|---|---|---|---|
| CRIT-PLACEHOLDER-01 | major | Explainer scene 04's collateral is six unlabelled black rectangles in an irregular 2×2-ish cluster. Against a headline about $8M being auctioned for nothing, they read as unstyled placeholders rather than a quantity. | Label them, or make the count meaningful (as algorithmic-art's census bars do). |
| A11Y-SIZE-06 | minor | 74 of 176 deck strings under 18px; the floor case is 13px table labels at 700 weight, 5.33:1. Legible, but the table header ramp is one step too small for a projected deck. | 13px → 15px for `Case` / `P receives` / `N receives`. |
| COPY-OK-01 | — | The only contender that renders its provenance legibly in the body (`Source: asset-manager-pitch-deck.md Slide 14; rwa-redstone-2026.md Part 1 (a), Part 2 · figures as-of their source dates`) rather than hiding it in 10px grey. | — |
## Rankings

**brand mode**

| # | track | total | critic | brand | a11y | copy |
|---|---|---|---|---|---|---|
| 1 | canvas-design | **7.8** | 9.0 | 9.0 | 3.5 | 8.5 |
| 2 | impeccable | **7.7** | 6.5 | 9.5 | 7.0 | 9.0 |
| 3 | visual-explainer | **7.2** | 8.0 | 9.0 | 3.5 | 7.5 |
| 4 | algorithmic-art | **6.4** | 6.0 | 9.0 | 3.5 | 7.5 |
| 5 | html-ppt | **6.0** | 5.0 | 9.0 | 4.5 | 6.5 |

canvas-design and impeccable finish 0.1 apart on opposite arguments: canvas-design wins on its
plates and loses nearly two points of a11y for setting them in 1.7:1 grey; impeccable is the least
ambitious and wins by being the only brand-mode contender you can actually read. At a .3 a11y
weight, impeccable takes brand mode outright.

**free mode**

| # | track | total | critic | brand(consistency) | a11y | copy |
|---|---|---|---|---|---|---|
| 1 | html-ppt | **8.2** | 7.5 | 8.5 | 9.0 | 8.5 |
| 2 | visual-explainer | **7.2** | 7.0 | 8.5 | 6.5 | 7.0 |
| 3 | algorithmic-art | **7.0** | 6.5 | 8.0 | 6.0 | 8.0 |
| 4 | impeccable | **6.7** | 6.0 | 8.5 | 7.5 | 5.5 |
| 5 | canvas-design | **6.5** | 7.5 | 8.5 | 2.5 | 6.5 |

**brand → free delta**

| tool | brand | free | Δ |
|---|---|---|---|
| html-ppt | 6.0 | 8.2 | **+2.2** |
| algorithmic-art | 6.4 | 7.0 | +0.6 |
| visual-explainer | 7.2 | 7.2 | 0.0 |
| impeccable | 7.7 | 6.7 | **−1.0** |
| canvas-design | 7.8 | 6.5 | **−1.3** |

The delta splits the field by what each tool actually is. **html-ppt is a template engine**: under
the house brand it re-skins tokyo-night into true-black Plex and produces hollow, template-shaped
slides, but given a free hand it reaches for the layout system it was built around and makes the
most professionally resolved deck here — the brand was costing it +2.2. **canvas-design and
impeccable go the other way**: both are craft skills whose discipline *is* the constraint, so
removing it removes what made them good, and both free artifacts acquire real defects (broken text
flow, footer overlap, unscaled stages) their brand twins do not have. **visual-explainer is flat at
7.2** — the only contender indifferent to the brand, because a payoff curve is a payoff curve in any
palette.

Does `free` still read as Medici? Three of five. algorithmic-art/free (seeded blue-cyan, mono chrome)
and visual-explainer/free (amber on ink, blueprint grid) stay in the family; impeccable/free reads as
a private-bank prospectus and canvas-design/free as a mathematics monograph. html-ppt/free is
furthest away — a light surface with a crimson accent, the exact inversion of §2.1 — and it is also
the best deck, which is the uncomfortable finding.
## Blind spots in this review

I did not have the rubric this seat was meant to apply, and I substituted one — the .4/.2/.2/.2 split
is the seat brief's and the taxonomy is mine, so a reviewer running the real gstack workflow could
reasonably reorder this, and the two closest pairs (canvas-design/impeccable at 0.1,
visual-explainer's twins at 0.0) sit inside that noise. Coverage is thin: three frames per
track-mode out of 14 slides and 8–9 scenes plus one spot-check slide, roughly 20%, and I never
opened `presentation-writing` at all, so a lane-specific failure would have escaped me. My motion
evidence is synthetic — every animation seeked to 85% of its duration and paused, which shows end
states but says nothing about easing or timing against the SCRIPT.md narration, so the most
important property of the explainers is the one I inspected least and I am grading motion from stills.
The a11y numbers are the most defensible part of this review and still have a hole: background
detection walks to the nearest ancestor above 60% alpha, which is wrong wherever text sits over a
canvas backplate or gradient — exactly where algorithmic-art and canvas-design put theirs. I caught
one class of that bug mid-review (SVG text paints through `fill`, not `color`; it had
canvas-design/free showing 164 phantom failures) and fixing the one I noticed is no evidence it was
the only one. I also nearly filed three `blocker` layout findings that turned out to be my own
harness — the `free` explainers are 1920-native and correct at 1080p, and only a re-render at the
right size caught it. Finally I graded these as design, not against the corpus: I checked that
figures are *cited*, never that `$0.895`, `−1.25%/yr` or `$840M+` are *correct*, so a contender that
invented a number and set it beautifully would have scored well here.

---

# Addendum — impeccable-polish (brand, free)

Two late track-modes under the same seat: `critic .4 / brand .2 / a11y .2 / copy .2`, 0–10, same
`CRIT-`/`BRAND-`/`A11Y-`/`COPY-` codes, same `blocker`/`major`/`minor` ladder. `impeccable-polish`
is `tracks/html-ppt/{brand,free}/` copied verbatim and put through impeccable v4.0.4's `polish`
(+`animate`) refine pass — so the comparison this seat can make is unusually clean: two artifacts
differing only by a finish pass, gradable against each other on the same instruments.

**Evidence base.** `shots/impeccable-polish/` does not exist, so I rendered my own: one headless
Chrome (Playwright + installed Chrome), deck slides 1 / 6 / 11 at 1280×720, explainer scenes 4 and 6
at 1920×1080 frozen at 85% of each scene's `data-dur` through the artifacts' own `?scene=N&still=T`
(brand) / `?scene=N&at=T` (free) hooks, plus a 1280×720 explainer re-render to test stage fit —
24 frames, `staging` primary and `pitch-deck-mastery` spot-checked. **Crucially I re-ran the whole
a11y harness against the `html-ppt` baseline through the identical code path**, so the numbers below
are a measured delta rather than two methods compared. Same method as the main review: computed
styles from the live DOM, SVG resolved through `fill`/`fill-opacity`, alpha composited onto the
nearest opaque ancestor, WCAG 2.x. Floors unchanged: deck ≥18px at 1280×720, explainer ≥28px at
1920×1080.

## Measured a11y delta (the shared evidence for every A11Y finding below)

Sampled through one code path, `staging` and `pitch-deck-mastery`, active-slide states:

| artifact | strings <4.5:1 — baseline → polish | worst CR — baseline → polish | min px | slides in the a11y tree |
|---|---|---|---|---|
| brand · staging · deck | **6 → 3** | **1.55 → 3.66** | 11 → 12 | 14 → **1** |
| brand · staging · explainer | **3 → 1** | **1.55 → 3.66** | 20 → 20 | — |
| brand · pitch-deck-mastery · deck | **6 → 3** | **1.55 → 3.66** | 11 → 12 | 14 → **1** |
| brand · pitch-deck-mastery · explainer | **3 → 1** | **1.55 → 3.66** | 20 → 20 | — |
| free · staging · deck | 0 → 0 | 5.33 → 5.33 | 14 → 14 | — |
| free · staging · explainer | 0 → 0 | 5.33 → 5.33 | 24 → 24 | — |
| free · pitch-deck-mastery · deck | 1 → 1 | 1.1 → 1.1 | 14 → 14 | — |
| free · pitch-deck-mastery · explainer | 5 → 5 | (harness FP, see blind spots) | 28 → 28 | — |

Named elements, computed style, before → after:

| element | baseline | polish | CR |
|---|---|---|---|
| `.conf` — the mandated confidentiality footer | `#666666` 11px | `#8A8A8A` 12px | **3.66 → 6.10** |
| `.slide-no` — slide counter | `#666666` 12px | `#8A8A8A` 12px | **3.66 → 6.10** |
| presenter legend `← → · click · N notes · F full` | `#2E2E2E` 11px, in every frame | auto-hides at 2.4s | **1.55 → not in frame** |
| explainer scene id `s4 4/9` | `#2E2E2E` 20px | `--text-3` 20px | **1.55 → 3.66** |
| `.eyebrow` — section label, every slide | `#666666` 13px | **`#666666` 13px** | **3.66 → 3.66** |
| `.kicker` | Electric Blue 13px | Electric Blue 13px | 4.49 → 4.49 |
| `:focus-visible` ring (brand guide §9.3) | **absent** | 2px Electric Blue, 2px offset | — |
| inactive slides in the a11y tree | 13 extra slides, `opacity:0` only | `visibility:hidden` | — |

`prefers-reduced-motion` blocks: brand deck 1/1, brand explainer 2/2, free deck 1/1, free explainer
2/2 — unchanged, and the brand pass additionally extended its own block to cover the transitions it
added, which is the correct discipline when adding motion.

### impeccable-polish · brand — **6.8** (critic 5.5 · brand 9.0 · a11y 7.5 · copy 6.5)

The most improved artifact in the bake-off on this seat's own measurements, and still fourth. Every
finding I filed against html-ppt/brand that a finish pass could reach, it reached — the footer that
the brief *requires* on every slide is now legible, the presenter chrome is out of the recorded
frame, thirteen of fourteen slides left the screen-reader tree, a spacing scale exists where none
did. Every finding it could not reach is a composition, and all three are still on screen.

| code | sev | evidence | fix |
|---|---|---|---|
| CRIT-RHYTHM-02 | major | **CRIT-RHYTHM-01 is unfixed.** Slide 01 still leaves ~225px between the headline baseline (y≈185) and the lede (y≈411), which still floats above two pills; slide 06 still clusters `$0` + two bullets between 45% and 70% height with ~200px empty above and ~160px below; `pitch-deck-mastery` 06 is the same shape. The pass installed a real `--sp-1…12` 4px scale and snapped 21 declarations onto it — and then re-flowed nothing, because re-flowing is composition. A spacing system under a composition that does not use it. | Anchor the content block to a baseline grid. Unchanged from the original finding. |
| CRIT-CLIP-02 | major | **CRIT-CLIP-01 is unfixed.** The shield watermark still bleeds off the bottom-right of the cover and is still cut by the stage edge. | Inset it, or cut it. |
| CRIT-EMPTY-04 | major | **CRIT-EMPTY-03 is unfixed.** Explainer scene 4 at 85% of its duration is a headline, a thin rule, `$0` and two grey captions, with roughly 300px of void between them; the "auctioned for zero" half of the claim is still not drawn as a second bar. | Draw the second bar. |
| A11Y-CONTRAST-11 | major | The pass added `--text-chrome:#8A8A8A` (6.1:1) and routed the footer, the slide counter, the print footer and 28 SVG figure labels through it — verified. It did **not** route `.eyebrow`, which is still `rgb(102,102,102)` at 13px = **3.66:1 on every slide**, though the track's own notes list "the header eyebrow" among the elements retokenised. `.kicker` at Electric Blue measures **4.49:1** — under the floor by 0.01. | `.eyebrow` → `--text-chrome`; lift the kicker blue one step or set it at 15px/600 to qualify as large text. |
| A11Y-SIZE-07 | major | Explainer min 20px against the 28px floor, unchanged. The film ramp was never the pass's target. | Raise the film ramp. |
| A11Y-OK-01 | — | Two fixes the detector could not have found and this seat rates highest: the a11y tree (14 slides read at once → 1) and the mandated footer's contrast. Both came from looking, not scanning. | — |
| BRAND-DEVIATION-01 | minor | Two honest deviations, both recorded in the track's notes rather than buried: one colour added outside `brand.toml`'s three pinned neutrals (`#8A8A8A`, interpolated, no new hue), and §9.1's *named* `ease-in-out` replaced by `cubic-bezier(.16,1,.3,1)` at the pinned 200ms. Against that, §9.3's `:focus-visible` ring — which the incumbent simply omitted — now exists. | Net-neutral; both deviations are defensible and disclosed. |
| COPY-OK-02 | — | Copy is provably untouched: my own tags-stripped extraction over all six artifacts returns identical word counts, identical exhibit counts (15/42) and identical citation counts (8/42) against the baseline. Copy stays 6.5 — including the 8/42 citation rate that earned it. | — |

**Δ vs html-ppt/brand: +0.8 (6.0 → 6.8).** All of it in a11y (+3.0 × .2) and half a point of critic
(+0.5 × .4). Brand and copy did not move and could not.

### impeccable-polish · free — **8.2** (critic 7.5 · brand 8.5 · a11y 9.0 · copy 8.5)

**Zero delta on every one of this seat's four axes.** That is the finding, not a failure to measure:
html-ppt/free was already the most accessible artifact in the bake-off (zero strings under 4.5:1,
zero under the 28px floor, reduced-motion in both media), so the a11y column — where the brand arm
banked its entire gain — had no headroom left to give. My re-measure returns the identical failure
set on both sampled variants, string for string.

| code | sev | evidence | fix |
|---|---|---|---|
| CRIT-PLACEHOLDER-02 | major | **CRIT-PLACEHOLDER-01 is unfixed.** At 85% of explainer scene 4 the collateral is two bare black rules and a dotted red one, unlabelled, at 1280 and at 1920 alike. Against a headline about $8M auctioned for nothing they still read as unstyled placeholders. | Label them, or make the count meaningful. |
| A11Y-NULL-01 | — | The pass's real a11y work here is invisible to this seat by construction: gradient-filled text (`-webkit-text-fill-color:transparent`) went solid, which is the difference between **5.09:1** and *no measurable contrast at all* — but my harness reads `color`, so the baseline scored those strings as passing and there is no delta to book. Likewise the one genuine sub-floor failure fixed (`presentation-writing`'s `.kicker.rose`, 4.39:1 → 5.41:1) is in the lane I did not sample, then or now. | Nothing to fix; recorded so the 0.0 is not read as "the pass did nothing for a11y". |
| A11Y-HELD-01 | minor | Two contrast findings survive by explicit decision, both defensible: `.section-num` watermarks at 1.1:1 (170px, `pitch-deck-mastery`) are load-bearing identity carrying no decodable information, and darkening them would put them in competition with the headline; the two `dark-glow` detector hits are real offset shadows on *light* pages, i.e. correct depth. | Held, flagged, not changed. |
| CRIT-STAGE-01 | minor | At the brief's 1280×720 the explainer letterboxes and `MakerDAO collateral, auctioned` overprints the confidentiality footer. Correct at 1920 — the same harness artifact I nearly filed three blockers on in the main review, so I am filing it as `minor` and naming it as geometry, not a defect. | Fit-scale the stage, or pin the brief's explainer geometry at 1920. |
| COPY-OK-03 | — | Provably byte-identical: tags-stripped visible text and all three SCRIPT.md files diff to zero lines against the baseline. | — |

**Δ vs html-ppt/free: 0.0 (8.2 → 8.2).**

## Revised rankings

**brand mode (6)**

| # | track | total | critic | brand | a11y | copy |
|---|---|---|---|---|---|---|
| 1 | canvas-design | **7.8** | 9.0 | 9.0 | 3.5 | 8.5 |
| 2 | impeccable | **7.7** | 6.5 | 9.5 | 7.0 | 9.0 |
| 3 | visual-explainer | **7.2** | 8.0 | 9.0 | 3.5 | 7.5 |
| 4 | **impeccable-polish** | **6.8** | 5.5 | 9.0 | **7.5** | 6.5 |
| 5 | algorithmic-art | **6.4** | 6.0 | 9.0 | 3.5 | 7.5 |
| 6 | html-ppt | **6.0** | 5.0 | 9.0 | 4.5 | 6.5 |

impeccable-polish now posts the **second-best a11y score in brand mode**, behind only impeccable's
7.0 — beating it, in fact — and still finishes fourth, because this seat weights the critic column
at .4 and the critic column is composition. It jumps two places over artifacts with better
compositions and worse contrast, which is exactly what a .4/.2/.2/.2 jury is for.

**free mode (6)**

| # | track | total | critic | brand(consistency) | a11y | copy |
|---|---|---|---|---|---|---|
| 1 | **impeccable-polish** | **8.2** | 7.5 | 8.5 | 9.0 | 8.5 |
| 1= | html-ppt | **8.2** | 7.5 | 8.5 | 9.0 | 8.5 |
| 3 | visual-explainer | **7.2** | 7.0 | 8.5 | 6.5 | 7.0 |
| 4 | algorithmic-art | **7.0** | 6.5 | 8.0 | 6.0 | 8.0 |
| 5 | impeccable | **6.7** | 6.0 | 8.5 | 7.5 | 5.5 |
| 6 | canvas-design | **6.5** | 7.5 | 8.5 | 2.5 | 6.5 |

A genuine tie on every axis. I have written impeccable-polish first on the narrowest possible
tie-break — it is the same deck carrying twelve fewer detector findings, 40KB less dead CSS, one
fewer measured contrast failure in a lane neither of us sampled, and no bounce curve — but the
honest reading is **1=**: this seat cannot distinguish them, and should say so rather than
manufacture an order.

## brand → free delta, revised

| tool | brand | free | Δ |
|---|---|---|---|
| html-ppt | 6.0 | 8.2 | **+2.2** |
| **impeccable-polish** | **6.8** | **8.2** | **+1.4** |
| algorithmic-art | 6.4 | 7.0 | +0.6 |
| visual-explainer | 7.2 | 7.2 | 0.0 |
| impeccable | 7.7 | 6.7 | −1.0 |
| canvas-design | 7.8 | 6.5 | −1.3 |

The polish arm inherits html-ppt's brand→free gradient and flattens it, from +2.2 to +1.4 — because
the pass moved the brand artifact and could not move the free one. That is the same finding from the
other side: **the house brand was costing html-ppt 2.2 points, and a finish pass recovered about a
third of it.**

## What polish bought — under this seat

**+0.8 in brand, 0.0 in free, and all of it in the accessibility column.** The brand arm's a11y went
4.5 → 7.5, the single largest one-axis movement anywhere in this review: the mandated confidentiality
footer went from 3.66:1 to 6.10:1, the presenter legend left the frame, the scene id came off 1.55:1,
thirteen slides left the screen-reader tree, and a focus ring the brand guide pins and the incumbent
omitted now exists. On my measurements that makes it the most accessible brand-mode deck in the
field — a real, checkable result, and one the main review's own thesis predicted nobody would reach
by trying harder at composition.

And it finished fourth of six, because **every blocker and major I filed on the critic axis is still
on screen**: the dead vertical bands, the clipped shield, the undrawn second bar. Three findings,
three compositions, zero addressed. This seat's weighting says why: `critic .4` is twice `a11y .2`,
and a refinement pass is structurally forbidden from touching the thing the critic column measures.
The free arm makes the same point by returning a flat zero — the incumbent had already banked
everything a finish pass can bank, so there was nothing left to buy.

The one-line version: **polish buys the a11y column outright and cannot touch the critic column, so
it is worth about +0.8 on a deck that was failing contrast and exactly nothing on a deck that
wasn't.**

## Blind spots in this addendum

The main review's blind spots all still apply; three more are specific to this pair. **First, a
harness bug I can name but did not fix:** on the `free/pitch-deck-mastery` explainer my background
walker reports five strings at ≈1:1 including a 76px headline, on both the baseline and the polish
tree — that is the ancestor-detection hole I flagged in the main review (the page's background is a
`linear-gradient`, i.e. a `background-image`, which `backgroundColor` cannot see), and the rendered
frame shows navy-on-near-white at perfectly good contrast. I have excluded those five from every
conclusion and left them in the table so the number is not silently laundered. **Second, the free
arm's a11y delta is genuinely unmeasurable by me rather than genuinely zero:** its two real contrast
gains are gradient-filled text (which my harness scored as passing when it had no measurable
contrast at all) and a kicker in `presentation-writing` (the lane I have still never opened), so the
0.0 in that column is a limit of the instrument as much as a property of the artifact — and the
polish arm is the one contender penalised by it. **Third, and the one I would most want checked:**
I scored a delta on 24 frames out of 84 slides and 17 scenes across two modes, about 20% coverage
again, and I never watched either explainer play. The brand pass's motion work — a 200ms dissolve
where there was a hard cut, the film progress bar off per-frame layout, one arrival per scene
instead of two — is precisely what a still cannot show, so the critic column for both explainers is
a floor, and a seat grading recordings rather than screenshots would likely give the brand arm more
than the +0.5 I did.
