# SCRIPT.md — Medici explainer · `presentation-writing` · impeccable / free

**Runtime 132s (2:12) · 8 scenes · 1920×1080 · no audio, no TTS, no video.**
Screen-record `explainer/explainer.html`; it auto-plays on load. `?scene=N` jumps to a scene,
Space / → advance, ← steps back, `P` pauses. `window.__player` exposes `{scene, t, total, seek(n)}`.

VO column is **verbatim** from `messaging/presentation-writing/staging.yaml`; nothing was reworded or added.
Motion roles, energies and peaks are the contract's, not the designer's.

| # | scene | start | dur | on-screen text | VO (verbatim) | what moves |
|---|---|---|---|---|---|---|
| 1 | `1` · hold | 0:00 | 12s | Real collateral, on a ledger, that nobody can sell in one transaction<br>A tokenized fund share. A gold bar with a ticker. | A tokenized fund share. A gold bar with a ticker. Real collateral, on a ledger — and none of it can be sold inside a single transaction. | The frame is given, not developed. One gold-leaf plate holds at centre with a slow luminance breath; the claim settles once. The piece has one loud moment and this is not it. |
| 2 | `2` · strain | 0:12 | 18s | Every venue prices that loan against a liquidation threshold anyway<br>RedStone calls those fundamental design constraints, not edge cases. | Every venue that lends against it prices the loan against a liquidation threshold anyway. So the desks patch the gap by hand — signed liquidation agreements with the issuer, curator-run de-leverage frameworks, NAV instead of a market price. RedStone calls those fundamental design constraints, not edge cases. | Comfort becomes load. The gold plate squashes to 86% and skews from 3.6s. Three patch strips drop in over the threshold at 4.3s, 7.2s and 10.1s, each offset lower and further right than the last — one is prudence, three is a workaround. The threshold line itself never moves. |
| 3 | `3` · accumulate · **peak** | 0:30 | 16s | When the pathway runs, it runs at zero<br>Black Thursday: $8 million of MakerDAO collateral, auctioned for $0. | And when the pathway actually runs, it runs at the worst possible price. On Black Thursday, MakerDAO collateral was auctioned for zero dollars. Eight million dollars of it. One forced sale sets off the next. | One value — forced sales — grows continuously across the scene rather than happening once. Nine vermilion columns rise in sequence from 1.9s, each taller than the last and each entering as the previous finishes: a chain that feeds itself, not a single event repeated. |
| 4 | `4` · hold | 0:46 | 12s | Medici asks a different question<br>Not how do we liquidate this safely — what if there were nothing to liquidate? | Medici asks a different question. Not how do we liquidate this safely — what if there were nothing to liquidate? Split the collateral instead. | Deliberately still and deliberately empty: the contract gives this scene no figures at all. The claim settles on the bare ruled field and nothing else happens for twelve seconds. This is the quiet scenes 3 and 6 are paid for with. |
| 5 | `5` · assemble | 0:58 | 20s | One position becomes two claims that always add back to it<br>Closed form, at every price. The oracle isn’t even read until settlement. | One position becomes two claims. P is capped and income-bearing. N takes everything above the strike. P plus N always equals the collateral — closed form, at every price, enforced by the contract that records the split. The oracle isn’t even read until settlement. | One object becomes two and nothing leaves the system. The source plate contracts at 2.8s as P and N slide out of it; the payoff assembles beneath in narration order — axes 2.0s, strike 3.2s, gold P 4.4s, vermilion N 8.8s — and the verdigris balance rule foots across at 13.2s. Every part that arrives stays on screen. |
| 6 | `6` · rupture · **peak** | 1:18 | 24s | The liquidation line has nowhere to sit<br>At or below the strike: P 1.00, N 0.00. Above it: P = S/x, N = 1 − S/x. | At maturity there are two cases. At or below the strike, P is worth the whole collateral and N is worth nothing. Above it, P is the strike over the price; N is the rest. Now draw the liquidation line every other venue needs. There is nowhere on this axis to put it — no price under-collateralizes the vault. | The two cases assemble first (P 5.3s, N 10.6s, verdigris balance rule 15.8s). Then the break: at 15.8s a vermilion threshold is introduced and tries three positions on the axis — right, far left, right again — and at 23s fades to 18% without ever landing. The threshold is introduced and then cannot be placed; this is the only rupture in the film. |
| 7 | `7` · divest | 1:42 | 17s | P is short a call, and the decline is the income<br>Nine years of backtest: net drift −1.25%/yr. Never a cliff. | That is not free. P is short a call above the strike, so P’s value falls continuously as the asset rallies — nine years of backtest put the net drift at minus one and a quarter percent a year. Never a cliff. | The film is turned against its own argument and motion is subtractive only. The N region leaves at 3.7s, the grid at 7.5s, until only P’s continuous decline remains under the balance rule; beside it four unbuilt claims are struck out one at a time from 5.1s. This is also scene 6’s payment. |
| 8 | `8` · cadence | 1:59 | 13s | Bring us the thing you can’t sell in a hurry<br>There is no liquidation price. The math doesn’t permit it. On Canton, where your collateral already lives. | So bring us the thing you can’t sell in a hurry. There is no liquidation price. The math doesn’t permit it. Medici — on Canton, where your collateral already lives. | One gesture, then stop. The asset from scene 1 returns and opens into P and N at 1.8s, the verdigris tether reads at 6.0s, and the frame holds still to the end — the same asset, now split, still held. |

