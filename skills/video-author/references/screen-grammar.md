# Diagram and code-on-screen grammar

No donor skill ships this, and it does more work in a technical explainer
than every chart rule combined: the typical subject is *record shapes* — a
JSON fact, a YAML warrant, a config block, a table, a chain, a cell diagram
— not plottable data. Distilled from the bake-off runs (the control run
invented it under fire; the staged and hybrid runs confirmed the floors).

## Size floors (1920×1080 canvas)

| Element | Floor |
|---|---|
| Monospace record/code text | **≥23 px** — 25 px overflows an 11-line card; below 23 px is unreadable at video compression |
| Body/caption sans | ≥28 px |
| On-screen headline text | large enough to read at a glance; it is 2–5 words, so it can be |
| Diagram labels | ≥22 px, `nowrap` — a label that wraps mid-word (`irreversible-tier`) reads as two labels |

## Line and content budgets

- **One record per scene.** A frame holding two records has two heroes.
- **≤11 lines** of mono per record. A record that needs more is quoted
  partially (elide with a comment line), or split across a before/after
  pair of scenes — never shrunk below the size floor.
- A literal record IS a legitimate scene — the audience that wants the
  mechanism wants the record shape — but it is *read*, so its scene needs
  reading time: budget narration that walks it, and reveal it **as a
  block** (one ~0.4 s fade), never typed character-by-character (typing
  reads as a product demo and steals time from the reading).
- Long command lines: author the continuation explicitly (`\` + an
  indented continuation style). A soft-wrapped command renders flush-left
  and reads as a *second command* — every automated check passes on it;
  only a looked-at frame catches it.

## Syntax colouring inside the brand rule

The accent rule (the brand contract's accent only, no new hues) governs
*emphasis*, not functional colour. The working grammar:

- keys / field names → the light structural accent (e.g. `--blue-lt`)
- comments → muted ink (`--muted`)
- values → primary/secondary ink (`--ink` / `--sec`)
- functional states keep the guide's functional palette: danger red
  **only** on failing verdicts/refusals (1–2 % of surface), never for
  emphasis or decoration. When the argument turns on a PASS/FAIL
  distinction, rendering both in accent blue destroys the claim.
- Any *semantic* hue beyond that (a second actor, a query lane) is a brand
  ruling, not an authoring choice — flag it PENDING with the fallback
  stated (collapse to accent + a caption).

## Build in narration order

- Every progressive reveal follows the sentence being spoken — members of
  a group arrive in the order the narration names them, top→bottom then
  left→right, on the locked stagger.
- A reveal that the narration does not walk is revealed as one block.
- Diagrams draw their connectors **once**, then hold still: no marching
  ants, no travelling dots, no pulse. A structural claim is not a runtime
  trace.
- Numbers do not count up. A count-up carries no meaning, and (on GSAP)
  an `onUpdate`-driven counter freezes under every seek-based gate, so it
  cannot even be verified.
- Tables arrive one row per narration clause (delivery, not evidence —
  budget its energy accordingly); a comparison table's axis order is the
  narration's axis order.
- Before/after is shown **in place** where the claim is "overwritten /
  replaced": the old value leaves by its own row height into the slot the
  new value takes. A value that travels off somewhere else reads as
  *moved*, not replaced — and travels off-frame where no check but a
  per-element measurement will see it.

## The two-audience register

- On-screen text: 2–5 words, plain verbs, one job per element — what the
  viewer reads while the voice says the sentence. Never the transcript.
- Subtitles: the full narration (omit the `subtitle` column; the pipeline
  reuses narration). This is the accessible answer and the sanctioned one.
- A deep-dive act may put denser records on screen than an explainer act,
  but density is spent on the *record*, never on simultaneous motion — the
  intensity budget does not change with register.
