# SCRIPT.md — Medici explainer · `staging` · impeccable / free

**Runtime 120s (2:00) · 9 scenes · 1920×1080 · no audio, no TTS, no video.**
Screen-record `explainer/explainer.html`; it auto-plays on load. `?scene=N` jumps to a scene,
Space / → advance, ← steps back, `P` pauses. `window.__player` exposes `{scene, t, total, seek(n)}`.

VO column is **verbatim** from `messaging/staging/staging.yaml`; nothing was reworded or added.
Motion roles, energies and peaks are the contract's, not the designer's.

| # | scene | start | dur | on-screen text | VO (verbatim) | what moves |
|---|---|---|---|---|---|---|
| 1 | `s1` · hold | 0:00 | 10s | Tokenized assets are on-chain, and mostly sitting still.<br>Treasuries. Fund shares. Gold. | Tokenized treasuries, fund shares, gold: on-chain now, and mostly sitting still. Making one productive means accepting a liquidation price. There is a way that doesn’t. | Nothing develops. One gold-leaf position holds at centre on the ruled field with a slow 9s luminance breath; the claim settles once and stops. The cold open spends no contrast. |
| 2 | `s2` · accumulate | 0:10 | 10s | Every venue that takes that collateral prices a liquidation threshold.<br>Morpho RWA deposits: ~zero in early 2025 → $620M+ by March 2026. | Every venue that lends against these assets prices in a liquidation threshold. On Morpho, tokenized collateral grew from nothing to over $620 million in a year. | Fourteen gold columns grow from the baseline left to right across the scene — the climb is the point, not the end value. At 6.0s a vermilion dashed threshold is laid across the whole field, above every column. |
| 3 | `s3` · strain | 0:20 | 10s | This collateral cannot be sold in a single transaction.<br>NAV pricing · monthly redemption windows · so the market signs liquidation agreements with issuers. | But this collateral doesn’t behave: NAV pricing, monthly redemption windows, no sale in a single transaction. So the market signs liquidation agreements with issuers. | A vermilion load arrow descends from 1.8s; the stack of ruled lines compresses to 72% and skews under it. A sell arrow runs at the redemption window twice (4.4s, 6.8s) and is turned back both times. The load never resolves. |
| 4 | `s4` · rupture · **peak** | 0:30 | 12s | In March 2020, MakerDAO collateral was auctioned for zero dollars.<br>Under stress, the machinery does exactly what it was built to do. | Under stress, that machinery does exactly what it was built to do. March 2020: MakerDAO’s collateral was auctioned for zero dollars. Around eight million dollars of it, sold for nothing. | The balance rule across the top snaps and wipes out at 3.6s. Six gold blocks collapse to the baseline in a fast stagger from 4.1s. A 132px vermilion $0 lands hard at 7.4s. The caption follows at 9.1s. This is the film’s only break. |
| 5 | `s5` · hold | 0:42 | 10s | The problem is the mechanism, not the risk management.<br>Curators. LTV policy. De-leverage frameworks. Signed agreements. The threshold is unchanged. | Every fix since has been discipline: better curators, tighter frameworks, more paperwork. The mechanism is unchanged. It still has a threshold, and thresholds get breached. | The turn happens while still. Four procedural labels fade in one at a time, each a step lower than the last. The vermilion threshold appears at 1.0s and never moves again. This is the quiet the rupture was bought with. |
| 6 | `s6` · assemble · **peak** | 0:52 | 24s | P and N always sum back to the collateral.<br>At or below the strike, P is worth the whole collateral and N nothing. Above it, P takes S/x and N takes the rest. | Medici splits the collateral in two: P, protected, and N, amplified. At maturity one price is read against the strike. At or below it, P is worth the whole collateral, N nothing. Above it, P takes S over x, N takes the rest. They always sum to the collateral, at every price. No under-collateralized state. No threshold. Nothing to force-sell. | Reveal order follows the narration exactly and nothing that arrives ever leaves. 3.4s the single plate contracts and the P and N plates slide out of it; 1.4s the axes, 3.8s the strike; 5.3s the gold P region wipes in from the left, 10.6s the vermilion N region above it; 11.0s the verdigris tether reads “one collateral, never leaves the vault”; 15.8–20.6s the verdigris balance rule foots across the top at 1.00 and holds. The invariant is only legible as an accumulation that never breaks. |
| 7 | `s7` · hold | 1:16 | 14s | It settles where the collateral already lives, privately and atomically.<br>$344 billion of real-world assets already sit on Canton. | It runs on Canton, where three hundred and forty-four billion dollars of real-world assets already sit. Positions are visible to their counterparties and no one else. Split, roll and settlement are single atomic transactions. | The turn is one of place, not process, so the frame settles rather than develops. Eighty gold marks fade up in a slow field wash; at 6.4s a verdigris dashed scope encloses them; at 8.7s the atomic-settlement bracket closes underneath. Nothing moves after that. |
| 8 | `s8` · divest | 1:30 | 18s | P gives up everything above the strike, and nothing is on mainnet.<br>Nine years of backtest put the drift at −1.25%/yr, on ETH. | The cost is real. P is short a call above the strike: when the asset rallies, P’s value declines, continuously and computably. Nine years of backtest put that drift at negative one and a quarter percent a year, on ETH. And nothing is on mainnet yet. | Motion is subtractive only; nothing new enters. The N region leaves at 4.0s, its label at 4.0s, the grid at 7.9s, leaving P’s continuous decline alone under the balance rule. Beside it four claims are struck through one at a time from 5.4s and dim. The film removes its own apparatus. |
| 9 | `s9` · cadence | 1:48 | 12s | Bring one tokenized position and argue with the payoff table.<br>If the math holds, the asset never has to be sold. | So this is not a pitch to allocate. Bring one tokenized position, and argue with the payoff table. If the math holds, the asset never has to be sold. | One gesture, then stop. The position from scene 1 returns and opens into P and N, tethered, at 1.7s; the verdigris tether reads at 5.5s; the frame then holds absolutely still to the end of the recording. It resolves the opening image: whole, and still held. |

