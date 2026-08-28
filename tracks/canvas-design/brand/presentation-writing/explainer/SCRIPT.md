# SCRIPT — Medici for RWA tokens — presentation-writing

Explainer film, 132s, 8 scenes. 1920×1080. No audio, no TTS: the
voice-over column is the narration to be read over a screen recording of
`explainer.html`. Durations are the contract's `vo_seconds`, unchanged.

Design: **Conservation Plate** (see ../../PHILOSOPHY.md). Motion is measurement —
each scene's movement is the one named in the contract's `motion_role`, and the
quiet scenes stay quiet.

Playback: auto-plays on load. `?scene=N` starts at a scene; Space pauses;
←/→ step scenes. `window.__player = {scene, t, total, seek(n)}`.

| # | id | start | dur | motion | on-screen text | voice-over (verbatim from the contract) | what moves |
|---|----|-------|-----|--------|----------------|------------------------------------------|------------|
| 1 | `1` | 0s | 12s | hold | Real collateral, on a ledger, that nobody can sell in one transaction · A TOKENIZED FUND SHARE · A GOLD BAR WITH A TICKER | A tokenized fund share. A gold bar with a ticker. Real collateral, on a ledger — and none of it can be sold inside a single transaction. | The held field is given, not developed. One position in it is outlined; nothing else changes for twelve seconds. |
| 2 | `2` | 12s | 18s | strain | Every venue prices that loan against a liquidation threshold anyway · SIGNED AGREEMENTS · DE-LEVERAGE FRAMEWORKS · NAV INSTEAD OF A PRICE | Every venue that lends against it prices the loan against a liquidation threshold anyway. So the desks patch the gap by hand — signed liquidation agreements with the issuer, curator-run de-leverage frameworks, NAV instead of a market price. RedStone calls those fundamental design constraints, not edge cases. | The patches arrive one at a time and each one presses the stack down harder onto the threshold line, which never moves. One patch is prudence; three is a workaround. |
| 3 | `3` | 30s | 16s | accumulate (peak) | When the pathway runs, it runs at zero · BLACK THURSDAY · $8M OF COLLATERAL · CLEARED FOR $0 | And when the pathway actually runs, it runs at the worst possible price. On Black Thursday, MakerDAO collateral was auctioned for zero dollars. Eight million dollars of it. One forced sale sets off the next. | Forced sales accumulate left to right across the whole scene, each one dragging the next mark to the baseline — a chain that feeds itself, not one event repeated. |
| 4 | `4` | 46s | 12s | hold | Medici asks a different question · NOT: HOW DO WE LIQUIDATE THIS SAFELY. | Medici asks a different question. Not how do we liquidate this safely — what if there were nothing to liquidate? Split the collateral instead. | Nothing on screen but the question and the frame. Deliberately empty: this is the quiet that scenes 3 and 6 are paid for with. |
| 5 | `5` | 58s | 20s | assemble | One position becomes two claims that always add back to it · THE ORACLE ISN'T READ UNTIL SETTLEMENT | One position becomes two claims. P is capped and income-bearing. N takes everything above the strike. P plus N always equals the collateral — closed form, at every price, enforced by the contract that records the split. The oracle isn't even read until settlement. | The whole divides; the two claims arrive and stay; the tether to the vault is drawn last and never lets go. Nothing leaves the frame, which is the proof. |
| 6 | `6` | 78s | 24s | rupture (peak) | The liquidation line has nowhere to sit · NO PRICE ON THIS AXIS UNDER-COLLATERALIZES THE VAULT | At maturity there are two cases. At or below the strike, P is worth the whole collateral and N is worth nothing. Above it, P is the strike over the price; N is the rest. Now draw the liquidation line every other venue needs. There is nowhere on this axis to put it — no price under-collateralizes the vault. | The payoff assembles, then the threshold line is introduced and driven along the axis looking for a price to land on. It reaches, and is refused, and the frame holds. |
| 7 | `7` | 102s | 17s | divest | P is short a call, and the decline is the income · NET DRIFT −1.25%/YR OVER NINE YEARS · NEVER A CLIFF | That is not free. P is short a call above the strike, so P's value falls continuously as the asset rallies — nine years of backtest put the net drift at minus one and a quarter percent a year. Never a cliff. | Every persuasive mark is taken away one at a time until only the decline curve and its cost remain. Subtractive only. |
| 8 | `8` | 119s | 13s | cadence | Bring us the thing you can't sell in a hurry · ON CANTON, WHERE YOUR COLLATERAL ALREADY LIVES | So bring us the thing you can't sell in a hurry. There is no liquidation price. The math doesn't permit it. Medici — on Canton, where your collateral already lives. | The same asset from scene 1 returns, now split and still held. One gesture, then stop. |

Total: 132s.
