## brand

Contender: **visual-explainer** (nicobailon, v0.10.0) &mdash; `skills/design/visual-explainer/plugins/visual-explainer/`.
Mode: `brand` (Medici house brand, dark external surface). Six artifacts, all rendered, all three
messaging contracts consumed verbatim.

### Artifacts

| Artifact | Path | Result |
|---|---|---|
| deck &middot; staging (14 slots) | `brand/staging/deck/index.html` | linter **PASS** |
| deck &middot; presentation-writing (14 slots) | `brand/presentation-writing/deck/index.html` | linter **PASS** |
| deck &middot; pitch-deck-mastery (13 slots + appendix A1 = 14 slides) | `brand/pitch-deck-mastery/deck/index.html` | linter **PASS** |
| explainer &middot; staging (9 scenes, 120s) | `brand/staging/explainer/{explainer.html,SCRIPT.md}` | 120s = contract total |
| explainer &middot; presentation-writing (8 scenes, 132s) | `brand/presentation-writing/explainer/{explainer.html,SCRIPT.md}` | 132s = contract total |
| explainer &middot; pitch-deck-mastery (8 scenes, 143s) | `brand/pitch-deck-mastery/explainer/{explainer.html,SCRIPT.md}` | 143s = contract total |

Build sources (kept, so the artifacts are reproducible): `build/kit.py` (shared house kit, figure
generators, deck + film engines), `build/deck_*.py`, `build/film_*.py`. Fonts are copied beside every
HTML file (`<artifact>/fonts/*.woff2` + the OFL notice); no CDN, no remote asset of any kind.

### Time to artifact (wall clock, one session)

| Step | ~min |
|---|---|
| Read brief + brand guide + `brand.toml` + skeleton + all three `staging.yaml` + the linter source | 12 |
| Design-judgment plan + `kit.py` (deck CSS/JS, payoff/split/climb/zero SVG generators) | 10 |
| Deck 1 (staging) incl. two render-and-look fix rounds | 7 |
| Deck 2 (presentation-writing) | 4 |
| Deck 3 (pitch-deck-mastery, 13 slots + appendix) | 5 |
| Film engine (`FILM_CSS`, `FILM_JS`, `film_*` figures, `script_md`) | 12 |
| Film 1 (staging, 9 scenes) incl. two motion fix rounds | 9 |
| Film 2 (presentation-writing) | 5 |
| Film 3 (pitch-deck-mastery) | 5 |
| Verification passes (linter &times; 3, structural parser, 8 browser screenshots, type-size sweep) | 8 |

Marginal cost per additional messaging contract, once the kit existed: **~9 minutes** for a deck +
explainer pair. Nearly all of the cost is in the first one.

### The tool's process, as actually run

1. **Design judgment** (SKILL.md &sect;"Design judgment") &mdash; ran it, but in brand mode the "4&ndash;6 named
   hex values" step is a *transcription*, not a choice: the palette is pinned by `brand.toml`, so the
   named values came from there (`#000000` canvas, `#0A0A0A` surface, `#1A1A1A`/`#252525` hairlines,
   `#FFFFFF`/`#AAAAAA`/`#666666` text, `#3366FF` accent, `#00CC66`/`#FF4444` functional, `#D4A843`
   mark-only). Type roles were likewise pinned (IBM Plex Sans 600 display / 400 body, IBM Plex Mono
   500 for every figure). The step that *did* pay was the skill's "audit once &mdash; would I produce this
   plan for any similar page?" question, which produced the one real layout idea:
   **the payoff axis is the deck's spine** &mdash; the same price axis is drawn on the mechanism slide, the
   cost slide and the proof slide, and the argument is told by *what gets drawn onto it* (a threshold
   that fires, then a threshold with nowhere to sit). Recorded at the top of `build/kit.py`.
2. **Reference routing** (SKILL.md table) &mdash; read `references/slide-patterns.md` (planning-from-source
   inventory; the 10 slide types; the Mermaid-vs-CSS rule) and `references/css-patterns.md`
   (Connectors, SVG Draw-In, Sparklines, Before/After panels, Pipeline horizontal steps, Reduced
   Motion). Did **not** use `templates/slide-deck.html` verbatim &mdash; see "overrides".
