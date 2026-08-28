# Messaging review — reviewer: `staging`

Rubric: `skills/messaging/staging/SKILL.md` v2 + `references/{audience,slide-functions,transitions,motion-roles}.md`
and `references/genres/executive-explainer.md`. Facts spot-checked against `source/medici/`.
Reviewed: `messaging/{staging,presentation-writing,pitch-deck-mastery}/` (messaging.md, staging.yaml, native artifact, NOTES.md).
Self-review is included and is not softened.

---

## 1. `staging` (self)

| Gate | Verdict | Evidence |
|---|---|---|
| Genre from the closed seven | PASS | `genre: executive-explainer`; 4 rejections each citing the failed `pick_when` (≥2 required) |
| Audience block (4 dims + fork) | PASS | assumed_knowledge names the may-use/must-explain lists; fork declared `presented-primary, read-fallback` |
| Closed function vocabulary (16) | PASS | cover/statement/fact/comparison/quote/pivot/mechanism/evidence/objection/ask/end — all legal |
| Sequencing rules | PASS | no split comparison; mechanism = 1 slot, nothing inserted; ask(d13)+end(d14) adjacent; 1 pivot; no appendix in hall |
| Claim ≤12 words + complete sentence | PASS | 23 claims, longest 12, every one a terminated declarative |
| `problem_share` ≥30% | PASS (soft) | claims 50% by counting `common-ground` as a problem beat; change+consequence alone = 39% |
| `one_mechanism` | PASS | d8 only; video s6 only |
| Bold moment, deck | PASS | d6, 6/14 = 42.9%, inside 40–50%, index < first `move` slot (d8) |
| Bold moment, video (derived) | PASS | derivation shown from this lane's `runtime_shares`: 0.35×120 = 42 s window close; s4 = 30–42 s |
| Transitions at beat boundaries | PASS | 5 boundaries, 5 types, one `turn` only, `gate` immediately before `ask` |
| Video arithmetic (shares/wpm) | PASS | 120 s × 150 wpm = 300 w budget, 299 written; scenes sum 120 s; shares 42/48/18/12 s exact |
| Motion budget R1–R5 | PASS | EVENT/CONDITION walk written, event_count 1; mean 2.33; 33% quiet; no adjacent peaks; 1 answering rhyme |
| Ornament gate R6 | PASS | ≤2 figures/scene, 14 total, three cuts named at STAGE |
| Design-leak (contract rule 1) | PASS with one soft hit | no chart/layout/palette/font/hex; but "the payoff **table**" appears in d13 and s9 |
| Facts trace to source | PASS | $344B/$2T, $620M/87%, $423.5M/$106M/269, $8M@$0, −1.25%/yr, $0.895, 54 templates/5,700 LOC all verified |

**Goals (0–10)** — 1. What Medici is: **9** · 2. RWA value prop: **9** · 3. Mechanism redrawable: **8**
(one mechanism slot buys gate compliance at the cost of teaching time; the two maturity cases share d8).

**Top 3 findings**

1. **The playbook's video `credibility bridge` device is silently dropped.** `executive-explainer`
   video devices require an explicit beat between "we understand this problem" and "we have standing
   to solve it", and warns the piece reads as generic without it. s7 is *venue* credibility (Canton),
   not standing. No gate line and no NOTES entry admits the omission.
   *Fix:* re-cut s7's 34 words to spend ~8 on standing ("built and running on Canton today, backtested
   nine years, not yet on mainnet") — it is already true from s8's material — or record the drop as a
   named assumption with its cost.
2. **d3 is labelled `fact` but carries two datasets.** `slide-functions.md`: "one fact per `fact`
   slot… a `fact` slot with five numbers on it is an `evidence` slot that has not admitted it." d3
   carries Morpho ($620M, 87%) *and* Aave Horizon ($423.5M/$106M/269).
   *Fix:* cut the Aave line to d9's comparison (which already benchmarks the incumbent) and keep d3 to
   the single Morpho number, or relabel d3 `evidence`.
