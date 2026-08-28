---
name: deck-author
description: >
  Author and render a deck FROM a staging.yaml contract — the design half
  of the staging → deck pipeline. Brand-parameterized: applies the render
  layer a brand contract (brand.toml) defines — footer rule, self-hosted
  type, palette, marks — on a fixed 1280x720 stage, with the Medici house
  brand shipped as the default instance (brands/medici/). Runs the machine
  gate (tools/check_deck.py) and the mandatory render-and-look gate, and —
  when motion is in play — applies the motion-role governor to slides. Use
  when someone asks to "author a deck", "build the slides", "render the
  staged deck", "turn this staging.yaml into a deck", or wants the HTML deck
  after staging has ruled the structure. Requires a staging.yaml; if none
  exists, run the staging skill first — this skill never decides what is
  said or in what order.
---

# deck-author

Deck-author is the design half of the composition contract. It consumes the
`staging.yaml` the `staging` skill emits and produces the deck:

```
<deck-dir>/staging.yaml   # input — staging's contract (the argument)
<deck-dir>/index.html     # output — the rendered deck, static slide markup
<deck-dir>/deck.md        # output — slide map + speaker notes + cut list
```

## The composition contract (hard, and it binds THIS skill)

```
staging  owns WHAT is said and IN WHAT ORDER    → emits staging.yaml
design   owns HOW IT LOOKS                       → consumes staging.yaml
```

What this skill may never do:

1. **Never reorder slots and never rewrite a headline claim.** The slot
   sequence and every claim in `staging.yaml` are the argument, already gated.
   Legal: splitting one slot across two surfaces; rewording a claim's
   *phrasing* for line-breaking (same insight, same force); typographic
   emphasis inside a claim.
