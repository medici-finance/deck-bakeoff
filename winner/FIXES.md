# FIXES — `winner/` (ship-tomorrow artifact)

Source: `tracks/canvas-design/brand/staging/` (deck/index.html + explainer/{explainer.html,SCRIPT.md}),
copied verbatim with its four sibling IBM Plex `.woff2` files into `winner/deck/` and `winner/explainer/`.

Fix list: `bakeoff/JUDGING-design-claude.md` §4, plus the canvas-design/brand findings in
`reviews/design/{by-messaging-rubrics,by-open-design-review,by-impeccable-critique,by-academic-pptx}.md`.

Scope rule applied: **correctness and legibility only.** No redesign, no reordering, no rewording of
headline claims. Two of the judge's seven items are content/contract decisions rather than defects and
are recorded as HELD at the end, with reasons.

Contract of record: `messaging/staging/staging.yaml`.

---

## Measured before / after

Rendered in headless Chrome 152 at the artifact's own native sizes (deck 1280×720, film 1920×1080,
scale 1.0), contrast computed per WCAG 2.x relative luminance against the composited background
(the brand-pinned `#000000` canvas).

| | strings | under 4.5:1 | min CR | min rendered px | under type floor |
|---|---|---|---|---|---|
| deck **before** | 268 | **152** | 1.66 | 10.5 | 211 (floor 18px) |
| deck **after** | 270 | **0** | **5.03** | 10.5 | 212 (floor 18px — see HELD-2) |
| film **before** | 124 | **77** | 1.66 | 16.0 | 36 (floor 28px) |
| film **after** | 115 | **0** | **5.03** | **28.0** | **0** |

Text-over-text collisions (rendered bounding boxes, same line band): deck 0 → 0; film **4 → 0**.
Near-touches (< 10px horizontal gap on a shared line band): deck 1 → 0; film 1 → 0.
Content overflow past the padding box: deck 0 → 0 on all 14 slides.

Deck string count 268 → 270 = the two nodes added by F1. Film 124 → 115 = the nine motion-role
eyebrow words removed by F4.

---

## F1 — d11's dropped roll-cost supporting point (correctness)

**Finding.** `by-messaging-rubrics.md` L60: *"`d11` 'Roll cost −1.2%/yr at 10bps across ~12.2 rolls/yr
is the dominant cost driver' absent from the deck entirely (grep for `10 bps`, `12.2`, `1.2%` = 0 hits)
— **fact dropped**, and the only two contract numbers missing from any deck."* Judge fix 1, and the
driver of the −1.25%/yr already stated on that same slide.

**Change.** `deck/index.html`, slide 11. Added a fourth annotation cell carrying `supporting[3]`
**verbatim from `staging.yaml`**:

> `Roll cost −1.2%/yr at 10bps across ~12.2 rolls/yr is the dominant cost driver.`

Inserted at its contract position — after `supporting[1]` (CONTINUOUS AND COMPUTABLE) and before
`supporting[4]` (STATED LIMIT) — so contract order is preserved, not reordered. The slide's annotation
grid went `repeat(3,1fr)` → `repeat(4,1fr)`, which is the deck's own existing mechanism for a
four-point slot (the layout engine already supports 1–4 columns).

**Verification.**
- `grep -c 'Roll cost −1.2%/yr at 10bps across ~12.2 rolls/yr is the dominant cost driver.'` → 1 in
  `deck/index.html`, byte-identical to the `staging.yaml` d11 `supporting[3]` line.
- Rendered slide 11: 21 measured strings (was 19), **0 overlaps, 0 overflow**. The provenance strip
  bottoms out at y=662.0 against the 662px content bottom — exactly where slide 13 (the deck's other
  dense slide) already sits, so this is the existing bottom, not a new overrun.
- `shots/deck-11.png`.

## F2 — provenance / SRC line and the whole low-contrast ramp (legibility)

**Findings.** `by-open-design-review.md` A11Y-CONTRAST-01 (blocker): the traceability line renders
`rgb(58,58,58)` on `#000` at 10.5px = **1.85:1**, *"required content set below the threshold of sight."*
A11Y-CONTRAST-02 (major): in-plate SVG labels at `fill:#333` = **1.66:1**; 123 of 221 sampled strings
under 4.5:1. Judge fix 2: *"`.prov` from `#3A3A3A`/10.5px to `#AAA`/13px; in-plate SVG labels off
`#333`."*

**Change.** A four-step grey ramp where every step clears 4.5:1, applied identically to both files, so
the existing four levels of hierarchy survive rather than collapsing into two. Hairline **strokes**
were deliberately left alone (`#666666` as `stroke=` — 151 in the deck, 112 in the film — and the four
non-text `fill=`s), per the review's *"reserve `#333` for hairlines only."*

