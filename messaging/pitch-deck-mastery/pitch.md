# Medici for RWA tokens — deck + explainer treatment

**Skill**: `pitch-deck-mastery` (12-slide framework, stage adjustments, deck-review checklist)
**Genre**: product pitch / explainer to prospects. Educate first; the ask is a conversation.
**Audience**: RWA issuers, tokenization platforms, asset managers and their risk/product leads,
plus chain-ecosystem BD. Technical-adjacent, finance-literate, not DeFi-native.
**Deck**: 13 slides, ~10 minutes spoken (600 s ÷ 13 = 46 s per slide).
**Explainer**: 8 scenes, 143 s.
**Sources**: everything on a slide traces to `source/medici/*.md`. Roadmap and market figures are
as-of their source's date (July 2026 for the decks, March–July 2026 for the landscape files) and
are labelled as such on the slide.

---

## 1. Stage call and framework mapping

`pitch-deck-mastery` routes on **stage** (pre-seed → Series B+). This is not a raise, so the stage
axis does not apply directly. Two things were settled before staging:

**Stage analogue.** The company is pre-revenue, pre-audit, pre-mainnet, with a working MVP and a
9-year backtest (`canton-pitch-deck.md` Slide 9; `asset-manager-pitch-deck.md` Slide 12). Under the
skill's stage table that is **seed** — *"10-12 slides, emphasise Product and Traction, minimise
detailed financials."* Adapted for a product pitch: emphasise Mechanism and Evidence, cut financial
projections entirely, and add a Risk slide, because the buyer here is a risk committee rather than
an investment committee. Result: 13 slides, one over the seed band and two under the skill's
"no more than 15 for seed" ceiling.

**Framework mapping.** Every one of the skill's 12 slides is either kept, re-purposed or replaced.
Nothing is dropped silently.

| # | Skill's slide | Investor question | Kept / re-purposed | Product-pitch slot |
|---|---|---|---|---|
| 1 | Title | "What is this company?" | Kept | S1 Cover |
| 2 | Problem | "Why does this matter?" | Kept, re-aimed at the prospect's own book | S2 Problem |
| 3 | Solution | "How do you solve it?" | Kept | S3 Solution |
| 6 | Product | "What does it look like?" | Re-purposed — no screenshots; the *mechanism* is the product | S4 Mechanism, S5 Invariant |
| — | — | — | **Added** — the skill has no "who is on each side" slide; a two-sided instrument needs one | S6 Two sides |
| 4 | Why Now | "Why is now the right time?" | Kept | S7 Why now |
| 5 | Market Size (TAM/SAM/SOM) | "How big is the opportunity?" | **Replaced** — a prospect does not buy on your TAM. Same slot, new job: where the collateral and the borrow demand already sit | S8 Where this runs |
| 9 | Competition | "Why will you win?" | Kept, reframed as category placement, not a win claim | S9 Category |
| 7 | Traction | "Is it working?" | Re-purposed — no revenue to show; traction is build state plus what does **not** exist | S10 Evidence |
| 11 | Financials | "Projections, use of funds?" | **Replaced** — projections are meaningless to a buyer and unsourced here. Same slot, new job: the risk register | S11 Risk |
| 8 | Business Model | "How do you make money?" | Kept, read from the buyer's side: what it costs them | S12 Cost |
| 10 | Team | "Can you execute?" | Kept, re-aimed as counterparty diligence | S13 (folded into close) |
| 12 | Ask | "What are you asking for?" | Re-purposed — the ask is a scoped conversation, not a cheque | S13 Ask |

Team is folded into S13 rather than given its own slide: for a prospect at first contact, three
founder credentials and the entity structure are diligence inputs to the *next* conversation, not a
persuasion beat. Full team detail is carried as the appendix slide A1.

**The skill's own rules applied throughout**: one idea per slide; the headline is the takeaway, not
a label; no bullet over 10 words; adjectives replaced with sourced numbers; charts over tables where
a trend is the point.

---

## 2. The deck, slide by slide

### S1 — Cover · function: cover

**Headline**: Medici splits tokenized collateral into two claims that never liquidate