---

## Per-scene detail

### 1. `1` — hold, energy 1

- **In / out:** 0:00 → 0:12 (12s)
- **On screen:** Real collateral, on a ledger, that nobody can sell in one transaction
- **Second line:** A tokenized fund share. A gold bar with a ticker.
- **VO (verbatim):** A tokenized fund share. A gold bar with a ticker. Real collateral, on a ledger — and none of it can be sold inside a single transaction.
- **What moves:** The frame is given, not developed. One gold-leaf plate holds at centre with a slow luminance breath; the claim settles once. The piece has one loud moment and this is not it.
- **Source:** rwa-redstone-2026.md, Part 2 — “Vault standards”

### 2. `2` — strain, energy 3

- **In / out:** 0:12 → 0:30 (18s)
- **On screen:** Every venue prices that loan against a liquidation threshold anyway
- **Second line:** RedStone calls those fundamental design constraints, not edge cases.
- **VO (verbatim):** Every venue that lends against it prices the loan against a liquidation threshold anyway. So the desks patch the gap by hand — signed liquidation agreements with the issuer, curator-run de-leverage frameworks, NAV instead of a market price. RedStone calls those fundamental design constraints, not edge cases.
- **What moves:** Comfort becomes load. The gold plate squashes to 86% and skews from 3.6s. Three patch strips drop in over the threshold at 4.3s, 7.2s and 10.1s, each offset lower and further right than the last — one is prudence, three is a workaround. The threshold line itself never moves.
- **Source:** rwa-redstone-2026.md, Part 2 — “Liquidation mechanics and risk frameworks”

### 3. `3` — accumulate, energy 3.5, **peak**

- **In / out:** 0:30 → 0:46 (16s)
- **On screen:** When the pathway runs, it runs at zero
- **Second line:** Black Thursday: $8 million of MakerDAO collateral, auctioned for $0.
- **VO (verbatim):** And when the pathway actually runs, it runs at the worst possible price. On Black Thursday, MakerDAO collateral was auctioned for zero dollars. Eight million dollars of it. One forced sale sets off the next.
- **What moves:** One value — forced sales — grows continuously across the scene rather than happening once. Nine vermilion columns rise in sequence from 1.9s, each taller than the last and each entering as the previous finishes: a chain that feeds itself, not a single event repeated.
- **Source:** canton-pitch-deck.md Slide 2

### 4. `4` — hold, energy 1

- **In / out:** 0:46 → 0:58 (12s)
- **On screen:** Medici asks a different question
- **Second line:** Not how do we liquidate this safely — what if there were nothing to liquidate?
- **VO (verbatim):** Medici asks a different question. Not how do we liquidate this safely — what if there were nothing to liquidate? Split the collateral instead.
- **What moves:** Deliberately still and deliberately empty: the contract gives this scene no figures at all. The claim settles on the bare ruled field and nothing else happens for twelve seconds. This is the quiet scenes 3 and 6 are paid for with.
- **Source:** canton-pitch-deck.md Slide 3

