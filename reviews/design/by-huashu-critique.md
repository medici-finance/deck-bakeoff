# Design review — huashu critique rubric (independent judge)

Rubric: `skills/review/huashu-critique-guide.md`, applied verbatim and alone.
Six dimensions: **Concept** (0, highest weight), Philosophy Alignment, Visual Hierarchy,
Craft Quality, Functionality, Originality. Total = weighted mean
(0.30 / 0.15 / 0.15 / 0.15 / 0.15 / 0.10).

**Hard veto (rubric §0):** Concept ≤ 5 caps the total at **6.0**, no matter how good the
execution. Concept is scored by three tests: (a) can you say the idea in one sentence?
(b) cover all text and the logo — is the subject still recognisable? (c) swap the client
name — does it still work? *Yes to (c) = template = Concept ≤ 5, automatically.*

**Evidence.** No `shots/` tree existed, so I rendered my own: headless Chrome, 1280×720
(the brief's stage), deck slide 1 + slide 6, explainer `?scene=4` + `?scene=6`, for all ten
track-modes, plus 1920×1080 re-renders where a stage overflowed, plus five spot-check frames
from a second messaging variant. 45 frames read. **Caveat carried into every explainer score:
`--virtual-time-budget` does not advance these timelines, so every explainer frame is a
scene-*entry* state — fades and reveals unfinished.** Motion-as-meaning is therefore judged
from the code, not the frame. Consistency across messaging variants was additionally checked
structurally (slide-count parity + `<style>` hash) for all ten.

---

## 1. canvas-design / brand — "Conservation Plate"

| Dimension | Score | One line |
|---|---|---|
| Concept | **9** | A conserved quantity can be drawn — and so can its absence. |
| Philosophy | 9 | Registration frame, `PL. 07 · DIAGRAM · SERIES OF 14`, one figure + one sentence, colour *spent* not distributed (11 accent uses across 14 plates) — the manifesto is executed literally. |
| Hierarchy | 8 | Plate label → headline → figure → specimen-label caption row: four tiers, squint-stable. |
| Craft | 8 | Disciplined greyscale ramp, constant margins plate to plate; explainer labels collide (below). |
| Function | 8 | Dense but nothing decorative; the `SRC ·` line is real provenance, not chrome. |
| Originality | 9 | The pitch-deck-mastery plate 05 — seven ⊘ marks, "SEVEN ATTEMPTS TO PLACE A LIQUIDATION PRICE / NO SUCH PRICE EXISTS" — is the single best visual in the bake-off: it draws a *non-existence*. |

**Total 8.6 / 10 — 优秀.** Idea: *every slide is an engraved plate on which the total never
moves, and the liquidation price is the one line that is never drawn.*

Findings: (1) explainer sc.06 collides — the axis label clips `P` off `P + N ≡ 1.00`, and the
formula row overprints `REFERENCE PRICE X AT MATURITY`; fix by reserving a 32px gutter left of
the value axis and moving the formula row below the plot frame. (2) sc.04's `CLEARED FOR` label
sits under the bar field; move it outside the plot rect. (3) Cover carries two meta rows
(`PL. 01 COVER SERIES OF 14` + the logo lockup) before the headline — drop one.

## 2. canvas-design / free — "Invariant Field"

| Dimension | Score | One line |
|---|---|---|
| Concept | **8** | One horizontal line held at constant height; everything changes beneath it. |
| Philosophy | 8 | The constant edge really is on every plate; the Didone/teal-amber layer is added style, not doctrine. |
| Hierarchy | 7 | Plate 06's giant vermilion `0` out-shouts its own headline. |
| Craft | 7 | Clean type; the explainer has no scale-to-fit — at 1280×720 the 1920 stage renders offset and clipped. |
| Function | 7 | Deck is efficient; the explainer's meaning-bearing motion arrives late in each scene, so any still is 60% dead field. |
| Originality | 8 | The P/N stack under a fixed rule is content-derived, not stock. |

**Total 7.6 / 10 — 良好+.** Findings: (1) add a `transform: scale()` fit so the film survives a
1280 stage; (2) plate 06 — halve the `0`, it is competing not supporting; (3) the lower 55% of
every explainer frame is unused — raise the stage or move the figure into it.

## 3. algorithmic-art / brand — "Conserved Entry"

| Dimension | Score | One line |
|---|---|---|
| Concept | **8** | The picture *is* the quantity: a fixed population that may rearrange but never grow, with a live census proving it. |
| Philosophy | 8 | The `census · P 1.000 · N 0.000 · Σ 1.000` readout is on every slide, and flips to `conservation off` on the failure slide — a real inversion. |
| Hierarchy | 7 | Text-left / field-right holds, but on plate 06 the bright swirl outweighs the headline. |
| Craft | 7 | Type is immaculate; the field drifts into deep-blue-plus-neon-glow — rubric problem #9, the named taste floor. |
| Function | 6 | On most slides the field is ambient: delete it and only mood is lost. Explainer sc.06's dash noise is illegible as "P + N". |
| Originality | 8 | The census counter as proof-device is genuinely unexpected-but-reasonable. |

**Total 7.4 / 10 — 良好.** Findings: (1) make the field *answer* the headline on at least the
mechanism and failure slides (population literally splitting P/N), not just accompany it;
(2) drop the glow and lift line contrast — the neon-on-navy is the cliché the rubric names;
(3) sc.06 needs the two territories separated in space, not by luminance.

## 4. algorithmic-art / free — "Invariant Drift"

| Dimension | Score | One line |
|---|---|---|
| Concept | **7** | Same conservation law, but stated in the manifesto more than shown on the surface. |
| Philosophy | 6 | The philosophy promises a closed system filling the frame; the artifacts are typographic with a small ornament. |
| Hierarchy | 6 | Deck reads well; the explainer's header overprints the scene label and the footer overprints the bullets. |
| Craft | 5 | Real overlap defects at the brief's own 1280×720; partly persist at 1920. |
| Function | 6 | `SEED 3446` and the seed swatch strip survive deletion — decoration. |
| Originality | 7 | The seeded-backplate idea is sound; the execution retreated from it. |

**Total 6.3 / 10 — 良好−.** Findings: (1) fix the two-region collision (header band and footer
band need reserved height, body clamped between them); (2) either commit the generative layer
to full frame or cut it — the current 90px blob reads as an accident; (3) delete the seed
telemetry from the audience-facing surface.

## 5. impeccable / brand — "Notice / clause"

| Dimension | Score | One line |
|---|---|---|
| Concept | **5** ⚠ | A pitch typeset as a numbered legal notice with an `AUTHORITY` citation per slide — but swap the client and it stands unchanged. **Template ⇒ veto.** |
| Philosophy | 8 | The DESIGN.md pins are honoured to the token; nothing off-palette. |
| Hierarchy | 8 | Best ratio discipline in the brand field — headline ≈3× body, ruled clause rows, right-aligned figures (`~$8M` / `$0`). |
| Craft | 8 | Very clean; one defect (below). |
| Function | 8 | Every row earns its space; the numbered clause id is a genuine speaking aid. |
| Originality | 5 | Gold shield-with-checkmark watermark on the cover = stock trust cliché. |

**Raw 6.8 → capped 7.4→ **6.0 / 10** (concept veto).** Findings: (1) the cover shield is the
one element that must go — it says "security product", which is precisely the wrong frame for
"no liquidation exists"; (2) explainer sc.04 clips the box label to `ollateral`; (3) find a
motif that dies when the client name changes — the notice chrome is a container, not an idea.

## 6. impeccable / free — "The Libro Segreto"

| Dimension | Score | One line |
|---|---|---|
| Concept | **8** | Medici's own double-entry ledger: two columns that must balance, in quattrocento pigment. |
| Philosophy | 8 | Lapis/gold-leaf/vermilion/verdigris, Cardo display, folio numbering, and a real *catchword* footer — the period device for "this continues" doing actual work. |
| Hierarchy | 8 | Folio numeral → headline → rule → figure → notes; slide 06's `$0` + one sentence is exemplary restraint. |
| Craft | 6 | Slide 01's citation line **overprints** the second note line; the explainer needs a 1920 stage (offset at 1280); the gold gradient bars are heavy for the ink they carry. |
| Function | 7 | Slide 01 carries a real P/N payoff area chart — the best mechanism visual in the field — but the gold-bar imagery and the ◆ ornament are mood. |
| Originality | 8 | Fails the name-swap test in the right direction: this design cannot be resold to another client. |

**Total 7.6 / 10 — 良好+.** Findings: (1) fix the slide-01 collision (the note block and the
citation rail are both absolutely positioned into the same 40px band); (2) scale-to-fit the
film; (3) replace the gold bars with the ledger's own vocabulary — two ruled columns footing
to one total — the pigment is already doing the "wealth" work.

## 7. visual-explainer / brand

| Dimension | Score | One line |
|---|---|---|
| Concept | **4** ⚠ | None. The track's own NOTES record a theme + a slide-type routing table and no concept step. Cover the text and nothing remains but pill chips. **Veto.** |
| Philosophy | 6 | Coherent "technical editorial", but that is a default, not a chosen system. |
| Hierarchy | 8 | Genuinely good: eyebrow / headline / body / figure, generous air. |
| Craft | 8 | Tidy, few colours, accurate alignment. |
| Function | 8 | The `~$8M → $0` comparison pair is the clearest rendering of that fact anywhere in brand mode. |
| Originality | 4 | Rounded chips + faint block outlines = stock SaaS marketing. |

**Raw 6.1 → **6.0 / 10** (veto).** Findings: (1) the whole track needs a step 0 — one motif
derived from `P + N ≡ collateral` before any slide is laid out; (2) delete the decorative
outlined blocks bottom-right of the cover (rubric #8: remove it and nothing worsens);
(3) the mechanism scene enters with empty axes — draw the frame *and* the constant total on
entry so a still is never meaningless.

## 8. visual-explainer / free

| Dimension | Score | One line |
|---|---|---|
| Concept | **5** ⚠ | A recurring mini payoff-chart used as a mark is content-derived, but the surrounding industrial-terminal skin survives any client swap. **Veto.** |
| Philosophy | 6 | The grid + amber + condensed grotesk is held consistently. |
| Hierarchy | 8 | Strongest headline scale of the ten; the `$0` slab is the best single hierarchy moment in free mode. |
| Craft | 6 | The on-screen nav widget (`← outline ? →`) sits *inside* the stage and would be recorded and printed; the citation line overprints the bottom rule; slide 06 crams two bullets onto one line. |
| Function | 7 | The payoff thumbnail on the cover is a good promise; the help chrome is not the audience's business. |
| Originality | 6 | The thumbnail-as-monogram is a real idea that the rest of the system does not pick up. |

**Raw 6.2 → **6.0 / 10** (veto).** Findings: (1) hide the nav widget behind `?present=1` or
`:hover` — it is currently in every frame; (2) promote the payoff thumbnail into the actual
motif (recur it at three scales) and the concept score moves off the floor; (3) give slide 06's
two bullets separate rows.

## 9. html-ppt / brand

| Dimension | Score | One line |
|---|---|---|
| Concept | **3** ⚠ | A theme skinned with house tokens, plus the same shield-check watermark. **Veto.** |
| Philosophy | 6 | Tokens honoured; nothing beyond that. |
| Hierarchy | 5 | Cover leaves a ~200px dead band between headline and sub-line; slide 06 floats `$0` + bullets in the middle with the top third empty. |
| Craft | 6 | Alignment is fine; vertical rhythm is arbitrary — no evident spacing scale. |
| Function | 6 | Usable; the chips add nothing. |
| Originality | 3 | Template, visibly. |

**Total 4.7 / 10 — 需改进.** Findings: (1) adopt one vertical spacing scale (8/16/24/48/64) and
re-flow every slide — the dead bands are the biggest single defect; (2) cut the shield;
(3) the cover's sub-line and chips belong as one block directly under the headline.

## 10. html-ppt / free

| Dimension | Score | One line |
|---|---|---|
| Concept | **4** ⚠ | International Style, red/black/white, visible column grid. Well made and entirely transferable. **Veto.** |
| Philosophy | 7 | The Swiss look is held rigorously across the deck. |
| Hierarchy | 8 | The cleanest *read* of all ten decks: headline, rule, two-column body, `$0` slab. |
| Craft | 5 | Deck is clean, but the explainer collides at 1280×720 (headline over the logo lockup, footer over the caption), and the `presentation-writing` deck in the same track-mode is a **different theme** (dark slate) — the track has no single identity. |
| Function | 7 | Legible and printable; the grid lines are ornament. |
| Originality | 4 | Red square + neo-grotesk is the most-copied identity in existence. |

**Total 5.7 / 10 — 需改进.** Findings: (1) one theme per track-mode — the theme swap between
messaging variants is the finding, not a feature; (2) fix the explainer's header/footer
collision at the brief's stage; (3) drop the visible column rules, keep the grid as a
constraint, not a graphic.

---

## Ranking — brand mode

| # | Track-mode | Total | Note |
|---|---|---|---|
| 1 | **canvas-design / brand** | **8.6** | Only artifact in the field with an idea a viewer could restate. |
| 2 | algorithmic-art / brand | 7.4 | Idea present, execution ambient. |
| 3 | impeccable / brand | 6.0 (raw 6.8) | Best craft + hierarchy in the field; vetoed for a transferable container. |
| 4 | visual-explainer / brand | 6.0 (raw 6.1) | Clearest information design; no concept step at all. |
| 5 | html-ppt / brand | 4.7 | Template with dead vertical space. |

## Ranking — free mode

| # | Track-mode | Total | Note |
|---|---|---|---|
| 1 | **impeccable / free** | **7.6** | Ties on the number; placed first for concept specificity (a design that cannot be resold) and for carrying the only real payoff chart on a cover. |
| 2 | canvas-design / free | 7.6 | The cleaner *system*; the weaker film. |
| 3 | algorithmic-art / free | 6.3 | Freedom shrank the generative argument to an ornament. |
| 4 | visual-explainer / free | 6.0 (raw 6.2) | Best headline scale; concept floor. |
| 5 | html-ppt / free | 5.7 | Best legibility, least authorship. |

## Brand → free delta

| Tool | Brand | Free | Δ | Does `free` still read as Medici? |
|---|---|---|---|---|
| canvas-design | 8.6 | 7.6 | **−1.0** | Yes — same conserved-line system, warmer skin. The constraint made the better work. |
| algorithmic-art | 7.4 | 6.3 | **−1.1** | No — reads as any generative-art deck. Freedom cost it its strongest layer. |
| impeccable | 6.0 (6.8) | 7.6 | **+1.6 / +0.8 raw** | *More* Medici than its brand mode — the name is the concept. Largest gain in the field. |
| visual-explainer | 6.0 (6.1) | 6.0 (6.2) | **0.0** | No. Freedom changed the skin, not the thinking. |
| html-ppt | 4.7 | 5.7 | **+1.0** | No. A better template is still a template. |

The pattern: freedom helps a tool that has a *concept step* to spend it on (impeccable's
DESIGN.md), and hurts a tool whose discipline came from the constraint (canvas-design,
algorithmic-art). It does nothing at all for a tool with no concept layer — which is the
rubric's own thesis restated: execution is an amplifier.

## Blind spots in this review

Three of them, all structural. **First and largest:** every explainer frame I read is a
scene-*entry* state, because headless Chrome would not advance these timelines — so I judged
motion from source, and I have systematically under-credited exactly the dimension
algorithmic-art and canvas-design invested most in. A track whose meaning arrives at t+2s
looks empty to me and full to a viewer; treat every explainer sub-score as a floor.
**Second:** this rubric is concept-first by construction, and it punishes template competence
harder than an actual RWA buyer would. Four of ten artifacts are capped at 6.0 while scoring
7–8 on hierarchy, craft and function — an issuer's risk lead in a 10-minute meeting may well
prefer html-ppt/free's legibility to canvas-design's engraved density, and this ranking does
not price that. **Third:** I rendered at the brief's 1280×720, which penalises the three films
authored for a 1920 stage; the brief pins that geometry for the *deck*, not explicitly for the
explainer, so part of what I scored as a craft defect may be an under-specified brief. I also
read HTML/CSS as the design, so font-load failures, print-to-PDF pagination and actual scene
timing are outside what I can see, and I spot-checked only one alternate messaging variant per
track-mode (structural parity was checked for all ten; three tracks differ in CSS between
messagings, and html-ppt/free differs in *theme*).

---

# Addendum — impeccable-polish (brand, free)

Two late track-modes, scored under the same rubric, by the same judge. `impeccable-polish` is
not a design: it is `tracks/html-ppt/{brand,free}/` copied verbatim and run through impeccable
v4.0.4's `polish` (+`animate`) refine pass. Copy, slot order, headline claims and scene
durations are provably untouched (the track's NOTES verifies it; my own tags-stripped
extraction over all six artifacts agrees — identical word counts, identical exhibit counts,
identical citation counts). So the only question this rubric can ask is: **what did execution
buy, on a design whose concept layer nothing touched?**

**Evidence.** `shots/impeccable-polish/` does not exist, so I rendered my own on one headless
Chrome (Playwright, installed Chrome): deck slides 1 / 6 / 11 at 1280×720 and explainer scenes
4 and 6 at 1920×1080 frozen at 85% of each scene's `data-dur` via the artifacts' own
`?scene=N&still=T` (brand) / `?scene=N&at=T` (free) hooks — 24 frames, staging as the primary
variant and `pitch-deck-mastery` spot-checked. The same harness was re-run against the
`html-ppt` baseline so every delta below is like-for-like rather than read off two different
methods.

## 11. impeccable-polish / brand — "the same template, correctly built"

| Dimension | Score | Δ vs html-ppt/brand | One line |
|---|---|---|---|
| Concept | **3** ⚠ | 0 | Still a theme skinned with house tokens; the gold shield-with-checkmark is still on the cover, still bleeding off the bottom-right edge. **Template ⇒ veto.** |
| Philosophy | 7 | +1 | It now honours brand pins the incumbent simply omitted — §9.3's `:focus-visible` ring did not exist before — against one recorded deviation from §9.1's *named* easing curve. |
| Hierarchy | 6 | +1 | The section kicker was regrouped with the headline it labels (20px above / 8px below, was 8/16) and the 1px type step at `h3` became a real one (19→21px). The dead vertical bands that set the 5 are still there — verified, not inferred. |
| Craft | 8 | +2 | The largest gain anywhere in this addendum: a real `--sp-1…12` 4px scale with 21 declarations snapped onto it, header/footer insets equalised at 24px, `.g1` given the rule it was already relying on, six unreachable tokens removed, the 3px coloured card rails routed through the `rgba(hue,…)` idiom the file already owned. |
| Function | 7 | +1 | The presenter legend no longer prints into the frame — in the baseline `← → · click · N notes · F full` sat in **every** frame at 1.55:1, a dead state *and* a recording artifact; it now announces itself and fades at 2.4s. The chips still add nothing. |
| Originality | 3 | 0 | Refinement is not authorship. Nothing here was authored. |

**Raw 5.4 → 5.4 / 10 — 需改进** (under the 6.0 veto cap, so the cap never binds).
**Δ vs html-ppt/brand: +0.7 (4.7 → 5.4).**

Findings: (1) **the biggest defect in the baseline is untouched.** My finding on html-ppt/brand
was "adopt one vertical spacing scale and re-flow every slide — the dead bands are the biggest
single defect". Polish adopted the scale and did not re-flow: the cover still leaves ~225px
between the headline and its lede, slide 06 still floats `$0` + two bullets in a band with
~200px empty above and ~160px below, `pitch-deck-mastery` 06 the same. The scale was installed
under a composition that never used it. (2) **The contrast fix does not reach the element its
own notes claim it reached.** The footer went `#666666`/11px → `#8A8A8A`/12px (3.66:1 → 6.1:1)
and the slide counter with it — both verified by computed style. But `.eyebrow` is still
`rgb(102,102,102)` at 13px, **3.66:1, on every slide**, and the notes list "the header eyebrow"
among the elements retokenised. `.kicker` is Electric Blue at 4.49:1 — under the floor by
0.01. (3) **The shield survives.** It was finding (2) on the baseline and it is finding (3)
here: the one element that has to go says "security product" on a deck whose whole argument is
that no liquidation exists. Polish cannot remove it, because removing it is authorship.

## 12. impeccable-polish / free — "a byte-identical picture, tidier underneath"

| Dimension | Score | Δ vs html-ppt/free | One line |
|---|---|---|---|
| Concept | **4** ⚠ | 0 | International Style, red/black/white, visible column grid. Unchanged, and still entirely transferable. **Veto.** |
| Philosophy | 7 | 0 | The Swiss look is held as rigorously as before, which is to say: exactly as before. |
| Hierarchy | 8 | 0 | Copy, slots and layout are provably identical; the settled-state render is pixel-identical bar a 3px progress-bar edge. |
| Craft | 6 | +1 | 40KB of dead vendored CSS pruned, bounce easing removed, gradient *text* made solid (it had no measurable contrast at all), one 4.39:1 kicker lifted to 5.41:1, `.posn` given the padding its text was wrapping against. All real; almost none of it visible. |
| Function | 7 | 0 | The grid lines are still ornament. |
| Originality | 4 | 0 | Red square + neo-grotesk, unchanged. |

**Total 5.8 / 10 — 需改进.** **Δ vs html-ppt/free: +0.1 (5.7 → 5.8).**

Findings: (1) **the two defects that set the craft score both survive.** The explainer still
overprints `MakerDAO collateral, auctioned` on the confidentiality footer at the brief's
1280×720 stage (it resolves at 1920, so this is a stage-fit defect, as it was before), and the
`presentation-writing` deck in the same track-mode is still a **different theme** — the track
still has no single identity. That was my finding (1) on html-ppt/free and it is untouched.
(2) **The explainer's collateral figure is still six unlabelled rules.** At 85% of scene 4 the
"$8M auctioned for nothing" half of the claim is two black horizontal lines and a dotted red
one, at 1280 and at 1920 alike. A refinement pass that cannot label a figure cannot fix a
figure that is unlabelled. (3) **A +0.1 is the honest number and it is the finding.** The
free arm removed 40,026 bytes and twelve detector findings and moved this rubric by a rounding
error, because this rubric asks what a design *says*, and byte-level hygiene says nothing.

## Revised ranking — brand mode (6)

| # | Track-mode | Total | Note |
|---|---|---|---|
| 1 | **canvas-design / brand** | **8.6** | Only artifact in the field with an idea a viewer could restate. |
| 2 | algorithmic-art / brand | 7.4 | Idea present, execution ambient. |
| 3 | impeccable / brand | 6.0 (raw 6.8) | Best craft + hierarchy; vetoed for a transferable container. |
| 4 | visual-explainer / brand | 6.0 (raw 6.1) | Clearest information design; no concept step at all. |
| 5 | **impeccable-polish / brand** | **5.4** | The template, built correctly. Craft 6→8, concept 3→3. |
| 6 | html-ppt / brand | 4.7 | The same template, built carelessly. |

## Revised ranking — free mode (6)

| # | Track-mode | Total | Note |
|---|---|---|---|
| 1 | **impeccable / free** | **7.6** | A design that cannot be resold. |
| 2 | canvas-design / free | 7.6 | The cleaner system; the weaker film. |
| 3 | algorithmic-art / free | 6.3 | Freedom shrank the generative argument to an ornament. |
| 4 | visual-explainer / free | 6.0 (raw 6.2) | Best headline scale; concept floor. |
| 5 | **impeccable-polish / free** | **5.8** | 40KB lighter, 0.1 better. |
| 6 | html-ppt / free | 5.7 | Best legibility, least authorship. |

## What polish bought — under this rubric

**+0.7 in brand, +0.1 in free, and not one point of it in the two dimensions that decide the
ranking.** The gains land exactly where the rubric weights them least: Craft (+2 / +1) and
Function (+1 / 0), at 0.15 each. Concept and Originality — 0.40 of the weight between them —
did not move and structurally cannot: the rubric's concept test is *cover the text and the
logo, is the subject still recognisable*, and no refinement pass adds a subject. This is the
rubric's own §0 thesis running in a controlled experiment: **execution is an amplifier, so
amplifying a 3 gives you a louder 3.**

The finding that generalises past this bake-off is where the ceiling actually sat. The brand
arm went from the worst-built artifact in the field to a genuinely well-built one — measurably:
a spacing system where there was none, a11y contrast on the mandated footer, thirteen of
fourteen slides removed from the screen-reader tree, presenter chrome out of the recorded frame
— and finished **fifth of six**, ahead of nothing but the file it was copied from. Every
finding I filed against html-ppt/brand that polish could reach, it reached; every finding it
could not reach was the one that mattered. The refinement arm's own notes name the boundary
honestly (`craft-floor` bans the eyebrow absolutely, `polish.md` forbids touching copy, "a
from-scratch impeccable contender would not have shipped these; this arm cannot remove them"),
and the boundary is the verdict: **the ceiling on a polish pass is the concept it inherits.**

## Blind spots in this addendum

Four. **First:** I am scoring a delta between two artifacts whose difference is largely
invisible in a still, on a rubric that reads stills — the free arm's single biggest change
(40KB of unreachable CSS) is by construction unscoreable here, and I have credited it only
through Craft, which may under-price it for anyone who has to maintain the file. **Second:**
my frames are again scene-*entry*-plus-freeze rather than live playback; the brand arm's motion
work (200ms dissolve on scene change, per-frame layout cost removed from the film progress bar,
one arrival per scene instead of two) is the kind of change a viewer feels and a still cannot
show, so the Function score for both explainers is a floor. **Third:** I sampled staging plus
one spot-check per mode, as before; the free arm's one genuine measured contrast fix lives in
`presentation-writing`, the lane I did not open, so I have taken it on the notes' word and
credited it without verifying it. **Fourth, and structural:** this is the only pair in the
bake-off where I knew the answer before scoring — the arm is *defined* as "the baseline, plus
finish" — and a rubric that vetoes on concept was always going to return "the concept did not
move". A reader should treat the +0.7 / +0.1 as the honest measurement it is and the framing
around it as the least independent judgement in this file.