2. **A slot you cannot render is refused, not fixed.** Refusal returns to
   staging with a reason ("this claim carries three ideas; no slide holds
   them"). A design pass that changed the argument's order or content has
   broken the contract — the resulting deck is invalid, however good it looks.
3. **No staging.yaml, no deck.** If the brief arrives without one, invoke the
   `staging` skill (or ask for its output). Improvising the arc inside the
   design pass is exactly the leak the contract exists to stop — and the
   bake-off's finding is that the model's improvised staging is wrong in
   *predictable* places (leads with its best material, over-slots, omits the
   cost, over-asks).

## The brand contract — one skill, any brand

Everything brand-specific this skill and its linter touch lives in ONE file:
a **`brand.toml`** contract — org identity + confidentiality footer strings,
type (families, files, licence note), a named palette, marks, and rules
(accent budget, gradients, remote assets). Schema, annotated example, and the
consumption map: `references/brand-contract.md`. The core of the skill is
brand-neutral; a brand is an *instance* of the contract, and the shipped
default instance is the Medici house brand: `brands/medici/` — its
`brand.toml`, its self-hosted fonts, and its worked skeleton.

**Resolution order** (the linter implements the same one):

1. an explicit contract path given by the user/caller;
2. `brand.toml` at the consuming repo's root;
3. the skill's shipped default instance, `brands/medici/brand.toml`;
4. no contract at all.

**With no contract**, run an abbreviated INTERVIEW before authoring: ask for
the org name, the footer wording (or none), the font families, and the
canvas + accent colours — then offer to write the `brand.toml` those answers
derive, so the next deck skips the interview. If the user declines, proceed
**brand-neutral**: the linter's brand gates downgrade to SKIP-with-notice
(structural checks still rule), and be honest in the handoff that a
brand-neutral deck carries **no confidentiality footer** unless one is given.

## The render layer

Start every deck by deriving a skeleton from the brand contract using the six
documented decisions below — or, on the shipped default, by copying
`brands/medici/deck-skeleton-external.html` into `<deck-dir>/index.html` and
`brands/medici/fonts/` beside it (adjust the `@font-face` URLs to the real
relative path). The Medici instance is the **dark external surface**: `#000`
canvas, `#0A0A0A` cards, `#1A1A1A` hairlines, IBM Plex Sans/Mono self-hosted,
the external footer on every slide, the gold shield-tick assay mark, and a
fixed 1280×720 letterboxed stage. Internal decks keep the light internal
skeleton (not shipped here); the footer wording is the authoritative class
marker on that brand.

### The six skeleton decisions — the derivation checklist for ANY brand

These were derived the hard way during the bake-off (the control cell paid the
invention tax; its notes are the source). They are the decisions a brand guide
does **not** answer — so deriving a skeleton for a new brand means answering
all six from its `brand.toml`, once, deliberately. `brands/medici/` is the
worked default: each decision below states the rule, then how Medici answered
it. Do not re-litigate them per deck; change them only by changing the
skeleton, deliberately.

1. **Type is self-hosted (the contract's `[type]` files) — never a CDN.**
   Fonts are a dependency, not a fetch. **The silent-failure trap:** declare
   variable fonts with their real weight range and static instances at their
   single weight — get this backwards and the browser synthesises bold; the
   deck looks subtly wrong in a way nobody can name. Medici: IBM Plex,
   `ipx-sans.woff2` variable (`font-weight: 100 700`), mono static 400/500 —
   see `brands/medici/fonts/NOTICE.md` — replacing a legacy CDN trio the
   brand guide itself forbade.
2. **Pick ONE heading treatment from the contract's families and hold it.**
   Medici: IBM Plex Sans SemiBold, sentence case — no serif display face;
   where a legacy artifact contradicts the current guide, the guide wins.
3. **Derive the dark (or light) token block from the contract's `[palette]`,
   token-for-token, and invent the missing surfaces explicitly.** Medici:
   `#000` canvas, `#0A0A0A` cards, `#1A1A1A`/`#252525` hairlines,
   `#FFFFFF`/`#AAAAAA`/`#666666` text; functional colours at their true hues;
   the `#060606` code-block surface *invented* (no guide had a deck
   code-block spec) and recorded in the contract — an invention that is not
   written down gets re-invented differently next deck.
4. **The footer (`[identity]` strings) is a per-slide `::after` in BOTH
   screen and print, paired with `<meta name="deck-footer">`.** Not a
   viewport-fixed bar (it would sit outside the letterboxed frame), and never
   Chrome's `footerTemplate` — the one-page-per-slide print path is mutually
   exclusive with it, so a "simplification" to footerTemplate silently loses
   the confidentiality mark on every PDF page. The meta tag is the PDF
   renderer's contract; it hard-errors without it, by design.
5. **Marks (`[marks]`) ship as a plate-stripped `<symbol>` library, not the
   raw brand SVGs.** Brand files are often *app avatars* — Medici's bake in a
   512px near-black rounded plate that reads as a grey box on a true-black
   slide. The Medici skeleton ships plate-stripped symbols: the gold
   shield-tick assay mark (`#assay-mark`), a stroke-only watermark variant,
   and the app-role glyphs. Mark-own colours (the contract's
   `exempt_colors` — Medici's gold) appear **only** inside the mark.
6. **The stage is a fixed 1280×720 board, letterboxed (scaled to fit) — not
   viewport-fluid.** Brand-independent: the presenter's view, a screenshot,
   and the PDF page are the same composition, which is what makes the render
   gate's overflow measurement and screenshots meaningful.
   `@page { size: 1280px 720px }`.

### Render-layer rules on top of the skeleton

- **One accent, and it stays one.** The brand contract's `accent` is the only
  frequent colour; at most `accent_budget` (default two) visible accent uses
  per slide. Functional colours (red/green/amber) only functionally —
  `REFUSED`/fail, `pass` — never decoration. No gradient text; no shadows —
  depth comes from border contrast.
- **Anchor discipline.** Content slides top-aligned so kicker + headline land
  in the same place; centred composition reserved for the cover, the bold
  moment, and the close — so a change of alignment *means* something.
- **Density follows the lane.** A table-lane deck may run smaller type and up
  to six elements per slide; a hall-lane deck runs larger type and rarely more
  than four. Same skeleton, different rhythm. If content exceeds the mode,
  split the slide (a `tight` variant exists for one stubborn table) — never
  shrink below the floor.
- **Static slide markup, always.** Slides are literal `<section class="slide">`
  elements. A deck that builds its DOM from a script array is invisible to the
  machine gate (a static parser) and un-diffable in review. The bake-off's
  staged decks made this mistake; do not repeat it.
- **Headline claims render as the slide's `<h1>`/`<h2>`, verbatim in force.**
  The ghost-deck output of the linter must read as staging's helicopter test.

## Motion on decks — the governor, not the mood

Default is **static**. Motion enters only when `staging.yaml` carries motion
fields (a restraint-off run) or the brief explicitly lifts restraint — and then
it is *governed*, never ambient. The rules are the staging skill's
`references/motion-roles.md` applied to slides; the bake-off's animated cells
proved each one on a real deck:

- **Peaks are derived, not chosen.** Walk the claims: only a claim containing
  an EVENT (a thing that happens, with a before and after) may be enacted.
  Count the events — that is the peak budget, and there is no other number to
  argue about. (The animated explainer found exactly two: an erasure, and the
  same erasure refused — one peak and its answer.)
- **Absences are decisions.** The slide after a peak takes a `hold` — no
  entrance, no build; the room needs a still frame to sit in. The limits/
  objection slide is *drained* — accent pulled, field monochrome — so the deck
  audibly stops selling at the moment it admits what is not built.
  "Animate everything" cannot produce either of these, by construction.
- **The ornament gate.** At most **two** animated figures per slide (the bold
  moment may spend three); every figure names the clause of the claim it
  renders; a figure with no clause is decoration and is cut. This gate exists
  because the intensity budget was obeyed on a real run and four
  micro-diagrams shipped anyway, two of them decoration.
- **Motion is not free in the time shape.** A build must be watched; re-run
  staging's time-shape arithmetic with per-slot dwell and record the new
  runtime as a re-gated judgment (the animated explainer bought one extra
  minute, deliberately). Never quietly extend the time.
- **Degradation and safety.** Under `prefers-reduced-motion` the deck degrades
  to its static twin — every final frame complete, argument-bearing, reachable
  with zero input. No build runs on a timer the presenter does not control;
  every step advances on the same key as the deck; stepping backward lands on
  a coherent frame. No spring, bounce, or overshoot (house motion register)
  unless a single deliberate violation is recorded in the notes.

## The machine gate

```bash
python3 <skill-dir>/tools/check_deck.py <deck-dir>/index.html --deck-md <deck-dir>/deck.md \
        [--brand <brand.toml> | --brand none]
```

`tools/check_deck.py` is the re-pinned linter (provenance in its docstring:
the harness is create-html-deck's, MIT © tt-a1i; the rule table pinned three
times over — see the docstring history). It is **brand-parameterized**: with
no `--brand` it auto-discovers a contract per the resolution order above; the
brand-specific gates (footer wording, font allowlist, accent budget,
remote-asset severity) read the contract instead of constants, and the tool
stays stdlib-only (`tomllib`, python ≥ 3.11 — an older python gets a clear
error on an explicit `--brand` and a SKIP notice on a discovered one). With
no contract in force the brand gates print SKIP notices and only the
structural checks rule. It enforces: document structure, the `deck-footer`
meta + the contract's footer enum + print footer parity, the fixed-stage
geometry, the contract's font pin, offline-only assets that exist on disk,
the closed layout pool (`data-layout`), folio sequence, alt text,
process-language and placeholder leaks, the accent budget, action-title
and key-question smells, and `deck.md` ↔ `index.html` parity. It also prints
the **ghost deck** — the titles in order — which is meant to be read, not just
exit-coded.

- **Scoped ignores** live in `.deckcheck.json` (copy the skill's default
  beside your deck). Every ignore carries a written `reason`; an entry without
  one is discarded. The two stock ignores (pure `#000`/`#fff`) are the pinned
  brand overriding generic dark-theme craft advice — deliberate, not drift.
- **Errors fail, notices pass.** Fix or reason-ignore every error; read every
  notice.
- **`deck.md` format:** one `## SNN · <action title>` row per slide, plus
  speaker notes and a closing **cut list** (which slides compress under clock
  pressure, and which two must never be dropped).

## The render-and-look gate — mandatory, and why

A passing structural check proves the contract, not the deck. Every defect
that mattered in the bake-off was invisible to static/DOM checks and instantly
visible in a rendered frame: a stray `</script>` that stacked every slide and
dumped JS as page text; a table that overflowed the stage by 19px into the
footer (clipped, so invisible in a browser); a command line that soft-wrapped
into what read as a second command; a scene that finished its choreography in
the first sixth of its slot. **An overflow measurement tests whether pixels
are inside the frame, not whether the frame is legible** — so the gate ends
with a person or a model actually looking at the frames.

The recipe (headless Chromium via Playwright, from any environment that has
it — `npm i -D playwright` or an existing house install):

```js
// render-check.mjs — run: node render-check.mjs <deck-dir>
import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
const errs = [];
p.on('pageerror', e => errs.push(e.message));
p.on('console', m => m.type() === 'error' && errs.push(m.text()));
p.on('requestfailed', r => errs.push(r.url()));
await p.goto('file://' + deckDir + '/index.html', { waitUntil: 'networkidle' });
// 1. fonts actually loaded (the variable/static trap makes this non-optional)
await p.evaluate(() => document.fonts.ready);
for (const f of ['400 16px "IBM Plex Sans"', '600 16px "IBM Plex Sans"',
                 '400 16px "IBM Plex Mono"', '500 16px "IBM Plex Mono"'])
  assert(await p.evaluate(s => document.fonts.check(s), f), 'font missing: ' + f);
// 2. per slide: activate, (step every build to its end), then MEASURE overflow
//    against the 1280x720 stage — measure laid-out children, skipping anything
//    an overflow:hidden ancestor clips; the stage clips, so eyes alone miss it.
// 3. footer text + shield-tick mark present on EVERY slide, including cover.
// 4. screenshot >= 6 frames: cover, the bold moment, the densest table/code
//    slide, the close — and, if anything animates, frames caught MID-animation.
// 5. animated decks: a full second pass under emulated prefers-reduced-motion.
// 6. zero page errors, console errors, failed requests.
```

Then **look at the screenshots** and say what you looked for: legibility at
distance, soft-wrapped lines, dead space, a pace that matches the slot. Record
the pass in the deck's notes: slides checked, screenshots taken, findings and
fixes. A render gate that was not run, or whose frames nobody looked at, is
reported as NOT RUN — never implied.

## Delivery

Ship `<deck-dir>/index.html` + `fonts/` (or `../fonts/`, stated), `deck.md`,
and `staging.yaml` — the contract travels with the deck; it is the reviewable
argument. If a PDF is wanted, the house renderer prints it (the house
`render-deck-pdf.cjs`, not shipped with this skill:
`node render-deck-pdf.cjs <deck-dir>/index.html <deck-dir>/deck.pdf`); it
waits for `document.fonts.ready`, prints backgrounds, and takes the footer
from the meta tag — the three rules nobody may "simplify" away. The handoff
states: paths, slide count, the minutes the pacing assumed, which gates ran
with what result, and any refusal sent back to staging.

## Worked example

The winning bake-off run is the reference implementation:
`<loom-bakeoff sandbox>/tracks/deck/staged/` in the loom-bakeoff repo — two decks
(`tech-deep-dive/`, `explainer/`) each with `staging.yaml`, `index.html`,
`deck.md`, plus `NOTES.md` recording what the gates actually caught, and
`explainer-animated/` with the motion governor exercised end to end
(its NOTES.md §3–§7 are the motion sections above, with evidence). When this
skill is installed outside that repo, the pointer is provenance, not a
dependency — nothing here reads those files at run time.

## Provenance and licences

- `tools/check_deck.py` — harness from **create-html-deck** (MIT, © tt-a1i);
  rule table house-pinned (full history in the file's docstring). Keep the
  docstring when adapting.
- The skill's stage discipline distils the bake-off composite skill, itself
  assembled from MIT/Apache-2.0 donors — **create-html-deck** (MIT, © tt-a1i),
  **open-design** (Apache-2.0, + upstream MIT credit to refero_skill © Refero
  Design), **open-codesign** (MIT, © OpenCoworkAI Contributors),
  **pitch-deck-mastery** (MIT, © Steve Kaplan), **frontend-slides** (MIT,
  © Zara Zhang); academic-pptx rules restated only (licence contradiction
  upstream). All restated in house wording; no donor prose is copied here.
- `brands/medici/deck-skeleton-external.html` — house-derived (bake-off control cell,
  2026-08-18) from the internal skeleton + brand guide; internal.
- `brands/medici/fonts/` — IBM Plex, © IBM Corp., SIL Open Font License 1.1
  (`brands/medici/fonts/NOTICE.md`).
- `brands/medici/brand.toml` — the shipped default brand-contract instance
  (house values); the schema it instantiates is `references/brand-contract.md`.
- The motion governor is the `staging` skill's (see its `LINEAGE.md` for the
  full ledger, including the HyperFrames Apache-2.0 vendored gate on the video
  side).