### 5. `5` — assemble, energy 3

- **In / out:** 0:58 → 1:18 (20s)
- **On screen:** One position becomes two claims that always add back to it
- **Second line:** Closed form, at every price. The oracle isn’t even read until settlement.
- **VO (verbatim):** One position becomes two claims. P is capped and income-bearing. N takes everything above the strike. P plus N always equals the collateral — closed form, at every price, enforced by the contract that records the split. The oracle isn’t even read until settlement.
- **What moves:** One object becomes two and nothing leaves the system. The source plate contracts at 2.8s as P and N slide out of it; the payoff assembles beneath in narration order — axes 2.0s, strike 3.2s, gold P 4.4s, vermilion N 8.8s — and the verdigris balance rule foots across at 13.2s. Every part that arrives stays on screen.
- **Source:** canton-pitch-deck.md Slides 3, 5

### 6. `6` — rupture, energy 5, **peak**

- **In / out:** 1:18 → 1:42 (24s)
- **On screen:** The liquidation line has nowhere to sit
- **Second line:** At or below the strike: P 1.00, N 0.00. Above it: P = S/x, N = 1 − S/x.
- **VO (verbatim):** At maturity there are two cases. At or below the strike, P is worth the whole collateral and N is worth nothing. Above it, P is the strike over the price; N is the rest. Now draw the liquidation line every other venue needs. There is nowhere on this axis to put it — no price under-collateralizes the vault.
- **What moves:** The two cases assemble first (P 5.3s, N 10.6s, verdigris balance rule 15.8s). Then the break: at 15.8s a vermilion threshold is introduced and tries three positions on the axis — right, far left, right again — and at 23s fades to 18% without ever landing. The threshold is introduced and then cannot be placed; this is the only rupture in the film.
- **Source:** canton-pitch-deck.md Slide 5; asset-manager-pitch-deck.md Slide 4

### 7. `7` — divest, energy 1

- **In / out:** 1:42 → 1:59 (17s)
- **On screen:** P is short a call, and the decline is the income
- **Second line:** Nine years of backtest: net drift −1.25%/yr. Never a cliff.
- **VO (verbatim):** That is not free. P is short a call above the strike, so P’s value falls continuously as the asset rallies — nine years of backtest put the net drift at minus one and a quarter percent a year. Never a cliff.
- **What moves:** The film is turned against its own argument and motion is subtractive only. The N region leaves at 3.7s, the grid at 7.5s, until only P’s continuous decline remains under the balance rule; beside it four unbuilt claims are struck out one at a time from 5.1s. This is also scene 6’s payment.
- **Source:** asset-manager-pitch-deck.md Slides 3, 4

### 8. `8` — cadence, energy 2

- **In / out:** 1:59 → 2:12 (13s)
- **On screen:** Bring us the thing you can’t sell in a hurry
- **Second line:** There is no liquidation price. The math doesn’t permit it. On Canton, where your collateral already lives.
- **VO (verbatim):** So bring us the thing you can’t sell in a hurry. There is no liquidation price. The math doesn’t permit it. Medici — on Canton, where your collateral already lives.
- **What moves:** One gesture, then stop. The asset from scene 1 returns and opens into P and N at 1.8s, the verdigris tether reads at 6.0s, and the frame holds still to the end — the same asset, now split, still held.
- **Source:** house-brand-guide.md §8.3; canton-pitch-deck.md Slide 4

---

## Motion ledger

| scene | role | energy | peak | figures rendered |
|---|---|---|---|---|
| 1 | hold | 1 | — | yes |
| 2 | strain | 3 | — | yes |
| 3 | accumulate | 3.5 | yes | yes |
| 4 | hold | 1 | — | none — the contract gives this scene no figures |
| 5 | assemble | 3 | — | yes |
| 6 | rupture | 5 | yes | yes |
| 7 | divest | 1 | — | yes |
| 8 | cadence | 2 | — | yes |

Total runtime: 132s, matching the contract's 132s.
Every slide and scene carries the footer `Medici — Proprietary & Confidential`.