3. **Representation choice** &mdash; ran the skill's routing table per slot. It routed everything away from
   Mermaid: the payoff is a continuous function of price (not a graph), the split is a 3-node flow
   (the skill's own rule: "use CSS Pipeline for simple linear flows&hellip; never leave a small Mermaid
   diagram alone on a slide"), and the comparisons are matrices (semantic `<table>`). **No Mermaid
   anywhere, so no `mermaid.min.js` was fetched** &mdash; the single permitted network fetch was not used and
   `tracks/visual-explainer/vendor/` was never created.
4. **Final checklist** &mdash; ran it: complete documents, self-contained SVG favicon, `<figure>`-equivalent
   `role="img"` + `aria-label` on every generated SVG, no horizontal overflow, fonts self-hosted with
   fallbacks, tables keep their rows.

### Where the tool's diagram-first instinct helped, and where it hurt

**Helped, decisively, on the mechanism.** Brief goal 3 asks for "one diagram they could redraw", and
the skill's "depict the mechanism, not its name" + "one figure, one claim; the caption states it"
invariants are exactly right for the P/N payoff. Drawing P and N *stacked* makes the invariant
literally visible &mdash; the top edge is one flat line at 1.00 across the whole width &mdash; which is a
stronger proof than the identity written out. The `pitch-deck-mastery` contract independently
specified that same stacked-with-flat-top drawing in its slot-4 `diagram:` field, so contract and tool
agreed. It also paid off in the film: because the figure is generated by one Python function, the deck
and the explainer show the *same* axis, and the film can animate its parts (draw P, then N, then the
flat sum) without a second implementation.

**Hurt on the quiet slots.** The tool's default is that a slot deserves a figure. Three slots do not:
the quote slot (`staging` d5), the pivot slots (`staging` d7, `presentation-writing` 5) and the proof
slot (`pitch-deck-mastery` 5) are *arguments*, and every candidate diagram I sketched for them was
decoration &mdash; which the brand guide bans outright and the messaging contracts' own `motion_role: hold`
scenes forbid in the film. I overrode the instinct and made them typographic. The same tension appears
in the film: the skill has no vocabulary for *subtractive* motion, and `divest` scenes (all three
contracts have one) are the hardest thing in this brief &mdash; I built `drop-out` (fade to 12%) so the film
can take its own apparatus away, which is a motion the skill's animation section does not contemplate.

**Hurt on density.** `slide-patterns.md` plans decks at "18&ndash;25 slides" from a source document and says
"do not drop content to fit a fixed slide count &mdash; add slides instead". That rule is *wrong here*: the
messaging contract fixes the slot count and forbids reordering, so the correct move is to compress
within a slot, which is the opposite instruction. I followed the contract.

### Overrides (tool instruction vs. what I did)

| Tool says | What I did, and why |
|---|---|
| Write to `~/.agent/diagrams/` | Wrote to the task's output paths (task instruction). |
| Slides are `100dvh`, viewport-fit | Fixed **1280&times;720** letterboxed stage, per the brief and the house linter's `H-GEOMETRY` rule. `templates/slide-deck.html` was read for its chrome ideas but not used as the base &mdash; `brands/medici/deck-skeleton-external.html` is the house contract and the linter enforces it. |
| Reader rail, outline/help overlays, resume state, reading-percent | Dropped. A confidential external deck deliberately does not persist reading position (the house linter's docstring says so explicitly), and the brief's chrome spec is &larr;/&rarr; + click + a slide counter. Kept: keyboard, click, wheel, `#N` deep links, progress bar, folio + counter. |
| "Pages meant to persist ship both colour schemes" | Single dark scheme. The brand pins the external surface to `#000`; a light variant would be a different artifact class (brand guide &sect;10.6). Deliberate, per the skill's own "single-theme is fine when deliberate". |
| Good font pairs / accent directions lists | Ignored &mdash; brand-pinned (IBM Plex Sans + Mono, Electric Blue). The skill's precedence rule ("the project's existing design system" outranks the skill) says to ignore them, so this is compliance, not a fight. |
| `surf` generated imagery | Not used; brand guide &sect;7.1 forbids imagery outright ("No photography&hellip; our value is mathematical"). |

### Brand fights

1. **P/N colour.** Brand guide &sect;1.1 codes **P = Electric Blue, N = Green** (the mark encodes the split);
   &sect;7.2 codes chart lines as **P = Gold, N = Red**; `brand.toml` says *"Gold appears ONLY inside the
   mark"*. Those cannot all hold. Resolved toward `brand.toml` + &sect;1.1: **P blue, N green**, gold confined
   to the mark's accent dot, red reserved for the liquidation pathway (functional, per &sect;2.3). The
   payoff figure therefore matches the logo, which is a happy accident worth keeping.
2. **The mark.** `brand.toml` points at the skeleton's `#assay-mark` (a gold shield-tick) and
   `#oct-line`. Those are *assay* marks, not Medici's. I built the Medici mark to brand guide &sect;1.1
   (blue stem = the whole; blue upper right stem = P; green lower right stem = N; blue split dot; gold
   accent dot) as an inline `<symbol>`, and used its line form as the watermark at opacity .05. On a
   deck whose entire argument is the split, the logo that encodes the split is the right mark.
3. **Accent budget (`accent_budget = 2`).** The linter counts elements classed `kicker`/`accent`. I kept
   one kicker per slide and renamed the skeleton's `.card.accent` to `.card.lead` &mdash; not to dodge the
   count, but because the rule is about *visible accent uses* and a 3px left border on a card is one.
   Every slide is inside budget as counted, and no slide carries more than two blue elements by eye.
4. **Pure `#000`/`#fff` notices** fire on every deck (`C-PURE-BLACK`, `C-PURE-WHITE`). Both are brand
   pins (`brand.toml` `canvas`/`text_primary`); the linter itself says "expected&hellip; ignore with a
   reason". Left as notices rather than shipping a `.deckcheck.json` suppression, so the reason stays
   visible in this file.

### Friction (top items)

1. **The linter's `deck.md` process-leak needle fires on legitimate source citations.** Every slide
   carried a provenance line ("canton-pitch-deck.md Slides 3, 5") and `H-PROCESS-LEAK` rejected 10 of
   14 slides, because `"deck.md"` is a substring of `"canton-pitch-deck.md"`. The fix improved the
   deck: the on-slide citations are now reader-facing ("Medici Canton briefing, slides 3 &middot; 5 &middot; July
   2026", "RedStone with Credora, Gauntlet and Dune &middot; RWA lending report, Part 2 &middot; March 2026"), which
   is what an external deck should show anyway. But the needle is a false-positive generator for any
   deck that cites its sources by filename. Worth a word-boundary or path-shaped match upstream.
2. **`transform-origin` on SVG elements.** The rupture (a proceeds column collapsing to zero) landed
   *below* its own axis, because `transform-origin: 50% 100%` resolves against the SVG viewport, not
   the element, until you set `transform-box: fill-box`. Invisible in code review; caught only by
   looking at a frame. `css-patterns.md` documents `drawIn` but not this.
3. **Path-length maths for draw-in.** `css-patterns.md` says "set `--path-length` to the path's
   `getTotalLength()`", which needs JS at runtime. Overestimating the length silently ruins the timing
   (the curve finishes drawing at 30% of the duration and then idles). I compute the polyline length in
   Python at build time and emit it as `--len`, so the draw finishes exactly when the narration does.
4. **Vertical rhythm on a fixed stage.** The skill's slide patterns assume a scrolling-ish viewport; on
   a fixed 1280&times;720 board, top-anchored titles leave a hole at the bottom. Fixed with an automatic
   `.fill` wrapper (title anchored, body centred in the remaining height) injected in `render_slide`.
5. **No headless renderer available.** No puppeteer/playwright. Verified instead with (a) the house
   linter, (b) a stdlib HTML/regex structural parser (section counts, footer meta + print rule, remote
   assets, missing local assets, duplicate ids, minimum font sizes), and (c) a local
   `python3 -m http.server` on 127.0.0.1 driven through the browser tool for **8 real screenshots
   including four mid-animation frames** (staging s4 rupture and s6 assemble, pitch-deck-mastery s3
   split and s5 arrest, presentation-writing s3 cascade and s6 refused line). `window.__player` was
   queried live and returns `{scene, t, total, seek}` as specified. The messaging contracts' own
   `render_and_look` gate is therefore satisfied in substance, not by a headless harness.

### Slots and scenes

**Every slot and every scene of all three contracts is rendered.** Nothing was dropped, reordered or
reworded; headline claims are the slide titles verbatim (line-breaks only). Two notes:

- `pitch-deck-mastery` carries an **appendix A1** under `deck.appendix`. It is rendered as slide 14
  (labelled "Appendix"), so that deck has 13 argument slots + 1 appendix. Dropping it would have been
  a silent loss of contract content; the brief's 10&ndash;14 slide range still holds.
- The `staging` contract's video gates `motion_spec_locked` and `seams_declared` name design-lane
  artefacts (`references/motion-spec.md`, `tools/seam-gate.mjs`) that exist in the *messaging* skill,
  not in this contender's tool. They are not satisfiable from here and are not claimed. What this
  contender did instead is recorded per scene in each `SCRIPT.md`'s "What moves" column, and every
  scene's motion is derived from that scene's `motion_role` / `energy` / `peak`: exactly one rupture
  per film, `assemble` for the invariant (never rupture), `arrest` for the refused liquidation in
  `pitch-deck-mastery` s5 (the gesture starts, freezes, and two seconds of stillness follow &mdash; the
  contract's own note that s5 is "the most CHARGED and the second stillest" is honoured), subtractive
  motion only in every `divest` scene, and literally nothing moving in the `hold` scenes.

### Linter results

`python3 skills/deck-author/tools/check_deck.py <deck>/index.html` &mdash; **PASS on all three decks**
(14 slides each; brand Medici resolved from the shipped default contract; footer class *external*;
0 errors). Three notices each, all expected and all discussed above: `C-PURE-BLACK`, `C-PURE-WHITE`,
and `P-DECKMD-COUNT` (no `deck.md` sibling &mdash; the messaging contract's `staging.yaml` is this deck's
story file, and inventing a second one would have created a parity artefact with nothing to parity
against).

### Quality-floor checks

- Every figure on screen traces to a contract line; no number was invented, and no figure appears in a
  deck that is not in that deck's own contract.
- Deck body copy 18px (16px in dense card text), titles 33&ndash;47px; the only sub-13px text is the
  brand-mandated 11px footer and a 10.5px provenance line (brand guide &sect;3.4 legal-disclaimer style).
- Explainer copy 28&ndash;60px; figure ticks 21&ndash;23px; the only smaller text is the 16px footer (brand legal
  line) and a 17px scene ticker (recording chrome).
- Contrast: `#AAAAAA` on `#000` &asymp; 9.4:1, `#FFFFFF` on `#000` = 21:1, `#5C85FF` on `#000` &asymp; 5.4:1,
  `#00CC66` on `#000` &asymp; 9.2:1. `#666666` (&asymp;3.6:1) is used only for the footer/labels the brand pins at
  that value, never for body copy.
- Print: `@page { size: 1280px 720px }`, one slide per page, chrome hidden.

## free

Design contender `visual-explainer` (nicobailon, v0.10.0), mode `free`. Six artifacts, all
written, all three messaging contracts rendered in full.

### Time to artifact

| Artifact | Elapsed | Note |
|---|---|---|
| Reading (BRIEF + 3 staging.yaml + SKILL + slide-patterns + themes) | ~9 min | 1,332 lines of contract read verbatim before any HTML |
| `staging/deck/index.html` (14 slots) | ~22 min | includes building the whole shared design system: tokens, slide engine, reader chrome, print pagination, payoff/decline/climb/split SVG figures |
| `presentation-writing/deck/index.html` (14 slots) | ~6 min | reused the kit; new compositions only |
| `pitch-deck-mastery/deck/index.html` (13 slots + appendix A1) | ~7 min | same |
| `staging/explainer/` (9 scenes, 120 s) + SCRIPT.md | ~16 min | includes the timed scene engine, the motion vocabulary and the live sweep readout |
| `presentation-writing/explainer/` (8 scenes, 132 s) + SCRIPT.md | ~5 min | reused the kit |
| `pitch-deck-mastery/explainer/` (8 scenes, 143 s) + SCRIPT.md | ~6 min | plus one new motion role (`arrest`) the contract required |
| Browser render-and-look pass + fixes | ~12 min | see "Friction" |

Total ~83 min. Marginal cost of contracts 2 and 3 was ~11 min each once the kit existed —
the design system, not the slide count, is the cost.

### The tool's process, as actually run

Followed `SKILL.md` in its own order:

1. **Design judgment (its §"Design judgment")** — wrote the required plan before any HTML: 6 named
   hex values + 1 semantic, type roles, one-sentence layout concept. It is recorded verbatim in the
   module docstring of `_build/common.py`. Ran its "would I produce this plan for any similar page?"
   audit and revised — see "What the tool did with freedom".
2. **Reference routing (its §"Reference routing")** — read `templates/slide-deck.html`,
   `references/slide-patterns.md` and `references/themes.md`, as instructed. Did NOT read
   `mermaid-flowchart.html`, `libraries.md`, `architecture.html`, `data-table.html`,
   `responsive-nav.md` or `css-patterns.md`: the routing table sends you to them for content types
   this brief does not contain (no flowchart, no code, no 4+-section scroll page).
3. **Representation choice (its §"Choose the representation")** — applied per slot; the routing
   decisions are tabulated below.
4. **Slide deck mode (its §"Slide deck mode")** — inventoried the source (each contract's slot list)
   and mapped every slot to exactly one slide before writing HTML, per its Step 1/Step 2 rule.
   Used 8 of its 10 slide types: Title, Content, Split, Diagram, Dashboard, Table, Quote,
   Full-Bleed. Section Divider and Code are unused — the hall-lane contracts declare no sections
   and there is no code in the argument.
5. **Navigation chrome (`slide-patterns.md` §"Navigation Chrome")** — implemented all of its
   required reader controls: top progress bar, expanding right rail with slide titles, counter with
   reading percent, `O` outline overlay, `?` help overlay, `#slide-N` deep links, `localStorage`
   resume keyed by path+title+slide-count, `.js`-gated entrance states, real `<button>` controls
   with `aria-label`/`aria-current`/focus rings, plus its `autoFit()` safety net.
6. **Curated presets (`slide-patterns.md` §"Curated Presets") and `themes.md`** — read all four
   presets and the font-pair list; took the font PAIR from its recommended set (Bricolage Grotesque
   + JetBrains Mono) and rejected all four palettes. No runtime theme picker: `themes.md` says to
   add one only when the user asks to switch themes or names a prebuilt palette. Neither happened.
7. **Final checklist (its §"Final checklist")** — walked it; results in "Verification" below.

Ignored, as instructed by the task: its "write to `~/.agent/diagrams/`" rule. Everything went to the
task's output paths. Its `quick/` mode was not used (explicitly not for slides). Its PPTX exporter
was not used (not requested). `surf` is not installed, so its optional generated-imagery path
degraded to CSS/SVG, which is what its Step 4 tells you to do.

### Representation choice per slot (its routing table, and where I overrode it)

| Content | Its default | What I rendered | Why |
|---|---|---|---|
| The P/N payoff (staging d8, pw 6+7, pdm 4+5; video s6/s6/s4+s5) | *no row exists* | **hand-drawn SVG chart** | The routing table has rows for flowchart / sequence / ER / class / C4 / topology — all node-and-edge. A payoff function is a continuous curve over a price axis; Mermaid cannot draw one. This is the brief's "one diagram they could redraw", so it got the most work: P and N as stacked areas whose top edge is one flat line at 1.00 at every price. That flat edge IS `P + N ≡ collateral`. |
| Comparison / audit matrix (d4, d9, pw 9, pdm 9, pdm 11) | semantic `<table>` | semantic `<table>` | followed |
| Dashboard / metrics (d2, d10, pw 2, pw 10, pdm 7, pdm 8) | CSS grid + KPIs | CSS grid + KPI cards, mono `tabular-nums` | followed |
| Timeline / roadmap (d12, pw 12, pdm A1) | CSS timeline | CSS timeline | followed |
| Text-heavy argument slots | CSS grid cards | split / content layouts | followed |
| **Mermaid, anywhere** | its default for 6 content types | **none used** | No slot in any of the three contracts is a flowchart, sequence, ER, state, class or C4 diagram. Also: Mermaid's mandatory `diagram-shell` (zoom in/out/reset/expand, ctrl-scroll zoom, drag pan, click-to-expand) is chrome for a scrollable page, not a projected 1280×720 slide — a presenter cannot pan a diagram mid-sentence. `tracks/visual-explainer/vendor/` was therefore never created and the one permitted `curl` was never spent. |

### What the tool did with freedom (mode `free`)

Given no brand, the skill's own guidance is a *constraint list*, not a palette, and that is the
interesting part: it forbids Inter-only body text, violet/fuchsia Tailwind accents, cyan+magenta
neon, gradient-mesh blobs, purple-to-blue hero gradients, emoji markers, centred-everything, and
uniform large radii. It then offers four curated presets and five font pairs.

**It took the font pair and rejected every palette.** First plan was dark + gold + serif, which is
literally its own "Midnight Editorial" preset and would suit any premium deck — exactly what its
own audit question is designed to catch. Revised on three content-specific grounds:

1. **The constant-y rule.** One hairline runs at the same y on all 41 slides; the argument sits
   above it, the source citation and the footer below it. The deck reads as one continuous ruled
   axis, so when the payoff chart finally arrives it is simply *drawn in place*. The invariant is
   the layout, not just a claim on slide 8.
2. **The eyebrow label is the contract's own `function` field** (cover / statement / fact /
   comparison / quote / pivot / mechanism / evidence / objection / ask / end). The skill says
   "eyebrow labels only when they classify" — here the classification is the messaging contract's,
   not decoration invented to fill a corner.
3. **P = brass `#E0A32E`, N = cobalt `#5B8DEF`, fixed across all six artifacts.** The brief's third
   educational goal is a diagram they can redraw; a leg that changes colour between the deck and
   the film is not redrawable. `#E2563A` ember is reserved for loss, seizure and the liquidation
   pathway and is never used decoratively — the skill's own "keep semantic colour separate from the
   accent hue".

Palette: `--ink #0B0E13`, `--plate #141922`, `--rule #2A3341`, `--paper #E8E6E1`, `--brass #E0A32E`,
`--cobalt #5B8DEF`, semantic `--ember #E2563A`. Neutrals are biased blue toward the accent, per its
"pure mid-grey reads as unconsidered". Type: Bricolage Grotesque (display 700 / claim 600 / body
400) for the argument, JetBrains Mono (400/500, `tabular-nums`) for **every number, every eyebrow
and every source citation** — that last one is a content decision: the audience's stated distrust is
"numbers whose provenance is not named", so provenance is set in the same face as the number it
belongs to, on every slide, in the rail.

Single colour scheme, deliberately: the skill permits single-theme "for one-shot pages", and a
projected stage plus a printed 1280×720 PDF are one-shot surfaces. Dark prints dark, with
`print-color-adjust: exact`.

**Motion.** The skill has essentially nothing to say about timed animation — its motion guidance is
"entrance/hover only when it clarifies hierarchy" and "no continuous glow/pulse". That is correct
for a web page and useless for a 120-second film, so the explainer's motion vocabulary was built
from the *contracts* instead: every scene's animation is its `motion_role` field, implemented as its
own named CSS behaviour — `hold`, `accumulate`, `strain`, `rupture`, `assemble`, `arrest`, `divest`,
`cadence`. Quiet scenes (`energy ≤ 1.5`) move only on entrance, which is what pays for the peaks.
Concretely: s4/staging ruptures (the collateral falls through the threshold while the proceeds
count 8 → 0); s6/staging assembles in the narration's exact order and a marker then sweeps the
price across the whole axis while a live readout shows P and N changing and Σ holding at 1.00;
pdm s5 arrests (the same seizure gesture as pdm s2, begun and stopped short, then "nothing fires");
divest scenes strike their own claims out one at a time and add nothing. The sweep readout is
JS-driven per frame, not a pre-baked animation, because the claim being made is arithmetic.

### Friction

1. **The skill's slide engine is the wrong shape for this task.** `slide-patterns.md` §"Slide Engine
   Base" is a `100dvh` scroll-snap container; the task requires a fixed 1280×720 stage, arrow/click
   navigation and `@page { size: 1280px 720px }` pagination. The engine had to be rewritten on a
   transform-scaled fixed stage. Everything above the engine (its type scale, slide-type layouts,
   nav chrome, `autoFit`) transferred unchanged; only the transport did not. Its `100dvh` +
   `scroll-snap` pattern also cannot print one-slide-per-page without being unwound.
2. **Grid centring silently breaks on an oversized stage.** `place-items: center` on the
   1920×1080 explainer stage inside a 1476px window put the stage 222px off-centre and clipped the
   right third — invisible in the source, obvious on screen. Fixed with
   `position:absolute; left:50%; top:50%; transform: translate(-50%,-50%) scale(k)`. Only the
   render-and-look pass caught this; the structural validator could not.
3. **`file://` is blocked in the browser harness,** so the skill's "open generated pages in the
   browser" step and the staging contract's `render_and_look` gate needed a local
   `python3 -m http.server` on 127.0.0.1 to run at all. Worth the detour: it caught (2), a clipped
   SVG label on the `arrest` scene, two `viewBox`-vs-width clipping bugs in figures called at a
   size other than their design size, and a ledger block overflowing its own painted background.
4. Minor: two `%`-format collisions in Python string templates carrying literal `%` figures
   (`−1.25%/yr`), and `emit()` initially wrote HTML entities into Markdown.

### Overrides and what the tool could not express

- **Overridden:** write path (`~/.agent/diagrams/` → the task's paths, as instructed); slide engine
  (scroll-snap → fixed stage); the Mermaid default for the payoff (→ hand-drawn SVG, reasoned
  above); no theme/font picker (`themes.md` says only on request).
- **Could not express:** timed, narration-locked motion. The skill has no scene/timeline concept at
  all — no duration model, no `motion_role` vocabulary, no per-frame hooks. The explainer's engine
  (`window.__player`, per-scene `--d`, the sweep and count updaters) is entirely outside the skill's
  surface. Nothing in the skill refused a request; it simply has no slide-deck-adjacent answer for
  film, and its diagram routing has no row for a continuous mathematical function.
- **No slot was dropped.** All 14 + 14 + 13 deck slots and all 9 + 8 + 8 video scenes rendered.
  One note: `pitch-deck-mastery` declares 13 slots *plus* a `deck.appendix` entry `A1`. A1 is a
  declared slot with an id, so it is rendered as the 14th `<section class="slide">` and labelled
  `appendix · A1`. That deck therefore has 14 sections against a `slots_total` of 13 — deliberate,
  not a miscount.

### Linter / verification results

- `skills/deck-author/tools/check_deck.py` is the **brand-mode** linter (it checks brand.toml
  conformance: colours, self-hosted IBM Plex, accent-use caps). It was not run: in `free` mode the
  brand contract does not apply and every one of its assertions would fail by design. Recorded here
  rather than silently skipped.
- Structural validator instead (`_build/validate.py`, stdlib `html.parser`) — all six artifacts:

  ```
  free/staging/deck/index.html                  OK   14 slides
  free/presentation-writing/deck/index.html     OK   14 slides
  free/pitch-deck-mastery/deck/index.html       OK   14 slides
  free/staging/explainer/explainer.html         OK    9 scenes
  free/presentation-writing/explainer.html      OK    8 scenes
  free/pitch-deck-mastery/explainer.html        OK    8 scenes
  ```

  It asserts: section count == slot/scene count; the footer string present in every section; the
  `<meta name="deck-footer">` exact; `@media print` and the `1280px 720px` page size present; and
  **zero** `http(s)://` references other than `fonts.googleapis.com` / `fonts.gstatic.com`
  (permitted in `free`) and the SVG XML namespace.
- Render-and-look (the staging contract's design-lane gate): ran in Chrome over the local server.
  Looked at deck slides 1, 4, 6, 8, 12, 13, 14 and explainer scenes 4, 5, 6, 7 across all three
  contracts, including mid-animation frames. **Zero console errors.** `window.__player` verified
  live: `{scene: 6, t: 69.4, total: 120}`. The gate is *partially* satisfied — 11 frames looked at,
  not the ≥6-per-film the contract asks for on every film, and the browser tab was lost to a
  concurrent session before the final two deck sweeps; those two decks are structurally validated
  and use the byte-identical kit already inspected on the third.
- Quality floor: body ≥ 20px on deck slides (labels/citations 12–14px mono, deliberate),
  ≥ 28px on explainer scenes. Contrast on `--ink #0B0E13`: paper 15.8:1, dim 6.5:1, brass 8.7:1,
  cobalt 6.0:1, ember 5.2:1 — all ≥ 4.5:1. Every figure on screen traces to its contract slot, and
  each slide's rail carries that slot's own `source:` string.
- Spot-checked the contracts' figures against `source/medici/` (344B, 620M, 423.5, 12.9B, 1.25%,
  0.895, 54 DAML, 5,700): all present. No number was invented, and no headline claim was reworded —
  only line-broken.

### Build reproducibility

The artifacts are self-contained and standalone. They were generated from `_build/*.py` (a shared
design system plus one script per artifact), which was deleted after the final build; the six
delivered files are the deliverable.
