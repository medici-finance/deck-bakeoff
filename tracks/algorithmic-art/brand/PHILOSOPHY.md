# CONSERVED ENTRY

*An algorithmic philosophy. Written 2026-08-27 for the Medici RWA bake-off, brand mode.
Step 1 of the algorithmic-art skill's two-step process; step 2 is the p5.js expression in
`*/deck/index.html` and `*/explainer/explainer.html`.*

---

## The movement

**Conserved Entry** is a generative movement built on a single law: *nothing in the frame is
ever created, and nothing is ever destroyed.* Every mark on the canvas is one member of a
population whose cardinality was fixed before the first frame and is asserted, every frame,
by a live count. The population may divide. It may migrate between territories, stratify,
cool, drift, thin to near-invisibility. It may not grow, and it may not shrink. The image is
therefore never a picture of a quantity; it *is* the quantity, re-arranged. A viewer who
counts what is on screen and a viewer who reads the number in the corner arrive at the same
figure, always, and that agreement is the whole aesthetic.

This is a harder constraint than it sounds, and it is where the craftsmanship lives. A flow
field is easy to make beautiful by spawning and killing particles at the boundaries — the
cheap trick every field system reaches for, and the one this movement forbids outright.
Under conservation, a particle that leaves the frame must be *returned*, not respawned;
density must be redistributed rather than manufactured; a fade must be a fade of luminance
and never a fade of population. Every one of those substitutions had to be found and tuned by
hand, over many iterations, by someone who has built enough particle systems to know exactly
which shortcut each one replaces. The finished algorithm should read as effortless and be
nothing of the kind: a meticulously crafted conservation solver wearing the clothes of a
drifting noise field.

## Two basins and a separatrix

The field is a two-well potential laid over layered Perlin noise. A single scalar — the
**separatrix position**, the ratio of a driving price to a fixed strike — decides how the
population settles between the wells, and it decides it in closed form rather than by
simulation: below the separatrix the left basin takes the entire population; above it, the
left basin retains exactly the reciprocal of the drive and the right basin takes the
remainder. Sweep that one scalar and the population performs a payoff curve without any
curve ever being drawn. The system has no chart mode. It has a parameter, and the parameter
has consequences, and the consequences are the composition.

The noise is not decoration either. Three octaves at falling amplitude give the field its
turbulence; the potential gradient gives it its allegiance; the sum gives every particle a
velocity that is smooth in space and discontinuous in meaning exactly at the separatrix.
Trails accumulate on a persistence buffer so that density — the visible weight of a basin —
is an integral of history rather than a snapshot, which is why the image continues to be
legible when the population is standing almost still. The octave weights, the potential
depth, the advection step, the trail decay: four numbers whose ratios took painstaking
optimisation to balance, because at every wrong setting the field either freezes into
banding or boils into noise. The right setting is a narrow window, and finding it is the
product of deep computational expertise, not of a lucky seed.

## Time, and the one broken law

Conserved Entry has three temporal registers, and a master-level implementation keeps them
strictly separate. **Advection** is fast and continuous: particles always move. **Migration**
is slow and monotone: allegiance eases between basins over seconds, never snapping.
**Divestment** is slower still and one-directional: luminance leaks from a basin at a fixed
rate per cycle, so a population can grow dim while remaining, to the count, entirely intact.
The distinction between a thing losing value and a thing ceasing to exist is the movement's
central expressive claim, and it is available only because the count is honest.

And then, exactly once in any sequence, the law is broken. In the **rupture** register the
conservation solver is switched off and the population is annihilated — not faded, not
migrated, *removed*, with the counter falling to zero while the frame is still full of the
trails of things that were there a second ago. A movement that has spent every prior frame
proving that nothing is ever lost can spend that credit precisely once. The rupture must be
rare, brief, and never repeated; a second one would reveal the first as a special effect
instead of a violated principle. This is the discipline the whole system exists to serve,
and it is why the conservation is enforced in code rather than promised in a caption.

## Absence as a motion that does not complete

The fourth register is the movement's signature and its hardest problem: how does an
algorithm render something that *is not there*? Conserved Entry answers with the **seek**:
a scan traverses the entire parameter range looking for a state that violates the law — a
price at which the two basins do not sum to the population — and, finding none, decelerates
and dissolves without arriving. The gesture is drawn from the rupture's own vocabulary so
the eye recognises it starting; it is then denied its completion. Nothing flashes, nothing
is labelled, no red line is struck through. The viewer watches a search fail, and the
failure is the statement. Getting the deceleration curve right — early enough to feel
deliberate, late enough to feel disappointed — is the single most re-tuned parameter in the
system, and it is the one that separates a competent generative sketch from a piece of
computational rhetoric.

## Restraint as palette

The movement is monochrome by conviction, not by limitation. True black is the ground, and
it is genuinely black — the field must be able to fall to nothing at the edges so text and
silence can share the same surface. The population renders in grey at low alpha, and exactly
one hue, an electric blue, marks the protected basin. Blue never exceeds a few percent of
any frame's coverage; it is a *state*, not a colour scheme, and the moment it becomes
decorative the composition has failed. A second functional hue exists solely for the rupture
and appears nowhere else in any sequence. If a frame looks colourful, the parameters are
wrong.

Every run is seeded and every seed is reproducible: the same seed must produce the same
frame today, in a PDF, and in a screen recording made a month from now. Reproducibility here
is not a convenience feature — it is the same claim as conservation, extended along the time
axis. The algorithm should feel like the work of someone at the absolute top of the field:
restrained where restraint costs more than flourish, exact where exactness is invisible, and
built so that the beauty is in the process running correctly rather than in any single frame
it happens to produce.

---

## The conceptual seed

*The reference embedded in the parameters, never announced on the surface.*

The Medici of Renaissance Florence are remembered for patronage; what they actually
contributed was **double entry** — the insistence that every debit is matched by a credit,
that the books of every branch reconcile against the centre, and that a balance is therefore
something you verify rather than something you are told. Conserved Entry is that ledger,
rendered as a field. The population is the ledger's total. The two basins are the two
columns. The live count in the corner is the trial balance, struck every frame. The
separatrix is the price at which the entry is posted. And the rupture — the one frame where
the count does not hold — is what a bank looks like when its books stop balancing.

Someone who knows the history will feel it. Everyone else sees a field of grey and blue
particles that never quite settles, and a number that never changes.
