---
name: The Libro Segreto
description: A quattrocento double-entry ledger, rendered in saturated pigment, for Medici's collateral-splitting pitch surfaces.
colors:
  lapis-deep: "#080F2A"
  lapis-field: "#0B1436"
  lapis-raised: "#132049"
  lapis-lifted: "#1B2B5E"
  page-head: "#111D4A"
  page-mid: "#0D1739"
  page-foot: "#0A1230"
  rule-lead: "#2C3E7C"
  rule-soft: "#1B2A58"
  ruling-overlay: "rgba(44,62,124,.34)"
  scrubber-track: "rgba(44,62,124,.55)"
  scene-tick: "rgba(11,20,54,.85)"
  vignette-deck: "rgba(4,8,24,.55)"
  vignette-film: "rgba(3,6,20,.62)"
  paper-print: "#fff"
  ink-vellum: "#F2ECDC"
  ink-muted: "#AEB9DA"
  ink-marginal: "#7E8AB6"
  ink-struck: "#55618E"
  gold-leaf: "#E8B44A"
  gold-burnish: "#F7DC90"
  gold-shadow: "#B8862C"
  gold-edge: "#C08F2E"
  vermilion: "#FF6A4D"
  minium: "#DE3F24"
  minium-deep: "#B92E19"
  verdigris: "#4FB89E"
  verdigris-deep: "#2E7D6B"
typography:
  display-cover:
    fontFamily: "Cardo, Georgia, 'Times New Roman', serif"
    fontSize: "57px"
    fontWeight: 700
    lineHeight: 1.13
    letterSpacing: "-0.02em"
  display-turn:
    fontFamily: "Cardo, Georgia, 'Times New Roman', serif"
    fontSize: "54px"
    fontWeight: 700
    lineHeight: 1.13
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Cardo, Georgia, 'Times New Roman', serif"
    fontSize: "43px"
    fontWeight: 700
    lineHeight: 1.13
    letterSpacing: "-0.012em"
  headline-with-figure:
    fontFamily: "Cardo, Georgia, 'Times New Roman', serif"
    fontSize: "37px"
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: "-0.012em"
  title-quote:
    fontFamily: "Cardo, Georgia, 'Times New Roman', serif"
    fontSize: "33px"
    fontWeight: 400
    lineHeight: 1.32
  title-case:
    fontFamily: "Cardo, Georgia, 'Times New Roman', serif"
    fontSize: "27px"
    fontWeight: 400
    lineHeight: 1.34
  seal:
    fontFamily: "Cardo, Georgia, 'Times New Roman', serif"
    fontSize: "76px"
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: "-0.01em"
  rupture-figure:
    fontFamily: "Cardo, Georgia, 'Times New Roman', serif"
    fontSize: "92px"
    fontWeight: 700
    lineHeight: 0.9
    letterSpacing: "-0.04em"
  body:
    fontFamily: "'Alegreya Sans', Optima, 'Segoe UI', system-ui, sans-serif"
    fontSize: "19px"
    fontWeight: 400
    lineHeight: 1.42
  body-apparatus:
    fontFamily: "Cardo, Georgia, 'Times New Roman', serif"
    fontSize: "18px"
    fontWeight: 400
    lineHeight: 1.38
  numeral:
    fontFamily: "Cardo, Georgia, 'Times New Roman', serif"
    fontSize: "20px"
    fontWeight: 700
    lineHeight: 1.4
  plate-axis:
    fontFamily: "'Alegreya Sans', Optima, 'Segoe UI', system-ui, sans-serif"
    fontSize: "22px"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "0.03em"
  plate-callout:
    fontFamily: "'Alegreya Sans', Optima, 'Segoe UI', system-ui, sans-serif"
    fontSize: "24px"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "0.03em"
  label:
    fontFamily: "'Alegreya Sans', Optima, 'Segoe UI', system-ui, sans-serif"
    fontSize: "14px"
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: "0.14em"
  label-folio:
    fontFamily: "'Alegreya Sans', Optima, 'Segoe UI', system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: "0.06em"
  film-display:
    fontFamily: "Cardo, Georgia, 'Times New Roman', serif"
    fontSize: "72px"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.018em"
  film-display-stack:
    fontFamily: "Cardo, Georgia, 'Times New Roman', serif"
    fontSize: "62px"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.018em"
  film-body:
    fontFamily: "'Alegreya Sans', Optima, 'Segoe UI', system-ui, sans-serif"
    fontSize: "31px"
    fontWeight: 400
    lineHeight: 1.45
  film-figure-label:
    fontFamily: "'Alegreya Sans', Optima, 'Segoe UI', system-ui, sans-serif"
    fontSize: "30px"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "0.03em"
  film-figure-mark:
    fontFamily: "Cardo, Georgia, 'Times New Roman', serif"
    fontSize: "56px"
    fontWeight: 700
    lineHeight: 1.0
  film-label:
    fontFamily: "'Alegreya Sans', Optima, 'Segoe UI', system-ui, sans-serif"
    fontSize: "28px"
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: "0.1em"
  film-rupture-figure:
    fontFamily: "Cardo, Georgia, 'Times New Roman', serif"
    fontSize: "132px"
    fontWeight: 700
    lineHeight: 0.9
    letterSpacing: "-0.04em"
