# Medici for RWA tokens — key messaging

**Distilled from** `outline.md` (narrative architecture, `powerpoint-keynote-presentation` skill).
Every figure carries its source file and slide/section. No number appears here that is not in
`source/medici/` or `source/brand/`. Market and roadmap figures are as-of their source dates: the
Medici decks are July 2026, the RedStone research is March 2026.

---

## 1. The repeatable line

> **Medici splits a tokenized asset into two claims that always sum back to the collateral — P, the
> capped income leg, and N, the amplified leg — so there is no liquidation price, because the math
> doesn't permit it.**

The second clause is the house canonical sentence and is reused verbatim, never paraphrased
[`house-brand-guide.md` §8.3, §0.8 "No liquidation, said plainly"].

**Short forms:**

- Ten words: "Two claims that always add back to the collateral."
- Spoken: "There is no liquidation price — the math doesn't permit it."

---

## 2. Positioning statement

> For RWA issuers, tokenization platforms and asset managers holding tokenized funds, treasuries and
> commodities on Canton, **Medici is the collateral-splitting layer that makes those holdings
> productive without a liquidation price.** Unlike the RWA money markets — Morpho, Aave Horizon —
> which manage the liquidation pathway with curators, LTVs and signed liquidation agreements with the
> issuer, Medici removes the pathway from the payoff function: `P + N ≡ collateral` is a closed-form
> invariant, so there is no under-collateralization condition to trigger one.

Consistent with the house positioning: Medici is infrastructure, not an app or a venue; the guarantee
is "a proven invariant of the contracts, not a policy of an operator" [`house-brand-guide.md` §0.5].

---

## 3. Three value pillars — for RWA holders and issuers

### Pillar 1 — The asset you cannot sell is never force-sold

The RWA market's hardest unsolved problem is the liquidation pathway for collateral that cannot be
liquidated in one transaction; it is currently solved with signed liquidation agreements with asset
issuers and curator-run de-leverage frameworks, which the report calls "not edge cases but
fundamental design constraints" [`rwa-redstone-2026.md`, Part 2, "Liquidation mechanics and risk
frameworks"]. Medici deletes the constraint rather than administering it: no margin call, no forced
sale, no bad debt, and nothing for the issuer to sign [`canton-pitch-deck.md` Slide 3;
`asset-manager-pitch-deck.md` Slide 7].

*Says it in one line:* your unsellable collateral never has to be sold.

### Pillar 2 — Income from a position you keep, with the cost named

The holder keeps the leg they want and sells the other; the sale proceeds are the liquidity, with no
repayment schedule and no forced sale [`asset-manager-pitch-deck.md` Slide 5]. For a fund treasury
this is additional income on assets that otherwise sit earning only their stated yield
[`canton-pitch-deck.md` Slide 6, "RWA yield enhancement"]. The cost is published, not implied: net
drift **−1.25%/yr**, P ending at **$0.895** on **$1.00** over a **9-year** backtest
[`asset-manager-pitch-deck.md` Slide 3]. This is an options-income product, not a yield product
[`canton-pitch-deck.md` Slide 3].

*Says it in one line:* covered-call-shaped income on collateral you never hand over.

### Pillar 3 — Institutional plumbing, because the collateral is already on it

Positions are stakeholder-scoped — visible to counterparties, not to the market. Splits, rolls and
settlements are atomic single transactions. No gas, no MEV, no mempool, so execution cost is the
spread and nothing else [`canton-pitch-deck.md` Slide 4]. Canton carries **$344B represented and
$2T/month in repo**, so the collateral needs no bridge and no wrapper [same]. Confidentiality is a
property of the ledger, not a promise in a policy document [`house-brand-guide.md` §0.7].

*Says it in one line:* the privacy and settlement institutions ask for are properties of the ledger,
not features of our app.

---

## 4. The mechanism, in 113 words

