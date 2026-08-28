# Product

<!-- impeccable:product-schema 1 -->

> **Interview substitution, disclosed.** `init.md` step 3 requires a real probe through a
> structured question tool before inferring. This session's tool surface carries no
> question/decision tool (no `AskUserQuestion`, no browser for `serve-question.mjs`; the
> task brief is explicit that nothing leaves the directory and no network calls are made).
> The probe mechanism does not exist, so every fact below is inferred from the explicit
> brief and the three messaging contracts, and every inference is labelled `[ASSUMED]`.
> Nothing here was confirmed by a human.

## Platform

web

## Stack

`[ASSUMED — pinned by the task brief, not by a user answer]` Plain static HTML/CSS/JS,
one self-contained file per artifact. Fonts self-hosted as local `woff2` beside each
artifact. No build step, no framework, no network fetch of any kind (brand mode forbids
CDNs outright: house brand guide §3.1, `brand.toml` `rules.no_remote_assets = true`).

## Users

Primary: **RWA issuers, tokenization platforms, asset managers, and their risk and product
leads.** Finance-literate and technical-adjacent; not DeFi-native. They know collateral,
NAV, strike, maturity, redemption windows, covered calls. They do **not** know what a
liquidation cascade feels like from inside, and terms like *looping*, *MEV*,
*sub-transaction privacy* and *DAML* must be explained if used.

Secondary: **chain-ecosystem BD people who make the introduction.** Their job on this
artifact is retellability — they must be able to repeat the mechanism accurately to a risk
lead who was not in the room.

Two reading situations, both real:

1. **Presented once** — ~10 minutes spoken, a small two-way room that will interrupt.
2. **Forwarded ten times** — read alone, without a narrator, often on the first pass
   without sound (for the film). Every headline claim therefore has to be a complete
   sentence that stands by itself.

## Product Purpose

Medici (AAA Flowers S.A., Panama, operating as Medici) is a **collateral-splitting
primitive for tokenized real-world assets**. A tokenized RWA position — an MMF share, a
tokenized treasury, a bond, a fund unit — is split into two claims that always sum back to
the collateral:

- **P**, the protected leg: full collateral value at or below strike; no margin call, no
  forced sale; capped upside; a computable decline above strike (P = S/x). An
  options-income product, not a yield product.
- **N**, the amplified leg: everything above strike.

Success for these artifacts is educational, not commercial: the audience leaves able to
(1) say what Medici is in one sentence, (2) say why a tokenized-asset holder or issuer
cares, and (3) redraw the P/N split as one diagram. The ask is a conversation, never
capital.

## Positioning

`P + N ≡ collateral` is a **closed-form invariant**, so forced liquidation is
mathematically impossible: there is no liquidation threshold in the payoff function
because there is no under-collateralized state for one to trigger on. That is the claim a
neighbouring lending protocol cannot truthfully copy — every one of them manages a
threshold; this one deletes it. Supporting, and also uncopyable in combination:

- The oracle is read **once, lazily, at settlement** — no live feed to manipulate
  mid-position.
- Split, roll and settlement execute as **single atomic transactions**.
- Positions are **stakeholder-scoped** (sub-transaction privacy) on Canton — the #1 RWA
  network, where the collateral already lives. No gas, no MEV, no mempool.

## Operating Context

The artifacts are a **product pitch / explainer** pair, rendered three times over three
independent messaging contracts:

| Contract | Deck | Film |
|---|---|---|
| `staging` | 14 slots (d1–d14) | 9 scenes, 120s |
| `presentation-writing` | 14 slots (1–14) | 8 scenes, 132s |
| `pitch-deck-mastery` | 13 slots + 1 appendix (A1) | 8 scenes, 143s |

Deck: 1280×720 fixed stage, keyboard/click navigation, prints one slide per page.
Film: 1920×1080 stage, auto-plays with per-scene durations equal to the contract's
`vo_seconds`, screen-recorded by a human afterwards. No audio, no video, no TTS — the
narration lives in `SCRIPT.md` and is read by a person.

The messaging contracts are **consumed verbatim**: slot order is fixed, headline claims are
fixed, no facts may be added. Rephrasing for line breaks is the only licence.

## Capabilities and Constraints

- **Every figure on screen traces to a source file.** No invented numbers, no TAM, no
  projection, no forecast. The corpus is `source/medici/`.
- Roadmap and market figures are **as-of their source date** (Medici decks July 2026,
  RedStone landscape March 2026) and must be marked as such on the slide that carries them.
