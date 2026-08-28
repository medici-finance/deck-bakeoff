# Medici for RWA — comprehension diagnosis and messaging fix

**Medici** (AAA Flowers S.A.) · August 2026 · v0.1
method: `skills/messaging/house-guide/messaging-guide.md` (Assay, v0.1, 2026-07-17), applied
faithfully to a different product · all seven sections
audience: RWA issuers, tokenization platforms, asset managers and their risk/product leads, plus
the chain-ecosystem BD people who introduce them — finance-literate, technical-adjacent, not
DeFi-native

Grounded in: `source/medici/canton-pitch-deck.md` (2026-07-04), `source/medici/asset-manager-pitch-deck.md`
(2026-07-04, reframed 2026-07-18), `source/medici/rwa-redstone-2026.md`, `source/medici/rwa-standards-canton.md`,
`source/medici/authorization-pitch-deck.md` (background), `source/brand/house-brand-guide.md` §0, §8.

**The sequencing rule this whole document serves**: scene → value → mechanism → honest boundary.
Every failure in §1 is a violation of it, and every fix in §2–§7 is a restoration of it.

---

## 1. DIAGNOSIS — why a finance-literate reader stalls on the current decks

The two source decks are unusually honest and unusually well-organised for strawman drafts. They
still fail comprehension, in the same nine ways the method names, and mostly for the same root
cause: **they are written from inside the mechanism, for a reader who already believes the
mechanism matters.**

**B1. The headline states what the product does not do, before saying what it is.** Both decks open
on a negation: *"No forced liquidation. Ever."* (canton Slide 1) and *"Lending against BTC — with no
liquidation price."* (asset-manager Slide 1). The closer is worse: *"No liquidation price exists.
That sentence is the product."* (asset-manager Slide 15). That line is a payoff — satisfying after
you hold the model, hollow before it. A reader who does not yet know that liquidation is the
mechanism being removed hears a feature they were not worried about. The brand's own essence,
*"The math holds"* (brand guide §0.5), is explicitly labelled internal for exactly this reason; the
decks are one step away from putting it on a slide.

**B2. Category soup in the lede.** *"a collateral-splitting primitive for tokenized real-world
assets"* (BRIEF), *"a novel DeFi primitive live on Canton that no other RWA chain has"* (canton
Slide 1 ask), *"protocol-grade software for options-based synthetic assets"* (brand §0.1). Three
abstractions per phrase — *primitive*, *synthetic asset*, *protocol-grade* — and no concrete noun
for what the buyer holds afterwards. "Primitive" is DeFi-native vocabulary presented to an audience
the brief classifies as not DeFi-native.

