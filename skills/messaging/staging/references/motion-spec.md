# The motion-language spec — one choice per row

A **design-side** reference, not a staging one. Staging allocates *how much*
motion each scene gets (`references/motion-roles.md`); this file is the single
page the design pass fills in to say *what motion is, in this piece*.

Two rules, and they are the whole point of the form:

1. **The spec is LOCKED before authoring.** Every number below is decided and
   written down before the first scene is built. A motion language chosen
   scene-by-scene is not a language; it is a habit with variations.
2. **The spec is AUDITED after.** Re-read the finished piece against every row
   and record the result — including the rows that failed and were fixed. An
   unaudited spec is a wish.

## Units are frame-relative, never pixels

Every distance is a **percentage of frame height** — including horizontal
travel, so one number survives a change of aspect ratio and a change of render
resolution. `24px at 1080p` is not a motion language; it is a number that
happens to be true of one output. The instance file may print the pixel
equivalent in brackets for the implementer, but the spec value is the
percentage.

## The table — one choice per row

| Property | The one choice | House value |
|---|---|---|
| **Easing family** | Exactly **two** curves for entrances and exits (one OUT for entrances, landings and draws; one IN for exits), **plus a declared closed set of at most three** for state change and continuous motion (drains, shuttles, strain builds, sanctioned collapses), each printed in the instance with what it governs. `linear` is legal only on a single declared continuous ambient or accumulation. No default ease anywhere — every tween names its curve. *(Row amended 2026-08-18: the original two-curve lock had no slot for state change — an OUT curve on a disappearance makes a thing that is going look like a thing that is arriving; found FAIL–NOT-FIXED by the hybrid/loom run, resolved here and in video-author §4.)* | OUT `cubic-bezier(0.22, 1, 0.36, 1)` · IN `cubic-bezier(0.4, 0, 1, 1)` · state-change set declared per instance (≤3) · overshoot **0%** (no spring, no bounce, no back/elastic) |
| **Base timing unit** | One unit; every duration in the piece is a multiple of it. Four values exist and there is no fifth. | unit **0.4 s** — micro 0.2 s (½) · base 0.4 s · hero 0.8 s (2×) · ambient 1.6 s (4×) |
| **Transition family** | One family for every scene boundary, plus a stated budget of **reserved** vectors for chapter boundaries the argument marks. | **hard cut**, crossfade **0** · lateral throw **14 % of frame height**, exit 0.45 s / entry 0.55 s · reserved: **≤ 3 per film**, Z push or Z pull only, each on a boundary the narration names |
| **Stagger rhythm** | One value for every grouped reveal in the piece, in reading order. | **0.06 s**, cascade, top→bottom then left→right |
| **Motion intensity** | One travel figure for support, one for hero, one scale range, and a **stated exception list**. | support **0.75 % H** · hero **2.2 % H** · scale 0.96→1.00 · opacity 0→1 · no rotation, ever · **exception:** the bold moment's carrier may travel up to **22 % H** when the travel *is* the event (an erasure that only nudges is not an erasure) |
| **Hold floor** | The minimum stillness after a beat, and — the row people get wrong — whether the slack is *flexed* or *fixed*. | **≥ 0.4 s** after every beat, and **every inter-event gap is a flexed hold**. Slack becomes stillness distributed across the rests; a scene never invents another move to fill its slot. |
| **Intensity budget** | Animated events per scene, and the bold moment's allowance. | **≤ 3 events per scene** (1 hero + ≤ 2 support groups); the bold moment may spend **5**. At most **⅓ of on-screen elements in motion at once**. |

Two eases, one unit, one transition family, one stagger, one travel pair, one
hold floor, one budget. Seven rows. A spec with a second value in any row has
not made the choice that row exists to force.

## The restraint pass

The senior half of the form. List what **could** have moved and does not, with
the reason. It is the shortest section and the one that changes the piece most:
a camera that never moves, a mark that never animates into a character, code
blocks revealed as a block rather than typed, numbers that never count up,
connectors drawn once and then still, an ambient that never reacts to the
content in front of it.

## The audit

Re-run every row against the finished scenes and publish the result as a table
with a column per deliverable. Rows that failed are written as **FAIL → FIXED**
with what the fix was. Two failures recur often enough to be worth naming in
advance:

- **The terminal-hold pile-up.** Fixed gaps plus one flexed hold at the end
  means every scene plays its whole choreography in the first three seconds and
  then sits still for the rest of its slot. Invisible in the code, invisible in
  a scene-count check, obvious in a screenshot taken mid-slot. The fix is the
  hold-floor row: flex *every* gap.
- **Two heroes in one frame.** Two figures drawing themselves at once, each
  looking like the subject. The fix is demotion, not a shorter duration.

The audit is where a locked spec pays for itself: without the lock, both of
these get renamed as choices.
