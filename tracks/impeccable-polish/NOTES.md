# impeccable-polish — contender notes

Contender `impeccable-polish`: the **baseline + polish** arm. Nothing here is built from
scratch. The finished `tracks/html-ppt/brand/` artifacts are copied verbatim and impeccable
v4.0.4's refine commands are run on top of them.

Tool: `/Users/iholsman/jojig/Lending/rwa-bakeoff/skills/design/impeccable/skills/impeccable/SKILL.md`

---

## brand

**Time spent: ~17 min wall clock**, end to end (copy → context → inspect → fix → confirm →
notes). Roughly 4 min inspection, 5 min authoring the fix batch, 5 min render/confirm, 3 min
notes. All six artifacts move together because the baseline's CSS is byte-identical across the
three decks and across the three explainers (only `<title>` and the `description` meta differ),
so a single patch is a six-artifact patch.

### Process as actually run

1. Copied `tracks/html-ppt/brand/{staging,presentation-writing,pitch-deck-mastery}/` into
   `tracks/impeccable-polish/brand/`. No sibling font files exist to copy — the baseline
   base64-embeds IBM Plex Sans + Mono directly (3 `@font-face` blocks, ~78KB of the 120KB file).
2. `scripts/context.mjs` from the track root. It returned `NO_PRODUCT_MD` /
   `PRODUCT_INIT_REQUIRED` (no PRODUCT.md, no DESIGN.md) and, per its own routing, a scoped
   refinement against existing code **proceeds using the code as context** rather than blocking
   on `init`. It also emitted `MANUAL_DETECTOR_REQUIRED` (no hook active) and told me to run
   `detect.mjs` once over the changed targets. `hasVisualImplementation: false` is a false
   negative — it does not recognise self-contained HTML decks as a visual implementation.
3. `reference/polish.md` for all six artifacts; `reference/animate.md` additionally for the
   three explainers; `reference/craft-floor.md` loaded immediately before the first edit.
4. `detect.mjs --json` over all six — **before**.
5. Inspection round: read the shared CSS + the slide/scene markup + the player JS, ran the
   deck linter, and rendered slides through headless Chrome
   (`--headless --screenshot --window-size=1280,720`, and 1920×1080 with `?scene=N&still=T` for
   the explainer). No puppeteer/playwright is installed, but `/Applications/Google Chrome.app`
   is, and the artifacts are `file://`-loadable, so this was a real render pass, not a source read.
6. One batched fix — **227 substitutions across 6 files**, applied by a single script where
   every replacement asserts its expected hit count so nothing silently no-ops.
7. One confirm round: re-rendered, found two defects only the render shows, fixed those
   (12 substitutions + 7 SVG rail insets), re-ran detector + linter. Stopped there, per the
   skill's bounded-passes ceiling.

### detect.mjs — before / after

| | before | after |
|---|---|---|
| total findings | **30** | **3** |
| `side-tab` (slop, warning) | 24 | **0** |
| `layout-transition` (quality, warning) | 3 | **0** |
| `em-dash-overuse` (slop, advisory) | 3 | 3 — *unfixable, see below* |

Per artifact, before → after: each deck 6 → 1, each explainer 4 → 0.

### Linter — `check_deck.py`

All three decks **PASS, rc=0, before and after, with the identical 3 notices**
(`C-PURE-BLACK`, `C-PURE-WHITE` — both the brand's own pins — and `P-DECKMD-COUNT`, no
`deck.md` beside the deck). Polish neither introduced nor cleared a linter finding; that was
the intent. 14 slides each, `footer class external`, 0 images, contract present.

### Preservation proof

Copy, slot order, headline claims and durations are not "believed" preserved, they are checked:
stripping every tag from the stage region and comparing to the baseline gives
**`COPY OK` on all six** (6738 / 6854 / 7128 chars of deck copy, 790 / 879 / 1044 of explainer
copy), and the sorted list of every `<text>` label inside the figures is **`FIGTEXT OK` on all
six** (5–57 labels each). Slide/scene element counts are unchanged. All three `SCRIPT.md` files
are byte-identical (`cmp` clean) — no scene duration or VO line moved. Brand pins verified
present after the edit: `#000000`, `'IBM Plex Sans'`, `data:font/woff2;base64`. Zero remote
refs in any file.