- Medici — collateral splitting for tokenized real-world assets
- One position becomes P and N. P + N ≡ collateral.
- AAA Flowers S.A. (Panama), operating as Medici

**Speaker note**: give the repeatable sentence twice — once now, once at the close. "Medici splits a
tokenized real-world asset into two claims that always sum back to it, so the position can never be
force-sold." That is the sentence they should be able to repeat to their risk lead tomorrow.

**Sources**: `canton-pitch-deck.md` Slides 1, 3.

---

### S2 — Problem · function: problem

**Headline**: RWA lending's hardest problem is the liquidation nobody can execute

- Every venue prices your collateral against a liquidation threshold
- Tokenized funds cannot be sold in one transaction
- So the market hand-builds the workout: signed liquidation agreements with issuers, formal
  de-leverage frameworks, curators with direct lines to the issuer
- RedStone, March 2026: these are *"not edge cases but fundamental design constraints"*
- When the threshold does break: Black Thursday, $8M of collateral liquidated for $0

**Speaker note**: this is the slide the room already agrees with, so do not argue it — quote it.
The market has told itself in print that forced liquidation does not work for RWA collateral and
has responded by rebuilding a TradFi workout desk on top of a money market. Land the cost of the
status quo in their terms: legal agreements per issuer, a human curator in the loop, NAV pricing
against a redemption window that is monthly or quarterly.

**Sources**: `rwa-redstone-2026.md` Part 2, "Liquidation mechanics and risk frameworks";
`canton-pitch-deck.md` Slide 2; `asset-manager-pitch-deck.md` Slide 2.

---

### S3 — Solution · function: solution

**Headline**: One position becomes two claims that always sum back to it

- **P — the Protected leg.** Full collateral value at or below strike. No margin call, no forced sale.
- **N — the Amplified leg.** Everything above strike.
- P + N ≡ collateral, at every price, by construction
- Split, hold, then recombine or settle at maturity — atomically

**Speaker note**: lead with the outcome, not the feature. The outcome is that nobody has to sell
anything at a bad moment, because there is no moment at which the vault is short of collateral. Say
"Protected" and "Amplified", not "stable" and "leverage" — P drifts and N amplifies costs as well as
gains. Three differentiators, no more, per the skill's solution rule.

**Sources**: `canton-pitch-deck.md` Slides 3, 5; `asset-manager-pitch-deck.md` Slide 3;
`source/brand/house-brand-guide.md` §8.2 terminology canon.

---

### S4 — Mechanism · function: mechanism · **the diagram slide**

**Headline**: At maturity, P takes S/x and N takes the rest

| At maturity, reference price `x`, strike `S` | P receives | N receives |
|---|---|---|
| x ≤ S — price at or below strike | 1.00 (full collateral value) | 0.00 |
| x > S — price above strike | S/x | 1 − S/x |

- Every row sums to exactly the collateral
- Above strike, P declines continuously — a slope, never a cliff
- The oracle is read once, at settlement, not continuously

**Speaker note**: this is the slide they must be able to redraw. Draw the payoff by hand if the room
allows it. Two lines and one strike marker: P flat at 1.00 up to the strike then falling away as
S/x; N flat at zero then rising as 1 − S/x; the two stacked always making one flat band at the
collateral. Then point at the place a lending protocol would put a vertical liquidation line and say
that no such line exists on this chart.

**Sources**: `canton-pitch-deck.md` Slide 5; `asset-manager-pitch-deck.md` Slide 4.

---

### S5 — The invariant · function: proof · **BOLD MOMENT**

**Headline**: No liquidation threshold exists because no under-collateralization condition exists

- "No forced liquidation" is a theorem, not a risk parameter
- Closed-form invariant, verified as pure math — not a runtime assert
- There is no price `x` at which the vault is short of collateral
- Nothing to breach, so nothing to seize, so no liquidation agreement to sign

**Speaker note**: the whole deck is paid for here. Say the sentence, then stop talking. The
mechanism slide showed the payoff; this slide states what is *absent* from it, which is the harder
and better point. Do not soften it — "liquidation-resistant" and "low liquidation risk" are the
wrong words. If someone objects that risk cannot be destroyed, they are right and S11 is the answer:
the price risk stays and is fully computable, the *forced sale* is what is gone.