---

## Per-scene detail

### 1. `s1` — hold, energy 1

- **In / out:** 0:00 → 0:10 (10s)
- **On screen:** Tokenized assets are on-chain, and mostly sitting still.
- **Second line:** Treasuries. Fund shares. Gold.
- **VO (verbatim):** Tokenized treasuries, fund shares, gold: on-chain now, and mostly sitting still. Making one productive means accepting a liquidation price. There is a way that doesn’t.
- **What moves:** Nothing develops. One gold-leaf position holds at centre on the ruled field with a slow 9s luminance breath; the claim settles once and stops. The cold open spends no contrast.
- **Source:** canton-pitch-deck.md Slides 4, 7

### 2. `s2` — accumulate, energy 2

- **In / out:** 0:10 → 0:20 (10s)
- **On screen:** Every venue that takes that collateral prices a liquidation threshold.
- **Second line:** Morpho RWA deposits: ~zero in early 2025 → $620M+ by March 2026.
- **VO (verbatim):** Every venue that lends against these assets prices in a liquidation threshold. On Morpho, tokenized collateral grew from nothing to over $620 million in a year.
- **What moves:** Fourteen gold columns grow from the baseline left to right across the scene — the climb is the point, not the end value. At 6.0s a vermilion dashed threshold is laid across the whole field, above every column.
- **Source:** rwa-redstone-2026.md Part 2 addendum; canton-pitch-deck.md Slide 2

### 3. `s3` — strain, energy 3

- **In / out:** 0:20 → 0:30 (10s)
- **On screen:** This collateral cannot be sold in a single transaction.
- **Second line:** NAV pricing · monthly redemption windows · so the market signs liquidation agreements with issuers.
- **VO (verbatim):** But this collateral doesn’t behave: NAV pricing, monthly redemption windows, no sale in a single transaction. So the market signs liquidation agreements with issuers.
- **What moves:** A vermilion load arrow descends from 1.8s; the stack of ruled lines compresses to 72% and skews under it. A sell arrow runs at the redemption window twice (4.4s, 6.8s) and is turned back both times. The load never resolves.
- **Source:** rwa-redstone-2026.md Part 2 — vault standards + liquidation mechanics

### 4. `s4` — rupture, energy 5, **peak**

- **In / out:** 0:30 → 0:42 (12s)
- **On screen:** In March 2020, MakerDAO collateral was auctioned for zero dollars.
- **Second line:** Under stress, the machinery does exactly what it was built to do.
- **VO (verbatim):** Under stress, that machinery does exactly what it was built to do. March 2020: MakerDAO’s collateral was auctioned for zero dollars. Around eight million dollars of it, sold for nothing.
- **What moves:** The balance rule across the top snaps and wipes out at 3.6s. Six gold blocks collapse to the baseline in a fast stagger from 4.1s. A 132px vermilion $0 lands hard at 7.4s. The caption follows at 9.1s. This is the film’s only break.
- **Source:** canton-pitch-deck.md Slide 2; asset-manager-pitch-deck.md Slide 2

### 5. `s5` — hold, energy 1