**B3. Metrics before mental model, and the first one is a loss.** Both decks put the economics
table on the *"What Medici is"* slide (canton Slide 3, asset-manager Slide 3), so the reader's first
quantitative impression of the product — before they know what P and N are — is **net drift
−1.25%/yr**, followed immediately by its caveats (*"the backtest is third-party and ETH-only; the
flagship RWA/MMF use case has different vol characteristics"*). The discipline is right and rare.
The placement asks a reader to price a structure they cannot yet picture, which is not scepticism-
management, it is comprehension debt.

**B4. Insider vocabulary, unglossed, at density.** Asset-manager Slide 3 uses, in one table:
*P*, *N*, *strike*, *theta*, *roll*, *oracle*, *Deribit*, *Black-Scholes at mid*, *net drift* —
nine terms, none glossed, above the fold of the first content slide. Elsewhere: *sub-transaction
privacy*, *lazy/on-demand oracle*, *DAML*, *Canton*, *MEV*, *mempool*, *perp DEX*, *looping*,
*liquidation cascade*, *ERC-3643*, *T-REX*, *ONCHAINID*, *propose-accept*, *CIP-0056*. Each costs a
parse. The worst offenders are the two that look like plain English: **"roll"** (finance-literate
readers know it, RWA product leads often do not, and it is where the dominant cost lives) and
**"settlement"** (which here means one specific dated event, not the ordinary post-trade sense).

**B5. Abstraction without a worked example.** Neither deck ever instantiates the payoff with
numbers. Canton Slide 5 gives `P receives S/x`; asset-manager Slide 5 walks a $10M BTC vault through
six steps and never states what anyone receives at maturity at any price. The one closed-form
identity the whole product rests on is never once shown *arriving at a dollar figure*. A reader who
cannot compute one example cannot redraw the diagram, and the brief's third educational goal is
exactly that they can.

**B6. No before/after.** Nowhere does either deck put the buyer's **current** world beside the
Medici world for the same asset: the position page, the loan-to-value line, the curator's LTV
policy, the margin call, the signed liquidation agreement with the issuer. The material for it is
sitting unused in `rwa-redstone-2026.md` Part 2 — the market's own account of how it handles RWA
collateral today is a hand-run workout desk, and it is the strongest before-picture in the corpus.

**B7. Too many novelties at once.** The canton deck asks a first-time reader to absorb, in twelve
slides: a new payoff structure (P/N), a new ledger (Canton), a new operating model (a 12-agent
autonomous fleet), a new compliance stack (ERC-3643 registries), a new settlement rail (Send.it /
CUSD / Pool Party), and a new entity posture (Panama development company, SPV to follow). Any one
is a pitch. Six is a seminar, and the P/N split — the only one the audience must leave holding —
gets one slide of the six.

**B8. Claims that overreach the thing actually proven.** This is the house's F-08 analogue, and it
needs care, because the brand guide's tone principle 4 (§8.1) *requires* the liquidation claim to be
stated without hedging — and that requirement is correct. The defect is not the unhedged claim; it
is the **silent widening of its scope from the payoff function to the system**:

| Where | The claim as written | Why it overreaches |
|---|---|---|
| asset-manager Slide 7 (risk table) | *"Forced-liquidation risk — ✗ None"*, *"Counterparty risk (Medici mechanism) — ✗ None"* | A risk table is a statement about the deployed system, not about the payoff algebra. The same slide concedes the contracts are unaudited; unaudited code cannot carry a "none" row. |
| canton Slide 3 | *"Forced-liquidation risk — **Zero** — no margin call, no forced sale, no bad debt"* | "Zero", in a properties table beside operational facts, reads as a system property. |
| asset-manager Slide 14 | *"The mechanism is de-risked… That's execution risk, not research risk"* | Proven math plus unaudited implementation is not de-risked. Two independent audits are named as unfunded Phase 1 work on the very next slide. |
| both decks, Slide 9/12 | *"Verification — closed-form invariant proofs, pure tests"* listed beside *"not yet audited"* | True and load-bearing, but adjacency invites the reader to hear "proved" as "proved correct in production". |

**The defensible claim is narrower and lands harder**: *there is no liquidation threshold in the
payoff function, so no price move can force a sale — and everything else about this system is
ordinary technology risk that we name.* Say the guarantee unhedged; say its scope precisely.

**B9. Honest boundaries placed before comprehension.** Both decks put the cost inside the
"what it is" slide, and both put the maturity disclosure late — the exact inversion of what works.
The cost belongs *after* the mechanism, where a reader can price it, and the maturity disclosure
belongs at the close, where it reads as seriousness. The corpus already knows this: the brand guide
§0.8 says a surface stating the guarantee should be *"within one click or one slide of the cost"* —
one slide **after**, not on the same slide.

**One structural finding beyond B1–B9, because the diagnosis surfaced it.** The two decks
disagree with themselves about the flagship RWA underlying. Canton Slide 7 and asset-manager Slide 6
sell tokenized **fund shares and MMFs**; `rwa-redstone-2026.md` (takeaway 2, both passes) concludes
that near-zero-volatility collateral is the *worst* fit for an options split and names **tokenized
gold** first. An options split needs volatility to make N worth anything. Messaging that promises an
MMF split works is selling against the house's own research, and a risk lead will find it.

---

## 2. THE 30-SECOND VERSION (say this first, verbatim-usable)

> Tokenized fund shares and treasuries only start earning when you post them as collateral — and
> every venue that takes them can force-sell them. Medici splits the position instead. One
> tokenized asset becomes two claims: a protected one and an amplified one. Sell either, keep the
> other. The two always add back up to the collateral, at every price, so there is no liquidation
> price to breach — there is nothing to force-sell. What it costs is the upside above a price you
> set.

**79 words. At 150 words per minute that is 32 seconds** — the arithmetic matters, because the
method's own source artifact labels a 250-word passage as a 30-second version and it is not one.

**The 90-second extension** (append when you have the room; do not lead with it):

> Here is what the market does today. A tokenized fund unit redeems monthly, at a valuation nobody
> can strike intraday, and it is posted to a lending market whose liquidation logic assumes it can
> be sold this afternoon. Everyone knows it cannot, so the gap is patched by hand: signed
> liquidation agreements with the issuer, a curator running a de-leverage framework, direct lines
> to the fund. That is a workout desk bolted onto a mechanism that does not fit the asset.
>
> Medici removes the mechanism rather than patching it. The protected claim pays out in full at or
> below the price you set. Above it, the protected claim's value declines — continuously,
> computably, and that decline is exactly what the income on it is paid for. The amplified claim
> receives everything above that price. The two sum to the collateral at every price, which is why
> no threshold exists to breach.
>
> To be precise about what that does and does not remove: it removes the forced sale. It does not
> remove loss. If the asset rallies hard the protected side is worth less, with no floor — and in a
> nine-year third-party backtest on ETH, the published cost of running the structure was about
> 1.25% a year. Today it is a working system on a development cluster: no mainnet, no audit, no
> real collateral, no users. What we are asking for is the conversation, not a commitment.

Both versions obey the sequence: **scene** (idle asset, and the one thing you must do to make it
productive) → **value** (nothing can force a sale) → **mechanism** (two claims, one identity) →
**honest boundary** (the loss, the cost, the maturity), in that order, every time.

---

## 3. ANALOGY SET (each with its honest break)

| # | Analogy | One-liner | Where it breaks |
|---|---|---|---|
| 1 | **Selling the top floor of a building you keep** | You own the building and keep the rent. You sell, for cash today, the right to whatever it is worth above an agreed price. Nobody can foreclose, because nobody lent you anything. | Air rights sell once, permanently. Here the sale expires at maturity and has to be re-struck — a *roll* — and roll execution at 10bps about 12 times a year is **−1.2%/yr**, the dominant cost of the whole structure (asset-manager Slide 3). The analogy hides the recurring cost; say it in the same breath. |
| 2 | **Stripping a bond into principal and coupons** | One instrument becomes two claims that sum back to the original, and each side goes to a buyer who wants that half. Standard, boring, decades old. | STRIPS split a *known schedule*; both halves accrue. P and N split a *price-dependent* payoff — P does not accrue toward par, it declines when the asset rallies. The familiarity is a loan you have to pay back in the next sentence. |
| 3 | **A pawnbroker versus a co-owner** | A margin loan is a pawnbroker: miss the line and your item is sold at whatever the shop can get. Medici is closer to selling a share of the item — no one can seize it, because no one is owed anything. | A co-owner has no expiry and no strike. N's claim is defined and settles on a date. And a co-owner does not "lose" when the asset rises; P does. Use this analogy for the *seizure* point only, then drop it. |
| 4 | **Writing an insurance policy for the premium** | The income on the protected side is a premium for a policy that pays out if the asset rallies past the agreed price. | Insurance works by diversifying uncorrelated risks. Every P holder writes the same policy on the same asset at the same time, so the losses are perfectly correlated — this is a premium, not a book. |
| 5 | **A fire door with no lock on it** | A liquidation threshold is a lock that someone else holds the key to. Medici's payoff has no lock, because it has no door: there is no state in which the position is worth less than the collateral backing it. | The absence is real in the payoff function and only there. The contracts, the price read at settlement, and the custody chain above the token are all ordinary risks that remain — the analogy tempts a listener to hear "nothing can go wrong". |
| 6 | **Double-entry bookkeeping** (brand-native, brand guide §0.6) | The Medici bank's technology was the ledger: no entry recorded unless it balances. P + N = the collateral is the same idea — the contract cannot record an unbalanced state. | Double entry catches *recording* errors, not *valuation* errors. It says nothing about whether the collateral in the vault is worth what its token claims, which is the upstream custody question Medici does not touch. Use in a keynote; never as the primary explanation, because it explains the invariant and not the payoff. |

**Best openers by audience.** Fund treasury / issuer → **#1** (it is the only one that names the
cash today). Risk committee → **#3 then #4** (seizure first, correlation second — they will ask).
Chain-ecosystem BD, introducing you to someone else → **#2** (it survives being retold by a
non-specialist). Keynote or brand surface → **#6**, and only there.