**Sources**: `canton-pitch-deck.md` Slide 5; `asset-manager-pitch-deck.md` Slide 4;
`source/brand/house-brand-guide.md` §8.2.

---

### S6 — Two sides · function: application

**Headline**: Two legs, two holders, each with an intrinsic reason

| Holder | Takes | Why they want it |
|---|---|---|
| Fund treasury / issuer | P | Income on an asset they keep — never sold, never called |
| Allocator / speculator | N | Amplified exposure with no liquidation price, no funding rate |

- The pattern: volatile collateral plus two intrinsic holders = endogenous two-sided demand
- Sell P and the proceeds are liquidity — with no repayment schedule and no forced sale
- The split needs volatility to price N; treasuries have least of it, gold and equity-linked most

**Speaker note**: this is where an RWA issuer sees themselves. It is also where the honest caveat
belongs: an options split needs a reference price and volatility. Tokenized T-bill collateral on
Morpho fell 92% while tokenized gold grew 7x, and gold is the one RWA collateral being borrowed
against in "straightforward non-looped borrowing" at roughly 40% loan-to-collateral. If the prospect
holds an MMF share, the P leg is still an income leg on an asset they keep; the N leg prices thin.
Say that before their quant does.

**Sources**: `canton-pitch-deck.md` Slide 6; `asset-manager-pitch-deck.md` Slide 5;
`rwa-redstone-2026.md` Part 2, "Who lends against what" and "What changes in the Part 1 analysis".

---

### S7 — Why now · function: timing

**Headline**: The asset side arrived; the lending side still liquidates

- Tokenized treasuries $12.9B, up roughly 300% year on year (rwa.xyz, July 2026)
- $840M+ of tokenized RWA already deposited into DeFi lending protocols
- Every one of those venues prices against a liquidation threshold
- Nobody in RedStone's 2026 report offers a no-liquidation design
- The category does not exist yet — it is being asked for in the report's own words

**Speaker note**: the skill lists five legitimate "why now" triggers; this is *market failure* —
incumbent mechanism stagnation — and it is documented rather than asserted. Keep the dates visible.
Everything on this slide is as-of March–July 2026.

**Sources**: `asset-manager-pitch-deck.md` Slide 14; `rwa-redstone-2026.md` Part 1 (a) and Part 2.

---

### S8 — Where this runs · function: context *(replaces Market Size)*

**Headline**: Canton already holds the collateral, the privacy, and the settlement

- $344B represented on Canton, $2T per month in repo — the collateral is already here
- Sub-transaction privacy: a position is visible to its counterparties, not to the network
- No gas, no MEV, no mempool — cost is the spread, not an infrastructure tax
- Atomic settlement: split, roll and settle are single transactions, no partial fill
- Franklin Templeton, WisdomTree, Invesco and BlockBooster are already issuing here (May–July 2026)

**Speaker note**: the skill wants TAM/SAM/SOM here and warns that top-down sizing is weak. There is
no sourced TAM for this product in the corpus, and inventing one would break the brief, so the slot
does the job a prospect actually needs: where the assets are and what the venue gives them. Be
straight about the counterweight if asked — Canton does not appear anywhere in RedStone's 2026
lending map. Distribution is an open problem, not a solved one.

**Sources**: `canton-pitch-deck.md` Slides 4, 7; `rwa-redstone-2026.md` Part 1 (b) item 2, Part 2
"Survives — the Canton distribution gap".

---

### S9 — Category · function: comparison

**Headline**: Not a better lending rate — a different risk category

|  | Lending market (Aave, Compound, Morpho) | Medici P |
|---|---|---|
| Who carries price risk | Borrower, until the threshold breaches | P holder, continuously and computably |
| What you are paid for | Supplying liquidity | Selling upside above the strike |
| Worst case | Cascade, bad debt, socialised loss | The asset rallies; P declines toward zero |
| Liquidation pathway | Curators, LTVs, signed issuer agreements | None — there is nothing to liquidate |