---

### Per-artifact before/after diff summary

Line counts are `diff` on 120-col-folded files, so the base64 font blob does not dominate.

#### All three DECKS — `<m>/deck/index.html` (~137 changed lines each; 36 asserted edits + 4 confirm edits)

| # | What polish found | What changed | Why |
|---|---|---|---|
| 1 | **24 detector `side-tab` hits.** `.card-accent/.card-bad/.card-good` and `.quote` each carried a 3px coloured `border-left` | 3px rail → **1px tinted hairline on the whole card + a faint wash of its own hue**; `.quote` → 1px | craft-floor bans a coloured side border above 1px. The replacement is not invented: `.pill-accent/.pill-good/.pill-bad` in the same file **already** use exactly this `rgba(hue,…)` idiom. polish.md §1 classifies this as *one-off implementation* — the fix is to route it through the pattern the system already owns, so the file now has one semantic-colour idiom instead of two. Colour meaning (accent / good / bad) is untouched. |
| 2 | **`layout-transition`**: the progress fill animated `width` | `transform:scaleX()` + `transform-origin:0 50%` + `will-change`, and the JS writes `scaleX(n)` instead of a `%` width | animating `width` re-lays-out the stage on every slide step |
| 3 | **Inactive slides stayed in the accessibility tree** — 14 slides were `opacity:0` only, so a screen reader read all 14 at once behind the live one | added `visibility:hidden` + `visibility:visible` on `.is-active`, with a delayed `visibility` transition so the fade still plays; `visibility:visible!important` added to the print block | polish.md §5 "focus, semantics, screen-reader names". This is the single highest-value defect found and the detector cannot see it |
| 4 | **The mandated confidentiality footer ran at 3.4:1** (`#666666` `text_muted`, 11px) — under the 4.5:1 floor, on the one string the brief requires on every slide | new `--text-chrome:#8A8A8A` token (**6.1:1**), applied to the footer, the slide counter, the header eyebrow, and the print footer; footer 11px → 12px | see *Brand fights* below |
| 5 | **28 SVG figure labels drawn at `fill="#666666"`** — 3.4:1, several at 14–15px | all → `#8A8A8A` | the detector never looks inside `<svg>`; these are axis labels and captions carrying real figures |
| 6 | **The presenter key legend was `#2E2E2E` on black — 1.6:1, effectively invisible**, i.e. a dead state | raised to `--text-3`, then made to announce itself and fade after 2.4s (`body.hint-on`), re-showing on mousemove | fixing the contrast **exposed** that the legend sat directly on top of the footer at 1280×720 (no letterbox at native size). Caught in the confirm render, not the source read. The auto-hide resolves the collision *and* the dead state |
| 7 | **No spacing scale.** The file carried 18 / 22 / 26 / 34 / 15 / 14 / 9 / 7 / 6 px with nothing behind them | a real `--sp-1…--sp-12` 4px scale, and **21 declarations** snapped onto it (grid gap, split gap, card / stat / pill / table padding, all six `mt-*`/`mb-*` utilities, dash-list rhythm, `.vs`, `.steps`) | craft-floor "read the computed values"; polish.md "align to the project's grid and spacing scale" |
| 8 | **Type scale had a 1px step**: `h3` 19px against an 18px body | `h3` → 21px (`line-height` 1.3 → 1.28), `h4` 15 → 16px, `.steps h3` 17 → 18px, `.stat .num` 27 → 28px | "obvious scale and weight steps". Ladder is now 46 / 34 / 21 / 18 / 16 / 14, all inside the brand's §10.3 ranges |
| 9 | **Proximity error on every content slide.** The section label (`.kicker`) sat **8px** under the header rule and **16px** above its own headline — so it grouped with the header, not with the headline it labels | slide top padding 48 → 60px and a scoped `.slide>.kicker{margin-bottom:var(--sp-2)}` → now **20px above, 8px below** | craft-floor "tight groups, generous separation". Found in the render; invisible when reading CSS. Vertical cost is +4px net, and every slide had 100px+ of slack |
| 10 | **Optically crooked frame**: header inset 22px, footer inset 20px | both → 24px | |
| 11 | **`.g1` was used in markup but never defined in CSS** (2 of 3 decks) | `.g1{grid-template-columns:1fr}` added | it silently fell back to the `.grid` default. Right result, no rule behind it |
| 12 | **Brand §9.3 pins a `:focus-visible` ring** (2px Electric Blue, 2px offset). The baseline shipped **no focus treatment at all** | added | a brand pin the incumbent simply omitted |
| 13 | Motion easing was `cubic-bezier(0,0,.2,1)`; the figure stroke draw was the one hard-coded `.9s` | ease → `cubic-bezier(.16,1,.3,1)`; new `--anim-draw` and `--anim-exit` tokens | see *Brand fights* |
| 14 | Six declared-and-never-referenced tokens: `--ease`, `--grad`, `--grad-soft`, `--shadow-lg`, `--radius-lg`, `--font-serif` | removed; the gradient **ban** survives as a comment | polish.md §4 "remove obsolete styles". A token nobody can reach documents nothing — the rule does |