**Never use**: "a savings account", "a floor", "principal protection", "hedged". The brand's
terminology canon (§8.2) bans the first three by implication; the fourth is false — P is capped,
not floored, and the corpus says so on both Slide 3s.

---

## 4. DEMO NARRATIVE — the "aha" in minute one

The current failure mode: the decks open inside the machinery — the invariant, the templates, the
agent fleet, the chain — and make the viewer reverse-engineer why any of it was needed. Invert it.
Stage the buyer's problem, show the mechanism arriving, then show it **losing money on purpose**,
and only then open the machinery.

1. **(0:00–1:00) The scene, on their screen, not ours.** A tokenized fund unit posted as collateral
   on a lending market: a loan-to-value line, a liquidation price in red. Say it out loud: *"That
   number says this position can be sold this afternoon. The asset redeems monthly. It cannot."*
   Then show what the market actually does about that — the curator's de-leverage framework and the
   **signed liquidation agreement with the issuer** (`rwa-redstone-2026.md` Part 2). *"This is a
   workout desk bolted onto a mechanism that does not fit the asset."* That is the aha frame:
   everything after is one alternative to a hand-run patch.

2. **(1:00–2:30) One position, one split, real numbers on screen.** Deposit a round number of units.
   Set a price. Two claims come back. Then **walk the price** and let the viewer watch the two
   claims move against each other while their sum sits still. Do not narrate the algebra; let them
   see the sum not move. This is the diagram they will redraw, and it must be a thing that moves,
   not a formula that is asserted.

