# Medici for RWA tokens — key messaging

**Method**: `skills/messaging/house-guide/messaging-guide.md` (the Assay comprehension-diagnosis
method), applied to Medici. The reasoning behind every line here is in
`messaging-guide-medici.md`; this file is the distilled, usable layer.
**Sequencing rule, everywhere**: scene → value → mechanism → honest boundary.
**Sources**: `source/medici/canton-pitch-deck.md` (2026-07-04), `source/medici/asset-manager-pitch-deck.md`
(2026-07-04, reframed 2026-07-18), `source/medici/rwa-redstone-2026.md` (report as-of 2026-03-26),
`source/brand/house-brand-guide.md`.
**Every number below cites its file and slide, and carries its as-of date.** Three figures in the
corpus failed the trace gate and are deliberately absent — see `messaging-guide-medici.md` §7.

---

## 1. The one-sentence definition (the repeatable line)

> **Medici splits a tokenized asset into two claims that always add back up to it — so the asset
> can be posted, sold against and earned on, with no liquidation price anywhere in it.**

Say it exactly this way every time. A claim repeated identically reads as a fact; paraphrased, it
reads as marketing (brand guide §0.8).

Two shorter forms, for when the line has to survive being retold:

- **Ten words**: "One tokenized asset, two claims that always sum back to it."
- **The BD version**, for someone introducing us to a risk lead: "They make a tokenized asset
  productive without giving anyone the right to sell it."

---

## 2. Positioning statement

> **For RWA issuers, tokenization platforms and asset managers holding tokenized collateral,
> Medici is the productive-collateral design with no liquidation pathway.** Everything else that
> makes a tokenized asset productive — money markets, permissioned institutional lending venues,
> prime-broker style desks — ends in someone's right to force a sale, and for collateral that
> prices at NAV and redeems monthly that right is patched by hand with signed liquidation
> agreements and curator-run de-leverage frameworks. Medici removes the mechanism instead of
> patching it: the payoff has no threshold to breach, because the two claims sum to the collateral
> at every price. The cost is the upside above a price you set, and it is published.

**Category vocabulary is borrowed, not coined.** "Productive collateral" is the RedStone / Credora
*Tokenization & RWA Standards Report 2026* Part 2 framing (2026-03-26). The mechanism's lineage is
Vitalik Buterin's "Options Instead of Debt" (ethresear.ch/t/25036, cited on asset-manager Slide 3).
Using their words for the problem and ours only for the answer is worth more credibility with this
audience than novelty is.

**The benchmark is Aave Horizon, not Aave** — the permissioned institutional RWA lending market
that proves demand at exactly this shape and has a liquidation pathway (`rwa-redstone-2026.md`
Part 2).

**What this positioning refuses to say**: that Medici is a better lending rate. It is a different
instrument with a different loss shape (asset-manager Slide 8).

---

## 3. Three value-prop pillars for RWA holders and issuers

### Pillar 1 — Nothing can force a sale, because nothing is owed

The protected and amplified claims sum to the collateral at every price, so there is no state in
which the position is short of itself and no threshold for a price move to breach. No margin call,
no forced sale, no bad debt in the payoff function. For collateral that cannot be sold in a single
transaction anyway — a fund unit that redeems monthly, priced at NAV — this removes a liability the
rest of the market currently manages with a signed agreement and a phone call to the issuer.

*Sources*: canton Slides 3, 5; asset-manager Slides 4, 5; `rwa-redstone-2026.md` Part 2
(liquidation mechanics).
*Boundary*: this is a property of the payoff, and only of the payoff. The contracts, the settlement
price and the custody chain above the token are ordinary risks and we name them.

### Pillar 2 — Income on an asset you keep, with the price of it written down first

Selling the protected claim is cash today against a position you still hold; keeping the amplified
claim is exposure above the strike with no liquidation price, no funding rate and no repayment
schedule. What it costs is stated in advance rather than discovered: the protected side gives up
everything above the strike, and its decline above the strike is exactly what its income is paid
for. In the corpus's nine-year third-party backtest — **ETH underlying, Hypercall, Aug 2017–Jun
2026** — net drift ran **−1.25%/yr**, of which **−1.2%/yr was roll execution** (10bps × ~12.2
rolls/yr, which re-derives to 1.22%).

*Sources*: asset-manager Slides 3, 5, 12.
*Boundary*: that backtest is third-party and ETH-only. It is not a Medici track record and it is
not an RWA figure — canton Slide 3 says so itself, and an options split needs volatility, so a
near-zero-volatility money-market share is the weakest case in the set, not the flagship.

