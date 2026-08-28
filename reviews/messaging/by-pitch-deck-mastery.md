# Messaging review — reviewer: `pitch-deck-mastery`

Rubric: `skills/messaging/pitch-deck-mastery/SKILL.md` + `references/` only — the 12-slide
framework, must-pass checklist, strength signals, common-mistakes list, content/narrative
rules. Nothing from the staging schema, motion vocabulary or brand guide is scored (see
blind spots). `S6 consistent visual identity` is n/a for all three and is not tabled — it
is design's row. Key: P pass · A adapted pass · F fail.

**Where the rubric assumes a fundraise:** `M4 Market size` (TAM/SAM/SOM → "where the
collateral and the borrow demand already sit", no TAM invented); `M6 Clear ask` (amount +
use of funds → a low-friction next commitment); `S1 Traction chart` (no curve can exist
pre-mainnet → honest build state scores instead); `X5 ≤15 slides at seed` (stage read as
company stage). `M5 Team` is kept unadapted — a risk lead evaluating a novel payoff from an
unknown Panamanian entity asks the counterparty question too. All three refused to invent a
TAM or a curve, so nobody is penalised by the adaptation.

---

## 1. `staging`

| Check | V | Evidence |
|---|---|---|
| M1 one-liner on title | P | `staging.yaml` d1 claim + `messaging.md` §1 corridor form ("two halves that always add back up") |
| M2 quantified problem | P | d3–d6: $620M/87%, $423.5M/$106M/269, "$8M for $0" — all cited |
| M3 solution tied to problem | P | d7 pivot → d8 payoff answers d4's "cannot liquidate in one transaction" clause for clause |
| M4 market size, sourced | A | d3 + d10 give position, not size; no TAM asserted anywhere |
| M5 team credentials | **F** | Entity name only (`d1` supporting: "AAA Flowers S.A."). No founder, no credential, in any of the three files |
| M6 clear ask | A | d13 "an hour and a counterexample"; capital asks explicitly cut and logged in `assumptions` |
| S1 traction trajectory | A | Correctly absent; d12 lists the five things that do not exist |
| S2 named logos | P | d2 Franklin Templeton BENJI; `messaging.md` proof 5 adds Invesco/WisdomTree/BlockBooster |
| S3 unit economics | **F** | Drift decomposition is on d11, but the 5–10bps fee lives only in `messaging.md` §5's closing paragraph — no slot carries it |
| S4 honest competition | P | Best of the three: d9 volunteers a row the incumbent wins ("$620M+ live deposits… Medici has no live users") |
| S5 "why now" insight | **F** | No timing slot. d3 carries the growth number but its claim is a fact, not an inflection |
| X1 10-word bullets | F | 33 of 45 supporting points exceed 10 words (d9, d11, d12, d13 = 100% over) |
| X2 unsourced market size | P | Every figure carries file + slide/section |
| X3 "no competition" | P | d9 concedes; objection 4 concedes the Canton distribution gap |
| X4 vanity metrics | P | −1.25%/yr is on the slide, labelled ETH-only and third-party |
| X5 ≤15 slides | P | 14 + no appendix |
| X6 generic team bios | P (vacuous) | Passes only because there are no bios at all — see M5 |
| Framework coverage | 9/12 | Missing: 4 Why Now, 8 Business Model, 10 Team. Nothing invented in their place |
| Headline = takeaway | P | All 14 claims are declarative insights; helicopter read genuinely stands alone |

