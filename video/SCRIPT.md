# The Deck Bake-Off — report, then the winning explainer

One video, one timeline, 22 scenes, **5:36 (336s)**, 1920×1080. No audio and no
TTS in this repo: the voice-over column is the narration to be spoken over a screen recording of
`explainer.html`, and the house `explainer-video` pipeline renders the mp4.

| Segment | Scenes | Runtime | What it is |
|---|---:|---:|---|
| **PART A** — the bake-off report as an explainer | 12 (`a1`–`a12`) | 208s | **Unbranded.** No house marks, no house palette, no house type. Set in report.pdf's own *Ordinal Field* look (`bakeoff/report-philosophy.md`): unprinted stock, iron-gall ink, one oxide accent; Young Serif / Lora / Geist Mono, base64-embedded. |
| **LEAD-IN** | 1 (`li`) | 8s | The hand-off. Reporting voice off, brand on. |
| **PART B** — the winning explainer, in full | 9 (`s1`–`s9`) | 120s | `winner/explainer/explainer.html`, **scenes copied verbatim**, its own Medici brand and IBM Plex faces kept and base64-embedded. |

**The one change made to PART B.** This copy is for public publication, so the per-frame footer
string reads **`Medici`** where the winner reads `Medici — Proprietary & Confidential`. It is a
one-token edit in the `.scene::after` rule and in the `deck-footer` meta; nothing else in the
winner's scenes, markup, timings, motion, palette or type is altered. Two mechanical merge
edits carry no visual change: the winner's `@font-face` blocks are re-pointed at the same four
woff2 files embedded as base64 (the file must be self-contained), and its `.scene` selectors are
narrowed to `.scene.b` so both parts can share one document. Every declared value is unchanged.

**Playback / review.** Auto-plays on load. `?scene=N` (1-based, across the whole timeline) starts
at a scene; `Space` pauses; `←`/`→` step scenes; `Home` restarts. `window.__player =
{scene, t, total, part, durations, seek(n), play(), pause()}`. The artifact reads
`window.SCENE_DURATIONS` (one float per scene, seconds) when the pipeline injects the measured
narration take, and falls back to the durations in this table otherwise; it sets
`document.body.dataset.done = "1"` when the timeline ends, which is the recorder's stop signal.
No network is touched: fonts and every screenshot are base64 inside the file.

**Voice-over.** ~150 wpm throughout; PART A + lead-in run 141–156 wpm per scene (540 words over
216s). PART B's narration is **copied verbatim** from `winner/explainer/SCRIPT.md` and is not
re-timed. Names: no personal names appear anywhere except *Ian*; co-founders are never named.

**Staging.** PART A and the lead-in are staged in `video/staging.yaml` (house `staging` skill v2,
video lane, `skills/messaging/staging/references/motion-roles.md`). PART B keeps the winner's own
staging (`messaging/staging/staging.yaml`, video lane) and is not restaged. The bold moment is
`a11` — one rupture in the whole of PART A — and its placement gate failure is recorded in
`video/staging.yaml`, not fudged.

---

## The talk track


