# Medici for RWA tokens — key messaging

Distilled from `pitch.md` (pitch-deck-mastery framework, product-pitch adaptation).
Every number carries a source file plus slide or section. Nothing here is invented.
Terminology follows `source/brand/house-brand-guide.md` §8.2: **Protected Token / P**,
**Amplified Token / N**, **split**, **recombine**, **settle**, **vault**, **drift**, **theta** —
never "stable", "leverage token", "yield", or "liquidation-resistant".

---

## 1. The one-sentence definition — the repeatable line

> **Medici splits a tokenized real-world asset into two claims that always sum back to it, so the
> position can never be force-sold.**

Say it at the open and again at the close. It survives being repeated second-hand by a
non-specialist, which is the only test that matters for this audience.

**Shorter, for a subject line or a handshake**: "Collateral splitting with no liquidation price."

**Longer, when the room wants the mechanism in the sentence**: "Medici splits a tokenized position
into a Protected leg that takes the collateral value up to a strike and an Amplified leg that takes
everything above it — P + N always equals the collateral, so no price move can under-collateralize
the vault."

*Source*: `canton-pitch-deck.md` Slides 1, 3, 5; `asset-manager-pitch-deck.md` Slide 3.

---

## 2. Positioning statement

> For RWA issuers, tokenization platforms and asset managers whose tokenized positions either sit
> idle or can only be financed against a liquidation price, **Medici** is a collateral-splitting
> primitive on Canton that turns one position into two claims — Protected and Amplified — which
> always sum back to the collateral. Unlike lending markets and prime venues, which manage
> liquidation with thresholds, curators, and signed liquidation agreements with issuers, Medici has
> no liquidation threshold to manage, because no under-collateralization condition exists in the
> payoff function.

The category line: **Medici is not a better lending rate. It is a different risk category.**
Aave and Compound pay you for supplying liquidity and liquidate the borrower when a ratio breaches.
Medici pays the Protected holder for selling upside above a strike and has nothing to breach.

*Source*: `asset-manager-pitch-deck.md` Slide 8; `canton-pitch-deck.md` Slide 5;
`rwa-redstone-2026.md` Part 2, "Liquidation mechanics and risk frameworks".

---

## 3. Three value-prop pillars for RWA holders and issuers

### Pillar 1 — No forced sale of an asset you could not sell anyway

Tokenized fund shares, private credit and treasuries cannot be liquidated in a single on-chain
transaction; NAV arrives daily or less often and redemption windows run monthly to quarterly. The
market's answer has been to build the workout by hand: **"formal liquidation agreements with asset
issuers… are not edge cases but fundamental design constraints"** (`rwa-redstone-2026.md` Part 2,
"Liquidation mechanics and risk frameworks"). Medici deletes the constraint rather than managing
it — P + N ≡ collateral at every price, so there is no margin call, no forced sale, and no bad debt
(`canton-pitch-deck.md` Slide 3; `asset-manager-pitch-deck.md` Slide 4).

**The line**: nothing to breach, so nothing to seize, so no liquidation agreement to sign.

### Pillar 2 — Income on an asset you keep, exposure without a liquidation price

The split creates two positions with two intrinsic holders. A fund treasury holds **P** and earns
theta on collateral it never sells; selling the P leg is itself the liquidity, with no repayment
schedule (`asset-manager-pitch-deck.md` Slide 5; `canton-pitch-deck.md` Slide 6). An allocator holds
**N** for amplified exposure with no liquidation price and no funding rate — which is the same
demand RedStone documents as looping, at **$840M+ of tokenized RWA deposited into DeFi lending
protocols** and **87% utilization on Morpho** ($248M of $284M lender supply borrowed)
(`rwa-redstone-2026.md` Part 1 (a), Part 2 "Who lends against what"). Two-sided demand is
endogenous, not incentivized: no Medici token, no emissions
(`asset-manager-pitch-deck.md` Slide 10).

**The line**: one position, two owners, each holding for a reason that already exists.

### Pillar 3 — Institutional settlement properties, on the network the collateral is already on

Canton carries **$344B represented and $2T per month in repo** (`canton-pitch-deck.md` Slide 4).
Four properties matter to a risk or operations lead, all from that slide: positions are
**stakeholder-scoped** under sub-transaction privacy — visible to counterparties, not to the
network; **no gas, no MEV, no mempool**, so the cost of the structure is the spread rather than an
infrastructure tax; **atomic settlement** — split, roll and settle are single transactions with no
partial-fill risk; and a **lazy oracle**, queried only at settlement, so there is no live price feed
to manipulate during the position's life (`canton-pitch-deck.md` Slide 3). Authorization is stated
in four rules and enforced by the ledger protocol rather than an application filter, with a
reconciler converging identity every 60 seconds (`authorization-pitch-deck.md` Slides 2, 3, 7).

**The line**: privacy is a property of the ledger, not a promise in a policy document.

---

## 4. The mechanism, in 120 words or fewer

