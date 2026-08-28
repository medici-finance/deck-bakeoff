# SCRIPT.md — Medici explainer · `pitch-deck-mastery` · impeccable / free

**Runtime 143s (2:23) · 8 scenes · 1920×1080 · no audio, no TTS, no video.**
Screen-record `explainer/explainer.html`; it auto-plays on load. `?scene=N` jumps to a scene,
Space / → advance, ← steps back, `P` pauses. `window.__player` exposes `{scene, t, total, seek(n)}`.

VO column is **verbatim** from `messaging/pitch-deck-mastery/staging.yaml`; nothing was reworded or added.
Motion roles, energies and peaks are the contract's, not the designer's.

| # | scene | start | dur | on-screen text | VO (verbatim) | what moves |
|---|---|---|---|---|---|---|
| 1 | `1` · hold | 0:00 | 13s | Your tokenized collateral has a price at which someone else sells it.<br>A fund share. A treasury. A bond. | You hold a tokenized position — a fund share, a treasury, a bond. The moment you finance it, somewhere in the paperwork there is a price at which somebody else sells it. | It needs time only to be given, not developed. One gold-leaf plate holds at centre; a vermilion dashed line is marked across it and stays there. That marked price is what scenes 2 and 5 both act on. |
| 2 | `2` · rupture · **peak** | 0:13 | 22s | When the threshold breaks, the position is sold at the worst price.<br>On Black Thursday, $8 million of collateral cleared for $0. Most tokenized assets cannot be sold in one transaction, so the market signs liquidation agreements with issuers. | That is a liquidation threshold. Price crosses it, and the collateral is sold into the fall. On Black Thursday, eight million dollars of collateral cleared for zero. Tokenized assets are worse — most cannot be sold in one transaction, so the market signs liquidation agreements with issuers. | The break must be seen to happen, because scene 5 begins the identical gesture and stops it. A price track is drawn from 2.2s and crosses the marked threshold at about 12s; at 11.4s the held plate is taken — it drops, flattens to 6% and greys out. The caption lands at 15.4s. |
| 3 | `3` · assemble | 0:35 | 20s | Medici splits one position into two claims: Protected and Amplified.<br>Both issued atomically. Both stay claims on collateral that never leaves the vault. | Medici does something else with the same collateral. It splits the position into two claims. Protected takes the value at or below a strike you choose. Amplified takes everything above it. Both are issued atomically, and both stay claims on collateral that never leaves the vault. | One object becomes two that remain one. The source plate contracts at 2.8s while the gold P and vermilion N plates slide out of it and stay; the verdigris tether appears at 9.2s and persists visibly across the gap. The tether is the whole figure — only time can show it holding. |
| 4 | `4` · accumulate | 0:55 | 21s | At maturity, P takes S/x, N takes the rest, and the two still sum to the collateral.<br>Sweep the price across the whole range. The top edge never leaves 1.00. | At maturity, one reference price is read. At or below the strike, Protected takes the full collateral value and Amplified takes nothing. Above it, Protected takes S over x and Amplified takes the rest. Sweep the price across the whole range: the two always add back to exactly the collateral. | The point is the sweep across every price, not any single price. The plate assembles (gold P 4.6s, vermilion N 9.2s, verdigris balance rule 13.9s) and a verdigris price marker then travels the full width of the axis from 6.3s to 17.2s. At every position it crosses, the gold and vermilion columns beneath it add to the same flat top edge. |
| 5 | `5` · arrest · **peak** | 1:16 | 21s | The price rises, and the liquidation that would fire does not exist.<br>A lending market would seize the collateral here. Nothing fires. A theorem, not a risk setting. | Now run that first scene again. Price moves hard against the Protected side. A lending market would seize the collateral here. Watch. [2 s hold] Nothing fires. There is no liquidation threshold, because the payoff has no under-collateralized state to trigger one. A theorem, not a risk setting. | The gesture from scene 2 starts identically and stops mid-motion. The vermilion liquidation bar sweeps in from the right at 4.2s, decelerates hard, and arrests at 13.0s a few pixels short of where it was going — then holds, unmoving, for the rest of the scene. “Nothing fires” appears at 15.1s into that stillness. This is the most charged scene and the second stillest; an absence can only be shown by a motion that does not complete. |
| 6 | `6` · hold | 1:37 | 17s | Two holders, two reasons: income kept, exposure amplified.<br>Selling a leg is the liquidity — with no repayment schedule. | Each leg has an owner who wants it. A fund treasury holds Protected and earns on an asset it never sells. An allocator holds Amplified for exposure with no liquidation price and no funding rate. Selling a leg is the liquidity. | Deliberately still: this is the quiet that pays for scene 5, and a viewer recovering from the bold moment should be reading, not tracking. The two holder plates fade up at 1.7s and 4.5s, the tether between them at 8.5s. Nothing moves after 8.5s. |
| 7 | `7` · divest | 1:54 | 14s | What is built is real; what is not built is named.<br>Fifty-four DAML contracts on Canton. A twelve-agent fleet. A nine-year backtest. Closed-form proofs. | What exists today: fifty-four DAML contracts on Canton, a twelve-agent fleet, a nine-year backtest, closed-form proofs. What does not: mainnet, an audit, live collateral, a customer. You should hear that from us. | Motion is subtractive only and nothing new may enter. Four claims are struck through in vermilion one at a time from 4.2s and dim as they go, until what remains on the ruled field is only what is actually built. The register turns from persuasion to disclosure. |
| 8 | `8` · cadence | 2:08 | 15s | Bring one position, and the split is modelled against it.<br>Two claims that always sum back to it, so the position can never be force-sold. | Medici splits a tokenized asset into two claims that always sum back to it, so the position can never be force-sold. Bring one position and a strike; we will show you the payoff at every price. | One gesture, then stop — not a summary of the film. The single position from scene 1 returns at 2.1s, opens into P and N, the tether reads at 6.9s, and the frame holds absolutely still to the end of the recording. |