3. **(2:30–4:00) The catch, staged deliberately.** Run the price well above the strike and let the
   protected claim visibly shrink. Say the number. *"This is the loss. It is continuous, it has no
   floor, and it is not a malfunction — it is what the income on this side is paid for."* This is
   the emotional peak of the whole demo. Adverse evidence, volunteered, is the most persuasive
   thing in the room, and it is the moment a risk lead starts trusting the rest.

4. **(4:00–5:30) Maturity, in one transaction.** One price, read once, on the day. Both claims
   settle together — no partial fills, no interim price feed to be gamed, no gas auction. The
   position was visible to the two counterparties and to nobody else, for its whole life. Show a
   transaction, not an architecture diagram.

5. **(5:30+) Machinery and boundaries, only now.** The contract set, the operating agents, the
   compliance registry, the chain. Then the maturity statement, plainly: development cluster, no
   mainnet, no audit, no real collateral, no users, no revenue. Delivered here it reads as
   seriousness. Delivered on slide three it reads as a warning label.

**Do not show early**: the agent-fleet table, contract or line counts, ERC-3643 registry mechanics,
the entity structure, the capital ask, the roadmap, or the −1.25%/yr drift figure before step 3. All
of them are answers to questions the viewer has not asked yet.

**The demo constraint the method did not anticipate**: there is no production system and there are
no users, so there is nothing to demonstrate *happening to someone*. The parameter walk in step 2 is
therefore the whole aha, and it has to be flawless. It is also the one asset that is cheap to build
honestly — it is arithmetic on a published payoff rule, not a simulation of a market.

---

## 5. GLOSSARY RULE (outbound material; contracts and internal docs keep their names)

The brand guide's terminology canon (§8.2) already fixes several outbound names. This table extends
it with the RWA-audience terms the canon does not cover, and it is a **gloss discipline**, not a
rename programme — the canon wins wherever the two touch.

