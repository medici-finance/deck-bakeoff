# Medici for RWA tokens — presentation-writing — explainer script

Messaging contract: `messaging/presentation-writing/staging.yaml` (video lane, 8 scenes, 132 s). Design: `algorithmic-art`, brand mode. Scene order, claims, VO text and durations are the contract's, unchanged.

Runtime **132 s**, 8 scenes. Durations are the messaging contract's
`vo_seconds`, unchanged. No audio ships with the file: the VO column is what a
narrator reads while the scene is on screen.

Playback: `explainer.html` auto-plays on load. `?scene=N` jumps to a scene;
`→` / `←` step; `Space` re-runs the current scene. `window.__player`
(`{scene, t, total, seek(n), play(), pause()}`) is exposed for tooling.

**What is moving.** Every frame is one run of the *Conserved Entry* field
(`brand/PHILOSOPHY.md`): 1000 particles, fixed before the first frame, never
created and never respawned. The `census` readout in the corner is struck from
the live particle count, not from a formula — P, N and their sum are what the
population actually is at that instant. That is why exactly one scene can afford
to break it.

| # | Scene | Start | Dur | On screen | VO (verbatim from the contract) | What moves |
|---|-------|-------|-----|-----------|----------------------------------|------------|
| 1 | `w1` | 0:00 | 12s | Real collateral, on a ledger, that nobody can sell in one transaction | A tokenized fund share. A gold bar with a ticker. Real collateral, on a ledger — and none of it can be sold inside a single transaction. | One undivided population, idling. The frame is given, not developed; the census sits at Σ 1.000 and never moves. The film's loud moment is not here. |
| 2 | `w2` | 0:12 | 18s | Every venue prices that loan against a liquidation threshold anyway / signed agreements · de-leverage frameworks · NAV pricing | Every venue that lends against it prices the loan against a liquidation threshold anyway. So the desks patch the gap by hand — signed liquidation agreements with the issuer, curator-run de-leverage frameworks, NAV instead of a market price. RedStone calls those fundamental design constraints, not edge cases. | Comfort turns into load. The threshold rule fades in and the field's turbulence climbs against it; the population visibly stops settling. Three patches accumulate on screen as the strain rises — one is prudence, three is a workaround. |
| 3 | `w3` | 0:30 | 16s | When the pathway runs, it runs at zero / $8M of collateral, auctioned for $0 | And when the pathway actually runs, it runs at the worst possible price. On Black Thursday, MakerDAO collateral was auctioned for zero dollars. Eight million dollars of it. One forced sale sets off the next. | THE ONE BROKEN LAW, played as accumulation rather than a single break: the annihilation rate itself accelerates (cubic), so each removal visibly makes the next one faster — one forced sale setting off the next. The census runs down to Σ 0.000 and says “conservation off”. |
| 4 | `w4` | 0:46 | 12s | Medici asks a different question | Medici asks a different question. Not how do we liquidate this safely — what if there were nothing to liquidate? Split the collateral instead. | Deliberately still. The population is whole again and barely moving; this is the quiet that scene 3 and scene 6 are paid for with. |
| 5 | `w5` | 0:58 | 20s | One position becomes two claims that always add back to it | One position becomes two claims. P is capped and income-bearing. N takes everything above the strike. P plus N always equals the collateral — closed form, at every price, enforced by the contract that records the split. The oracle isn't even read until settlement. | One object becomes two and nothing leaves the system. The field reorganises into the ledger and the driving price crosses the strike; particles change allegiance in rank order, so the parts are watched arriving and staying. The top edge — the sum — does not move. |
| 6 | `w6` | 1:18 | 24s | The liquidation line has nowhere to sit | At maturity there are two cases. At or below the strike, P is worth the whole collateral and N is worth nothing. Above it, P is the strike over the price; N is the rest. Now draw the liquidation line every other venue needs. There is nowhere on this axis to put it — no price under-collateralizes the vault. | The threshold from scene 2 is drawn onto the payoff and then cannot be placed: it fades as a scan crosses every price looking for a column that sums to less than one, decelerates, and dissolves without arriving. The population is untouched throughout — the census holds Σ 1.000 while the search fails, which is the whole argument. |
| 7 | `w7` | 1:42 | 17s | P is short a call, and the decline is the income / −1.25%/yr net drift over nine years | That is not free. P is short a call above the strike, so P's value falls continuously as the asset rallies — nine years of backtest put the net drift at minus one and a quarter percent a year. Never a cliff. | Subtractive only: the blue band dims continuously while its count stays fixed. No cliff anywhere in the motion — the decline is a slope, and the film removes its own apparatus to show it. |
| 8 | `w8` | 1:59 | 13s | Bring us the thing you can't sell in a hurry / There is no liquidation price. The math doesn't permit it. | So bring us the thing you can't sell in a hurry. There is no liquidation price. The math doesn't permit it. Medici — on Canton, where your collateral already lives. | The asset from scene 1 returns, split and still held: the two populations recombine into one and the scan crosses once more and dissolves. One gesture, then stop. |
