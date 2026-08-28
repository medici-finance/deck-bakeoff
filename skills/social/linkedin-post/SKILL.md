---
name: linkedin-post
description: Find post-worthy material in the Assay/Medici repos and draft a PAIR — a long-form practitioner article plus a LinkedIn summary post — in Ian's voice, saved via a draft PR (article in docs/articles/, summary in docs/articles/linkedin/YYYY-MM-DD-<slug>.md). Use when asked to "draft a linkedin post", "write a post/article about X", "find something worth posting", or on a recurring content cadence. NEVER posts to LinkedIn itself — output is draft files; Ian posts manually.
---

# LinkedIn Pair Generator (article + summary)

Every run produces a PAIR from real material in the repos: a **long-form article** (the
deep piece — method, numbers, the hedge) and a **LinkedIn summary post** derived from
it. The audience for both: recruiters, hiring execs, and senior engineers. The
strategic frame (2026-07): Ian is a fintech CTO whose differentiator is *operating
AI-agent fleets under real controls* — both artifacts are practitioner evidence of
that, never product marketing.

The pairing exists because a 200-word post can carry one insight but not the method.
The article is where a reader learns to run the diagnosis themselves; the post is the
door. `source:` in the post frontmatter MUST point at the paired article. If an article
already covers the material (sweep step below), do not write a duplicate — draft only
the summary and point `source:` at the existing article.