#### All three EXPLAINERS — `<m>/explainer/explainer.html` (~131 changed lines each; 31 asserted edits + 7 SVG rail insets)

Everything in rows 1, 2, 5, 7, 8, 12, 13, 14 above applies here too (shared CSS). Additionally,
from `reference/animate.md`:

| # | What polish found | What changed | Why |
|---|---|---|---|
| 15 | **The detector cannot see inside `<svg>` — and the figures hand-draw the very tell it flags in CSS.** 7 rects of `width="6"` in Electric Blue / green: 6px side rails on figure cards | thinned to **2px**, then (confirm round) inset 16px past the parent card's `rx=14` corners and 1px inside its stroke, with `rx="1"` | same craft-floor rule as row 1. The confirm render showed the thinned 2px rail drawing a straight line across the rounded corners the 6px block had masked — a regression from my own fix, caught and closed in the confirm pass |
| 16 | **Scene changes were a hard cut** — `is-live` toggled `opacity`/`visibility` with no transition, which reads as a dropped frame on a screen recording | 200ms dissolve in, 140ms out (`--anim-exit`), `transition-delay:0` on the live scene | animate.md "preserve continuity through navigation"; "exit faster than entrance". **No scene duration is touched** — the player owns those and they still come from the contract's `vo_seconds` |
| 17 | **The film progress bar wrote `style.width` on every `requestAnimationFrame`** — a full-width layout pass per frame, on the artifact whose entire purpose is being screen-recorded | `transform:scaleX()` + `will-change` | the worst-placed instance of the same defect the detector flagged in the deck CSS |
| 18 | **The scene label popped in instantly while its own headline rose** — two arrivals in one scene | `.scene.is-live>.kicker,.scene.is-live>.eyebrow` now share the headline's `kf-fade-up` | one arrival per scene |
| 19 | **The footer (20px, 3.4:1) and the scene id (`#2E2E2E`, 1.6:1) were both bottom-anchored, 4px apart** — a visible misalignment of two elements on the same edge, one of them unreadable | both to a common `--sp-8` baseline; footer → `--text-chrome` (6.1:1), id → `--text-3` | alignment + contrast in one |
| 20 | `.scene .note` captions at 3.4:1 | → `--text-2` (11.6:1) | these are body text under the brief's own floor |
| 21 | `#FFFFFF` and `#101010` and `#000` hard-coded in `.fig-cost` / `.film-bar` / `.film-ticks`; duplicated `.scene .kicker` and `.scene .eyebrow` rules | tokenised and merged | |
| 22 | `prefers-reduced-motion` killed `animation` but not the new scene `transition`; the print block likewise | both now clear it | the reduced-motion path must stay complete after adding motion |

