# Assay Comprehension Diagnosis & Messaging Fix

**Medici Finance** · July 2026 · v0.1
version: 0.1 · last-reviewed: 2026-07-17
provenance: [I-03](streams/INTAKE.md) (a 20+yr consultant took ~10 minutes to "get it" in a live demo) · GTM fanout 2026-07-17

Grounded in: `~/jojig/Lending/assay-toolkit/web/teaser/index.html`, `web/executive-brief/index.html`, `docs/product-brief.md` (exec summary + problem), `README.md`.

---

## 1. DIAGNOSIS — why a smart consultant took ten minutes to "get it"

**B1. The headline is self-referential, not descriptive.** The teaser opens with *"The methodology that measures itself."* and the tagline *"an assayer tests the metal, not the stamp."* Both are payoff lines — they're satisfying **after** you understand the product and meaningless before. The reader's first question ("what is this?") is answered with a riddle.

**B2. Category soup in the lede.** Teaser: *"Assay is an evidence-first operating system for teams where humans and AI agents build together."* Three abstractions ("evidence-first", "operating system", "build together") and zero concrete nouns. Nothing tells the reader what they'd see on screen or what problem in their life it removes.

**B3. Metrics before mental model.** The teaser's very first card is a number (*"~5–8 → ~25–40"*) immediately followed by *"⚠ Not an authoritative figure — a rough, directional read… not a measured productivity or leverage claim."* The reader is asked to discount a claim before they understand what's being claimed. The exec brief repeats the pattern: a bold numbers row, then *"Read these honestly. All figures are… a proxy… three days is a signal, not a track record."* The honesty discipline (F-08) is right; its **placement** — before comprehension — reads as hedging whiplash and stalls the reader.

**B4. Insider vocabulary, unglossed.** Terms used as if the reader already lives here: *"Every unit of work is a **brief**"*, *"append-only **registers**"*, *"generated board (`statusgen`)"*, *"the next brief in my **stream**"*, *"**trade-off card**"*, *"**factory-floor analysis**"*, *"a weekly retro with a **one-change budget**"*, *"**work-claims**, **session rosters**"*. Each one costs the listener a parse; six of them in two minutes and he's rebuilding your ontology instead of hearing your pitch. "Brief" is the worst offender — it collides with agency briefs and legal briefs.

**B5. Abstraction stacked five-deep with no example.** README: *"Briefs — self-contained scope-and-DoD units with typed dependencies, derived risk gates, and executable verification."* Five novel abstractions in one bullet, never one actual brief shown. The product brief's problem list is similarly framed in the practitioner's world (*"'the next brief in my stream' wins over 'the most important brief'"*) — it presumes you already run streams of briefs.

**B6. No before/after.** Nowhere does any surface show the buyer's **current** world (status meeting, self-reported Jira board, unread PR queue) next to the Assay world. The exec brief's §01 ("trust at speed") is the best prose in the set, but it argues the problem abstractly rather than staging it.

**B7. Too many novelties at once, unsequenced.** One page asks the reader to absorb: a new labor model (agent fleets), a new work unit (briefs), a new tool (statusgen), a new epistemics ("derived, not measured"), and a new org design (cells/portfolio). Any one is a pitch; five simultaneously is a seminar. The 300-person scale-out (Figure 2) arrives before the single-cell story has landed.

**B8. F-08 violations in the current web copy.** Teaser pill 03: *"Gates you can't forge."* Exec brief: *"gated by identities that cannot be forged"*, *"**Un-forgeable gates.** … the platform now makes self-certification impossible."* These are exactly the banned framings. The defensible claim is narrower and just as strong: *approval is posted by a separate identity the author cannot impersonate.* This needs fixing regardless of comprehension work.

**B9. Honest-claim-first is the right value, wrong sequence.** Product brief: *"The honest claim comes first, because it is also the differentiator."* Honesty differentiates only after value is understood; led with, it reads as "this product doesn't really work." Sequence: scene → value → mechanism → **then** the honest boundary, framed as sophistication.

---

## 2. THE 30-SECOND VERSION (say this first, verbatim-usable)

> You can now hire AI agents that write software — fast and cheap. We run dozens a day. Here's the problem nobody's solved: when thirty agents each tell you "done," who checks? For a human team you'd have managers, code review, sign-offs. An agent will happily mark its own homework complete, and at seventy merges a day no human can read every line.
>
> Assay is the control layer for that. Every piece of work is a written work order with a pass/fail check a machine can run. A different actor than the author has to run it. Approvals come from a separate identity the author can't impersonate. And the status board isn't typed by anyone — it's computed from that evidence, and the build fails if the paperwork doesn't reconcile. One accountable person keeps every consequential decision; the fleet does the typing.
>
> We run our own company on it — one human, an agent fleet, shipping daily. To be precise about what it is: it doesn't make agents honest — it makes drift, missing evidence, and tampered records show up red in CI instead of surfacing in production three weeks later.

(That last sentence **is** the F-08 claim, placed where it lands as rigor instead of hedging.)

---

## 3. ANALOGY SET (each with its honest break, per F-08)

