# Motion roles — the kinetic governor (video lanes)

Read this whenever the medium is **video**. It is a closed vocabulary, exactly
like `slide-functions.md`, and it is loaded at `STAGE` pass 2 alongside it.

## Why staging allocates motion at all

Base staging emits, per slot: **function + beat + claim**, and exactly one bold
moment for the whole piece. That is enough for a static artifact and enough for
a film whose only kinetic decision is *"where is the one loud bit"*.

A film has a second scarce resource the base contract does not allocate:
**kinetic energy over time**. An arc has a shape in energy the same way it has
a shape in claims. If staging does not allocate it, design allocates it by
default — and the default is *animate everything*, which means nothing reads as
a peak.

**The line that is still held.** A motion role names **what the argument does in
time**, not what the frame looks like. `rupture` says the argument breaks here;
it does not say "chromatic tear, ember palette, 12px displacement". `arrest`
says a motion is begun and refused; it does not say what moves. The composition
contract's test applies verbatim: no chart type, no layout, no palette, no font,
no hex code, no named transition effect may appear in a staging artifact. Design
may render `rupture` a dozen legitimate ways and may refuse a role as
unrenderable — but a refusal returns to staging, it is not fixed in the timeline.

## The standard field set

Every scene in a video lane carries these four fields **in addition to** the base
`function` / `beat` / `claim`:

| Field | Type | Means |
|---|---|---|
| `motion_role` | one of the eight below | what the argument does in time in this scene |
| `energy` | 0–5 | kinetic **amplitude allowance** — a budget design may not exceed and should not undershoot. Not a look. |
| `peak` | bool | whether this scene is one of the piece's earned kinetic peaks |
| `motion_turn` | prose | *which value this scene turns, and why that turn needs time to be legible.* A scene that cannot fill this field is not entitled to motion. |
| `figures` | int + list | the ornament count and what each figure renders — see the ornament gate |

## The closed role vocabulary — eight

| role | means |
|---|---|
| `hold` | The argument stops moving; the frame is given, not developed. The quiet a peak is paid for with. |
| `accumulate` | One value grows continuously across the scene; the point IS the growth, not any single state of it. |
| `strain` | Something intact is put under load and visibly does not cope. Rising, contained, **not yet broken**. |
| `rupture` | The break itself. The loudest thing in the piece; the staged bold moment and nothing else. |
| `arrest` | A motion is begun and **refused mid-gesture**. High in meaning, deliberately LOW in amplitude — the anti-rupture. |
| `assemble` | Separate parts converge into one structure and everything that arrives stays. Constructive, layered, busy. |
| `divest` | The piece gives up its own persuasive apparatus in front of the audience; motion is **subtractive only**. |
| `cadence` | One final gesture that resolves an image opened earlier, then stop. Not a summary, not a flourish. |

In a restrained lane every scene is implicitly `{motion_role: hold, energy: ≤1}`
except the bold moment, so the governor is backward-compatible with a film that
declines to use it.

## The allocation rules

**R1 — earned, not spread.** A kinetic peak is earned only by a scene that
*turns a value* (the dead-slot test), never by one that merely advances the
argument. Most scenes turn something — that is why they exist — but only a few
turn something the viewer must still be carrying tomorrow. Those, and no others,
may peak.

**R2 — a peak is paid for.** No two adjacent scenes may both peak, and every
peak must have a neighbour at `energy ≤ 1.5`. A peak is a contrast effect, not
an absolute one; a peak with a loud neighbour is noise with a label on it. This
rule is what makes the budget bite: buying a peak costs a quiet scene. A pair of
slots the genre forbids splitting (mechanism + its consequence) may take a
declared exception — *declared in the artifact, with the amplitudes stepped
down across the pair*, never taken silently.

**R3 — the ceiling is an ordering.** Allocating motion does **not** lift the cap
on the bold moment. The staged bold moment holds the single highest energy in
the piece and every other peak is capped strictly below it. *"Two bold moments
is zero bold moments"* survives as an ordering rather than as a count.

**R4 — rhyme only to answer.** A scene may repeat an earlier scene's motion only
in order to **answer** it. Repetition for decoration is a dead motion in the
sense R1 means dead.

**R5 — the film is quiet more than half.** Mean energy across scenes ≤ 3.0, and
at least a third of scenes sit at ≤ 1.5.

**R6 — the ornament gate (per scene, not per film).** R1–R5 govern a scene's
*intensity*. They say nothing about **how many things move inside it**, and that
is where an obedient allocation still ships decoration: a scene correctly marked
`assemble` acquires four micro-diagrams, two of which restate their own captions.

> **The rule.** At most **two animated figures per scene** — one *hero* (the
> figure the claim is about) plus at most one *support* group. The staged bold
> moment may spend **three**. Every figure must name **the clause of the claim it
> renders**. A figure that cannot be attached to a clause is decoration and is
> **cut at STAGE**, not softened at design.

The counting unit is a *figure*: an independently animated diagram, card,
chain, table or mark. Staggered members of one group are one figure. Text
entrances (eyebrow, headline, caption) are not figures — they are the scene's
delivery, and they are capped separately by the motion spec's intensity budget.

R6 exists because it was found the hard way: an arc-driven budget stopped a
slot being made a peak and did nothing at all about the four diagrams inside it.
Half the motion in that artifact was doing work — a defensible ratio, and not
the one the allocation rule promised.

## Peaks are derived, not chosen

`rupture` and `arrest` are legal only on a scene whose claim contains an
**EVENT** — a thing that happens, with a before and an after. A claim that
states a **CONDITION**, however important, cannot be ruptured or arrested; it
can only be accumulated, strained or held.

Walk the claims, mark each `EVENT` or `CONDITION`, and count. That count is the
event budget, and there is no other number to argue about. Write the walk into
the artifact — it is mechanical, unarguable, and it is the reason this rule
earns its place.

## The gate

`motion_budget` in `gates:` must state, all of it:

```yaml
motion_budget:
  peaks_earned: N          # and the R1 justification per peak
  ceiling_order: "s4 (5.0) > s12 (3.5) > …"      # R3
  quiet_scenes: [ … ]                            # R2's payment
  mean_energy: N.NN                              # R5, ≤ 3.0
  adjacency: pass | "declared exception at …"    # R2
  rhymes: [{scene: N, answers: M}]               # R4
  figures_total: N                               # R6
  ornament_gate: pass | "cut at STAGE: …"        # R6 — name what you cut
```

A `motion_budget` that reports only a peak count has not been run.