| Term | Verdict | Outbound form |
|---|---|---|
| **P / N** | Keep, **always introduce by role first** | "two claims — a protected one and an amplified one (we call them P and N)". Never open a sentence with the letters. Canon: Protected Token / Amplified Token, never "stable" or "leverage" token. |
| **strike** | Keep, **gloss once** | "a price you set up front — the strike". After the first gloss, use it freely; this audience knows it. |
| **roll** | Keep, **gloss and cost it in the same sentence** | "at maturity you settle or re-open at a new price — a roll, and each one costs about 10bps". A roll mentioned without its cost is the single most misleading term in the set. |
| **theta** | Keep for finance audiences, **gloss** | "the income from selling that upside — theta". Canon bans "yield" and "interest": both imply a promised return. |
| **settlement** | Keep, **gloss once** | "settlement — the one day the price is read and both claims pay out". |
| **drift** | Keep, **gloss**, never compare to anything | "drift — the gap between holding P and simply holding the asset". Canon bans "impermanent loss" and "slippage". |
| **Canton** | Keep as a proper noun, **never lead with it** | Lead with the property: "it settles on the ledger where most tokenized institutional assets already sit — Canton". The chain is a *reason it works*, not the product. |
| **DAML** | **Internal / technical docs only** | Outbound: "the contracts". A slide headline containing "DAML" has spent a novelty budget on an implementation detail. |
| **sub-transaction privacy** | **Rename outbound** | "your position is visible to you and your counterparty, not to the market". Nine syllables of jargon for a sentence the audience already wants. |
| **lazy / on-demand oracle** | **Rename outbound** | "the price is read once, at settlement" — and immediately: "which is a smaller attack surface and a bigger single read; we use multiple independent feeds with a consensus threshold". State both halves; the corpus does (canton Slide 3). |
| **vault** | Keep, **gloss once** | "a vault holds one depositor's collateral" (canon: vault ≠ pool, and the distinction is load-bearing). |
| **primitive**, **synthetic asset**, **protocol-grade** | **Drop from outbound** | Say what the buyer holds: "two claims on your collateral". |
| **looping, MEV, mempool, perp DEX, liquidation cascade** | **Drop** (gloss only if the audience raises them) | This audience is not DeFi-native; each of these imports a whole world to explain a point already made. |
| **ERC-3643 / T-REX / ONCHAINID** | **Compliance conversations only** | Outbound first mention: "the permissioned-token standard institutional funds already use — the same one BUIDL uses". |
| **"zero risk", "counterparty risk: none", "de-risked", "risk-free", "principal protected"** | **Banned** (B8) | Replace with: "there is no liquidation threshold in the payoff function, so no price move can force a sale. The contracts, the settlement price and the custody chain above the token are ordinary risks, and we name them." |
| **"can't be liquidated"** | **Keep, unhedged** (brand §8.1 principle 4) | Say it flat. Never "liquidation-resistant", never "designed to prevent". Scope it to the payoff in the same sentence and it is both unhedged and true. |

**Standing rule for all outbound copy** (inherited verbatim from the method): every novel term gets
exactly one parenthetical gloss on first use, and no sentence may carry more than one unglossed
novel term. If a sentence needs two, it is two sentences. The nine-term table on asset-manager
Slide 3 is what this rule exists to prevent.

---

## 6. Category positioning — ride "productive collateral", win on the liquidation pathway

The market has already named both the category and the problem, in the same document, and neither
name is ours to coin.

**The category is "productive collateral."** It is the framing of the RedStone / Credora
*Tokenization & RWA Standards Report 2026* Part 2 (2026-03-26, with Gauntlet and Dune), which treats
vault standards as the layer that turns a held tokenized asset into working collateral, and states
the gap plainly: *"the gap between 'tokenized asset exists onchain' and 'functions as productive
collateral' is where vault infrastructure earns its relevance."* Adopt that vocabulary. It is the
sentence our buyers have already read.

**The problem inside it is the liquidation pathway**, and the report says so as a structural
finding, not an aside: RWA lending *"must account for monthly or quarterly redemption cycles,
NAV-based (rather than market-based) pricing, and the need for formal liquidation agreements with
asset issuers. These are not edge cases but fundamental design constraints."* Curators with
*"signed liquidation agreements, formal de-leverage frameworks, direct lines to asset issuers"* are
the industry's current answer. **Nobody in either part of the report offers a design without a
liquidation pathway.**

**The positioning line (verbatim-usable):**

> Medici is the productive-collateral design with no liquidation pathway.

And the retail version of the same sentence, for a room that has not read the report:

> Every way to make a tokenized asset productive today ends in someone's right to sell it. Medici
> is the one that does not, because there is no threshold in the payoff.

**Cite the lineage; do not re-coin it.** Two lineages, two layers, both named in the corpus:

- *The mechanism* — Vitalik Buterin, **"Options Instead of Debt"** (ethresear.ch/t/25036, cited on
  asset-manager Slide 3). Medici is an implementation of a published idea, and saying so buys more
  credibility than novelty does with this audience.
- *The category* — RedStone / Credora's **productive collateral** (Part 2, 2026-03-26). Use their
  words for the problem, ours only for the answer.

**The benchmark is Aave Horizon, not Aave.** The corpus's own revision (`rwa-redstone-2026.md`,
"What changes in the Part 1 analysis") lands on Horizon — the permissioned institutional RWA lending
market, **$423.5M market size, $106M borrowed, 269 addresses, ~2–6% borrow rates, as-of March
2026** — as the structural comparison. It proves demand at exactly this shape and it has a
liquidation pathway. That is the comparison a risk lead will accept; "we're not Aave" is one they
have heard.

**The honest boundary of the position**: Medici is not a better lending rate and must never be sold
as one (asset-manager Slide 8 gets this right and should be preserved). It is a different
instrument with a different loss shape, and the P side competes for an options-income allocation,
not a safe-yield allocation.

**Citation discipline** (binds this section and every deck that reuses it). Every venue figure above
is as-of **March 2026** and every Canton or issuer figure is as-of **July 2026**; both are stale by
the time anyone presents them. Re-dereference before use, and label the as-of date on the slide, not
in a footnote. A moving number asserted as a live fact is the failure this discipline exists to
prevent.

---

## 7. Content gate — trace every number, and refuse the ones that do not reconcile

Every figure below was re-derived against the corpus while writing this document. The gate is:
**no number ships whose derivation a reviewer cannot reproduce from a named file and slide.** Three
figures failed and are withheld; that is the gate working, not the gate misfiring.

| Figure | Value | Source (file · slide/section) | As-of | Re-derivation | Verdict |
|---|---|---|---|---|---|
| The invariant | P + N ≡ collateral | canton Slide 3, Slide 5; asset-manager Slide 4 | — | Identity, not a measurement. Stated identically in both decks. | **SHIP** — the one claim that needs no date |
| Payoff above strike | P = S/x; N = 1 − S/x | canton Slide 5; asset-manager Slide 4 | — | Both tables agree. Sums to 1 by construction. | **SHIP** |
| Net drift | −1.25%/yr; P ends at $0.895 on $1.00 | asset-manager Slides 3, 12; canton Slide 3 | Hypercall backtest Aug 2017–Jun 2026 | Third-party (Hypercall), **ETH** underlying, Deribit options, Black-Scholes at mid. $1.00 × (1 − 0.0125)^9 = $0.893 ≈ $0.895 — **re-derives** | **SHIP WITH ITS LABEL**: a third-party ETH backtest, not a Medici track record and not an RWA figure. Canton Slide 3 says the RWA/MMF case has different vol characteristics — say that too |
| Roll cost | −1.2%/yr | asset-manager Slide 3 | same backtest | 10bps × 12.2 rolls/yr = 122bps = **1.22% ≈ 1.2% — re-derives** | **SHIP** — and it is the most useful number in the corpus, because the buyer can check it |
| Gross theta | +0.57%/yr | asset-manager Slide 3 | best sub-period 2021–22 | Labelled "not the full-period average. Full-period gross was lower." Full-period gross is **not published**. Implied: net (−1.25) + roll (+1.2) ⇒ ≈ **−0.05%/yr** | **WITHHOLD** — a reader cannot bridge +0.57 to −1.25 without a number we do not publish, and the implied full-period figure is near zero. See NOTES Q2 |
| Contract templates | **54 templates / ~5,700 LOC** (canton Slide 9) vs **36 templates / ~5,100 LOC** (asset-manager Slide 12) | both decks | both 2026-07-04 | Two same-dated sources, two values, no reconciliation anywhere in the corpus | **WITHHOLD BOTH** — say "the contract set" with no count until a human reconciles. See NOTES Q1 |
| Compliance analysis | 2,900 lines (canton Slide 9) vs 2,600 lines (asset-manager Slides 7, 11) | both decks | both 2026-07-04 | Same conflict, same date | **WITHHOLD** — and the substance is the same either way: *drafted, not reviewed by counsel* |
| Agent fleet | 12 agents; 6 live, 6 in progress | canton Slide 8; asset-manager Slide 9 | July 2026 | Both decks agree on 12; canton names the 6/6 split | **SHIP** with the split stated — "six live, six in progress" is more credible than "twelve" |
| Canton scale | $344B represented; $2T/month repo | canton Slide 4 | July 2026 | Single-sourced in corpus; no external cite carried | **SHIP WITH AS-OF**, re-dereference before external use |
| Franklin BENJI | $800M on-chain within $2.5B digital AUM | canton Slide 7; asset-manager Slide 2 | July 2026 | Consistent across both decks | **SHIP WITH AS-OF** — and never as a customer. Canton Slide 11 lists these firms as *pilot conversations* |
| Fee | 5–10bps per transaction | canton Slide 7; asset-manager Slide 10 | July 2026 | Consistent | **SHIP** |
| Morpho RWA collateral | $620M+ deposits; gold 7×, T-bills −92%; gold ~40% borrow-to-collateral; 87% utilisation | rwa-redstone-2026 Part 2 | March 2026 | Dune-sourced in the report; internally consistent | **SHIP WITH AS-OF** |
| Aave Horizon | $423.5M market size; $106M borrowed; 269 addresses; ~2–6% borrow | rwa-redstone-2026 Part 2 | March 2026 | Report-sourced | **SHIP WITH AS-OF** |
| "RWA deposits in DeFi lending" | $840M+ | rwa-redstone-2026 Part 1, **via KuCoin's summary** | March 2026 | Secondary source summarising the report; the report's own venue figures are primary | **PREFER THE VENUE FIGURES**; if used, attribute to the summary |
| Black Thursday | March 2020; ~$8M collateral auctioned for $0 | canton Slide 2 ($8M); asset-manager Slide 2 (no figure) | March 2020 | The $8M appears in one deck only, with no external cite | **SHIP THE EVENT AND DATE; WITHHOLD THE $8M** until externally sourced |
| Mango Markets | $116M exploit | both decks Slide 2 | 2022 | Consistent; widely reported | **SHIP** |
| Tokenized treasuries | $12.9B, ~300% YoY | asset-manager Slide 14 (rwa.xyz) | July 2026 | Named external source, dated | **SHIP WITH AS-OF** |
| Mainnet | Q4 2026 | canton Slide 12 | as-of July 2026 | A roadmap statement, one month stale at time of writing | **SHIP AS A DATED INTENTION**: "targeted, as-of the July 2026 plan" — never as a commitment |

