# Product

<!-- impeccable:product-schema 1 -->

> **Interview substitution notice.** `reference/init.md` Step 3 requires one real
> ask round through a structured question tool before writing this file. This
> session runs as a non-interactive design contender with no AskUserQuestion tool
> and no decision-page browser in its tool surface, so the mechanical test for an
> answer mechanism fails. Every fact below is therefore inferred from the explicit
> brief (`rwa-bakeoff/BRIEF.md`) and the three messaging contracts, and is marked
> **[inferred]** where the brief does not state it outright. Nothing here was
> confirmed by a human.

## Platform

web

## Stack

Plain static HTML/CSS/JS, single self-contained file per artifact. **[inferred —
fixed by the task]**: the deliverables are `index.html` (1280×720 fixed stage) and
`explainer.html` (1920×1080 stage), each self-contained, no build step, no bundler,
no remote assets except Google Fonts (permitted in `free` mode only).

## Users

Primary: RWA issuers, tokenization platforms, asset managers, and their risk and
product leads. Secondary: chain-ecosystem BD people who make the introduction and
then forward the artifact.

Situation and job: finance-literate, technical-adjacent, **not** DeFi-native. They
know collateral, NAV, strike, maturity, redemption windows, call options, oracles,
settlement. They do not know what a liquidation cascade feels like from inside, and
terms like MEV, looping, sub-transaction privacy and DAML must be explained if used.
The deck is presented once in ~10 minutes and then forwarded and read alone; the
film is watched alone, often with sound off on the first pass.

The decision they hold: a credibility judgment plus the authority to grant a
conversation — "should we spend an hour on this / should I introduce them". Not a
cheque, not an allocation.

What they distrust: numbers whose provenance is not named; enthusiasm with no
downside attached; a comparison table where the presenter wins every row; anyone
claiming a novel structure is safe; backtests without their underlying.

## Product Purpose

Medici is a collateral-splitting primitive for tokenized real-world assets. A
tokenized RWA position is split into two claims that always sum back to the
collateral:

- **P** — the protected leg. No margin calls, no forced sale. Capped upside;
  computable decline above the strike (P = S/x). An options-income product, not a
  yield product.
- **N** — the amplified leg. Receives everything above the strike.

Success for these three artifacts: the viewer leaves able to (1) say in one sentence
what Medici is, (2) name why a tokenized-asset holder or issuer cares, and (3) redraw
the P/N split from memory as one diagram.

## Positioning

`P + N ≡ collateral` is a closed-form invariant, not a risk parameter. Because no
under-collateralization condition exists anywhere in the payoff function, no
liquidation threshold exists to breach — forced liquidation is mathematically
impossible rather than merely unlikely. Neighboring products (Aave, Maker, Compound,
Morpho, Aave Horizon) all price collateral against a threshold and then hand-build
the workout pathway with signed issuer liquidation agreements and curator-run
de-leverage frameworks. That is the claim a neighbor could not truthfully copy.

Supporting position: oracles are read lazily, once, at settlement — there is no live
feed to manipulate mid-position. Split, roll and settlement are single atomic
transactions. Positions are stakeholder-scoped on Canton (sub-transaction privacy),
which is where the collateral already lives.

## Operating Context

Two artifacts, three messaging contracts, six renders:

- **Deck** — 1280×720 fixed stage, presented live in about 10 minutes, then emailed.
  Keyboard ←/→ and click navigation, a slide counter, `@media print` paginating one
  slide per page at 1280px × 720px. It must survive being read with no narrator.
- **Explainer** — 1920×1080 stage, 120–143 s depending on contract, auto-playing on
  load, meant to be screen-recorded by a human into a video. No audio, no TTS, no
  video element. `?scene=N`, Space and → override the timeline; `window.__player`
  is exposed for the recording tool.

Every slide carries the footer `Medici — Proprietary & Confidential`.

## Capabilities and Constraints

- Every figure on screen traces to a messaging contract slot; **no invented numbers**,
  no invented customers, no projections, no TAM.
- The messaging contracts are consumed verbatim: slot order fixed, headline claims
  fixed (re-breaking a line is fine, rewording is not). An unrenderable slot is
  logged, never dropped.
