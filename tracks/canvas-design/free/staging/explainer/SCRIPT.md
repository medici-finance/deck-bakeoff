# SCRIPT.md — Medici explainer · **staging** contract

Design contender **canvas-design**, mode **free**, movement **Invariant Field**.
Stage 1920×1080. Auto-plays on load. `?scene=N` jumps to a scene; **Space / →** advance,
**←** back, **P** pause, **R** restart. `window.__player = {scene, t, total, seek(n)}`.
No audio, no video, no TTS — this file is the narration record; Ian records the screen.

**Runtime 120 s over 9 scenes** — every duration is the contract's own `vo_seconds`,
unaltered. Narration below is verbatim from `messaging/staging/staging.yaml`.

| scene | start | dur | on-screen text | VO (verbatim) | what moves |
|---|---|---|---|---|---|
| `s1` | 0:00 | 10 s | Tokenized assets are on-chain, and mostly sitting still. <br> Tokenized treasuries, fund shares, gold. <br> Making one productive means accepting a liquidation price. | Tokenized treasuries, fund shares, gold: on-chain now, and mostly sitting still. Making one productive means accepting a liquidation price. There is a way that doesn't. | Nothing turns yet, on purpose. 344 marks arrive by rule and stop; the promise lands on a still image. |
| `s2` | 0:10 | 10 s | Every venue that takes that collateral prices a liquidation threshold. <br> On Morpho, tokenized collateral grew from nothing to over $620 million in a year. | Every venue that lends against these assets prices in a liquidation threshold. On Morpho, tokenized collateral grew from nothing to over $620 million in a year. | The climb draws continuously — the growth is the point, not the end number — then the threshold line is laid across it. |
| `s3` | 0:20 | 10 s | This collateral cannot be sold in a single transaction. | But this collateral doesn't behave: NAV pricing, monthly redemption windows, no sale in a single transaction. So the market signs liquidation agreements with issuers. | The position and the money market pull apart; the connectors stretch and do not reach. Load rises and visibly does not cope. |
| `s4` | 0:30 | 12 s | In March 2020, MakerDAO collateral was auctioned for zero dollars. | Under stress, that machinery does exactly what it was built to do. March 2020: MakerDAO's collateral was auctioned for zero dollars. Around eight million dollars of it, sold for nothing. | Eight marks fall to the proceeds line one after another and the zero rises. The only break in the film. |
| `s5` | 0:42 | 10 s | The problem is the mechanism, not the risk management. | Every fix since has been discipline: better curators, tighter frameworks, more paperwork. The mechanism is unchanged. It still has a threshold, and thresholds get breached. | The direction of the film turns while the frame stays still: three procedural fixes are struck out and the threshold does not move. |
| `s6` | 0:52 | 24 s | P and N always sum back to the collateral. | Medici splits the collateral in two: P, protected, and N, amplified. At maturity one price is read against the strike. At or below it, P is worth the whole collateral, N nothing. Above it, P takes S over x, N takes the rest. They always sum to the collateral, at every price. No under-collateralized state. No threshold. Nothing to force-sell. | Reveal order follows the narration exactly: split, the price read, each branch, then the flat sum line. Everything that arrives stays on screen. |
| `s7` | 1:16 | 14 s | It settles where the collateral already lives, privately and atomically. | It runs on Canton, where three hundred and forty-four billion dollars of real-world assets already sit. Positions are visible to their counterparties and no one else. Split, roll and settlement are single atomic transactions. | The same 344-mark field as scene one, now with one position enclosed and lit. The frame settles rather than develops. |
| `s8` | 1:30 | 18 s | P gives up everything above the strike, and nothing is on mainnet. | The cost is real. P is short a call above the strike: when the asset rallies, P's value declines, continuously and computably. Nine years of backtest put that drift at negative one and a quarter percent a year, on ETH. And nothing is on mainnet yet. | Subtractive only. The film removes its own apparatus and the decline curve is left standing alone with its measured drift. |
| `s9` | 1:48 | 12 s | Bring one tokenized position and argue with the payoff table. | So this is not a pitch to allocate. Bring one tokenized position, and argue with the payoff table. If the math holds, the asset never has to be sold. | The position from scene one returns, split and still held. One gesture, then stop. |

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
