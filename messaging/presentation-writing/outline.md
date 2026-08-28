# Medici for RWA tokens — narrative outline

**Skill**: `powerpoint-keynote-presentation` (marcusnelson) — narrative architecture, not files.
**Built from**: `source/medici/*` (four decks + two research docs), `source/brand/house-brand-guide.md` §0, §8.
**Date**: 2026-08-27. Roadmap and market figures are as-of their source dates (July 2026 for the
Medici decks; March 2026 for the RedStone report) and are labelled where they appear.

---

## Phase 2 — Audience diagnosis

The skill requires the audience read to be stated and confirmed. No human was available to confirm;
the read below is taken from `BRIEF.md` verbatim where it speaks, and inferred where it does not.
Every inference is logged in `NOTES.md` with its provenance.

| Question | Read |
|---|---|
| Who is in the room | RWA issuers, tokenization platforms, asset managers and their risk/product leads, plus chain-ecosystem BD people who make the introduction (`BRIEF.md`, "Audience") |
| What they already know | Finance-literate, technical-adjacent, **not** DeFi-native. They know NAV, redemption windows, covered calls, counterparty risk. They do not know what a liquidation cascade feels like from the inside |
| What they care about | Not losing an asset they cannot replace; income on positions they already hold; what their risk committee will ask; whether the counterparty is real |
| Power dynamic | Presenting across, not up. Nobody in the room reports to us and nobody in the room writes a cheque today |
| Decision context | Education first. The ask is a conversation, not funding (`BRIEF.md`, "Genre") |

**The read, stated as the skill asks it:** this is a room of people who hold assets that cannot be
sold in a hurry, being told by everyone else in the market that the way to make those assets
productive is to accept a liquidation price. The goal is not to close them. It is to leave them able
to repeat one sentence and redraw one diagram.

---

## Phase 3 — Scaffold selection

**Chosen: The Keynote, with two beats borrowed.**

> "Here's what you think you know. Here's what's actually true. Here's what to do about it."

That is exactly the job. The audience holds no budget decision, so the persuasion is a belief shift,
not an approval. The material has a genuine crack in the conventional wisdom — the RWA lending
market's own report names the liquidation pathway as its hardest unsolved problem and then solves it
with lawyers — and a reframe that answers it.

**Borrowed, deliberately:**

- **The Workshop, components 1–3** → slides 6 and 7. Goal 3 in the brief is that they can redraw the
  diagram. Keynote evidence beats do not teach a mechanism; Workshop components do.
- **The Close, "The Objection"** → slide 8. The room's first question is *where did the risk go*, and
  a keynote that waits for the Q&A to answer it loses the middle of the talk.

**Rejected:**

- **The Pitch** — it front-loads a funding ask this room is not being made. Slide 9 of The Pitch is
  "how much, what it funds." There is no cheque here.
- **The Case** — needs a room with authority to approve, and an options table. Presenting "The
  Options" to people who have not yet accepted there is a problem is backwards.
- **The Report-Out** — no shared history to report a delta against.

