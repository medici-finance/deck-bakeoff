# Design-contender task (stage 2) — read in full before starting

You are ONE design contender × ONE brand mode. Work ONLY under
/Users/iholsman/jojig/Lending/rwa-bakeoff/ with ABSOLUTE literal paths in every
command. Never `cd` into, reference, or use a shell variable whose value is a
prefix of /Users/iholsman/jojig/Lending/assay-toolkit (a write guard blocks the
call). A single `cd /abs/dir && …` chain is allowed. No git, no PRs, no network
fetches other than Google Fonts links inside `free`-mode HTML. Nothing leaves the
directory.

## Inputs
- /Users/iholsman/jojig/Lending/rwa-bakeoff/BRIEF.md — the brief (audience, three goals, media specs).
- Three messaging contracts — you render ALL THREE:
  - /Users/iholsman/jojig/Lending/rwa-bakeoff/messaging/staging/staging.yaml (+ messaging.md)
  - /Users/iholsman/jojig/Lending/rwa-bakeoff/messaging/presentation-writing/staging.yaml (+ messaging.md, outline.md)
  - /Users/iholsman/jojig/Lending/rwa-bakeoff/messaging/pitch-deck-mastery/staging.yaml (+ messaging.md, pitch.md)
  Consume each verbatim: never reorder slots/scenes, never rewrite a headline
  claim (rephrasing for line-breaks is fine), never add facts. A slot you cannot
  render → log in NOTES.md, do not drop silently.
- Source corpus for fact-checking only: /Users/iholsman/jojig/Lending/rwa-bakeoff/source/medici/.
- Brand (mode `brand` only): /Users/iholsman/jojig/Lending/rwa-bakeoff/source/brand/house-brand-guide.md
  (§2 colour, §3 type, §9 motion, §10 surfaces), machine contract
  /Users/iholsman/jojig/Lending/rwa-bakeoff/skills/deck-author/brands/medici/brand.toml,
  fonts in /Users/iholsman/jojig/Lending/rwa-bakeoff/skills/deck-author/brands/medici/fonts/
  (copy the woff2 files beside your HTML, or base64-embed them; never a CDN),
  skeleton with the inline mark symbols
  /Users/iholsman/jojig/Lending/rwa-bakeoff/skills/deck-author/brands/medici/deck-skeleton-external.html.
  Linter: `python3 /Users/iholsman/jojig/Lending/rwa-bakeoff/skills/deck-author/tools/check_deck.py <index.html>`
  (read its --help; run it on every brand-mode deck, record the result).
- Mode `free`: NO brand limits. Your tool's own aesthetic judgement on palette,
  type (Google Fonts allowed), layout, motion. Fixed: the facts, the footer
  string `Medici — Proprietary & Confidential` on every slide, the name Medici.
  Go as far as the tool lets you — this mode exists to show the tool's ceiling.

## Outputs (6 artifacts + notes)
For each messaging m ∈ {staging, presentation-writing, pitch-deck-mastery}:
- `tracks/<design>/<mode>/<m>/deck/index.html` — self-contained, 1280×720
  fixed stage, one `<section class="slide">` per slot, keyboard ←/→ + click
  navigation, slide counter, `<meta name="deck-footer" content="Medici — Proprietary &amp; Confidential">`
  in <head>, footer text visible on every slide, `@media print` paginating one
  slide per page (page size 1280px 720px). No remote assets except Google Fonts
  in `free` mode.
- `tracks/<design>/<mode>/<m>/explainer/explainer.html` + `SCRIPT.md` —
  self-contained animated explainer for screen recording: 1920×1080 stage,
  scenes from the contract's video lane, auto-plays on load with per-scene
  durations equal to the contract's vo_seconds, `?scene=N` and Space/→ to
  override, a tiny progress bar, and `window.__player = {scene, t, total, seek(n)}`
  exposed for tooling. Motion MUST carry meaning (the P/N split, the payoff at
  maturity, the refused liquidation) per the scene's motion_role/energy/peak;
  quiet scenes stay quiet. No audio, no video, no TTS. SCRIPT.md = per-scene
  table: scene id, start time, duration, on-screen text, VO narration verbatim
  from the contract, what moves.
- `tracks/<design>/NOTES.md` (one per design contender, shared by both modes —
  append a `## <mode>` section): time-to-artifact per artifact, the tool's
  process as actually run (which of its steps/commands/references you used),
  friction, overrides, what the tool refused or could not express, brand
  fights (brand mode), what the tool did with freedom (free mode), linter
  results, any slot you could not render and why.

## Quality floor (both modes)
- Every figure on screen traces to the contract; no invented numbers.
- Text legible at 1280×720 (deck ≥ 18px body) and 1920×1080 (explainer ≥ 28px).
- Colour contrast ≥ 4.5:1 for body text.
- Open each HTML in a headless check if available (`node -e` with any local
  puppeteer/playwright — none is installed; otherwise validate structure with
  python3: parse HTML, count slides == slot count, footer present on each,
  no `http(s)://` refs except fonts.googleapis/gstatic in free mode).
- Finish ALL six artifacts. If time is short, reduce polish, never count.

Report back ≤15 lines: artifacts written (paths), linter results, top 3
friction items, one sentence on what the tool did best.
