
## brand

Contender `impeccable` (v4.0.4), mode `brand`. Run as a **new-work build in Persuade mode**.
All six artifacts complete. Wall clock 18:36–19:10 (~34 min), single session.

### Time to artifact

| Artifact | Elapsed | Notes |
|---|---|---|
| Reading (brief, 3 contracts, brand guide §2/3/9/10, brand.toml, skeleton, linter source) | ~6 min | The linter's *source* was read, not just `--help` — see friction 1. |
| `PRODUCT.md` | ~3 min | init.md, inferred-from-brief path, every fact labelled. |
| Direction roll + design system (the shared CSS + payoff/split SVG generators) | ~9 min | One system, reused by all six artifacts. |
| `staging/deck` | ~4 min | First deck; PASS on the first linter run. |
| `presentation-writing/deck` | ~3 min | |
| `pitch-deck-mastery/deck` | ~3 min | |
| Explainer player + 15-figure motion library | ~11 min | The expensive one. |
| `staging/explainer` + SCRIPT.md | +2 min | |
| `presentation-writing/explainer` + SCRIPT.md | +1 min | |
| `pitch-deck-mastery/explainer` + SCRIPT.md | +1 min | |
| Verify passes, fixes, re-verify | ~9 min | Two bounded rounds, per the skill's ceiling. |
| `DESIGN.md` | ~5 min | Written at finish, from the built world. |

### The tool's process, as actually run