| # | seg | id | start | dur | motion | subtitle (on-screen text) | narration (voice-over, verbatim) | what moves | screenshot source |
|--:|:--|:--|--:|--:|:--|---|---|---|---|
| 1 | A | a1 | 0:00 | 10s | hold | The Deck Bake-Off · 36 decks · 36 explainers · 9 review rubrics · 2 model judges | Six AI design tools and four messaging skills were given one product pitch, one source corpus, and one afternoon. This is what the reviewers found. | Nothing moves. The title plate is given whole on one still frame; the four counts settle beneath it in reading order and stop. | — |
| 2 | A | a2 | 0:10 | 22s | accumulate | 3 teaching goals · 1 corpus · no invented numbers · 6 × 2 × 3 = 36 tracks · 72 artifacts | One product pitch on tokenized real-world assets. Three teaching goals: what the product is, what it is worth, and how the mechanism works. Same corpus for everyone, no invented numbers. Then every tool rendered it twice — under a pinned house brand, and with no brand limits — against three messaging contracts. Thirty-six decks and thirty-six explainers. | A hairline bar grows left to right along the foot of the plate for the whole scene — the field filling, not a total announced. The contact sheet is already mounted when the scene opens. | `shots/canvas-design/brand/staging/deck-contact.png` |
| 3 | A | a3 | 0:32 | 13s | hold | staging · house messaging-guide · pitch-deck-mastery · presentation-writing | Four methods staged the argument first: the house staging skill, the house messaging guide, pitch-deck-mastery, and presentation-writing. Three produced the contracts the design layer rendered; the fourth arrived after the tracks were built. | Still list, read in order. The three rendered lanes mount beneath it one at a time, left to right, and stay. | `shots/canvas-design/brand/presentation-writing/slide-08.png` · `shots/canvas-design/brand/staging/slide-08.png` · `shots/canvas-design/brand/pitch-deck-mastery/slide-08.png` |
| 4 | A | a4 | 0:45 | 13s | assemble | canvas-design · algorithmic-art · impeccable · impeccable-polish · visual-explainer · html-ppt | The design field: Anthropic’s canvas-design and algorithmic-art; impeccable, as an author and as a finishing pass over the html-ppt baseline; visual-explainer; and html-ppt itself. This is slide eight — the mechanism — from all six. | Six specimens assemble in reading order, one every 1.4 seconds, and nothing that arrives ever leaves. The plate is complete and still for the last three seconds. | `shots/canvas-design/brand/staging/slide-08.png` · `shots/algorithmic-art/brand/staging/slide-08.png` · `shots/impeccable/brand/staging/slide-08.png` · `shots/impeccable-polish/brand/staging/slide-08.png` · `shots/visual-explainer/brand/staging/slide-08.png` · `shots/html-ppt/brand/staging/slide-08.png` |
| 5 | A | a5 | 0:58 | 12s | hold | 4 independent rubrics + 4 messaging skills · then 2 model judges · then Ian | Four independent rubrics graded every track — concept, accessibility, evidence, craft — plus the four messaging skills turned back on the design layer. Then two model judges wrote verdicts, before Ian formed his. | Held. The roster is read; only the contact sheet beside it fades up, once, at the end of the list. | `shots/canvas-design/brand/staging/explainer-contact.png` |
| 6 | A | a6 | 1:10 | 14s | hold | 30/30 decks · 30/30 explainers · 0/6 tools had a timeline | Thirty of thirty decks and thirty of thirty explainers rendered every slot and scene, in order, claims verbatim. And all six had to write the timed-explainer engine themselves — no design skill has a timeline. | Still. Two paragraphs settle, then the rendered scene mounts beside them and holds for the rest of the slot. | `shots/canvas-design/brand/staging/scene-06.png` |
| 7 | A | a7 | 1:24 | 16s | assemble | house-guide 8 · pitch-deck-mastery 9 · staging 10 · presentation-writing 13 | The messaging verdict. All four told the same story; only the emphasis and the order diverged. On rank sum — lowest wins — house-guide eight, pitch-deck-mastery nine, staging ten, presentation-writing thirteen. The call was staging as transport, house-guide as content gate. | The rank line assembles left to right, then the three lanes’ bold-moment frames mount together — the same scene number, three different arguments. | `shots/canvas-design/brand/staging/scene-04.png` · `shots/canvas-design/brand/presentation-writing/scene-04.png` · `shots/canvas-design/brand/pitch-deck-mastery/scene-04.png` |
| 8 | A | a8 | 1:40 | 31s | strain | brand: 1st on 4 of 5 rubrics, rank sum 4 of 4 · free: sums 9.5 – 16.5, no winner on rank | In brand mode there was one answer: canvas-design, first on four of five rubrics and a rank sum of four out of a possible four. It takes the run overall too, on nineteen across both modes. In free mode, nothing agreed. Every tool but one placed first on some rubric and last or nearly last on another; the sums span nine and a half to sixteen and a half. Reporting a winner there would be manufacturing one. | The consensus specimen mounts alone and holds for fourteen seconds, then the two free-mode specimens arrive beside it and the plate presses upward by a fraction and does not resolve. | `shots/canvas-design/brand/staging/slide-08.png` · `shots/impeccable/free/staging/slide-08.png` · `shots/html-ppt/free/staging/slide-08.png` |
| 9 | A | a9 | 2:11 | 15s | strain | 9 films of 10 · peak in the wrong place · 1 untraceable on-screen figure | Then the findings. Nine films of ten put their loudest frame somewhere other than their designated peak. And one tool printed a live render statistic where a measurement belongs — a value that appears nowhere in the corpus. | The strain continues from the previous scene without resetting: the two specimens rise a fraction and hold under load. | `shots/algorithmic-art/brand/staging/slide-08.png` · `shots/visual-explainer/brand/staging/scene-04.png` |
| 10 | A | a10 | 2:26 | 18s | strain | 1.85:1 provenance · 123 of 221 strings under 4.5:1 · 0 composition findings closed | The mandatory citation lines were set below the threshold of sight — as low as one point eight-five to one. Internal contract vocabulary reached the screen in four of six tools. And the finishing pass bought the whole craft floor while closing not one composition finding. | The load peaks: the plate strains upward across the whole scene, and the finished specimen holds beside it, unchanged from the baseline it refined. | `shots/impeccable-polish/brand/staging/slide-08.png` |
| 11 | A | a11 | 2:44 | 24s | rupture | 1 dropped fact in 30 decks · in the winning track · 4 rubrics ranked it first anyway | And then the one event that changes what the verdict means. The winning deck dropped a line — the roll-cost figure that drives the drift number printed on the same slide. The only fact missing from any of the thirty decks. Four rubrics ranked it first anyway; the fifth ranked it fourth, and the fifth is the only one that checked. | At six seconds the thirty specimen marks beside the slide collapse to the baseline in 320ms, one of them stays standing in oxide, and the frame goes still for the rest of the scene. The only break in PART A. | `shots/canvas-design/brand/staging/slide-11.png` |
| 12 | A | a12 | 3:08 | 20s | cadence | messaging · design · finish · review — plus the two checks nobody had written | The recommendation is a stack, not a favourite. Stage with staging, gate with the house messaging guide, draw with canvas-design under the brand, finish with a mandatory impeccable polish. Plus the two checks nobody had written: assert the bold moment is the measured peak, and diff the contract against the rendered text. | One gesture: the field of specimens opened in plate 02 returns as a single stack of four stages, settling top to bottom. Then it stops. | `shots/canvas-design/brand/staging/slide-01.png` |
| 13 | LEAD-IN | li | 3:28 | 8s | hold | The winning explainer · canvas-design · brand · staging · 9 scenes · 120s | What follows is the winning explainer — canvas-design under the Medici brand, staging’s messaging — as a prospect would see it. | One line, held, then the plate is given up: the registration frame and the apparatus fade out and the paper goes to black on the cut. | — |
| 14 | B | s1 | 3:36 | 10s | hold | Tokenized assets are on-chain, and mostly sitting still. · ISSUED · HELD · EARNING THEIR STATED YIELD AND NOTHING MORE | Tokenized treasuries, fund shares, gold: on-chain now, and mostly sitting still. Making one productive means accepting a liquidation price. There is a way that doesn't. | Nothing moves. The held field is given whole, on one still frame, so the promise in the third sentence lands on stillness. | `winner/shots/scene-1.png` |
| 15 | B | s2 | 3:46 | 10s | accumulate | Every venue that takes that collateral prices a liquidation threshold. · MORPHO RWA DEPOSITS · ~0 EARLY 2025 → $620M+ MARCH 2026 | Every venue that lends against these assets prices in a liquidation threshold. On Morpho, tokenized collateral grew from nothing to over $620 million in a year. | The bar field grows left to right across the whole scene — the climb is the figure, not its endpoint. The title lands over it. | `winner/shots/scene-2.png` |
| 16 | B | s3 | 3:56 | 10s | strain | This collateral cannot be sold in a single transaction. · NAV PRICING · MONTHLY REDEMPTION WINDOWS | But this collateral doesn't behave: NAV pricing, monthly redemption windows, no sale in a single transaction. So the market signs liquidation agreements with issuers. | The two halves load against each other: the continuous tick field presses right, the NAV steps hold, the frame strains and does not cope. | `winner/shots/scene-3.png` |
| 17 | B | s4 | 4:06 | 12s | rupture (peak) | In March 2020, MakerDAO collateral was auctioned for zero dollars. · ABOUT $8M OF COLLATERAL · CLEARED FOR $0 | Under stress, that machinery does exactly what it was built to do. March 2020: MakerDAO's collateral was auctioned for zero dollars. Around eight million dollars of it, sold for nothing. | At four seconds every proceeds mark collapses to the baseline in 320ms and the frame goes still for the rest of the scene. The only break in the film. | `winner/shots/scene-4.png` |
| 18 | B | s5 | 4:18 | 10s | hold | The problem is the mechanism, not the risk management. · CURATORS · LTV POLICY · DE-LEVERAGE FRAMEWORKS · SIGNED AGREEMENTS | Every fix since has been discipline: better curators, tighter frameworks, more paperwork. The mechanism is unchanged. It still has a threshold, and thresholds get breached. | Still. The patch stack is already in place when the scene opens; only the threshold line beneath it is left uncovered. Motion here would let the viewer off the previous scene early. | `winner/shots/scene-5.png` |
| 19 | B | s6 | 4:28 | 24s | assemble (peak) | P and N always sum back to the collateral. · NO UNDER-COLLATERALIZED STATE · NO THRESHOLD · NOTHING TO FORCE-SELL | Medici splits the collateral in two: P, protected, and N, amplified. At maturity one price is read against the strike. At or below it, P is worth the whole collateral, N nothing. Above it, P takes S over x, N takes the rest. They always sum to the collateral, at every price. No under-collateralized state. No threshold. Nothing to force-sell. | Reveal order follows the narration exactly: constant edge, P region, N region, strike, then a marker sweeps the whole price axis. Nothing that arrives ever leaves. | `winner/shots/scene-6.png` |
| 20 | B | s7 | 4:52 | 14s | hold | It settles where the collateral already lives, privately and atomically. · $344B REPRESENTED · $2T A MONTH IN REPO | It runs on Canton, where three hundred and forty-four billion dollars of real-world assets already sit. Positions are visible to their counterparties and no one else. Split, roll and settlement are single atomic transactions. | The field is already there when the scene opens; only the scoped envelope and the single settlement atom resolve into it. A turn of place, not of process. | `winner/shots/scene-7.png` |
| 21 | B | s8 | 5:06 | 18s | divest | P gives up everything above the strike, and nothing is on mainnet. · NET DRIFT −1.25%/YR · 9-YEAR BACKTEST · ETH · THIRD-PARTY | The cost is real. P is short a call above the strike: when the asset rallies, P's value declines, continuously and computably. Nine years of backtest put that drift at negative one and a quarter percent a year, on ETH. And nothing is on mainnet yet. | Subtractive only. The apparatus is removed a mark at a time until the decline curve and its two numbers are all that is left standing. | `winner/shots/scene-8.png` |
| 22 | B | s9 | 5:24 | 12s | cadence | Bring one tokenized position and argue with the payoff table. · IF THE MATH HOLDS, THE ASSET NEVER HAS TO BE SOLD | So this is not a pitch to allocate. Bring one tokenized position, and argue with the payoff table. If the math holds, the asset never has to be sold. | One gesture: the empty specimen slot from the opening field returns, whole and still held, and the payoff table settles beside it. Then it stops. | `winner/shots/scene-9.png` |

