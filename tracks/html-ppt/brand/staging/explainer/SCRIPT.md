# Medici for RWA tokens — no liquidation price exists — explainer script

Track `html-ppt` / mode `brand` / messaging `staging`. 9 scenes, 120s total. Scene durations are the contract's `vo_seconds`, unmodified.

Player: `explainer.html` auto-plays on load. `?scene=N` opens at scene N; Space / → advance, ← goes back, `P` pauses, `R` restarts, `F` fullscreen. `window.__player` exposes `{scene, t, total, scenes, playing, sceneStart, seek(n), play(), pause()}` — `scene` is the 1-based scene number, `t` and `total` are seconds.

| scene | start | duration | window | on-screen claim |
|---|---|---|---|---|
| `s1` | 0s | 10s | 0&ndash;10s | Tokenized assets are on-chain, and mostly sitting still. |
| `s2` | 10s | 10s | 10&ndash;20s | Every venue that takes that collateral prices a liquidation threshold. |
| `s3` | 20s | 10s | 20&ndash;30s | This collateral cannot be sold in a single transaction. |
| `s4` | 30s | 12s | 30&ndash;42s | In March 2020, MakerDAO collateral was auctioned for zero dollars. |
| `s5` | 42s | 10s | 42&ndash;52s | The problem is the mechanism, not the risk management. |
| `s6` | 52s | 24s | 52&ndash;76s | P and N always sum back to the collateral. |
| `s7` | 76s | 14s | 76&ndash;90s | It settles where the collateral already lives, privately and atomically. |
| `s8` | 90s | 18s | 90&ndash;108s | P gives up everything above the strike, and nothing is on mainnet. |
| `s9` | 108s | 12s | 108&ndash;120s | Bring one tokenized position and argue with the payoff table. |

---

### s1 &middot; 0s &rarr; 10s (10s)

**On screen** &mdash; Medici / Tokenized assets are on-chain, and mostly sitting still.

**Figure labels** &mdash; a tokenized treasury, fund share, gold bar on-chain now, and mostly sitting still making it productive means accepting a liquidation price

**VO (verbatim from `staging.yaml`)** &mdash; “Tokenized treasuries, fund shares, gold: on-chain now, and mostly sitting still. Making one productive means accepting a liquidation price. There is a way that doesn't.”

**What moves** &mdash; hold / energy 1 — nothing moves. The position card is drawn once and held; the cold open spends no contrast before there is anything to contrast with.

### s2 &middot; 10s &rarr; 20s (10s)

**On screen** &mdash; Every venue that takes that collateral prices a liquidation threshold. / Morpho RWA deposits, early 2025 → March 2026

**Figure labels** &mdash; early 2025 March 2026 $620M+ 87% utilization ~0 every venue prices a liquidation threshold

**VO (verbatim from `staging.yaml`)** &mdash; “Every venue that lends against it prices in a liquidation threshold. On Morpho, tokenized collateral grew from nothing to over $620 million in a year.”

**What moves** &mdash; accumulate / energy 2 — the deposit curve draws itself across 3.4s from ~0 to $620M+; the red dashed threshold line is already there, unmoving, waiting.

### s3 &middot; 20s &rarr; 30s (10s)

**On screen** &mdash; This collateral cannot be sold in a single transaction.

**Figure labels** &mdash; NAV-priced collateral, monthly redemption NAV pricing monthly redemption windows so the market signs liquidation agreements with issuers

**VO (verbatim from `staging.yaml`)** &mdash; “But this collateral doesn't behave: NAV pricing, monthly redemption windows, no sale in a single transaction. So the market signs liquidation agreements with issuers.”

**What moves** &mdash; strain / energy 3 — three hand-built patches arrive under the position at 1.6s, 3.0s, 4.4s and the asset frame settles downward over 6s: an arrangement visibly not coping.

### s4 &middot; 30s &rarr; 42s (12s)

**On screen** &mdash; In March 2020, MakerDAO collateral was auctioned for zero dollars.

**Figure labels** &mdash; ~$8M of collateral $0 March 2020 auctioned for nothing

**VO (verbatim from `staging.yaml`)** &mdash; “Under stress, that machinery does exactly what it was built to do. March 2020: MakerDAO's collateral was auctioned for zero dollars. Around eight million dollars of it, sold for nothing.”

