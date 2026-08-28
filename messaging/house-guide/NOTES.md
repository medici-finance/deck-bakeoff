# NOTES — house-guide messaging contender

**Contender**: `skills/messaging/house-guide/messaging-guide.md` — the Assay comprehension-diagnosis
and messaging-fix method (v0.1, 2026-07-17), applied to Medici for RWA.
**Run date**: 2026-08-27.

---

## 1. Time to artifact

| Phase | Wall clock | Notes |
|---|---|---|
| Read: BRIEF, method guide, both pitch decks, both research docs, brand §0/§8, staging contract + both closed vocabularies + one field template | 19:03 → 19:08 | ~2,400 lines. The method itself is 127 lines and cost about a minute of that. |
| `messaging-guide-medici.md` (the seven sections) | 19:08 → 19:11 | The number gate (§7) took the largest single share, because it is the only section that required re-deriving arithmetic rather than composing prose. |
| `messaging.md` | 19:11 → 19:13 | Almost entirely distillation — every line already existed in the native artifact. |
| `staging.yaml` + parse/arithmetic validation | 19:13 → 19:17 | Deck lane and video lane, then a scripted check of the word/second/energy arithmetic. |
| `NOTES.md` | 19:17 → 19:21 | |
| **Total** | **~18 minutes** | Single pass. Nothing was rewritten after the fact except two word counts. |

The method is unusually cheap to run because §1 is a *diagnosis of existing material* — the first
pass over the corpus produces both the understanding and the deliverable at once. Every other
messaging approach I know reads the corpus, forms a view, and then starts writing; here the reading
IS section one.

## 2. Friction

- **The method has no transport format.** It emits prose sections, not a contract. The bake-off's
  `staging.yaml` had to be built by mapping the method's outputs onto a *different* skill's field
  names. That mapping was clean but it is not free, and it is the method's largest structural gap:
  §2 (the 30-second version), §4 (the demo narrative) and §7 (the number gate) each contain enough
  to generate a deck, and none of them says in what order or how many slots.
- **§4's demo narrative assumes a live product.** The Assay version stages a live tamper on a
  running system with real users. Medici has a development cluster, no users, and nothing that can
  be demonstrated *happening to someone*. The narrative had to be re-based onto a parameter walk of
  the published payoff, which is honest but thinner — and it moved the emotional peak from "watch
  the system catch a cheat" to "watch us show our own loss".
- **§1's diagnosis wants live surfaces.** It was written against a web teaser, an exec brief and a
  README — copy that a reader hits cold. The Medici corpus is two *presenter-narrated* decks, so
  several failures (B1, B2) had to be judged on slide headlines and the deck's opening slide rather
  than on a page a reader lands on. B6 (no before/after) transferred perfectly. B3 and B9 transferred
  so exactly that they diagnose the same slide in both decks.
- **The corpus fights itself on the flagship use case.** The decks sell tokenized fund shares and
  MMFs as the RWA use case; the research document concludes that near-zero-volatility collateral is
  the worst possible underlying for an options split and names tokenized gold first. The method has
  no procedure for a corpus that contradicts itself, so I invented one: name the requirement
  (volatility), refuse to promise the split works on an MMF, and let the buyer name the underlying
  (deck slot d12). The messaging is honest under either reading of the corpus, which is the most a
  messaging pass can do without a human ruling.
- **Word-count discipline is on the author, not the method.** The video lane's arithmetic
  (110s × 150 wpm = 275 words) came from the staging contract, not from the house guide. Left to
  itself the method would have produced a 30-second version that runs 100 seconds — which is
  exactly what its own worked example does.

## 3. Where an Assay-specific rule did not transfer