3. **"Argue with the payoff table" names a rendering.** It is the ask claim (d13) and the closing VO
   (s9), so design cannot refuse it without returning to staging — which is exactly the leak rule 1
   exists to stop.
   *Fix:* "Bring one tokenized position and argue with the payoff at every price."
   Secondary: the bold moment is MakerDAO's incident, not an RWA one; the arc never answers the
   obvious retort "that is a DeFi story". A half-line in the d7 transition would close it.

---

## 2. `presentation-writing`

| Gate | Verdict | Evidence |
|---|---|---|
| Genre from the closed seven | PASS | `genre: executive-explainer` declared; scaffold rejections given in native terms (3 rejected) |
| Audience block (4 dims + fork) | PASS | all four dims; lane `mixed(hall)` with read-fallback stated |
| Closed function vocabulary | PASS | cover/intro/claim/evidence/pivot/mechanism/objection/comparison/ask/end all legal |
| Claim ≤12 words | FAIL (1) | slot 2 = 13 words |
| Claim = complete sentence (read-fallback) | FAIL | no deck claim is terminated; slot 14 "No liquidation price. Not a policy — a property of the payoff" is two fragments; scene 1 claim is a bare noun phrase |
| `one_mechanism` | **FAIL** | two `mechanism` slots (6, 7) in the deck and two (s5, s6) in the video; the playbook: "If the mechanism needs four slots, either the audience is more technical than classified (→ re-CLASSIFY) or the mechanism is being explained at a depth the mandate does not require" |
| Bold moment placement, deck | **FAIL** | slot 7 = 50%, and it sits **inside the `move`/solution beat**, after the pivot at slot 5. Rule: "at the LAST problem beat, immediately before the pivot — never inside the solution". Gate `bold-before-relief` (bold index < first `move` index) is violated |
| Bold moment placement, video | **FAIL** | self-reported "1:18–1:42 of 2:12 = 59%–77%"; the derived window from `runtime_shares` closes at ~42%. No derivation attempted |
| `problem_share` ≥30% | PASS (marginal) | deck beats 1–2 = 3.0/10 min = 30.0%; video s1–s3 = 46/132 s = 34.8%. No gate line asserts it |
| Transitions | FAIL | 13 transitions on 8 beats — one per slot, not per boundary; three `turn`s (after 1, 4, 8) against "the single pivot of the artifact. Once." |
| Video arithmetic | PASS with drift | 301 w / 132 s = 137 wpm; runtime 132 s exceeds the playbook's 120 s max (inside the brief's 150 s) |
| Motion budget R1–R5 | PASS | mean 2.44; 3/8 quiet; adjacency shown; two rhymes, both answering |
| Ornament gate R6 | PASS | ≤2/scene, 3 on s6, two STAGE cuts named |
| Gates block completeness | FAIL | 6 gates reported; `kill_conditions`, `problem-share`, `one-mechanism`, `limit-stated`, `ask-matches-authority`, `standalone`, `retell`, and the three design-lane video gates are absent |
| Design-leak | PASS (soft hit) | no palette/font/layout; s6 VO "nowhere on this **axis**" prescribes the rendering in narration |
| Facts trace to source | PASS | 92%/7x/$194M, 269 addresses, <$1K equities, −1.25%/yr, 54 templates all verified |

**Goals (0–10)** — 1: **8** · 2: **9** · 3: **9** (the best mechanism teaching in the field —
"draw the liquidation line every other venue needs; there is nowhere to put it").

**Top 3 findings**

1. **The bold moment is inside the solution.** This is the genre's named anti-pattern ("it reads as a
   pitch even though nothing is being sold → bold moment placed inside the solution beat → the problem
   beats retroactively become setup"). *Fix:* promote slot 4 (Black Thursday, the pathway running at
   $0) to the bold moment and mark it as such — it is already a dated instance at index 4/14 = 29%,
   before the pivot; then demote slot 7's threshold demonstration to the mechanism's second half at
   normal intensity. Video: the same swap makes s3 (already peaked) the bold moment at 30–46 s = 23–35%,
   inside the derived window, and s6 drops from `rupture` 5.0 to `assemble` ≤3.
