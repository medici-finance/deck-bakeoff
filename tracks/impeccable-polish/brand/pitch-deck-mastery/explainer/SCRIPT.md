# Medici — collateral splitting for tokenized real-world assets — explainer script

Track `html-ppt` / mode `brand` / messaging `pitch-deck-mastery`. 8 scenes, 143s total. Scene durations are the contract's `vo_seconds`, unmodified.

Player: `explainer.html` auto-plays on load. `?scene=N` opens at scene N; Space / → advance, ← goes back, `P` pauses, `R` restarts, `F` fullscreen. `window.__player` exposes `{scene, t, total, scenes, playing, sceneStart, seek(n), play(), pause()}` — `scene` is the 1-based scene number, `t` and `total` are seconds.

| scene | start | duration | window | on-screen claim |
|---|---|---|---|---|
| `s1` | 0s | 13s | 0&ndash;13s | Your tokenized collateral has a price at which someone else sells it. |
| `s2` | 13s | 22s | 13&ndash;35s | When the threshold breaks, the position is sold at the worst price. |
| `s3` | 35s | 20s | 35&ndash;55s | Medici splits one position into two claims: Protected and Amplified. |
| `s4` | 55s | 21s | 55&ndash;76s | At maturity, P takes S/x, N takes the rest, and the two still sum to the collateral. |
| `s5` | 76s | 21s | 76&ndash;97s | The price rises, and the liquidation that would fire does not exist. |
| `s6` | 97s | 17s | 97&ndash;114s | Two holders, two reasons: income kept, exposure amplified. |
| `s7` | 114s | 14s | 114&ndash;128s | What is built is real; what is not built is named. |
| `s8` | 128s | 15s | 128&ndash;143s | Bring one position, and the split is modelled against it. |

---

### s1 &middot; 0s &rarr; 13s (13s)

**On screen** &mdash; Medici / Your tokenized collateral has a price at which someone else sells it.

**Figure labels** &mdash; a fund share. a treasury. a bond. you hold a tokenized position the moment you finance it… a price at which somebody else sells it

**VO (verbatim from `staging.yaml`)** &mdash; “You hold a tokenized position — a fund share, a treasury, a bond. The moment you finance it, somewhere in the paperwork there is a price at which somebody else sells it.”

**What moves** &mdash; hold / energy 1.0 — the position is drawn once and held. At 6s the marked price fades in below it and stays: the object scenes 2 and 5 will both act on is planted, not animated.

### s2 &middot; 13s &rarr; 35s (22s)

**On screen** &mdash; When the threshold breaks, the position is sold at the worst price. / Tokenized assets are worse — most cannot be sold in one transaction, so the market signs liquidation agreements with issuers to do it by hand.

**Figure labels** &mdash; liquidation threshold ~$8M of collateral $0 March 2020 auctioned for nothing

**VO (verbatim from `staging.yaml`)** &mdash; “That is a liquidation threshold. Price crosses it, and the collateral is sold into the fall. On Black Thursday, eight million dollars of collateral cleared for zero. Tokenized assets are worse — most cannot be sold in one transaction, so the market signs liquidation agreements with issuers to do it by hand.”

**What moves** &mdash; rupture / energy 3.5, a peak — the threshold appears at 0.4s, the price line draws down into it from 0.8s to 4.0s, and at 4.2s the collateral column collapses to the baseline in 0.55s. $0 lands at 4.7s. The break must be SEEN for scene 5's refusal to mean anything.

### s3 &middot; 35s &rarr; 55s (20s)

**On screen** &mdash; Medici splits one position into two claims: Protected and Amplified. / Both are issued atomically, and both stay claims on collateral that never leaves the vault.

**Figure labels** &mdash; one tokenized position collateral never leaves the vault P · protected capped, income-bearing N · amplified everything above strike P + N ≡ collateral

**VO (verbatim from `staging.yaml`)** &mdash; “Medici does something else with the same collateral. It splits the position into two claims. Protected takes the value at or below a strike you choose. Amplified takes everything above it. Both are issued atomically, and both stay claims on collateral that never leaves the vault.”

**What moves** &mdash; assemble / energy 3.0 — the position lifts at 1.4s, P separates left at 2.0s and N right at 2.4s, and the tether fades up at 3.0s and persists visibly as the parts separate. The identity lands at 3.6s and nothing afterwards removes it.

