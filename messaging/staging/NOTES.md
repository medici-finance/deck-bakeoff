# NOTES — messaging contender `staging`

Skill: `skills/messaging/staging/SKILL.md` (v2, 2026-08-18), read end to end, plus
`references/audience.md`, `slide-functions.md`, `transitions.md`, `motion-roles.md`,
`references/genres/executive-explainer.md` (the chosen playbook, read in full),
`references/genres/technical-deep-dive.md` (selection + bold-moment + time-shape sections, for the
rejection), `references/genres/STUBS.md`, and `references/seam-gate.md`.

## 1. Time to artifact

| Marker | UTC |
|---|---|
| Start (first tool call) | 2026-08-27 23:24:41 |
| Deliverables complete | 2026-08-27 23:35:13 |
| **Elapsed** | **~10.5 minutes** |

Rough split: ~4 min reading the skill + references + genre playbook, ~3 min reading the corpus
(five source files, brand §0 and §8), ~3.5 min staging and writing the three artifacts. Two
mechanical fixes after the first write (VO word budget overrun on scene 6; declared-vs-actual word
counts), both caught by running the numbers rather than by re-reading.

## 2. Flow, as run

`INTAKE (skipped) → CLASSIFY → LOAD → STAGE (5 passes) → GATE → HANDOFF`.

- **INTAKE skipped**, and said out loud in `staging.yaml`: the brief names the audience, the
  judgment they hold, both media and both time budgets. No questions were put to a human; every
  remaining gap is a recorded assumption (§4 below and `assumptions:` in the contract).
- **CLASSIFY**: chose `executive-explainer`, rejected four with the specific `pick_when` each
  fails; `technical-deep-dive` contributes one named beat (`cost`).
- **LOAD**: one playbook, kill conditions checked before staging anything. None fired.
- **STAGE**: arc → slots → claims → bold moment → motion allocation (video only, including the
  EVENT/CONDITION peak walk and the ornament cut).
- **GATE**: all deck gates and all staging-owned video gates pass with their arithmetic shown;
  three video gates are design-lane and are recorded **NOT RUN** rather than fudged (§5).

## 3. Validator / tool run

`skills/messaging/staging/tools/seam-gate.mjs` — **not applicable at this layer, not run.**
It is a numeric verifier for *rendered* scene boundaries: it needs `--ledger seams.json`, a
`--comp-url file://…/explainer.html`, and a page exposing `window.__player` / `__playerReady` /
`__renderReady`. None of those exist in a messaging deliverable — the film has not been authored
yet, and authoring it is the design contender's job. Environment is ready for whoever does run it:
**node v26.7.0** present (the script requires ≥ 22 and a local Chrome). The seam *boundaries* it
would check are named in `video.transitions` in `staging.yaml`; the ledger is design's to declare.

What I did run instead, because a staging contract should be machine-checkable:

| Check | Result |
|---|---|
| `staging.yaml` parses as YAML (`python3 -c "import yaml…"`) | PASS |
| Every headline claim ≤ 12 words (brief's constraint) | PASS — 23 claims, longest 12 |
| Every scene's declared `words` == actual VO word count | PASS after one fix (s6 was 68 against a 60-word slot) |
| Scene seconds sum to the stated runtime | PASS — 120s exactly |
| VO word budget ≤ 150 wpm × runtime | PASS — 299 words against a 300-word budget |
| Per-scene delivery rate ≤ ~160 wpm | PASS — range 144–156 wpm |
| Motion budget arithmetic (mean energy, quiet share, ceiling order, adjacency) | PASS — mean 2.33 ≤ 3.0; 3 of 9 scenes ≤ 1.5 (33%); no adjacent peaks |

## 4. Questions the skill would have put to a human — answered here, with provenance

The skill's rule is that anything beyond the three INTAKE questions is a **recorded assumption, not
a question**. These are the twelve that came up, each answered from the corpus.

1. **"Who is in the room and what decision do they hold?"**
   RWA issuers, tokenization platforms, asset managers and their risk/product leads, plus
   chain-ecosystem BD introducers. They hold a **credibility judgment plus the authority to grant a
   conversation** — not a resource decision. *Provenance: `BRIEF.md` §Audience ("the ask is a
   conversation, not funding").* This is the fork `executive-explainer` warns about most loudly, so
   the ending is an invitation to engage, never an approval ask.

2. **"How long, and presented or read?"**
   Deck 10–14 slides / ~10 minutes; film 90–150s. Declared **presented-primary, read-fallback** —
   a pitch deck of this kind is presented once and forwarded ten times, and `audience.md` says to
   stage for read and let delivery subtract. Consequence: every headline claim is a complete
   sentence. *Provenance: `BRIEF.md` §Audience; `references/audience.md` "The fork".*

3. **"What must they believe, in one arguable sentence?"**
   *"Forced liquidation is not a risk to be managed on tokenized collateral — it is a mechanism
   that can be removed, and removing it is what makes a tokenized asset productive."* Arguable: a
   risk lead can disagree (and objection 1 is exactly that disagreement). *Provenance:
   `canton-pitch-deck.md` Slide 2 ("liquidation is the mechanism. Remove it, and you remove the
   entire category of failure") + the brief's three educational goals.*

4. **"Is there an instance of the cost, ideally one that happened to us?"**
   No Medici incident exists — there has never been live collateral (`canton-pitch-deck.md`
   Slide 9). The strongest available named, dated instance is **Black Thursday, March 2020:
   MakerDAO collateral auctioned for $0, ~$8M of it** (`canton-pitch-deck.md` Slide 2;
   `asset-manager-pitch-deck.md` Slide 2). Used as the bold moment, with the "not ours" caveat
   recorded in `assumptions:`.

5. **"The two decks disagree on what is built — which count is true?"**
   `canton-pitch-deck.md` Slide 9 says **54 DAML templates / 9 modules / ~5,700 LOC**;
   `asset-manager-pitch-deck.md` Slide 12 says **36 templates / ~5,100 LOC**. Both are dated
   2026-07-04 (the asset-manager deck reframed 2026-07-18, i.e. *later* with the *lower* number).
   Resolved by the brief's stated source priority — canton deck first — and flagged rather than
   reconciled. The same split exists on the compliance memo (**~2,900** vs **2,600** lines) and is
   resolved the same way. **This is a genuine open question for a human**; a reader who has both
   decks will notice.

6. **"Video length — 150s or 120s?"** The brief allows 90–150s; the playbook's video `max` is 120s
   and its `ideal` is 90s. Staged at **120s**, which satisfies both. Recorded what a 150s cut would
   buy (a second proof scene, not a longer mechanism).

7. **"Is P the 'stable-ish' leg?"** The brief says stable-ish; the house terminology canon
   (`house-brand-guide.md` §8.2) forbids "stable" for P because P drifts. Resolved in favour of the
   brand: **Protected Token / P**, **Amplified Token / N**. Content unchanged, vocabulary corrected.

8. **"Which RWA underlying should the piece name?"** Tokenized **gold**, not treasuries: on Morpho,
   T-bill collateral fell 92% from a ~$194M peak while gold grew 7x at a conservative ~40%
   borrow-to-collateral ratio, and an options split needs volatility.
   *Provenance: `rwa-redstone-2026.md`, Part 2 addendum + updated takeaway 2.* It appears in the
   ask slot and in objection 2, not in the mechanism, because it is a parameterization choice.

9. **"Do we carry the sources' capital asks?"** No. Both decks end on money (Foundation funding;
   $5–50M strategic + $10–25M pilot). Carrying either would have fired the genre's *"the ask is
   capital → re-CLASSIFY as investor-pitch"* kill condition. Cut, not softened.

10. **"14 slots or 11?"** The playbook's ideal is 11 slots at 6 minutes; the brief says 10–14 at
    ~10 minutes. Staged at 14, which keeps 50s/slot — above the 40s floor. Recorded which slots a
    6-minute cut should drop first (d5, then d10).

11. **"Should the comparison slot concede a row?"** Yes. `audience.md` lists *"a comparison table
    where you win every row"* as the buyer's reflex distrust, so d9 states where the incumbent
    wins: $620M+ of live RWA deposits, an operating history, an existing borrower base — against
    Medici's zero live users. Same reason d4/d5 put the problem in RedStone's words, not ours.

12. **"How deep does the mechanism go?"** One slot, one nameable structural property (the payoff
    identity). The brief's educational goal 3 wants more than that surface — the split, the
    invariant, and maturity behaviour above and below strike — so the payoff identity carries all
    three as *arithmetic on one slot*, and "what changes operationally" moves to the comparison
    slot behind it. Four mechanism slots would have failed the genre's `one-mechanism` gate and its
    "four mechanisms explained, none remembered" anti-pattern.

## 5. Friction — where the skill fought the brief, and what it cost

- **The deck bold-moment window drove the slot count.** `placement_deck` is 40–50% by index, and
  the bold moment must be the last problem beat. That is a constraint on *arc length*, not on
  emphasis: at 12 slots it lands at 41.7%, at 13 slots at 38.5% (out of window), at 14 slots at
  42.9%. The arc is 14 slots partly because 14 is the count at which two volunteered-limit slots
  and a compliant bold placement coexist. Defensible, but the arithmetic led the argument for one
  pass, which is the exact failure mode `motion-roles.md` R6 was written about in the other lane.
- **`mechanism: ONE slot` vs "one diagram they could redraw".** The genre is right that four
  mechanism slots produce no memory, and the brief is right that the payoff behaviour is the
  deliverable. Resolved as above; it is the tightest slot in the deck and the most likely place a
  design contender asks for a split. If one is needed, the split is *claim on d8, payoff table
  beside it* — same slot, two surfaces, which the composition contract explicitly permits.
- **Three of the ten video gates cannot be run by this layer.** `motion-spec-locked`,
  `seams-declared` and `render-and-look` all require an authored film. They are recorded as
  **NOT RUN** with the reason, not as pass. The skill is clear that a failed gate names the step to
  return to; it is less clear what a *staging-only* run should do with gates that belong to the
  design step. Recording them as NOT RUN with the owner named is the reading I took, and the
  design contender should treat all three as inherited work items.
- **Corpus contradiction handling has no home in the schema.** Item 5 above (54 vs 36 templates) is
  the sort of thing a staging pass discovers and a design pass must not silently pick a side on.
  It went into `assumptions:` and into this file; a `provenance_conflicts:` block would be the
  right field.
- **Reading the video-lane word budget as a hard gate caught a real error.** The first draft of
  scene 6 was 68 words in a 60-word slot — 13% over, which at 150 wpm is a scene that either
  overruns its own motion or is delivered fast at the exact moment the audience is being asked to
  memorise arithmetic. The skill's line that *on a film the time gate writes the script* is
  accurate, and it is the single most useful thing in the video lane.

## 6. What the skill could not express (and where it went instead)

| Thing the brief needed | Why the schema has no field | Where it went |
|---|---|---|
| Per-slot **source citation** | Not in the HANDOFF schema at all | Added `source:` to every slot and scene — an extension, flagged here |
| Per-slot **supporting points (facts only)** | Schema carries `function`/`beat`/`claim` only | Added `supporting:` list per slot |
| Per-scene **VO text** and `vo_seconds` | Schema has `seconds` + `words`, no narration | Added `vo:` and `vo_seconds:`; kept `words:` as the budget check |
| The **one diagram description** | The composition contract forbids naming a visual in a staging artifact, and would rightly reject it | `messaging.md` §4 — described as *what it must show and the redraw test*, never as a layout, palette or effect |
| **Objections in the audience's own words** (`audience.md` rule 1 asks for six to eight, sorted by likelihood) | No `objections:` field in the schema, though the rule is normative | `messaging.md` §6 (five, sorted, plus two held in reserve); slots d11/d12 and scene s8 carry the two that made the arc |
| **Terminology canon / tone constraints** (P is never "stable"; "can't be liquidated" is never hedged) | These are constraints on *what is said*, so they are staging's business — but there is no field for them | Stated in `messaging.md` §1 and obeyed in every claim; a `vocabulary:` block would belong in the contract |
| **As-of dating of roadmap claims** | No date/provenance field | Header of `messaging.md` plus per-slot `source:`; d12's supporting points carry "as of July 2026" inline |

One more, worth stating plainly: the skill has no notion of a **corpus** — it assumes the material
is in the room with you. Everything about "which of five source documents wins when they disagree"
had to come from the brief, not the skill. For a bake-off that is fine; for repeated use against a
document set, a `sources:` block with a priority order would earn its place.

## 7. Deliverables

| File | What it is |
|---|---|
| `messaging.md` | The key messaging: repeatable line, positioning statement, three pillars, the 118-word mechanism + the one diagram description, five cited proof points, five objections with answers |
| `staging.yaml` | The skill's native contract, both lanes: 14 deck slots (~10 min, 50s/slot) and 9 video scenes (120s, 299 words), one bold moment with per-lane derivation, full motion budget and gate results |
| `NOTES.md` | This file |