> A vault splits your tokenized collateral into two claims at a strike you choose.
> **Protected (P)** takes the collateral value at or below the strike. **Amplified (N)** takes
> everything above it. At maturity one reference price `x` is read. If `x` is at or below the
> strike `S`, P receives the full collateral value and N receives nothing. If `x` is above `S`, P
> receives `S/x` and N receives `1 − S/x`. Both rows sum to exactly the collateral, at every price.
> Because no price leaves the vault short, there is no liquidation threshold to breach and no
> position to seize. Above the strike P declines continuously — a slope, never a cliff — and that
> decline is what pays P.

*(118 words. Source: `canton-pitch-deck.md` Slide 5; `asset-manager-pitch-deck.md` Slides 4, 5.)*

### The one diagram

**A payoff chart with the liquidation line missing.**

Horizontal axis: the reference price `x` at maturity, running from well below the strike to well
above it. Vertical axis: value, from zero to one unit of collateral. One vertical marker on the
horizontal axis labelled `S` — the strike.

Two stacked regions. **P** occupies the full height at 1.00 for every price at or below the strike,
then falls away to the right along the curve `S/x`, approaching zero but never reaching it and never
stepping. **N** is zero at every price at or below the strike, then rises to the right along
`1 − S/x`. The top edge of the two stacked together is a **flat horizontal line at 1.00 across the
entire width** — that flat top is the invariant, and it is the whole picture.

The last element is an absence, and it should be annotated as one: mark the point on the horizontal
axis where a lending market would draw its vertical liquidation threshold, and show that no such
line exists here. A viewer who can redraw two curves, one flat top, and one missing vertical line
has understood the product.

---

## 5. Five proof points, with citations

| # | Proof point | Number / claim | Source |
|---|---|---|---|
| 1 | The invariant is closed-form, not a risk parameter | P + N ≡ collateral, closed-form verified; "no under-collateralization condition exists in the payoff function"; P = S/x above strike | `canton-pitch-deck.md` Slide 5; `asset-manager-pitch-deck.md` Slide 4 |
| 2 | The market has named this its unsolved problem | "Formal liquidation agreements with asset issuers… are not edge cases but fundamental design constraints"; curators run "formal de-leverage frameworks"; no venue in either part of the report offers a no-liquidation design | `rwa-redstone-2026.md` Part 2, "Liquidation mechanics and risk frameworks" and "Genuinely new" |
| 3 | Institutional demand exists at exactly this shape | Aave Horizon: $423.5M market size, $106M borrowed, 269 addresses, 9 tokens, Ethereum-only, 2–6% borrow rates. Morpho: RWA deposits $620M+ by March 2026, 87% utilization, 21 assets across 8 blockchains in 18 months | `rwa-redstone-2026.md` Part 2, "Who lends against what" |
| 4 | The collateral is already where Medici runs | Canton: $344B represented, $2T/month repo. Issuing there: Franklin Templeton BENJI ($800M on-chain within $2.5B digital AUM; first on-chain Treasury trade on Canton via Tradeweb, July 2026), WisdomTree ($3M RWA fees, May 2026), Invesco USTB ($2.5M RWA fees, May 2026), BlockBooster (joined Canton Foundation May 2026) | `canton-pitch-deck.md` Slides 4, 7 |
| 5 | The mechanism is built and measured, and the gaps are published | 54 DAML templates across 9 modules (~5,700 LOC); 12 TypeScript agents behind a Go Ledger Service, 6 core live; 9-year backtest (Hypercall, Aug 2017 – Jun 2026, ETH underlying, Deribit options data) with net drift −1.25%/yr, P ending at $0.895 on $1.00; closed-form invariant proofs. Not yet: mainnet, real collateral, live users, audit, revenue | `canton-pitch-deck.md` Slides 3, 8, 9; `asset-manager-pitch-deck.md` Slides 3, 12 |

**Two source discrepancies, carried openly rather than smoothed:** the contract count is 54
templates / ~5,700 LOC in `canton-pitch-deck.md` Slide 9 and 36 templates / ~5,100 LOC in
`asset-manager-pitch-deck.md` Slide 12; the US regulatory analysis is ~2,900 lines in the former
(Slide 9) and 2,600 lines in the latter (Slides 7, 11). The brief ranks `canton-pitch-deck.md`
first, so 54 and ~2,900 are used, and neither figure is load-bearing for any claim above.

---

## 6. Top five objections, with answers

### O1 — "You have not removed the risk, you have moved it."

Correct, and it is on the slide. What is removed is the **forced sale**, not the price risk. P is
economically short a call above the strike: as the reference price rises, P's value declines
continuously as `S/x`, with no floor. That decline is the source of P's theta, not a side effect.
The difference from a lending market is the shape — a slope you can compute at every price, rather
than a cliff at a threshold, with no margin call and no bad debt at any point on the curve. Note
what is *not* claimed: the payoff at any given price is computable, but the *distribution* of future
prices, and therefore the probability of loss, depends on volatility assumptions and is not
computable without a model.
*Source*: `asset-manager-pitch-deck.md` Slides 4, 7; `canton-pitch-deck.md` Slide 5.