**Density: Flexible** (the skill's default, unconfirmed by a human — logged in `NOTES.md`). Slides 5,
7 and 14 carry a single statement. Slides 9 and 10 carry tables because comparison *is* the argument
there. Everything else takes two or three points.

---

# Part 1 — The deck (14 slides, ~10 minutes)

---

## Slide 1: Medici splits tokenized collateral into two claims that always sum back to it

- P — the capped, income-bearing leg. N — the amplified leg that takes everything above the strike.
- One line, spoken as the title card lands: there is no liquidation price, because the math doesn't
  permit it. [`house-brand-guide.md` §8.3]
- Medici (AAA Flowers S.A.) · built for Canton · material as-of July 2026.

**Transition:** Before the mechanism, the reason it exists — and it isn't a crypto reason.

*Speaker note:* Say the definition sentence once, slowly, and do not decorate it. This is the
sentence you want to hear repeated back to you in the follow-up email.

---

## Slide 2: RWA lending is real — against collateral nobody can sell in one transaction

- Morpho's RWA deposits went from roughly zero in early 2025 to **$620M+ by March 2026**, running at
  **87% utilization**. Aave Horizon: **$423.5M** market, **$106M** borrowed, **269 addresses**.
  [`rwa-redstone-2026.md`, Part 2, "Who lends against what"]
- What sits behind those numbers: private-credit receipts, tokenized fund shares, gold. NAV-priced,
  not market-priced. Redemption windows measured in months. [same]
- The report's own sentence: a vault holding tokenized private credit "cannot liquidate its position
  in a single onchain transaction." [same]

**Transition:** So how does a market that lends against unsellable collateral handle a default?

*Speaker note:* Do not sell the numbers as excitement. They are here to establish that this is a
live, institutional market — so the flaw you are about to name is a flaw in something real.

---

## Slide 3: The market's fix for unsellable collateral is paperwork, not math

- Curators — not credit committees — set the LTVs and "manage liquidation pathways" for collateral
  whose quality is "not directly observable onchain." [`rwa-redstone-2026.md`, Part 2, "Liquidation
  mechanics and risk frameworks"]
- The tooling that makes it work: **signed liquidation agreements with the asset issuers**, formal
  de-leverage frameworks, direct lines to the issuer. [same]
- The report's verdict on that: "These are not edge cases but fundamental design constraints." [same]

**Transition:** Paperwork holds until the day the pathway actually runs.

*Speaker note:* This is the slide where the room recognizes their own operating model. Deliver it
straight — it is not a criticism of the curators, it is an observation that they are rebuilding a
workout desk on top of a money market.

---

## Slide 4: When the liquidation pathway runs, it runs at the worst possible price

- Black Thursday, March 2020: MakerDAO collateral auctioned for **$0** — **$8M** of it.
  [`canton-pitch-deck.md` Slide 2; `asset-manager-pitch-deck.md` Slide 2]
- Mango Markets: **$116M** taken through an oracle the protocol had to read in real time.
  [`canton-pitch-deck.md` Slide 2]
- The shape of the risk, not the size of it: fine one block, wiped out the next. A cliff, not a
  slope. [`asset-manager-pitch-deck.md` Slide 2]

**Transition:** Every fix on offer makes the cliff less likely. None of them removes it.

*Speaker note:* Two examples, no more. The point is not that DeFi is dangerous — this room already
believes that. The point is that the failure is mechanical, so it can be engineered away.

---

## Slide 5: Medici deletes the liquidation pathway instead of managing it

> Split the collateral into two claims that always add back to it. Then there is no threshold to
> cross, because there is no under-collateralization condition anywhere in the payoff function.

[`canton-pitch-deck.md` Slide 5; `asset-manager-pitch-deck.md` Slide 4]

**Transition:** That is a strong claim. Here is the whole mechanism — it takes two slides.

*Speaker note:* Single statement, no bullets, and a pause. This is the pivot; if they only carry one
slide out of the room, it should be this one or the next.

---

## Slide 6: One position becomes two claims that always add back to it

- Deposit a tokenized asset, pick a strike. The vault issues **P** (capped, income-bearing) and **N**
  (everything above the strike). [`canton-pitch-deck.md` Slide 3]
- **P + N ≡ collateral** at every price — closed-form, verified as math rather than asserted at
  runtime. [`canton-pitch-deck.md` Slides 3, 5]
- The oracle is read once, at settlement — there is no live feed to manipulate during the position's
  life. [`canton-pitch-deck.md` Slide 3; `asset-manager-pitch-deck.md` Slide 3]

**Transition:** Hold that identity in your head, because the next slide is where it does the work.

*Speaker note:* Keep the vocabulary tight: split, strike, settle, recombine. Introduce each once and
then use it — the room is finance-literate and will resent being taught twice.

---

## Slide 7: At maturity there are two cases, and neither is a margin call  ★ BOLD MOMENT

| At maturity, reference price `x`, strike `S` | P receives | N receives |
|---|---|---|
| `S ≥ x` — price at or below strike | 1.00 (the whole collateral) | 0.00 |
| `S < x` — price above strike | `S/x` | `1 − S/x` |

[`canton-pitch-deck.md` Slide 5; `asset-manager-pitch-deck.md` Slide 4]

- **The bold moment, staged as a thing that happens:** draw the liquidation threshold every other
  venue needs. There is nowhere on the price axis to put it — no `x` leaves the vault worth less than
  the collateral. The line is drawn and then has to be taken away.
- This is the diagram they redraw on a whiteboard.

**Transition:** Nothing is free. Here is what P gives up to get that.

*Speaker note:* Do not rush this. Let the room watch the line fail to land. If someone says "so
where's the catch" out loud, the deck is working and the next slide is your answer.

---

## Slide 8: P is short a call — that decline is what P earns

- Above the strike, P's value falls continuously as `P = S/x`. No floor, no cliff, computable at
  every price. That decline **is** the source of P's income. [`asset-manager-pitch-deck.md` Slide 4]
- The measured cost: **net drift −1.25%/yr**, P ending at **$0.895** on **$1.00**, over a **9-year**
  backtest (Hypercall, Aug 2017–Jun 2026; ETH underlying, Deribit options, Black-Scholes at mid).
  [`asset-manager-pitch-deck.md` Slides 3, 12; `canton-pitch-deck.md` Slide 3]
- Where the cost goes: roll execution, **−1.2%/yr** at 10bps across ~12.2 rolls a year. Best
  sub-period gross theta was **+0.57%/yr** (2021–22) — not the full-period average.
  [`asset-manager-pitch-deck.md` Slide 3]

**Transition:** Which is why the comparison everyone reaches for is the wrong one.

*Speaker note:* Say the negative number out loud before anyone asks for it. This is an options-income
product, not a yield product, and the backtest is ETH-only — say that too. The credibility you buy
here is what carries slides 10 through 12.

---

## Slide 9: This is a different instrument, not a better lending rate

| | RWA money market (Morpho, Aave Horizon) | Medici |
|---|---|---|
| Who takes the price risk | The borrower, until the threshold breaches | The P holder, continuously, above the strike |
| What you are paid for | Supplying liquidity | Selling the upside above the strike |
| Worst case | Forced sale of collateral that has no bid | The asset rallies; P declines, computably |
| What the issuer must sign | A liquidation agreement | Nothing |

[`asset-manager-pitch-deck.md` Slide 8; `rwa-redstone-2026.md`, Part 2]

- Medici does not compete for the safe-yield allocation. It is closer to a covered-call program than
  to a lending desk. [`asset-manager-pitch-deck.md` Slide 8]

**Transition:** So which tokenized assets does this actually suit?

*Speaker note:* The axes are the ones a risk lead would pick, not the ones we win on. Say that. If
you pick the axes, the table reads as a sales table and they stop believing the rest of the deck.

---

## Slide 10: The collateral this fits is the collateral institutions already rotated into

- On Morpho, tokenized T-bill deposits **fell 92%** from their ~$194M October 2025 peak while
  tokenized **gold grew 7x** — gold now 71% of that combined pool.
  [`rwa-redstone-2026.md`, Part 2, "Gold vs T-bills"]
- Gold borrows at a conservative **~40%** collateral ratio — "straightforward non-looped borrowing,"
  which is the demand profile an options split needs. [same]
- What it does not fit, said plainly: private credit is NAV-priced and illiquid; tokenized equities
  are live on Morpho with **under $1K** deposited. An options split needs volatility and a defensible
  settlement price. [`rwa-redstone-2026.md`, Part 2; Part 1 §(b)4]

**Transition:** And the assets themselves are already sitting on one particular ledger.

*Speaker note:* This is where you disqualify your own product for near-zero-vol collateral. Do it —
a tokenized MMF share will not carry a meaningful split, and the treasurer in the room already knows
it. Naming the limit is what makes the gold case credible.

---

## Slide 11: Canton already holds the assets and enforces the privacy institutions require

- **$344B represented, $2T/month in repo.** The collateral is already there — no bridge, no wrapper.
  [`canton-pitch-deck.md` Slide 4]
- Sub-transaction privacy: positions are stakeholder-scoped — visible to counterparties, not the
  market. No gas, no MEV, no mempool. Splits, rolls and settlements are atomic.
  [`canton-pitch-deck.md` Slide 4]
- The honest counter: Canton appears **nowhere** in the RedStone RWA-lending report — every venue
  with live lending volume is Ethereum, an EVM L2, Solana or Provenance. Getting collateral into a
  vault is the open problem, and it is a distribution problem, not a mechanism problem.
  [`rwa-redstone-2026.md`, Part 2, "Survives — the Canton distribution gap"]

**Transition:** Which brings us to what is actually built.

*Speaker note:* Put the distribution gap on the slide, not in the Q&A. This audience includes the BD
people who would close that gap — naming it is how you make them the protagonist.

---

## Slide 12: The mechanism runs today; the audit, mainnet and users do not

- What exists: **54 DAML templates across 9 modules**, a **12-agent** TypeScript fleet behind a Go
  ledger service (**6 core agents live**, 6 in progress), a React frontend end-to-end against a dev
  cluster, closed-form invariant proofs, and a ~2,900-line US regulatory analysis.
  [`canton-pitch-deck.md` Slides 8, 9]
- What does not: mainnet deployment, real collateral, live users, a third-party audit, revenue.
  [`canton-pitch-deck.md` Slide 9]
- As of July 2026 the plan was: audit and legal review Q3 2026, Canton mainnet Q4 2026, compliance
  layer H1 2027, first institutional pilot H2 2027. [`canton-pitch-deck.md` Slide 12]

**Transition:** So the ask is small, and it is not for money.

*Speaker note:* Read the second bullet at the same volume as the first. The room has heard "working
MVP" before; what they have not heard is a founder listing the missing pieces without being asked.

---

## Slide 13: Bring us the asset you can't sell in a hurry

- Name one tokenized position on Canton you would not want force-sold. Gold or a volatile fund unit
  is the fit; a near-zero-vol treasury fund is not. [`rwa-redstone-2026.md`, Part 2]
- We will size the split against it — strike, maturity, and the drift you would be paying, using the
  published −1.25%/yr as the starting number. [`asset-manager-pitch-deck.md` Slide 3]
- Then tell us where the payoff breaks. If P + N holds at every price you can name, the conversation
  becomes a pilot.

**Transition:** One sentence to leave with.

*Speaker note:* This is the whole ask: an asset, a strike, and an attempt to break the payoff. Give
them the third one — a room that is invited to falsify the claim engages harder than a room that is
invited to agree.

---

## Slide 14: No liquidation price. Not a policy — a property of the payoff

> There is no liquidation price — the math doesn't permit it.

[`house-brand-guide.md` §8.3, canonical sentence, reused verbatim]

*Speaker note:* Say the line, stop, and do not add a thank-you. It is the same sentence from slide 1;
the repetition is the point — a claim repeated identically reads as a fact.

---

## Phase 6 — Pressure tests

**The "so what" test.** *Why does this deck exist and what does it ask?* It exists to move an RWA
holder from "liquidation risk is a parameter I negotiate" to "liquidation risk is a design choice I
can decline," and it asks them to name one asset they would not want force-sold. Passes.

**The "drunk test."** Skimmed at 11pm, the reader gets: unsellable collateral → the market patches it
with lawyers → Medici splits the asset in two so there is nothing to seize → it costs ~1.25%/yr →
gold first → not audited yet. Passes.

**The "cut test."** Slide 11 (why Canton) is the weakest — it survives because the collateral's
location is the whole reason this is an RWA pitch and not a crypto pitch, and because the
distribution gap is the honest counterweight. Slide 2 could compress into slide 3, but then the
market's scale arrives as an assertion instead of a number. Everything else collapses the argument if
removed. Passes with one flag.

**The "order test."** Slides 6 and 7 cannot be separated (the mechanism runs in its own order), 8
cannot precede 7 (a cost before the thing it buys), and 4 cannot precede 3 (the cliff only lands once
the paperwork is established as the alternative). Passes.

---

# Part 2 — The explainer video (8 scenes, 132 seconds)

Format note: this skill produces slide outlines. The scene format below is its slide format adapted —
thesis, support, transition — plus the two fields a film needs and a deck does not: spoken VO and a
duration. Narration is budgeted at ~140 wpm; the totals are stated per scene and reconciled at the
end. Motion roles are carried in `staging.yaml`, not here, because they are a transport concern.

---

## Scene 1 (0:00–0:12, 12s): Real collateral, on a ledger, that nobody can sell in one transaction

**VO (26 words):** "A tokenized fund share. A gold bar with a ticker. Real collateral, on a ledger —
and none of it can be sold inside a single transaction."

- Establishes the asset, not the protocol. The viewer's own position is on screen.
- Quiet open, deliberately: the piece has one loud moment and this is not it.

**Transition:** The venues that lend against it behave as though it could be.

---

## Scene 2 (0:12–0:30, 18s): Every venue prices that loan against a liquidation threshold anyway

**VO (46 words):** "Every venue that lends against it prices the loan against a liquidation threshold
anyway. So the desks patch the gap by hand — signed liquidation agreements with the issuer,
curator-run de-leverage frameworks, NAV instead of a market price. RedStone calls those fundamental
design constraints, not edge cases."

- The quote is load-bearing and is the market's own words, not ours.
  [`rwa-redstone-2026.md`, Part 2]

**Transition:** Paperwork holds right up until the pathway runs.

---

## Scene 3 (0:30–0:46, 16s): When the pathway runs, it runs at zero

**VO (35 words):** "And when the pathway actually runs, it runs at the worst possible price. On Black
Thursday, MakerDAO collateral was auctioned for zero dollars. Eight million dollars of it. One forced
sale sets off the next."

- One event, named and dated. [`canton-pitch-deck.md` Slide 2]

**Transition:** Every fix on offer makes that less likely. None removes it.

---

## Scene 4 (0:46–0:58, 12s): Medici asks a different question

**VO (23 words):** "Medici asks a different question. Not how do we liquidate this safely — what if
there were nothing to liquidate? Split the collateral instead."

- The turn. Nothing else happens in this scene; it is the quiet that the next two are paid for with.

**Transition:** Here is the split, in full.

---

## Scene 5 (0:58–1:18, 20s): One position becomes two claims that always add back to it

**VO (43 words):** "One position becomes two claims. P is capped and income-bearing. N takes
everything above the strike. P plus N always equals the collateral — closed form, at every price,
enforced by the contract that records the split. The oracle isn't even read until settlement."

- The vocabulary the viewer must leave with: split, strike, P, N, settle.
  [`canton-pitch-deck.md` Slides 3, 5]

**Transition:** Now watch what that identity does at maturity.

---

## Scene 6 (1:18–1:42, 24s): The liquidation line has nowhere on the axis to sit  ★ BOLD MOMENT

**VO (58 words):** "At maturity there are two cases. At or below the strike, P is worth the whole
collateral and N is worth nothing. Above it, P is the strike over the price; N is the rest. Now draw
the liquidation line every other venue needs. There is nowhere on this axis to put it — no price
under-collateralizes the vault."

- The payoff, both cases, then the threshold drawn and refused. This is the one thing that *happens*
  in the film. [`canton-pitch-deck.md` Slide 5]

**Transition:** That is not free.

---

## Scene 7 (1:42–1:59, 17s): P is short a call, and the decline is the income

**VO (41 words):** "That is not free. P is short a call above the strike, so P's value falls
continuously as the asset rallies — nine years of backtest put the net drift at minus one and a
quarter percent a year. Never a cliff."

- The film gives up its own persuasion here: the cost, with its number and its provenance.
  [`asset-manager-pitch-deck.md` Slides 3, 4]

**Transition:** So the ask is an asset, not a cheque.

---

## Scene 8 (1:59–2:12, 13s): Bring us the thing you can't sell in a hurry

**VO (29 words):** "So bring us the thing you can't sell in a hurry. There is no liquidation price.
The math doesn't permit it. Medici — on Canton, where your collateral already lives."

- Closes the image opened in scene 1: the same asset, now split, still there.
  [`house-brand-guide.md` §8.3]

---

### Video reconciliation

| | |
|---|---|
| Scenes | 8 |
| Runtime | 12 + 18 + 16 + 12 + 20 + 24 + 17 + 13 = **132s** (brief allows 90–150s) |
| VO words | 26 + 46 + 35 + 23 + 43 + 58 + 41 + 29 = **301** |
| Rate | 301 words ÷ 132s × 60 = **~137 wpm** — inside a comfortable narration band |
| Bold moment | Scene 6, at 1:18–1:42 — 59% to 77% of runtime, in the last half, after the mechanism is complete and before the cost |

### Video pressure tests

- **So what:** the viewer leaves able to say "they split the asset in two so there's nothing to
  liquidate." Passes.
- **Cut test:** removing scene 7 (the cost) would make the film shorter and less true. It stays.
  Removing scene 4 would put the turn inside the mechanism scene, which is where films lose people.
  It stays.
- **Order test:** 6 cannot precede 5, 7 cannot precede 6, 3 cannot precede 2. Fixed order. Passes.
