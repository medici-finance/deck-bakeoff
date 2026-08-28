# Bake-off reference screenshots — INDEX

Captured 2026-08-27 via headless Chromium (Playwright, `chromium.launch()` from
`/Users/iholsman/jojig/Lending/rwa-bakeoff/skills/video/explainer-video/node_modules/playwright`)
against every `deck/index.html` and `explainer/explainer.html` under
`/Users/iholsman/jojig/Lending/rwa-bakeoff/tracks/<design>/<mode>/<messaging>/`.
Output lives at `/Users/iholsman/jojig/Lending/rwa-bakeoff/shots/<design>/<mode>/<messaging>/`.

All 6 designs × 2 modes × 3 messagings (36 track-mode×messaging directories, 72
artifacts total: 36 decks + 36 explainers) were present and complete at capture
time — no `impeccable-polish` track was still in progress. **Zero failures.**

## Summary

| Design | Mode | Messaging | Deck slides | Deck contact | Explainer scenes | Explainer contact |
|---|---|---|---:|:---:|---:|:---:|
| algorithmic-art | brand | pitch-deck-mastery | 14 | yes | 8 | yes |
| algorithmic-art | brand | presentation-writing | 14 | yes | 8 | yes |
| algorithmic-art | brand | staging | 14 | yes | 9 | yes |
| algorithmic-art | free | pitch-deck-mastery | 14 | yes | 8 | yes |
| algorithmic-art | free | presentation-writing | 14 | yes | 8 | yes |
| algorithmic-art | free | staging | 14 | yes | 9 | yes |
| canvas-design | brand | pitch-deck-mastery | 14 | yes | 8 | yes |
| canvas-design | brand | presentation-writing | 14 | yes | 8 | yes |
| canvas-design | brand | staging | 14 | yes | 9 | yes |
| canvas-design | free | pitch-deck-mastery | 14 | yes | 8 | yes |
| canvas-design | free | presentation-writing | 14 | yes | 8 | yes |
| canvas-design | free | staging | 14 | yes | 9 | yes |
| html-ppt | brand | pitch-deck-mastery | 14 | yes | 8 | yes |
| html-ppt | brand | presentation-writing | 14 | yes | 8 | yes |
| html-ppt | brand | staging | 14 | yes | 9 | yes |
| html-ppt | free | pitch-deck-mastery | 14 | yes | 8 | yes |
| html-ppt | free | presentation-writing | 14 | yes | 8 | yes |
| html-ppt | free | staging | 14 | yes | 9 | yes |
| impeccable-polish | brand | pitch-deck-mastery | 14 | yes | 8 | yes |
| impeccable-polish | brand | presentation-writing | 14 | yes | 8 | yes |
| impeccable-polish | brand | staging | 14 | yes | 9 | yes |
| impeccable-polish | free | pitch-deck-mastery | 14 | yes | 8 | yes |
| impeccable-polish | free | presentation-writing | 14 | yes | 8 | yes |
| impeccable-polish | free | staging | 14 | yes | 9 | yes |
| impeccable | brand | pitch-deck-mastery | 14 | yes | 8 | yes |
| impeccable | brand | presentation-writing | 14 | yes | 8 | yes |
| impeccable | brand | staging | 14 | yes | 9 | yes |
| impeccable | free | pitch-deck-mastery | 14 | yes | 8 | yes |
| impeccable | free | presentation-writing | 14 | yes | 8 | yes |
| impeccable | free | staging | 14 | yes | 9 | yes |
| visual-explainer | brand | pitch-deck-mastery | 14 | yes | 8 | yes |
| visual-explainer | brand | presentation-writing | 14 | yes | 8 | yes |
| visual-explainer | brand | staging | 14 | yes | 9 | yes |
| visual-explainer | free | pitch-deck-mastery | 14 | yes | 8 | yes |
| visual-explainer | free | presentation-writing | 14 | yes | 8 | yes |
| visual-explainer | free | staging | 14 | yes | 9 | yes |

Deck screenshots are 1280×720; explainer scene screenshots are 1920×1080, taken
at the scene's midpoint (`dur/2`). Every directory also has `deck-contact.png`
(4-column, 320px-wide thumbnails, ≤1320px total width) and
`explainer-contact.png` built the same way.

## Missing / failed captures

None. All 36×2 = 72 artifacts captured on the first full run
(`shots/_results.json` records `status: "ok"` for every row).

## Defect found and fixed: phantom duplicate slides (html-ppt-family, free mode)

`html-ppt/free/*` and `impeccable-polish/free/*` (6 directories) initially
produced **28** `slide-NN.png` files instead of 14. Root cause: these two
decks' `free`-mode `runtime.js` eagerly builds a hidden slide-overview grid at
boot via `s.cloneNode(true)` (see `deck/index.html`, search `cloneNode`/
`overview`), so `document.querySelectorAll('.slide').length` returns 28 (14
real `<section class="slide">` + 14 hidden clones inside `.overview .thumb`)
even though only 14 slides are navigable. The `brand`-mode variant of the same
engine does not build this overview eagerly and was unaffected (correctly
reported 14).

