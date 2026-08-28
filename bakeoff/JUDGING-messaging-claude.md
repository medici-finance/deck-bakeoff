# JUDGING — messaging leg (Claude)

Judge: Claude, 2026-08-27. Independent; written before Ian's verdict and without reference to it.
Read: `BRIEF.md`, `bakeoff/PROTOCOL.md`, all five `source/medici/*.md`, `source/brand/house-brand-guide.md`,
all nine files under `messaging/{staging,presentation-writing,pitch-deck-mastery}/`, and the three SKILL.md
bodies (+ `staging/references/slide-functions.md`, `presentation-writing/references/scaffolds.md`).

**Scoring convention.** (a) *tool difficulty* is scored **inverse**: 10 = the tool fit the job with little
adaptation and logged its friction honestly; low = heavy adaptation. All three NOTES.md files are unusually
good, so the axis is mostly measuring **fit**, not candour.

**Headline finding on correctness.** I ran every numeric token in all six deliverable files against the
corpus. **Zero invented content figures in all three contenders.** Every number that does not appear in
`source/` is staging metadata (energies, runtime shares, word budgets, per-slot seconds). That is a clean
sweep and the brief's hardest constraint held everywhere.

---

## 1. Per-contender scorecards

### `staging` — 9 / 8 / 9

**(a) Tool difficulty — 9.** ~10.5 min, single pass, two mechanical fixes caught by running its own
arithmetic. This is the only contender whose skill was *built for this job*: genre→audience→arc, a closed
function vocabulary, a motion governor, and `staging.yaml` as its native deliverable. Friction is real but
small and well-named: no `sources:` / `objections:` / `vocabulary:` / `provenance_conflicts:` fields (all
four had to be invented as extensions), and — the sharpest self-criticism in the bake-off — the deck landed
at 14 slots partly because 14 is the count at which the 40–50% bold-moment window is satisfiable, i.e. the
arithmetic led the argument for one pass. Three video gates (`motion_spec_locked`, `seams_declared`,
`render_and_look`) are recorded **NOT RUN** with the owner named rather than fudged to pass; that is the
correct call and the only contender that had to make it. It also ran seven machine checks on its own output
(YAML parse, ≤12-word claims, declared-vs-actual VO words, second sums, wpm band, motion arithmetic) — I
re-ran all of them and they hold.

