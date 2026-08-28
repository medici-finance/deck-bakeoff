# NOTES — pitch-deck-mastery contender

## 1. Time to artifact

| Phase | Elapsed |
|---|---|
| Read brief, skill (SKILL.md + README + references index), full Medici corpus, brand §0/§8, staging contract + motion-roles | 18:25 → 18:29 (~4 min) |
| Framework mapping, stage call, slot design, bold-moment placement, motion allocation | 18:29 → 18:33 (~4 min) |
| `pitch.md` written, VO timing measured and re-cut to fit the 150 s cap | 18:33 → 18:34 |
| `messaging.md`, `staging.yaml` (YAML-validated), `NOTES.md` | 18:34 → 18:37 |
| **Total** | **~12 minutes**, single pass, no rework of the argument |

The corpus is unusually good input: two of the five source files are already decks with slide
numbers, so citation was cheap and the framework mapping had something to map onto. Most of the
elapsed time went to the two genuinely hard calls — what replaces Market Size and Financials, and
where the bold moment sits.

## 2. Where the framework assumed a fundraise, and what I did

`pitch-deck-mastery` is fundraise-native throughout: its description triggers on "investor
presentations, fundraising decks, demo day slides"; its stage axis is pre-seed → Series B+; its
metrics tables are MRR/NDR/CAC/LTV; and its research loop tells Claude to `web_fetch` example decks
from ten investor-facing resources. Nine distinct fundraise assumptions had to be adapted. Every one
is logged; none was silently dropped.

| # | Fundraise assumption | Where it lives in the skill | Adaptation |
|---|---|---|---|
| 1 | **The whole genre is a raise** | Skill description; slide 12 "Ask: raise amount, terms, next steps" | Reframed as a product pitch. The Ask slot survives with the same *function* — a specific, low-friction next commitment — but the ask is "bring one position and a strike and we will model the split", which is the sales-proposal move, not the raise move. Slot 13 states explicitly what we are **not** asking for (capital, custody, commitment), because a prospect reading a deck that looks like a raise assumes they are about to be asked for money. |
| 2 | **Stage routing** (pre-seed/seed/A/B+) | "Stage-Specific Adjustments" table; "Identify the stage" is step 1 of the research loop | There is no round, so I mapped *company* stage instead: pre-revenue, pre-audit, pre-mainnet, working MVP, 9-year backtest → the seed row. I then took the seed row's guidance (10-12 slides, emphasise Product/Traction, minimise financials) and re-read it for a buyer: emphasise Mechanism and Evidence, cut financials entirely. Landed at 13 slides. |
| 3 | **Market Size (TAM/SAM/SOM)** is a must-pass | Slide 5; must-pass checklist "Market size with credible sourcing" | **Replaced, same slot index.** A prospect does not buy on the vendor's TAM — and the corpus contains no TAM for Medici, so asserting one would have broken the brief's "do not invent numbers" rule outright. The slot now answers the question the prospect actually has: where is the collateral and where is the borrow demand, sourced bottom-up ($344B on Canton; $840M+ RWA deposits in DeFi lending; Aave Horizon $423.5M / $106M borrowed). The skill's own rule that "bottom-up > top-down" is the licence for this. |
| 4 | **Financials / use of funds** | Slide 11 | **Replaced, same slot index** — with the risk register. There are no projections in the corpus, no round to allocate, and the person who kills this deal is a risk lead, not a CFO. The slot keeps the original's spirit: it is the slide where you show your numbers can be interrogated. |
| 5 | **Traction = up-and-to-the-right** | Slide 7; strength signal "Traction chart showing growth trajectory" | **Re-purposed.** There is no revenue, no user, no mainnet. The slot became "what is built, and the five things that do not exist". Fabricating a curve would have failed the skill's own common-mistake check ("no vanity metrics without context"), so the honest version scores better against the skill than a compliant one would have. |
| 6 | **Team answers "can you execute over 5 years"** | Slide 10 | Folded into the close as counterparty diligence, with depth pushed to the appendix. An investor buys the team; a prospect at first contact buys the mechanism and checks the team afterwards. Keeping a full team slide in a 10-minute product pitch would have failed the dead-slot test — nothing turns on it at this stage. |
| 7 | **Competition = "why will you win"** | Slide 9 | Reframed as category placement. The claim is "different risk category", not "we beat Aave" — and Aave Horizon is named as a working alternative with real volume, because the honest answer to "what happens if we do nothing" is "you use Horizon plus a lawyer, and that works today". The skill's 2x2 rule survives intact; the axes are liquidation-pathway × permissioned. |
| 8 | **Business model = how you make money** | Slide 8 | Same content, flipped to the buyer's side: what the structure costs *them*. Placed adjacent to the risk slot because the roll spread is already inside the −1.25%/yr drift number, and separating them would let the room double-count. |
| 9 | **Research by fetching investor decks** | "How to Research for a User", `references/resources.md` (YC, Slidebean, Failory, OpenVC …) | Not executed. Every one of the ten resources is fundraise-specific, none would inform a Canton RWA product pitch, and the bake-off is a closed-corpus exercise. The checklist patterns those resources produced are already distilled in SKILL.md, and those I applied in full. Logged rather than skipped silently. |