- **In / out:** 0:42 → 0:52 (10s)
- **On screen:** The problem is the mechanism, not the risk management.
- **Second line:** Curators. LTV policy. De-leverage frameworks. Signed agreements. The threshold is unchanged.
- **VO (verbatim):** Every fix since has been discipline: better curators, tighter frameworks, more paperwork. The mechanism is unchanged. It still has a threshold, and thresholds get breached.
- **What moves:** The turn happens while still. Four procedural labels fade in one at a time, each a step lower than the last. The vermilion threshold appears at 1.0s and never moves again. This is the quiet the rupture was bought with.
- **Source:** canton-pitch-deck.md Slide 2; rwa-redstone-2026.md Part 2

### 6. `s6` — assemble, energy 4, **peak**

- **In / out:** 0:52 → 1:16 (24s)
- **On screen:** P and N always sum back to the collateral.
- **Second line:** At or below the strike, P is worth the whole collateral and N nothing. Above it, P takes S/x and N takes the rest.
- **VO (verbatim):** Medici splits the collateral in two: P, protected, and N, amplified. At maturity one price is read against the strike. At or below it, P is worth the whole collateral, N nothing. Above it, P takes S over x, N takes the rest. They always sum to the collateral, at every price. No under-collateralized state. No threshold. Nothing to force-sell.
- **What moves:** Reveal order follows the narration exactly and nothing that arrives ever leaves. 3.4s the single plate contracts and the P and N plates slide out of it; 1.4s the axes, 3.8s the strike; 5.3s the gold P region wipes in from the left, 10.6s the vermilion N region above it; 11.0s the verdigris tether reads “one collateral, never leaves the vault”; 15.8–20.6s the verdigris balance rule foots across the top at 1.00 and holds. The invariant is only legible as an accumulation that never breaks.
- **Source:** canton-pitch-deck.md Slides 3, 5; asset-manager-pitch-deck.md Slides 4, 5

### 7. `s7` — hold, energy 2

- **In / out:** 1:16 → 1:30 (14s)
- **On screen:** It settles where the collateral already lives, privately and atomically.
- **Second line:** $344 billion of real-world assets already sit on Canton.
- **VO (verbatim):** It runs on Canton, where three hundred and forty-four billion dollars of real-world assets already sit. Positions are visible to their counterparties and no one else. Split, roll and settlement are single atomic transactions.
- **What moves:** The turn is one of place, not process, so the frame settles rather than develops. Eighty gold marks fade up in a slow field wash; at 6.4s a verdigris dashed scope encloses them; at 8.7s the atomic-settlement bracket closes underneath. Nothing moves after that.
- **Source:** canton-pitch-deck.md Slide 4

### 8. `s8` — divest, energy 1

- **In / out:** 1:30 → 1:48 (18s)
- **On screen:** P gives up everything above the strike, and nothing is on mainnet.
- **Second line:** Nine years of backtest put the drift at −1.25%/yr, on ETH.
- **VO (verbatim):** The cost is real. P is short a call above the strike: when the asset rallies, P’s value declines, continuously and computably. Nine years of backtest put that drift at negative one and a quarter percent a year, on ETH. And nothing is on mainnet yet.
- **What moves:** Motion is subtractive only; nothing new enters. The N region leaves at 4.0s, its label at 4.0s, the grid at 7.9s, leaving P’s continuous decline alone under the balance rule. Beside it four claims are struck through one at a time from 5.4s and dim. The film removes its own apparatus.
- **Source:** canton-pitch-deck.md Slides 3, 9; asset-manager-pitch-deck.md Slides 4, 7, 12

### 9. `s9` — cadence, energy 2

- **In / out:** 1:48 → 2:00 (12s)
- **On screen:** Bring one tokenized position and argue with the payoff table.
- **Second line:** If the math holds, the asset never has to be sold.
- **VO (verbatim):** So this is not a pitch to allocate. Bring one tokenized position, and argue with the payoff table. If the math holds, the asset never has to be sold.
- **What moves:** One gesture, then stop. The position from scene 1 returns and opens into P and N, tethered, at 1.7s; the verdigris tether reads at 5.5s; the frame then holds absolutely still to the end of the recording. It resolves the opening image: whole, and still held.
- **Source:** BRIEF.md (ask = a conversation); house-brand-guide.md §0.5

---

## Motion ledger

| scene | role | energy | peak | figures rendered |
|---|---|---|---|---|
| s1 | hold | 1 | — | yes |
| s2 | accumulate | 2 | — | yes |
| s3 | strain | 3 | — | yes |
| s4 | rupture | 5 | yes | yes |
| s5 | hold | 1 | — | yes |
| s6 | assemble | 4 | yes | yes |
| s7 | hold | 2 | — | yes |
| s8 | divest | 1 | — | yes |
| s9 | cadence | 2 | — | yes |

Total runtime: 120s, matching the contract's 120s.
Every slide and scene carries the footer `Medici — Proprietary & Confidential`.