A holder deposits a tokenized asset into a vault and picks a strike. The vault splits the deposit
into two tokens. P is the capped, income-bearing leg: at or below the strike it is worth the whole
collateral; above it, P = S/x, declining continuously as the asset rallies. N is the amplified leg:
nothing at or below the strike, 1 − S/x above it. At every price P + N equals the collateral, so the
vault cannot be under-collateralized and no liquidation threshold exists to cross. The holder keeps
one leg and sells the other; the proceeds are the liquidity. An oracle is read once, at settlement.
Then the two legs recombine, or roll.

[`canton-pitch-deck.md` Slides 3, 5; `asset-manager-pitch-deck.md` Slides 3, 4, 5]

### The one diagram — "the line with nowhere to sit"

A payoff chart the audience can redraw from memory. Horizontal axis: the reference price `x`, with
the strike `S` marked. Vertical axis: value, in units of the collateral, from 0 to 1.00.

- A flat reference line at **1.00** across the whole axis, labelled *collateral*.
- **P**: flat along 1.00 from the left edge to the strike, then curving down to the right as `S/x` —
  approaching zero, never reaching it, never stepping.
- **N**: flat at 0 from the left edge to the strike, then rising as `1 − S/x`.
- P and N stacked: their sum traces the 1.00 line exactly, at every price on the axis. That is the
  invariant, drawn.
- The single annotation: a vertical liquidation threshold of the kind every other venue draws — shown
  once and then removed, because there is no `x` where the stack falls below the collateral line.

Nothing else on the diagram. No palette, no styling: the design contenders own that.

---

## 5. Five proof points

| # | Proof | Source |
|---|---|---|
| 1 | The market names the liquidation pathway as its own unsolved problem: RWA looping "must account for monthly or quarterly redemption cycles, NAV-based pricing, and the need for formal liquidation agreements with asset issuers. These are not edge cases but fundamental design constraints." | `rwa-redstone-2026.md`, Part 2, "Liquidation mechanics and risk frameworks" |
| 2 | Institutional demand for RWA lending is live and permissioned: Morpho RWA deposits **$620M+** by March 2026 at **87% utilization**; Aave Horizon **$423.5M** market, **$106M** borrowed, **269 addresses**, borrow rates ~2–6%. | `rwa-redstone-2026.md`, Part 2, "Who lends against what" |
| 3 | Collateral has already rotated toward the assets a split fits: tokenized T-bill deposits **−92%** from a ~$194M peak while tokenized **gold grew 7x**; gold borrows at a conservative **~40%** ratio in non-looped borrowing. | `rwa-redstone-2026.md`, Part 2, "Gold vs T-bills" |
| 4 | The economics are measured, not modelled: **9-year** backtest (Hypercall, Aug 2017–Jun 2026; ETH underlying, Deribit options, Black-Scholes at mid) — net drift **−1.25%/yr**, P ending **$0.895** on **$1.00**; roll cost **−1.2%/yr** at 10bps across ~12.2 rolls a year; best sub-period gross theta **+0.57%/yr** (2021–22). | `asset-manager-pitch-deck.md` Slides 3, 12; `canton-pitch-deck.md` Slide 3 |
| 5 | The system exists and runs: **54 DAML templates across 9 modules**, a **12-agent** TypeScript fleet behind a Go ledger service with **6 core agents live**, a React frontend end-to-end, closed-form invariant proofs — deployed on Canton single-node and int clusters. Not yet: mainnet, audit, real collateral, users, revenue. | `canton-pitch-deck.md` Slides 8, 9 |

Supporting citations available on request in the same shape: Canton **$344B represented / $2T-a-month
repo** [`canton-pitch-deck.md` Slide 4]; Franklin Templeton BENJI **$800M on-chain** within **$2.5B**
digital AUM and the first on-chain Treasury trade executed on Canton via Tradeweb, July 2026
[`canton-pitch-deck.md` Slide 7]; Black Thursday **$8M** of collateral auctioned for **$0**, Mango
Markets **$116M** [`canton-pitch-deck.md` Slide 2].

---

## 6. Top five objections