rounded:
  hairline: "2px"
  plate: "3px"
spacing:
  ruling: "28px"
  row: "11px"
  group: "18px"
  block: "26px"
  gutter: "36px"
  page-x: "74px"
components:
  entry:
    backgroundColor: "transparent"
    textColor: "{colors.ink-muted}"
    typography: "{typography.body}"
    padding: "11px 0"
  entry-key:
    textColor: "{colors.ink-vellum}"
    typography: "{typography.body}"
    padding: "11px 0"
  balance-head:
    textColor: "{colors.gold-leaf}"
    typography: "{typography.label}"
    padding: "12px 0"
  balance-row-concede:
    textColor: "{colors.vermilion}"
    typography: "{typography.body}"
    padding: "12px 0"
  verbatim:
    textColor: "{colors.ink-vellum}"
    typography: "{typography.title-quote}"
    padding: "0 0 0 56px"
  citation:
    textColor: "{colors.ink-marginal}"
    typography: "{typography.body-apparatus}"
    padding: "14px 0 8px"
  folio-versal:
    textColor: "{colors.gold-leaf}"
    typography: "{typography.display-turn}"
---

# Design System: The Libro Segreto

## Overview

**Creative North Star: "The Libro Segreto"**

The Medici bank's contribution to finance was not a product; it was double-entry bookkeeping — a
page on which every entry has two sides, and which is only correct when they balance. Medici's
product is the same shape: `P + N ≡ collateral`, two claims that must foot. So the surfaces are
built as a codex page, not as a slide: a ruled field, a ruled margin carrying an illuminated
folio, and a catchword at the foot naming the next page.

The rendition is deliberately not the parchment one. A quattrocento manuscript's expensive
materials were pigments, not paper — levigated lapis lazuli, gold leaf, vermilion and minium,
verdigris — and this system is built from those, on a saturated lapis ground with the lettering as
the light laid over it. That inverts a real manuscript, which is correct here: these surfaces are
projected in a room and forwarded to screens, and a dark saturated field carries a two-hour meeting
better than a cream one carries a projector.

Two anti-references are held explicitly, both named before any code was written: the dark-neon
protocol deck with its glass panels and glowing edges, and the cream-paper institutional-finance
broadsheet with its high-contrast serif and hairline rules. The first is what this category ships;
the second is its predictable opposite.

**Key Characteristics:**
- Pigment ground, light lettering; never a light ground.
- Every figure of P and N is topped by one continuous rule at 1.00. The invariant is drawn.
- Colour is spent like a rubricator's ink: rarely, and always on the thing that matters.
- Ruled hairlines instead of cards, boxes, or shadows. There are no shadows in this system.
- Every number carries its source on the apparatus line of the same surface.

## Colors

Four pigments on one ground: the ground is a mineral blue, and gold, vermilion and verdigris are
the three inks laid on it, each with exactly one job.

