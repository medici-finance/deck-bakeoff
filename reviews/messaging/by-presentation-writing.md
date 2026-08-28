# Messaging bake-off review — reviewer: `presentation-writing`

**Rubric**: `/Users/iholsman/jojig/Lending/rwa-bakeoff/skills/messaging/presentation-writing/powerpoint-keynote-presentation/SKILL.md`
+ `references/scaffolds.md`. Only principles that skill defines are scored below.
**Fact-checked against**: `/Users/iholsman/jojig/Lending/rwa-bakeoff/source/medici/` and `source/brand/house-brand-guide.md`.
**Reviewed**: `/Users/iholsman/jojig/Lending/rwa-bakeoff/messaging/{staging,presentation-writing,pitch-deck-mastery}/`.
Bullet counts and word lengths below are measured from each `staging.yaml`, not eyeballed.

---

## 1. `presentation-writing` (my own output) — `messaging/presentation-writing/`

| Principle | Verdict | Evidence |
|---|---|---|
| Scaffold diagnosed, not menu-offered (Ph.3) | **Pass** | `outline.md` §Phase 3: Keynote chosen, Workshop 1–3 and Close's objection beat borrowed, Pitch/Case/Report-Out rejected with a reason each. |
| Audience diagnosed + verified (Ph.2) | **Pass w/ flag** | `outline.md` Phase-2 table; the skill's "do not proceed until confirmed" gate is unmet — logged as Q1–Q2 in `NOTES.md` §3, not silently skipped. |
| One thesis per slide, declarative (rule 1) | **Fail** | Slot 1 claim is `"…two claims that always sum back"` — the object is truncated off by the 12-word cap. Incomplete sentence, and design renders it verbatim. |
| Three bullets maximum (rule 2) | **Pass** | 14/14 slots at ≤3 supporting points. Best of the three. |
| Bullets are fragments, not paragraphs (Tone 7) | **Fail** | Mean 19 words/bullet, max 34 (slot 7). Slot 7's third point is a stage direction ("…is drawn — and there is no reference price…so it has to be taken away"), not slide copy. |
| No orphan slides — transitions written (rule 3) | **Pass** | 13 transitions for 13 boundaries, each typed and phrased (`staging.yaml` `transitions`). Only contender at full coverage. |
| Front-load the hook (rule 4) | **Fail** | First content slot is a market-size slide; the visceral beat (Black Thursday) is slot 4 = 29% in. Slot 2 is stakes-adjacent, not stakes. |
| End with an ask or charge (rule 5) | **Pass** | Slot 13 ask ("name one position, we size it, then try to break the payoff"), slot 14 charge. No "Questions?". |
| Cut ruthlessly (rule 6) | **Fail** | Slots 1, 5 and 6 each assert the split/sum-back idea. My own cut test in `outline.md` flagged only slot 11 and cleared the redundancy. |
| Density decision surfaced (Ph.5) | **Pass** | Flexible declared in `outline.md` §Phase 3 and `NOTES.md` Q4, with the single-statement slots named (5, 14). |
| Four pressure tests run (Ph.6) | **Pass** | so-what / drunk / cut / order all written out, deck and video, with a flag rather than a clean sweep. |
| Speaker notes: conversational, why not what (Ph.7) | **Pass** | Per slide, 2–3 sentences, presenter-facing ("Say the negative number out loud before anyone asks for it"). |
| Concrete over corporate; earned abstractions (Tone 2/4) | **Pass** | Every abstraction carries its number and file/slide tag; slot 10 disqualifies the product for near-zero-vol collateral. |
| AI language tells (Tone 7) | **Pass w/ flag** | No banned vocabulary. But "The honest counter", "said plainly", "Honestly, not much" is performative candour used as a personality substitute — also a `house-brand-guide.md` §8.1.6 miss. |
| Anti-patterns (agenda / history / dump / false close / hedge / Questions) | **Pass** | None present. |

