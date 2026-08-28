# Design

<!-- impeccable:design-schema 1 -->

Written at finish, from the six built artifacts, not before them. Mode: **Persuade**
(the visitor decides whether to grant a conversation; the artifact is the product).

---

## 0. Authority order

1. **The house brand guide is pinned and non-negotiable.** `source/brand/house-brand-guide.md`
   §2 colour, §3 type, §9 motion, §10 surfaces, plus the machine contract
   `skills/deck-author/brands/medici/brand.toml`. Impeccable's own rule — *"The brief wins.
   Honor pinned aesthetics, eras, materials, fonts, and palettes even when they conflict with
   a saturated-pattern warning"* — makes this section outrank every default and every
   craft-floor preference below. Section 6 lists each place the two collided and records that
   the brand won.
2. **The three messaging contracts are consumed verbatim.** Slot order fixed, headline claims
   fixed, no facts added. Line-breaking is the only licence taken.
3. Everything else in this file is the built world, recorded so the next surface can match it.

---

## 1. The pins, transcribed

These are copied from the brand guide and the brand contract. They are constraints, not
choices, and nothing below may override them.

### Colour (§2.1, §2.3, §2.4, §2.6 · `[palette]`)

| Token | Hex | Role as built |
|---|---|---|
| True Black | `#000000` | The canvas. Every deck slide and every explainer frame. |
| Surface | `#0A0A0A` | Object fills — the collateral rect, the code surface. |
| Hairline | `#1A1A1A` | Clause rules, table rules, the column divider. |
| Hairline 2 | `#252525` | The masthead rule, section heads, plot frame. |
| White | `#FFFFFF` | Headings, operative sentences, figure values. |
| Text | `#AAAAAA` | Clause body, comparison cells, sub-lines. |
| Meta | `#8A8A8A` | Subject labels, authority values, axis labels, dimension lines. |
| Dim | `#7A7A7A` | Clause numbers, folios, struck provisions, the refused threshold. |
| Muted | `#666666` | The confidentiality footer only (§3.4 rule 6, legal register). |
| Electric Blue | `#3366FF` | The one frequent accent. Notice seal, P leg, progress rule. |
| Blue Light | `#5C85FF` | The P label on the payoff plot. |
| Green | `#00CC66` | N leg — §2.1 pins this green as "N Token representation". Functional only. |
| Gold | `#D4A843` | Inside the mark, and nowhere else (`[marks] usage`). |

**Accent budget: ≤2 visible Electric Blue uses per slide** (`[rules] accent_budget = 2`).
As built, every slide spends exactly one on the masthead seal and at most one more — the
blockquote rule on `staging` notice 05, or the P encoding of the payoff figure, never both.
The house linter counts `.kicker`/`.accent`-classed elements; blue-carrying elements are
therefore classed `accent` honestly rather than renamed to duck the count.

**§2.6 ratios**: black and surface tones 70–80%, white 15–20%, blue 3–5%, functional colours
1–2%. As built the figures are hairline drawings on black, which lands inside the band.

### Type (§3.1–§3.4 · `[type]`)

- **IBM Plex Sans** does all text; **IBM Plex Mono** does data, references and labels.
  Hierarchy is weight and size, never a serif/sans split.
- **Self-hosted `woff2`, never a CDN.** Four files are copied beside every artifact
  (`fonts/`), with `NOTICE.md` (SIL OFL 1.1) alongside. `ipx-sans.woff2` is declared
  `font-weight: 100 700` because it is a **variable** font; the two mono files are declared
  400 and 500 because they are **static** instances. Getting that backwards produces
  browser-synthesised weight that looks subtly wrong in a way nobody can name — the trap
  named in `fonts/NOTICE.md`.
- Headings sentence case, SemiBold, never all-caps display. Body 400; 500 for emphasis.
- Mono is never italicised (§3.4 rule 4). The one italic in the system — the *"No such
  provision"* line of a vacated clause — is IBM Plex Sans italic.
