# SCRIPT.md — Medici explainer · **presentation-writing** contract

Design contender **canvas-design**, mode **free**, movement **Invariant Field**.
Stage 1920×1080. Auto-plays on load. `?scene=N` jumps to a scene; **Space / →** advance,
**←** back, **P** pause, **R** restart. `window.__player = {scene, t, total, seek(n)}`.
No audio, no video, no TTS — this file is the narration record; Ian records the screen.

**Runtime 132 s over 8 scenes** — every duration is the contract's own `vo_seconds`,
unaltered. Narration below is verbatim from `messaging/presentation-writing/staging.yaml`.

| scene | start | dur | on-screen text | VO (verbatim) | what moves |
|---|---|---|---|---|---|
| `1` | 0:00 | 12 s | Real collateral, on a ledger, that nobody can sell in one transaction <br> A tokenized fund share. A gold bar with a ticker. | A tokenized fund share. A gold bar with a ticker. Real collateral, on a ledger — and none of it can be sold inside a single transaction. | The frame is given, not developed: the position arrives and holds. The piece has one loud moment and this is not it. |
| `2` | 0:12 | 18 s | Every venue prices that loan against a liquidation threshold anyway | Every venue that lends against it prices the loan against a liquidation threshold anyway. So the desks patch the gap by hand — signed liquidation agreements with the issuer, curator-run de-leverage frameworks, NAV instead of a market price. RedStone calls those fundamental design constraints, not edge cases. | Three patches stack over a gap they never close. One is prudence; three read as a workaround — which is why the accumulation needs the time. |
| `3` | 0:30 | 16 s | When the pathway runs, it runs at zero | And when the pathway actually runs, it runs at the worst possible price. On Black Thursday, MakerDAO collateral was auctioned for zero dollars. Eight million dollars of it. One forced sale sets off the next. | Forced sales grow continuously across the scene — a chain that feeds itself, not one event repeated — and the proceeds line stays at zero. |
| `4` | 0:46 | 12 s | Medici asks a different question | Medici asks a different question. Not how do we liquidate this safely — what if there were nothing to liquidate? Split the collateral instead. | Deliberately still. One question is struck through, the other is set beneath it. This is the quiet that scenes 3 and 6 are paid for with. |
| `5` | 0:58 | 20 s | One position becomes two claims that always add back to it <br> The oracle isn't even read until settlement. | One position becomes two claims. P is capped and income-bearing. N takes everything above the strike. P plus N always equals the collateral — closed form, at every price, enforced by the contract that records the split. The oracle isn't even read until settlement. | One object becomes two and nothing leaves the system: the tether holds while the parts separate, then the two widths are measured back against the whole. |
| `6` | 1:18 | 24 s | The liquidation line has nowhere to sit | At maturity there are two cases. At or below the strike, P is worth the whole collateral and N is worth nothing. Above it, P is the strike over the price; N is the rest. Now draw the liquidation line every other venue needs. There is nowhere on this axis to put it — no price under-collateralizes the vault. | The payoff assembles, a price marker sweeps the whole axis holding the sum at 1.00, then the threshold is drawn — and erased where it stands. The break is that the line cannot be placed. |
| `7` | 1:42 | 17 s | P is short a call, and the decline is the income | That is not free. P is short a call above the strike, so P's value falls continuously as the asset rallies — nine years of backtest put the net drift at minus one and a quarter percent a year. Never a cliff. | The persuasive apparatus is taken away and the cost is left standing alone. Motion is subtractive only. |
| `8` | 1:59 | 13 s | Bring us the thing you can't sell in a hurry | So bring us the thing you can't sell in a hurry. There is no liquidation price. The math doesn't permit it. Medici — on Canton, where your collateral already lives. | The asset from scene one returns, now split and still held. One gesture, then stop. |

## Motion contract

Motion is the argument, not decoration. Each scene's verb is the contract's own
`motion_role`, expressed in one shared vocabulary:

| role | how it is drawn in Invariant Field |
|---|---|
| `hold` | elements arrive and then nothing develops; the constant line never moves |
| `accumulate` | a value grows continuously and everything that arrives stays on screen |
| `strain` | members pull apart; connectors stretch and fail to reach |
| `rupture` | marks fall to a zero line; the alarm colour is spent here and nowhere else |
| `assemble` | one object becomes two and the tether between them stays visible |
| `arrest` | a gesture begins, stops mid-stroke, and is followed by dead stillness |
| `divest` | motion is subtractive only — the piece removes its own apparatus |
| `cadence` | one resolving gesture that answers scene 1, then stop |

The constant line sits at the same height (y = 236) on every scene of every film, and the
progress bar is two segments — elapsed warm, remaining cold — whose total width never
changes. That is the invariant, drawn, whether or not the payoff is on screen.