### Primary
- **Lapis Field** (`#0B1436`, laid as `linear-gradient(177deg,#111D4A,#0D1739 42%,#0A1230)`): the
  page itself. Denser at the foot than the head, the way levigated pigment settles. This is a
  Drenched colour strategy — the ground owns the whole surface, not an accent on a neutral.
- **Gold Leaf** (`#E8B44A`, burnished `#F7DC90`, shadowed `#B8862C`): the **P** leg, and any total
  that holds. Rendered as a three-stop leaf gradient on shapes, never on type.

### Secondary
- **Vermilion** (`#FF6A4D`, deep `#DE3F24`): the **N** leg, the liquidation threshold, and every
  cost the surface volunteers. The rubricator's ink — it marks what must be noticed, including the
  bad news.

### Tertiary
- **Verdigris** (`#4FB89E`, deep `#2E7D6B`): the sum that holds. It draws **the balance rule
  itself** — the continuous 3–4px line across the top of every stacked payoff at 1.00 — plus the
  tether between P and N, the price sweep that proves the invariant, the footing's sum chip, and
  the "removed" row in a risk ledger. It never appears on a claim. ~7.4:1 on the lapis field.

### Neutral
- **Ink Vellum** (`#F2ECDC`): all display and emphasized text. ~15:1 on the lapis field.
- **Ink Muted** (`#AEB9DA`): body and ledger rows. ~8.7:1.
- **Ink Marginal** (`#7E8AB6`): folio, footer, catchword, source citations. ~5.2:1.
- **Lead Rule** (`#2C3E7C`) and **Soft Rule** (`#1B2A58`): the scribe's ruling; every structural
  line in the system is one of these two at 1px.

### Named Rules

**The Rubricator's Rule.** Each of the three inks has exactly one referent and never borrows
another's. Gold is P and totals. Vermilion is N, the threshold, and the cost. Verdigris is the sum
that holds. A surface that needs a fourth meaning gets a rule, not a colour.

**The Volunteered-Cost Rule.** Vermilion is used on the surface's own bad news — the conceded
comparison row, the drift figure, the "not real" ledger entries — at the same weight it is used on
the argument. Toning down the concession would break the audience's trust before the mechanism
does.

## Typography

**Display Font:** Cardo (with Georgia, 'Times New Roman', serif)
**Body / Label Font:** Alegreya Sans (with Optima, 'Segoe UI', system-ui, sans-serif)

**Character:** Cardo is a Renaissance revival with real quattrocento texture — asymmetric serifs,
a low-contrast humanist axis, old-style colour on the page. Alegreya Sans is its clerk: a
book-companion humanist sans with lining tabular figures, used for everything a scribe would have
written in a smaller hand — ledger rows, column headings, figures, folio, source citations. The
pairing is one voice at two registers, not a display face bolted to a UI face.

### Hierarchy
- **Display** (Cardo 700, 72px explainer / 57px deck cover, 1.10–1.13, −0.02em): the scene or cover
  claim. One per surface.
- **Headline** (Cardo 700, 43px, 1.13, −0.012em; 37px on mechanism and proof surfaces where a
  figure must share the page): every other slot claim. Max 24.5ch, `text-wrap: balance`.
- **Title** (Cardo 400/700, 33px italic for verbatim quotations, 27px roman for the maturity cases,
  76px for the closing `P + N ≡ collateral` seal).
- **Body** (Alegreya Sans 400, 19px deck / 31px explainer, 1.42–1.45): ledger entries, balance rows,
  scene sub-lines. Never below 18px on a 1280×720 stage or 28px on a 1920×1080 one, and that floor
  covers provenance too: citations, attributions and the as-of line are body, not chrome.
- **Label** (Alegreya Sans 700, 14px deck / 28px explainer, 0.1–0.16em, uppercase): column
  headings, case headings, footer, folio suffix, navigation hint. 16px roman for the folio itself.
  These are tracked uppercase chrome, never reading text — the 18px floor above governs everything
  a reader reads, and the label tier is not an exemption from it, it is a different thing.