**(a) The banned-framings rule collides head-on with the house brand.** The method's B8 says to
replace absolute claims ("un-forgeable", "impossible") with narrower defensible ones. The Medici
brand guide §8.1 principle 4 says the opposite, by name: *"'Can't be liquidated' is a statement of
mathematical fact. We don't hedge it with 'designed to resist' or 'aims to prevent.'"* Both are
right, and the resolution is a **scope** rule rather than a hedging rule: the liquidation claim is
true of the *payoff function* and is stated flat and unhedged; what must be banned is its silent
widening to the *system* — "forced-liquidation risk: zero" and "counterparty risk: none" as rows in
a risk table about unaudited software, and "the mechanism is de-risked". This is the single largest
adaptation in the run and it is written up as B8 in `messaging-guide-medici.md` §1. Anyone reusing
the method in a house with a strong tone canon should expect this collision and should resolve it
the same way: hedge nothing, scope everything.

**(b) §6 assumed one external category with one citable lineage.** Assay could adopt "harness
engineering" — a named category with a dated essay and an anthology. RWA has **two** relevant
lineages at **two different layers** and **no coined name** for the thing Medici is: the mechanism's
lineage is Vitalik Buterin's "Options Instead of Debt" (2025, cited on asset-manager Slide 3) and the
category's is RedStone/Credora's "productive collateral" (Part 2, 2026-03-26). The method's rule —
adopt the category, don't re-coin a synonym — had to be applied twice, and the positioning line
became a *position within* a borrowed category rather than a re-labelling of it: "the
productive-collateral design with no liquidation pathway". The method survives the transfer; its
single-lineage assumption does not.