| token / rule | before | CR | after | CR |
|---|---|---|---|---|
| `.prov` (deck, the SRC line) | `#3A3A3A` @ 10.5px | **1.85** | `var(--text)` `#AAAAAA` @ **13px** | **9.04** |
| `--muted` — deck+film footer, film `.sub` | `#666666` | 3.66 | `#8A8A8A` | 6.08 |
| `--faint` — `.hdr`, `.annots .k`, `.coverlist .k` | `#4A4A4A` | 2.37 | `#7C7C7C` | 5.03 |
| `.slide-no` (deck folio) | `#3A3A3A` | 1.85 | `var(--faint)` `#7C7C7C` | 5.03 |
| `.hint` (deck nav hint) | `#242424` | 1.35 | `var(--faint)` `#7C7C7C` | 5.03 |
| `.count` (film folio) | `#3A3A3A` @ 16px | 1.85 | `var(--faint)` `#7C7C7C` @ 28px | 5.03 |
| SVG `<text fill>` tertiary — 21 deck, 16 film | `#333333` | **1.66** | `#7C7C7C` | 5.03 |
| SVG `<text fill>` secondary — 39 deck, 25 film | `#666666` | 3.66 | `#8A8A8A` | 6.08 |

Retained levels: `#FFFFFF` 21.0 · `#AAAAAA` 9.04 · `#8A8A8A` 6.08 · `#7C7C7C` 5.03.

**Verification.** Every string on all 14 slides and all 9 scenes re-measured from computed style +
`getScreenCTM` scale: **deck 0/270 under 4.5:1 (min 5.03), film 0/115 under 4.5:1 (min 5.03)**, down
from 152/268 and 77/124. The SRC line specifically: 1.85:1 @ 9.2px rendered → **9.04:1 @ 13.0px**.
See `shots/deck-01.png`, `shots/deck-11.png`.

## F3 — film type ramp to the 28px floor (legibility)

**Findings.** `by-open-design-review.md` A11Y-SIZE-01 (major): *"Explainer min 16px against a 28px
floor; 7 of 10 strings under it, including the scene counter at 1.85:1."* Judge fix 6.

**Change.** `explainer/explainer.html` — the three CSS-level strings that were genuinely below the
floor: `.hdr` 17px → 28px, `.scene::after` (the mandated footer) 17px → 28px, `.count` 16px → 28px.
The figure type (`.l1`/`.l2`/`.l3` at 20/23/26 SVG user units inside a 1180→1660 figure) already
renders at 28.1/32.4/36.6 CSS px, so it was left untouched — raising the declared numbers would have
pushed it to 39–51px and broken every plate. `.hdr` flex `gap` 22px → 44px so the two remaining
eyebrow fields still read as two fields at the larger size.

**Verification.** Film **min rendered size 16.0px → 28.0px; strings under the 28px floor 36 → 0**,
across all 9 scenes at their midpoints. No new overflow: 0 items past the scene padding box.

## F4 — the scene eyebrow printed internal motion vocabulary (correctness)

**Findings.** `by-messaging-rubrics.md` L89: house-guide **B4 fails in the film** — *"the scene eyebrow
prints staging's internal motion vocabulary (`SC. 04 / 09 RUPTURE`, `ACCUMULATE`, `STRAIN`) to the
viewer"*; L144: *"unglossed insider terms in front of a room."* Judge fix 4.

**Change.** Removed the `<b>{motion_role}</b>` field from all nine scene eyebrows. The eyebrow keeps
`SC. NN / 09` and the time range — sequence and timing the viewer uses. The motion role stays where it
belongs, in `SCRIPT.md`'s `motion` column and in the `data-role` attribute that drives the CSS.

The judge's suggested replacement was `SC. 04 / 09 · MARCH 2020`. Applied as a **removal** rather than
a relabel: `MARCH 2020` is contract text for scene 4 only, and the other eight scenes have no
equivalent anchor in the contract — relabelling all nine would mean authoring nine strings
`staging.yaml` does not contain, which the no-new-copy rule forbids. Removal resolves the finding
(no internal vocabulary reaches the viewer) with zero invented copy.

**Verification.** `grep -c '<b>' explainer/explainer.html` → **0**; the eyebrow field that carried
the role is gone from all nine scenes. Rendered text of all 9 midpoint frames re-extracted: no bare
motion-role label appears anywhere on screen (the only substring hits are inside contract prose —
`THRESHOLD`, `HOLDS`). `SCRIPT.md` still documents all nine roles in its `motion` column and still
matches the film row-for-row. See any `shots/scene-*.png`.

## F5 — six text collisions in the film, one near-touch in the deck (legibility)

Judge fix 5 named two (`s6`, `s4`). Measuring every rendered text bounding box at each scene's midpoint
found four true overprints and two near-touches; all six are fixed. Every change is a coordinate move —
no text, size or colour was altered by this fix.

