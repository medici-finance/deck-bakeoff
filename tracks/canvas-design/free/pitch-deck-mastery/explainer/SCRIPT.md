# SCRIPT.md — Medici explainer · **pitch-deck-mastery** contract

Design contender **canvas-design**, mode **free**, movement **Invariant Field**.
Stage 1920×1080. Auto-plays on load. `?scene=N` jumps to a scene; **Space / →** advance,
**←** back, **P** pause, **R** restart. `window.__player = {scene, t, total, seek(n)}`.
No audio, no video, no TTS — this file is the narration record; Ian records the screen.

**Runtime 143 s over 8 scenes** — every duration is the contract's own `vo_seconds`,
unaltered. Narration below is verbatim from `messaging/pitch-deck-mastery/staging.yaml`.

| scene | start | dur | on-screen text | VO (verbatim) | what moves |
|---|---|---|---|---|---|
| `1` | 0:00 | 13 s | Your tokenized collateral has a price at which someone else sells it. | You hold a tokenized position — a fund share, a treasury, a bond. The moment you finance it, somewhere in the paperwork there is a price at which somebody else sells it. | The position is given, then the marked price is planted — the same price scenes 2 and 5 both act on. |
| `2` | 0:13 | 22 s | When the threshold breaks, the position is sold at the worst price. | That is a liquidation threshold. Price crosses it, and the collateral is sold into the fall. On Black Thursday, eight million dollars of collateral cleared for zero. Tokenized assets are worse — most cannot be sold in one transaction, so the market signs liquidation agreements with issuers to do it by hand. | The price path is drawn, crosses the threshold, and the seizure follows: the break has to be seen happening for scene 5's refusal to mean anything. |
| `3` | 0:35 | 20 s | Medici splits one position into two claims: Protected and Amplified. | Medici does something else with the same collateral. It splits the position into two claims. Protected takes the value at or below a strike you choose. Amplified takes everything above it. Both are issued atomically, and both stay claims on collateral that never leaves the vault. | One object becomes two that remain one — the tether persists visibly as the parts separate. |
| `4` | 0:55 | 21 s | At maturity, P takes S/x, N takes the rest, and the two still sum to the collateral. | At maturity, one reference price is read. At or below the strike, Protected takes the full collateral value and Amplified takes nothing. Above it, Protected takes S over x and Amplified takes the rest. Sweep the price across the whole range: the two always add back to exactly the collateral. | A reference-price marker sweeps the whole axis with a live SUM = 1.00 readout. The point is the sweep, not any single price. |
| `5` | 1:16 | 21 s | The price rises, and the liquidation that would fire does not exist. | Now run that first scene again. Price moves hard against the Protected side. A lending market would seize the collateral here. Watch. [2 s hold] Nothing fires. There is no liquidation threshold, because the payoff has no under-collateralized state to trigger one. A theorem, not a risk setting. | Scene 2's gesture starts identically — the price runs, the seizure line begins to be drawn — and stops mid-stroke. Then 2.5 seconds in which nothing on screen moves at all. The absence is the motion that does not complete. |
| `6` | 1:37 | 17 s | Two holders, two reasons: income kept, exposure amplified. | Each leg has an owner who wants it. A fund treasury holds Protected and earns on an asset it never sells. An allocator holds Amplified for exposure with no liquidation price and no funding rate. Selling a leg is the liquidity. | Deliberately still: the quiet that pays for scene 5. A viewer recovering from the bold moment should be reading, not tracking. |
| `7` | 1:54 | 14 s | What is built is real; what is not built is named. | What exists today: fifty-four DAML contracts on Canton, a twelve-agent fleet, a nine-year backtest, closed-form proofs. What does not: mainnet, an audit, live collateral, a customer. You should hear that from us. | The register turns from persuasion to disclosure. Nothing new enters; the not-built column arrives as hollow marks. |
| `8` | 2:08 | 15 s | Bring one position, and the split is modelled against it. | Medici splits a tokenized asset into two claims that always sum back to it, so the position can never be force-sold. Bring one position and a strike; we will show you the payoff at every price. | The single position from scene one returns, now split and summing. One gesture, then stop — not a summary of the film. |

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
