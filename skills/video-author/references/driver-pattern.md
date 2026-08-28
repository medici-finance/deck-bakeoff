# The hand-rolled scene driver — the sanctioned GSAP fallback

When the GSAP adapter cannot be bundled (no `node_modules` in the snapshot,
npm out of scope) and no vendored copy is reachable, implement the renderer
contract by hand. This pattern is ~90–110 lines, dependency-free, and was
proven on two full runs (`<loom-bakeoff sandbox>/tracks/video/staged/`, `<loom-bakeoff sandbox>/tracks/video/inhouse/`);
the reference implementation below is the control run's driver, verbatim in
shape. It is a fallback for the *runtime*, never for the contract — every
requirement in SKILL.md §2 still binds.

## The timing model the driver MUST reproduce

This is the house adapter's model; approximating it is not implementing it.

1. **Durations: injected else fallback, never ambiguous.**
   `window.SCENE_DURATIONS` is declared **empty** exactly once; the pipeline
   rewrites that first regex match with measured seconds. Non-empty →
   use it. Empty/absent → use the authored `FALLBACK` estimates **with a
   console warning** naming the fact. A length mismatch against the scene
   count warns too.
2. **Natural-pace authoring, per beat.** Every animated beat carries
   `data-at="<seconds>"` (optionally `data-dur`), authored to the pace of
   the sentence, not to a stopwatch of the slot.
3. **Reconciliation, per scene.** Compute the authored span (max
   `data-at + data-dur`). Against the measured slot:
   - span ≤ slot → play at natural pace;
   - span > slot → compress by a **uniform time-scale** and emit a console
     warning **naming the scene** (the render check greps for it).
4. **Slack becomes distributed holds, not a terminal freeze.** When the
   slot is longer than the authored span, stretch the *rests between beats*
   proportionally (or author the cue schedule so the final beat lands at
   ≥60 % of the estimated slot). The GSAP adapter does this with flexed
   holds; a driver that plays everything in the first three seconds and
   freezes fails the render check's front-load probe (visible content at
   85 % of the slot must be ≥ at 15 %). Hold ≥0.4 s of stillness after
   every beat.
5. **The done discipline.** On the last scene's expiry plus a short tail:
   `document.body.dataset.done = "1"`, `dataset.doneReason = "complete"`.
   No scenes, or a thrown boot → `doneReason = "error"` (+`dataset.error`)
   within seconds. A watchdog at `total + tail + ~5 s` raises
   `doneReason = "watchdog"`. A failed render must never look like a
   successful one.
6. **Visibility, not display.** Hide inactive scenes with
   `opacity`/`visibility`, never `display:none` — inline SVG needs live
   layout for stroke-length draw-ons. Reset a scene's beats before playing
   it (one `requestAnimationFrame` later, so the reset lands first).
7. **The seam shim still ships.** Expose `window.__explainer`
   (`durations`, `total`, `scenes`, `failure`) and bridge
   `window.__player` + `__playerReady` + `__renderReady` per
   `../../staging/references/seam-gate.md`, so the seam gate and the render
   check run against the delivered file. A `setTimeout`-driven driver needs
   a seekable notion of the master clock for this — either keep a
   deterministic schedule you can re-derive positions from, or drive beats
   off one `requestAnimationFrame` clock you can pause and seek.

## Reference implementation

From `<loom-bakeoff sandbox>/tracks/video/inhouse/build/src/driver.js` (annotated there; ~109
lines with comments). The skeleton:

```js
(function () {
  var CROSSFADE = 0.2, TAIL = 0.5;
  var scenes = [].slice.call(document.querySelectorAll('.scene'));
  var D = (window.SCENE_DURATIONS && window.SCENE_DURATIONS.length)
    ? window.SCENE_DURATIONS : null;
  if (!D) { console.warn('[explainer] no injected SCENE_DURATIONS — using authored ESTIMATES'); D = FALLBACK; }
  if (D.length !== scenes.length)
    console.warn('[explainer] ' + D.length + ' durations vs ' + scenes.length + ' scenes');

  var total = 0; for (var i = 0; i < D.length; i++) total += (D[i] || 4);
  window.__explainer = { durations: D, total: total, scenes: scenes.length, failure: null };

  var timers = [];
  function done(reason, msg) {
    if (document.body.dataset.done === '1') return;
    document.body.dataset.doneReason = reason;
    if (msg) document.body.dataset.error = msg;
    document.body.dataset.done = '1';
  }

  function playScene(sc, seconds) {
    var beats = [].slice.call(sc.querySelectorAll('[data-at]'));
    var span = 0;
    beats.forEach(function (b) {
      span = Math.max(span, parseFloat(b.getAttribute('data-at')) +
                            (parseFloat(b.getAttribute('data-dur')) || 0.7));
    });
    var avail = Math.max(0.4, seconds - CROSSFADE);
    var scale = span > avail ? (avail / span) : 1;   // compress…
    if (scale < 1) console.warn('[explainer] scene "' + sc.dataset.scene +
      '" authored ' + span.toFixed(1) + 's into ' + avail.toFixed(1) + 's — compressed');
    // …or, when avail > span, stretch the inter-beat rests instead of
    // freezing at the end: scale = avail / span capped at ~1.6 is a
    // serviceable flex; beyond that, hold the excess at the LAST REST,
    // not after the final beat only.
    beats.forEach(function (b) {
      var at = parseFloat(b.getAttribute('data-at')) * scale * 1000;
      timers.push(setTimeout(function () { b.classList.add('in'); }, at));
    });
  }

  function run() {
    var i = 0;
    (function next() {
      if (i >= scenes.length) { setTimeout(function () { done('complete'); }, TAIL * 1000); return; }
      var sc = scenes[i], secs = D[i] || 4;
      scenes.forEach(function (s, j) { s.classList.toggle('on', j === i); });
      [].slice.call(sc.querySelectorAll('[data-at]')).forEach(function (b) { b.classList.remove('in'); });
      requestAnimationFrame(function () { playScene(sc, secs); });
      i++;
      timers.push(setTimeout(next, secs * 1000));
    })();
  }

  window.addEventListener('load', function () {
    if (!scenes.length) { done('error', 'no scenes'); return; }
    setTimeout(function () { done('watchdog'); }, (total + TAIL + 5) * 1000);
    try { setTimeout(run, 250); }
    catch (e) { window.__explainer.failure = String(e); done('error', String(e)); }
  });
})();
```

CSS side: beats start hidden (`opacity:0`, small rise ≤ the motion spec's
support/hero travel) and `.in` transitions them per the locked spec's
curves and durations. The active scene carries `.on`
(opacity/visibility, never display).

## Practical notes from the runs

- Author every scene's span at ~55–65 % of its estimated slot; the measured
  take then has room to run long without compression — but pair this with
  flexed rests (or late-landing cues), or the front-load probe fails.
- Keep the driver and the authored scene bodies in separate source files
  and inline at build time; a hand-editable file and a file with ~80 KB of
  base64 in it cannot be the same file. Make the build **fail** on: more
  than one `SCENE_DURATIONS` assignment, any external `src`/`href`, a
  scene/duration count mismatch (`<loom-bakeoff sandbox>/tracks/video/inhouse/build/build.mjs`,
  `<loom-bakeoff sandbox>/tracks/video/hybrid/build/build.mjs` are both worked examples).
- The two expected console warnings during checking — the fallback-path
  notice, and per-scene compression under deliberately short injected
  durations — are the runtime doing its job; both name their scene.
