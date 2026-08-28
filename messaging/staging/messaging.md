# Medici for RWA tokens — key messaging

**Staged by**: `skills/messaging/staging` (v2, 2026-08-18) · genre `executive-explainer`
**Brief**: `BRIEF.md` (Ian, 2026-08-27)
**Sources**: `source/medici/*` — all figures below carry a file + slide/section citation.
**As-of**: every source deck is dated **July 2026** (canton + asset-manager decks: strawman draft
2026-07-04, asset-manager reframed 2026-07-18); the RedStone material is dated **2026-03-26**; the
standards investigation **2026-07-24**. All roadmap and status statements are as-of those dates.

---

## 1. The repeatable line

> **Medici splits a tokenized real-world asset into two claims — Protected (P) and Amplified (N) —
> that always sum back to the collateral, so the position has no liquidation price.**

Shorter, for a corridor: *"It splits the asset into two halves that always add back up, so there
is nothing to force-sell."*

Naming follows the house canon (`source/brand/house-brand-guide.md` §8.2): **Protected Token / P**,
**Amplified Token / N**, **split**, **recombine**, **settle**, **can't be liquidated** (never
"liquidation-resistant"). The brief's shorthand "stable-ish leg" is deliberately not used — §8.2
forbids "stable" for P because P drifts.

## 2. Positioning statement

> For RWA issuers, tokenization platforms, and the asset managers and risk leads holding tokenized
> positions, Medici is the collateral-splitting layer that makes a tokenized asset productive
> without a liquidation price. Its defining guarantee — P + N ≡ the collateral at every price — is
> a proven invariant of the contracts, not a policy of an operator.

Traceable to the house positioning (`house-brand-guide.md` §0.5) and its essence, *the math holds*.
Lead theme: **mathematical certainty**; support theme: **privacy by architecture** (§0.8). One
theme plus one support — no third.

## 3. Three value-prop pillars (RWA holders and issuers)

### Pillar 1 — Your collateral is never force-sold, because there is nothing to force

No margin call, no liquidation threshold, no bad debt: the payoff function contains no
under-collateralization condition (`canton-pitch-deck.md` Slide 5; `asset-manager-pitch-deck.md`
Slide 4). This matters most precisely where RWA collateral is hardest: the market's own report says
RWA lending needs "formal liquidation agreements with asset issuers" and curator-run "de-leverage
frameworks" because the collateral is NAV-priced, redeemable only in monthly or quarterly windows,
and "cannot liquidate its position in a single onchain transaction"
(`rwa-redstone-2026.md`, Part 2 addendum — "Liquidation mechanics and risk frameworks"). Medici
deletes that problem class rather than staffing it.

### Pillar 2 — Income from a position you keep, with the cost written down in advance

The holder keeps the underlying and keeps N (leveraged exposure, no liquidation price, no funding
rate); P is sold to income buyers. Sale proceeds are the liquidity — no repayment schedule, no
forced sale (`asset-manager-pitch-deck.md` Slide 5). For a tokenized fund, this is additional income
on assets that otherwise sit idle earning only their stated yield (`canton-pitch-deck.md` Slide 7).
The price of that income is stated, not implied: P is short a call above the strike, its value
declines as `P = S/x`, and the 9-year backtest puts net drift at **−1.25%/yr**
(`canton-pitch-deck.md` Slide 3). An options-income product, not a yield product.

### Pillar 3 — It settles where institutional collateral already lives, privately and atomically

Canton is the #1 RWA network — **$344B represented, $2T/month repo** — so the collateral does not
have to move (`canton-pitch-deck.md` Slide 4). Positions are stakeholder-scoped: visible to
counterparties, not to the market. Split, roll and settlement are single atomic transactions, so
there is no partial-fill risk, and there are no gas fees, no MEV and no mempool — execution cost is
the spread, not an infrastructure tax (`canton-pitch-deck.md` Slide 4). The oracle is read lazily,
at settlement only, so there is no live feed to manipulate during a position's life
(`canton-pitch-deck.md` Slide 3).

## 4. The mechanism (118 words)

A holder deposits a tokenized position into a vault and splits it at a chosen strike into two
tokens: P (Protected) and N (Amplified). Nothing is borrowed, so nothing can be called. At maturity
a single reference price `x` is read against the strike `S`. At or below strike (`S ≥ x`), P
receives the full collateral value, 1.00, and N receives 0.00. Above strike (`S < x`), P receives
`S/x` and N receives the rest, `1 − S/x`. P + N equals the collateral at every price, so no
under-collateralization condition exists: there is no threshold to breach and nothing to force-sell.
P's decline above strike is continuous and computable, and it is P's income.