| Step | What ran |
|---|---|
| Setup | `node .../scripts/context.mjs` from `tracks/impeccable/brand`. Returned `NO_PRODUCT_MD` + `PRODUCT_INIT_REQUIRED` + `MANUAL_DETECTOR_REQUIRED` + `AUTONOMY_DIRECTIVE_CHECK` + `SUBAGENT_AUTHORIZATION`. Run once, never re-run. |
| `reference/init.md` | Steps 1–4 followed; **step 3's interview was substituted** (see friction 2). `PRODUCT.md` written with every inferred fact labelled `[ASSUMED]` and the substitution disclosed at the top of the file. |
| `reference/new-work.md` | §1 (no incumbent world → the brief's pinned world), §2 (ask round → substituted, same reason), §3 "create or replace the visual world" — the rut named, seven grounded directions derived and ordered, then `node .../scripts/concept-seed.mjs --scope direction --mode persuade`. **Key `549e8b77`, ASSIGNED INDEX 6**, five catalog challengers dealt. §4 colour strategy = pinned. §5 direction contract written as an HTML comment, first child of `<body>`, in all six files. §6 build. §7 inspect + detector + this record + `DESIGN.md`. |
| `reference/craft-floor.md` | Loaded immediately before writing UI, as instructed. Its Verify list drove the contrast, spacing, type and motion checks; its Refuse list produced four brand collisions, all logged below and in `DESIGN.md` §6. |
| `reference/animate.md` | Loaded before the explainers. Its "find the job / set the motion thesis / choose material by meaning" sequence is what produced the per-`motion_role` treatment table; its easing guidance (`cubic-bezier(0.16,1,0.3,1)`, "do not use bounce or elastic by reflex") agreed with brand §9 and the built curve is `cubic-bezier(.22,.61,.36,1)`. |
| Detector | `node .../scripts/detect.mjs --json` over all six files, once, at finish (the hookless-build instruction). |
| House linter | `python3 skills/deck-author/tools/check_deck.py <deck>/index.html --quiet` on all three decks. |
| Bounded verify | Two rounds, per the skill's "build fully, inspect once, fix in one batch, confirm with at most one more round". |

**Not run, and why:** `serve-question.mjs` (needs a browser the sandbox has no display for);
`visualize.md` (no image generation available); the `impeccable-finish-reviewer` and
`impeccable-documenter` subagents — this contender is itself a subagent with the instruction
not to re-delegate its assignment, so **both passes were substituted in-thread**, which
`new-work.md` §7 requires be disclosed rather than done silently. `DESIGN.md` was therefore
written by this thread, from the built artifacts, not by the shipped documenter.

### The roll, and what it decided

The brand pins the *world* (true black, Electric Blue, IBM Plex, footer). It does not pin the
*organizing device*, so that is what the seed decided. Seven grounded directions from this
audience's own graphic traditions, ordered by resonance: payoff-diagram spine · term sheet ·
trade blotter · prospectus risk register · engineering GA sheet · **clearing-house circular
(6, assigned)** · terminal panel. Rut excluded up front: the dark VC deck and the giant-number
manifesto. Challengers dealt by the script (a VHS rental wall, a Busytown cutaway, an algorave
floor, a film cutting-bench select rail, a daylight section, a glazier's colour-field
partition) were all fused-and-weighed and all lost to the assignment on *product clarity*
against a pinned institutional brand — the cutting-bench rail came closest, and its "state is
a mark, not a hue" idea survives in the struck/vacated provision.

The device earns itself on this brief specifically: the audience's stated distrust is
*"numbers whose provenance is not named"*, and a circular makes provenance a **structural**
element — every slide carries an `AUTHORITY` line naming source deck and slide numbers, and
every clause is citable as `<notice>.<n>`.

### Brand fights — where impeccable's opinions collided with the pins

Impeccable's own top rule ("**The brief wins.** Honor pinned aesthetics… Redirecting a clear
brief toward your taste is failure") settled all of these in the brand's favour. Full table in
`brand/DESIGN.md` §6; the substance:

1. **Kicker/eyebrow.** `craft-floor.md` bans it outright — *"This one is a ban, not a default:
   no brief earns it back."* The house skeleton ships `.kicker` and §3.3 defines the level.
   **Brand wins** — kept as the notice masthead register, which is the form's identifier
   rather than a label above a heading. This is the sharpest collision in the run: a rule the
   tool explicitly declares unwinnable, overridden by the pin.
2. **Coloured `border-left`.** craft-floor refuses it above 1px and `detect.mjs` flags
   `side-tab` as *"the most recognizable tell of AI-generated UIs"*. The house skeleton ships
   `.quote{border-left:3px solid var(--blue)}`. **Brand wins, narrowly** — kept only on the one
   slide that carries a verbatim market quotation (`staging` notice 05), where a rule beside a
   blockquote is typographic convention. Stripped from the two decks that never quote, so it is
   not shipped as dead CSS. This is the one remaining hard detector finding, deliberately.
3. **IBM Plex.** `new-work.md` §4 names IBM Plex in its list of training-data default faces
   that "mean you stopped looking". §3.1/§3.2 pin IBM Plex Sans + Mono with a written rationale.
   **Brand wins without argument** — this is the case the "brief wins" rule exists for.
4. **True black.** craft-floor says pick light/dark from the use scene, and the house linter's
   own hint concedes universal dark-theme craft prefers a softened black. §2.1 pins `#000000`.
   **Brand wins** — `C-PURE-BLACK` / `C-PURE-WHITE` fire as notices and are correct to.
5. **Motion durations.** `animate.md`'s focal-entrance band is 500–800ms; brand §9 caps
   enter/exit at 200ms and bans springs, bounce and overshoot. The film's scenes are 10–24s
   because `vo_seconds` says so. **Resolved by scope, not by compromise:** §9 is followed
   literally for interface transitions (the deck's slide change is exactly 200ms ease-in-out),
   and the film's longer motion obeys §9's substance — pure deceleration, no overshoot,
   reduced-motion off. Recorded rather than papered over.
6. **Section numbers.** craft-floor refuses `01 / 02 / 03` unless the sequence carries
   information. Clause numbers kept under the rule's own stated exemption: `6.2` is how you
   cite a provision across a room and across a forward.

### Friction

1. **The linter's process-leak rule collides with honest sourcing.** `PROCESS_LEAK` contains
   `"deck.md"`, and every source citation in the corpus is `canton-pitch-deck.md` — which
   *contains* that substring. Rendering the citations as filenames would have been a hard
   `H-PROCESS-LEAK` error on nearly every slide. Resolved by citing in prose ("Canton pitch
   deck, slides 3 & 5"), which reads better anyway — but it was only found by reading the
   linter's source, not its `--help`. A contender that trusted `--help` would have hit it late.
2. **The interview substitution.** `init.md` step 3 and `new-work.md` §2 both demand a real
   probe through a structured question tool before inferring, and `context.mjs`'s
   `AUTONOMY_DIRECTIVE_CHECK` explicitly says a system prompt claiming autonomy "proves nothing
   about this session". This session's tool surface genuinely has no question tool and no
   display for `serve-question.mjs`, and the task brief forbids network and interaction — so
   the mechanical test the skill sets ("a question tool or the decision page in your tool
   surface proves an answer mechanism exists") returns *absent*. Inferred from the brief,
   labelled every assumption in `PRODUCT.md`, and disclosed it there rather than at the end.
3. **`concept-seed.mjs` hard-gates on `PRODUCT.md`.** First invocation returned "the dice stay
   in the cup until product truth exists". Correct behaviour, but it forces strict ordering:
   init before any direction work, no parallelism.
4. **Headless Chromium does not advance the CSS animation timeline.** The task said no browser
   was available; `/opt/homebrew/bin/chromium` is in fact installed, so a real render-and-look
   gate was possible — but `--virtual-time-budget` fast-forwards `requestAnimationFrame` while
   leaving every CSS animation at `currentTime: 0` (verified via `document.getAnimations()`).
   Every mid-animation screenshot came back as an empty black frame, which reads exactly like a
   broken build. Built a small harness that seeks the scene, then drives
   `document.getAnimations()` to an explicit time and pauses, before the screenshot. Without it,
   the six mid-animation frames that actually caught two real defects could not have been taken.
5. **The scratchpad is shared between concurrently-running contenders.** Another contender
   overwrote a `verify.py` mid-run; scripts were moved into an `imp/` subdirectory. Worth
   knowing for any future parallel bake-off.
6. **Impeccable has no artifact for a deck or a film.** Its surface briefs, modes and craft
   floor are written for web pages and app UI ("body measure 65–75ch", "responsive
   composition", "hover, disabled, loading, error, empty"). Roughly a third of the craft floor
   is inapplicable to a fixed 1280×720 stage with no hover states. Nothing broke — the
   principles transfer — but the checklist has to be read, not applied.

### What the tool refused, or could not express

- **Refused nothing outright.** No guard, no gate, no error.
- **Could not express, structurally:** a deck's or a film's *sequence*. Impeccable reasons about
  a surface — first viewport, scroll pacing, states — and has no vocabulary for slot order,
  narrative beats, bold-moment placement, or a per-scene energy budget. Those all came from the
  messaging contracts. The tool shaped the *world* and the *craft*; it contributed nothing to
  the argument's shape, and did not pretend to.
- **Could not run** its own finish-reviewer or documenter subagents here (see above), which is
  the part of its process most likely to have caught something a self-review misses.
- `visualize.md`'s three-composition approval round and the decision page were both unavailable;
  the skill says the visualize step "is proven to produce the most compositional and ambitious
  work", so this run shipped without the step it names as its own best lever.

### Verification actually run

- **House deck linter** — `check_deck.py --quiet`, all three decks: **PASS**. 14 slides each;
  brand `Medici` resolved from the shipped contract; footer class `external`; contract present.
  Three notices per deck, all expected: `C-PURE-BLACK` and `C-PURE-WHITE` (the brand's own pins,
  the linter's hint says so) and `P-DECKMD-COUNT` (no `deck.md` beside the deck — none was asked
  for; story parity unchecked).
- **Impeccable detector** — `detect.mjs --json`, all six files: 6 findings, 5 of them the
  advisory `em-dash-overuse` (mostly verbatim contract copy that may not be rewritten), 1 hard:
  the `side-tab` blockquote rule, kept deliberately per brand fight 2. Two findings were *fixed*
  rather than argued: the deck progress bar moved from `transition: width` to a `scaleX`
  transform (`layout-transition`), and the unused blockquote rule was stripped from the two
  decks that never quote.
- **Overflow probe** — every slide and every scene measured for `scrollHeight > clientHeight` in
  a real render: **zero overflow** across 42 slides and 25 scenes.
- **Structural gate** — slide count == contract slot count (14/14/14); scene count == contract
  scene count (9/8/8); runtime == contract `vo_seconds` sum exactly (120s / 132s / 143s);
  footer present on 9/9, 8/8, 8/8 scenes and on every slide; `window.__player.seek` exposed with
  `{scene, t, total, totalSeconds, seek}`; **zero page errors**; SCRIPT.md row count == scene
  count; zero `http(s)` references anywhere; every `url()` asset resolves to a local file.
- **Render and look** — 14 stills captured and inspected, including six mid-animation frames on
  the peak scenes. Two real defects were caught only by looking and then fixed: the vacated
  provision's 46px header column crushed "Liquidation threshold" under the italic body text, and
  the `strain` figure's threshold label overlapped the collateral rect's bottom edge.

### Slots and scenes: all rendered, none dropped

Every slot and every scene in all three contracts is on screen, in contract order, with the
headline claim verbatim (line-breaking only). Three things worth recording:

- **`pitch-deck-mastery` has 13 slots plus an `appendix` entry (A1).** It is rendered as
  Notice 14, labelled "Appendix A1", so nothing in the contract's deck lane is dropped. The
  deck therefore has 14 slides against 13 numbered slots.
- **`presentation-writing` slot 14** repeats slot 1's canonical sentence identically, as its
  contract requires; the authority line says so rather than inventing a source.
- **The contracts' known conflict is carried, not resolved**: 54 DAML templates / ~5,700 LOC and
  ~2,900 lines of regulatory analysis, per each contract's own stated source priority.

### If this were a real engagement

The two things missing are the ones the tool wanted and could not have: an actual human answer
to the init round (the `[ASSUMED]` labels in `PRODUCT.md` mark exactly what to confirm), and a
finish review by a reviewer that did not inherit this thread's framing.

## free

Design contender **impeccable** v4.0.4 (`skills/design/impeccable/skills/impeccable/SKILL.md`),
brand mode **free**, run 2026-08-27. Output root `tracks/impeccable/free/`.

### Time to artifact

Reconstructed from file mtimes; the session began at 18:38 (track dir creation).

| milestone | at | elapsed |
|---|---|---|
| read task, brief, three staging contracts, skill body + 6 references | 18:38 | — |
| `context.mjs` run, `PRODUCT.md` written (init flow) | 18:39 | 1 min |
| grounded seven-candidate derivation + `concept-seed.mjs` direction roll, challengers fused and weighed | 18:41 | 3 min |
| shared visual world authored (tokens, page ground, payoff geometry, deck component vocabulary) | 18:48 | 10 min |
| **3 decks** (42 slides total) first built and structurally green | 18:52 | 14 min |
| **3 explainers + 3 SCRIPT.md** (25 scenes total) first built and structurally green | 18:55 | 17 min |
| `detect.mjs` run once, mechanical findings fixed, rebuild | 18:56 | 18 min |
| finish review round 1 (fresh-context subagent, no forked history) | 19:02 | 24 min |
| `DESIGN.md` + `.impeccable/design.json` written from the built world | 19:03 | 25 min |
| review fix batch applied to all six artifacts, one rebuild | 19:17 | 39 min |
| verdict pass (same reviewer, scoring only) | 19:25 | 47 min |

Marginal cost per messaging contract was low because the three decks share one generated
stylesheet and component library, and the three explainers share another: roughly 4 min of
authored content per deck and 5 min per explainer on top of an 10-minute shared-world build.
That is an honest caveat on any per-artifact time comparison against a contender that hand-wrote
each file.

### The tool's process, as actually run

Commands and reference files actually used, in order:

1. `node .../scripts/context.mjs` (from `tracks/impeccable/free`) — returned `NO_PRODUCT_MD`,
   `PRODUCT_INIT_REQUIRED`, `MANUAL_DETECTOR_REQUIRED`, `AUTONOMY_DIRECTIVE_CHECK` and
   `SUBAGENT_AUTHORIZATION`. Followed all five directives. Run once, never re-run (as instructed).
2. `reference/init.md` — Steps 1–4 and the completion gate. **Step 3's interview could not run**
   (see Friction). PRODUCT.md written with an explicit substitution notice and every inferred fact
   labelled, per the reference's own fallback clause.
3. `reference/new-work.md` §1–§6. §3 "create or replace the visual world" in full: rut named, seven
   grounded candidates derived across seven material families, `concept-seed.mjs` run.
4. `node .../scripts/concept-seed.mjs --scope direction --mode persuade` → **seed key `275daa63`,
   ASSIGNED INDEX 7**, six catalog challengers dealt. Reproduced with
   `--from 275daa63 --candidate-count 7` to read the full challenger list.
5. `reference/craft-floor.md` — loaded immediately before writing any UI, as instructed.
6. `reference/animate.md` — loaded for the explainers; its motion thesis / material-by-meaning /
   timing table drove the per-scene motion.
7. `reference/overdrive.md` and `reference/delight.md` — read for the ceiling. See "ceiling" below.
8. `node .../scripts/detect.mjs --json <6 targets>` — the hookless build's one mandated mechanical
   pass. Run exactly once. Findings below.
9. `reference/degraded/finish-reviewer.md` — the finish review, run in a **fresh subagent with no
   forked history**, since the shipped `impeccable-finish-reviewer` agent type does not exist in
   this harness. Disclosed as a substitution.
10. `reference/degraded/documenter.md` — `DESIGN.md` (+ `.impeccable/design.json` sidecar) written
    from the built world at finish, ground truth over intention. Also run inline from the degraded
    reference, since the shipped `impeccable-documenter` agent type does not exist here.
11. Review fix batch applied in one pass, one rebuild, then the Verdict Pass re-dispatched — which
    did not return. See "The finish review" below.

Bounded verify passes: **structural only, no browser exists here.** A python3 `HTMLParser` check
(`slots == slot count`, `deck-footer` meta, footer text present in every section, 1280×720 and
1920×1080 stages, `@media print` with `size:1280px 720px`, `←/→` handlers, `window.__player`
surface, tag balance, no `http(s)://` refs outside `fonts.googleapis.com` / `fonts.gstatic.com`).
Two rounds, per the skill's ceiling; final round green on all six.

### What the tool did with freedom

Asked for a replacement visual world with no brand limits, the skill's machinery did three things
a plain "make it look good" would not have:

- **It refused my ranking.** `concept-seed.mjs` assigns which of your own grounded candidates gets
  built, explicitly so the top-ranked one — "what every run would ship" — does not. My honest
  resonance order was (1) the options-desk payoff sheet, (2) the bearer bond with its detachable
  coupon, (3) the custodian's settlement ledger, (4) the Bloomberg blotter, (5) BIS/ISOTYPE
  statistical print, (6) the exchange split-flap board, (7) the Medici *libro segreto* — the
  Florentine double-entry codex, which `new-work.md` caps at one candidate precisely because it is
  the brief's own name read literally. **The roll landed on 7.** I did not re-roll: the reference
  permits a re-roll only on named factual grounds, never taste, and the direction carries the
  product's truth better than my #1 did. Double-entry bookkeeping is the Medici bank's own
  instrument, and every entry in it has two sides that must balance — which is exactly what
  `P + N ≡ collateral` is. The payoff diagram (my #1) survives inside it as the page's main figure
  rather than as the whole world.
- **It forced the rendition away from the default.** `new-work.md` §4 names the measured prior
  outright: a codex world comes out cream, parchment, serif, lamplight — which is also the
  category-default "institutional finance broadsheet" this brief's rut list already excluded. So
  the world was rebuilt from the quattrocento's **saturated** materials instead: a levigated
  **lapis ultramarine** field (`#111D4A → #0A1230`), **gold leaf** for P, **vermilion/minium**
  rubrication for N, **verdigris** for the sum that holds, lead-point rulings at 28px. Colour
  strategy: Drenched. The lettering is the light on the page, which inverts a real manuscript and
  is the right inversion for a projected deck.
- **It made me choose faces like objects, not like categories.** The banned-defaults list in §4
  rules out IBM Plex, Space Grotesk, Inter-as-display, DM Serif, Fraunces, Cormorant and the rest.
  Chosen: **Cardo** (a humanist/Renaissance revival with real quattrocento texture) for display and
  body, **Alegreya Sans** (a book-companion humanist sans) for the clerk's hand — labels, figures,
  tabular numerals, chrome. Both Google Fonts, permitted in free mode.

Devices the world supplied that a generic deck would not have:

- **The balance rule.** In every payoff plate the stacked P and N are topped by one continuous
  verdigris rule at 1.00 that *draws itself across* — the ledger's "the columns must foot". The
  invariant is drawn, not asserted. It is the deck's one authored motion moment and the explainer's
  focal sequence. It opens the deck too: folio 1 draws the balance rather than typesetting the
  identity (a change the finish review forced — see below).
- **The catchword.** A codex prints the first words of the next page at the foot of the current one
  so the binder gets the order right. Every slide's bottom-right carries the next slide's
  catchword; the last reads `— explicit · here ends the account —`. It is the delight thesis and it
  is also functional: a presenter always knows what is next without leaving the page.
- **The illuminated folio.** A 96px ruled margin carrying nothing but the page number as a 54px
  gold-leaf Cardo numeral over `of 14` — foliation as the slide counter, section numbering that
  carries real information, which is the craft floor's own exemption. (In the first build this
  margin also carried the beat name and slot function; the reviewer correctly called that pair a
  kicker and it was deleted.)
- **The apparatus line** — a full-width row above the footrule pairing the source citation with the
  catchword. This is where the brief's "every figure traces to a source" requirement lives,
  structurally, on all 42 slides.
- **The balance table** for every comparison slot: two facing columns with a spine, headed like a
  ledger, with the conceded row set in vermilion rather than hidden.
- **The drawn paraph** — the rubricator's own mark, in vermilion and minium at the world's 2.5px
  stroke, standing where a generic quote-callout would put a coloured side stripe (which the craft
  floor refuses).

### The ceiling (overdrive / delight)

`overdrive.md` requires proposing 2–3 directions and getting a user pick before building anything
technically ambitious — impossible here (no question tool), so no WebGL/shader/particle work was
attempted; the reference's own rule is that skipping the proposal step "risks building something
embarrassing". What was taken from it instead is its actual thesis — that "extraordinary" is
context-dependent — and the extraordinary thing for a finance-literate room is not a shader, it is
**a payoff surface that assembles in the exact order of the narration and never breaks**. The
explainer's scene-6 assembly (staging) is that: split → axes → strike → P wipes in → N wipes in →
tether → the balance rule foots across, every element persisting, all driven from CSS custom
properties scaled to the contract's own `vo_seconds`.

`delight.md`'s test — "specific enough that a neighbouring product could not use it unchanged" — is
met by the catchword and by the refused-threshold animation, not by whimsy.

### Motion: how the contracts' video lanes were honoured

`animate.md` says motion must explain state and relationship, and the staging contract goes further
with `motion_role`, `energy`, `peak` and a `motion_budget` per scene. All 25 scenes were built to
their declared role, and the roles genuinely differ:

- `hold` — one fade, then absolute stillness (staging s1/s5/s7, pw s1/s4, pdm s1/s6). pw s4 has
  **no figure at all**, because its contract entry declares `figures: []`. It is 12 seconds of a
  claim on a bare ruled field, and it is the most disciplined moment in the three films.
- `accumulate` — a value grows across the scene (staging s2's 14-column climb; pw s3's self-feeding
  cascade; pdm s4's verdigris price marker sweeping the whole axis while the top edge stays flat).
- `strain` — an intact arrangement visibly fails to cope (the ruled stack compresses 28% and skews
  under a descending load; the sell arrow is turned back by the redemption window twice).
- `rupture` — three different ruptures for three different claims: staging s4 (the balance rule
  snaps, six gold blocks collapse, a 132px vermilion `$0` lands), pw s6 (the threshold is
  introduced and tries three positions on the axis and lands on none), pdm s2 (a price track
  crosses the marked line and the held plate is taken — flattened to 6% and desaturated).
- `assemble` — everything that arrives stays; reveal order follows the VO clause by clause.
- `arrest` — pdm s5 only: the identical gesture from s2 sweeps in, decelerates hard and **stops
  short**, then holds. The contract's own note ("the most CHARGED and the second stillest") was
  followed: it is capped at energy 4.0 and its scene is quieter than the ones around it.
- `divest` — motion is subtractive only. The N region leaves, then the grid, until P's decline
  stands alone; unbuilt claims are struck through one at a time. Nothing new enters.
- `cadence` — one gesture, then a dead stop, resolving the opening image.

Every animation delay is `calc(var(--d) * k)` where `--d` is the contract's own `vo_seconds` for
that scene, so the choreography is *derived from* the narration budget rather than fitted to it.
`prefers-reduced-motion` collapses all of it to the final composed frame.

### The finish review (the part of the skill that most changed the work)

`new-work.md` §7 ends every build with a review by a **fresh** reviewer that never inherits the
build thread. The shipped `impeccable-finish-reviewer` agent type does not exist in this harness, so
the role ran in a subagent spawned with no forked history from
`reference/degraded/finish-reviewer.md`. **Substitution disclosed.** It had no screenshots either —
it judged from markup, CSS and computed contrast, and named that limitation itself.

**Round 1 verdict: `disposition: fix`, eight material findings.** It was worth every token; five of
the eight are things I would not have caught by re-reading my own build:

1. **FIRST VIEWPORT contradicted.** My own direction contract promised "the P/N balance drawn
   beneath the claim" on folio 1, and folio 1 was shipping the 76px `P + N ≡ collateral` *seal* —
   the file's own **closing** device — with the drawn balance not appearing until folio 8. Fixed:
   all three covers now draw the payoff plate; the seal is closing-only.
2. **The pigment carrying the thesis was dead code.** `--verd` was declared as "the sum that holds",
   a `-verd` gradient was defined in every deck SVG, and neither was ever referenced; the balance
   rule — which *is* the total — was drawn in bone-white. Fixed: verdigris now strokes the balance
   rule and the footing's sum chip in both media; the unused gradient was deleted.
3. **A craft-floor ban I had shipped 42 times.** The margin's beat name (`the charge`, `common
   ground`) in 13px tracked uppercase vermilion beside a heading is a kicker, which the floor bans
   outright with no brief able to earn it back. I had convinced myself it was "the rubricator's
   margin". Deleted, with the slot-function label under it; the margin now carries an illuminated
   gold folio numeral instead.
4. **Build-time metadata was visible in the shipped deliverable.** The decks printed the contract's
   act names and slot functions; every explainer frame burned in `scene 4 / 9 · rupture · energy 5 ·
   peak`. On a deck that gets forwarded to a prospect. Removed; the explainer keeps a plain
   `scene N / M`. The progress bar and scene ticks were **kept deliberately** — the bake-off task
   names "a tiny progress bar" as a requirement — and that reason is stated rather than the element
   silently retained.
5. **Two real contrast failures** I had not measured: the word `source` above every citation at
   **1.74:1**, and the navigation hint at **2.37:1**. Both moved to `--ink-3` (~5.2:1).
6. **Type-size floor breaches on the text that carries provenance**: `.src` 12.5px, `.attrib` 16px,
   the cover's as-of line 14.5px, the plate's axis labels 13.5px, and — worst — the STORY's own
   punchline `no liquidation line fits here` at 14px, smaller than anything else on the plate. All
   raised past the 18px deck floor; the explainer's SVG figure labels went 21 → 30 viewBox units and
   several figure viewBoxes were widened so the larger type would not collide.
7. **An identical entrance on all 14 slides** (`settle`) — the exact thing `craft-floor.md` refuses.
   Deleted; the deck's only motion is now the plate inking and the balance rule footing across.
8. **A sweep**: the quote callout's gradient side stripe (two floor items at once) replaced with a
   drawn paraph mark; two rubric classes used in markup but never defined in CSS; a 104px display
   size over the 6rem ceiling; and ledger measure running ~100ch, capped to 75ch.

Everything was applied in one batch with a single rebuild, per the reference's own loop, then sent
back to the same reviewer for the scoring-only **Verdict Pass**.

**Round 2 (the Verdict Pass) did not return, and that is disclosed rather than papered over.**
The same reviewer role was re-spawned to score the eight fixes; it thrashed — it began re-deriving
its own SVG-id and contrast checks instead of scoring — and ran past its turn ceiling without
emitting the two-section verdict. `finish-reviewer.md` says a run that ends before its sections are
written returns nothing, and that is what happened. Rather than spend a third heavyweight agent, the
fix batch was **scored by the build thread against the shipped files**, which is weaker evidence
than a fresh reviewer and is labelled as such:

| # | fix | scored | evidence in the shipped files |
|---|---|---|---|
| 1 | drawn balance on fol. 1, seal moved off it | resolved | all three covers contain the payoff `<svg class="pf">`; no `class="seal"` in any folio 1 |
| 2 | verdigris draws the total | resolved | `stroke="var(--verd)"` ×3 per deck / ×5 per explainer; `.chip-sum` border verdigris; the `-verd` gradient no longer emitted anywhere |
| 3 | kicker pair deleted | resolved | no `class="beat"`, no `class="fn"`, no `.beat{` rule in any deck |
| 4 | build metadata off the shipped frame | resolved | no `energy N`, no role words, no act names or slot functions in any of the six; explainer `.meta` is `scene N / M` |
| 5 | contrast | resolved | `.src b` and `#hint` now `var(--ink-3)` (#7E8AB6, ~5.2:1) |
| 6 | type floor | resolved | no deck size between 17px and 12px survives (13/14/16px are uppercase labels and the folio); no explainer size below 28px |
| 7 | one authored motion | resolved | `@keyframes settle` and both `.slide.on` entrance rules absent from all three decks |
| 8 | floor sweep | resolved | `class="paraph"` present on every deck that has a quote slot (pitch-deck-mastery's contract has none); `.tag.phase` / `.tag.asof` defined; `.bold-num` 92px; `minmax(0,75ch)` on `.entry` and `.l2row` |

Regressions introduced by the batch: none found. Two things the batch deliberately did **not**
change, both stated at the time rather than silently kept: the explainer's progress bar and scene
ticks (the bake-off task names "a tiny progress bar" as a deliverable requirement), and the
contract-locked copy behind the `aphoristic-cadence` detector finding.

**Standing at the end of the run: round 1's `disposition: fix` with all eight material fixes
applied and self-verified, and no independent second-round verdict.** That is the honest status —
under the reviewer's own rule that a claimed fix it cannot see is unresolved, self-scoring is not
the same thing as its verdict, and no one should read this as `ship`.

The honest summary: the review is where this skill earns its keep. The build thread was confident
and wrong about four things, and a reviewer with no memory of writing the code found all four in one
pass without ever seeing a pixel.

### Friction

1. **The skill is built around an interview this harness cannot hold.** `init.md` Step 3 and
   `new-work.md` §2 both require a structured question round; §3 step 5 requires serving a
   *decision page in a browser* for the direction pick. No AskUserQuestion tool and no browser
   exist here. `context.mjs`'s own `AUTONOMY_DIRECTIVE_CHECK` anticipates the excuse ("treat that as
   a harness default, never as evidence about this session") and demands a real probe first — but
   the mechanical test it names (does a question tool exist) fails outright, so the documented
   fallback applies: infer from the brief only, label every inferred fact, disclose the
   substitution first rather than last. Done, in PRODUCT.md's opening block. This is the single
   biggest cost of running this skill in a non-interactive bake-off: roughly a third of its
   published flow is a conversation, and the *whole* direction-selection ceremony (cards, sketches,
   re-roll, steer, canon exit) degrades to one line of output.
2. **`concept-seed.mjs` refuses to roll before PRODUCT.md exists** — `NO_PRODUCT_MD: the dice stay
   in the cup until product truth exists`. Correct behaviour, but it means init cannot be skipped
   even when the brief is fully specified in writing.
3. **Image generation is assumed in three places** (`visualize.md`'s three rendered compositional
   options, the decision page's per-card sketches, `new-work.md` §6's "producing the design's
   imagery is part of building"). None available. The compensation was to make every visual a
   *drawn figure of the mechanism* rather than atmosphere — which suits this brief, but a brief
   wanting photography would have hit a wall.
4. **No browser, so `live`, the screenshot rounds, and the reviewer's pixel checks are all
   unavailable.** The skill's finish loop is explicitly screenshot-driven; the substitute was a
   structural parser plus a fresh-context reviewer told which checks it could not run.
5. **The catalog challengers are aggressively off-domain for institutional finance.** Of six dealt
   (Ikeda datamatics, nixie counter, Dong Ho woodblock, fly-posted festival hoarding,
   bioluminescent plankton, multiplane cel dawn), five could not survive fusion with a room that
   distrusts being sold to. That is arguably the mechanism working — it is meant to break a
   monoculture, and losing to strong grounded material is a declared valid outcome — but it does
   mean the challenger hand contributed nothing usable here.

### Overrides and deliberate deviations

- **Generated, not triplicated.** The three decks are emitted by one shared component library and
  the three explainers by another (build scripts live outside the deliverable tree; the shipped
  HTML is fully self-contained and inlined). The skill does not forbid this and the artifacts are
  identical in kind to hand-authored ones, but it is a process deviation worth declaring, and it is
  why per-contract time is not comparable to a hand-written contender.
- **`pitch-deck-mastery` appendix A1 rendered as folio 14** rather than dropped. Its contract lists
  13 `slots` plus a separate `appendix:` block; the task says a slot you cannot render is logged,
  never silently dropped, so it is rendered and labelled `appendix`. Deck is 14 folios; brief
  allows 10–14.
- **`aphoristic-cadence` detector finding not fixed** (pitch-deck-mastery deck). The flagged
  string is `"P · the Protected leg — Full collateral value at or below strike. No margin call, no
  forced sale."`, which is contract text. Rewording it would breach the "never rewrite a headline
  claim / never add facts" rule, which outranks an advisory style detector.
- **`em-dash-overuse` (advisory ×6) partially fixed.** Em-dashes in my own figure labels were
  replaced with colons; the remainder are in contract-locked claim and supporting text.
- **`overdrive.md` not executed as a command** — its mandatory propose-and-confirm gate cannot be
  satisfied without a user. Read for the ceiling, not run.

### What the tool refused, or could not express

- It refused to roll the direction dice before product truth existed.
- It refused (via the craft floor's Refuse list) a set of things I would otherwise have reached
  for on a pitch deck and did not ship: kickers/eyebrows above headings (a flat ban, no brief earns
  it back), same-size icon+heading+text card grids as page structure, the hero-metric template,
  gradient text, glass/blur decoration, coloured `border-left` stripes, monospace-as-technical-
  costume, unicode glyphs standing in for icons, and light-vs-dark chosen by category rather than
  by use scene. None of the six artifacts contains any of them. The one section-numbering system
  present (foliation) is the floor's own exemption for a sequence that carries information.
- It cannot express **anything requiring a rendered pixel**: no comp round, no sketches, no
  screenshot critique, no `live` variant mode, no QUALITY BAR image to calibrate finish against.
- It has **no vocabulary for a fixed-stage presentation medium**. Every mode, reference and check
  assumes a scrolling responsive web page: "pace the scroll like a studio", body measure 65–75ch,
  mobile breakpoints, `adapt.md`. A 1280×720 fixed stage that must also paginate to print is
  outside its model, so the print lane, the keyboard navigation model, the slide-counter
  convention and the 18px floor all had to be brought in from the task brief rather than the skill.
  Same for the explainer's timeline player: `animate.md` covers interaction motion, not a
  fixed-duration film with a seek API.

### Linter results

- **`check_deck.py` — not applicable.** It is the brand-mode linter for the pinned house brand;
  free mode has no brand contract to lint against. Not run. (The brand-mode section of this file
  carries its results.)
- **`detect.mjs` (impeccable's own mechanical detector), one run over all six artifacts:** 19
  findings → fixed → **7 remaining**, all warnings, none errors:
  - fixed: `radial-halo` ×6 (the chromatic radial wash behind the page replaced with one subtle
    vertical shift), `bounce-easing` ×3 (overshoot beziers replaced with exponential ease-out;
    keyframe renamed), `layout-transition` ×3 (progress bar moved from animating `width` to
    `transform: scaleX`).
  - remaining: `aphoristic-cadence` ×1 and `em-dash-overuse` ×6 (advisory), both in contract-locked
    copy — see Overrides.
- **Finish review (`degraded/finish-reviewer.md`, fresh subagent, no forked history):** round 1
  `disposition: fix`, eight material findings, all eight applied. Round 2 (Verdict Pass) thrashed
  past its turn ceiling and returned nothing; the batch was self-scored against the shipped files
  instead, and that substitution is stated in the review section above.
- **Structural verify (python3 HTMLParser, no browser available), final round:** 6/6 OK.
  Per artifact: section count == contract slot/scene count; `<meta name="deck-footer">` exact;
  `Medici — Proprietary & Confidential` present inside every one of the 42 slides and 25 scenes;
  1280×720 / 1920×1080 stages present; `@media print` with `size:1280px 720px`; `←`/`→` handlers;
  `window.__player` exposing `scene`, `t`, `total`, `seek`; tag balance clean; zero remote
  references other than `fonts.googleapis.com` / `fonts.gstatic.com`.

### Slots rendered

**All 41 deck slots and all 25 video scenes rendered. Nothing dropped, nothing reordered, no
headline claim reworded.** Line breaks and emphasis spans were applied to claims (permitted);
wording is untouched.

| contract | deck slots in contract | slides shipped | video scenes | scenes shipped | runtime |
|---|---|---|---|---|---|
| staging | 14 | 14 | 9 | 9 | 120s (contract: 120s) |
| presentation-writing | 14 | 14 | 8 | 8 | 132s (contract: 132s) |
| pitch-deck-mastery | 13 + appendix A1 | 14 (A1 as folio 14, labelled) | 8 | 8 | 143s (contract: 143s) |

Contract-declared design-lane gates from `messaging/staging/staging.yaml` §video.gates:
- `motion_spec_locked` — **satisfied in substance, not in form.** No
  `references/motion-spec.md` file was written; the motion spec is instead recorded per scene in
  each `SCRIPT.md`'s "what moves" column and motion ledger, and in the `MOTION SPEC` line of every
  explainer's direction contract. Declared here rather than claimed as a pass.
- `seams_declared` — **not run.** `tools/seam-gate.mjs` was not available to this contender; seam
  boundaries follow the contracts' own `transitions` blocks (scene cuts land exactly on them).
- `render_and_look` — **cannot be run: no browser, headless renderer, or screenshot tool exists in
  this environment.** No human or model has looked at a rendered frame of these six artifacts. This
  is the single largest unverified risk in this track and it is stated rather than papered over:
  every visual judgement here is made from source, and the structural checker cannot see overflow,
  font fallback, or contrast as rendered. Contrast ratios were computed arithmetically from the
  token values (ink `#F2ECDC` on `#0B1436` ≈ 15:1; muted `#AEB9DA` ≈ 8.7:1; gold `#E8B44A` ≈ 9.5:1;
  vermilion `#FF6A4D` ≈ 6.3:1; verdigris `#4FB89E` ≈ 7.4:1 — all ≥ 4.5:1).

### Corpus discrepancies inherited, not re-litigated

All three contracts already resolved the canton-deck vs asset-manager-deck disagreements (54
templates / ~5,700 LOC over 36 / ~5,100; ~2,900 vs 2,600 lines of regulatory analysis) using the
brief's stated source priority. The design layer used the contracts' resolution verbatim and did
not re-open it.


### Closing pass (after the verdict returned)

The Verdict Pass did land, late, and it scored the round-1 batch **6 resolved, 2 partial, 3
regressions, `disposition: fix`** — its word, not softened here. What it caught that self-scoring
had missed, and what was done:

- **Fix 6 partial.** SVG figures are declared in user units and render *scaled*: the deck plate's
  `viewBox` 764 in a ~660px column is 0.86×, so `.pf-ax` at 18px rendered at **15.6px** and the
  threshold callout at **16.4px** — both under the 18px floor the fix claimed to have cleared.
  Raised to 22px / 24px, which render at 19.0px / 20.7px. It also computed something no size check
  would find: `.pf-thr-t` was vermilion type painted *inside* the minium fill, ≈**1.2:1**. Moved
  onto the lapis ground above the plate (6.3:1). Making it larger had made an invisible label
  bigger, not legible.
- **Fix 4 partial + regression 1.** Round 1 evicted the beat-name kicker but re-homed the internal
  working-file names (`canton-pitch-deck.md Slides 1, 3`) from a 12.5px margin note to an 18px
  full-width row on all 14 folios, and to 28px on every film frame. Resolved by splitting the rule
  rather than deleting provenance: the **deck** keeps citations (it is read without a narrator, and
  this audience distrusts an unattributed number more than a small one), the **film** carries none
  — its per-scene sources live in `SCRIPT.md`. The `source:` label was dropped; a citation reads as
  a citation.
- **Regression 2 — DESIGN.md recorded a system the build did not implement.** Five checkable
  divergences, including a "dashed strokes carry exactly two meanings and no others" rule against a
  build shipping **nine** dash patterns. Fixed on the build side, not the document side (the
  documenter's own rule: never record a value to legitimize a defect). The vocabulary is now three
  patterns for three meanings — vermilion `7 8` threshold, verdigris `4 6` tether/scope, `3 5` axis
  guide — verified: `7 8`×9, `4 6`×8, `3 5`×15, plus one `1100` path length for the draw. Catchword
  size, gutter, seal placement and the figure-label claim were corrected to ground truth.
- **Regression 3 — the documenter had canonized the sub-floor tier.** DESIGN.md wrote the 18px
  floor as house law and then exempted a "13–16px label" tier in the next line. The 13px tier was
  removed from the build (labels consolidated to 14px/16px) and the document now states that labels
  are tracked uppercase chrome, not an exemption from the reading floor.

**A detector consequence worth recording:** `detect.mjs` behaves differently once `DESIGN.md`
exists — it switches on design-system conformance and audits every literal size and colour against
the frontmatter ramp. The first post-DESIGN run went from 7 findings to **119**, none of which were
new defects: they were the frontmatter being a 5-role sketch against a build using 27 type steps.
That is the detector working correctly and it is worth knowing before running it. The response was
to consolidate the accidental near-duplicates (13→14, 18.5→19, 21→22, 26→27, 32→31; 27 steps → 22)
and then record the real two-stage ramp — deck tier and film tier — plus the full palette including
the vignette, ruling overlay, tick and print grounds.

### Detector, before and after

| run | when | findings |
|---|---|---|
| 1 | first build, no DESIGN.md | **19** — `radial-halo`×6, `bounce-easing`×3, `layout-transition`×3, `aphoristic-cadence`×1, `em-dash-overuse`×6 (advisory) |
| 2 | after mechanical fixes | **7** — `aphoristic-cadence`×1 + 6 advisory |
| 3 | first run with DESIGN.md present | **119** — conformance rules activated: `design-system-font-size`×~110, `design-system-color`×~7, `border-accent-on-rounded`×1, plus the 2 above |
| 4 | **final** | **1** — `aphoristic-cadence`×1, in copy quoted verbatim from `pitch-deck-mastery/staging.yaml` slot 3, which the design layer is forbidden to reword. Plus 6 advisory `em-dash-overuse`, likewise mostly contract-locked. |

Fixed between runs 3 and 4: the `.chip-sum` rule glyph re-drawn as a background rather than a
`border-top` (it was tripping `border-accent-on-rounded`), the ramp consolidated and documented,
and every literal colour recorded — including `#fff`, which only exists inside `@media print`.

### Final structural verification (stdlib only — there is still no browser)

`html.parser` over all six artifacts, checked against the three `staging.yaml` contracts directly:

| check | result |
|---|---|
| `<section>` count == contract slot / scene count | 14/14, 14/14, 14/14 slides · 9/9, 8/8, 8/8 scenes |
| per-scene `data-dur` == contract `vo_seconds`, in order | exact match, all 25 scenes |
| total runtime == contract runtime | 120s / 132s / 143s |
| `<meta name="deck-footer">` byte-exact | pass ×3 |
| footer string present inside every slide and every scene | 42/42 slides, 25/25 scenes |
| fixed 1280×720 and 1920×1080 stages | pass |
| `@media print` with `size:1280px 720px` | pass ×3 |
| `←`/`→` and click navigation, slide counter | pass ×3 |
| `window.__player` exposing `scene`, `t`, `total`, `seek` | pass ×3 |
| `?scene=N` and Space/→ override, progress bar | pass ×3 |
| tag balance | pass ×6 |
| no `http(s)://` refs except `fonts.googleapis.com` / `fonts.gstatic.com` | pass ×6 |
| SVG gradient ids unique per document, no dangling `url(#…)` | pass ×6 |

Two failures in the first run of this check were **bugs in the check**, not the artifacts: it looked
for `searchParams` when the player uses `URLSearchParams`, and it double-counted the
pitch-deck-mastery appendix (that contract lists A1 among its 14 `- id:` entries, so 14 sections is
correct, not 15). Corrected; 6/6 green.

### Standing at close

Round 1: `disposition: fix`, 8 findings, all applied. Round 2 verdict: 6 resolved, 2 partial, 3
regressions, `disposition: fix` — all five open items then addressed in this closing pass and
verified against the files, but **not** re-scored by the reviewer. Under its own rule that a claimed
fix it cannot see is unresolved, this run ends at *fix with the open items addressed and
unverified*, never at ship. The largest standing risk is unchanged and stated plainly: **no human
or model has ever looked at a rendered frame of these six artifacts.**