---

## Per-scene detail

### 1. `1` — hold, energy 1

- **In / out:** 0:00 → 0:13 (13s)
- **On screen:** Your tokenized collateral has a price at which someone else sells it.
- **Second line:** A fund share. A treasury. A bond.
- **VO (verbatim):** You hold a tokenized position — a fund share, a treasury, a bond. The moment you finance it, somewhere in the paperwork there is a price at which somebody else sells it.
- **What moves:** It needs time only to be given, not developed. One gold-leaf plate holds at centre; a vermilion dashed line is marked across it and stays there. That marked price is what scenes 2 and 5 both act on.
- **Source:** asset-manager-pitch-deck.md Slide 2

### 2. `2` — rupture, energy 3.5, **peak**

- **In / out:** 0:13 → 0:35 (22s)
- **On screen:** When the threshold breaks, the position is sold at the worst price.
- **Second line:** On Black Thursday, $8 million of collateral cleared for $0. Most tokenized assets cannot be sold in one transaction, so the market signs liquidation agreements with issuers.
- **VO (verbatim):** That is a liquidation threshold. Price crosses it, and the collateral is sold into the fall. On Black Thursday, eight million dollars of collateral cleared for zero. Tokenized assets are worse — most cannot be sold in one transaction, so the market signs liquidation agreements with issuers.
- **What moves:** The break must be seen to happen, because scene 5 begins the identical gesture and stops it. A price track is drawn from 2.2s and crosses the marked threshold at about 12s; at 11.4s the held plate is taken — it drops, flattens to 6% and greys out. The caption lands at 15.4s.
- **Source:** canton-pitch-deck.md Slide 2; rwa-redstone-2026.md Part 2 “Liquidation mechanics and risk frameworks”

### 3. `3` — assemble, energy 3

- **In / out:** 0:35 → 0:55 (20s)
- **On screen:** Medici splits one position into two claims: Protected and Amplified.
- **Second line:** Both issued atomically. Both stay claims on collateral that never leaves the vault.
- **VO (verbatim):** Medici does something else with the same collateral. It splits the position into two claims. Protected takes the value at or below a strike you choose. Amplified takes everything above it. Both are issued atomically, and both stay claims on collateral that never leaves the vault.
- **What moves:** One object becomes two that remain one. The source plate contracts at 2.8s while the gold P and vermilion N plates slide out of it and stay; the verdigris tether appears at 9.2s and persists visibly across the gap. The tether is the whole figure — only time can show it holding.
- **Source:** canton-pitch-deck.md Slide 3

### 4. `4` — accumulate, energy 3