**What the framework got right for a non-fundraise, unchanged:** the Problem → Solution arc; "the
headline is the takeaway, not a label"; the 10-word bullet rule; "quantify everything"; the
"so what?" test; credibility stacking; and — most valuable here — the entire Common Mistakes list,
which is genre-neutral and did real work (it is why there is no traction chart and no TAM).

**One structural gap the framework has for this genre**: it has no slot for *who is on each side of
a two-sided instrument*. An investor deck does not need one; a product pitch for an instrument that
requires two buyers absolutely does, or the room leaves asking "who takes the other leg". Added as
slot 6.

## 3. Questions the skill would have asked a human — answered from the corpus

The skill's research loop opens with "Identify the stage" and assumes a live founder to interview.
No human was available, so each question was answered from the corpus with provenance recorded.

| # | Question the skill asks | Answer | Provenance |
|---|---|---|---|
| 1 | What stage are you at? | Pre-revenue, pre-audit, pre-mainnet; working MVP dev-deployed on Canton; 9-year third-party backtest. Seed-equivalent. | `canton-pitch-deck.md` Slide 9; `asset-manager-pitch-deck.md` Slide 12 |
| 2 | How much are you raising, and against what use of funds? | N/A by ruling — the brief sets the genre as a product pitch. For the record, the corpus asks are Canton Foundation funding for audits/legal/opex, and $5–15M strategic plus a $10–25M pilot scaling to $100M+. **No part of either appears in any slot.** | `canton-pitch-deck.md` Slide 11; `asset-manager-pitch-deck.md` Slide 13 |
| 3 | What is your traction? | None of the kind the skill means. 54 DAML templates, 12 agents (6 core live), React frontend against dev cluster, closed-form proofs, 9-year backtest. No mainnet, no collateral, no users, no audit, no revenue. | `canton-pitch-deck.md` Slide 9 |
| 4 | What is your TAM/SAM/SOM? | Not in the corpus, and not derivable without inventing a number. Available sourced anchors: $344B represented on Canton; $840M+ RWA deposits in DeFi lending; Morpho $620M+; Aave Horizon $423.5M; tokenized treasuries $12.9B (rwa.xyz, Jul 2026); RedStone forecast $50–60B for 2026. Decision: no sizing slide; slot 8 states position, not size. | `canton-pitch-deck.md` Slide 4; `rwa-redstone-2026.md` Part 1 (a), Part 2; `asset-manager-pitch-deck.md` Slide 14 |
| 5 | Who is on the team, and why them? | Ian (technical lead, 30+ years platforms, ASF veteran, named inventor on blockchain patents); Co-founder (RWA tokenization, Canton/DAML, institutional partnerships); Co-founder (DeFi growth). Entity: AAA Flowers S.A. (Panama), moving to a purpose-built SPV for institutional deployment. | `canton-pitch-deck.md` Slide 10; `asset-manager-pitch-deck.md` Slide 11 |
| 6 | Who are the competitors, and on which two axes? | Aave, Compound, Maker, perp DEXs (permissionless, liquidating); Aave Horizon (permissioned, institutional, liquidating); Morpho with curators; Figure/Provenance as an own-chain precedent; Ethena, Ondo, Morpho/Gauntlet and Pendle listed as adjacent. Axes chosen: liquidation pathway × permissioned. | `asset-manager-pitch-deck.md` Slide 8 and appendix; `rwa-redstone-2026.md` Part 2 |
| 7 | Which underlying leads? | **The corpus contradicts itself and I did not paper over it.** The Canton deck's RWA use case is tokenized fund shares (USTB, BENJI); the RedStone analysis says T-bills are a poor underlying — near-zero volatility, and Morpho T-bill deposits fell 92% while gold grew 7x. Both are true: the Protected leg works on any collateral, the Amplified leg needs volatility to price. Resolution: the brief's MMF/treasury framing leads, with the volatility caveat stated on slot 6 and answered head-on as objection O3 in `messaging.md`. | `canton-pitch-deck.md` Slides 6, 7; `rwa-redstone-2026.md` Part 2 |
| 8 | What is the deck's one-liner? | Written, not found — the corpus has three competing taglines ("No forced liquidation. Ever.", "Lending against BTC — with no liquidation price.", "Index exposure without liquidation risk."). None fits an RWA product pitch: the first is a slogan without a subject, the second is BTC-specific, the third is the brand's public tagline for a different surface. The repeatable line in `messaging.md` §1 is new, built from the mechanism. | `canton-pitch-deck.md` Slide 1; `asset-manager-pitch-deck.md` Slide 1; `house-brand-guide.md` §8.3 |

