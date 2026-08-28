# SCRIPT.md — Medici explainer (presentation-writing contract)

Brand mode. Stage 1920×1080, `explainer.html`, self-contained, no audio and no TTS —
narration below is read by a person over the screen recording. Scene durations are the
messaging contract's `vo_seconds`, unchanged. Total runtime **132 s**.

Playback: auto-plays on load. `?scene=N` jumps to a scene; Space or → advances, ←
steps back, Home restarts. `window.__player = {scene, t, total, totalSeconds, seek(n)}`
is exposed for tooling. `prefers-reduced-motion: reduce` disables all motion and every
scene still reads as a still frame.

Eight scenes, energies 1.0 · 3.0 · 3.5 · 1.0 · 3.0 · 5.0 · 1.0 · 2.0 — the contract's motion budget, rendered. Two peaks (s3 accumulate, s6 rupture), never adjacent; three quiet scenes (1, 4, 7).

| # | Start | Dur | On-screen text | VO narration (verbatim from the contract) | What moves |
|---|------:|----:|---|---|---|
| 1 | 0:00 | 12 s | Real collateral, on a ledger, that nobody can sell in one transaction | A tokenized fund share. A gold bar with a ticker. Real collateral, on a ledger — and none of it can be sold inside a single transaction. | hold (1.0) — the position rises in once and the frame is given, not developed. The piece has one loud moment and this is not it. |
| 2 | 0:12 | 18 s | Every venue prices that loan against a liquidation threshold anyway | Every venue that lends against it prices the loan against a liquidation threshold anyway. So the desks patch the gap by hand — signed liquidation agreements with the issuer, curator-run de-leverage frameworks, NAV instead of a market price. RedStone calls those fundamental design constraints, not edge cases. | strain (3.0) — the threshold is present from frame one; three patches attach at 16%, 42% and 68% while the position's stroke thickens and greys across the full scene. One patch is prudence, three is a workaround, and that needs time to accumulate. |
| 3 | 0:30 | 16 s | When the pathway runs, it runs at zero · Black Thursday — $8M of MakerDAO collateral auctioned for $0 | And when the pathway actually runs, it runs at the worst possible price. On Black Thursday, MakerDAO collateral was auctioned for zero dollars. Eight million dollars of it. One forced sale sets off the next. | accumulate (3.5, peak) — seven positions fall and grey out in sequence at a quickening cadence, and the caption lands at 72%. A cascade is a chain that feeds itself, not one event repeated, so the growth is the point. |
| 4 | 0:46 | 12 s | Medici asks a different question | Medici asks a different question. Not how do we liquidate this safely — what if there were nothing to liquidate? Split the collateral instead. | hold (1.0) — one 0.35 s rule strikes the old question out and the new one rises. Deliberately still: this is the quiet that scenes 3 and 6 are paid for with. |
| 5 | 0:58 | 20 s | One position becomes two claims that always add back to it | One position becomes two claims. P is capped and income-bearing. N takes everything above the strike. P plus N always equals the collateral — closed form, at every price, enforced by the contract that records the split. The oracle isn’t even read until settlement. | assemble (3.0) — the collateral and its dimension line arrive first; the split arrow at 18%; N at 30% and P at 42%, stacked with no gap so their combined height is unchanged; the second dimension line at 58% is exactly as long as the first. The identity is only legible if the viewer watches the parts arrive and stay. |
| 6 | 1:18 | 24 s | The liquidation line has nowhere to sit | At maturity there are two cases. At or below the strike, P is worth the whole collateral and N is worth nothing. Above it, P is the strike over the price; N is the rest. Now draw the liquidation line every other venue needs. There is nowhere on this axis to put it — no price under-collateralizes the vault. | RUPTURE (5.0, peak, bold moment) — the payoff is already complete and still. From 12% the threshold line is dragged across the whole axis looking for a place, decelerates, and at 76% the verdict lands. The threshold is introduced and then cannot be placed; this is the only break in the film. |
| 7 | 1:42 | 17 s | P is short a call, and the decline is the income | That is not free. P is short a call above the strike, so P’s value falls continuously as the asset rallies — nine years of backtest put the net drift at minus one and a quarter percent a year. Never a cliff. | divest (1.0) — motion is subtractive only: the apparatus is taken away at 18% and the cost is left standing alone at 58%. This is also scene 6's payment. |
| 8 | 1:59 | 13 s | Bring us the thing you can’t sell in a hurry | So bring us the thing you can’t sell in a hurry. There is no liquidation price. The math doesn’t permit it. Medici — on Canton, where your collateral already lives. | cadence (2.0) — the same asset from scene 1, now split and still held; one dimension line draws at 26%, then stop. |

**Footer.** `Medici — Proprietary & Confidential` is on every frame (house brand
guide §10.6 rule 1 — the footer is the authoritative artifact-class marker).