- **In / out:** 0:55 → 1:16 (21s)
- **On screen:** At maturity, P takes S/x, N takes the rest, and the two still sum to the collateral.
- **Second line:** Sweep the price across the whole range. The top edge never leaves 1.00.
- **VO (verbatim):** At maturity, one reference price is read. At or below the strike, Protected takes the full collateral value and Amplified takes nothing. Above it, Protected takes S over x and Amplified takes the rest. Sweep the price across the whole range: the two always add back to exactly the collateral.
- **What moves:** The point is the sweep across every price, not any single price. The plate assembles (gold P 4.6s, vermilion N 9.2s, verdigris balance rule 13.9s) and a verdigris price marker then travels the full width of the axis from 6.3s to 17.2s. At every position it crosses, the gold and vermilion columns beneath it add to the same flat top edge.
- **Source:** canton-pitch-deck.md Slide 5; asset-manager-pitch-deck.md Slide 4

### 5. `5` — arrest, energy 4, **peak**

- **In / out:** 1:16 → 1:37 (21s)
- **On screen:** The price rises, and the liquidation that would fire does not exist.
- **Second line:** A lending market would seize the collateral here. Nothing fires. A theorem, not a risk setting.
- **VO (verbatim):** Now run that first scene again. Price moves hard against the Protected side. A lending market would seize the collateral here. Watch. [2 s hold] Nothing fires. There is no liquidation threshold, because the payoff has no under-collateralized state to trigger one. A theorem, not a risk setting.
- **What moves:** The gesture from scene 2 starts identically and stops mid-motion. The vermilion liquidation bar sweeps in from the right at 4.2s, decelerates hard, and arrests at 13.0s a few pixels short of where it was going — then holds, unmoving, for the rest of the scene. “Nothing fires” appears at 15.1s into that stillness. This is the most charged scene and the second stillest; an absence can only be shown by a motion that does not complete.
- **Source:** canton-pitch-deck.md Slide 5

### 6. `6` — hold, energy 1

- **In / out:** 1:37 → 1:54 (17s)
- **On screen:** Two holders, two reasons: income kept, exposure amplified.
- **Second line:** Selling a leg is the liquidity — with no repayment schedule.
- **VO (verbatim):** Each leg has an owner who wants it. A fund treasury holds Protected and earns on an asset it never sells. An allocator holds Amplified for exposure with no liquidation price and no funding rate. Selling a leg is the liquidity.
- **What moves:** Deliberately still: this is the quiet that pays for scene 5, and a viewer recovering from the bold moment should be reading, not tracking. The two holder plates fade up at 1.7s and 4.5s, the tether between them at 8.5s. Nothing moves after 8.5s.
- **Source:** canton-pitch-deck.md Slide 6; asset-manager-pitch-deck.md Slide 5

### 7. `7` — divest, energy 2

- **In / out:** 1:54 → 2:08 (14s)
- **On screen:** What is built is real; what is not built is named.
- **Second line:** Fifty-four DAML contracts on Canton. A twelve-agent fleet. A nine-year backtest. Closed-form proofs.
- **VO (verbatim):** What exists today: fifty-four DAML contracts on Canton, a twelve-agent fleet, a nine-year backtest, closed-form proofs. What does not: mainnet, an audit, live collateral, a customer. You should hear that from us.
- **What moves:** Motion is subtractive only and nothing new may enter. Four claims are struck through in vermilion one at a time from 4.2s and dim as they go, until what remains on the ruled field is only what is actually built. The register turns from persuasion to disclosure.
- **Source:** canton-pitch-deck.md Slide 9; asset-manager-pitch-deck.md Slide 12

### 8. `8` — cadence, energy 1

- **In / out:** 2:08 → 2:23 (15s)
- **On screen:** Bring one position, and the split is modelled against it.
- **Second line:** Two claims that always sum back to it, so the position can never be force-sold.
- **VO (verbatim):** Medici splits a tokenized asset into two claims that always sum back to it, so the position can never be force-sold. Bring one position and a strike; we will show you the payoff at every price.
- **What moves:** One gesture, then stop — not a summary of the film. The single position from scene 1 returns at 2.1s, opens into P and N, the tether reads at 6.9s, and the frame holds absolutely still to the end of the recording.
- **Source:** canton-pitch-deck.md Slides 1, 11

---

## Motion ledger

| scene | role | energy | peak | figures rendered |
|---|---|---|---|---|
| 1 | hold | 1 | — | yes |
| 2 | rupture | 3.5 | yes | yes |
| 3 | assemble | 3 | — | yes |
| 4 | accumulate | 3 | — | yes |
| 5 | arrest | 4 | yes | yes |
| 6 | hold | 1 | — | yes |
| 7 | divest | 2 | — | yes |
| 8 | cadence | 1 | — | yes |

Total runtime: 143s, matching the contract's 143s.
Every slide and scene carries the footer `Medici — Proprietary & Confidential`.