- Two axes that matter to this room: is there a liquidation pathway, and is the venue permissioned
- Aave Horizon is the honest benchmark: permissioned, institutional, $423.5M market, $106M borrowed,
  269 addresses — and it still liquidates

**Speaker note**: the skill's competition rule is a 2x2, not a feature checklist you win everywhere.
Axes: *liquidation pathway (yes/no)* against *permissioned (yes/no)*. Aave/Compound/Morpho sit in
permissionless-with-liquidation; Aave Horizon sits in permissioned-with-liquidation and proves the
institutional demand shape; Medici sits in permissioned-without-liquidation, which is empty. Say the
quadrant is empty; do not say there is no competition — the alternative to Medici is Horizon plus a
lawyer, and that alternative works today.

**Sources**: `asset-manager-pitch-deck.md` Slide 8; `rwa-redstone-2026.md` Part 2, Aave Horizon and
Morpho sections.

---

### S10 — Evidence · function: evidence *(re-purposed Traction)*

**Headline**: The mechanism is built and backtested; the mainnet is not

| Built | Detail |
|---|---|
| DAML contracts | 54 templates across 9 modules, ~5,700 LOC |
| Agents | 12 TypeScript agents behind a Go Ledger Service; 6 core live |
| Backtest | 9 years, Aug 2017 – Jun 2026 (Hypercall); ETH underlying, Deribit data |
| Verification | Closed-form invariant proofs, pure tests |
| Deployed | Canton single-node and int clusters, FluxCD-managed |

- Not yet: mainnet, real collateral, live users, third-party audit, revenue
- Backtest is third-party and ETH-only; RWA collateral has different volatility

**Speaker note**: the skill's traction slide wants a chart going up and to the right. There isn't
one, and pretending otherwise would fail its own "no vanity metrics without context" rule. This room
rewards the disclosure more than the chart would have earned: state what exists, then state the five
things that do not, unprompted. It is also the credibility that makes S11 believable.

**Sources**: `canton-pitch-deck.md` Slides 8, 9; `asset-manager-pitch-deck.md` Slide 12.

---

### S11 — Risk · function: risk *(replaces Financials)*

**Headline**: Every risk we removed, and every risk we did not

| Risk | Status |
|---|---|
| Forced liquidation | Removed — structural, no under-collateralization condition |
| Counterparty risk to Medici | None — the vault is collateralized by the deposit itself |
| Principal risk above strike | Present by design — P is short a call, P = S/x, no floor |
| Net drift | −1.25% per year over the 9-year backtest; P ends at $0.895 on $1.00 |
| Smart-contract risk | Present — not yet audited; two independent DAML audits are Phase 1 |
| Liquidity for N | Present — market-maker agent plus endogenous demand |
| Regulatory | Open — internal analysis drafted, fund-counsel review not yet done |
| Upstream custody | Unchanged — the collateral's own custody chain sits above the vault |

**Speaker note**: the drift number is the one that decides the meeting, so put it on the slide
rather than in the appendix. The −1.25% is dominated by roll execution: −1.2% per year at 10bps
across roughly 12.2 rolls, against gross theta of +0.57% in the best sub-period. It is the published
cost of the structure, on ETH, with third-party data — and it improves with better execution and
higher volatility. A structure that publishes its own drag is a structure whose risk you can model.

**Sources**: `asset-manager-pitch-deck.md` Slides 3, 7; `canton-pitch-deck.md` Slide 3.

---

### S12 — Cost · function: commercial

**Headline**: Five to ten basis points on flow. No token.

- Commission on each split, roll and settlement, in the settlement currency
- Fee schedule set by multi-sig governance, adjustable within circuit-breaker bounds
- No Medici token, no inflationary incentives
- No bridge: each chain is a self-contained deployment, so no cross-chain dependency

**Speaker note**: the skill's business-model slide is written for the investor. Flip it: the buyer
wants to know the all-in cost of holding the structure. It is the commission plus the roll spread —
and the roll spread is already priced into the −1.25% on the previous slide, which is why the two
slides sit next to each other.