| # | scene | defect (measured) | change |
|---|---|---|---|
| a | `s4` | `$0` (52px) sat at y=314 with its cap-top at ≈277, **overprinting the white $0-baseline at y=286**; `CLEARED FOR` sat at the far left (x=90), 1000 units from the value it labels, reading as a caption on the bar field | `$0` y=314 → **338** (cap-top 301, clear of the ticks at 295); `CLEARED FOR` moved to `x=1006 text-anchor="end"` y=338, so it reads `CLEARED FOR $0` as one phrase — matching the scene's own sub-line |
| b | `s6` | y-axis `1.00` ended 16.9px from `P + N ≡ 1.00` while overlapping its line band by 11px — the "clipping" the judge saw | axis labels `1.00`/`0` x=120 → **108** (`1.00` right edge 299.4 → 282.5; clearance 16.9px → **33.8px**). `P + N ≡ 1.00` kept at x=132, still aligned to the plot's left edge |
| c | `s6` / deck `pl.08` | the `S` tick and its `STRIKE` gloss were 9.3px apart (deck: 8.7px) and read as one token `S STRIKE` | `STRIKE` x=452.67 → **464** in both files (clearance 9.3px → **25.0px** film, 8.7px → **19.8px** deck) |
| d | `s3` | `"cannot liquidate its position…"` (x 249–1255) and `SO THE PATHWAY IS BUILT BY HAND, PER ISSUER` (x 861–1670) **overprinted on one baseline, 394.5 × 37.6px** | `SO THE PATHWAY…` y=306 → **340** |
| e | `s7` | `ONE POSITION, VISIBLE TO ITS COUNTERPARTIES AND NO ONE ELSE` **overprinted** `ONE ATOMIC TRANSACTION`, 155.7 × 32.4px | the left caption pair y=272/298 → **316/342**; the right caption stays at y=268 as its box's own caption |
| f | `s9` | `NOT ASKED FOR: CAPITAL, CUSTODY, OR A COMMITMENT` **overprinted** `WHAT COMES BACK IS THE PAYOFF AT EVERY PRICE`, 186.6 × 37.0px; separately, the table head rendered as **`REFERENCE PRICE xP`** (gap −0.6px) | `NOT ASKED FOR…` y=288 → **322**; the P/N/SUM columns x=790/910/1020 → **812/920/1024** (header and all three value rows moved together, 12 nodes) |

**Verification.** Re-measured every text pair on all 14 slides and all 9 scenes:
**0 overprints, 0 near-touches** (< 10px horizontal gap on a shared line band) in either medium.
The three residual bounding-box overlaps the detector still reports — `P`/`PROTECTED` and
`N`/`AMPLIFIED` in `s6` (13px), the two-line callout in `s8` (6–7px), `ONE POSITION`/`YOURS` in `s9`
(4.3px) — are line-box leading between deliberately stacked label pairs, not ink collisions; confirmed
by eye in `shots/scene-6.png`, `shots/scene-8.png`, `shots/scene-9.png`. Frames:
`shots/scene-3.png`, `scene-4.png`, `scene-6.png`, `scene-7.png`, `scene-9.png`, `shots/deck-08.png`.

## F6 — green in the cover mark (brand-pin correctness)

**Finding.** `by-open-design-review.md` BRAND-MARK-01: *"The cover 'M' mark renders blue **and green**.
Brand §2.6 makes green functional-only and `brand.toml` says gold appears only inside the mark."*
`brands/medici/brand.toml` `[palette]`: `good = "#00CC66"` under *"Functional colours — used only
functionally (pass/fail/warn), never decoration."*

**Change.** `deck/index.html` cover mark, one attribute: the lower stacked rect `fill="#00CC66"` →
`fill="#3366FF"`. The mark now carries only Electric Blue plus the gold dot that `brand.toml`
explicitly exempts (`exempt_colors = ["#D4A843"]`, *"Gold appears ONLY inside the mark"*).

**Verification.** `grep -c '#00CC66' deck/index.html` → 1 (the unused `--green` token declaration only);
0 occurrences in any slide body. Accent budget unaffected: `check_deck.py` counts class-driven accent
uses *outside* SVG (`if self._svg_depth == 0 and ({"kicker","accent"} & classes)`), so the mark is
outside the budget by the contract's own design — `H-ACCENT-BUDGET` is not raised on any slide, before
or after. `shots/deck-01.png`.

---

## Held, with reasons

