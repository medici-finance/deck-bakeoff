# NOTES — presentation-writing contender

**Skill under test**: `powerpoint-keynote-presentation` (marcusnelson), at
`skills/messaging/presentation-writing/powerpoint-keynote-presentation/SKILL.md` + `references/scaffolds.md`.
**Run date**: 2026-08-27.

---

## 1. Time to artifact

| Marker | UTC |
|---|---|
| Start (first read of `BRIEF.md`) | 23:24:53 |
| Finish (last artifact written) | 23:34:40 |
| **Elapsed** | **~10 minutes**, single pass, no rework cycle |

Rough split: ~4 min reading (brief, skill + scaffolds, five source docs, brand §0/§8, the staging
schema and motion-role vocabulary), ~5 min composing the three artifacts, ~1 min reconciling word
counts and validating the YAML parses.

No human was in the loop, so none of the skill's four confirmation gates cost wall-clock time. A
faithful attended run would be longer and would stop four times (see §3).

---

## 2. Friction

1. **The skill gates on a human four times and has no "recorded assumption" escape.** Phase 2 says
   "Do not proceed until the audience is confirmed." Phase 3 asks the scaffold to be verified. Phase 5
   asks the density question. Phase 6 says its closing prompt "is not optional." In an unattended
   bake-off every one of those becomes an assumption, and the skill offers no mechanism for logging
   one — unlike the staging skill next door, which explicitly says "anything else you want to know is
   a recorded assumption, not a question." I answered all four from the corpus and logged them in §3.

2. **Phases 7 and 8 pull toward the wrong deliverable.** Phase 8 wants to build a .pptx with a
   defaulted Inter + IBM Plex "Bauhaus" style, complete with hex codes, tracking values and accent-bar
   geometry. The bake-off gives that job to six design contenders and forbids messaging from touching
   it. I ran Phase 8's *brand-intake question* (the useful half) and discarded its build half. The
   skill has no mode that stops at the outline.

3. **No provenance field anywhere in the output format.** The skill's slide format is thesis + up to
   three bullets + transition. The brief's hardest constraint is that every number traces to a source
   file. I extended the bullet format with an inline `[file · slide]` tag on every figure. This is an
   addition to the skill's format, not something it provides.

4. **The skill's only data discipline is chart orientation.** Phase 1 spends 25 lines on transposing
   row-oriented spreadsheets and zero on whether a number is true or where it came from. The corpus
   here has no spreadsheets and two internal numeric conflicts (§3, Q7). The check that mattered was
   not the one the skill runs.

5. **A tension between the skill's voice rules and the house brand.** The skill wants "one moment of
   genuine personality per 5-7 slides" and dry humour. `house-brand-guide.md` §8.1 says direct, not
   clever, and §8.4 bans exclamation marks. Resolved toward the brand: the personality in this deck is
   candour, not wit — slide 10 disqualifies the product for near-zero-vol collateral, slide 12 lists
   what does not exist. Both are "a specific human wrote this for a specific room" in the skill's
   sense without breaking §8.

6. **Headline length.** The skill asks for a declarative thesis sentence; the transport contract caps
   headline claims at 12 words. The two are not the same length. `outline.md` carries the full thesis;
   `staging.yaml` carries the trimmed claim. They are the same claim — design consumes the staging
   form verbatim, and should not go looking for the longer one.

7. **Minor**: the skill package has a `README.md` but no LICENSE file of its own; several sibling
   design skills in this repo do ship one (`algorithmic-art`, `visual-explainer`, `html-ppt-skill`,
   `pitch-deck-mastery`). See §5.

---

## 3. Questions the skill would have asked a human — answered from the corpus

**Q1 (Phase 2, audience confirmation).** *"This reads like a pitch to [audience] where the goal is
[decision]. The room cares most about [priority]. Am I reading this right?"*
**Answer:** RWA issuers, tokenization platforms, asset managers and their risk/product leads, plus
chain-ecosystem BD introducers. Technical-adjacent, finance-literate, not DeFi-native. The goal is
education; the ask is a conversation, not funding.
**Provenance:** `BRIEF.md`, "Audience + the three educational goals" and "Genre" — stated verbatim, so
this was not actually an open question.