- Body text ≥ 18px on the deck, ≥ 28px on the explainer; contrast ≥ 4.5:1.
- Terminology the audience already owns: collateral, strike, maturity, call option,
  oracle, settlement, on-chain. Terminology that must be explained on first use:
  liquidation cascade, MEV, sub-transaction privacy, DAML.
- Roadmap and market figures are as-of their source date (Medici decks July 2026;
  RedStone landscape March 2026) and every surface carrying one says so.
- The corpus disagrees with itself on two counts (54 templates / ~5,700 LOC vs 36 /
  ~5,100; ~2,900 vs 2,600 lines of regulatory analysis). The brief's source priority
  resolves both to the canton deck; the contracts already did this and the design
  layer does not re-litigate it.

## Brand Commitments

Fixed in `free` mode: the name **Medici**, the legal identity **AAA Flowers S.A.
(Panama), operating as Medici**, and the footer string `Medici — Proprietary &
Confidential` on every slide. Everything else — palette, type, layout, motion — is
this design contender's own judgment. The house brand guide is deliberately **not**
read in this mode. **[inferred — fixed by the task]**

## Evidence on Hand

Real, cited, usable:

- Canton: $344B represented, $2T/month repo; Franklin Templeton BENJI $800M on-chain
  within $2.5B digital AUM; Franklin Templeton, WisdomTree, Invesco, BlockBooster
  issuing (May–Jul 2026).
- Morpho RWA deposits ~zero early 2025 → $620M+ by March 2026 at 87% utilization;
  T-bill collateral −92% from a ~$194M Oct 2025 peak while tokenized gold grew 7×
  at ~40% borrow-to-collateral. Aave Horizon: $423.5M market, $106M borrowed, 269
  addresses. Tokenized treasuries $12.9B, ~+300% YoY (rwa.xyz, July 2026). $840M+
  tokenized RWA deposited into DeFi lending.
- Black Thursday, March 2020: ~$8M of MakerDAO collateral auctioned for $0. Mango
  Markets: $116M through a real-time oracle read.
- RedStone (with Credora, Gauntlet, Dune), 2026-03-26, verbatim: formal liquidation
  agreements with asset issuers "are not edge cases but fundamental design
  constraints."
- Hypercall backtest, Aug 2017 – Jun 2026, ETH underlying, Deribit options,
  Black-Scholes at mid: net drift −1.25%/yr, P ends at $0.895 on $1.00; roll cost
  −1.2%/yr at 10bps across ~12.2 rolls/yr; best sub-period gross theta +0.57%/yr
  in 2021–22.
- Build state: 54 DAML templates across 9 modules (~5,700 LOC), 12 TypeScript agents
  behind a Go Ledger Service (6 core live, 6 in progress), React frontend end-to-end,
  closed-form invariant proofs, Canton single-node + int clusters.
- Named people: Ian (technical lead), Co-founder (RWA tokenization),
  Co-founder (growth).

Explicit absences that must never be fabricated: **no mainnet deployment, no real
collateral, no live users, no third-party audit, no revenue, no customer logos, no
testimonials, no screenshots of a running product, no photography of any kind.** No
image-generation tool is available to this session, so every visual is drawn in code.

## Product Principles

1. **The invariant is the product.** Every surface that can show `P + N ≡ collateral`
   as an unbroken quantity should show it, not assert it.
2. **The absence is the argument.** The thing to dramatize is a line that cannot be
   drawn — a threshold with nowhere to sit — not a feature that can.
3. **Volunteer the cost before it is asked for.** P is short a call; the decline is
   the income; nothing is on mainnet. Stating the limit early is what buys the
   mechanism its credibility with this audience.
4. **Provenance travels with the number.** Every figure carries its source on the
   same surface, because this audience distrusts unattributed numbers more than it
   distrusts a small number.
5. **It must survive being forwarded.** Every headline claim is a complete sentence
   that stands without a narrator.

## Accessibility & Inclusion

Deck body ≥ 18px, explainer body ≥ 28px, contrast ≥ 4.5:1 for body text throughout.
Keyboard navigation on both artifacts. The explainer carries no audio, so nothing is
carried by sound alone; the film's first pass is assumed silent. `prefers-reduced-
motion` is honored on the deck; the explainer is a recording target and keeps its
timeline, but does not rely on motion to carry any figure that the on-screen text
does not also state.
