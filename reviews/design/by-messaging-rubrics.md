# Design contenders judged by the messaging contenders' own rubrics

Reviewer pass over the 10 finished track-modes
(`canvas-design, algorithmic-art, impeccable, visual-explainer, html-ppt` × `brand, free`),
all three rendered messaging variants each (30 decks + 30 explainers + 10 NOTES.md).
`house-guide` is applied as a rubric only — no track was asked to render it.

**Method.** (1) Programmatic fidelity diff: every contract slot/scene `claim` and every
`supporting`/`supporting_points` entry normalised and matched against the text actually
extracted from the rendered HTML (script/style stripped, entities unescaped); numbers matched
in both directions. (2) Render-and-look: no `shots/` existed, so 130 frames were rendered with
headless Chrome (`/Applications/Google Chrome.app`, CDP driver) into
`/Users/iholsman/jojig/Lending/rwa-bakeoff/shots/`, deck slides driven by real ArrowRight
key events and verified by reading back the active slide index. (3) Motion measurement: each
`staging` explainer was played once end to end and sampled every 1.5 s (82 frames × 10 films,
820 frames); per-scene motion = max share of pixels changing >12/255 between consecutive
in-scene frames, cut frames excluded. Metric limits: it reads amplitude-over-area, so a slow
large move and a fast small move are not distinguished, and sub-1.5 s events can be missed.
(4) House deck linter re-run independently on all five brand `staging` decks.

**`tools/seam-gate.mjs`: NOT RUN — for all ten track-modes.** Every explainer exposes
`window.__player`, but the gate additionally requires a seams ledger (`--ledger ledger.json`,
`references/seam-gate.md`), and no track produced one — `find tracks -iname '*ledger*'` is empty.
`motion_spec_locked` is likewise unrun everywhere: no `references/motion-spec.md` was written by
any contender. `impeccable` claims it "in substance" via a `MOTION SPEC` line, which in fact
appears only in its three *free* explainers, not the brand ones.

---

## 1. Fidelity matrix — design × messaging

Cells are **headline claims verbatim / reworded / dropped** (of 14 slots for `staging` and
`presentation-writing`, 13 + declared appendix for `pitch-deck-mastery`). Slot order was
checked against render order in every deck: **no reordering anywhere**. Footer present on
every slide of all 30 decks.

| design / mode | staging | presentation-writing | pitch-deck-mastery |
|---|---|---|---|
| canvas-design / brand | 14 / 0 / 0 | 14 / 0 / 0 | 13 / 0 / 0 |
| canvas-design / free | 14 / 0 / 0 | 14 / 0 / 0 | 13 / 0 / 0 |
| algorithmic-art / brand | 14 / 0 / 0 | 14 / 0 / 0 | 13 / 0 / 0 |
| algorithmic-art / free | 14 / 0 / 0 | 14 / 0 / 0 | 13 / 0 / 0 |
| impeccable / brand | 14 / 0 / 0 | 14 / 0 / 0 | 13 / 0 / 0 |
| impeccable / free | 14 / 0 / 0 | 14 / 0 / 0 | 13 / 0 / 0 |
| visual-explainer / brand | 14 / 0 / 0 | 14 / 0 / 0 | 13 / 0 / 0 |
| visual-explainer / free | 14 / 0 / 0 | 14 / 0 / 0 | 13 / 0 / 0 |
| html-ppt / brand | 14 / 0 / 0 | 14 / 0 / 0 | 13 / 0 / 0 |
| html-ppt / free | 14 / 0 / 0 | 14 / 0 / 0 | 13 / 0 / 0 |

Every headline claim in every deck is verbatim (line-breaking and a styled full stop only).
Apparent rewordings in a first pass were normaliser artefacts — a period inside a decorative
`<span>` — and resolve to verbatim on inspection.

**Supporting-point and number exceptions** (144 supporting points per design-mode; everything
not listed placed intact, including payoff branches rendered as diagram labels or table rows,
which the matcher first flagged and manual reading cleared):

| exception | where | class |
|---|---|---|
| `d11` "Roll cost −1.2%/yr at 10bps across ~12.2 rolls/yr is the dominant cost driver" absent from the deck entirely (`grep` for `10 bps`, `12.2`, `1.2%` = 0 hits) | canvas-design / brand / staging | **fact dropped** — and the only two contract numbers missing from any deck |
| slot 2 "Black Thursday, $8M of collateral liquidated for $0" rendered only as an unlabelled figure (`$8M SOLD INTO THE FALL` + a `0`); "Black Thursday" appears nowhere in the file, though it does in the same design's brand deck | canvas-design / free / pitch-deck-mastery | **name dropped, number kept** |
| a per-slide generative `seed NNNN` (3441…3454) printed on every slide, and `SEED 12004` on every explainer frame | algorithmic-art / free | on-screen number tracing to nothing |
| the full staging contract embedded verbatim as `window.SHOW_DATA` inside a "Proprietary & Confidential" artifact | algorithmic-art / free | not visible, but it ships the contract |