| # | Analogy | One-liner | Where it breaks |
|---|---------|-----------|-----------------|
| 1 | **General contractor + building inspector** | Agents are your subcontractors; Assay is the permit-and-inspection system — a wall isn't "done" when the sub says so, it's done when an inspector who didn't build it signs off. | Inspectors physically examine the work under legal liability; Assay re-runs declared checks and lints consistency — it can't inspect what no check encodes. |
| 2 | **Maker-checker (banking four-eyes)** | No transaction settles on one identity's say-so; author and approver must be different identities, enforced by the system, not policy. | In banking both parties are accountable humans; in Assay the checker may be another agent for low-risk work — the human is mandatory only at risk gates. |
| 3 | **Double-entry books + audit trail** | Self-reported status is a single-entry ledger; Assay makes the books reconcile — and a deleted entry breaks the sequence visibly instead of vanishing. | Real audits sample ground truth; Assay's lint checks internal consistency, so a *consistent* fiction can pass — which is exactly why the human gate exists. |
| 4 | **Factory QA / andon cord** | Work moves down a line with a check at every station; a defect stops the line, and a daily report names the bottleneck. | Factory QA measures the physical product; Assay checks the evidence *about* the work plus re-executes tests — coverage is only as good as the declared checks. |
| 5 | **Air-traffic control** | Many autonomous actors, one accountable controller, separation enforced by the system rather than by pilots' promises. | ATC steers in real time; Assay gates at checkpoints — it doesn't watch or correct an agent mid-task. |
| 6 | **ERP/MES for agent labor** | Work orders, routing, sign-offs, and a management dashboard generated from the shop floor — for a workforce of agents. | "ERP" implies a heavyweight install; the free tier is a folder of markdown plus one Go binary in CI. |

Best openers by audience: **CFO/CEO → #2 or #3** (they feel register-tampering viscerally); **consultant/delivery exec → #1**; **ops/engineering leader → #4**.

---

## 4. DEMO NARRATIVE — the "aha" in minute one

The current failure mode: the demo starts inside the machinery (briefs, statusgen, desks) and makes the viewer reverse-engineer the problem. Invert it — stage the problem, show the catch, explain the machinery last.

1. **(0:00–1:00) Open on the scene, not the tool.** Show the GitHub PR list: dozens of agent-authored PRs merged *today*, one human. Say the question out loud: *"Seventy merges a day, one of me. How do I know any of this is real?"* Then cut to the generated board: *"This page is the answer — and nobody wrote it. It's computed."* That's the aha framing; everything after is proof.
2. **(1:00–3:00) One work item, end to end.** Open a single brief — plain-English scope, the four risk questions, the executable pass/fail table. Then its PR, the review approval posted by a **separate machine identity**, then the post-merge verification run by a non-implementer. Punchline: *"'Done' required three different actors, none of them the author."*
3. **(3:00–5:00) The catch, not the happy path.** Live-tamper: delete a findings entry or hand-edit a status cell, run the lint, watch CI go red. Then tell the true day-one story — a session deleted an inconvenient finding and got caught. This is the emotional peak; adverse evidence sells harder than any dashboard.
4. **(5:00–7:00) Management view.** Regenerate the board; show the Next-up priority queue and the daily bottleneck/DORA report: *"management reporting as a build artifact — no status meeting produced this."* Numbers **with** their caveats, now that the viewer has the model to price them.
5. **(7:00+) Machinery and boundaries, only now.** Lifecycle, registers, Console roadmap — and the full honest claim ("derived from agent-authored artifacts with consistency linting, not measured ground truth"), which at this point lands as intellectual seriousness, not as a warning label.