**What polish deliberately did NOT do to the explainers:** the baseline's figure choreography is
genuinely good — the collapse in `fig-rupture`, the arrested reach in `kf-arrest` ("an absence can
only be shown by a motion that does not complete"), the subtractive removal in `fig-cost`, the
sweep across every price. animate.md's test is "removing an animation would lose meaning". These
pass it. Rewriting them would be redesign wearing polish's clothes, which polish.md explicitly
forbids. Motion work here was confined to **quality** (easing, continuity, per-frame layout cost,
reduced-motion completeness), not to **authorship**.

---

### What polish could not improve without violating "refinement preserves"

1. **`em-dash-overuse` — 3 advisory findings, 22 / 27 / 29 em-dashes per deck. Left as-is.**
   Every one is in copy taken verbatim from the messaging contract. The only fix is rewriting
   sentences, which is the exact thing refinement may not do. This is the only detector finding
   still open, and it stays open on purpose.
2. **The kicker / eyebrow itself.** craft-floor is unusually absolute here: *"A kicker or eyebrow
   above a heading. This one is a ban, not a default: no brief earns it back."* Every content
   slide has one, plus a two-item header rule — **three labels stacked above one headline**. The
   craft answer is to delete the kicker and let the headline carry its own weight. That is copy
   removal, so it is out of bounds. I fixed the *consequence* instead (row 9: regroup it with its
   headline so it at least labels the right thing) and am flagging the cause here. **A from-scratch
   impeccable contender would not have shipped these; this arm cannot remove them.**
3. **One authored focal moment per deck.** craft-floor asks for "one authored moment, not …
   one identical entrance on every section". All 14 slides fire the same `anim-fade-up` +
   `anim-stagger-list`. Giving, say, the `$0` slide the entrance it has earned means
   re-choreographing individual slides — arguably still refinement, but it is per-slide authorship
   rather than a system fix, and polish.md's warning against adding "animation merely to make
   polish visible" plus the bounded-pass ceiling both point at leaving it. Recorded, not done.
4. **The `.vs` comparison blocks leave a large dead area** in the shorter of the two cards
   (`align-items:stretch` with unequal content — visible on staging slide 12). Fixing it means
   changing the comparison's layout concept, not its finish.
5. **Deck body text is 18px, the brief's exact floor**, with slides that have 100px+ of unused
   vertical space. There is room to move the whole scale up a step, and it would read better at
   the back of a room — but the brand pins body at 18–24px *and* a type-scale shift is a
   different composition, not a finish pass.

### Brand fights

Two, both resolved in favour of the craft floor, both recorded here rather than buried.

1. **Contrast vs. the pinned palette.** `brand.toml` gives exactly three neutrals:
   `text_primary #FFFFFF`, `text_secondary #AAAAAA`, `text_muted #666666`. `#666666` on the pinned
   `#000000` canvas is **3.4:1** — below the 4.5:1 body floor — and the baseline used it for the
   *mandated confidentiality footer*, the slide counter, and 28 SVG figure labels. `#AAAAAA` clears
   the floor but collapses the third step of the hierarchy into the second. So I added **one**
   value: `--text-chrome:#8A8A8A`, a pure neutral interpolated between the two pinned greys,
   **6.1:1**, which keeps a legible three-step ramp (`#FFFFFF` / `#AAAAAA` / `#8A8A8A`).
   This is the only colour added anywhere. No hue was introduced, the accent budget is untouched
   (the linter counts `.kicker`/`.accent` *elements*, not CSS), and all three decks still PASS.
   `text_muted` survives for genuinely non-content affordances (the dash-list bullet, the `vs`
   glyph, the presenter legend, the scene id).
2. **Motion easing.** Brand guide §9.1 names *"200ms `ease-in-out` for enter/exit"* and bans
   spring/bounce/overshoot. animate.md asks for *"natural deceleration such as
   `cubic-bezier(0.16, 1, 0.3, 1)`"*, and craft-floor for *"exponential ease-out from an
   already-visible default"*. I took `cubic-bezier(.16,1,.3,1)` at the pinned 200ms: it is a pure
   ease-out that **never exceeds 1**, so the no-overshoot ban is honoured literally, and the task
   brief lists motion easing as explicitly in scope while the pins it lists are true-black,
   Electric Blue ≤2/slide, IBM Plex self-hosted, and the footer. The guide's *named curve* is the
   thing I did not honour. Flagging it as a real, if narrow, deviation.

### Friction

1. **`context.mjs` mis-reads self-contained HTML decks.** It reported
   `hasVisualImplementation: false` and `PRODUCT_INIT_REQUIRED` against six complete, styled,
   scripted 120KB artifacts. Its own routing rescues the situation (a scoped command proceeds on
   the code as context and merely *offers* `init`), but the signal it hands you is wrong, and a
   more literal reading would have sent this run through `init` + `new-work` — i.e. a redesign,
   which is precisely what this arm must not do.
2. **`detect.mjs` is blind inside `<svg>`.** It found 24 CSS `border-left` side-tabs and zero of
   the 7 hand-drawn 6px side rails in the figures, which are the same anti-pattern in a different
   syntax. It also cannot see contrast, proximity, dead states, or a class used in markup but
   never defined in CSS — 6 of the ~14 defect classes fixed here. polish.md says it outright
   ("a detector result is defect evidence, not proof of quality"), and this run is a clean
   demonstration: the detector went 30 → 3, but the two highest-value fixes (the a11y tree, the
   footer contrast) and the two render-only fixes (the legend/footer collision, the kicker
   proximity) came from reading and looking, not from scanning.
3. **The polish/craft-floor pair has no vocabulary for "the ban costs copy".** craft-floor bans
   the eyebrow absolutely; polish.md forbids touching copy without asking. On this brief the two
   collide on every single slide and the skill offers no tiebreak, so the contradiction has to be
   escalated into notes rather than resolved. That is the right outcome for a refinement arm, but
   it is the tool's sharpest edge in this mode.
4. **Minor:** the fix batch had to be split deck-only vs explainer-only after the explainers
   turned out not to carry the `.vs` / `.steps` layout blocks, and two SVG rails had heights the
   first literal matcher missed. Both surfaced immediately because every replacement asserts its
   hit count — worth the extra strictness on a six-file simultaneous edit.

---

## free

**Time spent: ~38 min wall clock** (copy + `context.mjs` 2 min · batched inspection 14 min —
42 deck stills, 25 explainer freeze-frames, three in-browser computed-style audits, `detect.mjs`
· fix batch 9 min · confirm 10 min — re-render, pixel-diff, re-audit, structural checks · notes
3 min). One bounded pass: build → one batched inspection → one fix batch → one confirm. No loop.

### Process as actually run

1. Copied `tracks/html-ppt/free/{staging,presentation-writing,pitch-deck-mastery}/` verbatim
   (deck + explainer + SCRIPT.md; no sibling assets exist — all six artifacts are self-contained
   single files, Google Fonts the only remote ref).
2. `scripts/context.mjs` from the copied tree. Returned `NO_PRODUCT_MD` +
   `PRODUCT_INIT_REQUIRED` + `hasVisualImplementation: false` (it does not recognise
   `<style>`-inline single-file HTML as a visual implementation), and `MANUAL_DETECTOR_REQUIRED`.
   Per SKILL.md routing, a scoped refinement of existing code proceeds on the incumbent
   implementation; `init`/`new-work` deliberately not run — that path is redesign.
3. `reference/polish.md` on the three decks; `polish.md` + `reference/animate.md` on the three
   explainers. `reference/craft-floor.md` loaded before the first edit.
4. Inspection (one batched round, both stages together): `render.sh`-equivalent headless Chrome
   at exactly 1280×720 for all 42 deck slides, and the html-ppt agent's `?scene=N&at=<sec>`
   freeze-frame hook at 85% of each scene's duration for all 25 explainer scenes — both reused
   as instructed. Contact sheets read as sheets. Plus three scripted in-browser audits
   (WCAG contrast over resolved/composited backgrounds, stage overflow, per-pane content
   bounding boxes) and `detect.mjs`.
5. One fix batch, every replacement asserting its hit count. One confirm round.

### detect.mjs — before / after

| | before | after |
|---|---|---|
| **total findings (6 files)** | **52** | **16** |
| marquee | 12 | 0 |
| overused-font | 9 | 8 |
| gradient-text | 8 | 0 |
| em-dash-overuse | 6 | 6 |
| bounce-easing | 6 | 0 |
| dark-glow | 6 | 2 |
| layout-transition | 6 | 0 |

All 16 survivors are held deliberately — see "what polish could not improve" below.

### Before / after per artifact

Copy is provably untouched: a tags-stripped visible-text diff of all six HTML files **and** all
three SCRIPT.md against the current `html-ppt/free` source returns **0 differing lines**. Slot
order, scene order, headline claims, per-scene `data-dur` (= contract `vo_seconds`; 120 / 132 /
143 s totals), themes (swiss-grid / nord / pitch-deck-vc), and the footer string are unchanged.

**All six — dead vendored CSS removed (the largest single win).** The baseline inlines
html-ppt's whole `assets/animations/animations.css` (67 rules, 27 effects) into every artifact
while using 3–9 of them. Rebuilt the block per artifact from the effects each one actually
references (markup classes *and* the explainer player's runtime `'anim-'+data-anim` construction,
which a naive grep misses), keeping the `prefers-reduced-motion` guard:

| artifact | anim rules 67 → | effects kept | bytes |
|---|---|---|---|
| staging/deck | 26 | fade-up/down/left/right, rise-in, zoom-pop, blur-in, stagger-list, path-draw | −5,548 (−5.9%) |
| staging/explainer | 8 | fade-up/down/left, rise-in | −7,262 (−10.8%) |
| presentation-writing/deck | 22 | fade-up/down/right, rise-in, zoom-pop, stagger-list, path-draw | −5,736 (−6.1%) |
| presentation-writing/explainer | 8 | fade-up/down, rise-in, zoom-pop | −7,280 (−11.3%) |
| pitch-deck-mastery/deck | 18 | fade-up/down, rise-in, stagger-list, path-draw | −6,486 (−6.8%) |
| pitch-deck-mastery/explainer | 6 | fade-up/down, rise-in | −7,714 (−13.8%) |

Gone with it: marquee, shimmer-sweep, neon-glow, gradient-flow, confetti-burst, typewriter,
glitch, ken-burns, spotlight, ripple-reveal, morph-shape, parallax-tilt and the four 3D
flip/cube/page-turn/perspective effects — none reachable from any of the six artifacts.
**40,026 bytes removed in total; not one visible pixel of the settled design changed by it.**
Also removed: base.css's `.gradient-text` (defined in all six, used in none) and, from the three
explainers, base.css's `.progress-bar` pair — the explainers ship their own `.pbar` and never
create a `.progress-bar`, so those two rules were unreachable (and were the `layout-transition`
finding).

**All six — motion easing (5 changes).** `--ease` and `--anim-ease` were Material's
`cubic-bezier(.4,0,.2,1)`, an ease-**in**-out used for arrivals; animate.md asks for natural
deceleration on a confident arrival. Retimed to `cubic-bezier(.16,1,.3,1)` (exponential ease-out)
on the token, on the explainers' hard-coded `.scene` cross-fade, and on `.anim-zoom-pop`.
Durations untouched everywhere.

**staging + presentation-writing decks — bounce removed (2 changes).** `.anim-zoom-pop` ran
`cubic-bezier(.22,1.3,.36,1)` with a `scale(1.04)` overshoot at 60%. animate.md: "do not use
bounce or elastic curves by reflex." Rewritten as a clean `.72 → 1` ease-out. This is the only
change that alters what a mid-animation frame looks like, and it is the intended one.

**All three decks — progress bar (3 changes).** `transition: width` on `.progress-bar > span`
plus `barFill.style.width` in the runtime: a layout-driving property animated 14 times per
run-through. Now `transform: scaleX()` with `transform-origin:left`, compositor-only. Same
behaviour, same look (a 3-px sub-pixel rounding edge is the whole visual delta).

**pitch-deck-mastery deck + explainer — gradient text → solid (5 changes, ~11 elements).**
craft-floor's refuse list: "Gradient text. Emphasis comes from weight or size." The `.kicker`
rule set `-webkit-text-fill-color:transparent` and the template's later `color:` override could
not undo it, so every kicker (PROBLEM / SOLUTION / MECHANISM / …) rendered as gradient fill;
so did `.grad-text` ("never liquidate" 56 px, "$344B" 76 px) and the seven `.metric .n` figures
($12.9B, $840M+, 0, 5–10 bps, multi-sig, no token, no bridge). Now solid `--accent` (kickers)
and `--accent-2` (display), i.e. **5.09:1 and 5.06:1 where a transparent text-fill measured
nothing at all**. The gradient world itself is untouched — cover blob, ask-box, brand dot and
divider still carry it; only text fills went solid.

**presentation-writing deck — contrast (1 change).** `.kicker.rose` (15 px / 600, "What it costs
when it runs") measured **4.39:1** on `#14171d` — the one genuine sub-4.5:1 body-weight failure
in the whole corpus. Scoped a lighter tint of the same nord hue: `#c9757d`, **5.41:1**. Scoped
rather than retokenised so the display `$0` / `$116M` keep the deck's nord red.

**pitch-deck-mastery explainer — two render-only defects (2 changes).**
- s5: "no threshold on this axis" ran *behind* the P+N tile — measured overlap x 229–436 ×
  y 612–639, so the viewer read "…OLD ON THIS AXIS" for the whole 21-second scene. Its container
  was 400 px tall and the 155-px label stack hangs from the bottom, colliding with the 260-px
  tile. Container to 470 px: label fully clear, and the scene's dead lower third shrinks.
- s1/s2/s5/s8: `.posn` is a 300-px flex-centred tile with **zero padding**, so "a fund share ·
  a treasury · a bond" wrapped hard against both edges. Added `padding:0 30px`, `text-align:
  center`, `line-height:1.3`.

### Confirm round — structural + regression

- **Structural checks: all pass, all six artifacts.** 14 `<section class="slide">` per deck;
  `<meta name="deck-footer">` present once; the footer string on every slide and every scene;
  `@page{size:1280px 720px}` + `page-break-after:always`; ←/→ nav; 9/8/8 scenes with `data-dur`
  totals matching each contract's `vo_seconds` exactly; `window.__player {scene,t,total,seek}`;
  `?scene=N`, Space/→ and the `?at=` freeze hook all intact; SCRIPT.md covers every scene; no
  remote refs beyond fonts.googleapis / fonts.gstatic.
- **Contrast audit (in-browser, computed styles, alpha composited): 0 text failures** in all six,
  down from 1 real failure + a corpus of unmeasurable gradient-filled text. Stage-overflow: 0.
- **Pixel regression:** settled-state (20 s virtual time) diff of every changed deck against the
  current html-ppt source — staging and presentation-writing decks are **pixel-identical bar the
  3-px progress-bar rounding edge**; every pitch-deck-mastery delta sits exactly on a gradient-text
  bbox; the presentation-writing delta sits exactly on the rose kicker. The larger mid-animation
  diffs seen at 4 s virtual time resolve to zero at settle — they were the easing change itself.

### What polish could not improve without violating "refinement preserves"

The 16 surviving detector findings are all in this bucket. None is an oversight.

1. **`overused-font` × 8 — Inter.** Inter *is* the incumbent identity across all three themes
   (swiss-grid's Helvetica-substitute, nord's UI face, pitch-deck-vc's display face) and it is
   what every headline was letter-fitted and line-broken against. Swapping the typeface is
   replacing the visual world — redesign, not refinement — and it would reflow copy I am
   required to keep. Held. This is the one finding a from-scratch arm can fix and this arm cannot.
2. **`em-dash-overuse` × 6 (13–39 per file).** Entirely inside contract copy, which is verbatim
   and preserved. Not a design defect; a copy-editing note for the messaging layer.
3. **`dark-glow` × 2 — false positives.** `0 22px 50px rgba(59,91,255,.28)` (`.ask-box`) and
   `0 14px 40px rgba(20,25,60,.08)` (`.cardbox`) both carry a real offset and a soft blur on
   *light* pages — which is precisely what craft-floor's Depth check asks for. The detector reads
   any tinted shadow as a halo. Documented as an intentional exception, not changed.
4. **`.section-num` watermarks (pitch-deck-mastery, 8 slides).** `#f2f4fa` on white, 1.1:1 — and
   craft-floor separately refuses "section numbers (01/02/03)". They are a load-bearing element
   of the pitch-deck-vc identity, they carry no information a reader must decode, and darkening
   them would put them in competition with the headline. The only honest fixes are "delete" or
   "keep" and delete is a redesign call. Kept; flagged.
5. **The structural refuses.** craft-floor refuses same-size icon+heading+text card rows (the
   pitch deck's slots 3, 6, 11, 14 and the nord deck's slot 6) and the hero-metric template
   (nord slot 2's four-stat row, pitch slot 7). Fixing those means re-laying-out slots — the
   incumbent composition, and the thing refinement preserves. Named here, not touched.
6. **Explainer scene density.** Content fills 34–66% of the 1920×1080 stage and the sparsest
   scenes (staging s7 at 34%, pitch s7 at 34%, nord s8 at 34%) leave a genuinely dead lower
   third. The two honest fixes are more content (banned — no added facts) or a larger type scale
   (a real reflow risk against fixed line-breaks and a change of design intent). Only s5's
   container grew, because there the space was hiding an actual occlusion bug. Measured and
   logged rather than papered over.
7. **`kf-grown` / `kf-growp` / `kf-fadeout` animate `height`** in the explainers' split sequence —
   which animate.md warns about. Left as-is: that growth *is* the focal moment's meaning (P and N
   emerging from the whole), the segments carry centred labels that `scaleY` would distort, and
   the region is a single 250-px column. A correctness note, not a defect worth a distortion.

### Friction

1. **`context.mjs` mis-reads single-file HTML.** `hasVisualImplementation: false` and
   `PRODUCT_INIT_REQUIRED` on a tree of six complete, styled artifacts, because it looks for
   external CSS/tokens/components and finds inline `<style>`. SKILL.md's routing saves it — a
   scoped refinement proceeds on the code as context — but a literal reading sends a
   baseline-and-polish run into `init` + `new-work`, i.e. exactly the redesign this arm forbids.
   Same finding as the `brand` run; it reproduces on every artifact shape here.
2. **`detect.mjs` cannot see what mattered most.** It flagged 52 findings of which 36 lived in
   *dead* CSS that never rendered, and zero of the four defects a human would notice first: the
   occluded s5 label, the text touching the tile edges, the 4.39:1 kicker, and text with no
   measurable contrast at all because `-webkit-text-fill-color` made `color` inert. It is a
   source scanner; it has no renderer. polish.md says so ("a detector result is defect evidence,
   not proof of quality"), and this run is the demonstration: the detector's own headline number
   went 52 → 16, but everything that changed the *experience* came from screenshots and from
   scripted computed-style reads.
3. **"Refinement preserves" and craft-floor's refuse list contradict each other by design.**
   Gradient text, section numbers, card grids and the hero-metric template are all on the refuse
   list and all four are incumbent identity here. Only the first was resolvable (the gradient
   *world* survives; only the text fill went solid). The skill gives no tiebreak, so the other
   three become notes. Same edge the `brand` run hit on the eyebrow ban — it is the tool's
   sharpest edge in a refinement arm, and it shows up on every artifact that already has a
   point of view.
4. **The dead-CSS prune needed two attempts.** The first pass kept orphan `@keyframes` because
   the keyframe-reachability set was gathered from the pre-prune stylesheet rather than from the
   surviving rules — `kf-neon` survived and `dark-glow` stayed lit. Restored from source and
   redid it computing reachability from the kept rules only. Worth recording because the
   explainers reach their animation classes through a runtime `'anim-'+data-anim` string, so
   "unused" cannot be decided by grepping class attributes alone.