**(c) §5's glossary assumed naming freedom the brand has already spent.** Assay's glossary is half
renames ("brief" → "work order", "stream" → "workstream"). Medici's brand guide §8.2 is an existing
terminology canon with reasons attached — Protected/Amplified not "stable"/"leverage", split/recombine
not mint/burn, drift not impermanent loss — and it outranks a messaging pass. So the glossary became
almost entirely **gloss discipline over a fixed canon**, with exactly one outright drop
("primitive", "synthetic asset", "protocol-grade") and one rename ("sub-transaction privacy" → "your
position is visible to you and your counterparty, not to the market"). The method's *standing rule*
(one gloss per novel term, at most one unglossed novel term per sentence) transferred with no
modification and is the single highest-value line in the whole method for this corpus: it alone
would have caught the nine-term table on asset-manager Slide 3.

**(d) The "aha in minute one" inverted differently.** Assay's inversion is *problem → catch →
machinery*, where the catch is the system detecting a cheat. Medici has no adversary and no
detection event, so the catch had to become the product's own loss, staged deliberately. That is a
genuinely different dramaturgy — Assay's peak is the system working, Medici's peak is the seller
disclosing — and the method's underlying principle ("adverse evidence sells harder than any
dashboard") is what carried across, not the shape.

**(e) The "30-second version" label does not survive its own arithmetic.** The method's worked
example is ~250 words, which is 100 seconds at any speaking pace. I wrote a real one (79 words,
32 seconds) and kept the longer passage as a labelled 90-second extension. Recommend the method fix
its own example.

## 4. Questions a human would have had to answer — and how they were answered from the corpus

Nothing in this run stalled on a human. Every open question was closed against the corpus, and the
provenance of each answer is recorded here.

| # | Question | Answer used | Provenance |
|---|---|---|---|
| Q1 | Is the contract set 54 templates / ~5,700 LOC or 36 / ~5,100? | **Unanswerable — withheld from every artifact.** Both figures are stated as fact in same-dated (2026-07-04) sources with no reconciliation. Outbound copy says "the contract set". | canton Slide 9 vs asset-manager Slide 12. Same conflict in the compliance analysis: 2,900 lines vs 2,600 lines. **This one needs a human**; it is the only question in the list I could not close. |
| Q2 | What is full-period gross theta, and why does the deck quote a sub-period? | **Not published; withheld.** The corpus gives net drift −1.25%/yr and roll cost −1.2%/yr, so full-period gross implies ≈ **−0.05%/yr** — near zero, which is why only the best sub-period (+0.57%/yr, 2021–22) appears on a slide. The deck labels the sub-period honestly; the messaging simply does not use either number, because a reader cannot bridge them. | asset-manager Slide 3, both rows; arithmetic mine. Flag for a human: if the implied figure is right, the "income" framing rests on execution improving, not on the backtest. |
| Q3 | Is the flagship RWA underlying tokenized fund shares/MMFs or tokenized gold? | **Neither is asserted.** The messaging names the *requirement* (an options split needs volatility) and lets the buyer name the underlying; objection O2 concedes outright that a money-market share is the weakest case in the set. | canton Slide 7 and asset-manager Slide 6 (fund shares) vs `rwa-redstone-2026.md` takeaway 2 in both passes (gold first; T-bills a poor underlying; Morpho T-bill deposits −92% while gold grew 7×). |
| Q4 | Does the artifact carry the funding ask ($5–50M strategic; Canton Foundation funding)? | **No.** The brief rules the ask is a conversation, so both capital asks are cut and slot d12 asks for an hour on one named underlying. | BRIEF.md §"Audience + the three educational goals"; asset-manager Slide 13; canton Slide 11. |
| Q5 | Can we say mainnet Q4 2026? | **Only as a dated intention.** The source is the July 2026 plan and today is 2026-08-27, so it ships as "targeted, as-of the July 2026 plan" and never as a commitment. | canton Slide 12; BRIEF.md ("statements of roadmap/timing are as-of the source's date; mark them as such"). |
| Q6 | May Franklin Templeton, WisdomTree, Invesco and BlockBooster appear? | **No — they appear on no slot and in no scene.** In the corpus they are target market and "pilot conversations"; on a slide they read as customers, and that implied claim is larger than any number on the page. | canton Slides 7, 11. |
| Q7 | Is the $8M Black Thursday figure usable? | **The event and date ship; the figure does not.** It appears in one source deck with no external citation and the second deck tells the same story without it. | canton Slide 2 vs asset-manager Slide 2. |
| Q8 | Which competitor is the benchmark — Figure or Aave Horizon? | **Aave Horizon.** The corpus revises itself explicitly on this point after reading Part 2 of the RedStone report. | `rwa-redstone-2026.md`, "What changes in the Part 1 analysis". |

## 5. What the method could not express

- **No transport contract, as above.** The method ends at prose. Everything downstream — slot count,
  slot function, ordering, timing, per-scene motion — came from the staging contract's field names,
  not from the method. Applied on its own it would hand a designer six pages of excellent copy and
  no structure, which is precisely the failure mode §1 diagnoses in other people's material.
- **No place to record a number that fails.** §7 governs numbers that trace; it has no verdict for a
  number that traces to *two sources that disagree*, which is the first thing this corpus produced.
  Three standing rules were added at the end of §7 to cover it (conflict ⇒ withhold both; prospect
  names are claims; roadmap dates decay faster than figures).
- **No two-audience mechanism.** The brief's audience is a holder *and* an issuer *and* a BD person
  who retells it. The method assumes a single reader and offers one lever for the difference — "best
  openers by audience" in §3. Everything else (the pillars, the 30-second version, the demo) had to
  serve all three at once. A holder wants to know what happens to their asset; an issuer wants to
  know what it does to their fund's distribution; the artifacts here answer the first well and the
  second only through objection O5.
- **No decay model.** Every figure in this corpus has an as-of date and two of the most useful ones
  are five months old. The method's freshness checklist is a pre-publication ritual ("re-dereference
  at post time"), not a property carried on the claim. For a pitch that will be presented repeatedly
  over months, the as-of date needs to live *in* the claim, which is a rule I added rather than
  inherited.
- **No ownership of an objection over time.** §3's honest breaks and §5's banned framings are
  authored once. Nothing in the method says who re-checks, when, or what happens when the answer
  changes — e.g. objection O4 ("not audited") becomes false the day an audit lands, and at that
  moment several lines in three files are wrong simultaneously.
- **Nothing about who is allowed to say it.** Assay's method assumes the author is the operator.
  Medici's material is presented by three founders to institutions, and the difference between "we
  have not been audited" said by a founder and written on a slide is real. The method has no register
  control, and the two source decks would have benefited from one.