- **Figure label** (Alegreya Sans, 30 viewBox units in the film, 22–24 in the deck plate): SVG
  labels render scaled. Measured worst cases: the film's narrowest layout puts them at **29.0px**
  and the deck's tallest plate puts the axis labels at **19.0px** — both clear their stage's floor.
  Any new figure gets checked at its own `viewBox`-to-column ratio, never assumed.

### Named Rules

**The Clerk's-Hand Rule.** Figures, ledger rows and headings are set in the sans with tabular
numerals; argument and quotation are set in the serif. A number never appears in the display face
except in the two places the system treats as inscription — the closing seal and the rupture
figure.

**The Measure Rule.** Ledger entries and ledger rows are capped at 75ch and balance columns at
40ch, even where the page is wider. These surfaces are built to be read without a narrator.

**The No-Costume Rule.** There is no monospace anywhere in this system. Nothing here is code, and
monospace standing in for "technical" is the tell the system was built to avoid.

## Layout

Both surfaces are fixed stages, scaled to the viewport by a single JS transform: the deck at
1280×720, the explainer at 1920×1080. Nothing reflows; the composition is the composition.

**The deck page** is a two-column codex spread: a 96px ruled margin separated by a 1px `rule-soft`
hairline, then a 36px gutter, then the text block. The margin carries only the illuminated folio —
a 54px gold Cardo numeral over `of 14` in label type — and no editorial label of any kind. Page
padding is 46px / 74px / 22px. Beneath the page sits the codex apparatus: an 18px italic apparatus
line with the source citation left and the catchword right, a 1px `rule-lead` footrule, then the
footer row carrying `Medici — Proprietary & Confidential`, a gold lozenge, and the folio.

**The explainer scene** is a single 92px / 128px / 104px field with four composition modes chosen
by the scene's motion role, so consecutive scenes never repeat a frame: `center` (still scenes),
`fig-right` and `fig-left` (a claim beside its figure), and `stack` (claim over a full-width
figure). A `duo` grid at .42fr / .58fr carries the scenes that need two figures at once.

**Rhythm.** The page's ruling pitch is 28px and every vertical measure is a multiple or half-step
of it: 11px row padding, 18px group gap, 26px block gap, 36px column gutter. More space above a
heading than below it. Ledger rows separate by a hairline, never by a gap.

## Elevation & Depth

**This system has no shadows.** Not one `box-shadow` exists in either stylesheet. A manuscript page
has no cast light and nothing floats above it; depth here is entirely tonal and material:

- four steps of lapis (`#080F2A` → `#1B2B5E`) for ground, page, panel and lifted surface;
- a repeating 28px `rgba(44,62,124,.34)` ruling overlay that reads as the scribe's pricking and
  ruling and sets the page's texture;
- one non-chromatic vignette (`radial-gradient` to `rgba(4,8,24,.55)`) that seats the page in the
  frame, used once per surface at the stage level;
- the gold and minium leaf gradients, which carry their own internal light and are the only thing
  in the system that reads as a raised material.

### Named Rules

**The Flat-Page Rule.** Nothing in this system lifts. A surface that needs to separate from
another does it with a hairline rule or one step of lapis, never with a shadow, a glow, or a blur.

## Shapes

The form language is **the rule, not the box**. Structure is carried by 1px hairlines in
`rule-lead` and `rule-soft`: the margin divider, the table spine, the row separators, the footrule.
There are no cards. There are no bordered containers except the two SVG figures that need an
enclosure (the redemption-window gate and the privacy scope), and both are drawn as open strokes.

Radius is effectively absent: 3px on the gold and vermilion plates that stand for a position or a
claim, 2px on the small chips. Everything else is square. Dashed strokes carry exactly three
meanings and no others, and the build uses exactly three patterns: **vermilion `7 8` is a
threshold** (a liquidation line, a marked price, the refused line), **verdigris `4 6` is a tether
or a scope** (the sum that holds, the privacy boundary), and **`3 5` in Ink Muted is an axis
guide** (the strike marker). A fourth pattern needs a fourth meaning first. The single long
`stroke-dasharray="1100"` in the film is not a dash pattern — it is a path length used to draw the
price track.

## Components