2. **Two mechanism slots / two mechanism scenes.** Under this genre that is a re-CLASSIFY signal, not a
   staging choice. *Fix:* either merge 6+7 into one slot carrying the split and both maturity cases
   (the material fits — it is six lines), or re-classify to `technical-deep-dive` and re-derive the
   bold-moment window from *that* lane's shares, which is precisely the case v2 of the skill was written
   around.
3. **Read-fallback declared but not delivered.** The lane is `mixed(hall)` with read-fallback, and the
   `standalone` gate ("every headline claim is a complete sentence") is neither run nor met — no claim
   is terminated and at least three are fragments. *Fix:* terminate all 22 claims and rewrite slot 14 as
   one sentence ("There is no liquidation price, because the payoff function has none.") and scene 1 as
   ("Real collateral sits on a ledger that nobody can sell in one transaction.").

---

## 3. `pitch-deck-mastery`

| Gate | Verdict | Evidence |
|---|---|---|
| Genre from the closed seven | **FAIL** | `genre: product-pitch-explainer` — not one of the seven; header states "its methodology (INTAKE/CLASSIFY/LOAD/STAGE/GATE) was NOT used" |
| CLASSIFY rejections (≥2) | **FAIL** | none in `staging.yaml`; the fundraise-adaptation table in NOTES.md is a framework mapping, not a genre rejection |
| Audience block (4 dims) | PASS | who / assumed_knowledge / distrusts / decision_they_hold / attention_budget all present and sharp |
| Closed function vocabulary | **FAIL** | 9 of 14 deck functions are outside the 16: `problem`, `solution`, `proof`, `application`, `timing`, `context`, `risk`, `commercial`, `close`; video repeats them |
| Sequencing rules | FAIL | no `pivot` anywhere; `ask`/`end` pair absent (slot 13 is `close`); mechanism content spans slots 3–5 |
| Claim ≤12 words | FAIL (1) | video s4 = 17 words |
| Claim = complete sentence | FAIL | deck headlines unterminated; slots 6, 9, 11, 12 and A1 are fragments ("Five to ten basis points on flow. No token.") |
| `problem_share` ≥30% | **FAIL** | deck: problem beat = slots 1–2 = 1.5/10 min = **15%**; video: s1+s2 = 35/143 s = **24.5%**. This is the genre's named anti-pattern — the problem gets one slot, the solution gets four |
| `one_mechanism` | FAIL | mechanism carried across slots 3, 4, 5 (and video s3, s4, s5) |
| Bold moment, deck | FAIL (rule) | slot 5 = 38%, inside the `the split` (solution) beat, with no pivot before it |
| Bold moment, video (derived) | **FAIL** | "opens at 76 s of 143 s = 53%" — stated, not derived; no `runtime_shares` block exists in the file to derive from |
| Transitions | **FAIL** | no transitions block in either lane; every beat boundary is unmarked |
| Video arithmetic | PARTIAL | scene seconds sum to 143 ✓; 332 w / 143 s = 139 wpm ✓; but no per-scene word counts and no runtime-share apportionment |
| Motion budget R1–R5 | PASS | mean 2.31 (verified); 3/8 quiet = 37.5%; adjacency clean; R3 ceiling conflict (arrest at the top) reasoned out explicitly and well |
| Ornament gate R6 | PASS | ≤2/scene, 3 on s5, two STAGE cuts named |
| Gates block completeness | FAIL | 6 gates; no kill_conditions, problem-share, one-mechanism, limit-stated, ask-matches-authority, standalone, motion/ornament gate lines |
| Design-leak (contract rule 1) | **FAIL** | slot 4 carries a `diagram:` field specifying the plot ("P is flat at 1.00 up to S then falls away as S/x… **stacked**, their top edge is one flat line… mark where a lending market would draw its **vertical** liquidation threshold"). The file's own header claims "Nothing in this file names a colour, font, layout, chart type or transition" |
| Facts trace to source | PASS | $12.9B/~300% YoY, $840M+, 5–10 bps, team names, $344B, backtest figures all verified |