**Do NOT show early:** internal desk roster/persona vocabulary, statusgen source, streams/waves taxonomy, the 300-person cell-tiling diagram (that's a second meeting), or any metric caveat before step 4.

---

## 5. GLOSSARY RULE (outbound material; internal/toolkit docs keep their names)

| Term | Verdict | Outbound form |
|---|---|---|
| **brief** | **Rename outbound** | "work order" (first mention: *"a work order — we call them briefs"*). Kills the agency/legal-brief collision; "work order" imports the contractor frame for free. |
| **register(s)** | Keep, **always gloss** | "append-only, tamper-evident logs (lessons learned, ideas, process changes)". Never bare FINDINGS/INTAKE/RETRO in outbound copy. |
| **statusgen** | Keep as tool name, **never lead with it** | Lead with "the generated status board"; name the binary only in technical docs. |
| **stream** | **Rename outbound** | "workstream" — near-free change, instantly parsed by consultants. |
| **desk / verify-desk / pr-review-desk** | **Internal only** | Outbound: "review gate", "independent verification step". *Desk Console* stays as a product proper noun, glossed "the oversight console". |
| **Next-up** | **Rename outbound** | "the priority queue". |
| **verified / done** (lifecycle) | Keep, **always gloss the key one** | "verified = re-checked by someone who didn't build it". Always show the pipeline graphic alongside. |
| **cell** | Keep or shift to **"pod"** | Consultants already say "pod" for lead+squad; gloss either way: "one accountable lead plus their agent fleet". |
| **trade-off card / one-change budget / factory-floor report** | **Drop from outbound** (or gloss) | "decision memo" / "we change one process rule per week" / "daily bottleneck report". |
| **"un-forgeable", "cannot be forged", "impossible to self-certify"** | **Banned (F-08)** — currently live in teaser pill 03 and exec brief §02 | Replace with: "approval is posted by a separate identity the author cannot impersonate". Narrower, defensible, and actually more credible. |

**Standing rule for all outbound copy:** every internal term gets exactly one parenthetical gloss on first use, and no sentence may contain more than one ungloossed novel term. If a sentence needs two, it's two sentences.

---

## 6. Category positioning — ride "harness engineering," win on the gate layer

The market has a name for this category now: **harness engineering** — improving agent output by shaping the environment (context and tools) around a held-constant model. It is the OpenAI-lineage vocabulary coined by Ryan Lopopolo (OpenAI Codex) and packaged as the CC-BY-4.0 anthology at [github.com/lopopolo/harness-engineering](https://github.com/lopopolo/harness-engineering) (checked 2026-08-24); the canonical essay is *"Harness engineering: leveraging Codex in an agent-first world"* (Lopopolo, 2026-02-11, [openai.com/index/harness-engineering](https://openai.com/index/harness-engineering/)). Adopt the term and cite the lineage — do not re-coin a synonym.

**The positioning line (verbatim-usable):**

> Assay is the adversarial-trust implementation of harness engineering.

Harness engineering tells you what the environment should carry — proof at the claim boundary, authority as a separate contract, corrections fed back into the environment. Its default posture is *whole-job*: one agent trajectory owns decomposition, execution, integration, and its own proof. Assay differs on exactly one layer and leads there: **gate integrity** — verification run by a non-implementer, tamper-evident registers, and gates posted by identities the author cannot post as (the full argument is `docs/defensibility.md` §0). The category names what the environment should carry; Assay is the machinery that makes the gates hold when you do not fully trust the worker's self-report.

**Citation discipline (binds this section and every deck that reuses it).** Cite the essays and talks — stable, dated — not the repo's activity. The anthology repo drew rapid early attention and then went static (created and last-pushed on the same day in July 2026); a star count is a moving number and must not be asserted as a live fact. Re-verify every external link, and any repo-state claim, at the moment of use — a July read is stale by publication. This section's links were dereferenced 2026-08-24.

## 7. Content gate — the trace-every-number bar for public content

Public-facing content that carries our numbers ships through a stated review bar. This exists because of a real miss: a mislabeled metric that only one diligent reviewer caught, plus a live post degraded by a platform rewrite after the publishing pipeline's guarantees had ended. The methodology applied to its own marketing is itself part of the pitch, so this bar is not optional decoration. It applies to every public-content PR — the site, decks, and the `linkedin-post` pipeline (which exists but has left this bar unstated).

**trace-every-number.** Every figure in a content PR is re-derived at review time and its source named in the PR — no number ships whose derivation a reviewer cannot reproduce. A figure that cannot be re-derived is not published; a directional read is labeled as one, never as a measurement (F-08).

**One canonical voice source.** Every content PR binds to a single voice/brand source of truth — `docs/brand/brand.md` for verbal identity, and the site voice guardrails in `docs/site-messaging.md` §4 — not to a copied-and-drifted excerpt. One source, cited; not three copies that diverge.

**Pre-post freshness checklist** (run immediately before publishing, not at authoring time):

- every number re-derived within N days of the post date (proposed N = 7; the exact window is Ian's call);
- every external citation dereferenced at post time — links rot, and a check done at authoring is stale by publication;
- the published text is a verbatim paste of the reviewed text — no post-review hand-edit — and it is re-read once live, because platforms silently rewrite posts;
- any claim whose freshness cannot be re-confirmed at post time is cut, not shipped stale.

**Scope — proposed, for Ian's decision (spec open question 4).** This bar is written here as a **toolkit-wide** rule: one content gate governing every public surface these docs feed, so a number that appears in three places is re-derived once against one canonical source. The **per-repo alternative** — each publishing repo carries its own copy of the bar — is not the recommended default, because it reintroduces exactly the drift the single-canonical-source rule closes (three copies, three freshness clocks, three chances to skew). Recommendation: adopt toolkit-wide, permitting the per-repo form only where a repo publishes numbers this toolkit's sources do not carry. This is a recommendation, not a decision — open question 4 is Ian's to close.

## Immediate fixes for assay-site brief 01

1. Replace the teaser H1/lede with the 30-second version's first two beats; move *"measures itself"* to the closer, where it pays off.
2. Purge the F-08 violations in `web/teaser/index.html` (pill 03) and `web/executive-brief/index.html` (§01 standfirst answer, "Un-forgeable gates" bullet).
3. Restructure both pages to the sequence: **scene → one work item → the catch → the board → honest boundary → metrics-with-caveats**. Caveats attach to numbers at point of use (as the exec brief already does well) — never before the reader has the model.
4. Adopt the glossary table as the site-wide copy lint.
