# INVARIANT DRIFT

*An algorithmic philosophy. Written first, before a single line of the algorithm —
because the algorithm is the argument, and the argument has to be true before it
can be beautiful.*

---

## The movement

**Invariant Drift** is a generative aesthetic built on a single refusal: *nothing
is created and nothing is destroyed.* Every composition in this movement is a
closed system of a fixed number of quanta. They may migrate, stratify, braid,
crowd into one basin and abandon another, burn bright at high velocity and cool
to ash at rest — but they may never be conjured and they may never be spent. The
census taken at the last frame equals the census taken at the first. Everything
else in the frame is free.

This is harder than it sounds, and it is where the craftsmanship lives. Most
generative systems cheat: particles are respawned at the edges, faded out,
culled for performance, topped up when the density looks thin. A meticulously
crafted Invariant Drift algorithm may do none of those things. Conservation is
not decoration applied after the fact — it is the integration rule, enforced at
every timestep, and the entire visual character of the work falls out of the
tension between a population that wants to spread and a total that cannot move.
The discipline is the aesthetic. Painstaking optimization is required precisely
because the easy escape hatches are closed.

## Emergence from partition, not from generation

The generative engine of this movement is not birth — it is **allegiance**. Each
quantum carries a scalar loyalty; a governing ratio decides which of two basins
it belongs to; and as the ratio moves, quanta cross. What the eye reads as
growth is only ever migration, and what it reads as collapse is only ever
migration in the other direction. The two basins have different climates —
different flow fields, different noise octaves, different colour temperatures —
so a quantum's crossing is a visible change of weather, not a change of state.
A master-level implementation makes the crossing legible at the scale of one
particle *and* at the scale of the whole population, which requires the field
turbulence to be tuned an order of magnitude below the migration velocity. That
ratio is the single most important number in the system, and it is found only by
iterating.

## The census is the only chart

Invariant Drift never draws a graph. It **counts**. At any moment the algorithm
may take a census of its own population — how many quanta in the left basin, how
many in the right — and stamp that count into the frame as a measured mark. Sweep
the governing ratio slowly across its range and the marks accumulate into a
curve; the curve was not plotted, it was *observed*, and it is therefore honest
in a way a drawn line can never be. This is the movement's central technical
demand and the place where deep computational expertise shows: the census must be
derived from the live population every frame, never from the closed-form function
the population happens to obey. If the two ever disagree, the algorithm is wrong,
and the artist wants to see that it is wrong. Beauty in this movement is a
falsifiable claim.

## Two temperatures, one ledger

Colour is never chosen; it is **derived**. A quantum's hue comes from its
allegiance, its luminance from its speed, its opacity from the local density it
finds itself in — and nothing in the palette responds to time. That constraint
gives Invariant Drift its characteristic stillness-inside-motion: the composition
churns continuously while its colour statistics stay dead flat, because the
statistics are a function of a conserved quantity. Beneath every composition runs
a single hairline **ledger** — one thin bar, partitioned at the population's
current split point. The partition slides. The bar's length never changes by a
pixel. It is the quietest mark in the work and it is the whole thesis.

## The seeking line, and what it fails to find

Every Invariant Drift piece contains an antagonist: a **scan** that sweeps the
field looking for a state that violates the conservation rule — a moment where
the census comes up short. It is drawn as a bright seeking line with a short
decay, and it is given a genuine test, evaluated against the real population, not
faked. In a conserved system it sweeps, finds nothing, and dissolves; the frame
is quieter after it passes than before. Run the *same algorithm* with
conservation disabled — one boolean, one parameter — and the scan latches, and
the population is annihilated, and the ledger bar collapses to nothing. Two runs
of one meticulously crafted algorithm; the entire difference is a parameter. That
is the movement's proof strategy: never argue with a second picture, argue with a
second parameter setting of the *same* picture.

## Craft, restated

An Invariant Drift work must look like the product of hundreds of hours: the
noise octaves layered so turbulence has weather rather than fuzz; the trail decay
tuned so accumulation reads as density and never as smear; the migration easing
chosen so a mass crossing has the mechanical inevitability of a tide and none of
the twitch of a transition library; the seeking line's decay curve refined until
its failure to find anything is felt as relief. Nothing here is a preset. Every
constant in the finished system should be the survivor of many rejected
constants. And the seed is sovereign: the same seed must produce the same
composition to the last quantum, forever, on any machine — because a system whose
whole subject is a quantity that cannot change has no business being irreproducible.

---

## The conceptual seed

*(embedded in the algorithm, not announced on the surface)*

The governing ratio is **S/x** — a strike over a reference price. The two basins
are the two claims a split collateral position becomes. The census curve that
draws itself as x sweeps is a payoff diagram nobody drew. The hairline ledger is
`P + N ≡ collateral`. The scan is a liquidation engine, given a real test, coming
back empty — and the one boolean that turns conservation off is the entire
difference between a structure that cannot be force-sold and a structure that was
auctioned for zero dollars in March 2020.

The oracle joke is buried deepest and is the part the author is fondest of: the
noise field driving the drift is **seeded once and read once, at settlement** —
`noiseSeed()` at initialization, sampled at the maturity frame — never
re-randomized mid-run. A continuous, manipulable price feed would have been one
line shorter to write. The system deliberately does not have one.

Someone who knows the mechanism will feel all of this in the first ten seconds.
Everyone else sees a conserved field drifting, and a bar that never changes
length.