*Source: `canton-pitch-deck.md` Slides 3 and 5; `asset-manager-pitch-deck.md` Slides 4 and 5.*

### The one diagram (description, not a design)

**What it must show, and nothing else**: one collateral bar, whole, on the left. It splits into two
stacked claims, P below and N above, read across a horizontal reference-price axis with the strike
marked on it. Left of the strike, P fills the entire bar and N is a zero-height sliver. Right of the
strike, P's share falls along `S/x` while N's grows as `1 − S/x`. At every point on the axis the two
stacked claims exactly fill the bar — that filled height is the invariant, and it is the only thing
the viewer has to remember. A second mark, optional: the point where a liquidation threshold would
sit on a lending chart, drawn as absent.

**The redraw test**: an audience member with a napkin should be able to reproduce it from one
sentence — *"a bar that always stays full, split by a line that moves once you cross the strike."*
Everything else (colour, type, motion, whether N sits above or below) is design's decision, not
messaging's.

## 5. Five proof points

| # | Proof | Source (file + slide/section) |
|---|---|---|
| 1 | **The invariant is closed-form, not a risk parameter.** P + N ≡ collateral, verified in closed form; "no under-collateralization condition exists in the payoff function." Payoff at maturity: `S ≥ x` → P 1.00 / N 0.00; `S < x` → P `S/x` / N `1 − S/x`. | `canton-pitch-deck.md` Slide 5 ("The Math"); `asset-manager-pitch-deck.md` Slide 4 |
| 2 | **The economics are measured, over 9 years, by a third party.** Hypercall backtest, Aug 2017–Jun 2026, ETH underlying, Deribit options data: net drift **−1.25%/yr**, P ending $0.895 on $1.00. Gross theta **+0.57%/yr** in the best sub-period (2021-22); roll cost **−1.2%/yr** at 10bps across ~12.2 rolls/yr is the dominant cost driver. | `canton-pitch-deck.md` Slide 3; `asset-manager-pitch-deck.md` Slides 3 and 12 |
| 3 | **A system exists and runs, on Canton, today.** 54 DAML templates across 9 modules (~5,700 LOC); 12 TypeScript agents behind a Go Ledger Service, 6 core agents live and 6 in progress; React frontend end-to-end; deployed on Canton single-node + int clusters (FluxCD-managed). Not mainnet. | `canton-pitch-deck.md` Slides 8 and 9 |
| 4 | **The market itself names forced liquidation as its unsolved problem.** RWA lending is real and growing — Morpho RWA deposits went from ~zero in early 2025 to **$620M+ by March 2026** at **87% utilization**; Aave Horizon is a **$423.5M** permissioned market with **$106M borrowed** across **269 addresses** — and the report's own finding is that "formal liquidation agreements with asset issuers… are not edge cases but fundamental design constraints." Nobody in either part of the report offers a no-liquidation design. | `rwa-redstone-2026.md`, Part 2 addendum ("Who lends against what", "Liquidation mechanics and risk frameworks") |
| 5 | **The collateral is already on the venue, and the venue is private and atomic.** Canton: **$344B represented, $2T/month repo**; sub-transaction privacy (positions stakeholder-scoped); no gas, no MEV, no mempool; atomic split/roll/settlement. Tokenized-fund issuers are already there: Franklin Templeton BENJI ($800M on-chain within $2.5B digital AUM; first on-chain Treasury trade executed on Canton via Tradeweb, July 2026), Invesco USTB, WisdomTree, BlockBooster. | `canton-pitch-deck.md` Slides 4 and 7 |

Supporting, if pressed on the business model: Medici clips **5–10bps** per transaction, there is
**no Medici token**, and the fee schedule is set by multi-sig governance
(`canton-pitch-deck.md` Slide 7; `asset-manager-pitch-deck.md` Slide 10).

## 6. Top five objections, in the audience's words

