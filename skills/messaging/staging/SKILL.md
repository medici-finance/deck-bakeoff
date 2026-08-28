---
name: staging
description: >
  Stage a deck, talk, or explainer video BEFORE anything is designed — the
  genre → audience → arc layer. Decides the genre, reads the audience, chooses
  the arc, assigns a function and a headline claim to every slot, places the one
  bold moment, allocates motion roles for video, and reconciles it all against a
  time budget in minutes. Emits a staging.yaml contract that a downstream
  authoring skill (deck-author, video-author) consumes. Use when someone asks to
  "stage a deck", "stage a video", "storyboard the argument", "plan the
  presentation", "structure this talk/explainer", or asks for any deck, talk,
  walkthrough, pitch, or explainer video whose structure has not already been
  ruled. Do NOT use it to choose charts, layouts, palettes, fonts, or animation
  effects — that is design's job, and staging is forbidden to touch it.
---

# staging

Staging is the layer between "here is the material" and "here is the deck."
It owns **what is said and in what order**. It is medium-aware — every genre
playbook carries a **deck lane** and a **video lane** over one shared arc.

## How this skill is invoked

Run staging **first**, before any authoring or design skill, whenever a deck,
talk, or explainer video is requested and no ruled `staging.yaml` exists yet.
Its single deliverable is `staging.yaml`, written beside where the artifact will
be built; the downstream skill (`deck-author` for slides, `video-author` for
film) consumes that contract and owns everything visual. If the brief already
comes with a reviewed `staging.yaml`, skip this skill and go straight to the
authoring skill. All file references in this skill (`references/…`, `tools/…`)
are relative to the skill's own directory, wherever it is installed; paths to
the material being staged come from the brief, never from this skill.

## Version

**v2 — 2026-08-18.** v1 staged both media but had only ever been *exercised* on
decks; the video lane shipped as a claim. v2 is what the video runs sent back.
Four changes, all in the video lane, all traceable to a run that found them:

1. **The kinetic governor is now a standard field set.** `motion_role`,
   `energy`, `peak`, `motion_turn` and `figures` on every scene, with a closed
   eight-role vocabulary and six allocation rules —
   `references/motion-roles.md`. In v1, motion was allocated by design, by
   default, which in practice means "animate everything", which means nothing
   reads as a peak.
2. **The ornament gate (R6).** v1's budget governed a slot's *intensity* and
   said nothing about how many things move *inside* it. An obedient allocation
   still shipped four micro-diagrams on one slot, two of them decoration.
3. **`bold_moment.placement` is per-medium and DERIVED.** v1 carried one
   percentage measured on deck slot indices. In `technical-deep-dive`'s video
   lane that figure is arithmetically unsatisfiable — with `rupture+diagnosis`
   at 0.35 and `mechanism` at 0.40 the proof beat cannot open before 75% — so
   the gate could not be passed by any staging of that lane. The rule is now:
   compute the window from the lane's own `runtime_shares`. A percentage
   inherited from the other medium is a rule that trains people to ignore
   gates.
4. **Two executable gates.** `references/motion-spec.md` (the design-side
   motion language, locked before authoring and audited after) and
   `tools/seam-gate.mjs` + `references/seam-gate.md` (numeric verification of
   every scene boundary). The video GATE stage now also makes
   **render-and-look** mandatory.

## The composition contract (hard)

```
staging  owns WHAT is said and IN WHAT ORDER    → emits staging.yaml
design   owns HOW IT LOOKS                       → consumes staging.yaml
```

Two rules, both testable, neither negotiable:

1. **Staging never names a chart type, a layout, a palette, a font, a
   transition animation, or a slide count used as geometry.** If a staging
   artifact contains the word "bar chart", "two-column", "hero image" or a hex
   code, staging has leaked into design and the artifact is invalid. The
   closest staging may come to visuals is a *function* from the closed
   vocabulary (`evidence`, `comparison`, `mechanism`) and a *claim*. How that
   claim is shown is not staging's business.