### Ledger entry (the support layer)
- **Character:** a ruled account line, not a bullet.
- **Shape:** 22px marker column + content, 11px vertical padding, 1px `rule-soft` bottom rule; the
  set opens with a `rule-soft` top rule.
- **Marker:** an 11×1.5px lead-coloured dash. The one *key* entry per surface upgrades its dash to
  2px gold. There are no bullet glyphs.
- **Emphasis:** `<b>` lifts to Ink Vellum at weight 500; figures take the serif in gold; negative
  figures take the serif in vermilion.

### Balance table (every comparison slot)
- **Character:** two facing columns of an account that must foot.
- **Shape:** `1fr / 1px / 1fr` with a `rule-soft` spine, `rule-lead` top rule, 26px column padding,
  64px minimum row height.
- **Color assignment:** the incumbent column heads in Ink Marginal, Medici's column head in gold;
  incumbent rows in Ink Muted, Medici rows in Ink Vellum.
- **Concession row:** set in vermilion, in the same size and weight as every other row.

### Payoff plate (the signature component)
- **Character:** the product, drawn. Stacked P (gold leaf) and N (minium) against reference price,
  with the strike marked, topped by one continuous 3–4px **verdigris** rule at 1.00.
- **Placement:** it opens the deck. Folio 1 carries the drawn balance beneath the claim, never a
  typeset identity. The 76px `P + N ≡ collateral` seal is a *closing* device only, and only where
  the closing slot's own claim asks for it: one of the three decks uses it (the one whose final
  claim repeats the cover sentence verbatim). The other two close on the payoff plate with the
  refused threshold, which is the stronger ending where the claim is about an absence.
- **Geometry:** `P = min(1, S/x)`, `N = 1 − P`, plotted over `x ∈ [0.45S, 2.6S]` at 240 steps; the
  stacked top edge is flat by construction.
- **Footing:** a three-row legend set as a ledger footing rather than a chart key — P's row, N's
  row, and the invariant's row led by a 3px verdigris rule glyph rather than a colour chip.
- **Threshold variant:** a vermilion `7 8` dashed vertical with the label *no liquidation line fits
  here*. It is the only element in the system permitted to fail to land.

### Verbatim (external quotation)
- **Style:** Cardo italic at 33px, inset 56px behind a **drawn paraph mark** — a 34×38 SVG in
  vermilion and minium at the world's own 2.5px stroke. Not a coloured side stripe; the floor
  refuses those and the world has its own mark for exactly this job. Attribution below at 18px.
- **Rule:** used only for words the system did not write. Medici's own claims are never set this
  way.

### Ruled margin and the illuminated folio
- **Style:** a 96px ruled margin closed by a 1px `rule-soft` hairline, carrying only the folio: the
  page number as a 54px gold-leaf Cardo numeral with `of 14` beneath it in 14px label type. It is
  the slide counter and the page's one illuminated element.
- **Rule:** the margin carries no editorial label. A short evocative phrase set in small tracked
  uppercase beside a heading is a kicker, which this system does not have and cannot earn back.

### Apparatus line (provenance + catchword)
- **Style:** a full-width row above the footrule: the source citation left in 18px italic Cardo,
  the catchword right in 18px italic Cardo, both in Ink Marginal. No `source` label precedes the
  citation — a citation reads as a citation, and that label was the last sub-floor string on the
  page.
- **Behavior:** present on every surface without exception, including the cover. No figure appears
  on a page whose apparatus line does not cite it.

### Catchword
- **Style:** 18px italic Cardo, right-aligned on the apparatus line, prefixed with a faint `catchword ·`
  and carrying the opening words of the next page. The final page reads
  `— explicit · here ends the account —`.
- **Purpose:** the codex's own binding aid, working here as a presenter's next-slide cue.

### Navigation
- **Deck:** keyboard-first — `←`/`→`/`PageUp`/`PageDown`/`Space`, `Home`/`End`, click left 22% to go
  back and anywhere else to advance, hash-synced. One quiet hint in Ink Marginal at the foot that
  fades out after 5.2s. `window.__deck` exposes `{slide, total, go(n)}`.
