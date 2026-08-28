# Medici for RWA tokens — the asset you can't sell in a hurry — explainer script

Track `html-ppt` / mode `brand` / messaging `presentation-writing`. 8 scenes, 132s total. Scene durations are the contract's `vo_seconds`, unmodified.

Player: `explainer.html` auto-plays on load. `?scene=N` opens at scene N; Space / → advance, ← goes back, `P` pauses, `R` restarts, `F` fullscreen. `window.__player` exposes `{scene, t, total, scenes, playing, sceneStart, seek(n), play(), pause()}` — `scene` is the 1-based scene number, `t` and `total` are seconds.

| scene | start | duration | window | on-screen claim |
|---|---|---|---|---|
| `s1` | 0s | 12s | 0&ndash;12s | Real collateral, on a ledger, that nobody can sell in one transaction |
| `s2` | 12s | 18s | 12&ndash;30s | Every venue prices that loan against a liquidation threshold anyway |
| `s3` | 30s | 16s | 30&ndash;46s | When the pathway runs, it runs at zero |
| `s4` | 46s | 12s | 46&ndash;58s | Medici asks a different question |
| `s5` | 58s | 20s | 58&ndash;78s | One position becomes two claims that always add back to it |
| `s6` | 78s | 24s | 78&ndash;102s | The liquidation line has nowhere to sit |
| `s7` | 102s | 17s | 102&ndash;119s | P is short a call, and the decline is the income |
| `s8` | 119s | 13s | 119&ndash;132s | Bring us the thing you can’t sell in a hurry |

---

### s1 &middot; 0s &rarr; 12s (12s)

**On screen** &mdash; Medici / Real collateral, on a ledger, that nobody can sell in one transaction

**Figure labels** &mdash; a tokenized fund share. a gold bar with a ticker. real collateral, on a ledger and none of it can be sold inside a single transaction

**VO (verbatim from `staging.yaml`)** &mdash; “A tokenized fund share. A gold bar with a ticker. Real collateral, on a ledger — and none of it can be sold inside a single transaction.”

**What moves** &mdash; hold / energy 1.0 — the frame is given, not developed. One card, drawn once and held; the piece has one loud moment and this is not it.

### s2 &middot; 12s &rarr; 30s (18s)

**On screen** &mdash; Every venue prices that loan against a liquidation threshold anyway / RedStone calls those fundamental design constraints, not edge cases.

**Figure labels** &mdash; NAV-priced collateral, monthly redemption signed liquidation agreements with the issuer curator-run de-leverage frameworks NAV instead of a market price

**VO (verbatim from `staging.yaml`)** &mdash; “Every venue that lends against it prices the loan against a liquidation threshold anyway. So the desks patch the gap by hand — signed liquidation agreements with the issuer, curator-run de-leverage frameworks, NAV instead of a market price. RedStone calls those fundamental design constraints, not edge cases.”

**What moves** &mdash; strain / energy 3.0 — comfort turns into load. The three patches arrive at 1.6s, 3.0s and 4.4s while the asset frame settles downward across 6s: one patch is prudence, three is a workaround, and the scene has the time to show the difference.

### s3 &middot; 30s &rarr; 46s (16s)

**On screen** &mdash; When the pathway runs, it runs at zero / Black Thursday · one forced sale sets off the next

**Figure labels** &mdash; → → $8M of collateral, cleared for $0

**VO (verbatim from `staging.yaml`)** &mdash; “And when the pathway actually runs, it runs at the worst possible price. On Black Thursday, MakerDAO collateral was auctioned for zero dollars. Eight million dollars of it. One forced sale sets off the next.”

**What moves** &mdash; accumulate / energy 3.5, a peak — three collateral columns collapse in series at 3.4s, 4.3s and 5.2s, each collapse lighting the arrow into the next. The growth of the chain is the claim: a cascade is not one event repeated, it feeds itself.

### s4 &middot; 46s &rarr; 58s (12s)