### Pillar 3 — It settles where the collateral already is, privately, in one transaction

The assets are on Canton already — **$344B represented, $2T/month repo, as-of July 2026** — so the
split does not require moving anything to a new venue. A position is visible to its counterparties
and not to the market, because that is the ledger's data model rather than a permission setting.
The split, the roll and the settlement each execute as a single transaction, so there is no partial
fill, no interim price feed to game, and no gas auction between intent and execution: the cost of
execution is the spread.

*Sources*: canton Slide 4; authorization deck Slides 3, 4.
*Boundary*: Canton is absent from every RWA-lending venue map in the RedStone report — the assets
are there, the borrow demand documented in that report is not. Distribution is an open problem and
the corpus says so.

---

## 4. The mechanism (116 words)

A vault holds one depositor's tokenized collateral and splits it into two claims. You set a price
up front — the strike. The protected claim (P) pays out the full collateral value at or below that
price; above it, P pays the strike divided by the settlement price, and the amplified claim (N)
receives the rest. The two always sum to the collateral, at every price, which is why no
liquidation threshold exists: there is no state where the position is short of itself. Sell either
claim for cash today and keep the other. At maturity one price is read once, both claims settle in
a single transaction, and P plus N recombine into the collateral.

*Sources*: canton Slides 3, 5; asset-manager Slides 4, 5.

### The one diagram (a description, not a design)

**The sum that does not move.** A horizontal axis is the settlement price of the collateral, running
left to right through the strike, which is marked once. Two stacked quantities are drawn above it —
the protected claim below, the amplified claim above. Left of the strike, the protected claim is the
entire height and the amplified claim is nothing. Right of the strike, the protected claim falls
away as a smooth curve (it is the strike divided by the price) and the amplified claim takes exactly
what it gives up. **The top of the stack is a flat line all the way across, at the value of the
collateral.** That flat line is the whole product: it is what "no liquidation price" means, it is
what a listener redraws on a napkin, and the eye should find it before it finds anything else. One
worked instantiation belongs beside it — one deposit, one strike, three prices, three payouts —
because the identity is not believed until it has arrived at a number.

---

## 5. Five proof points

| # | Proof | Source (file · slide/section) | As-of |
|---|---|---|---|
| 1 | The absence of a liquidation threshold is checkable, not asserted: the payoff table is complete in two rows — at or below the strike P receives the full collateral value and N receives nothing; above it P receives S/x and N receives 1 − S/x. The two sum to the collateral in both rows, so no under-collateralised state exists to define a threshold over. | `canton-pitch-deck.md` Slide 5; `asset-manager-pitch-deck.md` Slide 4 | — (an identity) |
| 2 | The market names this exact problem as unsolved and is patching it by hand: RWA lending *"must account for … the need for formal liquidation agreements with asset issuers. These are not edge cases but fundamental design constraints"*, with curators running *"signed liquidation agreements, formal de-leverage frameworks, direct lines to asset issuers."* Nobody in the report offers a design without a liquidation pathway. | `rwa-redstone-2026.md` Part 2 addendum, liquidation-mechanics section (RedStone/Credora report) | 2026-03-26 |
| 3 | Demand exists at precisely this shape, at a permissioned institutional venue: Aave Horizon, **$423.5M market size, $106M borrowed, 269 addresses, ~2–6% borrow rates** — "fewer but larger institutional participants". | `rwa-redstone-2026.md` Part 2, Horizon section | 2026-03-26 |
| 4 | The collateral is already where this settles: Canton carries **$344B represented and $2T/month repo**; Franklin Templeton's BENJI is **$800M on-chain within $2.5B digital AUM**, and the first on-chain Treasury trade was executed on Canton via Tradeweb in July 2026. | `canton-pitch-deck.md` Slides 4, 7 | July 2026 |
| 5 | The cost is published and a buyer can re-derive it: net drift **−1.25%/yr** over a nine-year third-party backtest (Hypercall, Aug 2017–Jun 2026, ETH underlying, Deribit options, Black-Scholes at mid), of which roll execution is **−1.2%/yr** — 10bps × ~12.2 rolls/yr = 1.22%. | `asset-manager-pitch-deck.md` Slides 3, 12 | backtest to Jun 2026 |

**Deliberately absent**: contract and line counts (the two decks disagree — 54/~5,700 vs
36/~5,100, both dated 2026-07-04), full-period gross theta (not published; implied ≈ −0.05%/yr),
and the $8M Black Thursday figure (single-sourced in the corpus). See `messaging-guide-medici.md` §7.