- `font-variant-numeric: tabular-nums` on every mono figure and folio.

### Deck typographic spec (§10.3)

Headlines 36–48px, body 18–24px, data 16–20px, one gradient maximum per deck — the system
uses **zero** gradients, per `[rules] gradients = false`. As built:

| Role | Deck (1280×720) | Explainer (1920×1080) |
|---|---|---|
| Operative sentence | `h1` 52px / `h2` 33px / `h2.big` 44px, 600 | 60px, 600 |
| Clause body | 18px (17.5px on the dense `tight` variant), 400 | — |
| Sub-line | — | 32px, 400 |
| Schedule value | mono 23px, 500 | mono 26–40px, 500 |
| Masthead / subject | mono 12px, 500, 0.13em | mono 24px, 500, 0.16em |
| Authority line | mono 12px | — |
| Confidentiality footer | 11px `#666666` (pinned) | 28px `#666666` |

### Motion (§9)

Minimal, functional, fast. 150ms ease-out for hover, 200ms ease-in-out for enter/exit.
**No springs, no bounce, no overshoot. No page transitions.** `prefers-reduced-motion:
reduce` disables everything. As built: the deck's slide change is a 200ms `ease-in-out`
opacity crossfade and nothing else; the explainer's easing is
`cubic-bezier(.22,.61,.36,1)` — a pure deceleration curve with no overshoot — and scene
durations come from the contracts' `vo_seconds`, not from taste. See §5 for the one place
the brand's interface-motion table had to be read as a spirit rather than a literal.

### Surface class (§10.6)

External artifact. Dark surface by convention; the **footer is the authoritative class
marker** and appears on every slide and every frame:
`Medici — Proprietary & Confidential`, set legal-disclaimer style, deprioritized but never
hidden. Declared once in `<meta name="deck-footer">` and painted by `.slide::after` so it
survives print and PDF.

### Marks (`[marks]`)

The plate-stripped inline `<symbol>` library only: `#assay-mark` (gold shield-tick, cover
and closing at 58px) and `#oct-line` (stroke-only watermark at `opacity: .05`, cover and
closing only). The raw brand SVGs carry a baked near-black plate and never go on a slide.

---

## 2. The direction

**The clearing-house circular.** Seed key `549e8b77`, direction 6 of 7 on the grounded list,
assigned by `concept-seed.mjs --scope direction --mode persuade`.

The pinned brand fixes the *world* — black, blue, Plex, footer. It does not fix the
**organizing device**, and that is what the roll decided. Seven grounded directions were
derived from this audience's own graphic traditions (they read documents, not terminals),
ordered by resonance:

1. the payoff diagram as the deck's spine
2. the institutional term sheet / offering memorandum page
3. the settlement ledger / trade blotter
4. the prospectus risk-factor register
5. the engineering general-arrangement sheet
6. **the clearing-house circular / exchange notice** ← assigned
7. the market-data terminal panel

The rut, named and excluded before the roll: the dark VC pitch deck (centred headline, three
stat cards, a logo row) and its predictable opposite, the all-type manifesto with one giant
number per slide.

**Why the assignment carries the product's truth.** A circular is how the most consequential
statements in finance are actually published: numbered, dated, and signed by the authority
that issued them. This piece's central claim — *no liquidation price exists* — is a statement
about the rules of an instrument, and this audience's stated distrust is *"numbers whose
provenance is not named"*. The form answers the distrust structurally instead of rhetorically:
provenance is not a footnote, it is a fixed element of every slide.

---

## 3. The system as built

### Slide anatomy (the notice)

```
┌ masthead ─────────────────────────────────────────────────────────┐
│ ■ NOTICE 06 / 14   SUBJECT                        as-of stamp     │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│   The operative sentence — the contract's headline claim,          │
│   verbatim, sentence case                                          │
│                                                                   │
│   6.1   numbered provision                                        │
│   6.2   numbered provision                                        │
│                                                                   │
├───────────────────────────────────────────────────────────────────┤
│ AUTHORITY  Canton pitch deck, slides 3 & 5              06        │
│              Medici — Proprietary & Confidential                  │
└───────────────────────────────────────────────────────────────────┘
```