**Video lane.** Scene count equals contract scene count in all 30 explainers; SCRIPT.md rows
match; per-scene durations equal `vo_seconds` and VO is verbatim in all 30. Measured playback
scene starts land within one 1.5 s sample of the contract (0/10/20/30/42/52/76/90/108 for
`staging`) in all ten films — **no film alters the contract's timing**. Two shape notes:
`impeccable/free`'s SCRIPT.md tables carry extra sub-rows so a naive row sum reads 132 s rather
than 120 s (the player is correct at 120 s); `impeccable/brand` exposes
`window.__player.total = 9` (scenes) where the other nine expose `120` (seconds), putting
`totalSeconds` beside it — an interop divergence from the brief's `{scene, t, total, seek(n)}`.

---

## 2. Per track-mode — the four rubrics on the `staging` variant

Legend: **P** pass · **~** partial · **F** fail. Motion numbers are % of pixels changing
in-scene; contract energies are s1 1 · s2 2 · s3 3 · **s4 5 (rupture, bold moment)** · s5 1 ·
**s6 4 (assemble)** · s7 2 · s8 1 · s9 2.

### canvas-design

| rubric | brand | free | evidence |
|---|---|---|---|
| staging (motion roles / peak / seam) | **P** (seam NOT RUN) | ~ (seam NOT RUN) | brand: s4 3.35 is the film's maximum, s6 3.26 just below it (R3 ordering holds), quiet scenes s1/s5/s8 = 0.01/0.09/0.01 (R2 paid), rank correlation to contract energy ρ=+0.85 — the only film in the bake-off where the bold moment measurably *is* the peak. free: s1 (a `hold`, energy 1) moves 3.29 vs s4's 1.98, so the cold open the contract explicitly wanted still is the second-loudest thing in the film; s6 11.93 breaks R3. |
| presentation-writing (one idea, beats) | P | P | One declarative thesis per slide, supporting points as ≤3 annotations on the plate rather than bullet stacks; d6 is a single-statement stakes slide, d14 closes on the charge. |
| pitch-deck-mastery (must-pass) | ~ | ~ | Title one-liner P; quantified problem P; solution tied to problem P; ask clear P; *market size with sourcing* and *team credentials* are absent — the contract cut both, so this is the contract's miss inherited, not the design's. "Charts over tables" honoured throughout. |
| house-guide (B1–B9, §7) | ~ | ~ | B1/B2/B5/B6 pass — d8 is a real payoff diagram with P and N glossed *protected*/*amplified*. B4 fails in the film: the scene eyebrow prints staging's internal motion vocabulary (`SC. 04 / 09  RUPTURE`, `ACCUMULATE`, `STRAIN`) to the viewer. §7 fails once: the dropped roll-cost line above, plus a d6 bar field whose ~50 bar heights are decorative rather than data. |

### algorithmic-art

| rubric | brand | free | evidence |
|---|---|---|---|
| staging | **F** (seam NOT RUN) | ~ (seam NOT RUN) | brand: the film barely moves at all — every scene measures ≤0.28, s4 0.17, s6 0.01. An `assemble` that does not assemble and a `rupture` that does not rupture; the motion budget is unrendered, not restrained. Its own NOTES.md concedes "not done: an actual pixel look-pass". free: ρ=+0.67 and real amplitude, but s6 17.11 is 2.5× s4 6.80 — R3 inverted, the mechanism is the loudest thing in the film. |
| presentation-writing | ~ | ~ | d8 renders five bullets under one thesis, over the skill's three-bullet ceiling; the plate beside them shows a stripe field labelled only `price x → strike S` and does not draw the payoff, so the "no bullets, the visual carries it" option was available and not taken. |
| pitch-deck-mastery | ~ | ~ | "Show, don't tell" fails on the mechanism: the generative plate is not a chart of anything. The `census · Σ 1.000 · at every x` / `Σ 0.000 · conservation off` readout is the honourable exception — it is the invariant, live, and it is the strongest single idea either mode produced. |
| house-guide | F | F | B4 is the worst in the field: all 14 slides carry the contract's own function·beat vocabulary as the kicker (`COVER · COMMON-GROUND`, `PIVOT · CONSEQUENCE`), and in free mode the explainer prints staging's internal `figures:` names as viewer-facing bullets — "the breached threshold — 'does exactly what it was built to do'", "the proceeds falling to zero" (frame `shots/algorithmic-art__free__sc4.png`). That is design metadata staged as content. §7: `seed 3441…` on every slide. |

### impeccable

| rubric | brand | free | evidence |
|---|---|---|---|
| staging | ~ (seam NOT RUN) | **F** (seam NOT RUN) | brand: motion is real but uniformly tiny (max 0.58); the quiet `hold` s5 (0.58) moves more than the `rupture` s4 (0.33), so R3's ordering fails even though the restraint is deliberate and the frames read. free: s8 — the `divest`, energy 1, "motion here is subtractive only" — measures 12.91 and is the **loudest scene in the film**, ahead of s6 11.57 and s4 5.49. The one scene whose whole job is to give up the apparatus is the one that shows off. |
| presentation-writing | **P** | **P** | The best structural reading of the skill in the bake-off: one thesis, then a two-row ledger (`Collateral liquidated on Black Thursday ~$8M` / `Proceeds returned to its holders $0`), then one numbered clause. Density genuinely flexes — d6 is a single statement, d8 a diagram plus two case rows. |
| pitch-deck-mastery | ~ | **P** | free mode is the strongest "show, don't tell" artifact here: the d8 stacked area with the legend line "the top edge is flat at 1.00 at every price" states the invariant *and* draws it. 10-word rule respected in captions. |
| house-guide | **P** | **P** | B1/B2/B4/B5/B6 all pass — no internal vocabulary reaches the screen (its scene label is `THE BREACH`, not `RUPTURE`), P and N glossed on first use, and in brand mode d9 is a real `<table>`. §7 passes: every figure carries an `AUTHORITY` source line. |

### visual-explainer

| rubric | brand | free | evidence |
|---|---|---|---|
| staging | ~ (seam NOT RUN) | ~ (seam NOT RUN) | brand: ρ=+0.68 and the frames read, but s6 6.07 > s4 3.79 and even s8 (a quiet `divest`) 4.52 > s4 — the bold moment is third-loudest. free: ρ=+0.73, quiet scenes properly quiet (s1 0.02, s7 0.02), but s6 9.08 is 7× s4 1.31 — the rupture is nearly still. |
| presentation-writing | **P** | **P** | Front-loaded hook, one thesis per slide, comparison as a table, close on the charge. d6 is the cleanest bold-moment slide in brand mode: a `~$8M` block, an arrow, a red `$0`, nothing else. |
| pitch-deck-mastery | **P** | ~ | Headline-as-takeaway everywhere; quantified; charts over tables where trend is the point and a table where precision is. Same inherited market/team gaps as the rest. |
| house-guide | **P** | ~ | brand glosses and stays out of insider vocabulary. free regresses: the explainer prints `fact · accumulate`, `comparison · strain` as scene labels (B4). |

### html-ppt

| rubric | brand | free | evidence |
|---|---|---|---|
| staging | ~ (seam NOT RUN) | ~ (seam NOT RUN) | brand: s8, the quiet `divest`, is the loudest in-scene mover at 6.46, ahead of s9 4.45 and the s4/s6 peaks tied at 2.2 — the budget is inverted at the end of the film. free: ρ=+0.83, the best correlation after canvas-design/brand, quiet scenes at 0.08/0.01/1.25, but s6 8.62 > s4 5.53, so R3 fails by a nose. |
| presentation-writing | **P** | **P** | Thesis-per-slide, ≤3 bullets, a real payoff table on d8 with the invariant row spelled out; speaker notes carried in `.notes` as the skill prescribes. |
| pitch-deck-mastery | **P** | **P** | d8 pairs the `S ≥ x / S < x` table with the stacked chart and the `P + N = 1.00` dashed top edge — the clearest single answer to "how do you solve it?" in the deck lane. |
| house-guide | ~ | ~ | B5/B6 pass. B3 risk: `brand` d6 leaves the frame two-thirds empty around the `$0`, so the bold moment reads quieter on the page than it does in the argument. B4 minor: three of staging's `figures:` names reach the brand explainer's captions. |

---

## 3. Top three findings

**F1 — the bold moment is not the visual peak in nine of ten films.** Measured in-scene motion
puts s6 (`assemble`, energy 4) above s4 (`rupture`, energy 5) in six films, and puts a scene the
contract marks *quiet* above s4 in three more (`impeccable/free` s8 12.91 vs s4 5.49;
`html-ppt/brand` s8 6.46 vs s4 2.22; `canvas-design/free` s1 3.29 vs s4 1.98). Only
`canvas-design/brand` orders the film the way motion-roles.md R3 requires.
*Fix:* make R3 executable — have each contender emit the same per-scene measurement (any
frame-diff harness will do) and assert `max(s_bold) > max(all others)` before calling a film
done. It is a five-line check and it would have caught all nine.

**F2 — staging's internal vocabulary is being rendered as viewer-facing copy.**
`algorithmic-art/free` prints the contract's `figures:` names as on-screen bullets and its
`function · beat` labels as every slide's kicker; `canvas-design` (both modes) and
`visual-explainer/free` print motion-role names (`RUPTURE`, `ACCUMULATE`, `STRAIN`) as scene
eyebrows. Under house-guide B4 these are unglossed insider terms in front of a room that has
never read the contract; under motion-roles.md they are instructions to the designer, not content.
*Fix:* one line in DESIGN-TASK.md — `motion_role`, `function`, `beat` and `figures[].name` are
design inputs and must not appear on screen; `impeccable`'s `THE BREACH` is the pattern to copy.

**F3 — one real fact drop and one real name drop, both in canvas-design.**
`brand/staging` d11 loses the roll-cost line entirely (the two numbers missing anywhere in the
30 decks), which matters because it is the *driver* of the −1.25 %/yr the same slide shows —
a house-guide §7 trace-every-number failure, since the figure on screen can no longer be
re-derived from what is on screen. `free/pitch-deck-mastery` slot 2 keeps `$8M` and `$0` but
drops the name "Black Thursday", which is the retellable handle.
*Fix:* both are one-line restorations; more usefully, the fidelity differ used here (claim +
supporting-point coverage against extracted DOM text) should run as a contender self-check
before NOTES.md is written — it takes seconds and both tracks reported "nothing dropped".

---

## 4. Rankings

**brand mode** (messaging fidelity + comprehension)

1. **impeccable** — perfect claim fidelity, zero insider vocabulary on screen, sourcing on every
   figure, the clearest slide-level structure; loses only on motion amplitude (a deliberate
   restraint that nonetheless fails R3's ordering).
2. **visual-explainer** — same fidelity, nearly as clean, the best single bold-moment slide;
   marginally behind on P/N glossing and on the film's peak ordering.
3. **html-ppt** — strongest mechanism slide in the deck lane; docked for the inverted end of the
   film (s8 loudest) and slack framing on d6.
4. **canvas-design** — the only film that gets the motion budget right, and the only deck with a
   dropped fact; the two roughly cancel, and the `RUPTURE` eyebrow costs it comprehension.
5. **algorithmic-art** — verbatim text, but a film that does not move, a mechanism plate that
   draws nothing, and the contract's beat vocabulary on all 14 slides.

**free mode**

1. **impeccable** — the highest-comprehension artifact in the bake-off; the d8 stacked area with
   "the top edge is flat at 1.00 at every price" is the argument, drawn. Docked for the
   `divest` scene being the film's loudest.
2. **html-ppt** — best energy correlation of the free films (ρ=+0.83) with genuinely quiet quiet
   scenes, table + chart on the mechanism, no vocabulary leaks.
3. **visual-explainer** — clean and legible; loses ground to the `accumulate`/`strain` labels and
   a rupture that barely moves.
4. **canvas-design** — beautiful and high-fidelity, but the cold open moves more than the
   rupture and slot 2 of pitch-deck-mastery loses "Black Thursday".
5. **algorithmic-art** — the highest ceiling on show (real generative motion, ρ=+0.67, the live
   `Σ 1.000 · at every x` census) and the worst discipline: contract metadata as copy, seeds as
   on-screen numbers, the whole contract shipped inside a confidential file.

---

## 5. Which tools served the argument, and which decorated it

The dividing line was not aesthetic ambition — it was whether the tool's signature move was
pointed at a clause of the claim. `impeccable` and `html-ppt` served it most consistently:
their strongest gestures are a two-row ledger that makes `~$8M → $0` a single readable
sentence, and a payoff table whose dashed top edge *is* `P + N ≡ 1.00`. Nothing in either
artifact moves or exists that a supporting point did not ask for, which is why they also score
best on house-guide's comprehension tests. `visual-explainer` sits just behind, disciplined but
less inventive. `canvas-design` is the interesting split: its film is the only one that honours
the motion budget as written, and its plates are drawn from the claims — yet it is also the
only track that lost a fact, and its d6 bar field is fifty bars of nothing, a decorative
gesture inside an otherwise argument-led deck. `algorithmic-art` is the clearest decoration
case, and instructively so: its generative field is gorgeous and renders no clause of any
claim — while the small monospace readout beside it (`census · Σ 1.000 · at every x`, flipping
to `conservation off` at the liquidation slide) is the single most argument-serving invention
in the whole bake-off. The tool's own aesthetic was decoration; the one place it let the
argument drive the pixels, it beat everybody. The general lesson for the design layer is that
a contract's `figures[].name` is a commission, not a caption: the tools that read it as "draw
this clause" served the argument, and the tools that read it as "print this" decorated it.