- Where the two source decks disagree (54 templates / ~5,700 LOC vs 36 / ~5,100; ~2,900
  vs 2,600 lines of regulatory analysis), the contracts take `canton-pitch-deck.md` per
  the brief's stated source priority. Neither figure is load-bearing.
- Both source decks' capital asks are **out of scope** and appear nowhere.
- Text legibility floors: deck body ≥ 18px at 1280×720; explainer text ≥ 28px at
  1920×1080; body contrast ≥ 4.5:1.
- Motion in the film must **carry meaning** — the P/N split, the payoff at maturity, the
  refused liquidation. Quiet scenes stay quiet; decoration-only animation is a defect.

## Brand Commitments

**Binding, non-negotiable, and they outrank every default this tool holds** (house brand
guide `source/brand/house-brand-guide.md` §2/§3/§9/§10; machine contract
`skills/deck-author/brands/medici/brand.toml`):

- **True black `#000000` canvas**, `#0A0A0A` surfaces, `#1A1A1A` hairlines. External
  artifact class.
- **Electric Blue `#3366FF`** is the one frequent accent, and it is budgeted: **≤2 visible
  accent uses per slide**. Gold `#D4A843` appears only inside the mark. Green `#00CC66`,
  red `#FF4444`, amber `#FFCC00` are functional only, never decorative.
- **IBM Plex Sans + IBM Plex Mono, self-hosted woff2, never a CDN.** One family does all
  text; hierarchy is weight and size, never a serif/sans split. Headings sentence case,
  never all-caps display. `ipx-sans.woff2` is a variable font and must be declared
  `font-weight: 100 700`; the mono files are static 400 and 500 instances.
- **Footer `Medici — Proprietary & Confidential` on every slide and every frame**, set at
  11px `#666666` — deprioritized, never hidden. It is the authoritative artifact-class
  marker.
- **No gradients, no gradient text.** Depth comes from border contrast, never from shadow.
- **Motion is minimal, functional, fast**: 150ms ease-out, 200ms ease-in-out; no springs,
  no bounce, no overshoot; `prefers-reduced-motion` disables all of it.
- The mark is the plate-stripped inline `<symbol>` library in
  `brands/medici/deck-skeleton-external.html` (`#assay-mark`, `#oct-line`, `#oct`). The raw
  brand SVGs carry a baked near-black plate and must never go on a slide.

## Evidence on Hand

Real, and the only permissible material:

- `source/medici/canton-pitch-deck.md` — mechanism, payoff math, why-Canton, comparison
  against Aave/Maker/Compound. Highest priority.
- `source/medici/asset-manager-pitch-deck.md` — buyer framing, the 9-year backtest.
- `source/medici/rwa-standards-canton.md`, `source/medici/rwa-redstone-2026.md` — RWA
  landscape, token standards, oracle and lending context.
- `source/medici/authorization-pitch-deck.md` — authorization/reconciliation, background.

Absences that must not be papered over, and that the contracts deliberately put on screen:
**no mainnet deployment, no real collateral, no live users, no third-party audit, no
revenue.** The backtest is third-party (Hypercall, Deribit) and **ETH-only** — never
presented as a forecast for RWA collateral. The regulatory analysis is not counsel-reviewed.
There is no photography, no product screenshot, and no customer logo in the corpus; nothing
of that kind may be invented to fill a composition.

## Product Principles

1. **The invariant is the product.** Every artifact's centre of gravity is `P + N ≡
   collateral`; everything else is the approach to it or the consequence of it.
2. **State the cost before the ask.** P is short a call above the strike, −1.25%/yr net
   drift over the backtest, and nothing is on mainnet. The audience distrusts a
   comparison the presenter wins every row of; the volunteered limit is what buys belief.
3. **Arithmetic, not adjectives.** "Cannot be liquidated" is a theorem to be shown, not a
   promise to be asserted. Where a claim can be drawn as a payoff, draw it.
4. **Retellability outranks completeness.** One mechanism, arriving once, in the middle,
   redrawable on a napkin the next day.
5. **Name the provenance of every number, on the slide.** Source and as-of date travel
   with the figure, because this audience distrusts a figure whose provenance is not named.

## Accessibility & Inclusion

- Body and label contrast ≥ 4.5:1 against the true-black canvas — which is what rules
  `#666666` out of body copy and confines it to the 11px legal-register footer, exactly
  as the brand guide specifies.
- Full keyboard navigation on the deck (←/→/Home/End) and on the film (Space, →).
- `prefers-reduced-motion: reduce` disables every transition and every scene animation;
  the film still advances and every scene's end state remains legible as a still frame.
- No colour-only encoding: the P and N legs are distinguished by label and position, with
  colour as reinforcement only.
