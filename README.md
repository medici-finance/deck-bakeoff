# deck-bakeoff — presentation-tool bake-off on "Medici for RWA tokens"

A local bake-off (2026-08-27/28) of AI presentation-design skills and messaging
skills, all rendering the same product pitch — **Medici for RWA tokens** — as a
slide deck and as an animated HTML explainer, in two modes: the pinned Medici
house brand and "no brand limits". Everything here was produced by Claude Code
agents from one prompt (below); Ian judged separately.

## Layout

| Path | What |
|---|---|
| `BRIEF.md` | the shared brief every contender rendered (product story, audience, the three educational goals, media specs, brand modes) |
| `DESIGN-TASK.md` | the task spec every design agent followed |
| `bakeoff/PROTOCOL.md` · `CONTENDERS.md` | contenders, origins/URLs/licences, rules, judging axes |
| `messaging/<skill>/` | 4 messaging contenders: native artifact + `messaging.md` + normalized `staging.yaml` + `NOTES.md` |
| `tracks/<tool>/<mode>/<messaging>/deck/index.html` | 36 decks (1280×720, self-contained, prints one slide per page) |
| `tracks/<tool>/<mode>/<messaging>/explainer/{explainer.html,SCRIPT.md}` | 36 timed explainers (1920×1080, auto-play, `window.__player`) + talk tracks |
| `tracks/<tool>/NOTES.md` | each tool's time-to-artifact, friction, overrides, refusals |

`<mode>` is `brand` (pinned Medici house brand) or `free` (no brand limits); `<messaging>` is one of `staging`, `presentation-writing`, `pitch-deck-mastery`.

| Path | What |
|---|---|
| `reviews/messaging/by-<rubric>.md` | each messaging skill reviewing every messaging output (itself included) |
| `reviews/design/by-<rubric>.md` | 4 independent design rubrics + the 4 messaging rubrics over every rendered track |
| `bakeoff/JUDGING-*-claude.md` | Claude's verdicts (messaging, design), formed before Ian's |
| `shots/` | contact sheets + `INDEX.md` (per-slide PNGs are git-ignored) |
| `winner/` | the ship-tomorrow artifact (canvas-design / brand / staging) after the judge's fix list — `deck/index.html`, `explainer/{explainer.html,SCRIPT.md}`, `FIXES.md`, frames in `shots/` |
| `report.pdf` (source `report.html`, build `bakeoff/report-build.py`) | the final report: brief, contenders + URLs, both legs' cross-review matrices, issues found, verdicts, pipeline, the winning explainer + its talk track |
| `video/explainer.html` · `video/SCRIPT.md` | the ONE bake-off video source: unbranded report segment → lead-in → the winning explainer in full; rendered to mp4 by the house `explainer-video` pipeline (mp4 not committed) |
| `social/` | reddit post + LinkedIn teaser drafts (`{{YT_URL}}` placeholder) |
| `source/` | the input corpus (Medici pitch/research docs, house brand guide) — read-only inputs, names anonymized |

The house skills used in the run are committed under `skills/` — `messaging/staging`, `messaging/house-guide`, `deck-author` (with the Medici `brand.toml` contract and linter), `video-author`, `video/video-design`, `video/explainer-video` (the render pipeline; its `node_modules`, `out/` and voice-clone samples are excluded), `social/linkedin-post`, `social/humanizer`. Vendored third-party skills are git-ignored; their URLs and licences are in `bakeoff/CONTENDERS.md`.

## Contenders

**Messaging:** house `staging` skill · house messaging-guide method · Stevekaplanai/pitch-deck-mastery-skill (MIT) · marcusnelson/presentation-writing-claude-skill (unlicensed, local use).
**Design:** anthropics/skills `canvas-design` · anthropics/skills `algorithmic-art` · pbakaus/impeccable (new-work) · impeccable `polish` over the html-ppt baseline · nicobailon/visual-explainer · lewislulu/html-ppt-skill.
**Review rubrics:** alchaincyf/huashu-design critique-guide · nexu-io/open-design design-review · Gabberflast/academic-pptx-skill · impeccable `critique`.

## The prompt

This is the prompt, verbatim, that generated the bake-off (Claude Code, Fable 5,
session homed in the house `assay-toolkit` repo; follow-up instructions during
the run are listed after it):