**What moves** &mdash; rupture / energy 5, the bold moment — the collateral column collapses to the baseline in 0.55s at 4.2s and does not recover; $0 lands at 4.7s; the frame then holds in silence.

### s5 &middot; 42s &rarr; 52s (10s)

**On screen** &mdash; The problem is the mechanism, not the risk management.

**Figure labels** &mdash; liquidation threshold curators LTV policy de-leverage frameworks signed liquidation agreements the mechanism underneath is unchanged a threshold exists, and thresholds get breached

**VO (verbatim from `staging.yaml`)** &mdash; “Every fix since has been discipline: better curators, tighter frameworks, more paperwork. The mechanism is unchanged. It still has a threshold, and thresholds get breached.”

**What moves** &mdash; hold / energy 1 — a still frame. The patches and the threshold line are both simply present; nothing animates. This is the quiet the rupture was bought with.

### s6 &middot; 52s &rarr; 76s (24s)

**On screen** &mdash; P and N always sum back to the collateral.

**Figure labels** &mdash; one tokenized position P · protected N · amplified P + N ≡ collateral strike S reference price x → P + N = 1.00 P = S/x N = 1 − S/x

**VO (verbatim from `staging.yaml`)** &mdash; “Medici splits the collateral in two: P, protected, and N, amplified. At maturity one price is read against the strike. At or below it, P is worth the whole collateral, N nothing. Above it, P takes S over x, N takes the rest. They always sum to the collateral, at every price. No under-collateralized state. No threshold. Nothing to force-sell.”

**What moves** &mdash; assemble / energy 4 — reveal order follows the narration exactly: the whole position lifts (1.4s), P separates left (2.0s), N right (2.4s), the tether holds (3.0s), P + N ≡ collateral lands (3.6s); then the strike (7.6s), P's curve draws (8–10.2s), the P band fills (8.6s), the N band fills (10.2s), and the flat top edge — the invariant — arrives last (11.4s). A white sweep crosses every price from 12.4s. Nothing that arrives ever leaves.

### s7 &middot; 76s &rarr; 90s (14s)

**On screen** &mdash; It settles where the collateral already lives, privately and atomically.

**Figure labels** &mdash; Canton $344B represented your position, stakeholder-scoped visible to counterparties, not to the market split · roll · settle = one atomic transaction

**VO (verbatim from `staging.yaml`)** &mdash; “It runs on Canton, where three hundred and forty-four billion dollars of real-world assets already sit. Positions are visible to their counterparties and no one else. Split, roll and settlement are single atomic transactions.”

**What moves** &mdash; hold / energy 2 — the frame settles rather than develops: the stakeholder-scoped boundary fades up at 1.2s, the atomic-settlement line at 3.6s. One turn of place, not of process.

### s8 &middot; 90s &rarr; 108s (18s)

**On screen** &mdash; P gives up everything above the strike, and nothing is on mainnet. / 9-year backtest, ETH underlying · nothing is on mainnet yet

**Figure labels** &mdash; strike S reference price x → P + N = 1.00 P = S/x N = 1 − S/x −1.25%/yr net drift

**VO (verbatim from `staging.yaml`)** &mdash; “The cost is real. P is short a call above the strike: when the asset rallies, P's value declines, continuously and computably. Nine years of backtest put that drift at negative one and a quarter percent a year, on ETH. And nothing is on mainnet yet.”

**What moves** &mdash; divest / energy 1 — motion is subtractive only. The N band fades out at 4.0s, its label at 4.4s, the invariant edge at 5.0s, the P fill at 6.0s; what is left standing is P's bare declining line and the drift number at 7.2s.

### s9 &middot; 108s &rarr; 120s (12s)

**On screen** &mdash; Bring one tokenized position and argue with the payoff table. / If the math holds, the asset never has to be sold.

**Figure labels** &mdash; one tokenized position collateral never leaves the vault P · protected capped, income-bearing N · amplified everything above strike P + N ≡ collateral

**VO (verbatim from `staging.yaml`)** &mdash; “So this is not a pitch to allocate. Bring one tokenized position, and argue with the payoff table. If the math holds, the asset never has to be sold.”

**What moves** &mdash; cadence / energy 2 — the s1 position returns, splits once, and stops. One gesture; the opening image is resolved rather than summarised.

No audio, no video, no TTS — the VO column is the narration to be recorded over a screen capture of the 1920×1080 stage.