**On the weekly blog cadence the pair becomes a TRIPLE**: long-form article + summary
post + the **blog bundle** — a publish-ready per-article directory delivered as one
held PR to the `../assay-site` repo. The bundle is the third output added by
assay-blog/07; its format and lifecycle are pointers, not copied specs — see
[The blog bundle (third output)](#the-blog-bundle-third-output) below.

All three legs are the definition-of-done, not two-plus-an-optional: a blog bundle
delivered without its paired LinkedIn summary is an incomplete delivery — a defect to
catch, not a partial success. The summary is the leg that goes silently missing (a real
article once shipped its bundle with no blurb), so the pipeline treats "summary filed at
`docs/articles/linkedin/<date>-<slug>.md`, `source:` pointing at the article" as a
required precondition of the bundle delivery, checked by the delivery gate in the weekly
operating checklist (`docs/streams/assay-blog/weekly-checklist.md`). The summary lives in
this repo and the bundle in `../assay-site` — a sibling PR, never one moved into the
other; the private summary does not migrate into the public site tree.

## Hard rules (violating any of these kills BOTH artifacts)

1. **Practitioner voice, never founder or sales voice.** No polls, no CTAs, no "how
   would you consume this", no marketplace/SaaS/pricing/design-partner language, no
   "we're building/launching". Each artifact ends when its insight lands — no funnel.
   **One bounded exception (a site-owner-directed exception, 2026-08-20):** exactly one
   subscribe CTA to the site's own blog index (`assay.guide/blog/`) is permitted on a
   blog-cadence post. That is the entire license — a single subscribe CTA, to the
   owner's own blog, added at the site owner's direction — NOT a general CTA / poll /
   funnel license. Every other CTA stays banned, and "each artifact ends when its
   insight lands" still governs everything else; the subscribe line is the only thing
   that may follow the insight, and only on a blog-cadence post. The article may name
   products sparingly where the incident requires it; it never pitches them.
2. **No productivity multipliers, ever** ("worth N engineers", "10x"). House rule:
   most published AI-productivity figures fail an adversarial audit; ours don't get to
   join them.
3. **Every claim about our own tooling, process, or state must be verified at draft
   time** against current code and the current issue tracker — never from memory and
   never carried over from an earlier draft. Every number must be traceable to a
   re-runnable command you ran this session, a register entry (FINDINGS/retro) you
   confirmed is current, or a published article — and in the ARTICLE, the
   command/query appears inline next to the number it produces. A number whose source
   wasn't checked this session is decoration. Stale numbers get re-derived, not
   reused.
   **One bounded exception — testimony numbers (editorial-lessons/04, from
   `docs/research/2026-08-21-brokk-blog-writing-lessons.md` §2.2–2.3, lesson L5):** a
   genuinely experiential quantity — one that no re-runnable command, register entry,
   or published article can produce — may appear ONLY when explicitly labeled as
   testimony: sourced to the author's own stated practice with its span named ("in a
   year of running this desk, roughly…"), and presented as observation, never as
   measurement, benchmark, or study. That is the entire license. Wherever a verifiable
   source exists, the verified path above stays MANDATORY — testimony is the fallback
   for what cannot be measured, never a cheaper substitute for what can. It is NOT a
   license against the other rules: productivity multipliers stay banned regardless of
   labeling (rule 2 is not routable-around by calling the multiplier testimony), and
   tense honesty (rule 9) and the de-slop checklist bind a testimony sentence like any
   other. Both artifacts get the device; in the ARTICLE the span/source framing
   appears inline next to the number, in the same position this rule gives a
   command. The register, worked:
   - compliant testimony: "In a year of running this desk, roughly two briefs a week
     stalled on a stale Verify table — my count, not a measurement."
   - the same quantity dressed as measurement (banned): "Two briefs a week stall on
     stale Verify tables."
4. **The hedge stated, unflattering numbers kept.** The hedge is the brand: the
   article carries a dedicated `## the hedge` section — confounds, scope limits,
   trade-offs, live disclosures. (Renamed from "confounds" 2026-08-14: that word
   was technically narrow for what the section carries, and a label-style header
   sat against the de-slop rule that headers are assertions; `the hedge` is the
   house idiom doing the work.) The post carries at least one hedge line.
5. **No URLs, no release dates, no repo names in the POST body — with a bounded
   sanctioned-URL set:** (a) the paired article's canonical assay.guide blog URL, once
   the blog actually serves it (Ian's ruling, 2026-08-19, with the assay-blog stream);
   and (b) the site's own blog index (`assay.guide/blog/`), permitted solely as the
   target of the single site-owner-directed subscribe CTA sanctioned in hard-rule-1 (a
   site-owner-directed exception, 2026-08-20). No other URL is sanctioned. The
   exception is state-aware: until the article is published at assay.guide, the rule
   applies unmodified; a link to an unpublished or non-blog location is still banned.
   The blog-index URL rides only with that one subscribe CTA — outside it, a bare blog
   index link is not sanctioned. Everything else stays banned in the post body. In the ARTICLE: never
   cite a private repo's name, a private repo's URL, an internal PR/issue number, or an
   unreleased/on-hold plan — even when the owning repo's own other articles already do
   this. That an existing article sets that precedent is not permission; it is a defect
   to flag, not copy. Describe the incident without the identifying number or link
   instead. This rule binds the article the same as the post; the "POST body" scope in
   the header names where it is strictest, not where it stops applying.
6. **Never publish.** This skill writes draft files and opens a draft PR. Posting is
   Ian's manual act. Do not automate it, offer to automate it, or mark
   `status: posted` yourself. An accuracy-review verdict is never publication
   clearance — at most "fit to be considered." `status: approved` records
   accuracy-review completion only, and is set by nobody but Ian. The PR body
   carries the sentence "A review approval on this PR is accuracy-review
   completion only, not publication clearance" so it reaches the reviewer.
7. **Never run finished text through LinkedIn's (or any platform's) AI rewrite.** It
   re-slops the voice (2026-07-21 incident: a post about avoiding AI slop shipped in
   slop register and had to be edited live). The drafts ARE the final text; paste
   verbatim.
8. **De-slop pass is mandatory for BOTH artifacts before commit** — see checklist
   below. Run it even on text you just wrote; especially on text you just wrote.
9. **Every capability, tool, report, or control is written in the tense it actually
   occupies.** If it is proposed, filed, or in flight — not built — it either carries
   the assay-and-jira disclaimer device (a prominent block at the top stating the
   capability is not built and not scheduled; see
   `docs/articles/assay-and-jira.md` in `medici-finance/assay-toolkit` for the
   pattern — the exemplar exists only in this repo, so a draft landing in another
   repo's tree has no local file to copy from and must fetch this one) or is cut from
   the draft. "We have" means it ships.
10. **Before drafting, resolve every described weakness to fixed-or-open** against
    the issue tracker. State the resolution for each in the PR body. Weaknesses still
    open are routed to the disclosure block and never described as if publication is
    safe by default.
11. **Write about roles and organizations, not named people.** A failure or decision
    narrative is told through the function ("the reviewer", "the on-call engineer",
    "the desk") and the org, not a person's name or handle. This is the default, not a
    judgment call to defer — the Disclosure "Identifiable people" category exists for
    the residue that survives this rule (someone identifiable by context even without a
    name), which the block surfaces so Ian can decide; it is not the mechanism for
    catching names that should never have been drafted in the first place.
12. **State security posture accurately or not at all.** Any gate, credential/token
    handling, App or agent identity, or control named in a draft must say precisely
    what it does and does not catch — never imply broader coverage than the code
    provides. When the material is a "gate that caught something" (a preferred pattern
    per the hunt order below), verify at draft time exactly what class of failure it
    catches and state that scope, not a generalized "this keeps us safe."

## De-slop checklist (run against article AND post, line by line)

- Banned tokens, zero tolerance: "leverage" (verb), "landscape", "in the realm of",
  "delve", "journey", "robust", "seamless", "game-changer", "revolutionize", "unlock",
  "empower", "supercharge", "elevate", "in today's fast-paced world", "Let's dive in",
  "it's worth noting", "furthermore".
- No Title-Case Listicle Headers; headers are lowercase assertions ("the reject lane
  has rusted shut"), not labels ("Key Takeaways").
- No adjective doing a number's job: "massive backlog" → "<N> open issues". If an
  adjective survives, it must be earning irony or verdict, not size.
- No rhetorical-question openers, no "So, what does this mean for you?" transitions.
- Every sentence states a fact, a sourced number, or a judgment earned from one in the
  same section. Sentences that do none of these get cut.
- Read the last paragraph aloud: if it sounds like a keynote close or a pitch, delete
  it and end on the previous insight.
- No bold mini-headings on list items ("- **Grep your docs.** Every…" → "- Grep your
  docs. Every…"); bold is for the one planted learning sentence at most, and even that
  reads better plain. (humanizer §15/§16, adopted 2026-08-22.)
- Stock adverbs cut on sight: "actually", "quietly", "simply", "just" (as filler),
  "truly", "genuinely". (humanizer §7.)
- A passive with no agent names one: "the paragraph was never updated" → "nobody
  updated the paragraph". Passives with a named agent ("retired by ruleset") stay.
  (humanizer §13.)
- After the checklist, run the humanizer read (article-craft gate 3b) with the
  genre's exemplar as the writing sample; apply, then re-check cadence.

## Voice contract (from the published articles)

- **Lead with a failure or a damning number**, then earn the thesis from it. Never
  open with a win or a thesis statement.
- First person; long em-dash sentences alternating with abrupt two-beat verdicts
  ("The models were not the problem. The valve was.").
- Signature register, used sparingly (max one per POST; the article gets latitude but
  not repetition): assayer/metal-vs-stamp, gates, unreliable narrators, "done is a
  gate you pass", segregation of duties.
- Post: 120–220 words, one idea, line breaks between beats. Article: 800–1600 words,
  one method or one incident fully worked — sections, real commands, a metrics table
  where the material supports one, the hedge section, ends on the insight.
- The controls/segregation-of-duties frame is the through-line back to 30 years of
  compliant financial infrastructure — audit vocabulary (maker-checker, independent
  verification, audit trail) over dev-tool vocabulary where both fit.

## Cadence pass (after verification, before de-slop)

Once every claim is verified and both artifacts are content-complete, run the
`prose-cadence` skill (`.claude/skills/prose-cadence/SKILL.md`) over BOTH
artifacts: at most 2–3 devices per piece, registers diegetic-only, and its
precedence section defers to this skill's hard rules. It implements this voice
contract's rhythm clause (em-dash suspension alternating with two-beat
verdicts) rather than competing with it. The de-slop checklist re-runs AFTER
the cadence pass — cadence edits can reintroduce slop.

## Where to hunt for material (sweep in this order)

1. **`docs/articles/*.md`** here and in `../option-index-tracker/docs/articles/` — the
   deep source; check for sections not yet turned into posts (compare against
   `docs/articles/linkedin/` slugs and each post's `source:` frontmatter).
2. **`../option-index-tracker/docs/streams/findings/`** — named incidents with dates
   and lessons. The best pairs are failure-led; this is the failure register.
3. **Fresh metrics**: `statusgen --dora` **run from this repo's root** — the pinned
   `statusgen` release binary on `PATH` reads the board. statusgen is dehoused to public
   `medici-finance/assay` and consumed everywhere (this repo included) as a
   checksum-verified pinned binary via `.assay-versions` / `make statusgen-install`;
   there is no repo-local source to `go run`. Use `--dora` for current
   lead-time/throughput/change-failure numbers; the retro register for process changes
   that moved a number.
4. **Recently merged PRs / closed issues** with a surprising mechanism (a gate that
   caught something, a verifier that failed something review passed, a reviewer that
   ruled against its own interest).

Pick ONE item with: a concrete incident or number, a lesson that generalizes beyond
this codebase, and relevance to "how do you run AI agents safely". Prefer material NOT
already covered by an existing post slug (sweep ALL THREE linkedin dirs — this repo,
`jojig-dao/daml-option-index-tracker`, `medici-finance/reconciler`).

## Disclosure (applies to BOTH artifacts)

These categories must be surfaced in the PR body for every draft; the skill
identifies and enumerates them — it never clears them. Ian decides what (if
anything) to redact.

- **Fleet volume / throughput figures.** Agent fleet size, task counts,
  throughput rates, and any metric that implies current operational scale.
- **Still-open weaknesses.** Any weakness described in either artifact that
  remains open in the tracker (see rule 10) — state "open as of <date>" in the
  disclosure block.
- **Invalid-delivery-metrics disclosure.** Any metric known to be inflated or
  stale at draft time, with the direction and magnitude of the distortion.
- **Identifiable people.** Any person identifiable by context in a failure
  narrative — the disclosure block names them so Ian can decide.
- **Internal system/tool identities.** Any internal tool, system, or
  configuration name that appears in the artifact. The article may keep them
  where the incident requires them; the disclosure block registers them.

## Output

1. **Article**: `docs/articles/<slug>.md` in the repo that owns the source material,
   matching that repo's article header conventions (in this repo: H1 title with a
   colon-assertion, `**Assay · by Medici** — <Month Year>` byline, no YAML
   frontmatter). Method-first: a reader should be able to re-run the diagnosis or
   replicate the control from the article alone.
2. **Summary post**: `docs/articles/linkedin/YYYY-MM-DD-<slug>.md` (draft date, kebab
   slug) with the frontmatter block defined in that directory's README
   (`date/slug/status: draft/posted:/source/hook`). **The post always lands in
   `medici-finance/assay-toolkit`** — this is the one repo with a maintained
   `docs/articles/linkedin/` directory and README that Ian actually reviews for
   posting; it is the post's home regardless of which repo owns the source article.
   `source:` points at the paired article — same-repo relative path, or
   `<repo>/docs/articles/<slug>.md` when the article lives elsewhere (see the README's
   frontmatter example) — plus underlying registers/PRs as secondary pointers.
3. When the article's repo (step 1) is NOT `assay-toolkit`: the pair ships as two
   sibling PRs — one in the source repo for the article, one here for the post — and
   each PR body links the other and states it is one half of a pair. Otherwise land
   BOTH via one feature branch + draft PR in this repo (the pair is one unit; never
   split it when both live here, never batch two pairs in one PR). Skip the article
   only when `source:` points at a pre-existing article that already carries the
   method.
4. In the PR body: the hook, the source pointers, which numbers were re-derived vs
   quoted, the resolution of each described weakness (fixed or open, per rule 10),
   a disclosure block enumerating every instance found in the categories listed
   in the Disclosure section, the sentence "A review approval on this PR is
   accuracy-review completion only, not publication clearance," and a line
   confirming the de-slop pass ran on both artifacts.
5. **Distribution mode decides the image artifacts** (Ian's ruling, 2026-08-19).
   Two modes:
   - **Blog-linked** (the default once the paired article has an assay.guide blog
     home): the post carries the blog URL (rule 5's exception); the long-form is
     NOT pasted into LinkedIn's article editor; **no table twins and no LinkedIn
     cover are produced** — the blog bundle's cover/`og:image` carries the share
     card and the blog page renders real tables.
   - **Editor-pasted** (any piece whose article does NOT land on the assay.guide
     blog — off-assay material, repo-only pieces): the twin and cover
     requirements below apply in full.
6. **Editor-pasted mode: every table in the article ships with a PNG twin.**
   LinkedIn's article editor cannot render a table — pasting flattens it to
   run-on text — so each markdown table gets a rendered image for insertion at
   posting time: a self-contained HTML source AND the rendered PNG committed
   together under `docs/articles/img/<slug>/`, with the exact re-render command
   in a comment at the top of the HTML, and an HTML comment above the markdown
   table pointing at the twin. Light surface only (LinkedIn articles render on a
   white page; a PNG cannot theme-switch), tokens and status colors from the
   dataviz skill (icon + label, never color alone), rendered at 2× device scale.
   The markdown table stays the source of truth for repo readers; the PNG is a
   projection, regenerated whenever the table changes. Leak rules bind the image
   exactly as they bind the text — a withheld token in a PNG is still a leak,
   just one grep cannot see, so the twin renders only strings already cleared in
   the article.
7. **Editor-pasted mode: every article ships a cover image.** LinkedIn's article
   editor takes a cover/banner above the title; without one the header and the
   share card go dead. Same mechanics as the table twin: `cover.{html,png}` under
   `docs/articles/img/<slug>/`, re-render command pinned in the HTML, dataviz
   tokens on the light surface, 1920×1080 with the critical content in the
   central band (feed shares crop toward 1.91:1). The cover is drawn from the
   piece's own mechanism — never stock imagery, never a text card. LinkedIn
   prints the title directly beneath the cover, so the cover must not restate
   it; text inside stays to one motif line plus the byline. Leak rules bind it
   like any artifact. (Blog-linked mode skips both: one image lane — the blog
   bundle's cover/thumb — serves the blog page, the LinkedIn unfurl, and the
   mail teaser.)

## The blog bundle (third output)

On the weekly blog cadence, after the article + post pair is verified, de-slopped, and
content-complete, the pipeline produces a **third output**: the per-article **blog
bundle**, a publish-ready directory for the public /blog on assay.guide. The pair — both
the article AND its LinkedIn summary — is a **precondition** of this third output: the
bundle is not deliverable until the summary is committed at
`docs/articles/linkedin/<date>-<slug>.md` with `source:` pointing at the article. The
weekly operating checklist's delivery gate
(`docs/streams/assay-blog/weekly-checklist.md`) is what catches a bundle handed off
without its blurb. This does NOT
change the pair — the article stays the source of truth in `docs/articles/`; the bundle
is a projection of it into the site's bundle format. Everything below is referenced **by
pointer**; do not copy the referenced lane specs into this skill or into the bundle PR.

**Where the bundle lands.** One directory per article in the private `../assay-site`
repo, at `public/blog/<category>/<slug>/`. Category is one of the fixed v1 vocabulary
(`thought-leadership` · `how-assay-works` · `tooling-updates` · `learnings`) — see
`docs/streams/assay-blog/spec.md` §2 in `medici-finance/assay-toolkit`.

**What the bundle contains** (each item's format is owned by another lane — pointer only):

- `index.html` — the article rendered into the site's **article template**, with its
  metadata in the `<script type="application/json" id="assay-article">` block. Template
  and bundle format: assay-blog/**01** (`docs/streams/assay-blog/brief-01-ia-bundle-template.md`)
  and spec §2. Public metadata carries NO internal identifiers (spec §2, §4).
- `cover.png` + `thumb.png` — cover and gallery thumbnail per assay-blog/**03**
  (`docs/streams/assay-blog/brief-03-cover-thumbnail-lane.md`). The pair already renders a
  light-surface cover under `docs/articles/img/<slug>/` (Output item 6); the bundle's
  cover/thumbnail follow the 03 art spec and sizes.
- `SCRIPT.md` + `explainer.html` — explainer-video source per assay-blog/**04**
  (`docs/streams/assay-blog/brief-04-video-script-lane.md`). Scripts ONLY — the desk never
  renders the mp4 (spec §3 render boundary); Ian renders and supplies the YouTube link. The
  `explainer.html` starts from the gsap adapter's template.html and must satisfy 04's render
  contract (self-contained, one SCENE_DURATIONS literal, the data-done signal, scene count ==
  SCRIPT.md rows, inline slots left as empty stubs) AND pass 04's pre-delivery qa.mjs stills
  smoke test — every scene `doneReason=complete`, zero console errors — before the held PR
  opens. The deck is not done until it renders; ship it un-bundled (the render tool bundles at
  render time). Contract and procedure live in 04 — not restated here.
- `teaser.html` — email-safe teaser fragment per assay-blog/**05**
  (`docs/streams/assay-blog/brief-05-mail-teaser-subscriptions.md`). Sending it is a
  separate human mail-tool step, never automated here.

**How it ships: one HELD PR, never published by this skill.** The bundle lands as its own
**draft PR to `../assay-site`**, held un-published under the green-light lifecycle of
assay-blog/**02** (`docs/streams/assay-blog/brief-02-greenlight-lifecycle.md`, spec §3):
the PR stays held until BOTH (a) Ian's green-light on the PR and (b) the video leg
resolves (a YouTube link in the metadata, or the explicit `video: none` marker). Merge,
regeneration, and publication are the human's — this skill's rules 5, 6 and the render
boundary bind the bundle exactly as they bind the article and post. The end-to-end owned
steps live in the weekly operating checklist:
`docs/streams/assay-blog/weekly-checklist.md`.

When the article lives in `assay-toolkit`, the article + post pair ship in this repo (per
Output item 3) and the blog bundle is a **sibling held PR to `../assay-site`**; each PR
body links the other. Leak rules bind the bundle like any artifact — a withheld token in
the rendered HTML or PNG is still a leak.

## Cadence & interaction with the profile

- Target ~1 pair/week; never draft a burst for same-day posting (a burst reads as a
  launch). If asked for several, stagger the `date:` intents across separate PRs — one
  pair per PR.
- If a drafted pair's material overlaps a live founder-voice artifact on the profile
  (an open poll, a discovery post), note that in the PR body so Ian can retire the old
  one when this goes up.