**HELD-1 — judge fix 3, "reword citations for a reader" / the `house-brand-guide §0.5` reference on the
cover.** Not applied. The cover's SRC line is **verbatim from the contract**: `staging.yaml` d1
`source: "canton-pitch-deck.md Slides 1, 3; house-brand-guide.md §0.5"`. Rewriting it to
*"Medici Canton briefing, slides 1 · 3 · July 2026"* would drop the file-level traceability that scored
this deck 42/42 on `by-academic-pptx.md`'s in-slide-citation check and would put the deck out of sync
with its contract — a content decision for the messaging leg (edit d1's `source:`, and the deck
follows), not a rendering defect. The legibility half of the judge's complaint **is** fixed by F2:
the line now renders at 9.04:1 instead of 1.85:1. Flagged for the owner: if the internal reference
should not appear on a prospect's cover, change it in `staging.yaml` first.

**HELD-2 — judge fix 7, "claim 30px → 44px, paid for by cutting the 94-word body median toward 40."**
Not applied. The paying half is a rewrite of body copy on every slide, which the no-rewording rule
forbids, and the claim at 30px white-on-black is the largest text on its slide and far above any
legibility threshold — this is a type-scale preference, not a legibility failure. Raising `.claim` to
44px without the copy cut would overflow the slides (slide 11's provenance strip already bottoms at
exactly 662px of a 662px content box). This is why the deck's "under 18px" count is unchanged at
211 → 212; the film's floor, which the judge did raise as a defect, is fully met (F3).

**Not applicable / already satisfied.**
- `A11Y-MOTION-01` (zero `prefers-reduced-motion` blocks) is a canvas-design/**free** finding.
  This brand artifact has one block in each medium; both verified present and unmodified.
- `COPY-OVERFLOW-01` (clipped stat panel) is in the `pitch-deck-mastery` lane, not `staging`.
- `by-academic-pptx.md`'s "raise `.prov` to 22px" is superseded by the judge's explicit 13px.
- `by-impeccable-critique.md` P0/P1/P2 for this artifact (drop the `DIAGRAM`/`COMPARE`/`STATEMENT`
  plate-rail word, the 3px blue pull-quote rule, the pull-quote's ~2.0 line-height) are craft
  preferences on a 28/32 artifact, not correctness or legibility. Not applied.

---

## Gates run

| gate | result |
|---|---|
| `python3 skills/deck-author/tools/check_deck.py winner/deck/index.html` | **PASS** — 14 slides, brand Medici, footer class external, 0 errors, the same 3 expected notices as the source (`C-PURE-BLACK`, `C-PURE-WHITE`, `P-DECKMD-COUNT`) |
| 14 slides, `data-layout` in pool, action title on each | PASS |
| footer on every slide / scene (`.slide::after`, `.scene::after` = `Medici — Proprietary & Confidential`) + `deck-footer` meta | PASS |
| folio on every slide (14) and scene (9) | PASS |
| print pagination — `@page{size:1280px 720px;margin:0}`, `page-break-after:always` | PASS; `--print-to-pdf` yields exactly **14 pages** |
| film: 9 scenes, `data-dur` == contract `vo_seconds` `[10,10,10,12,10,24,14,18,12]`, total 120s | PASS |
| film: `window.__player` exported, `?scene=N` honoured | PASS |
| `SCRIPT.md`: 9 rows, durations match the film | PASS |
| `prefers-reduced-motion` block present in both media | PASS (1 / 1) |
| self-hosted IBM Plex only, no remote assets | PASS — 4 `@font-face` per file, 4 sibling `.woff2`, zero `http(s)://` outside the SVG namespace URI |
| brand pins: `#000000` canvas, `#FFFFFF` primary, Electric Blue budget | PASS — `H-ACCENT-BUDGET` not raised on any slide |
| no personal names except "Ian"; co-founders as "Co-founder" | PASS — zero personal names in either file or `SCRIPT.md`. Every capitalised token is an organisation (Medici, Canton, Morpho, MakerDAO, RedStone, Credora, Gauntlet, Dune, Franklin Templeton, Deribit, Hypercall, AAA Flowers S.A.), a place (Panama), a date, or sentence-initial. `Ian`, `founder`, `co-founder`: 0 occurrences |

## Frames

`winner/shots/` — 23 PNGs, rendered headless Chrome 152 at scale 1.0:
- `deck-01.png` … `deck-14.png` — all 14 slides at **1280×720**, driven by the deck's own `#N` hash route.
- `scene-1.png` … `scene-9.png` — all 9 scenes at **1920×1080**, each at its **midpoint**: seek via
  `?scene=N`, `window.__player.pause()`, then every `document.getAnimations()` entry paused and its
  `currentTime` set to `data-dur/2` (5000 / 5000 / 5000 / 6000 / 5000 / 12000 / 7000 / 9000 / 6000 ms).
  Frame geometry checked against the stage: the plate frame drawn at x=38 lands at x=37–38 in the PNG,
  confirming an unscaled 1:1 capture.