---

## 6. Top five objections, in the audience's words

**O1 — "There is no such thing as no liquidation. You have moved the risk, not removed it."**
Half right, and the half that is right is the important one. What is removed is the *forced sale*:
there is no threshold in the payoff, so no price move triggers anyone's right to sell your
collateral. What is not removed is *loss*. The protected claim is economically short a call above
the strike; if the asset rallies its value declines continuously, with no floor, and that decline is
what its income is paid for. A forced sale and a market loss are different risks, and only one of
them is being claimed away. (`asset-manager` Slides 4, 7, 8.)

**O2 — "Our fund shares barely move. What is there to split?"**
On a near-zero-volatility instrument, not much — and this is the concession the source decks bury.
An options split needs volatility for the amplified claim to be worth anything, and the house's own
research reaches the same conclusion: tokenized T-bills are a poor underlying, T-bill collateral
demand fell **92%** on Morpho while tokenized gold grew **7×** over the same period, and gold is the
realistic first RWA underlying — continuous pricing, real volatility, conservative ~40%
borrow-to-collateral demand already visible. Tokenized equities are the named second target, with
infrastructure live and usage near zero. A money-market share is the weakest case in the set, and we
would rather say so than sell you a split that does nothing. (`rwa-redstone-2026.md` Part 2,
takeaways 2 and 5; as-of 2026-03-26.)

**O3 — "Who buys the other side?"**
Today: nobody, because there are no live positions. Structurally the design wants two-sided demand
that already exists for its own reasons — an income allocator who wants a capped, computable options
position, and a holder who wants exposure above the strike without a liquidation price — supported
by a market-maker agent for secondary liquidity. The honest state of it: the asset-manager deck
lists liquidity for the amplified claim as a present risk, and the RedStone report shows Canton
absent from every venue where RWA borrow demand is documented. Distribution is the open problem, not
the mechanism. (`asset-manager` Slides 7, 9; `rwa-redstone-2026.md` Part 2, "the Canton
distribution gap".)

**O4 — "You are not audited and not on mainnet."**
Correct, and the list is worth having in full: no mainnet deployment, no real collateral, no live
users, no third-party audit, no revenue. What exists is a working system on a development cluster —
the contract set, twelve operating agents with six live and six in progress, a React front end
running end to end, closed-form invariant proofs, and a US regulatory analysis that is drafted and
**not** counsel-reviewed. The named next steps are two independent contract audits and a fund-counsel
opinion; mainnet was targeted for Q4 2026 as of the July 2026 plan, which is a dated intention and
should be re-confirmed before anyone repeats it. (`canton` Slides 8, 9, 12; `asset-manager`
Slides 7, 12.)

**O5 — "Our investors and our transfer restrictions cannot move to a new chain."**
They do not have to move, and Phase 1 asks no one's permission. The claims deploy as ERC-3643
permissioned tokens — the same standard BUIDL uses — on Medici's own identity registry, which no
counterparty can freeze or revoke; investors already verified with a major tokenized fund can be
fast-tracked rather than re-onboarded. The stretch goal of sharing an existing fund's registry needs
the fund sponsor's written consent and Securitize's active participation, is realistically 12–24
months after an audited mainnet deployment, and is not assumed anywhere in Phase 1. One caveat we
volunteer: the legal basis for that fast-track is itself a named Phase 1 question for fund counsel —
money-market-fund KYC is not derivatives-product KYC in every jurisdiction. (`asset-manager`
Slide 6; appendix "KYC fast-track legal basis".)

---

## 7. Copy rules that bind every surface using this messaging

- **Gloss rule**: every novel term gets exactly one parenthetical gloss on first use, and no
  sentence carries more than one unglossed novel term. Full table:
  `messaging-guide-medici.md` §5.
- **Never lead with the letters** P and N, with "Canton", or with "DAML". Lead with the role, the
  property, and the contracts respectively.
- **Never say** "zero risk", "counterparty risk: none", "de-risked", "risk-free", "principal
  protected", "stable token", "yield", "impermanent loss", or "liquidation-resistant".
- **Do say**, flat and unhedged: "there is no liquidation price — the math does not permit it",
  scoped in the same sentence to the payoff function.
- **A roll is never mentioned without its cost.** Ten basis points, about twelve times a year.
- **Prospect names are claims.** Franklin Templeton, WisdomTree, Invesco and BlockBooster appear in
  the corpus as pilot conversations and target market. They may never be shown in a way that implies
  a relationship.
- **Every number carries its as-of date in the visible text**, not in a footnote.