> I want to conduct a bake off on deck design tools. for 2 purposes.
> 1. creative presentation design
> 2. video presentations.
>
> the source for these presentation will be "Medici for RWA tokens", and we want a product pitch so the audience is educated on what Medici is, it's value prop in this space, and how the basic mechanism works.
>
> for each skill, I want 2 outputs.
> 1. with the brand design for medici.
> 2. with no brand "limits"
>
> first ask.
> 1. use anthropics canvas-design.
> 2. use algorthimic-art
> 3. potentially use impeccable to build it (if you can)
> 4. impeccable-design-polish
> 5. find 2 others using your websearch.
>
> second ask.
> 1. look for skills to help us build up the key messaging itself. (I believe we did something similar already.. if we did do 2-3 on the messaging.
>
> so 2 x 5 x 3 decks. (one for a deck, the other for a animated 'explainer' html that would get embedded into a video).
>
> for the video. don't do voice/mp4 generation.. just the html file that would be embedded into it
> fanout for this

Follow-up instructions given during the run:

- "for the messaging. did you run our 'house' messaging as well? if not please do. also is there a way for the messaging tools to review a deck? i would be interested to see how they judged a) themselves, but also the other participants in the bakeoff. (are there any tools to do this which are seperate?)"
- "for the reviews. I want a report showing how each messaging & design skill went. according to the AI tools. use the systems that 'won' the competition to build the final report. the report should go over what the bake off was about. who contended.. key things they all did, and what some of the issues were (that the reviews found). call that report.pdf."
- "we should also produce a video of the bake-off. it obviously use the winning solution, but we want to generate a talk-track and use our 'explainer' (from medici-platform). ideally when we do the notes section, it will include screenshots of the thing in question. this doesn't need to be in the 'assay' brand (or have any branding)"
- "do a sweep of the decks, and anonymize the other founders." / "also remove their names from source materials in this bakeoff" / "actually remove my lastname from sources an decks as well." / "make sure founders names aren't in final pdf and video"
- "in the final report. include the 'winning' explainer. (and produce the talk track for it)" / "1 video. not 2. the winning video will play after the report. (with a lead in)"
- "in the report, please ensure you name the skills that were in the bake-off and URLs for them"

## How it ran

1. Stage 1 — 4 messaging agents in parallel, each emitting its native artifact plus a normalized `staging.yaml` contract.
2. Stage 2 — 10 design agents (5 tools × 2 brand modes), each rendering all 3 original messaging contracts as deck + explainer (6 artifacts each); `impeccable-polish` ran after `html-ppt` as a refine-only pass.
3. Reviews — each messaging skill reviewed every messaging output including its own; 4 independent design rubrics + the messaging rubrics reviewed every rendered track; two Claude judges (messaging, design) wrote verdicts before Ian's.
4. Report + video — built with the winning messaging skill and design tool.

## Results (Claude judges; Ian's verdict recorded separately)

- **Messaging** — rank-sum across the four rubrics: house messaging-guide 8 · pitch-deck-mastery 9 · staging 10 · presentation-writing 13. Recommendation: `staging` as the transport contract + the house messaging-guide as the content gate. Details: `bakeoff/JUDGING-messaging-claude.md`.
- **Design** — brand mode: canvas-design (1st on 4 of 5 rubrics); free mode: impeccable (on ceiling; html-ppt/free the most robust); overall: canvas-design (rank sum 19 vs impeccable 22.5, visual-explainer 23.5 — close). Ship-tomorrow artifact: canvas-design / brand / staging, fixed in `winner/`. Details: `bakeoff/JUDGING-design-claude.md`.
- **Consensus issues** — no design skill has a timeline concept (all six built the explainer engine themselves); provenance/citation lines rendered below 4.5:1 contrast almost everywhere; messaging-contract vocabulary leaked onto slides in 4 of 6 tools; the brand linter false-errors on honest source citations; `polish` bought the craft floor but closed no composition finding; the review rubrics disagree by design (concept-led vs fidelity-led vs a11y-led).

## Licence

Apache License 2.0 — see `LICENSE`. Third-party skills retain their own licences (listed in `bakeoff/CONTENDERS.md`); the Medici source material in `source/` is © AAA Flowers S.A. and included as bake-off input only.