Symptom in the captured PNGs: slides 1–14 were all distinct; slides 15–28 were
a handful of repeating/looping frames (verified by MD5 — e.g. slide-15/16/19/
20/25/26/27/28 in `html-ppt/free/pitch-deck-mastery` were byte-identical),
because further `ArrowRight` presses past the real last slide had nowhere new
to go.

**Fix applied:** confirmed the real slide count with the scoped selector
`document.querySelectorAll('.deck > section.slide').length` (=14 in all 6
cases, matching brand mode), deleted `slide-15.png`…`slide-28.png` in the 6
affected directories, and rebuilt their `deck-contact.png` sheets. A
full re-scan (MD5 across every `slide-*.png` and `scene-*.png` in all 36
directories) confirms no duplicate frames remain anywhere.

**For a re-run on late tracks:** when counting slides for `html-ppt` or
`impeccable-polish` in `free` mode, use `.deck > section.slide`, not `.slide`
— the bare `.slide` selector over-counts by 2× on these two tracks' free
variant.

## Exact commands, per track type

All commands were driven from a single Node script using Playwright's bundled
Chromium (no system Chrome needed, though `/Applications/Google Chrome.app`
was also present and would work identically via `chromium.launch({executablePath:...})`
if preferred).

### Deck capture (all 6 designs — one universal method)

Every deck registers a `keydown` handler for `ArrowRight`/`Space` regardless
of design or mode (verified across all 12 design×mode variants), so keyboard
navigation is used instead of guessing each engine's own hash format or
exposed JS API (`window.__deck`), which differ by design **and** by mode
(e.g. `algorithmic-art`/`canvas-design`/`impeccable` expose `window.__deck.go()`
in `free` mode but only a plain `#N` hash in `brand` mode; `html-ppt`/
`impeccable-polish` use `#/N`; `visual-explainer` uses `#slide-N`).

```js
const { chromium } = require('playwright'); // bundled at skills/video/explainer-video/node_modules/playwright
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
await page.goto('file://' + deckIndexHtmlAbsPath, { waitUntil: 'load' });
await page.waitForTimeout(500);
// html-ppt / impeccable-polish FREE mode only: use '.deck > section.slide'
const count = await page.evaluate(() => document.querySelectorAll('.slide').length);
await page.screenshot({ path: outDir + '/slide-01.png' });
for (let i = 2; i <= count; i++) {
  await page.keyboard.press('ArrowRight');
  await page.waitForTimeout(450);
  await page.screenshot({ path: outDir + `/slide-${String(i).padStart(2,'0')}.png` });
}
```

### Explainer capture (all 6 designs — one universal method)

Every explainer supports a `?scene=N` (1-based) query-string deep link
(verified across all 12 design×mode variants) and autoplays forward in real
time from wherever it lands, so the scene's own `data-dur` (seconds, read off
each `.scene` element) is used to wait to the scene's midpoint in real
wall-clock time rather than reverse-engineering each engine's bespoke
freeze/seek hooks (which do exist on some tracks — `window.__player.freeze()`
+ `?at=`/`?still=` on `html-ppt`/`impeccable-polish`, `?p=0.5&paused` on
`canvas-design` free mode, `window.__tick()` on `algorithmic-art` — but differ
enough between `brand` and `free` variants of the *same* design that a single
generic method was more reliable at this scale). This matches the fallback
the task anticipated for CSS-driven animations.

```js
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
await page.goto('file://' + explainerHtmlAbsPath, { waitUntil: 'load' });
const durs = await page.evaluate(() =>
  [...document.querySelectorAll('.scene')].map(s => parseFloat(s.getAttribute('data-dur')) || 5));
for (let i = 1; i <= durs.length; i++) {
  await page.goto(`file://${explainerHtmlAbsPath}?scene=${i}`, { waitUntil: 'load' });
  await page.waitForTimeout(Math.max(300, (durs[i - 1] / 2) * 1000));
  await page.screenshot({ path: outDir + `/scene-${String(i).padStart(2,'0')}.png` });
}
```

### Contact sheets (all directories)

Python 3 + Pillow (PIL), 4 columns, 320px-wide thumbnails, filename label under
each tile:

```
python3 build_contacts.py   # globs shots/<design>/<mode>/<messaging>/{slide,scene}-*.png,
                             # writes deck-contact.png / explainer-contact.png per dir
```

(ImageMagick `montage` was not installed on this host; PIL was used instead —
both are equally valid per the task's fallback order.)

## Housekeeping

The 92 loose PNG/JSON files a previous reviewer/agent left directly under
`shots/` (flat `design__mode__deckNN.png` / `design__mode__scN.png` naming,
covering only 4 designs × 2 modes with no messaging dimension, plus
`htmlppt_free_probe.png` and `_probe.json`) were moved to
`shots/_reviewer-frames/` so the tree now holds only the structured
`<design>/<mode>/<messaging>/` output plus this INDEX and the capture-run
`_results.json`.