Total: **5:36 (336s)** — PART A 208s · lead-in 8s · PART B 120s.

---

## Sources

Every figure spoken or shown in PART A traces to one of these files; each is also printed in the
frame's own apparatus line, in the viewer's line of sight, per the house content gate.

| Figure on screen | Traces to |
|---|---|
| 6 design tools · 4 messaging skills · 2 brand modes · 3 messaging contracts | `README.md` “Contenders”, “How it ran” · `bakeoff/PROTOCOL.md` “Contenders” |
| 36 decks · 36 explainers · 36 tracks · 72 artifacts | `README.md` “Layout” · `shots/INDEX.md` “Summary” (36 directories, 72 artifacts) |
| the three teaching goals · same corpus · no invented numbers | `BRIEF.md` · `bakeoff/PROTOCOL.md` §Rules |
| every contender name, origin URL, version and licence | `bakeoff/CONTENDERS.md` |
| 9 review rubrics · 2 model judges, before Ian | `report.html` cover (“Nine review rubrics graded the result”) · `bakeoff/CONTENDERS.md` “Independent review rubrics (4)” · `README.md` “How it ran” |
| 30/30 decks and 30/30 explainers render every slot and scene, claims verbatim | `bakeoff/JUDGING-design-claude.md` §3 finding 7 · `report.html` §4.5 |
| no design tool has a timeline; all six built the engine themselves | `bakeoff/JUDGING-design-claude.md` §1 scoring convention, §3 finding 4 · `tracks/*/NOTES.md` |
| messaging rank sums 8 / 9 / 10 / 13; staging as transport + house-guide as gate | `bakeoff/JUDGING-messaging-claude.md` rev.2 §5, §7 |
| canvas-design 1st on 4 of 5 rubrics; rank sum 4 of a possible 4 | `bakeoff/JUDGING-design-claude.md` §2 (brand matrix), §4 |
| canvas-design overall on 19, against 22.5 and 23.5 | `bakeoff/JUDGING-design-claude.md` §4 |
| free-mode rank sums span 9.5–16.5, four tools inside two points | `bakeoff/JUDGING-design-claude.md` §2 “The dispersion is the result” |
| 9 films of 10 put their loudest frame off their designated peak | `bakeoff/JUDGING-design-claude.md` §3 finding 1 · `reviews/design/by-messaging-rubrics.md` |
| one untraceable on-screen figure (a live particle count in the evidence zone) | `bakeoff/JUDGING-design-claude.md` §3 finding 2 · `reviews/design/by-academic-pptx.md` |
| provenance at 1.85:1; 123 of 221 strings under the 4.5:1 floor | `bakeoff/JUDGING-design-claude.md` §3 finding 5 · `reviews/design/by-open-design-review.md` |
| internal contract vocabulary on screen in 4 of 6 tools | `bakeoff/JUDGING-design-claude.md` §3 finding 8 |
| the finishing pass closed not one composition finding, in either mode | `bakeoff/JUDGING-design-claude.md` §3 finding 6 |
| one dropped fact in 30 decks — the roll-cost line — in the winning track | `bakeoff/JUDGING-design-claude.md` §4 fix 1, §1 canvas-design/brand · `report.html` §5 |
| the recommended pipeline and the two missing five-line checks | `bakeoff/JUDGING-design-claude.md` §4 “Recommended house pipeline” · `bakeoff/JUDGING-messaging-claude.md` rev.2 §7 |
| every PART B number and every word of PART B's narration | `winner/explainer/SCRIPT.md` · `messaging/staging/staging.yaml` (video lane) |

Screenshots are the 2026-08-27 headless-Chromium capture in `shots/` and `winner/shots/`
(`shots/INDEX.md` records the run), downscaled to ≤1280px wide and base64-embedded. They are never
re-rendered: a re-render would no longer be evidence of what the rubrics judged.

## Description

A bake-off of six AI presentation-design skills and four messaging skills, all rendering the same
product pitch as a slide deck and as an animated explainer, in two brand modes — 36 decks and 36
explainers, graded by nine review rubrics. The first half is the read-out, unbranded, with a real
screenshot behind every claim. The second half is the artifact that won, played in full.