**Q2 (Phase 2, priority).** *"What does the room care most about?"*
**Answer (inferred):** not losing an asset they cannot replace; income on what they already hold; what
the risk committee will ask.
**Provenance:** inferred from `asset-manager-pitch-deck.md` Slide 7 (a slide built entirely around
"the risk profile your risk committee will ask about") and `rwa-redstone-2026.md` Part 2, which
describes allocator behaviour as "institutional portfolio management." Marked as inference.

**Q3 (Phase 3, scaffold).** *"This wants The Keynote scaffold — sound right?"*
**Answer:** yes, with Workshop components 1-3 for the mechanism and The Close's objection beat.
**Provenance:** `BRIEF.md` "the ask is a conversation, not funding" rules out The Pitch's slide 9;
brief goal 3 ("one diagram they could redraw") is a Workshop job, not a Keynote job. Reasoning is
written out in `outline.md` §"Phase 3".

**Q4 (Phase 5, density).** *"Consistent, Flexible, or Minimal?"*
**Answer:** Flexible — the skill's own stated default when unanswered, and it suits a deck whose
slides 5 and 14 are single statements while 7, 9 and 12 need structure.
**Provenance:** SKILL.md Phase 5, "proceed with Flexible and note the choice in the outline header."
Noted there.

**Q5 (Phase 6, next step).** *"Do you take this into Keynote, do I build a basic .pptx, or do I hand
off to the pptx skill?"*
**Answer:** none of the three. `staging.yaml` goes to six design contenders who render both a deck and
an explainer in two brand modes.
**Provenance:** `BRIEF.md`, "Messaging layer" and "Layout".

**Q6 (Phase 8, brand intake).** *"Do you have brand guidelines, a colour palette, or font
preferences?"*
**Answer:** yes, and they are not messaging's to apply. Two modes exist (`brand` pinned to
`house-brand-guide.md`, and `free`), and design owns both. What messaging took from the brand guide is
tone and terminology only: §8.2's canon (Protected/Amplified, split/recombine, drift/theta, "can't be
liquidated" unhedged), §8.3's canonical sentence reused verbatim, §0.8's rule that a surface stating
the guarantee stays within one slide of the cost.
**Provenance:** `BRIEF.md` "Two brand modes"; `house-brand-guide.md` §0.5, §0.8, §8.1-§8.4.

**Q7 (Phase 1, ambiguity — "stop and ask").** Three numeric conflicts inside the corpus:

- **DAML template count.** `canton-pitch-deck.md` Slide 9 says **54 templates across 9 modules,
  ~5,700 LOC**; `asset-manager-pitch-deck.md` Slide 12 says **36 templates, ~5,100 LOC** — and the
  asset-manager deck carries the *later* revision date (reframed 2026-07-18 vs 2026-07-04).
  **Resolved:** used 54/9 modules, because `BRIEF.md` names `canton-pitch-deck.md` as the first
  source of truth in priority order. **This is the one number in the deck a human should confirm.**
- **Regulatory analysis length.** ~2,900 lines (`canton-pitch-deck.md` Slide 9) vs 2,600 lines
  (`asset-manager-pitch-deck.md` Slides 7, 11). Same resolution rule; used ~2,900.
- **Agent fleet.** Not a conflict: 12 agents total, 6 core live and 6 in progress
  (`canton-pitch-deck.md` Slide 8); `asset-manager-pitch-deck.md` Slide 9 lists the same six live
  ones under a "12-agent fleet" heading.

**Q8 (Phase 1, strategic ambiguity).** Which RWA underlying is the flagship? `canton-pitch-deck.md`
Slides 6-7 lead with tokenized fund shares (USTB, BENJI, WisdomTree); `rwa-redstone-2026.md` Part 2
argues gold first and calls near-zero-vol treasuries a poor fit — with data (T-bill deposits −92%,
gold 7x).
**Resolved:** the deck states both, and states the boundary. Slide 10 says gold fits and near-zero-vol
MMF collateral largely does not; the income framing on slide 6 is what a fund treasury gets. The
research doc is the later and more evidence-backed position, and disqualifying our own product for the
wrong collateral is the most credible slide in the deck. **A human may want to overrule this** — it is
the only place where I chose a research document's conclusion over a pitch deck's framing.