**Scores (brief's goals):** 1. one repeatable sentence — **8**; 2. RWA value prop — **8**;
3. mechanism + one redrawable diagram — **8**.

**Top 3 findings**

1. **The buyer's cost question has no slide.** "5–10bps per transaction, no Medici token,
   multi-sig fee schedule" (`canton-pitch-deck.md` Slide 7) is in `messaging.md` §5 but not in
   `staging.yaml`, which the brief says design consumes verbatim — so six design contenders
   ship a deck that never says what it costs. *Fix:* add those three points to d13.
2. **No counterparty and no "why now".** M5 and S5 fail for one reason: 4 of 14 slots go to
   the problem beat, none to who is behind the payoff or why the window is open. *Fix:* fold
   the founders' credential lines (`canton-pitch-deck.md` Slide 10) into d13, and re-cast d3
   from a growth fact to the timing insight it supports — the asset side arrived while the
   lending side still liquidates.
3. **Two overstatements, and the transport carries no as-of block.** d9 credits the incumbent
   with "years of operating history" where the corpus gives ~14 months; d3 and video s2
   compress "~zero early 2025 → $620M+ March 2026" into "in a year" (the prose body is right).
   And `messaging.md`'s as-of header — the most precise here — has no counterpart in
   `staging.yaml`, where d10's $344B and s7's VO carry no date. *Fix:* "months, not years";
   give the two dates; add a top-level `as_of:`. (NOTES §5 also admits the arc is 14 slots
   because that is where the bold placement computes — a gate driving the argument.)

---

## 2. `presentation-writing`

| Check | V | Evidence |
|---|---|---|
| M1 one-liner on title | P | Slide 1 + slide 14 carry the identical canonical sentence — the strongest repetition discipline of the three |
| M2 quantified problem | P | Slides 2–4: $620M/87%, $423.5M, "$8M for $0", $116M Mango |
| M3 solution tied to problem | P | Slide 5 pivot names the exact thing slide 3 was patching |
| M4 market size, sourced | A | Slides 2, 10, 11 give position; no TAM |
| M5 team credentials | **F** | "Medici (AAA Flowers S.A.)" on the cover, nothing else. Presenters named only in `NOTES.md` Q9 |
| M6 clear ask | A | Slide 13: name one position, we size the split, then try to break the payoff |
| S1 traction trajectory | A | Correctly absent; slide 12 lists the gaps |
| S2 named logos | **F** | `staging.yaml` slot 11 names no issuer — Franklin Templeton/BENJI survives only in `messaging.md` §5's "available on request" paragraph, which design never reads |
| S3 unit economics | **F** | The fee does not appear in `outline.md`, `messaging.md` or `staging.yaml`. Framework slide 8 is missing outright, not replaced |
| S4 honest competition | P | Slide 9's axes are "the ones a risk lead would pick, not the ones we win on", and the speaker note says to say so aloud |
| S5 "why now" insight | **F** | No timing slot; slide 2 establishes scale, not an inflection |
| X1 10-word bullets | **F** | Worst of the three: 37 of 40 supporting points over 10 words; slide 2's bullets run 20+ |
| X2 unsourced market size | P | Every figure carries file + section |
| X3 "no competition" | P | Slide 11 volunteers "Canton appears nowhere in the RedStone report" |
| X4 vanity metrics | P | Slide 8 says the negative number out loud, before it is asked for |
| X5 ≤15 slides | P | 14, no appendix |
| X6 generic team bios | P (vacuous) | No bios at all — see M5 |
| Framework coverage | 9/12 | Missing: 4 Why Now, 8 Business Model, 10 Team |
| Headline = takeaway | P | Every slide title is an argument; slide 7's "neither is a margin call" is the best headline written by any contender |

**Scores:** 1. repeatable sentence — **9**; 2. RWA value prop — **8**; 3. mechanism + diagram — **9**.

**Top 3 findings**

1. **The product pitch never prices itself.** No artifact contains 5–10bps, "no Medici
   token" or the multi-sig fee schedule — the one framework slot a *buyer* cannot do without.
   The drift is presented as if it were the whole cost, and slides 8 and 13 both invite the
   room to model an economics missing a term. *Fix:* add a cost-to-hold slot from
   `canton-pitch-deck.md` Slide 7 + `asset-manager-pitch-deck.md` Slide 10, noting the roll
   spread is already inside the −1.25%.
2. **The strongest evidence is stranded outside the transport.** Issuer logos live in
   `messaging.md`; `staging.yaml` slot 11 does not carry them. Slot 7 *does* carry the
   drawn-then-removed line, which is why the diagram survives the handoff — apply that
   discipline to the rest. *Fix:* promote the issuer names into slot 11's
   `supporting_points` with the `canton-pitch-deck.md` Slide 7 citation.
3. **The film opens on a claim its own cited section contradicts.** Scene 1's VO — "*none of
   it* can be sold inside a single transaction" — is sourced to `rwa-redstone-2026.md` Part 2
   "Vault standards", the section saying ERC-4626 "fits liquid, instantly-redeemable assets —
   tokenized treasury funds, MMFs, equities"; the source scopes un-sellability to private
   credit. Slides 2 and 13 repeat it unqualified. And `messaging.md` §1 claims the canonical
   sentence is "reused verbatim, never paraphrased" — slide 14 does, slide 1 paraphrases it.
   *Fix:* scope to private credit; quote §8.3 exactly on slide 1 or drop the claim.

---

## 3. `pitch-deck-mastery` — self-review

| Check | V | Evidence |
|---|---|---|
| M1 one-liner on title | P | S1 headline + three registers in `messaging.md` §1; repeated at S13 and video s8 |
| M2 quantified problem | P | S2: the RedStone quote, the hand-built workout, "$8M for $0" |
| M3 solution tied to problem | P | S3 answers S2's three clauses; S5 states the absence S2 named |
| M4 market size, sourced | A | S8 replaces TAM with $344B / $840M+ / $423.5M, all cited; NOTES §3 Q4 logs the refusal to size |
| M5 team credentials | A | S13 names three founders with domain lines; A1 carries depth |
| M6 clear ask | A | S13 states the ask and, unusually, what is *not* being asked (capital, custody, commitment) |
| S1 traction trajectory | A | S10 build state + the five gaps |
| S2 named logos | P | S8 names four Canton issuers, explicitly as ecosystem context, never as customers |
| S3 unit economics | P | Only contender with both sides: S12 5–10bps on flow and S11's drift decomposition, placed adjacent on purpose |
| S4 honest competition | P | S9 names Aave Horizon as a working alternative with volume and says the empty quadrant is empty |
| S5 "why now" insight | P | S7 is a market-failure trigger, documented rather than asserted |
| X1 10-word bullets | **F — and falsely self-certified** | `pitch.md` §3 says "no bullet exceeds 10 words"; 28 of 45 deck bullets do, S3's first bullet is 18. `staging.yaml` slot 11 is 6 of 6 over |
| X2 unsourced market size | **F (attribution)** | Figures all trace, but `messaging.md` §3 credits "$840M+ … 87% utilization" to "RedStone documents" — the corpus is explicit it is KuCoin's summary of the report (`rwa-redstone-2026.md`), a conflation that file warns about |
| X3 "no competition" | P | S9 speaker note: "the alternative is Horizon plus a lawyer, and that alternative works today" |
| X4 vanity metrics | P | Backtest labelled third-party, ETH-only, negative, on the slide |
| X5 ≤15 slides | P | 13 + 1 appendix |
| X6 generic team bios | P | Canton/DAML, ASF, named patents — domain-specific |
| Framework coverage | **12/12** | Every slot kept, re-purposed or replaced with the swap logged in `pitch.md` §1; slot 6 added for the two-sided instrument |
| Headline = takeaway | P | All 13 |
| One idea per slide | **F** | S4 and S5 are one idea in two slots: S5 introduces no fact S4 did not, it re-states the identity as an absence |

**Scores:** 1. repeatable sentence — **8**; 2. RWA value prop — **9**; 3. mechanism + diagram — **8**.

**Top 3 findings**

1. **A checklist filled in wrong is worse than one never filled in.** `pitch.md` §3
   self-certifies "no bullet exceeds 10 words" and "no slide exceeds five bullets" against an
   artifact where 62% of bullets breach the first and S11 is an eight-row table; its M5 row
   credits "named blockchain patents" that appear only in `NOTES.md`, not on S13 or A1.
   *Fix:* re-run the checklist against the artifact, not the intent — mark X1 FAIL, split S11
   into removed/present/open, and put the patent line on A1 or drop the claim.
2. **The bold moment is a strong sentence in the deck lane — exactly what the rubric forbids.**
   `staging.yaml` gates it "a thing that happens on screen rather than a strong sentence":
   true for video scene 5's refused gesture, false for deck slot 5, whose four bullets are all
   assertion. The drawn-and-refused line sits in S4's *speaker note*, so a reader who never
   hears the talk never meets it; both rivals put the event inside slot content.
   *Fix:* move that instruction into S5's supporting points and narrow the gate to video.
3. **Four claims outrun their sources, on the widest-sourced deck here.** S8: the four issuers
   "are already issuing here" — the corpus evidences issuance for two, a Tradeweb *trade* for
   Franklin, and only "joined Canton Foundation" for BlockBooster. O5: distribution is "a
   problem we are solving with issuer partnerships" — the corpus lists pilot *conversations*
   as a line item the requested funding would cover. Pillar 1: treasuries "cannot be
   liquidated in a single on-chain transaction" — the source scopes that to private credit and
   calls treasury funds and MMFs instantly redeemable. O3 widens a verbatim quote from "equity
   collateral" to "volatile collateral". And `messaging.md` has no as-of header, unlike both
   rivals, so its $344B and $840M stand undated on a forwardable artifact.
   *Fix:* "issue or trade on Canton"; "pilot conversations"; scope to private credit; restore
   "equity"; add the header. (Also densest at 4.6 points/slot, and no `vo_words` per scene.)

---

## Ranking

**1. `staging` · 2. `pitch-deck-mastery` · 3. `presentation-writing`**

On raw coverage my own output wins (12/12 against 9/12 twice), and that is precisely why it
does not rank first: it was built by the rubric scoring it, so coverage is the one dimension
where the comparison is worthless. What separates `staging` is that every claim it makes about
itself is true — word budgets reconcile to the digit, arithmetic is shown, and three video
gates it could not run are recorded NOT RUN with the owner named rather than asserted as
passes. Mine self-certified a checklist row its own content contradicts, gated a bold moment as
an event when in the deck lane it is a sentence, and pushed four claims past their sources; a
deck-review skill that cannot review itself is failing at its stated job, and that outweighs
three slots of coverage. `presentation-writing` writes the best prose here by a distance, but
it has the widest content holes (no pricing, no counterparty, no timing beat), the longest
bullets, and it opens its film on a line its own cited section contradicts.

**What this rubric cannot see.** It is a fundraise checklist with a coverage bias: it rewards
having a slot and is nearly blind to whether the slot's *argument* is any good. It has no test
for whether claims in sequence constitute a proof, no notion of a time budget, no concept of a
bold moment or of motion, and nothing at all about the video lane — every scored row above is a
deck row, so each explainer was judged only by whether its content matched its deck. It cannot
tell a retellable sentence from a merely correct one, or judge whether a diagram is redrawable,
only that one was described. It is blind to transport-schema fidelity — `presentation-writing`
marks an `accumulate` scene as a peak, which may or may not be legal under the motion-role
vocabulary, and I have no standing to score it. And it has no fact-check: I ran the numbers
against the corpus by hand because the brief demanded it, not because this skill asks. Its
nearest check, "no unsourced market size claims", passes all three while a figure is quietly
attributed to the wrong publisher — which is exactly what my own output did. A reviewer running
only this rubric would rank by boxes filled and miss the real separator: whether a contender's
claims about itself can be trusted.

---

## Addendum — `house-guide`

Fourth contender, same twelve-slide framework, same must-pass / strength-signal / common-mistakes
checklist, same adaptation carve-outs (M4, M6, S1, X5 read as stated at the top of this review).
Key unchanged: P pass · A adapted pass · F fail.

| Check | V | Evidence |
|---|---|---|
| M1 one-liner on title | A | d1's headline is the benefit ("a tokenized asset can be made productive without giving anyone the right to sell it"), not the one-liner; the canonical sentence lands at d13 and video s9, **verbatim in both**, and `messaging.md` §1 publishes a ten-word form and a BD form beside it. Strongest repetition discipline after `presentation-writing`'s |
| M2 quantified problem | **F** | The problem beat is d2–d4 and it carries one figure — $12.9B / ~300% YoY, which sizes the *asset* side, not the cost. d3 is three quotations; d4's dollar figure is withheld by the file's own number gate. Morpho's $620M, Horizon's $423.5M and Mango's $116M are all in the corpus, all marked SHIP in its own trace table, and none is used to price the problem. A must-pass row, and the only contender to fail it |
| M3 solution tied to problem | P | d5 turns on the exact mechanism d3 quotes; d7's identity answers "cannot liquidate its position in a single onchain transaction" clause for clause |
| M4 market size, sourced | A | d2 and d9 give position, not size; no TAM anywhere; `NOTES.md` Q4 logs the refusal and its reason |
| M5 team credentials | **F** | Entity only ("AAA Flowers S.A. (Panama)", d1 and d13). No founder, no credential, in any of the four files — not even in NOTES. Third contender in a row |
| M6 clear ask | A | d12: one hour, your risk and product leads, one named underlying — and it states what is not being asked (allocation, commitment, capital). Ties `pitch-deck-mastery` for the cleanest ask in the leg |
| S1 traction trajectory | A | Correctly absent; d11 is the build state and the five things that do not exist, with counsel's non-review named |
| S2 named logos | **F (by rule)** | Franklin Templeton, WisdomTree, Invesco and BlockBooster appear on no slot and in no scene, under a standing rule that "prospect names are claims" (`messaging.md` §7, `assumptions`). The rule is the right call — the corpus has them as pilot conversations — and the row still fails, because the strength signal is *named logos on a slide* |
| S3 unit economics | **F, and self-inflicted** | The 5–10bps fee is marked **SHIP** in this contender's own number gate (`messaging-guide-medici.md` §7, "Fee · consistent · SHIP") and then appears on no slot, no scene, and in no pillar. Both halves were available; only the cost half (d10's drift decomposition) shipped |
| S4 honest competition | P | d9 carries a mandatory losing row — "THE ROW WE LOSE, and it is not cut: secondary depth. The venue has a live market; we have a market-maker agent, no live users" — with the axes declared as the audience's. Ties `staging` for best in the leg |
| S5 "why now" insight | **F** | No timing slot. d2's $12.9B / ~300% is staged as a fact about the buyer's world, and the note under it says so ("no mechanism, no chain, no product yet") |
| X1 10-word bullets | F | Mean ~22 words across 40 supporting points; d3's first and d9's second are 45-word block quotations. Better than both rivals that failed this, still a fail |
| X2 unsourced market size | **P — best in the leg** | Every figure carries file + slide + as-of *in visible text*, and three are refused with a stated reason. It is also the only contender that catches the $840M attribution problem I failed on: its gate marks the figure "via KuCoin's summary" and then declines to use it, preferring the report's own venue figures |
| X3 "no competition" | P | d9 concedes the row; `messaging.md` O3 concedes "today: nobody" on the other leg |
| X4 vanity metrics | P | −1.25%/yr is the bold moment itself, labelled third-party, ETH-only, nine-year, on the slot |
| X5 ≤15 slides | P | 13, no appendix — and the appendix material my own contender shipped (ERC-3643, the identity manifest) is explicitly cut here |
| X6 generic team bios | P (vacuous) | No bios at all — see M5 |
| Framework coverage | 9/12 | Missing: 4 Why Now, 8 Business Model, 10 Team. Nothing invented in their place, and each omission is logged |
| Headline = takeaway | P | All 13 are declarative insights; the helicopter chain is written out in the gates block and genuinely stands alone |
| One idea per slide | **F** | d8 carries the single price read, atomic settlement *and* privacy; d6–d8 is one mechanism spread over three slots |