- **Explainer:** a 4px `rule-lead` bar at the stage foot with a gold-burnish fill scaled by
  `transform: scaleX`, and 1px lapis tick marks at every scene boundary. `window.__player` exposes
  `{scene, t, total, seek(n), playing}`.

## Motion

Motion in this system is authored per *role*, and the roles are a fixed vocabulary: `hold`,
`accumulate`, `strain`, `rupture`, `assemble`, `arrest`, `divest`, `cadence`. Every delay and
duration is `calc(var(--d) * k)` where `--d` is the scene's own narration budget in seconds, so
choreography scales with the script rather than being fitted to it. Easing is
`cubic-bezier(.16,1,.3,1)` for arrivals and a steeper curve for collapses; there is no bounce or
elastic curve anywhere.

### Named Rules

**The Footing Rule.** In any figure that stacks P and N, the verdigris balance rule at 1.00 is the
**last** element to arrive and it draws across rather than fading in. Nothing may arrive after it.

**The One-Entrance Rule.** The deck has exactly one authored motion: the plate inking itself and
the balance rule footing across. Slides do not fade or rise on arrival — an identical entrance on
every surface is not a motion thesis, it is a habit.

**The Quiet-Payment Rule.** A peak is paid for by the stillness on either side of it. A scene
declared quiet carries no figure motion at all — one fade, then nothing — and a scene declared
`divest` may only *remove* things.

**The Nothing-Leaves Rule.** In an `assemble` scene, every element that arrives stays on screen to
the end of the scene. The invariant is only legible as an accumulation that never breaks.

## Do's and Don'ts

### Do:
- **Do** draw the invariant. Any surface asserting `P + N ≡ collateral` should show the flat top
  edge at 1.00 rather than write the identity in prose.
- **Do** put every figure's source on the deck's apparatus line. The deck is the artifact that gets
  forwarded and read without a narrator, so its provenance is audience-facing content, not build
  metadata — that is the line between this rule and the one below it. The **film** carries no
  filenames at all: its per-scene sources live in `SCRIPT.md`, where the auditor reads them and the
  viewer does not. This audience
  distrusts an unattributed number more than a small one.
- **Do** set the concession at full weight — vermilion, same size, same position in the ledger as
  everything else.
- **Do** keep the ground saturated. If a new surface needs more air, add rule spacing, not a
  lighter field.
- **Do** end each page by naming the next.

### Don't:
- **Don't** introduce a shadow, a glass panel, a blur, or a glow. This page has no cast light.
- **Don't** let gold, vermilion or verdigris drift off its single referent.
- **Don't** use monospace, gradient text, a kicker or eyebrow above a heading, a same-size card
  grid as page structure, a coloured `border-left` above 1px, or a unicode glyph where an icon
  belongs. None of these appear in the build and none is earned by this world.
- **Don't** render the codex in parchment. Cream ground, ivory, lamplight and a high-contrast
  serif on white are the softest rendition of this world and the one every model reaches for; the
  saturated pigments are the point.
- **Don't** animate a quiet scene, and don't let anything arrive after the balance rule.
- **Don't** print build-time *directives* on a shipped surface. Beat names, slot functions, motion
  roles, energy numbers and peak flags are instructions to the builder and mean nothing to the
  prospect. A source citation is not one of these: it is the evidence the claim above it rests on,
  and this audience distrusts an unattributed number more than a small one. Directives out,
  provenance in — and on the film, provenance goes to SCRIPT.md.
- **Don't** open with the closing seal. The first surface draws the balance; the last one states it.

---

*Recorded at finish from the built world (six artifacts, three decks and three explainers), per
`reference/degraded/documenter.md` — the shipped `impeccable-documenter` subagent type does not
exist in this harness, so the pass ran inline from the degraded reference. Ground truth is the
shipped code, not the plan.*

*Not canonized: the `aphoristic-cadence` and `em-dash-overuse` findings the detector raised against
copy that arrives verbatim from the messaging contracts. Those are properties of contract-locked
text the design layer may not rewrite, and they are recorded here as a defect the build carries,
never as a house rule for a future surface to inherit.*