2. **Design never reorders slots and never rewrites a headline claim.** Design
   may split one slot into two surfaces, may reword a claim's *phrasing* for
   line-breaking, and may refuse a slot as unrenderable — but a refusal returns
   to staging, it does not get fixed in the layout. A design pass that changed
   the argument's order has broken the contract.

A failed gate never gets patched at the gate. It names the upstream step to
return to (`CLASSIFY`, `STAGE`) and you go back there.

## The flow

`INTAKE → CLASSIFY → LOAD → STAGE → GATE → HANDOFF`

### 1. INTAKE — at most three questions, and skip them if you can

Do not interview. Three questions, maximum, and only the ones the brief has
not already answered:

1. **Who is in the room, and what decision do they hold?**
2. **How long, and will it be presented or read?**
3. **What must they believe by the end — in one arguable sentence?**

**Skip the interview entirely** when the brief already names the audience, the
decision or judgment they hold, and the time slot. Say so out loud: *"INTAKE
skipped — the brief answers all three."* If a shared answer ledger exists
(house bake-offs, a client intake doc), read from it verbatim rather than
asking again.

Anything else you want to know is a **recorded assumption**, not a question.
Write it down and keep going. Never stall a staging pass on an unanswered
question.

The one-sentence belief must be **arguable**. "Loom is a substrate for agentic
work" is a topic. "GitHub's data model, not our discipline, is what lets a
security block get erased" is a claim. If the sentence cannot be disagreed
with, there is nothing to stage.

### 2. CLASSIFY — name the genre you chose AND the ones you rejected

Route in two moves.

**Move 1 — the room.** Before genre, settle the idiom. Three axes:

| Axis | → **hall** | → **table** |
|---|---|---|
| Room size | dozens to thousands | roughly 2–25 |
| Interaction | one-way, presenter drives | two-way, audience interrupts |
| Medium | projected, read at a distance | read close, often *also* read alone |

Hall and table are house names for a split the canon settled long ago: the
persuasion-in-a-small-room idiom and the perform-to-a-crowd idiom are
different crafts, and the most common structural failure is running one in the
other's room. Consequences:

- **hall** — sparse slots, one idea per slot, a plan for a deliberate change of
  gear roughly every ten minutes, no appendix in the walk, the artifact does
  **not** stand alone without its narrator.
- **table** — dense slots permitted, evidence and footnotes legal, appendix
  legal, an objection loop expected, and the artifact **must** stand alone,
  because half the audience will read it without you.
- **Mixed** is normal and must be *declared*, not drifted into: state which
  lane leads. A deck that will be presented once and forwarded ten times is
  table-leaning whatever the room size.

**Move 2 — the genre.** Seven, deliberately not twenty-four:

| id | one-line mandate |
|---|---|
| `technical-deep-dive` | make a competent skeptic believe the mechanism is real and the tradeoffs are honest |
| `executive-explainer` | make a non-specialist decision-holder understand what changes and why it matters to them |
| `investor-pitch` | make a funder believe this team, this market, this moment |
| `board-update` | let a governing body exercise oversight without reading the appendix |
| `sales-proposal` | move a buying group from interest to a next commitment |
| `internal-decision` | get one specific decision made, in the room, today |
| `conference-keynote` | leave a room of strangers holding one idea they will repeat |
| `teach-workshop` | leave people able to *do* something they could not do before |

Full playbooks live in `references/genres/`. `technical-deep-dive` and
`executive-explainer` are complete; the rest are stubs in
`references/genres/STUBS.md` (id + mandate + pick_when only) and must be
written out before use.

**The output of CLASSIFY is a stated rejection.** Write, in the artifact:

```
CHOSE   <genre>  because <the audience's decision + the room>
REJECTED <genre> because <the specific pick_when it fails>
REJECTED <genre> because …
```

Two rejections minimum. A classification with no rejections was not a
decision. If two genres both fit, one **leads** (its arc, its time shape, its
gates) and the other **contributes named beats** — say which, and which beats.

### 3. LOAD — exactly one playbook