- `.slide` is a three-row grid (`auto 1fr auto`): masthead, centred body, authority foot.
  It is `position:absolute; inset:0` inside a fixed 1280×720 `.stage` that is
  `scale()`-fitted to the viewport — the house geometry contract, so the presenter's view,
  a screenshot and the PDF page are the same composition.
- **The seal** is a 9×9px Electric Blue square. It is the deck's only decorative mark and
  it is what makes a notice a notice.
- **Clause numbers are `<notice>.<n>`** — 6.2 is citable across a room and across a
  forward. They are the referencing mechanism of the form, which is the exemption
  craft-floor's section-number rule explicitly allows ("unless the sequence itself carries
  information the reader needs").
- **The authority line** carries the source file and slide numbers for every figure on the
  slide. Written as prose (*"Canton pitch deck, slides 3 & 5"*) rather than as a filename,
  both because it reads better and because the house linter's process-leak rule treats a
  rendered `*.md` path as a leak.

### Components

| Component | Rule |
|---|---|
| Clause row | `46px` mono gutter + text, hairline top and bottom. No bullets, no icons. |
| Figure schedule | label left, mono value right on a hairline row. **Never** a metric card. |
| Comparison | two ruled columns sharing one top rule, divided by a 1px vertical hairline. |
| Table | uppercase 12px `#8A8A8A` heads, 1px `#1A1A1A` row rules, first cell white 500. |
| Register | two lists under `What exists` / `What does not exist` heads. |
| **Vacated provision** | 226px struck header + an italic *"No such provision"* body, bounded above and below by `#252525`. The signature component. |
| Blockquote | 3px Electric Blue rule at the left, 26px white quotation, mono attribution. |

### The signature moment

On `pitch-deck-mastery` notice 05 and `presentation-writing` notice 07, the slide carries a
clause header — **~~Liquidation threshold~~** — struck through, with the body reading *"No
such provision."* An absence set as type. Every other deck in this category asserts "no
liquidation" in a headline; this one shows the clause being vacated, which is the only form
of the claim the audience can check. On `pitch-deck-mastery` notice 04 the same idea runs
inside the payoff plot: the threshold a lending market would draw is drawn, then crossed
out, with the caption *"a lending market draws its threshold here — nothing to cross."*

### Figures (all authored SVG, no library, no raster)

- **Payoff plot** — P (blue) flat at 1.00 to the strike, then S/x; N (green) the band between
  P and 1.00; the stacked top edge is one flat green line across every price. The invariant
  is the *flatness*, not a sentence about it.
- **Split diagram** — the collateral rect with a dimension line at its left; the two claims
  stacked without a gap at the right with an identical dimension line. Two rules of exactly
  the same length is the proof.
- No icons, no emoji, no glyph substitutes. Colour never carries meaning alone: P and N are
  labelled and positioned as well as coloured.

---

## 4. The explainer

Same world, 1920×1080, `?scene=N` + Space/→ override, `window.__player = {scene, t, total,
totalSeconds, seek(n)}`, a 3px progress rule at the foot.

**Motion thesis: the same gesture, performed and then refused.** Motion material is line,
mask, position and exactly one hard clip. Nothing glows, nothing bounces, nothing parallaxes.

| Role | As built |
|---|---|
| `hold` | one 0.5s entrance, then the frame is still for the rest of the scene |
| `accumulate` | a value grows across the *whole* scene on a linear clock |
| `strain` | constraints attach one at a time while the frame's own stroke greys and thickens |
| `rupture` | a 0.18s hard `clip-path` cut at the crossing, then a long dead hold |
| `assemble` | reveal order follows the narration exactly; nothing that arrives ever leaves |
| `arrest` | the seizing clamp enters on the identical easing and **stops** at 55% |
| `divest` | subtractive only; nothing new may enter the scene |
| `cadence` | one gesture, then stop |