### s4 &middot; 55s &rarr; 76s (21s)

**On screen** &mdash; At maturity, P takes S/x, N takes the rest, and the two still sum to the collateral. / Sweep the price across the whole range: the two always add back to exactly the collateral.

**Figure labels** &mdash; strike S reference price x → P + N = 1.00 P = S/x N = 1 − S/x

**VO (verbatim from `staging.yaml`)** &mdash; “At maturity, one reference price is read. At or below the strike, Protected takes the full collateral value and Amplified takes nothing. Above it, Protected takes S over x and Amplified takes the rest. Sweep the price across the whole range: the two always add back to exactly the collateral.”

**What moves** &mdash; accumulate / energy 3.0 — the strike at 1.6s, P's curve drawing 2–4.2s, the P band at 2.6s, the N band at 4.2s, the flat invariant edge at 5.4s, and then a white price line sweeping the entire axis from 6.4s to 10.8s. The point is the sweep, not any single price.

### s5 &middot; 76s &rarr; 97s (21s)

**On screen** &mdash; The price rises, and the liquidation that would fire does not exist. / A theorem, not a risk setting.

**Figure labels** &mdash; strike S reference price x → P + N = 1.00 P = S/x N = 1 − S/x a lending market would seize here nothing fires

**VO (verbatim from `staging.yaml`)** &mdash; “Now run that first scene again. Price moves hard against the Protected side. A lending market would seize the collateral here. Watch. [2 s hold] Nothing fires. There is no liquidation threshold, because the payoff has no under-collateralized state to trigger one. A theorem, not a risk setting.”

**What moves** &mdash; arrest / energy 4.0, the bold moment — the payoff is already assembled. At 9s the same red gesture from scene 2 begins dropping in from above; at ~10.7s it stops dead at half height and simply stays there for two seconds of stillness, then dims. ‘Nothing fires’ resolves at 11.6s. This is the most CHARGED scene and the second stillest: an absence can only be shown by a motion that does not complete.

### s6 &middot; 97s &rarr; 114s (17s)

**On screen** &mdash; Two holders, two reasons: income kept, exposure amplified. / Selling a leg is the liquidity.

**Figure labels** &mdash; Fund treasury holds P income on an asset it keeps never sold, never called Allocator holds N amplified exposure no liquidation price, no funding rate

**VO (verbatim from `staging.yaml`)** &mdash; “Each leg has an owner who wants it. A fund treasury holds Protected and earns on an asset it never sells. An allocator holds Amplified for exposure with no liquidation price and no funding rate. Selling a leg is the liquidity.”

**What moves** &mdash; hold / energy 1.0 — two cards, one at 1.0s and one at 2.2s, and then nothing. Deliberately still: a viewer recovering from the bold moment should be reading, not tracking.

### s7 &middot; 114s &rarr; 128s (14s)

**On screen** &mdash; What is built is real; what is not built is named. / You should hear that from us.

**Figure labels** &mdash; ● 54 DAML contracts on Canton ● a twelve-agent fleet ● a nine-year backtest ● closed-form proofs × mainnet × an audit × live collateral × a customer

**VO (verbatim from `staging.yaml`)** &mdash; “What exists today: fifty-four DAML contracts on Canton, a twelve-agent fleet, a nine-year backtest, closed-form proofs. What does not: mainnet, an audit, live collateral, a customer.”

**What moves** &mdash; divest / energy 2.0 — subtractive only. The four things that do not exist are struck out one at a time at 3s, 4s, 5s and 6s; what remains lit is only what is actually built. Nothing new may enter this scene.

### s8 &middot; 128s &rarr; 143s (15s)

**On screen** &mdash; Bring one position, and the split is modelled against it. / We will show you the payoff at every price.

**Figure labels** &mdash; one tokenized position collateral never leaves the vault P · protected capped, income-bearing N · amplified everything above strike P + N ≡ collateral

**VO (verbatim from `staging.yaml`)** &mdash; “Medici splits a tokenized asset into two claims that always sum back to it, so the position can never be force-sold. Bring one position and a strike; we will show you the payoff at every price.”

**What moves** &mdash; cadence / energy 1.0 — the single position from scene 1 returns, splits, and sums. One gesture, then stop — not a summary of the film.

No audio, no video, no TTS — the VO column is the narration to be recorded over a screen capture of the 1920×1080 stage.