**Goals (0–10)** — 1: **8** · 2: **8** · 3: **9** (slot 6 "who holds each leg" is the one thing neither
rival has, and the video's perform-then-refuse rhyme is the strongest kinetic idea in the bake-off).

**Top 3 findings**

1. **The `diagram:` field breaks the composition contract and contradicts the file's own header.**
   Design cannot consume this verbatim without inheriting a chart spec it never agreed to.
   *Fix:* delete the field. Its argumentative content is already legal as `figures` on video s4/s5
   ("the sweep", "the constant sum", "the absent line") plus a `motion_turn`; move the one load-bearing
   sentence ("annotate the absence") into the slot's claim, which is where it belongs.
2. **Problem share 15% deck / 24.5% video.** The room is given the split before it has been made to
   want one; the genre's fix is explicit ("the room cannot want an answer to a question it has not been
   made to ask"). *Fix:* split slot 2 — which currently carries the threshold, the unsellability, the
   hand-built workout, the RedStone verdict *and* Black Thursday, five arguments on one slot — into two
   slots (the structural problem; then the dated instance as the bold moment), and pay for them by
   merging slots 3+4 into one mechanism slot. That single move fixes problem_share, one_mechanism and
   the bold-moment placement together.
3. **Nine non-vocabulary functions and no transitions.** These are the two fields a design contender
   actually consumes: `function` tells it what a slot *is*, transitions tell it where beats break.
   *Fix:* map the nine onto the closed 16 (`problem`→`claim`, `solution`→`statement`, `proof`→`fact`,
   `application`→`evidence`, `timing`→`fact`, `context`→`evidence`, `risk`→`objection`,
   `commercial`→`evidence`, `close`→`ask`+`end`) and add a transition line at each of the seven beat
   boundaries, with `gate` immediately before the ask.

---

## Ranking

1. **`staging`** — passes every gate with its arithmetic shown, including the two the others do not
   attempt (the derived video bold-moment window, and NOT-RUN honesty on the three design-lane gates).
   Its findings are real but none is structural.
2. **`presentation-writing`** — the best-written argument of the three and the best mechanism teaching,
   but it puts the loud moment inside the solution and spends two slots on the mechanism, which are the
   two failures this genre is specifically built to prevent. Both are fixable by one swap.
3. **`pitch-deck-mastery`** — the best single idea in the bake-off (perform the liquidation in scene 2,
   begin and refuse it in scene 5) and the only contender that answers "who takes the other leg", but it
   declines the rubric openly and then leaks a chart specification into the contract, which is the one
   thing a downstream design contender cannot route around.

**What this rubric cannot see.** It scores conformance to one house's argument grammar, and conformance
is not effect. It cannot tell whether a room actually believes the piece, whether the P/N split lands
for a risk lead who has never held a call option, or whether a 42.9%-index bold moment beats a 53% one
in front of real people — the placement rules are house doctrine backed by a handful of runs, not
measurement. It is blind to prose quality, so `presentation-writing`'s far better sentences earn it
nothing and my own flatter ones cost me nothing. It is blind to the value of a *better idea* that
arrives in the wrong slot: `pitch-deck-mastery`'s arrest-at-scene-5 is a stronger film than my
rupture-at-scene-4, and my rubric ranks it third. It cannot judge whether `executive-explainer` was even
the right genre for a room that may well want to argue with the mechanism — two of us chose it and
neither tested the choice. And the conflict of interest is structural, not incidental: I wrote the
rubric's expectations into my own artifact before scoring the field against them, so my first place is
partly a statement that I read the same document twice. The honest reading of this ranking is
"conformance order", and a reader who wants "best pitch" should weight the goal scores, where the field
is 26 / 26 / 25 and effectively tied.

---

## Addendum — `house-guide`

Fourth contender, reviewed on the same rubric and at the same severity.
Read: `messaging/house-guide/{messaging-guide-medici.md,messaging.md,staging.yaml,NOTES.md}`.

| Gate | Verdict | Evidence |
|---|---|---|
| Genre from the closed seven | **FAIL** | `genre: product-explainer` — not one of the seven. The header is candid that only the CONTRACT is adopted and "the arc, the claims, the bold moment and the sequencing come from the house-guide method" |
| CLASSIFY rejections (≥2) | **FAIL** | no `classify:` block at all, zero rejections, and `kill_conditions` therefore never re-checked. Two of them would have fired usefully |
| Audience block (4 dims + fork) | PASS | all four dims; a may-use / must-explain vocabulary split; a one-new-mechanism cap; `lane: mixed(hall)` with read-fallback declared and the reason given |
| Closed function vocabulary (16) | PASS | 13/13 deck slots and 9/9 scenes legal — cover/claim/evidence/fact/pivot/mechanism/comparison/objection/ask/end |
| Sequencing rules | PASS | comparison on one slot; mechanism d6–d8 declared one unit with an explicit no-insert note; `ask`(d12)+`end`(d13) adjacent; one pivot; no appendix in the hall lane; the objection carries its own answer. Nit: d4 (`fact`) sits two slots from the d2 claim it supports |
| Claim ≤12 words | **FAIL** | 12 of 13 over; only d4 complies. Longest is d10 at 26 words, d9 at 24, d7 and d8 at 21 |
| Claim = complete sentence (read-fallback) | PASS | all 13 are terminated declaratives that stand without a narrator. Ties `staging` for best in the field, and unlike `staging` it says why in the `lane` comment |
| `problem_share` ≥30% | **FAIL (marginal)** | deck `scene` beat = 2.2/10 min = **22%**; counting the pivot as a problem beat = 31%. Video: `scene` 21.8%, +`value` 29.1%. Under-slotted for the same reason `pitch-deck-mastery` was — the arc spends its middle on mechanism and boundary |
| `one_mechanism` | **FAIL** | three `mechanism` slots (d6, d7, d8) and three scenes (s4–s6). Worse than `presentation-writing`'s two. Declared as one unit, which is the sequencing rule, not this gate |
| Bold moment, deck | **FAIL (rule)** | d10 at 10/13 = **76.9%**, inside the `boundary` beat — after the mechanism and after relief. `bold-before-relief` requires the index to precede the first `move`-beat slot |
| Bold moment, video (derived) | PASS (derivation) / FAIL (rule) | the only contender besides `staging` to *derive* the window from its own lane: shares sum 0.655 → 72 s, close opens 98 s, window 65.5–89.1%, s7 at 65.5–76.4%. The arithmetic is exact and the window is its own method's, not a playbook's — and it opens after the mechanism |
| Transitions at beat boundaries | PASS | 4 beat boundaries, all typed; one `turn` only (after d5); `gate` immediately before the ask; one extra intra-beat `escalate` after d2. Cleanest transition discipline in the field after `presentation-writing`'s per-slot set |
| Video arithmetic (shares/wpm) | PASS | 110 s × 150 wpm ÷ 60 = 275 words; 271 written; scene seconds sum to 110 exactly; 140–158 wpm per scene. I re-counted s1 (declared 30, actual 30) |
| Motion budget R1–R5 | PASS | EVENT/CONDITION walk written out (3 events → peak budget 3, 1 earned); mean 2.44 re-derived from 22.0 ÷ 9; 3/9 quiet = 33.3%; adjacency paid by s8 at 0.5; two rhymes, both answering |
| Ornament gate R6 | PASS | 15 figures, ≤2 per scene, 3 on the bold moment, every figure named against the clause it renders, three cuts named at STAGE |
| Gates block completeness | PASS with a hole | 8 deck + 8 video gate lines — the fullest block in the field — and `render_and_look` is recorded **NOT RUN** with the owner named. But `kill_conditions`, `problem-share`, `one-mechanism`, `retell` and `ask-matches-authority` are absent, and it would fail two of them |
| Design-leak (contract rule 1) | PASS with one soft hit | no chart type, layout, palette, font or hex anywhere; the diagram spec is deliberately kept out. Soft hit: d9's "Axes are the audience's, not ours" names a rendering, as `staging`'s "payoff table" did |
| Facts trace to source | **PASS — best in the field** | every figure carries file + slide + as-of in visible text; three figures are refused with a stated reason (54-vs-36 templates, gross theta, the $8M) and the refusals are re-asserted in `assumptions` as binding on design |

**Goals (0–10)** — 1. What Medici is: **8** · 2. RWA value prop: **9** · 3. Mechanism redrawable: **9**
(d6 is the only slot in the bake-off that *mandates* a worked instantiation, and d7 is the identity in
two rows; docked one because the redraw spec itself stays in `messaging.md` §4 and never enters the
contract, so design receives the arithmetic and not the picture).

**Top 3 findings**

1. **The sequencing gate certifies something the file contradicts twice.** `diagnosis_carried.b3` says
   "no figure appears before d7 / s5"; the `sequencing` gate says "no figure appears before d10 except
   the two context numbers in d2 and d9"; d10's own note says "the first number in the entire deck
   arrives here, on slot 10 of 13". At most one of the three is true — d2 carries $12.9B and ~300% YoY,
   d9 carries $423.5M and $106M. A design contender told to consume this verbatim cannot tell which
   rule binds it, and this is the same class of defect that cost `pitch-deck-mastery` its ranking here.
   *Fix:* delete d10's note sentence, restate b3 as "no figure about our own product appears before
   d10", and let the sequencing gate's exception clause be the single statement of the rule.
2. **A genre outside the seven and no CLASSIFY block at all.** The method's own reasoning already
   contains the rejections: `technical-deep-dive` fails because the audience is classified as
   technical-*adjacent* and will not evaluate the contracts; `investor-pitch` fails because the two
   capital asks were deliberately cut, which is that genre's entry condition inverted. Writing them
   costs two lines and would have forced the kill-condition re-check the file skips.
   *Fix:* declare `executive-explainer`, record those two rejections, re-run `kill_conditions` — and if
   the method's sequencing rule then conflicts with the playbook's bold placement, override it as a
   *declared* exception naming the gate, which is legal; silently having no genre is not.
3. **Three mechanism slots, and the peak lands behind the relief.** d6–d8 is a re-CLASSIFY signal under
   every playbook in the set, and d10 at 76.9% is the placement the `bold-before-relief` gate exists to
   prevent. The two are one problem: the mechanism run pushes the boundary beat, and the boundary beat
   is where the method insists the peak lives. *Fix:* fold d7's two payoff rows into d6, where the
   mandated worked example already has to state them — one mechanism slot, the run shortens by one, and
   the index frees up for a peak that can sit before the pivot without abandoning the method's rule.
   Secondary: "AAA Flowers S.A. (Panama)" appears on both d1 and d13, the only contender to spend it twice.

**Revised ranking**

1. **`staging`** · 2. **`house-guide`** · 3. **`presentation-writing`** · 4. **`pitch-deck-mastery`**

`house-guide` enters second and pushes both of the others down: it is the only contender besides
`staging` to adopt the closed vocabulary, type every beat boundary, derive the bold placement per lane
with the arithmetic shown, and run the full motion budget — it rejects only the genre taxonomy, and it
leaks no chart spec, which is exactly the line `pitch-deck-mastery` crossed and cannot be routed around
downstream. `presentation-writing` drops to third because `house-guide` matches its transition
discipline while delivering the complete-sentence claims and the honest video window that
`presentation-writing` asserted rather than derived. Nothing moved at the top: `staging` remains first
on conformance, and the goal totals are now 26 / 26 / 26 / 25, which is a four-way tie by any reading
that is not conformance order.