Scene animations are gated by `.scene:not(.on) .anim { animation-name: none !important }`,
which both prevents off-screen work and restarts every animation from zero on a seek.
Under `prefers-reduced-motion: reduce` all of it is disabled and every scene still reads as
a legible still frame.

---

## 5. Accessibility as built

- Every body and label colour clears 4.5:1 on `#000`: `#FFFFFF` 21:1, `#AAAAAA` 9.0:1,
  `#8A8A8A` 5.9:1, `#7A7A7A` 4.9:1.
- The single exception is the confidentiality footer at `#666666` (3.7:1) — pinned by the
  brand guide §3.4 rule 6 as legal-disclaimer register. Not softened; recorded.
- Deck: ←/→/↑/↓/PageUp/PageDown/Home/End/Space. Explainer: Space, →, ←, Home.
- Every figure is an `<svg role="img">` with an `aria-label` that states the relationship it
  draws, not the shapes it contains.
- No colour-only encoding anywhere.

---

## 6. Where the pinned brand overrode this tool, and stayed

Recorded because a design record that hides its conflicts is not a record. In every row the
brand won, per §0.

| Impeccable's default | The pin | Resolution |
|---|---|---|
| craft-floor bans an eyebrow/kicker above a heading — *"a ban, not a default: no brief earns it back"* | the house skeleton ships `.kicker`, and §3.3 defines a label/eyebrow level in the type scale | **Brand wins.** Kept, as the masthead's `NOTICE nn / nn · SUBJECT` register — which is the form's identifier, not a decorative label above a heading. |
| craft-floor refuses a coloured `border-left` above 1px — *"the most recognizable tell of AI-generated UIs"*, and the detector flags it | the house skeleton ships `.quote{border-left:3px solid var(--blue)}` | **Brand wins**, narrowly: kept only on `staging` notice 05's verbatim market quotation, where a rule beside a blockquote is centuries of typographic convention rather than a card tab. The rule is stripped from the two decks that never quote, so it is not dead CSS. |
| craft-floor refuses section numbers unless the sequence carries information | — | Clause numbers kept: in a circular they are the citation mechanism, which is the rule's own stated exemption. |
| new-work names `IBM Plex` in its list of training-data default faces that mean "you stopped looking" | §3.1/§3.2 pin IBM Plex Sans + Mono, self-hosted, with a written rationale | **Brand wins, without argument.** This is exactly the "pinned aesthetic" case impeccable's own top-level rule exists for. |
| craft-floor: pick light or dark from the use scene, never by category | §2.1/§10.3/§10.6 pin a true-black external surface | **Brand wins.** `#000000` exactly — not the softened near-black universal dark-theme craft prefers. The house linter raises `C-PURE-BLACK`/`C-PURE-WHITE` as notices and its own hint says "expected: this brand's contract pins the canvas at #000000". |
| animate.md's timing table tops out at 500–800ms for an authored focal entrance; §9 tops out at 200ms | the explainer's scenes are 10–24s long, timed to narration | **Both honoured, at different scopes.** §9 governs *interface* transitions (hover, toast, modal) and is followed literally in the deck. Scene-length film motion runs longer because a `vo_seconds` scene demands it, but obeys §9's substance: pure deceleration, no spring, no bounce, no overshoot, reduced-motion off. |
| detector advisory: em-dash saturation | — | Most em-dashes are verbatim contract copy that may not be rewritten. Not "fixed"; recorded. |

---

## 7. What this system does not have

No photography, no product screenshot, no customer logo, no icon set, no gradient, no
shadow, no glass, no card. There is no imagery in the source corpus and none was invented.
Depth comes from border contrast, as `[rules] gradients = false` requires.