**Sources**: `canton-pitch-deck.md` Slide 7; `asset-manager-pitch-deck.md` Slide 10.

---

### S13 — Ask · function: close

**Headline**: Bring one position; we will model the split with you

- Pick one tokenized position and a strike; we return the payoff at every price
- What we need from you: the instrument, the maturity you would want, your compliance constraints
- What we are not asking for: capital, custody, or a commitment
- Built by Ian (technical lead, 30+ years platforms), Co-founder (RWA tokenization and
  institutional infrastructure), Co-founder (growth)
- AAA Flowers S.A. (Panama), operating as Medici — institutional deployment moves to a purpose-built
  SPV

**Speaker note**: the skill says the ask should feel inevitable rather than requested. Here it is
cheap by construction — the deliverable of the next meeting is a payoff table for an instrument they
already hold, which costs them nothing and is the fastest way to convert the invariant from a claim
into something they have checked themselves. Repeat the one-liner from S1 and stop.

**Sources**: `canton-pitch-deck.md` Slides 10, 11; `asset-manager-pitch-deck.md` Slide 11.

---

### A1 — Appendix (not in the 10-minute walk)

Roadmap as-of July 2026 (`canton-pitch-deck.md` Slide 12): audits and legal Q3 2026; mainnet
deployment Q4 2026; compliance layer H1 2027; first institutional pilot H2 2027. Compliance path:
ERC-3643 (T-REX) at the EVM edge with Medici's own Identity Registry, the same standard BUIDL uses
(`asset-manager-pitch-deck.md` Slide 6). Identity control plane: declarative manifest, 60-second
convergence, full recovery from a wiped environment in ~4–6 minutes with zero manual steps
(`authorization-pitch-deck.md` Slides 7, 8). Deferred items are listed in both source decks'
appendices and are not restated here.

---

## 3. The skill's deck-review checklist, filled in

### Must-pass — instant rejection if missing

| Check | Verdict | Where |
|---|---|---|
| Clear one-liner on title slide | **Pass** | S1 — "splits tokenized collateral into two claims that never liquidate"; passes the mom test, no DeFi jargon |
| Specific, quantified problem | **Pass** | S2 — $8M liquidated for $0; RedStone's "fundamental design constraints" quote; the workout apparatus named |
| Solution clearly tied to the problem | **Pass** | S3 answers S2 clause for clause: no threshold → no seizure → no issuer liquidation agreement |
| Market size with credible sourcing | **Adapted — pass** | S8 replaces TAM with sourced position of collateral and demand ($344B Canton; $840M+ RWA lending deposits; $423.5M Horizon). No TAM is invented. Logged as a fundraise assumption in NOTES.md |
| Team slide with relevant credentials | **Adapted — pass** | Folded into S13 with appendix depth: 30+ years platforms, Canton/DAML pedigree, named blockchain patents |
| Clear ask (amount + use of funds) | **Adapted — pass** | S13. There is no amount because there is no raise; the ask is one position and one strike, with what we need and what we do not stated explicitly |

### Strength signals

| Signal | Verdict |
|---|---|
| Traction chart, up and to the right | **Absent, deliberately** — no revenue, no users, no mainnet. S10 shows build state and states the five gaps instead. Faking a curve would fail the common-mistakes check below |
| Named customers or logos | **Partial** — Franklin Templeton, WisdomTree, Invesco, BlockBooster are named as Canton issuers on S8, explicitly as ecosystem context, never as customers or pilots |
| Unit economics demonstrated | **Pass** — 5–10bps on flow (S12) against the −1.25%/yr drift decomposed into −1.2% roll cost and +0.57% best-period gross theta (S11) |
| Competitive positioning, honest not dismissive | **Pass** — S9 names Aave Horizon as a working alternative with real volume and says the empty quadrant is empty, not that competition does not exist |
| "Why now" with a genuine insight | **Pass** — S7's insight is that the market published its own unsolved problem and nobody has answered it mechanically |
| Consistent visual identity | **Deferred to design** — this artifact is staging only; the composition contract forbids naming palette, type or layout here |

### Common mistakes — checked against

