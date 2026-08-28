# Contenders — names, origins, licences (for report.pdf)

## Messaging skills (4)
| id | skill | origin / URL | version | licence |
|---|---|---|---|---|
| staging | house `staging` skill (genre → audience → arc → staging.yaml) | medici-finance house, packaged from loom-bakeoff 2026-08-18: `loom-bakeoff/skills/staging` | v2 (2026-08-18) | house |
| house-guide | house messaging method — comprehension diagnosis → 30-second version → analogies with honest breaks → glossary → trace-every-number gate | medici-finance/assay-toolkit `docs/messaging-guide.md` | v0.1 (2026-07-17) | house |
| pitch-deck-mastery | pitch-deck-mastery-skill — 12-slide framework, must-pass checklist | https://github.com/Stevekaplanai/pitch-deck-mastery-skill | 2026-08-16 | MIT |
| presentation-writing | presentation-writing-claude-skill (`powerpoint-keynote-presentation`) — persuasive slide-by-slide narrative outlines | https://github.com/marcusnelson/presentation-writing-claude-skill | 2026-08 | **no LICENSE file** (local use only) |

## Design tools (6)
| id | skill | origin / URL | version | licence |
|---|---|---|---|---|
| canvas-design | Anthropic `canvas-design` — design-philosophy manifesto → visual canvas | https://github.com/anthropics/skills/tree/main/skills/canvas-design | main @ 2026-08-27 | Apache-2.0 |
| algorithmic-art | Anthropic `algorithmic-art` — p5.js seeded generative art | https://github.com/anthropics/skills/tree/main/skills/algorithmic-art | main @ 2026-08-27 | Apache-2.0 |
| impeccable | impeccable — frontend design craft playbook (new-work, craft-floor, detect.mjs) | https://github.com/pbakaus/impeccable | 4.0.4 | Apache-2.0 |
| impeccable-polish | impeccable `polish` (+ `animate`) applied over the html-ppt baseline | https://github.com/pbakaus/impeccable | 4.0.4 | Apache-2.0 |
| visual-explainer | visual-explainer — self-contained HTML explanations, diagrams, slide decks (web-found) | https://github.com/nicobailon/visual-explainer | 0.10.0 | MIT |
| html-ppt | html-ppt-skill — HTML PPT Studio: 36 themes, 31 layouts, 27 animations (web-found) | https://github.com/lewislulu/html-ppt-skill | 2026-08 | MIT |

Web-search sources for the two "found" tools: https://github.com/ToseaAI/awesome-html-slide-skills and https://tosea.ai/blog/best-html-slide-skills-library-2026.
Excluded as already judged in loom-bakeoff (2026-08-18): huashu-design, frontend-slides, appautomaton/presentation; excluded on licence/provenance: guizang-ppt-skill (AGPL-3.0), jiji262/claude-design-skill.

## Independent review rubrics (4) + the 4 messaging skills reviewing as rubrics
| id | rubric | origin / URL | licence |
|---|---|---|---|
| huashu-critique | huashu-design `critique-guide.md` — six scored dimensions, Concept hard-veto | https://github.com/alchaincyf/huashu-design | MIT |
| open-design-review | nexu-io open-design `design-review` (Design Jury: critic .4 / brand .2 / a11y .2 / copy .2) | https://github.com/nexu-io/open-design | Apache-2.0 |
| academic-pptx | academic-pptx-skill — action titles, ghost-deck test, exhibit discipline | https://github.com/Gabberflast/academic-pptx-skill | MIT |
| impeccable-critique | impeccable `critique` + `detect.mjs` + craft-floor | https://github.com/pbakaus/impeccable | Apache-2.0 |

## House render/video pipeline (used for the bake-off video)
| explainer-video | TTS → Playwright-recorded explainer.html → subtitles → H.264 | medici-finance/medici-platform `tools/explainer-video` + `.claude/skills/video-design` | house |