**On screen** &mdash; Medici asks a different question / Not how do we liquidate this safely — what if there were nothing to liquidate? Split the collateral instead.

**VO (verbatim from `staging.yaml`)** &mdash; “Medici asks a different question. Not how do we liquidate this safely — what if there were nothing to liquidate? Split the collateral instead.”

**What moves** &mdash; hold / energy 1.0 — deliberately still, and deliberately figure-less: the contract gives this scene no figures, so the screen carries type alone. This is the quiet scenes 3 and 6 are paid for with.

### s5 &middot; 58s &rarr; 78s (20s)

**On screen** &mdash; One position becomes two claims that always add back to it / The oracle isn’t even read until settlement.

**Figure labels** &mdash; one tokenized position collateral never leaves the vault P · protected capped, income-bearing N · amplified everything above strike P + N ≡ collateral

**VO (verbatim from `staging.yaml`)** &mdash; “One position becomes two claims. P is capped and income-bearing. N takes everything above the strike. P plus N always equals the collateral — closed form, at every price, enforced by the contract that records the split. The oracle isn't even read until settlement.”

**What moves** &mdash; assemble / energy 3.0 — the whole position lifts at 1.4s, P separates left at 2.0s, N right at 2.4s, and the tether between them fades up at 3.0s and never breaks; the identity lands at 3.6s. Nothing leaves the system, which is the whole point of the scene.

### s6 &middot; 78s &rarr; 102s (24s)

**On screen** &mdash; The liquidation line has nowhere to sit

**Figure labels** &mdash; strike S reference price x → P + N = 1.00 P = S/x N = 1 − S/x liquidation threshold nowhere to put it

**VO (verbatim from `staging.yaml`)** &mdash; “At maturity there are two cases. At or below the strike, P is worth the whole collateral and N is worth nothing. Above it, P is the strike over the price; N is the rest. Now draw the liquidation line every other venue needs. There is nowhere on this axis to put it — no price under-collateralizes the vault.”

**What moves** &mdash; rupture / energy 5.0, the bold moment — the payoff assembles first (strike 0.6s, P's curve 1–3.2s, the P band 1.6s, the N band 3.2s, the flat invariant edge 4.4s). Then at 13s the red liquidation line drops in from above, reaches full height at ~14.8s, and fades out where it should have landed; ‘nowhere to put it’ is left on the axis. The break is that a motion completes and finds nothing.

### s7 &middot; 102s &rarr; 119s (17s)

**On screen** &mdash; P is short a call, and the decline is the income / Nine years of backtest · never a cliff

**Figure labels** &mdash; strike S reference price x → P + N = 1.00 P = S/x N = 1 − S/x −1.25%/yr net drift

**VO (verbatim from `staging.yaml`)** &mdash; “That is not free. P is short a call above the strike, so P's value falls continuously as the asset rallies — nine years of backtest put the net drift at minus one and a quarter percent a year. Never a cliff.”

**What moves** &mdash; divest / energy 1.0 — subtractive only. The N band fades at 4.0s, its label at 4.4s, the invariant edge at 5.0s, the P fill at 6.0s. What is left is the bare declining curve and the drift number at 7.2s: the film taking its own apparatus away.

### s8 &middot; 119s &rarr; 132s (13s)

**On screen** &mdash; Bring us the thing you can’t sell in a hurry / Medici — on Canton, where your collateral already lives.

**Figure labels** &mdash; one tokenized position collateral never leaves the vault P · protected capped, income-bearing N · amplified everything above strike P + N ≡ collateral

**VO (verbatim from `staging.yaml`)** &mdash; “So bring us the thing you can't sell in a hurry. There is no liquidation price. The math doesn't permit it. Medici — on Canton, where your collateral already lives.”

**What moves** &mdash; cadence / energy 2.0 — the scene-1 asset returns, splits once, and stops. One gesture, then the film ends; the opening image is resolved, not summarised.

No audio, no video, no TTS — the VO column is the narration to be recorded over a screen capture of the 1920×1080 stage.