**Q9 (Voice, Phase "Voice").** *"This is written in your voice. If someone else is presenting, tell me
who's in front of the room."*
**Answer:** Medici's own presenters — Ian (technical lead) and Co-founder (institutional
partnerships), per `canton-pitch-deck.md` Slide 10. Voice therefore follows the house tone rules
(`house-brand-guide.md` §8.1) rather than a personal voice profile: mathematical not mystical, direct
not clever, confident not defensive, and human-plain — §8.1 principle 6 explicitly warns against the
machine-default register, which is the same failure the skill's "Human Tone" section attacks.

**Q10 (not asked by the skill, asked by the material).** Both source decks carry an *ask* this brief
does not have — Canton Foundation funding, and a $5-50M strategic investment plus pilot. Both were
discarded. The ask here is slide 13: name one asset, size the split, try to break the payoff.

---

## 4. What the skill could not express

Listed because these are the gaps a design contender or a future revision should know about, not as
complaints — the skill is honest about being a deck-narrative skill and nothing else.

1. **Anything about video.** No scene concept, no duration, no VO. The scene format in `outline.md`
   Part 2 is the skill's slide format (thesis / support / transition) with two fields bolted on. Its
   persuasion rules did carry over cleanly — front-load the hook, one thesis per unit, no orphan
   scenes, end with a charge — which is the finding worth recording: the *structure* transferred to
   film, the *format* did not.
2. **Kinetics.** `motion_role`, `energy`, `peak`, `motion_turn`, `figures` and the whole motion budget
   in `staging.yaml` come from `skills/messaging/staging/references/motion-roles.md`, which the brief
   named as the closed vocabulary for the transport contract. The *allocation* is this skill's logic
   (the rupture sits on the answer to the crack; the divest scene is the honest-cost beat), but the
   vocabulary is borrowed. The skill has no notion that motion is a scarce resource.
3. **Diagrams.** The skill's only visual concept is "no bullets — when the visual carries the slide."
   Brief goal 3 requires one diagram the audience could redraw, so the diagram description lives in
   `messaging.md` §4 as prose, deliberately naming no palette, no styling and no chart type.
4. **Evidence provenance.** Covered in §2.3 — added, not provided.
5. **Two artifacts sharing one arc.** The skill builds one deck. The deck and the film here share a
   spine by construction on my part (film scenes 1-8 compress deck slots 2-14, and both put the bold
   moment on the payoff), not because the skill has a concept of a companion artifact.
6. **A count-bounded headline.** Covered in §2.6.
7. **Objection ordering.** The skill's Close scaffold has one objection beat ("name the biggest
   concern"); it has no rule for ordering five of them. I ran them in descending likelihood, which is
   the staging reference's rule, not this skill's.

One further note for design: `staging.yaml` scene 6's VO says the words "draw the liquidation line"
and "nowhere on this axis." That is narration text, and narration cannot avoid implying a picture —
but it is the closest this contract comes to naming a visual, and design is free to render the idea
any way it likes as long as the threshold is introduced and then cannot be placed.

---

## 5. Repo licensing

**`/Users/iholsman/jojig/Lending/rwa-bakeoff/` has no LICENSE file.** Checked directly; the path does
not exist. Nothing in the bake-off root states terms for the corpus, the brief, or the artifacts
produced under it.

Vendored skills carry their own, unevenly: `skills/design/algorithmic-art/LICENSE.txt`,
`skills/design/canvas-design/LICENSE.txt`, `skills/design/visual-explainer/LICENSE`,
`skills/design/html-ppt-skill/LICENSE`, `skills/messaging/pitch-deck-mastery/LICENSE`, and
`skills/messaging/staging/tools/LICENSE-hyperframes-Apache-2.0.txt` all exist. The skill under test
here — `skills/messaging/presentation-writing/` — ships a `README.md` and the `.skill` bundle but **no
LICENSE**. Worth resolving before any of this leaves the directory, which per `BRIEF.md` it does not.