| Mistake | Status |
|---|---|
| Wall-of-text slides | Clear — no slide exceeds five bullets; no bullet exceeds 10 words |
| Unsourced market-size claims | Clear — every figure carries a file and slide/section citation; no TAM is asserted |
| "We have no competition" | Clear — S9 names the alternative and credits its volume |
| Vanity metrics without context | Clear — the backtest is labelled third-party, ETH-only, 9-year, with the drift *negative* and on the slide |
| More than 15 slides at seed | Clear — 13 plus one appendix |
| Generic team bios | Clear — domain-specific credentials only (Canton/DAML, blockchain patents, platform engineering) |

---

## 4. Explainer video — scene treatment

**Length**: 143 s (brief window: 90–150 s). **Scenes**: 8. **Narration**: 332 words at ~2.35
words/second, plus a deliberate 2-second hold inside scene 5. Motion roles are drawn from the closed eight-role vocabulary; energy is an amplitude
allowance, not a look; nothing here names a colour, a font, a layout or a transition effect.

**The one animated argument**: the same liquidation gesture is performed twice. In scene 2 it
completes and destroys a position. In scene 5 it is begun and refused, because the thing it needs
to grab does not exist. Scene 5 answers scene 2; that rhyme is the film.

---

**Scene 1 — 13 s · hold · energy 1.0**
**Claim**: Your tokenized collateral has a price at which someone else sells it.
**VO**: "You hold a tokenized position — a fund share, a treasury, a bond. The moment you finance
it, somewhere in the paperwork there is a price at which somebody else sells it."
**On screen**: one position, at rest. A single marked price sits below it and does not move. Nothing
else animates.
**Figures**: 1 — the position (renders "you hold a tokenized position"); the marked price is part of
the same figure.