**1. "If nothing gets liquidated, where does the loss actually go?"**
To P, continuously, and it is computable in advance. P is economically short a call above the
strike; above strike its value declines as `P = S/x` with no floor, and that decline is the source
of P's income rather than a side effect. It is never a cliff and never a margin call. Over the
9-year backtest the net effect is −1.25%/yr. What is removed is not risk, it is *forced sale* and
*bad debt* — a different risk category, not a better lending rate.
*(`asset-manager-pitch-deck.md` Slides 4, 7 and 8; `canton-pitch-deck.md` Slides 3 and 5.)*

**2. "Your backtest is ETH. My collateral is a money-market fund."**
Correct, and the sources say so first: the backtest is third-party and ETH-only, and "the flagship
RWA/MMF use case has different vol characteristics." The mechanism needs volatility for N to be
worth anything, which is exactly why tokenized treasuries are the *wrong* first underlying — on
Morpho, T-bill collateral fell 92% from its ~$194M peak while tokenized gold grew 7x and shows a
conservative ~40% borrow-to-collateral ratio ("straightforward non-looped borrowing"). Tokenized
gold is the realistic first RWA underlying; the parameterization changes, the invariant does not.
*(`canton-pitch-deck.md` Slide 3; `rwa-redstone-2026.md`, Part 2 addendum + updated takeaway 2;
`asset-manager-pitch-deck.md` Slide 10.)*

**3. "Is any of this live?"**
No. It is a working MVP dev-deployed on Canton single-node and int clusters: 54 DAML templates,
12 agents (6 core live), closed-form invariant proofs, a React frontend end-to-end. What does not
exist: mainnet deployment, real collateral, live users, a third-party audit, revenue. Two
independent DAML audits ($150–400k each, 6–10 weeks per firm, niche auditor pool) and a fund-counsel
regulatory opinion are named Phase 1 deliverables; as of July 2026 the plan targets audit and legal
in Q3 2026 and mainnet in Q4 2026. The ~2,900-line US regulatory analysis has not been reviewed by
counsel.
*(`canton-pitch-deck.md` Slides 9, 11, 12; `asset-manager-pitch-deck.md` Slides 12 and 13.)*

**4. "Our assets — and our borrowers — are not on Canton."**
Two honest halves. Where RWA lending actually happens today is Ethereum, Solana, EVM L2s and
Provenance; Canton "is not mentioned anywhere in the report," and distribution is an open problem
Medici names rather than assumes away. But Canton is where the *collateral* is ($344B represented,
$2T/month repo), the issuers are already there (Franklin Templeton, Invesco, WisdomTree,
BlockBooster), and Medici deploys as a self-contained vault per chain with no cross-chain bridge,
so an EVM edge is a deployment decision, not a redesign. The standards work already maps P/N onto
the vocabulary EVM allocators integrate against (ERC-4626/7540 semantics; the P side is the
4626-conformant face).
*(`rwa-redstone-2026.md`, Part 2 "Survives — the Canton distribution gap"; `canton-pitch-deck.md`
Slides 4 and 7; `asset-manager-pitch-deck.md` Slide 10; `rwa-standards-canton.md` §4.4.)*

**5. "One oracle read at settlement sounds like a single point of failure."**
It is a deliberate trade, stated as one in the source: reading lazily removes the live feed an
attacker would manipulate mid-position (the Mango Markets shape, $116M), and it concentrates price
risk into a single read at settlement. The mitigation is multiple independent feeds with a consensus
threshold, published by the OracleAgent, with a RiskAgent monitoring oracle divergence and a circuit
breaker that can be triggered manually.
*(`canton-pitch-deck.md` Slide 3 (oracle model), Slide 2 (Mango Markets), Slide 8 (agents).)*

**Held in reserve** (asked less often by this audience, answered the same way): "who buys P?"
— endogenous two-sided demand, income buyers on P and speculators or treasuries on N
(`canton-pitch-deck.md` Slide 6); "what if N has no bid?" — N liquidity risk is disclosed as present
and mitigated by the market-maker agent (`asset-manager-pitch-deck.md` Slide 7).

## 7. What this messaging deliberately does not say

- **No funding ask.** Both source decks end on capital (Foundation funding; $5–50M strategic
  investment). The brief's ask is a conversation, so the capital ask is cut, not softened — a
  capital ask would have re-classified the genre to `investor-pitch`.
- **No "safe" or "protected principal".** P is capped, not floored; principal risk above strike is
  present by design (`asset-manager-pitch-deck.md` Slide 7).
- **No claim of an audit, a live user, or revenue.** None exists as of the July 2026 sources.
- **No invented numbers.** Every figure above appears in a cited source file.