Read the chosen genre file end to end. Check its `kill_conditions` **now**,
before staging anything: a kill condition that fires means this is the wrong
artifact entirely (a memo, a doc, a conversation), and saying so is a
legitimate, valuable output of this skill.

Supporting references, loaded as needed:

| File | Read it when |
|---|---|
| `references/audience.md` | always — the audience block drives density, order, and the objection loop |
| `references/slide-functions.md` | while building the slot sequence — the function vocabulary is closed |
| `references/transitions.md` | at every beat boundary, and when the deck feels flat in the middle |
| `references/genres/<genre>.md` | the one chosen playbook |
| `references/motion-roles.md` | **always, when the medium is video** — the kinetic governor and its six rules |
| `references/motion-spec.md` | video, at the design handoff — the locked motion language |
| `references/seam-gate.md` | video, before authoring the boundaries — how to declare and verify seams |

### 4. STAGE — four passes for a deck, five for a film, in this order

1. **Arc.** Take the playbook's beats. Delete any beat the material cannot
   fill honestly; never invent material to fill a beat. Beats are named in
   house words, not the playbook's — the playbook's beat names are a template,
   your arc's beat names are about *this* subject.
2. **Slot sequence.** Assign each beat one or more slots, each with a
   **function** from the closed vocabulary. Obey the sequencing rules in
   `slide-functions.md` — some functions may not be split from their
   neighbour, some may not open a section.
3. **Headline claim per slot.** One declarative sentence per slot, stating the
   *insight*, not the topic. "Three problems with the fact log" is a label.
   "The fact log makes erasure structurally impossible" is a claim. Every slot
   gets one, including the cover. A slot that cannot carry a claim is a slot
   that should not exist.
4. **Bold moment.** Place exactly **one**. Read the playbook's
   `bold_moment.placement` rule and obey it — the placement is genre-specific
   and it is the single most common thing a bare draft gets wrong. **Read the
   lane-specific figure**: `placement_deck` is measured on slot indices,
   `placement_video` is measured on TIME and is derived from that lane's
   `runtime_shares`. Show the derivation. Record the beat, the form, and *why
   this one*. Two bold moments is zero bold moments.
5. **Motion allocation — VIDEO ONLY.** Load `references/motion-roles.md` and
   assign every scene a `motion_role`, an `energy`, a `peak` flag, a
   `motion_turn` and a `figures` list. Peaks are **derived**: walk the claims
   and mark each EVENT or CONDITION; only an EVENT may be ruptured or
   arrested, and the event count is the peak budget. Then run the ornament
   gate scene by scene and **cut here**, not at design. This is a STAGE pass
   and not a gate on purpose: on the run that produced it, the check demoted
   two slots of eleven, and a check that changes a fifth of the assignments is
   doing design work too late.

### 5. GATE — five checks for a deck, ten for a film, each naming its return step

| Gate | Test | Fails to |
|---|---|---|
| **Helicopter** | Read ONLY the headline claims, in order, with nothing else. Do they form the whole argument, standing alone? | `STAGE` pass 3 |
| **Bold moment** | Exactly one, placed where the playbook says, and it is a *thing that happens*, not a strong sentence | `STAGE` pass 4 |
| **Dead slot** | Every slot must change something — a belief, a stake, a level of detail, a direction. A slot where nothing turns is cut, not improved | `STAGE` pass 2 |
| **Kill conditions** | Re-check the playbook's list against the arc you actually built | `CLASSIFY` |
| **Time shape** | slots × per-slot floor ≤ minutes. State the arithmetic | `STAGE` pass 2 (cut slots) or `INTAKE` (renegotiate minutes) |

The dead-slot test is the ruthless one and it is worth stating in full: a slot
earns its place by turning a value — the audience believed X and now believes
Y, the stakes were low and now are high, the thing was abstract and is now
concrete. *Restating* is not turning. Recapping is not turning. An agenda slot
turns nothing and almost never survives this gate.