**Scene 2 — 22 s · rupture · energy 3.5 · PEAK**
**Claim**: When the threshold breaks, the position is sold at the worst price.
**VO**: "That is a liquidation threshold. Price crosses it, and the collateral is sold into the
fall. On Black Thursday, eight million dollars of collateral cleared for zero. Tokenized assets are
worse — most cannot be sold in one transaction, so the market signs liquidation agreements with
issuers to do it by hand."
**On screen**: the price crosses the line and the position is taken. This is the loudest thing that
happens in the film and the only place a break is shown.
**Figures**: 2 — the crossing (renders "price crosses it"), the seizure (renders "sold into the
fall").

**Scene 3 — 20 s · assemble · energy 3.0**
**Claim**: Medici splits one position into two claims: Protected and Amplified.
**VO**: "Medici does something else with the same collateral. It splits the position into two
claims. Protected takes the value at or below a strike you choose. Amplified takes everything above
it. Both are issued atomically, and both stay claims on collateral that never leaves the vault."
**On screen**: the position separates into two parts that stay tethered to the whole. Everything
that arrives stays.
**Figures**: 2 — the split (renders "splits the position into two claims"), the tether to the
collateral (renders "claims on the same collateral").

**Scene 4 — 21 s · accumulate · energy 3.0**
**Claim**: At maturity, P takes S/x, N takes the rest, and the two still sum to the collateral.
**VO**: "At maturity, one reference price is read. At or below the strike, Protected takes the full
collateral value and Amplified takes nothing. Above it, Protected takes S over x and Amplified takes
the rest. Sweep the price across the whole range: the two always add back to exactly the collateral."
**On screen**: the reference price sweeps continuously across its range; the two shares move against
each other while their sum stays a flat, unchanging band. The growth of one against the other *is*
the scene.
**Figures**: 2 — the sweeping payoff (renders "sweep the price across the whole range"), the
constant sum (renders "always add back to exactly the collateral").

**Scene 5 — 21 s (19 s narrated + a 2 s hold) · arrest · energy 4.0 · PEAK · BOLD MOMENT**
**Claim**: The price rises, and the liquidation that would fire does not exist.
**VO**: "Now run that first scene again. Price moves hard against the Protected side. A lending
market would seize the collateral here. Watch. [2 s hold] Nothing fires. There is no liquidation
threshold, because the payoff has no under-collateralized state to trigger one. A theorem, not a
risk setting."
**On screen**: the scene-2 gesture starts identically and stops mid-motion. The threshold line is
reached for, and it is not there. Then two seconds of stillness before the VO resumes. The refusal
is the point; it is deliberately quieter than scene 2 was loud, and it holds the film's energy
ceiling because nothing else is allowed above it.
**Figures**: 3 (bold-moment allowance) — the reaching gesture (renders "a lending market would seize
the collateral here"), the absent line (renders "there is no liquidation threshold"), the payoff
continuing unbroken (renders "no under-collateralized state").

**Scene 6 — 17 s · hold · energy 1.0**
**Claim**: Two holders, two reasons: income kept, exposure amplified.
**VO**: "Each leg has an owner who wants it. A fund treasury holds Protected and earns on an asset
it never sells. An allocator holds Amplified for exposure with no liquidation price and no funding
rate. Selling a leg is the liquidity."
**On screen**: two holders, given rather than developed. Static.
**Figures**: 1 — the two holders (renders "each side has an owner who wants it for its own reason").

**Scene 7 — 14 s · divest · energy 2.0**
**Claim**: What is built is real; what is not built is named.
**VO**: "What exists today: fifty-four DAML contracts on Canton, a twelve-agent fleet, a nine-year
backtest, closed-form proofs. What does not: mainnet, an audit, live collateral, a customer. You
should hear that from us."
**On screen**: the film removes its own claims one at a time until only what is built remains.
Subtractive only — nothing new enters.
**Figures**: 1 — the shrinking claim set (renders "what does not: mainnet, an audit, live collateral").

**Scene 8 — 15 s · cadence · energy 1.0**
**Claim**: Bring one position, and the split is modelled against it.
**VO**: "Medici splits a tokenized asset into two claims that always sum back to it, so the position
can never be force-sold. Bring one position and a strike; we will show you the payoff at every
price."
**On screen**: the single position from scene 1 returns, now split and summing. Resolves the opening
image and stops.
**Figures**: 1 — the returned position (renders "always sum back to it").

---

### Motion budget

```
peaks_earned: 2
  s2 (rupture)  — R1: turns the audience from "liquidation is a parameter" to
                  "liquidation is a seizure I cannot execute on this asset"
  s5 (arrest)   — R1: turns the central belief; this is the value the viewer
                  must still carry tomorrow. Staged bold moment.
ceiling_order: "s5 (4.0) > s2 (3.5) > s3 (3.0) = s4 (3.0) > s7 (2.0) > s1 (1.0) = s6 (1.0) = s8 (1.0)"
quiet_scenes:  [s1 (1.0, pays for s2), s6 (1.0, pays for s5), s8 (1.0)]
mean_energy:   2.31          # R5 ceiling 3.0
quiet_share:   3 of 8 = 0.375  # R5 floor 0.333
adjacency:     pass — s2 and s5 are not adjacent; each has a neighbour at 1.0
rhymes:        [{scene: 5, answers: 2}]   # R4: the refusal answers the seizure
figures_total: 13
ornament_gate: pass — max 2 per scene, 3 on the bold moment. Cut at STAGE: a
               third figure in s3 restating the atomicity claim the VO already
               makes; a "Canton network" figure in s6 that rendered no clause of
               its claim.
event_walk:    s1 CONDITION · s2 EVENT · s3 EVENT · s4 EVENT · s5 EVENT ·
               s6 CONDITION · s7 CONDITION · s8 CONDITION
               → event budget 4, peaks taken 2. rupture and arrest are legal
               only on s2–s5; both taken there.
```

### Bold-moment placement

Deck: S5 of 13 = 38% through the slot sequence — inside the mechanism beat, immediately after the
payoff is drawn and before any application or evidence. Video: scene 5 opens at 76 s of 143 s = 53%
of runtime, closing at 68%. Both sit at the hinge between "here is how it works" and "here is what
follows", which is the only place the absence of a liquidation threshold can land — it is
unintelligible before the payoff is drawn and anticlimactic after the evidence.

One bold moment, in both media, and it is a thing that happens rather than a strong sentence: the
liquidation gesture is begun and refused on screen.