**Three standing rules this pass added to the method:**

1. **Two sources, same date, different values ⇒ withhold both.** The method's gate assumed a number
   either traces or does not. It has no rule for a number that traces to two places that disagree,
   and the corpus produced two such cases in one read.
2. **Prospect names are numbers.** "Franklin Templeton, WisdomTree, Invesco, BlockBooster" carry
   more implied claim than any figure on the slide. Every appearance must be visibly framed as a
   target market, never a relationship.
3. **Roadmap dates decay faster than figures.** Every timing statement carries "as-of \<source
   date\>" in the visible text. Q4 2026, stated in July, means something different in November.

---

## Immediate fixes for the two source decks

1. **Move the economics table off the "What Medici is" slide** in both decks (canton Slide 3,
   asset-manager Slide 3). It belongs one slide after the payoff table, where the reader can price
   it. That single move fixes B3 and B9 together.
2. **Add a worked example to the maths slide.** One deposit, one strike, three prices, three dollar
   outcomes. It costs one slide and it is the only thing that satisfies the brief's third
   educational goal.
3. **Rewrite the risk table's "None" rows** (asset-manager Slide 7) to scope the claim to the payoff
   function, per B8. Keep the unhedged liquidation claim; delete "de-risked" (Slide 14).
4. **Open on the buyer's world, not the mechanism.** Slide 2 of both decks argues the problem
   abstractly; `rwa-redstone-2026.md` Part 2 has the concrete before-picture — signed liquidation
   agreements and hand-run de-leverage frameworks — sitting unused.
5. **Reconcile the template and line counts, or delete them.** They are currently a due-diligence
   liability: whichever number a reader sees second, they will notice.
6. **Adopt the glossary in §5 as a copy lint** on every outbound surface, and put the gloss rule in
   the deck template so a nine-term table cannot be authored again.