The time-shape gate is arithmetic and must be shown: `minutes × 60 ÷
content_slots = seconds per slot`, compared against the playbook's floor. If
the answer is below the floor, **cut slots** — do not talk faster, and do not
quietly extend the time.

In the **video lane** the time-shape gate is a different and harder arithmetic:
`words = seconds × wpm`, apportioned across the lane's named `runtime_shares`.
On a deck the time gate cuts slides. On a film the time gate **writes the
script** — it decides how many words each beat gets, and a beat with no share
gets deleted rather than compressed.

#### The video GATE — five more, and they are not optional

| Gate | Test | Fails to |
|---|---|---|
| **Motion spec locked** | `references/motion-spec.md` filled in, dated, and locked **before** the first scene was authored — then its audit table run against the finished scenes, failures written as FAIL → FIXED | design (re-lock and re-author), never patched at the gate |
| **Seams declared + gate passing** | Every scene boundary in a seams ledger, `tools/seam-gate.mjs` run against the delivered file, **0 fail** | design (the boundary is the fix) |
| **Governor rules checked** | The full `motion_budget` block: peaks earned by R1, adjacency by R2, ceiling ordering by R3, rhymes by R4, mean energy by R5 | `STAGE` pass 5 |
| **Ornament gate** | ≤ 2 animated figures per scene (bold moment ≤ 3); every figure names the clause of the claim it renders; what was cut is named | `STAGE` pass 5 |
| **Render and LOOK** | Headless render of every scene, ≥ 6 screenshots including mid-animation, zero page errors, the done signal on both the injected and the fallback duration paths, scene count == script row count — **and a human or model actually looks at the frames** | design |

The last one is mandatory and the reason is worth stating: on the runs behind
v2, every automated check passed on a frame whose first command line soft-
wrapped and read as a second command, and on a scene that played its entire
choreography in three seconds and then sat still for seventeen. **An overflow
measurement tests whether pixels are inside the frame, not whether the frame is
legible**, and a scene-count check cannot see a pace. Both were caught by
looking at a screenshot.

### 6. HANDOFF — emit staging.yaml

```yaml
brief: <name>
genre: <id>
lane: hall | table | mixed(<leader>)
classify:
  chose: {genre: …, because: …}
  rejected: [{genre: …, because: …}, …]
audience: {assumed_knowledge: …, distrusts: …, decision_they_hold: …, attention_budget: …}
belief: "<the one arguable sentence>"
time_shape: {minutes: N, medium: deck|video, seconds_per_slot: N, floor: N}
arc: [{beat: …, minutes: …}, …]
bold_moment: {slot: N, beat: …, form: …, why: …}
slots:
  - {n: 1, function: cover,  beat: …, claim: "…"}
  - {n: 2, function: …,      beat: …, claim: "…"}
transitions: [{after_slot: N, type: turn|narrow|escalate|fold|gate, line: "…"}]
gates: {helicopter: pass, bold_moment: pass, dead_slot: pass, kill_conditions: pass, time_shape: "…arithmetic…"}
assumptions: ["…"]
```

**Video adds five per-scene fields and one block** (see
`references/motion-roles.md`):

```yaml
scenes:
  - {n: 1, function: …, beat: …, claim: "…", seconds: N, words: N,
     motion_role: hold|accumulate|strain|rupture|arrest|assemble|divest|cadence,
     energy: 0-5, peak: bool, motion_turn: "…", figures: [{name: …, renders: "<clause>"}]}
motion_budget: {peaks_earned: N, ceiling_order: "…", quiet_scenes: […],
                mean_energy: N.NN, adjacency: …, rhymes: […],
                figures_total: N, ornament_gate: …}
seams: <path to the declared-seam ledger>
motion_spec: <path to the locked motion-language instance>
```

`staging.yaml` is a **deliverable in its own right**, not scaffolding. It is
the reviewable artifact — an argument you can disagree with before anyone has
spent an hour on a layout. Ship it beside the deck.

Nothing in `staging.yaml` may name a visual. If you are tempted to write
`visual_family: chart`, that temptation is the leak this contract exists to
stop.
