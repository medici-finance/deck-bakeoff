# Shared brief — "Medici for RWA tokens" product pitch

Ruled by Ian, 2026-08-27. Every contender renders THIS brief. Nothing leaves this
directory (no PRs, no publication); source repos are read-only inputs.

## The product story

**Medici** (AAA Flowers S.A., operating as Medici) is a collateral-splitting
primitive for tokenized real-world assets. A tokenized RWA position (MMF share,
tokenized treasury, bond, fund unit, …) is split into two claims that always
sum back to the collateral:

- **P** — the stable-ish leg: no margin calls, no forced sale; capped upside,
  computable decline above strike (P = S/x). An options-income product, not a
  yield product.
- **N** — the leveraged-upside leg: receives everything above strike.

`P + N ≡ collateral` is a closed-form invariant, so **forced liquidation is
mathematically impossible** — no liquidation threshold exists in the payoff
function. Oracles are read lazily at settlement only. Settlement/rolls are
atomic. Positions are stakeholder-scoped (sub-transaction privacy on Canton,
the #1 RWA network — where the collateral already lives).

Source of truth (in priority order): `source/medici/canton-pitch-deck.md`
(mechanism, math, why-Canton, comparison vs Aave/Maker/Compound),
`source/medici/asset-manager-pitch-deck.md` (buyer framing),
`source/medici/rwa-standards-canton.md` + `rwa-redstone-2026.md` (RWA
landscape, token standards, oracle context), `source/medici/authorization-pitch-deck.md`
(how authorization/reconciliation works on Canton — background only).
**Do not invent numbers.** Every figure on a slide must trace to a source file.
Statements of roadmap/timing are as-of the source's date; mark them as such.

## Audience + the three educational goals

Audience: RWA issuers, tokenization platforms, asset managers and their
risk/product leads, plus the chain-ecosystem BD people who introduce them.
Technical-adjacent, finance-literate, not DeFi-native. They must leave knowing:

1. **What Medici is** — one sentence they can repeat.
2. **Its value prop in the RWA space** — why a tokenized-asset holder/issuer
   cares (no forced liquidation on institutional collateral; income without
   selling; privacy; atomic settlement; no gas/MEV tax).
3. **How the basic mechanism works** — the P/N split, the invariant, what
   happens at maturity above/below strike. One diagram they could redraw.

Genre: **product pitch / explainer** (educate first; the ask is a conversation,
not funding). Deck: 10–14 slides, ~10 minutes spoken. Explainer video: 90–150 s.

## Two brand modes (every design contender renders BOTH)

- **`brand`** — the pinned house brand: `source/brand/house-brand-guide.md`
  (§2 colour, §3 type, §9 motion, §10 surfaces). Dark external surface
  (#000/#0A0A0A), Electric Blue #3366FF accent (≤2 uses per slide), IBM Plex
  Sans/Mono self-hosted (fonts in `skills/deck-author/brands/medici/fonts/`),
  every slide footer `Medici — Proprietary & Confidential`. Machine contract:
  `skills/deck-author/brands/medici/brand.toml`; linter
  `skills/deck-author/tools/check_deck.py`.
- **`free`** — NO brand limits. The tool's own aesthetic judgment, any palette,
  any type, any motion. Only the footer string and the factual content are
  fixed. This is the mode that shows what the tool can actually do.

## Two media (every design contender renders BOTH, per brand mode)

- **deck** — `index.html`, self-contained, 1280×720 (16:9) fixed stage,
  keyboard-navigable, prints to PDF one slide per page (`@media print`),
  no remote assets except Google Fonts in `free` mode.
- **explainer** — `explainer.html` + `SCRIPT.md`: a self-contained animated
  HTML explainer meant to be screen-recorded into a video. Scenes advance on a
  timeline (auto-play with a `?scene=N` / keyboard override), each scene
  timed to the narration in SCRIPT.md (SCRIPT.md carries per-scene VO text +
  duration in seconds). **No TTS, no mp4, no external media** — Ian renders.
  Motion must carry meaning (the P/N split, the payoff at maturity); no
  decoration-only animation.

## Messaging layer

Three messaging contenders each produce `messaging/<skill>/` containing their
native artifact(s) AND a normalized `staging.yaml` (schema:
`skills/messaging/staging/SKILL.md` — genre, audience, slots with function +
headline claim, one bold moment, deck lane + video lane with per-scene VO
budget). Design contenders consume `staging.yaml` verbatim: **never reorder
slots or rewrite a headline claim**; a slot you cannot render is logged in
NOTES.md, not silently dropped.

## Layout

```
tracks/<design>/<brand|free>/<messaging>/deck/index.html
tracks/<design>/<brand|free>/<messaging>/explainer/{explainer.html,SCRIPT.md}
tracks/<design>/NOTES.md          — time-to-artifact, friction, overrides, what the tool refused
messaging/<messaging>/{<native artifacts>,staging.yaml,NOTES.md}
```

design ∈ {canvas-design, algorithmic-art, impeccable, impeccable-polish, visual-explainer, html-ppt}
messaging ∈ {staging, presentation-writing, pitch-deck-mastery}