**Brief's educational goals** — G1 one repeatable sentence: **7** (messaging.md's line is 32 words with three clauses; a 10-word short form rescues it, but the cover headline design actually renders is broken). G2 value prop in RWA: **9** (the market's own report is the argument; the Canton distribution gap and the collateral-fit limit are on-slide, not in Q&A). G3 mechanism/one diagram: **7** (two slots spent on it, and the diagram spec lives in `messaging.md` §4 prose — `staging.yaml` has no `diagram` field, so the design lane never receives it). **Total 23/30.**

**Top 3 findings**

1. **The cover headline ships broken.** Slot 1 = "Medici splits tokenized collateral into two claims that always sum back". *Fix*: set slot 1's claim to "Two claims that always sum back to the collateral" (9 words) and move "Medici" to the cover subtitle, which is not headline-locked.
2. **Three slots say one thing.** Slots 1, 5, 6 all state the split/invariant. *Fix*: cut slot 5 and fold "there is no threshold to cross" into slot 6's third point plus the after-slot-5 transition line; 13 slots, and slot 7 gets the extra 43s `time_shape` already admits it needs.
3. **The contract carries prose, not slide copy, and no diagram.** *Fix*: rewrite every `supporting_points` entry to ≤12-word fragments; move slot 7's stage direction into `bold_moment.form` (where a version already lives); add a `diagram:` key to slot 7 carrying `messaging.md` §4's "line with nowhere to sit" spec verbatim, so brief goal 3 reaches design.

---

## 2. `staging` — `messaging/staging/`

| Principle | Verdict | Evidence |
|---|---|---|
| Scaffold diagnosed, not menu-offered | **Pass** | `staging.yaml` `classify`: executive-explainer chosen; four genres rejected each against their own pick_when/skip_when. |
| Audience diagnosed | **Pass** | `audience.assumed_knowledge` splits vocabulary into may-use / must-explain, and caps new mechanisms at one. Sharpest audience read of the three. |
| One thesis per slide, declarative | **Pass w/ flag** | All 14 claims are complete sentences. d1's "two claims that cannot be liquidated" misattributes the property to the claims rather than the position. |
| Three bullets maximum | **Fail** | 5 of 14 slots over cap: d8 (5), d9 (4), d10 (4), d11 (5), d12 (4). |
| Bullets are fragments, not paragraphs | **Fail** | d12's first point is 35 words, d13's third is 30, d11 has two at 20+. Fully-formed thoughts with subordinate clauses — essay writing on a slide. |
| No orphan slides — transitions written | **Fail** | 5 transitions for 13 boundaries (after d2, d5, d7, d10, d12). Eight slot changes have no bridge. |
| Front-load the hook | **Fail** | d2 ("tokenization worked, assets sitting idle") and d3 (market growth) are context; the hook is d6 at 43%. That is the rubric's history-lesson opener in modern dress. |
| End with an ask or charge | **Pass** | d13 ask, d14 line to repeat. |
| Cut ruthlessly | **Pass w/ flag** | `dead_slot` gate argues a turned value per slot; d2 and d3 still overlap, and its own `assumptions` concedes a 6-minute cut would drop d5 and d10 first. |
| Density decision surfaced | **N/A → Fail** | No density concept; slot bullet counts drift 2→5 with no stated rule, which is Flexible by accident rather than by choice. |
| Four pressure tests run | **Pass (equivalent)** | `retell`, `helicopter`, `dead_slot`, `problem_share`, `sequencing` gates cover so-what/drunk/cut/order and go further (arithmetic on the time shape). |
| Speaker notes | **Fail** | None, in either lane. A deck it declares "read-fallback" and forwards ten times, with 35-word bullets and no presenter track. |
| Concrete over corporate | **Pass** | d9 concedes a row to the incumbent ("Medici has no live users") — the rubric's own anti-"we win every row" test, passed deliberately. |
| AI language tells | **Pass** | Clean on banned vocabulary; "Two honest halves" in `messaging.md` §6 is the one performative-candour touch. |
| Anti-patterns | **Pass** | No agenda, no data dump, no false close, no Questions slide. |

**Educational goals** — G1: **7** (`messaging.md` line is clean and a corridor version exists, but the deck cover says something different — "cannot be liquidated" — so the repeated sentence is not repeated). G2: **8** (d4/d5/d10 build it well; the deck never puts the collateral-fit limit on a slide — it lives in d13 and an objection). G3: **8** (d8 is the single mechanism slot and the "bar that always stays full" redraw sentence in `messaging.md` §4 is the best napkin handle produced by anyone; no `diagram` field in the contract). **Total 23/30.**

**Top 3 findings**

1. **d2 contradicts itself inside one slot.** Claim: assets "mostly sitting idle"; supporting point on the same slot: "$2T/month repo". Assets in $2T/month of repo are not idle, and "mostly sitting idle" traces to nothing — `canton-pitch-deck.md` Slide 6 says "idle assets" of a fund treasury, not of the $344B. *Fix*: re-claim d2 as "Tokenized fund shares earn their stated yield and nothing more" and move the $2T repo figure to d10, where it already appears.
2. **Three context slides before any tension.** *Fix*: promote d4 ("money markets assume collateral you can sell today; RWA collateral isn't") to slot 2 and demote d3's growth figures into its supporting points. Nothing is lost and the room is leaning in three minutes earlier.
3. **No presenter track at all.** *Fix*: add a transition line at each of the eight bare boundaries and a 2–4 sentence speaker note per slot; split d12 into "what is built" / "what is not", which also fixes the 35-word bullet.

---

## 3. `pitch-deck-mastery` — `messaging/pitch-deck-mastery/`

| Principle | Verdict | Evidence |
|---|---|---|
| Scaffold diagnosed, not menu-offered | **Pass** | `pitch.md` §1 maps all 12 framework slides to kept / re-purposed / replaced, with the stage call (seed analogue) argued from the corpus. Most transparent adaptation of the three. |
| Audience diagnosed | **Pass** | `staging.yaml` `audience` incl. `decision_they_hold` = "whether to spend an hour modelling one of their own positions" — the most operational read of the ask. |
| One thesis per slide, declarative | **Pass w/ flag** | 13 headline claims, all takeaways not labels. S1's "two claims that never liquidate" is a category error — claims do not liquidate; positions get force-sold. |
| Three bullets maximum | **Fail** | 11 of 13 slots over cap (slot 11 has 6). Only slot 1 is compliant. |
| Bullets are fragments, not paragraphs | **Pass** | Tightest copy of the three: max 20 words, most ≤13. The bullets read aloud. |
| No orphan slides — transitions written | **Fail** | No `transitions` block in `staging.yaml` and no bridging lines in `pitch.md`. 13 slots, 60+ bullets, zero connective tissue. |
| Front-load the hook (rule 4) | **Pass** | S2 is the hook: "RWA lending's hardest problem is the liquidation nobody can execute", with Black Thursday on the same slide. Best of the three. |
| End with an ask or charge | **Pass** | S13 is the last slide and the ask, and states what is *not* being asked (capital, custody, commitment). Cleanest against rule 5. |
| Cut ruthlessly | **Fail** | 13 slots plus an appendix for a 10-minute educate-first talk. S7 ("why now") re-states S2's problem and S8's placement; S12 (5–10bps) is a commercial slot the brief's ask does not need. |
| Density decision surfaced | **N/A → Fail** | Consistent-at-five is a design default, not a stated choice; the rubric's Phase-5 question is never asked or logged. |
| Four pressure tests run | **Pass (equivalent)** | The skill's own must-pass / strength-signal / common-mistakes checklist is filled in and self-adversarial (it marks the missing traction chart as deliberate). |
| Speaker notes | **Pass w/ flag** | Per slide, but several are notes-to-the-author about the framework ("the skill's competition rule is a 2x2…") rather than what the presenter says out loud. |
| Concrete over corporate | **Pass** | S9 names Aave Horizon as a working alternative with volume and says the empty quadrant is empty rather than claiming no competition. |
| AI language tells | **Pass** | Clean. "the honest benchmark" / "the uncomfortable half" is the one performative-candour tic. |
| Anti-patterns | **Pass** | No agenda, no history opener, no false close, no Questions slide; the appendix is used the way the rubric prescribes. |

**Educational goals** — G1: **9** (23-word single-chain sentence, instructed to be said at open and close, and it *is* carried verbatim into video scene 8; only the cover headline drifts). G2: **8** (S2/S6/S7/S8 cover it; the volatility caveat that decides fit sits in S6's speaker note, not on the slide). G3: **9** (S4 + S5 pair the payoff with its absence, and it is the **only** contender whose `staging.yaml` carries a `diagram:` field — the design lane actually receives the redrawable picture). **Total 26/30.**

**Top 3 findings**

1. **A false self-certification.** `pitch.md` §3 certifies "no bullet exceeds 10 words"; 35 of 60 do, and slot 11 runs six bullets at up to 18 words. A checklist that passes itself wrongly is worse than the violation it hides. *Fix*: split slot 11 into removed-risks / present-risks, push S2's RedStone quote into the speaker note, and correct the checklist row to state the measured distribution.
2. **Sixty bullets, no transitions.** *Fix*: cap each slot at three points with the rest moved to speaker notes, and add a `transitions` block to `staging.yaml` — the field does not exist, so no design contender can render a bridge even if it wanted to.
3. **An inference is presented as documentation.** `messaging.md` Pillar 2 states N demand "is the same demand RedStone documents as looping"; `rwa-redstone-2026.md` labels that mapping an inference twice ("The framing of N-as-looping-substitute is inference"). The same pillar stacks $840M against S9's $620M / $423.5M without the source's own reconciliation note (line 100). *Fix*: label the looping mapping as inference in `messaging.md`, and append the reconciliation sentence to slot 7's `source` field.

---

## Cross-cutting (fact-check, outside the rubric)

- **"AAA Flowers S.A. (Panama)" on the cover slide** — `staging` d1 and `pitch-deck-mastery` slot 1 both put it there. `asset-manager-pitch-deck.md` line 267 says that entity "triggers automatic OFAC/sanctions review at US institutions". Naming it in the first ten seconds of a pitch to US-regulated risk leads spends credibility for no persuasive gain; it belongs in the close or an appendix (where `presentation-writing` effectively left it, by omitting "Panama").
- All numeric claims I spot-checked in all three contenders trace correctly: $8M at $0, Mango $116M, $344B / $2T repo, Morpho $620M+ at 87%, Horizon $423.5M / $106M / 269, gold 7x vs T-bills −92% from ~$194M, equities under $1K, −1.25%/yr with $0.895 on $1.00, +0.57% best sub-period, −1.2% roll at ~12.2 rolls, 54 vs 36 templates. **No invented number found in any contender**, and all three log the 54/36 and 2,900/2,600 source conflicts rather than smoothing them.

## Ranking

**1. `pitch-deck-mastery` · 2. `presentation-writing` · 3. `staging`.**
This inverts my rubric's own structural scoring, and the inversion is the honest result. On the three named tests the rubric owns — three-bullets-max, the cut test, the order test — my own contender wins outright (14/14 on bullet count, full transition coverage, the only four-test pressure pass), and on that reading `presentation-writing` would place first. But the brief's three educational goals are the job, and there `pitch-deck-mastery` scores 26/30 against 23 and 23: it lands the repeatable sentence in the fewest words and repeats it verbatim across both media, it hooks on slide 2 where the other two spend two or three slides on context, and it is the only contender that puts the redrawable diagram inside the machine-readable contract the design lane actually consumes — the other two leave goal 3 stranded in a prose file design has no reason to open. Its failures (60 bullets, no transitions, a checklist that certifies a rule it breaks) are all repairable by deletion; `staging`'s hook placement and my own three-slots-saying-one-thing are argument-shaped problems, which cost more to fix. `staging` places third on the presenter-facing rubric despite having the most rigorous gates, because a deck with no speaker notes, five bridged boundaries out of thirteen and a slot that contradicts itself is not yet a talk.

**What this rubric cannot see.** It is a slide-narrative rubric and nothing else. It has no concept of time-based media, so every judgment I made about the three explainer lanes — scene count, VO budget, motion role, peak placement — was borrowed from the transport schema rather than derived from my own principles, and should be treated as unscored. It has no provenance machinery at all: its single data discipline is transposing row-oriented spreadsheets for charts, so every fact check above sits outside it, and a contender that invented a number would have passed all fifteen rows. It cannot see rendered output — whether a 19-word bullet survives a 1280×720 stage in IBM Plex at 15pt is exactly the question that separates my contender's "3 bullets" pass from `pitch-deck-mastery`'s "≤13 words" pass, and the rubric answers it in neither direction. It is silent on brand and terminology governance, on schema conformance for the handoff, and on whether design can consume any of this. And it is structurally keynote-shaped, which biases it toward my own scaffold choice and against an investor-framework adaptation; I corrected for that by scoring the brief's goals on their own, and the correction is what moved me off first place.

---

## Addendum — `house-guide` — `messaging/house-guide/`

Fourth contender, same rubric, same measurements (bullet counts and word lengths taken from
`staging.yaml`, not eyeballed).

| Principle | Verdict | Evidence |
|---|---|---|
| Scaffold diagnosed, not menu-offered (Ph.3) | **Pass (adapted)** | The method carries no scaffold menu; the arc is diagnosed from the source decks' own nine failures (`staging.yaml` `diagnosis_carried` b1–b9, each naming the fix it produced). `NOTES.md` §3 logs five method rules that did not transfer, with the resolution for each — the most transparent adaptation in the leg alongside `pitch-deck-mastery`'s. |
| Audience diagnosed + verified (Ph.2) | **Pass w/ flag** | All four dims plus a must-explain vocabulary list and a one-new-mechanism cap. No human confirmed; `NOTES.md` §4 closes eight open questions against the corpus and names the one (54 vs 36 templates) it could not close. |
| One thesis per slide, declarative (rule 1) | **Pass** | 13/13 complete declarative sentences. d1 is a benefit statement rather than a product label, which is what the rule is for. Only contender besides `staging` to clear this outright. |
| Three bullets maximum (rule 2) | **Fail** | 4 of 13 over cap: d6, d9, d10, d11 (4 each). Second-best of the four — better than `staging` (5) and `pitch-deck-mastery` (11), behind my own 14/14. |
| Bullets are fragments, not paragraphs (Tone 7) | **Fail** | Mean ~22 words. d3's first point is a 45-word quotation, d9's second is 45 words, d11's first is 35. Fully-formed thoughts with subordinate clauses — essay writing on a slide, and two of them are block quotes. |
| No orphan slides — transitions written (rule 3) | **Fail** | 5 transitions for 12 boundaries. Seven slot changes have no bridge. Same hole as `staging`, and the lines it does write are the best-phrased in the leg ("That is the case, including the loss and the things that do not exist yet. Here is the part that needs you."). |
| Front-load the hook (rule 4) | **Pass — best of the four** | d2, the first content slot, is the stakes ("making a tokenized asset productive means posting it somewhere that can force-sell it"); d3 is the market's own account of the patch; d4 is the dated event at 31%. No context slide before tension. |
| End with an ask or charge (rule 5) | **Pass** | d12 is one ask with a first step and states what is *not* being asked; d13 is the line to repeat, not a summary and not "Questions?". |
| Cut ruthlessly (rule 6) | **Fail** | Three mechanism slots where the file's own novelty budget (b7) says one new mechanism; d8 alone carries the single price read, atomic settlement *and* privacy — three ideas on the slot that closes the run. |
| Density decision surfaced (Ph.5) | **N/A → Fail** | No density concept anywhere. Counts drift 2→4 with no stated rule; Flexible by accident, again. |
| Four pressure tests run (Ph.6) | **Pass (equivalent)** | `helicopter` is written out as the full 13-claim chain; `dead_slot` argues the turned value slot by slot; `sequencing`, `glossary`, `number_trace` and `banned_framings` go further than the four. No order test. |
| Speaker notes: conversational, why not what (Ph.7) | **Fail** | None, in either lane. Thirteen slots, 40 supporting points, two 45-word quotations, and no presenter track — the exact deficit that put `staging` last on this rubric. |
| Concrete over corporate; earned abstractions (Tone 2/4) | **Pass — best of the four** | d9's fourth point is a mandatory losing row ("THE ROW WE LOSE, and it is not cut: secondary depth"); d11 lists five things that do not exist; `messaging.md` O2 refuses to sell the split on a money-market share at all. Every abstraction carries its file, slide and as-of date. |
| AI language tells (Tone 7) | **Pass** | No banned vocabulary; sentence rhythm varies. "Turns an advocate into a discloser" and "THE ROW WE LOSE" are the performative-candour tics — the same one all four contenders have. |
| Anti-patterns (agenda / history / dump / false close / hedge / Questions) | **Pass** | None present. d1 is a claim, not an origin story; d13 closes once. |

**Brief's educational goals** — G1 one repeatable sentence: **8** (the line is published in three
registers, including a ten-word form, and it is carried *verbatim* at d13 and video s9; but the cover
claim is a different sentence, so the repeated sentence is not repeated at the highest-attention moment,
and the primary form is 30 words). G2 value prop in RWA: **9** (each pillar states its own boundary;
O2 disqualifies the MMF case outright, which is the sharpest value-scoping anyone wrote; the issuer half
of the audience is served only through objection O5, which its own NOTES admits). G3 mechanism/one
diagram: **8** (d6's fourth point *mandates* a worked instantiation — one deposit, one strike, three
prices, three payouts — which no other contender does, and d7 is the identity in two rows; but there is
no `diagram` key, so the redraw spec in `messaging.md` §4 never reaches design). **Total 25/30.**

**Top 3 findings**

1. **The best diagram sentence in the bake-off is stranded outside the transport.** `messaging.md` §4:
   "the top of the stack is a flat line all the way across, at the value of the collateral… that flat
   line is the whole product… the eye should find it before it finds anything else." That is goal 3
   stated better than any of us managed, and no design contender will open the file it is in. *Fix*: add
   a `diagram:` key to d7 carrying that paragraph verbatim, with d6's worked example named as its
   instantiation. This is the third contender in a row to lose goal 3 at the handoff.
2. **Two block quotations are being used as slide copy.** d3's first supporting point and d9's second
   each run 45 words. *Fix*: cut d3 to the clause that does the work — "formal liquidation agreements
   with asset issuers: not edge cases but fundamental design constraints" — and put the full quotation
   in a speaker note; split d9's venue row into its two halves (what triggers the sale / who holds the
   right), which also brings the slot to three points.
3. **No presenter track at all, on a deck whose own `lane` says presented-primary.** *Fix*: 2–4
   sentences per slot in the presenter's voice, and a bridging line at each of the seven bare
   boundaries. The material exists — `messaging.md` §6's five objections are speaker notes that have not
   been filed as such.

**Revised ranking**

**1. `pitch-deck-mastery` · 2. `house-guide` · 3. `presentation-writing` · 4. `staging`.**

`house-guide` enters second and pushes my own contender and `staging` each down one. On the brief's
goals it scores 25 against 26 / 23 / 23, and on the one structural test this rubric owns that it wins
outright — front-load the hook — it is the only contender whose first content slot is the stakes rather
than the market. It does not take first because it inherits both of `staging`'s disqualifiers here (no
speaker notes, five bridges out of twelve) and because, like everyone except `pitch-deck-mastery`, it
leaves the redrawable picture in a prose file design has no reason to open. `presentation-writing` and
`staging` did not move relative to each other, and the reason `staging` stays last is unchanged: it is
the most rigorous instrument in the field and still not yet a talk.
