# Bake-off protocol — deck design tools × messaging skills, RWA pitch

Ruled by Ian, 2026-08-27. Brief: `../BRIEF.md`. Pattern inherited from
`../../loom-bakeoff/bakeoff/PROTOCOL.md` (2026-08-18).

## Contenders

### Messaging (stage 1 — runs first, feeds every design contender)
| id | skill | origin | licence |
|---|---|---|---|
| `staging` | `skills/messaging/staging` | house — loom-bakeoff winner (genre→audience→arc, staging.yaml) | house |
| `presentation-writing` | `skills/messaging/presentation-writing/powerpoint-keynote-presentation` | github.com/marcusnelson/presentation-writing-claude-skill — persuasive narrative outlines, "argument not design" | **no LICENSE file** (local use only) |
| `pitch-deck-mastery` | `skills/messaging/pitch-deck-mastery` | github.com/Stevekaplanai/pitch-deck-mastery-skill — 12-slide framework, must-pass checks | MIT |

### Design (stage 2 — each renders deck + explainer × brand + free × 3 messagings = 12 artifacts)
| id | skill | origin | licence | note |
|---|---|---|---|---|
| `canvas-design` | `skills/design/canvas-design` | anthropics/skills — design-philosophy→visual canvas (PNG/PDF poster art) | Apache-2.0 | not a deck tool; philosophy step drives an HTML render |
| `algorithmic-art` | `skills/design/algorithmic-art` | anthropics/skills — p5.js seeded generative art | Apache-2.0 | strongest fit for the explainer's motion; deck uses generative backplates |
| `impeccable` | `skills/design/impeccable` (v4.0.4) | pbakaus/impeccable — new-work / craft playbook | Apache-2.0 | Persuade mode; DESIGN.md per brand mode |
| `impeccable-polish` | same skill, `polish` (+`animate` for the explainer) command | pbakaus/impeccable | Apache-2.0 | applied ON TOP of the `html-ppt` output as the "baseline + polish" contender |
| `visual-explainer` | `skills/design/visual-explainer/plugins/visual-explainer` | nicobailon/visual-explainer (web-found, 8.8k★) — technical-diagram / editorial explainers | MIT | strongest fit for mechanism diagrams |
| `html-ppt` | `skills/design/html-ppt-skill` | lewislulu/html-ppt-skill (web-found, 6.4k★) — 36 themes, 31 layouts, 27 animations | MIT | baseline template-driven deck tool |

Web search sources: ToseaAI/awesome-html-slide-skills (curated 2026 list),
tosea.ai/blog/best-html-slide-skills-library-2026. Excluded: huashu-design,
frontend-slides, appautomaton (already judged in loom-bakeoff); guizang-ppt
(AGPL); jiji262/claude-design-skill (Anthropic system-prompt provenance).

## Rules
- Same source corpus for everyone (`../source/`). No invented numbers.
- Stage 1 before stage 2. Design contenders consume `messaging/*/staging.yaml`
  verbatim (no reorder, no claim rewrite).
- Results stay local. Videos deliver SCRIPT.md + explainer.html; Ian renders.
- Every contender writes NOTES.md: time-to-artifact, friction, overrides
  needed, what the tool refused or could not express, brand fights.

## Judging (two independent judges: Claude, then Ian)
Axes, per loom-bakeoff: (1) tool difficulty; (2) representation quality —
coverage of the three educational goals, correctness vs source, emphasis.
Extra axis here: (3) **brand-mode delta** — how much better is `free` than
`brand`, and does `free` still read as Medici? And for messaging: do the
three contenders tell the same story or different ones, and why (trace to the
methodology). Deliverables: `JUDGING-messaging-claude.md`,
`JUDGING-design-claude.md`; Ian's verdicts alongside.