**Recorded assumptions** (things I decided rather than asked, per the skill's "quantify everything"
and the brief's "do not invent numbers"): contract count taken as 54 / ~5,700 LOC from the priority
source over the asset-manager deck's 36 / ~5,100; regulatory analysis taken as ~2,900 lines over
2,600; all roadmap dates carried as-of July 2026 and labelled on-slide.

## 4. Friction

1. **The skill has no bold-moment concept.** The brief's `staging.yaml` requires exactly one, and
   `pitch-deck-mastery` never allocates emphasis — its closest analogue is one line in the Product
   slide guide, *"highlight the aha moment — what makes users stay"*. I bridged to that: the aha
   moment is the invariant, so the bold moment is slot 5. The bridge is defensible but it is mine,
   not the skill's.
2. **The skill has no motion vocabulary at all.** It is a slide skill; the explainer video is
   entirely outside its scope. The scene treatment in `pitch.md` §4 uses its narrative rules
   (problem → solution, credibility stacking, end with momentum) as the spine and takes only the
   closed `motion_role` vocabulary from the transport contract, as the brief permits. The skill
   contributed the *argument* of the film and nothing about its kinetics.
3. **The 10-word bullet rule fights a math product.** "Above strike, P declines continuously as
   P = S/x — fully computable, no cliff" is 12 words and cannot be usefully shortened. I split such
   points across two bullets rather than truncate the math, which the skill's "if you need a second
   point, make a second slide" rule tolerates but does not quite anticipate.
4. **Two source-number discrepancies** (54 vs 36 templates; 2,900 vs 2,600 lines of regulatory
   analysis) had to be adjudicated on the brief's priority ordering rather than on evidence. Both
   are recorded in `staging.yaml` `assumptions` and in `messaging.md` §5 so a design consumer does
   not "fix" one to match the other.
5. **`arrest` at the energy ceiling is a genuine tension.** The motion-roles reference says the bold
   moment holds the highest energy (R3), while the `arrest` role is by definition low-amplitude. The
   Medici bold moment is *an absence* — a gesture that starts and refuses — so `arrest` is the only
   honest role for it. Resolved as an ordering rather than an absolute: scene 5 sits at 4.0, not
   5.0, with everything else capped strictly below. Flagged in `staging.yaml` so no design contender
   reads 4.0 as licence to make it the busiest scene; it is the most charged and the second stillest.

## 5. What the skill could not express

- **A risk register.** The framework has no slot for "here is the risk you are taking, itemised, and
  here are the two we have not solved". For an investor that lives in the appendix; for a risk lead
  it is the slide that decides the meeting. I built slot 11 without the skill's help.
- **Honest disclosure as a persuasion beat.** The skill's checklist rewards traction and named
  logos and has no vocabulary for "what does not exist yet" being an asset. In this corpus the
  strongest available move is that both source decks publish their own gaps; the deck (slot 10) and
  the film (scene 7, `divest`) both use it, and the skill would score that slide as a weakness.
- **The two-sided-instrument problem.** No slot for "who buys the other leg", which for this product
  is the second question in the room.
- **Terminology governance.** The skill is silent on house language; the brand guide's canon
  (Protected/Amplified, never "stable"/"leverage"; "can't be liquidated", never
  "liquidation-resistant") came entirely from `house-brand-guide.md` §8.2 and is enforced across all
  three deliverables. Note that this required overriding the corpus itself, which uses "stable-ish"
  and "leveraged upside" in `canton-pitch-deck.md` Slide 3.
- **Anything about the medium.** No guidance on decks that will be read alone after being presented
  (the table/hall distinction), which is the real condition here — this deck will be forwarded. I
  handled it by keeping every slide self-sufficient with sources attached, and declared the lane as
  `mixed(table)` in the contract.