**(b) Representation quality — 8.** All three educational goals covered; the mechanism gets one slot (d8)
carrying the whole payoff identity as arithmetic, plus the single largest video scene (s6, 60 words / 24 s =
20% of runtime). Citation discipline is the highest of the three — a `source:` on *every* slot and *every*
scene. The one-diagram spec in `messaging.md` §4 includes an explicit redraw test ("a bar that always stays
full, split by a line that moves once you cross the strike"), which is the best statement of goal 3 produced.
Two deductions. First, a factual wording slip: pillar 2 says "the holder keeps the underlying **and** keeps
N" — the underlying is in the vault; the holder keeps *N*, and the proceeds of the P sale. Second, d14
paraphrases the house canonical sentence ("No liquidation price exists, because the payoff function has
none") where `house-brand-guide.md` §0.8 says reuse §8.3 *verbatim* across surfaces. Emphasis note: the
problem block is 50% of the deck's time budget. That is defensible for an educate-first genre and the
playbook's floor is 30%, but for a room that is being taught what Medici *is*, half the deck on the market's
problem is a choice a buyer may not thank it for.

**(c) Contract fitness — 9.** Every `function` value is inside the closed 16-term vocabulary; every slot
carries `claim` + `beat`; 5 transitions; both lanes present; bold placement **derived per lane** (deck 42.9%
by index, video from that lane's own `runtime_shares` → 24–42 s window) rather than one percentage inherited
across media. Claims: 23 of them, longest exactly 12 words. Video arithmetic is exact — declared words ==
actual on all nine scenes, seconds sum to 120 exactly, 299 words against a 300-word budget, per-scene
delivery 144–156 wpm. The EVENT/CONDITION peak walk (event_count 1 → one rupture budget) is the only piece
of reasoning in the bake-off that *derives* emphasis rather than asserting it. Deduction: the diagram spec
lives in `messaging.md`, not in the contract the design contenders are told to consume — a design contender
that reads only `staging.yaml` gets no diagram guidance at all.

### `presentation-writing` — 6 / 8 / 7

**(a) Tool difficulty — 6.** ~10 min, but with substantial adaptation. The skill gates on a human **four
times** (Phase 2 "do not proceed until the audience is confirmed"; Phase 3 scaffold verify; Phase 5 density;
Phase 6's "not optional" closing prompt) and has **no recorded-assumption escape**, so an unattended run
fakes four confirmations. Phases 7–8 pull hard toward building a `.pptx` with the skill's *own* default brand
(Inter + IBM Plex "Bauhaus", hex codes, tracking values) — a direct collision with the bake-off's design
layer; there is no mode that stops at the outline. No provenance field anywhere (its only data discipline is
25 lines on transposing spreadsheets — "the check that mattered was not the one the skill runs"). It has no
concept of video at all: the entire kinetic vocabulary in its `staging.yaml` is borrowed from
`staging/references/motion-roles.md`, which it declares. Its NOTES §5 also flags, correctly, that this skill
is the only one in the messaging set shipping **no LICENSE**.

**(b) Representation quality — 8.** The most brand-faithful contender: it is the only one to reuse §8.3's
canonical sentence *verbatim*, at slot 1 and again at slot 14, which is exactly what §0.8 asks for. Most
mechanism airtime of the three (deck slots 6+7; video scenes 5+6 = 44 s of 132 s = 33%). Best honesty
placement — slot 11 carries "Canton appears nowhere in the RedStone lending report" as a bullet on the
why-Canton slide, and slot 10 is an entire slide disqualifying the product for near-zero-vol collateral. Its
NOTES §2.5 explicitly resolves the skill's "one moment of personality per 5–7 slides" rule against
`house-brand-guide.md` §8.1 by making the personality *candour* rather than wit; that is the right reading
and it produced the two best slides in the leg. Deduction: the §1 "repeatable line" is 38 words and fails
educational goal 1 on its own terms — a sentence the room can repeat is not 38 words long. The 10-word short
form rescues it, but the headline artifact is the long one. Minor over-claim: "enforced by the contract that
records the split" (video s5) goes a step past the corpus's "closed-form invariant proofs, pure tests".

**(c) Contract fitness — 7.** In-vocabulary functions throughout; all 14 claims ≤12 words; the richest
transition set (13, one at every boundary) and the only one that writes the *spoken* bridge for every seam.
Deductions: the deck time-shape is `600 s / 14 = 43 s`, which counts cover and end as content slots (staging
excludes them; the note "cover and end run short" concedes the point); declared VO word counts are off by
exactly one on **every** scene (301 declared vs 308 actual) and per-scene delivery swings 120–157 wpm against
a declared 137, so some scenes will feel rushed and some slack; **two** mechanism slots where the genre rule
is one; and the bold moment sits at slot 7 / 50%, *inside* the solution and after the pivot — most bold-moment
rules put it at the last problem beat, before relief. That is a defensible choice (see §2) but it is a
contract a design contender will render with the loudest frame on the answer rather than the stakes.

### `pitch-deck-mastery` — 5 / 7 / 6

**(a) Tool difficulty — 5.** ~12 min, and the furthest tool from the job. This is a fundraise skill in every
line: its trigger list is "investor presentations, fundraising decks, demo day slides"; its axis is pre-seed →
Series B+; its must-pass checklist demands TAM/SAM/SOM, a traction chart, and "clear ask (amount + use of
funds)"; its research loop tells Claude to `web_fetch` ten investor-facing sites. **Nine** distinct fundraise
assumptions had to be adapted — Market Size replaced by "where is the collateral", Financials replaced by a
risk register, Traction repurposed to "what is built and the five things that do not exist", the raise
replaced by a modelling conversation, the research loop not executed. It has **no bold-moment concept**
(bridged to one line about "the aha moment"), **no motion vocabulary**, no risk-register slot, no
two-sided-instrument slot, no lane/medium concept, and no terminology governance. That said, its NOTES is the
single most useful document in the leg: the nine-row adaptation table is exactly the artifact a bake-off
exists to produce, and its observation that the skill "would score that [disclosure] slide as a weakness" is
the sharpest thing anyone wrote about tool–brief mismatch.

**(b) Representation quality — 7.** Best on educational goal 1: "Medici splits a tokenized real-world asset
into two claims that always sum back to it, so the position can never be force-sold" — 22 words, plus a
handshake form ("Collateral splitting with no liquidation price"). It is also the **only** contender to carry
both corpus contradictions in the body of `messaging.md` (§5, "carried openly rather than smoothed") instead
of burying them in a YAML `assumptions:` block a reader may never open. It adds two things the other two
missed that this audience genuinely needs: slot 6 ("who buys the other leg" — the second question in any room
for a two-sided instrument, which the other two leave in reserve objections) and slot 11 (an itemised risk
register, the slide a risk lead actually reads). It is the only one to use `authorization-pitch-deck.md`.
Deductions: it keeps the brief's MMF/treasury framing as lead and demotes the volatility caveat to a
supporting bullet on slot 6, where its own corpus says treasuries are the wrong first underlying; the
Canton-distribution counter appears in `messaging.md` O5 but **nowhere in the deck lane**; and slot 8 says
Franklin Templeton, WisdomTree, Invesco and BlockBooster "already issue here", where the source only has
BlockBooster *joining the Canton Foundation* — the one place any contender strengthened a source claim.

**(c) Contract fitness — 6.** The weakest transport artifact, and the problem is mechanical rather than
editorial. Deck slots use `headline:`, not the schema's `claim:`. Nine of its fourteen `function` values —
`problem`, `solution`, `proof`, `application`, `timing`, `context`, `risk`, `commercial`, `close` — are
**outside** the closed vocabulary the design layer keys on. There is no `beat` on any slot and **no
`transitions` block at all**. Slot 4 carries a `diagram:` field describing a payoff chart with axes, which
breaches the composition contract's rule 1 ("staging never names a chart type") — though it is simultaneously
the most immediately actionable field any contender wrote. An `appendix` slot (A1) sits outside the 13,
leaving design to decide whether it renders. Video scenes carry no per-scene word counts (declared 332, actual
334) and scene 5's VO contains a `[2 s hold]` stage direction inline, which a naive consumer will read aloud.
Credits: exactly one bold moment, correctly at the deck's 38% and the video's 53–68%; the clearest ask slot in
the leg (slot 13 states what is *not* being asked for: capital, custody, commitment); and the honest
`note_on_arrest_at_ceiling` resolving R3-vs-`arrest` as an ordering rather than pretending it away.

> **Stage-2 hazard, flagged now:** the three `staging.yaml` files are **not schema-interchangeable**. A design
> contender that parses `slots[].claim` + `function` against the closed vocabulary will run clean on `staging`
> and `presentation-writing` and break on `pitch-deck-mastery`. Design contenders should be told to map
> `headline`→`claim` and to treat PDM's function names as free-text before stage 2 starts.

---

## 2. Cross-contender comparison — same story, different emphasis and order

**They tell the same story.** All three converge on: one position → two claims → they always sum back → so
no liquidation price; the value prop as (no forced sale / income on an asset you keep / Canton's privacy,
atomicity, no-gas); and the mechanism as the `S ≥ x` / `S < x` payoff table with the invariant as the thing
to remember. All three reuse the same five proof points, the same five objections, and the same terminology
canon. Convergence is not luck: the brief pre-specifies the one-liner, the value prop and the mechanism as
three named educational goals, and the corpus is strongly opinionated. The interesting divergences are four,
and every one traces to methodology.

**Divergence 1 — the one-liner.** PDM's is shortest (22 words) because its framework's slide-1 guide demands
a "one-liner ≤10 words" that passes the "mom test", so it optimised for compression. PW's is longest (38
words) because The Keynote's slide 4 is "The Reframe — your thesis… one sentence, said clearly", which
rewards a *complete* thesis over a repeatable one; PW then compensates by reusing §8.3 verbatim as the
spoken line. `staging` sits between because its `audience.md` read declared **read-fallback**, so every claim
had to be a complete standalone sentence.

**Divergence 2 — the bold moment.** `staging` picks **Black Thursday, March 2020** — a dated event in the
problem block, at 42.9% by index, strictly before the first `move` slot. That is the executive-explainer
playbook's placement rule plus the GATE's requirement that the bold moment be "a *thing that happens*, not a
strong sentence", plus its EVENT/CONDITION peak walk, which found exactly one EVENT claim in the whole film
and therefore exactly one rupture budget. PW and PDM independently converge on the **opposite** choice: the
liquidation line drawn and then refused. PW places it at slot 7 / 50%, *inside* the solution, because The
Keynote scaffold has no problem-side rupture — its emotional peak is structurally "The Reframe… the slide the
audience remembers". PDM places it at slot 5 / 38% because it bridged to the only emphasis line its skill
contains ("highlight the aha moment"), which lives in the *Product* slide guide. So: one methodology derives
the peak from the claim types and lands on borrowed real-world pain; two methodologies inherit a
solution-side peak from their scaffolds and land on a demonstration. **PDM's video version is the best single
idea in the leg** — scene 2 completes the liquidation gesture and destroys a position, scene 5 begins the
identical gesture and stops mid-motion — and it is PDM's invention, not its skill's.

**Divergence 3 — value prop before or after mechanism.** PDM front-loads: problem is one slot (~15%), then
solution + mechanism + proof at slots 3–5, value prop at 6–9. That is the 12-slide framework's
Problem→Solution arc executed literally, with "make the investor feel the pain **before** revealing the cure"
compressed because there is no round to sell. `staging` inverts it: 50% of the deck is problem, the mechanism
lands at slot 8 (57%), and the venue value prop comes *after* it at d10 — a direct consequence of
executive-explainer's `problem_share ≥ 30%` gate and its `one_mechanism` gate, which forbids spending slots
building up to the mechanism twice. PW interleaves because it borrowed Workshop *components 1–3* for the
mechanism, which is inherently a multi-slot teaching structure — that is also exactly why PW is the only
contender with **two** mechanism slots.

**Divergence 4 — the 54-vs-36 and MMF-vs-gold contradictions.** On the template count all three reach the
same answer (54, per the brief's source priority) and all three log it, but they log it in three different
places: `staging` and PW in the YAML `assumptions:` block, PDM in the body of `messaging.md` where a reader
will actually see it. `staging` and PW both independently notice the thing that matters — the
asset-manager deck carries the **later** revision date (2026-07-18) with the **lower** number, so the priority
rule may be selecting the stale figure. On MMF-vs-gold the three genuinely diverge: PW promotes it to a
headline claim on its own slot 10 ("The collateral this fits is the collateral institutions already rotated
into") and flags in NOTES Q8 that "a human may want to overrule this — it is the only place where I chose a
research document's conclusion over a pitch deck's framing"; `staging` resolves the same way but places it in
the *ask* slot (d13) and objection 2; PDM keeps the brief's MMF framing as lead with the caveat as a
supporting bullet. Trace: `staging`'s `audience.md` lists "a comparison table where the presenter wins every
row" as this buyer's reflex distrust, which pushes disqualification into the arc; PW's Keynote scaffold turns
on "The Crack", so a slide that breaks its own case is native to it; PDM's checklist has no vocabulary for
self-disqualification at all — its own NOTES says the skill "would score that slide as a weakness" — so the
honesty had to be added against the framework rather than by it.

---

## 3. Recommendation

**Adopt `staging` as the house default for product pitches.** It is the only contender whose native output
*is* the transport contract, and it is the only one a reviewer can re-run: closed-vocabulary functions,
`claim` + `beat` on every slot, per-lane derived bold placement, an exact video arithmetic (299/300 words,
declared == actual on every scene, 144–156 wpm), a motion budget that derives emphasis from claim types, and
gates that are recorded NOT RUN rather than fudged. Its editorial output is the second-best of the three; its
contract is decisively the best, and the contract is what the next six contenders consume.

**Borrow, before the next run:**

- **From `presentation-writing`:** (1) reuse `house-brand-guide.md` §8.3's canonical sentence **verbatim** at
  the cover and the end — `staging` paraphrases it and should not; (2) promote the collateral-fit
  disqualification from `staging`'s ask slot to a slot of its own with a headline claim; (3) its
  transitions-at-every-boundary discipline (13 vs 5).
- **From `pitch-deck-mastery`:** (1) a **who-buys-the-other-leg** slot — a two-sided instrument that leaves
  that in reserve objections loses the room; (2) an itemised **risk register** slot, which is what a risk lead
  reads; (3) the twice-performed liquidation gesture as the video's bold moment (it is compatible with
  `staging`'s grammar as an R4 rhyme, and it is better than borrowing MakerDAO's pain); (4) carry corpus
  contradictions in the **body** of `messaging.md`, not only in a YAML `assumptions:` block.
- **Into the skill itself:** `staging` needs four fields it had to invent as extensions —
  `source:` per slot, `objections:`, `vocabulary:` (terminology canon), and `provenance_conflicts:` — plus a
  `sources:` block with a priority order. It has no notion of a *corpus*; that gap is why the 54-vs-36 call
  had to come from the brief rather than the skill.

**Top three issues a human must rule on before any of this goes external:**

1. **54 vs 36 DAML templates** (and ~5,700 vs ~5,100 LOC; ~2,900 vs 2,600 lines of regulatory analysis). All
   three contenders used 54 on the brief's priority rule — but `asset-manager-pitch-deck.md` is the *later*
   revision (2026-07-18 vs 2026-07-04) and says *less*. If 36 is the true count, every deck in this bake-off
   overstates the build on a first-contact slide, which is precisely the class of error a diligence process
   kills a conversation over. Ian states the number; the priority rule does not get to decide this one.
2. **"$344B represented / $2T-a-month repo / the #1 RWA network."** This is Medici's own deck asserting it
   with no external citation anywhere in the corpus, and it sits directly against `rwa-redstone-2026.md`'s
   repeated finding that **Canton appears nowhere** in either part of the 2026 RWA-lending map. All three
   contenders put it on a slide, two of them inside a headline claim, and only `presentation-writing` puts the
   counter on the same slide. Needs a source, or a hedge, before it leaves the room.
3. **Which underlying the pitch names.** The brief's product story leads with "MMF share, tokenized
   treasury"; the corpus's own research says near-zero-vol treasuries are the *wrong* first underlying (T-bill
   collateral −92% from a ~$194M peak while gold grew 7×) and names tokenized gold. `staging` and
   `presentation-writing` disqualify MMF collateral on a slide; `pitch-deck-mastery` keeps the MMF framing.
   This is a positioning ruling, not a fact-check, and it changes what the deck is — but it cannot be left to
   three contenders to decide differently.

*Runner-up flag, not top-three:* the canon's unhedged "can't be liquidated" sits one sentence from "P's value
declines with no floor" in all three decks. Every contender obeyed the canon correctly and disclosed the cost;
whether that pairing survives a compliance read for an external RWA audience is a counsel question, not a
messaging one.

---

# Revision 2 — four contenders + cross-review synthesis

Added 2026-08-27 after `messaging/house-guide/` landed and after the four rubric reviews under
`reviews/messaging/`, each now carrying a `house-guide` addendum. (a) is inverse-difficulty, i.e. fit.

## 4. `house-guide` — 6 / 9 / 8

**(a) Tool difficulty — 6.** ~18 min, single pass. On the comprehension-and-copy half it is the best-fitting
tool in the leg: §1's nine failures transferred to a different product almost unchanged, and the first pass
over the corpus produces the understanding and the deliverable at once. On the other half it does not fit at
all — **the method has no transport format**: no slot count, ordering, timing, bold moment, motion vocabulary
or genre, so the entire `staging.yaml` was built by mapping prose sections onto another skill's field names.
Five rules did not transfer and all five are written up (`NOTES.md` §3) — chiefly that B8 collides head-on
with brand §8.1 principle 4 and is resolved as a *scope* rule rather than a hedging rule. That log is the
most useful methodology artifact the bake-off has produced, `pitch-deck-mastery`'s nine-row table included.

**(b) Representation quality — 9.** The highest editorial ceiling here. The only contender that *mandates a
worked example* (d6: one deposit, one strike, three prices, three payouts) — the gap every rubric marked
against everyone else. Its number gate is the strongest artifact anyone produced: a verdict per figure, as-of
dates in visible text rather than footnotes, three explicit WITHHOLD rows (54-vs-36 templates, unpublished
full-period gross theta, the single-sourced $8M), three standing rules added back to the method, and it is
the only contender to catch that $840M is KuCoin's summary of the RedStone report rather than the report and
then decline the figure. It also has the only real gloss table and the only rule refusing prospect names.
Deductions — three statements in `staging.yaml` disagree about
when the first number arrives (`diagnosis_carried.b3`, the `sequencing` gate, d10's note) and d2/d9 contradict
all three; the `glossary` gate certifies PASS over a d10 shipping "net drift", "Deribit" and "Black-Scholes at
mid" unglossed against its own §5 row for *drift*; the analogies and the diagram spec never enter the
contract; the 5–10bps fee is marked SHIP in its own gate and appears on no slot; and "AAA Flowers S.A.
(Panama)" is the only cover entity spent twice (d1 and d13).

**(c) Contract fitness — 8.** 13/13 deck functions and 9/9 scene functions inside the closed 16;
`claim` + `beat` + `source` on every slot and scene; all 13 claims complete standalone sentences; the
mechanism run declared one unit; `ask`+`end` adjacent; every beat boundary typed, one `turn`, `gate` before
the ask; bold placement **derived per lane with the arithmetic shown in both** (only `staging` also does
this); video arithmetic exact (271 words against 275, seconds sum 110, 140–158 wpm per scene); a full motion
budget, EVENT/CONDITION walk and ornament gate; `render_and_look` recorded NOT RUN with its owner. Deductions: `genre: product-explainer` is outside
the closed seven and there is **no `classify:` block at all**, so kill-conditions were never re-checked; 12 of
13 claims exceed the 12-word cap two rivals held; three `mechanism` slots; the bold moment sits at 76.9% by
index, behind the relief; still no `diagram:` field.

## 5. Cross-review matrix

Rank each rubric's reviewer gave each contender (`reviews/messaging/*`, addenda included):

| Reviewer rubric | `staging` | `presentation-writing` | `pitch-deck-mastery` | `house-guide` |
|---|---|---|---|---|
| by-staging (structural) | **1** | 3 | 4 | 2 |
| by-pitch-deck-mastery (structural) | **1** | 4 | 2 | 3 |
| by-presentation-writing (comprehension) | 4 | 3 | **1** | 2 |
| by-house-guide (comprehension) | 4 | 3 | 2 | **1** |
| rank sum | 10 | 13 | 9 | **8** |

**The 2–2 split is real and it is not noise.** The two rubrics that grade *structure* — `staging`'s argument
grammar and `pitch-deck-mastery`'s coverage checklist — both put `staging` first, from opposite directions
but for one reason: it is the contender whose every claim about itself reconciles (word budgets to the digit,
per-lane derived placement, three video gates recorded NOT RUN rather than fudged), and structural rubrics
can check that. The two that grade *comprehension* both put `pitch-deck-mastery` at or near the top, because
it reaches the whole product fastest (mechanism at 31% of the deck against 43%, 46% and 57%) and is the only
contender carrying the redrawable picture *through* the transport in a `diagram:` field — precisely the field
the structural rubrics call a composition-contract breach. That is the whole disagreement in one artifact:
the same field is its best idea and its disqualifying leak, depending on who holds the pen. `house-guide`
lands second on three of four and first on the fourth, and is the only contender no rubric places worse than
third — the lowest rank sum, and the only artifact both camps can live with. Two caveats: two of the four are
self-reviews placing themselves first (both disclosed), and `house-guide` arrived last, having read the rest.

## 6. What every reviewer agreed on

1. **No invented numbers, in any of the four.** Every content figure traces to a named file and slide; the
   only unsourced numbers anywhere are staging metadata. Four independent fact-checks, one result.
2. **54-vs-36 templates (and 2,900-vs-2,600 lines) is unresolvable from the corpus.** Three take 54 on the
   brief's priority rule and log the conflict; `house-guide` withholds both and says "the contract set". All
   four note that the *later* revision carries the *lower* number.
3. **Unglossed jargon survives every method.** "No gas, no MEV, no mempool" ships bare in three of four;
   `house-guide` clears those and then ships "net drift", "Deribit", "Black-Scholes at mid" bare on its cost
   slot. Every rubric flagged it; no contender's own gate caught it.
4. **The fee is missing from the transport in three of four.** 5–10bps per transaction, no Medici token,
   multi-sig fee schedule — only `pitch-deck-mastery` puts it on a slot (S12); `house-guide` marks it SHIP in
   its own gate and omits it. Otherwise six design tracks ship a pitch that never says what it costs.
5. **"AAA Flowers S.A. (Panama)" on the cover.** `staging` d1, `pitch-deck-mastery` slot 1, `house-guide` d1
   *and* d13. `asset-manager-pitch-deck.md` line 267 says that entity triggers automatic OFAC/sanctions review
   at US institutions; spending it in the first ten seconds buys nothing.
6. **MMF-vs-gold is a positioning fork, not a fact-check.** `presentation-writing` disqualifies MMFs on a
   slide, `staging` in the ask, `house-guide` names the *requirement* and refuses to name an underlying,
   `pitch-deck-mastery` keeps the MMF framing. Four methods, four answers, one question.

## 7. Recommendation, revised

**Adopt `staging` as the transport and `house-guide` as the content gate — one pass, not a pick.** Revision
1's call stands on the contract: `staging` is still the only contender with a legal genre, a `classify:` block
carrying its rejections, one mechanism slot and a bold moment in front of the relief, and the contract is what
six design tracks consume. But `house-guide` beats it decisively on the editorial layer (9 vs 8), so its §7
number gate (verdict per figure, as-of in visible text, WITHHOLD as a legal outcome) and its §5 gloss table
become required blocks in `staging.yaml`, and scene→value→mechanism→honest-boundary the default arc check.

**Borrow, naming the slot and the device:**

- **`pitch-deck-mastery` slot 4's `diagram:` key** → onto `staging` d8, carrying `house-guide` `messaging.md`
  §4's spec verbatim ("the top of the stack is a flat line all the way across, at the value of the
  collateral… the eye should find it before it finds anything else"). It is the only device that gets goal 3
  through the handoff, and it is legal written as a *redraw spec* rather than a chart type.
- **`house-guide` d6's `WORKED EXAMPLE, required` line** → onto whichever mechanism slot survives.
- **`pitch-deck-mastery`'s video s2→s5 arrest** (the liquidation gesture completed, then begun and refused
  mid-motion) → legal under `staging`'s grammar as an R4 answering rhyme, and better than MakerDAO's pain.
- **`presentation-writing`'s covered-call analogy with its break** → onto the objection slot; its
  **speaker-note discipline** onto every slot — two of four contenders ship no presenter track at all; and
  **`pitch-deck-mastery` S12's fee line** onto the ask slot, in every future run.

**Human rulings needed** (1–3 restate Revision 1 unchanged; 4–6 are new):

1. **54 vs 36 templates**, ~5,700 vs ~5,100 LOC, ~2,900 vs 2,600 lines of analysis — the one question no
   contender could close (`house-guide` NOTES Q1 says so outright). Ian states the number.
2. **"$344B represented / $2T-a-month repo / the #1 RWA network"** — single-sourced, no external cite, and in
   tension with the RedStone report's finding that Canton appears nowhere in the lending map.
3. **Which underlying the pitch names** — MMF/treasury or gold. A positioning ruling; four methods, four answers.
4. **May the Panama entity appear on the cover?** Three of four put it there and the corpus says it triggers
   sanctions review at US institutions. Counsel or Ian, not a messaging call.
5. **Does the fee go on a slot at all**, given the educate-first framing? Decide once, for all six tracks.
6. **Implied full-period gross theta ≈ −0.05%/yr** (`house-guide` NOTES Q2, from the published net −1.25% and
   roll −1.2%). If that holds, the "income" framing rests on execution improving rather than on the backtest.