**Scores (brief's goals):** 1. one repeatable sentence — **8**; 2. RWA value prop — **8**;
3. mechanism + one redrawable diagram — **9** (d6 is the only slot in the bake-off that *requires* a
worked instantiation — one deposit, one strike, three prices, three payouts — and d7 is the identity in
two rows; but there is no `diagram:` field, so the picture itself stops at `messaging.md` §4).

**Top 3 findings**

1. **The buyer's cost question is missing from the transport for the third time in four contenders —
   and this one refused it after passing it.** Its own gate marks the fee SHIP; no slot carries it, so
   six design contenders again ship a deck that never says what it costs to hold. *Fix:* put "5–10 basis
   points per transaction, no Medici token, fee schedule under multi-sig" (`canton-pitch-deck.md`
   Slide 7, as-of July 2026) on d12, beside the ask where a buyer asks it.
2. **The problem beat is unquantified.** Per-figure the withholding is defensible every time; in
   aggregate a risk lead leaves d2–d4 with no magnitude for the thing being solved, which is the one
   thing the must-pass list will not trade. *Fix:* bring Morpho's $620M+ at 87% utilisation onto d3 (its
   own gate marks it SHIP WITH AS-OF) and pull the Horizon figures forward from d9 to d3 — the problem's
   scale and the demand's are the same evidence, and d9 keeps them for the comparison row.