**1. "No liquidation just moves the loss somewhere. Where did it go?"**
To P, continuously and computably. P is short a call above the strike, so P's value falls as
`P = S/x` when the reference asset rallies — no floor, but no cliff and no margin call either, and
that decline is the source of P's income rather than a side effect. The payoff at any given price is
fully computable; the *distribution* of future prices is not, and depends on a volatility model
[`asset-manager-pitch-deck.md` Slides 4, 7]. Say it as the deck does: the claim is that forced
liquidation is impossible, not that principal is protected.

**2. "Net drift is negative. Why would anyone hold P?"**
Because P is an options-income position, not a yield position, and the −1.25%/yr is the published
cost of never being liquidated [`canton-pitch-deck.md` Slide 3]. Two qualifiers we volunteer: the
dominant driver is roll execution, −1.2%/yr at 10bps over ~12.2 rolls a year, so execution quality
moves the number materially; and the backtest is ETH-only and third-party, while the flagship RWA use
case has different volatility characteristics [`asset-manager-pitch-deck.md` Slide 3;
`canton-pitch-deck.md` Slide 3]. A fund holding P is running a covered-call-shaped program and should
price it as one [`asset-manager-pitch-deck.md` Slide 5].

**3. "My collateral is a tokenized money-market fund. Near-zero vol — is there anything here?"**
Honestly, not much, and we would say so. An options split needs volatility for N to be worth
anything, and the market has already voted with the collateral: T-bill deposits on Morpho fell 92%
while gold grew 7x [`rwa-redstone-2026.md`, Part 2]. Tokenized gold is the realistic first RWA
underlying — continuous pricing, real volatility, visible non-looped demand at ~40% LTV, and a
cleaner commodity-option regulatory lane. Private credit is the largest slice and the worst
mechanical fit: illiquid, NAV-priced, and flagged in the report itself as lacking DeFi compatibility
[`rwa-redstone-2026.md`, Part 1 §(b)4 and Part 2].

**4. "Who takes the other side? If I keep N, someone has to buy P."**
Two-sided demand is endogenous to the structure: the holder keeps the leg matching their intrinsic
reason for holding the asset, and the other leg is a defined-outcome product someone else wants — a
fund treasury takes income on idle assets while a speculator takes leveraged RWA exposure with no
liquidation price [`canton-pitch-deck.md` Slide 6]. Mechanically, a MarketMakerAgent provides P/N
secondary liquidity [`canton-pitch-deck.md` Slide 8], and Canton-native rails are being explored with
Send.it — CUSD for settlement, Pool Party for P/N secondary liquidity [`canton-pitch-deck.md`
Slide 6]. It stays on the risk register: liquidity risk for N is listed as present and unmitigated
beyond those two mechanisms [`asset-manager-pitch-deck.md` Slide 7].

**5. "None of this is audited and none of it is on mainnet."**
Correct, and here is the exact line between the two. Real: 54 DAML templates across 9 modules, a
12-agent fleet with 6 core agents live, a React frontend running end-to-end, closed-form invariant
proofs, ~2,900 lines of US regulatory analysis not yet reviewed by counsel, deployed on Canton
single-node and int clusters. Not real: mainnet deployment, real collateral, live users, a
third-party audit, revenue [`canton-pitch-deck.md` Slides 9, 12]. The July 2026 plan put two
independent DAML audits and a fund-counsel regulatory opinion in Q3 2026, mainnet in Q4 2026, the
compliance layer in H1 2027 and a first institutional pilot in H2 2027 [`canton-pitch-deck.md`
Slide 12] — dates as-of that source, not a commitment restated today.

---

## 7. Terminology guardrails

Held from `house-brand-guide.md` §8.2 and §8.1:

- **Protected Token / P Token**, never "stable token" — P drifts and is not pegged.
- **Amplified Token / N Token**, never "leverage token."
- **Split** and **recombine**, not mint and burn. **Settle**, not exercise.
- **Drift** and **theta**, never "yield" or "interest" — we do not promise returns.
- **Can't be liquidated**, never "liquidation-resistant." The claim is not hedged.
- Every surface that states the guarantee stays within one slide of the cost (§0.8, "Costs, named").
  In this deck: slide 7 states the guarantee, slide 8 states the cost.