### O2 — "The backtest is negative. Why would anyone hold P?"

Because it is an options-income product with a published cost, not a yield product. Net drift over
the 9-year backtest is **−1.25% per year**, with P ending at **$0.895 on $1.00** — and it decomposes:
roll execution at 10bps across roughly 12.2 rolls a year is **−1.2%/yr**, the dominant driver, against
gross theta of **+0.57%/yr in the best sub-period (2021–22)**. Economics improve with better
execution and higher volatility. Two caveats we state before you ask: the backtest is third-party
(Hypercall, Deribit options data, Black-Scholes at mid) and it is **ETH-only** — RWA and MMF
collateral has different volatility characteristics, so the number is evidence about the mechanism,
not a forecast for your instrument.
*Source*: `asset-manager-pitch-deck.md` Slide 3; `canton-pitch-deck.md` Slide 3.

### O3 — "Our collateral barely moves. Does the split do anything on a money-market fund?"

The Protected leg works on any collateral — it is income on an asset you keep. The **Amplified** leg
is what needs volatility: with little price movement above the strike there is little for N to take,
so N prices thin and the two-sided demand is weaker. The evidence supports leading with volatile
collateral: on Morpho, tokenized T-bill deposits **fell 92%** from their ~$194M October 2025 peak
while **tokenized gold grew 7x**, and gold is the one RWA collateral showing "straightforward
non-looped borrowing" at a conservative **~40% borrow-to-collateral ratio**. Tokenized equities are
the whitespace — infrastructure went live on Morpho in February 2026 with **total deposits below
$1K** — and the report says volatile collateral "will require new risk frameworks adapted for
onchain execution", which is what an options split is.
*Source*: `rwa-redstone-2026.md` Part 2, "Who lends against what" and "What changes in the Part 1
analysis"; `canton-pitch-deck.md` Slide 6.

### O4 — "You are not audited and not on mainnet."

True, and both are named work items rather than surprises. What exists: 54 DAML templates deployed
on Canton single-node and int clusters under FluxCD, a 12-agent fleet with 6 core agents live, a
React frontend running end to end against the dev cluster, closed-form invariant proofs, and a
~2,900-line internal US regulatory analysis that counsel has not yet reviewed. What does not: mainnet
deployment, real collateral, live users, third-party audit, revenue. The stated path, as of July
2026, is two independent DAML audits and a fund-counsel regulatory opinion in Q3 2026, mainnet in Q4
2026, compliance layer in H1 2027, first institutional pilot in H2 2027. Those dates are as-of their
source and are not a commitment we are asking you to price today.
*Source*: `canton-pitch-deck.md` Slides 9, 11, 12; `asset-manager-pitch-deck.md` Slide 12.

### O5 — "Our assets and our investors are not on Canton, and we have transfer restrictions."

Two separate answers. **Distribution**: Canton holds $344B of represented RWA and is where Franklin
Templeton, WisdomTree, Invesco and BlockBooster are issuing — but we will say the uncomfortable half
too, which is that Canton does not appear anywhere in RedStone's 2026 lending map; the venues with
live RWA lending volume are Ethereum, Solana, EVM L2s and Provenance. Getting collateral to the
vault is a deliberate problem we are solving with issuer partnerships, not one we assume away. Each
chain is also a self-contained deployment with its own oracle and agent fleet — no bridge, so no
cross-chain dependency. **Compliance**: P and N deploy at an EVM edge as ERC-3643 (T-REX)
permissioned tokens — the same standard BUIDL uses — against **Medici's own** Identity Registry and
Identity Registry Storage, which needs no third party's permission; an investor already verified
with a major tokenized fund can be fast-tracked. Sharing an existing fund's registry is a Phase 3+
stretch requiring the sponsor's consent and Securitize's participation, and we do not assume it.
*Source*: `canton-pitch-deck.md` Slides 4, 7; `rwa-redstone-2026.md` Part 1 (a)–(b), Part 2
"Survives — the Canton distribution gap"; `asset-manager-pitch-deck.md` Slides 6, 10.

---

## 7. Words to use and words to avoid

| Use | Do not use | Why |
|---|---|---|
| Protected Token, P | stable token, stablecoin | P drifts; it is not pegged |
| Amplified Token, N | leverage token, speculative token | N amplifies theta cost as well as gain |
| split / recombine / settle | mint / burn / redeem / exercise | the operations are named for what they do |
| theta, options income | yield, interest, returns | we do not promise a return |
| drift | impermanent loss, slippage | drift is the specific tracking error |
| can't be liquidated | liquidation-resistant, low liquidation risk | it is mathematically impossible; hedging it reads as doubt |
| vault | pool | vaults are single-depositor |

*Source*: `source/brand/house-brand-guide.md` §8.1–8.2.