3. **No counterparty and no "why now", for the fourth time in four.** *Fix:* fold the founders'
   credential lines (`canton-pitch-deck.md` Slide 10) into d12 — a risk lead evaluating a novel payoff
   from an unknown Panamanian entity asks the counterparty question whatever the genre — and re-cast d2
   from a growth fact into the timing insight it already supports: the asset side arrived while every
   venue that will take it still prices a liquidation threshold.

**Revised ranking**

**1. `staging` · 2. `pitch-deck-mastery` · 3. `house-guide` · 4. `presentation-writing`**

`house-guide` enters third and displaces `presentation-writing`, which it beats on the ask, the
competition row and provenance while matching its holes. It does not go higher on this rubric, and the
reason is worth stating plainly: this is a coverage checklist, and `house-guide` is the contender that
deliberately empties boxes — the logos it refuses on principle, the fee it marks SHIP and then omits,
the problem figures it withholds — so it fails two must-pass rows where `staging` fails one and I fail
none. That is also the clearest demonstration yet of what this rubric cannot see. `house-guide` is the
only artifact in the bake-off whose every claim about its own numbers is true, with a trace table that
records three refusals and their reasons, which is precisely the discipline whose absence I identified
as my own worst failure — and the checklist scores it *down* for it, because a refused figure and a
missing figure look identical from here. The one place it fails on my own terms rather than the
checklist's is the "first number arrives at d10" line, which d2 and d9 contradict; that is the same
false-self-certification defect I marked as the separator, and it is why third rather than second.
