## brand

Design contender `html-ppt` (lewislulu's html-ppt-skill), mode `brand`.
Session 2026-08-27, 18:37 → 19:12 local (~35 min wall clock, one agent).

### What was produced

| artifact | path | shape |
|---|---|---|
| deck × 3 | `brand/<m>/deck/index.html` | 14 / 14 / 14 slides, 1280×720 fixed stage, self-contained (117–118 KB each, fonts base64-inlined) |
| explainer × 3 | `brand/<m>/explainer/explainer.html` | 9 / 8 / 8 scenes, 120 s / 132 s / 143 s, 1920×1080 auto-playing stage (124–126 KB) |
| script × 3 | `brand/<m>/explainer/SCRIPT.md` | per-scene table + per-scene block: id, start, duration, on-screen text, VO verbatim, what moves |

`pitch-deck-mastery` renders 13 slots **plus** the contract's declared `appendix` A1, so its deck is 14 slides too. No slot, scene or supporting point was dropped — see "Slots" below.

### Time-to-artifact

The six artifacts come out of one generator, so per-artifact time is mostly shared:

- ~10 min — reading the three `staging.yaml` contracts, the brand guide §2/§3/§9/§10, `brand.toml`, `check_deck.py`'s rule table, and the skill (SKILL.md, base.css, animations.css, runtime.js, themes, single-page layouts, scripts).
- ~12 min — the shared brand kernel: token re-pin, geometry re-pin, trimmed runtime, deck generator, the 13-figure SVG library, the timeline player.
- ~4 / ~3 / ~3 min — the three contract content files (slot-by-slot placement + scene choreography + VO/what-moves rows).
- ~6 min — render-and-look: 42 deck PNGs, 14 explainer stills, three print-to-PDF runs, four fix cycles.
- Emitting all six artifacts from source is now **< 1 s** (`build.py`).

### The tool's process, as actually run

Followed the skill's own authoring rules ("always start from a template", "use tokens, not literal colors", "respect chrome slots", "keyboard-first", "one `.slide` per logical page", "notes go in `.notes`"):

1. **Step 2 — pick a theme.** Read `references/themes.md` and all 36 `assets/themes/*.css`. Chose **`tokyo-night`** as the base: it is the only dark theme whose accent is already blue (`#7aa2f7`) and whose structure is a plain `:root` token block with no decorative body rules (unlike `blueprint`'s grid background, `terminal-green`'s global text-shadow, `sharp-mono`'s uppercase headings). Nothing of tokyo-night's *values* survives — see the override cost.
2. **Step 3 — pick layouts.** Copied slide blocks out of `templates/single-page/`: `cover`, `kpi-grid` + `stat-highlight`, `comparison` (its `.vs` three-column split is used verbatim, re-tokenised), `pros-cons`, `table`, `big-quote`, `two-column`, `three-column`, `process-steps`, `cta`/`thanks`. **10 of 31** layouts. Each is re-tagged with the deck-author closed layout pool via `data-layout` (`L-COVER`, `L-STATEMENT`, `L-TWO-COL`, `L-TABLE`, `L-DIAGRAM`, `L-STAT-ROW`, `L-COMPARE`, `L-SEQUENCE`, `L-CLOSING`).
3. **Step 4 — animations.** `data-anim` classes from `assets/animations/animations.css`, kept as classes and re-triggered on slide/scene entry using `runtime.js`'s own loop (`remove('anim-'+a); void offsetWidth; add('anim-'+a)`), verbatim.
4. **Step 5 — full-deck templates: not used.** All 15 were read; each ships scoped `.tpl-<name>` CSS built around its own palette and type (`pitch-deck` is a light YC-style surface, `obsidian-claude-gradient` is gradient-led, `hermes-cyber-terminal` is neon). Re-skinning any of them to true-black + Electric Blue + IBM Plex would have meant deleting more of the template than survived. Composing from `templates/single-page/` — which the skill itself recommends first — was the cheaper honest path.
5. **Step 6 — render.** `scripts/render.sh` (headless Chrome) used for every look pass: 14 PNGs per deck × 3. Note: `render.sh` only `mkdir`s its output dir when the third argument is omitted — passing an explicit out-dir that doesn't exist yet makes Chrome fail silently while the script still prints `✔`. Created the dir first.
6. `scripts/new-deck.sh` was **not** used: it scaffolds `examples/<name>/index.html` inside the skill tree with relative `../../assets/...` links, and this task requires a self-contained file at a fixed output path. `scripts/verify-output/` is not a checker — it is a directory of reference PNGs.

### Brand mode: what the pinned brand cost

**Tokens.** `tokyo-night.css` declares 23 custom properties; **all 23 were replaced**, and 9 more added (`--surface-2` → `#060606` code surface, `--gold`, `--font-mono`, `--font-display`, `--font-serif`, `--letter-tight`, `--letter-normal`, `--anim-dur`, `--anim-ease`). So the theme layer is 100 % overridden — the theme contributed its *structure*, not one value. Against `base.css`'s 29 defaults the same holds. What genuinely survived is the skill's **primitive layer**: `.slide`/`.is-active`, `.kicker`, `.lede`, `.card`, `.pill`, `.stat`, `.grid/.g2/.g3`, `.divider-accent`, `.deck-header`, `.deck-footer`, `.notes`, `.progress-bar`, `.counter`. Every one of those reads tokens, so re-skinning cost exactly one `:root` block — the skill's token discipline is real and it paid.

**Type.** `--font-sans` was `'Inter','Noto Sans SC',…` and `--font-serif` `'Playfair Display'`. Replaced with self-hosted IBM Plex Sans (variable, `font-weight: 100 700`) and IBM Plex Mono (static 400 and 500 — the `fonts/NOTICE.md` silent-failure trap), **base64-inlined as `data:` URIs**; `--font-serif` is aliased to the sans because brand §3.4.1 forbids a serif/sans split. **No CDN link remains anywhere** (`assets/fonts.css`, which is a CDN `@import`, was not included).

**Type scale.** The skill's display scale (h1 72 px / weight 800, h2 54 px / 700) is outside brand §10.3 (headlines 36–48, sentence case, weight 600 max). Re-pinned to h1 46 / h2 34 / body 18 / data 16–20, all weight 600. This is the single largest visual departure from stock html-ppt: the deck is much quieter than any of its showcase decks.

**Motion.** Brand §9.1 ("minimal, functional, fast; no spring, no bounce, no overshoot; 150 ms hover / 200 ms enter-exit") kills most of the skill's motion library:

- **7 of 27** CSS animations survive: `fade-up`, `fade-down`, `fade-left`, `fade-right`, `rise-in`, `blur-in`, `path-draw` (+ `stagger-list`, which is `rise-in` sequenced). `--anim-dur` re-pinned `.7s → .2s`, `--anim-ease` to a pure ease-out, and the translate distances halved (32 px → 14 px) so a 200 ms move doesn't read as a jump.
- **20 of 27 cut, not re-timed**: `zoom-pop` (overshoot curve), `confetti-burst`, `neon-glow`, `shimmer-sweep`, `gradient-flow` (and `.gradient-text`; `brand.toml` sets `gradients = false`), `glitch-in`, `typewriter`, `kenburns`, `marquee-scroll`, `morph-shape`, `spotlight`, `ripple-reveal`, `parallax-tilt`, and all four 3-D moves (`card-flip-3d`, `cube-rotate-3d`, `page-turn-3d`, `perspective-zoom`).
- **All 20 canvas FX modules (`data-fx`) are unusable here**: particle-burst, confetti-cannon, firework, starfield, matrix-rain, galaxy-swirl, sparkle-trail, shockwave and the rest are decoration by construction, and the brief's explainer rule is "motion must carry meaning; no decoration-only animation". `fx-runtime.js` is not loaded.
- Declared reading: the 200 ms pin is applied to **entry** animations (a UI transition). The explainer's figure motion — a payoff curve drawing over 2.2 s, a price sweep over 4.4 s, a liquidation line reaching and stopping — is *diegetic*: it runs on the narration clock, not the UI clock. §9 does not have a rule for a 24-second scene; this is an interpretation, flagged here rather than buried.

**Colour.** `--shadow`/`--shadow-lg` → `none` (§4.4: depth from border contrast, never shadow), radii 18/12/26 → 12/8/16, `--grad` → `none`. Accent budget (`brand.toml: accent_budget = 2`) held by giving each slide one blue `.kicker` and at most one further blue element; on diagram slides the kicker drops to the grey `.eyebrow` so the chart's blue P-leg is the accent. Functional colour is functional only: blue = P leg, `#00CC66` = N leg, `#FF4444` = liquidation/seizure (brand §2.1/§2.3 assign exactly these).

**Marks.** Used `#oct-line` from `deck-skeleton-external.html` as the cover/closing watermark at `opacity:.05`, per `brand.toml [marks].usage`. Deliberately did **not** place the gold `#assay-mark`: it is the Assay shield, and these are Medici artifacts. Gold appears nowhere; it stays a mark-only colour.

**Geometry.** `base.css` gives `.deck{width:100vw;height:100vh}`. `check_deck.py`'s `H-GEOMETRY` requires the deck-author contract: a fixed 1280×720 board with a letterbox `scale()` transform, `@page{size:1280px 720px}` and one page per slide. Replaced the viewport-fluid stage with the fixed one; the skill's `.slide{position:absolute;inset:0}` satisfied two of the eight required patterns unchanged.

**Runtime.** `assets/runtime.js` is 960 lines and cannot be inlined as-is: its theme cycling (`T`) rewrites `#theme-link`'s `href`, its presenter mode (`S`) opens a popup that loads the deck file by URL with `?preview=N`, and `fx-runtime.js` loads `fx/*.js` — all of which need sibling files, which the "self-contained, no remote assets" rule forbids. Inlined a trimmed runtime that keeps the semantics the artifact can honour: `.is-active`/`.is-prev` toggling, `←/→/Space/PgUp/PgDn/Home/End`, click-to-advance, `#/N` deep links, the progress bar, the `data-anim` re-trigger loop and the `.counter` count-up (both lifted verbatim), `.notes` (N) and fullscreen (F). **Lost: presenter mode, theme cycling, the overview grid, canvas FX.** For an *offline external deck* that is the correct trade, but it is the skill's headline feature and it is gone.

### The explainer: what the tool does not have

html-ppt has **no timeline** — it is a keyboard deck engine. The auto-playing 1920×1080 player is written on top: a `requestAnimationFrame` clock, per-scene `data-dur` equal to the contract's `vo_seconds`, `?scene=N`, `Space`/`→` to advance, `←` back, `P` pause, `R` restart, a 4 px progress bar with per-scene ticks, and `window.__player = {scene, t, total, scenes, playing, sceneStart, seek(n), play(), pause()}` (`scene` 1-based; `t` and `total` in seconds). Scene *entry* uses the skill's `data-anim` classes; the meaning-bearing motion is a purpose-built SVG figure library (13 figures) driven by `.scene.is-live` keyframes, choreographed against each scene's `motion_role` / `energy` / `peak` / `motion_turn`:

- `assemble` scenes accumulate and never remove (the split, then the payoff, the flat top edge arriving last — the invariant is legible only as an accumulation that never breaks);
- `rupture` collapses a collateral column to a red floor in 0.55 s and does not recover; the cascade variant fells three columns in series and leaves dashed ghosts so the aftermath stays readable;
- `arrest` (pitch-deck-mastery s5) starts the same red gesture and **stops it dead at half height** for two seconds before it dims — an absence shown by a motion that does not complete;
- `divest` scenes are subtractive only: the N band, its label, the invariant edge and the P fill fade out one at a time until only P's bare declining curve and the drift number remain;
- `hold` scenes genuinely do not move (presentation-writing s4 has no figure at all — its contract lists `figures: []`, and that was honoured rather than filled).

A debug affordance was added for the render-and-look gate: `?still=<seconds>` freezes every animation at time *t* via `document.getAnimations()`. Headless Chrome's `--virtual-time-budget` does **not** advance CSS animation clocks, so without it every mid-animation screenshot comes back at t=0.

### Friction (top items)

1. **`check_deck.py`'s `PROCESS_LEAK` list contains `deck.md`, which matches every real source citation.** "canton-pitch-deck.md slide 2" — the exact provenance the audience is said to distrust the absence of — is a hard `ERROR`. Fixed by naming sources in prose ("Canton pitch deck, slide 2") rather than by filename; the citation is still on the slide. Worth reporting upstream: the rule cannot distinguish a leaked process artifact from a cited one.
2. **The skill's aesthetic is fundamentally a *light, large, loud* one.** 800-weight 72 px display type, gradient text, spring pops, 20 particle-canvas effects, `--shadow` on every card. A restrained institutional dark brand uses almost none of it; the intersection between "what html-ppt is for" and "what this brand permits" is the token system and the layout blocks, not the look.
3. **Self-containment costs the tool's best feature.** Presenter mode, theme cycling and the FX runtime all assume a deck that sits inside the skill tree with siblings. One inlined file cannot have them.
4. Minor: `render.sh` prints `✔` for screenshots Chrome never wrote (missing out-dir); `.slide{position:absolute}` had to be reset to `static` in `@media print` or all 14 slides print onto one page (Chrome only paginated after `.deck` was reset too).

### Linter results

`python3 skills/deck-author/tools/check_deck.py <deck>/index.html`, brand resolved to the shipped `brands/medici/brand.toml`, footer class **external**:

| deck | result |
|---|---|
| staging | **PASS** — 14 slides, 0 errors, 3 notices |
| presentation-writing | **PASS** — 14 slides, 0 errors, 3 notices |
| pitch-deck-mastery | **PASS** — 14 slides, 0 errors, 3 notices |

The three notices are the same on all decks: `C-PURE-BLACK` and `C-PURE-WHITE` (both are deliberate brand pins — §2.1 True Black canvas, §2.4 `#FFFFFF` text — and the skill's shipped `.deckcheck.json` carries a written reason for each; re-running with `--config skills/deck-author/.deckcheck.json` gives **PASS, 1 notice, 2 suppressed**), and `P-DECKMD-COUNT` (no `deck.md` beside the deck — the task's output contract does not include one, so story-parity is not checked).

Also run: `verify.py` (stdlib structural floor) — slide count == slot count, scene count == contract scene count, scene durations sum to the contract runtime exactly (120 / 132 / 143 s), footer visible on every slide, `window.__player` present, `?scene=` handled, no duplicate ids, **zero `http(s)` references in any of the six files**. All green. Print-to-PDF via headless Chrome: **14 pages per deck**, one slide per page.

Render-and-look: 42 deck PNGs (`scripts/render.sh`), 14 explainer stills at chosen mid-animation times, four defects found and fixed (nested-SVG label clipping in the combined mechanism figure; a threshold label whose baseline sat above the plot area; a cascade that left an empty frame after it collapsed; print pagination).

### Overrides and interpretations, stated

- Deck body text is 18 px (task floor) rather than the brand's 14 px default; §10.3's deck spec (18–24 px body) governs, which is what the brand intends for presentations.
- The only text below 4.5:1 contrast is the 11 px `#666666` confidentiality footer and the folio — both are the brand's own pinned legal-disclaimer treatment (§10.6 rule 1, §3.4 rule 6). No body text uses `#666666`.
- Explainer figure motion runs on the narration clock, not §9's 200 ms UI clock (argued above).
- `?still=<seconds>` is a debug parameter left in the shipped explainers; it is inert during normal playback.

### Slots

**Every slot and every scene in all three contracts is rendered, in contract order, with headline claims verbatim** (line-breaking only). Supporting points are placed into layout — as dash lists, stat rows, comparison cards or table rows — never edited, merged or dropped. Nothing was returned to staging.

Two placements worth naming:
- `pitch-deck-mastery` slot 4 carries an explicit `diagram:` instruction in the contract ("annotate the absence: mark where a lending market would draw its vertical liquidation threshold and show that no such line exists"). It is rendered as specified, and the same figure drives that contract's video scene 5.
- `pitch-deck-mastery`'s `appendix` A1 is rendered as slide 14 rather than dropped, since the contract declares it.

---

## free

Design contender `html-ppt` (lewislulu's html-ppt-skill), mode `free`.
Session 2026-08-27, 18:37 → 19:30 local (~55 min wall clock, one agent, no parallelism).

### What was produced

| artifact | path (under `tracks/html-ppt/free/`) | shape | time-to-artifact |
|---|---|---|---|
| deck · staging | `staging/deck/index.html` | 14 slots, 1280×720, 92 KB self-contained | ~13 min (first render 18:44; layout debug to 18:58) |
| deck · presentation-writing | `presentation-writing/deck/index.html` | 14 slots, 92 KB | ~8 min |
| deck · pitch-deck-mastery | `pitch-deck-mastery/deck/index.html` | 13 slots + appendix A1 = 14 sections, 93 KB | ~9 min |
| explainer · staging | `staging/explainer/{explainer.html,SCRIPT.md}` | 9 scenes, 120 s, 1920×1080, 66 KB | ~16 min (incl. building the player + the headless-capture workaround) |
| explainer · presentation-writing | `presentation-writing/explainer/…` | 8 scenes, 132 s, 63 KB | ~7 min |
| explainer · pitch-deck-mastery | `pitch-deck-mastery/explainer/…` | 8 scenes, 143 s, 55 KB | ~7 min |

Every artifact is a single file: `assets/base.css`, the chosen `assets/themes/*.css`,
`assets/animations/animations.css` and (for the decks) all 37 KB of `assets/runtime.js`
are inlined verbatim; the only network reference is one Google Fonts `<link>`
(Inter + IBM Plex Mono), which `free` mode permits.

### The tool's process, as actually run

The skill's own workflow is: **pick a theme → start from a full-deck template or copy
`<section class="slide">` blocks out of `templates/single-page/*.html` → add `data-anim`
→ include `runtime.js` → render with `scripts/render.sh`.** That is what was run, in that
order, with one deviation (below).

- **Read first:** `SKILL.md` in full, then `assets/base.css`, `assets/fonts.css`,
  `assets/animations/animations.css`, `assets/runtime.js` (skimmed for the nav/chrome
  contract), six theme files (`swiss-grid`, `editorial-serif`, `pitch-deck-vc`,
  `corporate-clean`, `midcentury`, `blueprint`, then `nord`, `tokyo-night`, `sharp-mono`,
  `japanese-minimal`, `academic-paper`, `arctic-cool` while choosing), and the full-deck
  template `templates/full-decks/pitch-deck/{index.html,style.css}`.
- **Layouts copied from `templates/single-page/`:** `cover.html` (d1 of every deck),
  `bullets.html` (card-list slots), `comparison.html` (the two-column "assumes vs is"
  slots), `stat-highlight.html` (the $620M / $0 / $344B slots), `kpi-grid.html`
  (the metric rows), `two-column.html`, `table.html` (the venue-comparison and payoff
  tables), `big-quote.html` (the RedStone quote slot), `cta.html`/`thanks.html` (ask and
  end). Their markup idioms — `.kicker`, `.h1/.h2`, `.card`, `.grid g2/g3/g4`,
  `.pill`, `.divider-accent`, `.deck-header/.deck-footer/.slide-number` — carried straight
  through; the deck-scoped CSS is a token override on top, never a replacement.
- **Full-deck template used:** `templates/full-decks/pitch-deck/` for the
  `pitch-deck-mastery` deck. Its scoped `.tpl-pitch-deck` rules are reused (palette,
  `.num-tag`, the 170 px `.section-num` watermark, `.metric`, `.ask-box`, `.cover-blob`),
  re-scaled where its 1920-era type sizes (`.h1` 86 px, `.slide{padding:88px 112px}`)
  overflowed a 1280×720 stage. `scripts/new-deck.sh` was **not** run: it scaffolds into the
  skill's own `examples/` directory with relative `<link>`s to `../assets/`, which is the
  opposite of the self-contained single file this task requires.
- **Animations used (`data-anim`, from `assets/animations/animations.css`):** `fade-up`,
  `fade-down`, `fade-left`, `fade-right`, `rise-in`, `zoom-pop`, `blur-in`, `path-draw`
  (on the payoff SVG), `stagger-list` (on the fact lists and metric rows). `runtime.js`
  re-triggers `[data-anim]` on every slide change, which is why the decks re-animate on
  back-navigation for free.
- **Scripts run:** `scripts/render.sh <deck> 14 <out-dir>` on all three decks, repeatedly
  (≈120 slide PNGs over the session) and reviewed as contact sheets. `scripts/render.sh` is
  the only executable the skill ships besides `new-deck.sh`; `scripts/verify-output/` is a
  directory of reference PNGs for the skill's own showcases, not a checker, so there was
  nothing else to run. A structural validator was written for this task (scene/slot counts,
  duration sums, per-slide footers, no non-font remote refs) — results below.

### Theme choice — one per messaging contender, and why

The task allows a different theme per contender, and the three contracts are arguing in
three different registers, so they got three:

| contender | theme | why |
|---|---|---|
| `staging` | **`swiss-grid`** | Its contract declares `lane: mixed(hall)` with a **read-fallback**: sparse slots, one idea each, every headline a complete sentence that stands without a narrator. `swiss-grid` is the only theme in the set built on that premise — a 12-column rule grid painted into `.slide`, zero radius, zero shadow, Helvetica-feel Inter, and a single `#d6001c` accent. The red is spent exactly three times in 14 slots: on the cover's "cannot be liquidated", on d6's `$0`, and on d14's closing rule. It reads like a printed sheet, which is what a forwarded artifact is. |
| `presentation-writing` | **`nord`** | Its contract is The Keynote — a spoken belief-shift where the bold moment is *watched* (the liquidation line is drawn on the payoff and then has nowhere to sit). A dark stage is where a drawn-and-removed line reads; `nord`'s muted frost/plum/rose avoids the neon register the audience "distrusts" (their word: unhedged enthusiasm). The payoff chart is the only bright object on the slide. |
| `pitch-deck-mastery` | **`pitch-deck-vc`** + full-deck template `pitch-deck` | Its contract *is* a 12-slide VC framework (problem/solution/mechanism/proof/timing/comparison/evidence/risk/commercial/close), so it was rendered in the skill's own pitch idiom, including the giant `.section-num` beat numerals that make the framework's spine visible. The gradient is rationed: cover headline, the `.ask-box` on slot 13, and the four `.metric` numerals — not on body text. |

### What the tool did with freedom

- **36 themes is the freedom.** Choosing a theme is choosing a whole argument's register
  in one line, and having all three decks share one `base.css` token vocabulary meant the
  same payoff-chart component (a generated SVG of `P = min(1, S/x)`, `N = 1 − P`) could be
  dropped into a white Swiss deck, a dark Nord film and a blue VC deck by overriding six
  `.pf-*` rules. That component is the brief's "one diagram they could redraw", and it is
  byte-identical geometry across all six artifacts.
- **`.notes` earned its keep.** The skill's speaker-notes slot (hidden by default, opened
  with `N`/`S`) turned out to be the right home for each contract's `transitions` block —
  the escalate/narrow/turn/fold/gate lines. They are presenter material, not slide content,
  and the skill's own authoring rule ("NEVER put presenter-only text on the slide itself")
  says exactly that. All 5 staging transitions and all 13 presentation-writing transitions
  are rendered this way rather than dropped.
- **The animation vocabulary is genuinely expressive at deck scale** — `path-draw` on the
  payoff SVG makes the P curve draw itself, `stagger-list` sequences the fact rows — but it
  is an *entry* vocabulary. See "what it could not express" for where that ran out.

### Overrides and deviations (all deliberate, all logged)

1. **Fixed 1280×720 / 1920×1080 stage.** `base.css` defines `.deck{width:100vw;height:100vh}`.
   The task requires a fixed stage, so `.deck`/`.film` are pinned to the design size and a
   ~15-line script scales them with `transform:scale(min(vw/1280, vh/720))`. Everything
   inside is unchanged, so the skill's layouts still lay out at their design size.
2. **Per-slide footers instead of `.deck-footer`.** `base.css` hides `.deck-footer` under
   `@media print`, and the task requires the footer visible on every slide *including* the
   printed page. Each slide carries its own `.slide-footer`; the validator counts 14 of them
   per deck.
3. **Own slide counter.** `runtime.js` updates only the *first* `.slide-number` in the
   document (`document.querySelector`), so 14 per-slide counters would all show slide 1's
   number. The per-slide counters use a different class (`.slide-no`) with static
   `data-n`/`data-t`, which is also what makes them correct in print.
4. **Click navigation added.** `runtime.js` ships arrows / space / hash / overview /
   presenter — but no click-to-advance, which the task requires. ~10 lines: click on the
   right 78% advances, left 22% goes back, right-click goes back.
5. **`.counter` (counter-up) removed after testing.** The skill's counter animation rewrites
   `textContent` from 0 up to `data-to`. On a fact-checked deck that is a hazard, and the
   headless renders proved it: slides caught mid-count showed **$296B** where the contract
   says $344B, **$530M** where it says $620M. Worse, in print (and on any slide never
   visited) the element renders as literal `0`. Every figure is now a literal. It also
   mis-rounds decimals (`toFixed(1)` turns −1.25 into −1.3), which would have been a
   fabricated number on slide 11.
6. **`color-mix()` replaced with `rgba()` in the chart fills.** `base.css` uses
   `color-mix(in srgb, …)` for `.pill-accent`; the same idiom in my chart rules fell back to
   **solid black** in the capture browser, which silently turned the payoff diagram into a
   black box in the first render pass. Explicit `rgba()` per theme.
7. **Specificity: `:where()` for the body-size floor.** The task's ≥18 px body floor was
   enforced with `.slide p{font-size:19px;line-height:1.5}`, whose 0-2-0 specificity beat
   every 0-1-0 utility class in the deck CSS — including `.num{line-height:.9}`, which made
   a 168 px `$0` sit in a 252 px line box and collide with the footer. Rewritten as
   `:where(.slide) :where(p,li,…)` (zero specificity) so component classes win.
8. **`.tpl-pitch-deck .slide > *{position:relative}`** in the full-deck template's `style.css`
   overrides `position:absolute` on any direct child — which silently un-anchored the header,
   the footer and the template's own `.cover-bg`/`.section-num`. Re-scoped with `:not(...)`.

### What the tool refused / could not express

- **The skill has no timeline.** `runtime.js` is a *slide* runtime: discrete states advanced
  by a keypress. The explainer's auto-playing clock, per-scene `vo_seconds`, `?scene=N`,
  the progress bar with scene ticks and `window.__player = {scene, t, total, seek(n)}` are
  ~90 lines written on top of it. The skill's contribution to the films is real but
  bounded: the token system, the theme, and `data-anim` as the *entry* gesture of each
  scene. Everything the brief calls "motion that carries meaning" — the rupture, the
  assemble, the arrest, the divest — is bespoke `@keyframes` keyed on `.is-live`, because
  `animations.css` has no vocabulary for *development within* a state, only for arrival
  into one. (`marquee-scroll`, `kenburns` and `neon-glow` loop, but a loop is decoration,
  which the brief forbids.)
- **`data-fx` canvas effects (20 modules) were not used.** Every one of them —
  `confetti-cannon`, `firework`, `matrix-rain`, `particle-burst` — is decoration-only, and
  the brief bans decoration-only animation. `knowledge-graph` and `data-stream` were
  considered for the Canton scene and rejected: they render no clause of any claim, which
  is the contracts' own `ornament_gate` test.
- **Presenter mode (`S`) is inert here.** It opens a popup that loads the deck by URL with
  `?preview=N`; from `file://` the popup is same-origin-ish but the `BroadcastChannel` name
  keys on `location.pathname`, and the feature is designed for a served deck. `N` (the notes
  drawer) works from `file://` and is the practical way to read the transition lines.
- **`T` (theme cycling) is dead by construction.** It swaps a `<link id="theme-link">` href;
  with the theme inlined there is nothing to swap. Left in rather than stripped — it
  no-ops silently because `data-themes` is absent.
- **Headless capture cannot see the films.** Diagnosed with a 12-line probe: under
  `--virtual-time-budget`, Chrome advances `performance.now()` (measured 6007 ms) but
  **not** the CSS animation clock (a 2 s-delayed animation had not started). Every
  first-pass film screenshot was therefore the un-animated frame. Fixed by adding a
  `?at=<seconds>` hook to the player that shifts every `animation-delay` by −t and pauses,
  rendering the exact frame deterministically. That hook is also `window.__player.freeze(t)`
  and is how the mid-animation frames below were captured. Worth flagging to the skill:
  `scripts/render.sh` has the same blind spot for any delayed animation in a normal deck.

### Checks run

- **`scripts/render.sh`** (the skill's headless-Chrome PNG export): 14 slides × 3 decks,
  re-run after each fix pass; reviewed as 2-up contact sheets. Final pass clean — no
  overflow, no footer collisions, no clipped charts.
- **Film frames:** 14 (staging) + 12 (presentation-writing) + 14 (pitch-deck-mastery)
  frames captured via `?scene=N&at=<sec>`, **including mid-animation** at the peaks —
  staging s4 at 2.8 s (fragments falling) and s6 at 3.2/9/15/22 s (the assemble accumulating);
  presentation-writing s6 at 13 s (the threshold line mid-hunt) and 21 s (unplaced);
  pitch-deck-mastery s2 at 6.6/12 s (the gesture completing) against s5 at 9.5/16 s (the
  same gesture arrested). Zero page errors in any render.
- **Structural validator** (python3, no puppeteer/playwright installed) — **all 66 checks
  pass**: slot count == contract slots (14/14/14); scene count == contract scenes (9/8/8);
  scene durations sum to exactly the contract runtimes (120.0 s / 132.0 s / 143.0 s);
  `.slide-footer` present on all 14 slides of each deck and `.film-foot` on every scene;
  the footer string `Medici — Proprietary & Confidential` present slots+1 times (slides +
  the `<meta name="deck-footer">`); `@media print { @page { size: 1280px 720px } }` present;
  keyboard and click nav present; `window.__player {scene, t, total, seek}` present;
  `?scene=N` and Space/→ overrides present; **no `http(s)://` reference anywhere except
  `fonts.googleapis.com` / `fonts.gstatic.com`**; SCRIPT.md row count == scene count with
  all six required columns.
- **Brand-mode linter (`check_deck.py`) not applicable** — it enforces the pinned house
  brand, which `free` mode is defined as not having. Not run, by design.
- **Legibility / contrast (manual, against the quality floor):** deck body 19–21 px,
  smallest visible deck text 15 px (source citations) / 14 px (footer + eyebrow chrome);
  film body 32 px, smallest visible film text 24 px (chart axis ticks) — all above the
  28 px floor for actual copy. Every theme's `--text-3` was darkened/lightened for AA:
  swiss-grid `#888888 → #6b6b6b` (5.0:1 on white), nord `#7b8394 → #a3aec2` (~6:1 on
  `#2e3440`), pitch-deck-vc `#8b93a8 → #6a7290` (4.6:1). Body text (`--text-2`) is ≥7:1 in
  all three.

### Slots rendered, and nothing dropped

All 14 `staging` slots, all 14 `presentation-writing` slots, and all 13 `pitch-deck-mastery`
slots **plus its declared `appendix` A1** (rendered as slide 14, not dropped) are present, in
contract order, with headline claims verbatim — line-broken only, never reworded. All 9 + 8 + 8
video scenes are rendered at their exact `vo_seconds`. **No slot or scene could not be
rendered.** Two contract instructions were followed literally rather than interpreted:

- `pitch-deck-mastery` slot 4's explicit `diagram:` spec ("Stacked, their top edge is one flat
  line at 1.00 across the whole width — that flat top is the invariant. Annotate the absence:
  mark where a lending market would draw its vertical liquidation threshold and show that no
  such line exists") is the generated payoff SVG, annotated exactly so; the same geometry
  drives `presentation-writing` video scene 6, where the annotation becomes the motion.
- `pitch-deck-mastery` video's "the same liquidation gesture is performed twice" is implemented
  as one `.arm` element with one shared entry keyframe: scene 2 runs it to completion and the
  collateral is dragged off-frame; scene 5 runs the identical element from the identical
  starting transform and stops it 150 px short, where it stays. Its `note_on_arrest_at_ceiling`
  ("the most CHARGED scene, and the second stillest") is why scene 5 has no other motion at all.

### Friction, ranked

1. **`--virtual-time-budget` freezing the CSS animation clock** — cost the most time (~15 min
   including the probe) and would have silently shipped an unverified film. Now mitigated by
   the `?at=` freeze hook, which is arguably a feature the skill should ship.
2. **The `.slide p` specificity trap** — one 0-2-0 rule quietly overrode `line-height` on
   every component class in the deck stylesheets and produced three separate "why is this
   element 200 px lower than its box" bugs before the cause was found.
3. **`base.css`'s `.slide{justify-content:center}` + absolute chrome** — vertically centring
   a slide whose content is taller than the box pushes the top of the content *up under* the
   absolutely-positioned header. Every dense slot hit it. Switched to `flex-start` with an
   explicit `.vc` opt-in for the cover and end slots.

Runner-up: the skill's `counter-up` and `color-mix` idioms both fail *silently* — one
producing wrong numbers, the other a black rectangle — and both were caught only because
every pass was screenshotted and looked at.
