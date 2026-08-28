/*!
 * gsap-explainer — a GSAP renderer adapter for tools/explainer-video.
 *
 * Drop-in replacement for the hand-rolled animation JS inside an
 * `explainer.html`. It reads `window.SCENE_DURATIONS` (injected by the
 * pipeline before recording), builds ONE GSAP timeline per scene scaled to the
 * measured narration, advances scenes automatically (each boundary is a named
 * handoff — `data-exit="cut|fade|push|zoom"` on the outgoing scene, default
 * fade), and sets
 * `document.body.dataset.done = "1"` after the final scene so
 * `pipeline/record.mjs` stops recording. The engine stays untouched.
 *
 * Classic script (no ES modules) so it survives `file://` loading and inlining.
 * Requires `gsap` on the page first; `DrawSVGPlugin` is used when present and
 * falls back to a stroke-dashoffset implementation when it is not.
 *
 * Global: window.GsapExplainer
 */
(function (global) {
  'use strict';

  var gsap = global.gsap;
  if (!gsap) {
    throw new Error('gsap-explainer: gsap must be loaded before gsap-explainer.js');
  }

  // GSAP's lag smoothing freezes animation time during a jank spike, which
  // makes wall-clock elapsed time drift ahead of the timeline — fatal when the
  // frames must line up with a pre-rendered narration track. Off = time
  // advances with the real clock, which is what the recorder captures.
  gsap.ticker.lagSmoothing(0);

  var hasDrawSVG = false;
  if (global.DrawSVGPlugin) {
    gsap.registerPlugin(global.DrawSVGPlugin);
    hasDrawSVG = true;
  }

  // --- brand-motion defaults -------------------------------------------------
  // Fintech-restrained: 200ms ease-in-out enters/exits, functional draws, no
  // spring / bounce / overshoot anywhere.
  var DEFAULTS = {
    crossfade: 0.2,        // scene-to-scene fade (s) — the default handoff
    pushDuration: 0.3,     // data-exit="push" handoff (s)
    pushShift: 24,         // px travel of a push handoff — a shift, never a fling
    zoomDuration: 0.35,    // data-exit="zoom" handoff (s)
    zoomScale: 0.02,       // scale travel of a zoom handoff (0.98 in / 1.02 out)
    tail: 0.5,             // hold on the final frame before the done signal (s)
    enter: 0.2,            // enter/exit duration (s)
    enterEase: 'power2.inOut',
    enterShift: 8,         // px rise on enter — a nudge, never a slide
    stagger: 0.08,
    drawEase: 'power1.inOut',
    drawEach: 0.6,         // natural per-element draw duration before flexing (s)
    drawOverlap: 0.15,     // how much consecutive draws overlap (s)
    minFlex: 0.35,         // floor for a flexed segment (s)
    watchdogPad: 5,        // force the done signal this long after the expected end (s)
  };

  // Motion vocabulary guard: these ease families are off-brand. Warn loudly
  // rather than silently shipping a bouncy frame into a product video.
  var OFF_BRAND_EASE = /(^|\.)(back|elastic|bounce)/i;

  function checkEase(ease, where) {
    if (typeof ease === 'string' && OFF_BRAND_EASE.test(ease)) {
      console.warn('gsap-explainer: off-brand ease "' + ease + '" in ' + where +
        ' — motion is minimal/functional; no spring, bounce or overshoot.');
    }
    return ease;
  }

  // --- small helpers ---------------------------------------------------------
  function toArray(scope, targets) {
    if (!targets) return [];
    if (typeof targets === 'string') {
      return Array.prototype.slice.call(scope.querySelectorAll(targets));
    }
    if (targets.nodeType) return [targets];
    return Array.prototype.slice.call(targets);
  }

  var GEOMETRY = /^(path|line|polyline|polygon|circle|ellipse|rect)$/i;

  /** True when the author gave the element its own dash pattern. Stroke draw-on
   *  — DrawSVGPlugin and the dashoffset fallback alike — OWNS stroke-dasharray,
   *  so drawing a dashed element silently renders it solid. Detected on
   *  pristine geometry only (see the cache in isStrokeDrawable): once we have
   *  seeded a draw, the computed dasharray is ours, not the author's. */
  function hasAuthoredDash(el) {
    var d = global.getComputedStyle(el).strokeDasharray;
    if (!d || d === 'none') return false;
    return (d.match(/[\d.]+/g) || []).some(function (n) { return parseFloat(n) > 0; });
  }

  /** Decide once, on pristine geometry, how an element is animated on:
   *  'stroke' = progressive draw, 'reveal' = fade + rise. Cached on the node
   *  because the stroke path rewrites the very properties this reads. */
  function drawMode(el) {
    if (el.__drawMode) return el.__drawMode;
    var mode = 'reveal';
    var explicit = el.dataset && el.dataset.draw;
    if (explicit !== 'reveal' && GEOMETRY.test(el.tagName)) {
      var stroke = global.getComputedStyle(el).stroke;
      if (stroke && stroke !== 'none') {
        // `data-draw="stroke"` is the opt-in for authors who want the draw-on
        // even though it will consume their dash pattern.
        mode = (explicit === 'stroke' || !hasAuthoredDash(el)) ? 'stroke' : 'reveal';
      }
    }
    el.__drawMode = mode;
    return mode;
  }

  function isStrokeDrawable(el) {
    return drawMode(el) === 'stroke';
  }

  function totalLength(el) {
    if (typeof el.getTotalLength === 'function') {
      try {
        var len = el.getTotalLength();
        if (len > 0) return len;
      } catch (e) { /* fall through */ }
    }
    // Fallback: bounding-box perimeter is close enough to seed a dash pattern.
    try {
      var b = el.getBBox();
      return 2 * (b.width + b.height) || 1;
    } catch (e2) {
      return 1;
    }
  }

  /** Reading order = document order, unless the author overrides with
   *  `data-draw-order="N"` (stable, and only on the elements that need it). */
  function readingOrder(els) {
    return els
      .map(function (el, i) {
        var o = el.dataset && el.dataset.drawOrder;
        return { el: el, i: i, order: o == null || o === '' ? null : parseFloat(o) };
      })
      .sort(function (a, b) {
        var ao = a.order == null ? a.i : a.order;
        var bo = b.order == null ? b.i : b.order;
        if (ao !== bo) return ao - bo;
        return a.i - b.i;
      })
      .map(function (r) { return r.el; });
  }

  /** Seed every drawable element's dash pattern up front, while the whole
   *  document still has layout, so nothing flashes fully-drawn for one frame
   *  when its scene becomes visible. */
  function prepare(root) {
    toArray(root, '[data-draw]').forEach(function (el) {
      var kids = GEOMETRY.test(el.tagName) ? [el] : toArray(el, 'path,line,polyline,polygon,circle,ellipse,rect');
      kids.forEach(function (k) {
        if (!isStrokeDrawable(k)) return;
        if (hasDrawSVG) {
          gsap.set(k, { drawSVG: '0%' });
        } else {
          var len = totalLength(k);
          k.__drawLength = len;
          gsap.set(k, { strokeDasharray: len + ' ' + len, strokeDashoffset: len });
        }
      });
    });
  }

  // --- flexible segments -----------------------------------------------------
  // A "flex" child consumes whatever slack a scene has left after the fixed
  // motion is accounted for, so a draw-on stretches to the narration instead of
  // finishing early and leaving a dead pause.

  function span(child) {
    return child.endTime() - child.startTime();
  }

  function setSpan(child, seconds) {
    seconds = Math.max(seconds, 0.01);
    if (typeof child.timeScale === 'function' && child.getChildren) {
      // Nested timeline: its unscaled duration is fixed, so scale it in place.
      var natural = child.duration() || 0.01;
      child.timeScale(natural / seconds);
    } else {
      child.duration(seconds);
    }
  }

  function applyFlex(tl, flexes, available) {
    if (!flexes.length) return;
    var fixed = tl.duration();
    flexes.forEach(function (f) { fixed -= span(f.child); });
    var slack = available - fixed;
    var totalWeight = flexes.reduce(function (s, f) { return s + f.weight; }, 0) || 1;

    flexes
      .slice()
      .sort(function (a, b) { return a.child.startTime() - b.child.startTime(); })
      .forEach(function (f) {
        var share = slack > 0 ? (slack * f.weight) / totalWeight : 0;
        var target = Math.max(f.min, share);
        var before = span(f.child);
        setSpan(f.child, target);
        var delta = span(f.child) - before;
        if (Math.abs(delta) > 1e-6) {
          // Push every sibling that starts after this one, so the sequence
          // stays in order instead of overlapping.
          tl.shiftChildren(delta, true, f.child.startTime() + 1e-4);
        }
      });
  }

  // --- the per-scene authoring context --------------------------------------
  function makeContext(el, tl, available, cfg, flexes) {
    // GSAP's `timeline.to()` / `.fromTo()` return the TIMELINE, for chaining —
    // NOT the tween they just created. Returning that from an authoring helper
    // meant `ctx.flex(ctx.hold(1))` registered the whole scene as flexible and
    // time-scaled every tween in it. Build the tween standalone, then place it,
    // so every helper hands back the thing it actually made.
    function place(tween, at) {
      tl.add(tween, at == null ? '>' : at);
      return tween;
    }

    function registerFlex(child, opts) {
      flexes.push({
        child: child,
        weight: opts && opts.weight != null ? opts.weight : 1,
        min: opts && opts.min != null ? opts.min : cfg.minFlex,
      });
      return child;
    }

    var ctx = {
      /** the scene element */
      el: el,
      /** seconds of content time this scene has (measured duration minus the
       *  incoming handoff — crossfade by default) */
      duration: available,
      /** scoped selectors */
      $: function (sel) { return el.querySelector(sel); },
      $$: function (sel) { return toArray(el, sel); },

      /** brand enter: fade + an 8px rise, 200ms ease-in-out, staggered */
      enter: function (targets, opts) {
        opts = opts || {};
        var els = toArray(el, targets == null ? '[data-enter]' : targets);
        if (!els.length) return place(gsap.to({}, { duration: 0 }), opts.at);
        return place(gsap.fromTo(els,
          { opacity: 0, y: opts.shift == null ? cfg.enterShift : opts.shift },
          {
            opacity: 1, y: 0,
            duration: opts.duration == null ? cfg.enter : opts.duration,
            ease: checkEase(opts.ease || cfg.enterEase, 'ctx.enter'),
            stagger: opts.stagger == null ? cfg.stagger : opts.stagger,
          }), opts.at);
      },

      /** brand exit: the mirror of enter */
      exit: function (targets, opts) {
        opts = opts || {};
        var els = toArray(el, targets == null ? '[data-enter]' : targets);
        if (!els.length) return place(gsap.to({}, { duration: 0 }), opts.at);
        return place(gsap.to(els, {
          opacity: 0,
          y: opts.shift == null ? -cfg.enterShift : opts.shift,
          duration: opts.duration == null ? cfg.enter : opts.duration,
          ease: checkEase(opts.ease || cfg.enterEase, 'ctx.exit'),
          stagger: opts.stagger == null ? cfg.stagger : opts.stagger,
        }), opts.at);
      },

      /**
       * SVG draw-on. Progressively draws strokes and reveals non-stroke nodes
       * (labels, filled shapes) in reading order.
       *
       * @param targets selector / element / list — defaults to `[data-draw]`
       *                inside the scene. Container elements are expanded to
       *                their drawable descendants.
       * @param opts {duration:'fill'|seconds, weight, min, stagger, each,
       *              overlap, ease, from}
       */
      draw: function (targets, opts) {
        opts = opts || {};
        var picked = toArray(el, targets == null ? '[data-draw]' : targets);
        var items = [];
        picked.forEach(function (node) {
          if (GEOMETRY.test(node.tagName) || (node.dataset && node.dataset.draw === 'reveal')) {
            items.push(node);
          } else {
            var kids = toArray(node, '[data-draw],path,line,polyline,polygon,circle,ellipse,rect,text');
            if (kids.length) { items = items.concat(kids); } else { items.push(node); }
          }
        });
        items = readingOrder(items);
        if (!items.length) {
          console.warn('gsap-explainer: ctx.draw matched nothing in scene "' + (el.id || el.dataset.scene) + '"');
          return tl;
        }

        var each = opts.each == null ? cfg.drawEach : opts.each;
        var overlap = opts.overlap == null ? cfg.drawOverlap : opts.overlap;
        var step = Math.max(each - overlap, 0.05);
        var ease = checkEase(opts.ease || cfg.drawEase, 'ctx.draw');
        var dtl = gsap.timeline();

        items.forEach(function (node, i) {
          var at = i * step;
          if (isStrokeDrawable(node)) {
            if (hasDrawSVG) {
              dtl.fromTo(node, { drawSVG: '0%' }, { drawSVG: '100%', duration: each, ease: ease }, at);
            } else {
              var len = node.__drawLength || totalLength(node);
              node.__drawLength = len;
              dtl.fromTo(node,
                { strokeDasharray: len + ' ' + len, strokeDashoffset: len },
                { strokeDashoffset: 0, duration: each, ease: ease }, at);
            }
            // A shape that also carries a fill washes in behind its own
            // outline, once the outline is most of the way round.
            var fill = global.getComputedStyle(node).fill;
            if (fill && fill !== 'none' && node.dataset.drawFill !== 'off') {
              dtl.fromTo(node, { fillOpacity: 0 },
                { fillOpacity: 1, duration: Math.min(each, cfg.enter * 1.5), ease: cfg.enterEase },
                at + each * 0.6);
            }
          } else {
            dtl.fromTo(node, { opacity: 0, y: cfg.enterShift },
              { opacity: 1, y: 0, duration: Math.min(each, cfg.enter), ease: cfg.enterEase }, at);
          }
        });

        tl.add(dtl, opts.at == null ? '>' : opts.at);
        if (opts.duration == null || opts.duration === 'fill') {
          registerFlex(dtl, opts);
        } else {
          setSpan(dtl, opts.duration);
        }
        return dtl;
      },

      /** mark any tween/timeline as flexible — it absorbs the scene's slack */
      flex: function (child, opts) {
        if (!child) {
          console.warn('gsap-explainer: ctx.flex() was given nothing to flex — ignored.');
          return child;
        }
        if (child === tl) {
          console.warn('gsap-explainer: ctx.flex() was handed the scene timeline itself — ' +
            'ignored (flexing it would time-scale every tween in the scene). Pass the ' +
            'tween or nested timeline you want to stretch.');
          return child;
        }
        return registerFlex(child, opts);
      },

      /** an explicit pause in the sequence */
      hold: function (seconds, opts) {
        opts = opts || {};
        return place(gsap.to({}, { duration: seconds }), opts.at);
      },

      /** escape hatch: the raw scene timeline and the gsap instance */
      tl: tl,
      gsap: gsap,
      hasDrawSVG: hasDrawSVG,
    };
    return ctx;
  }

  // --- scene handoffs ----------------------------------------------------------
  // The boundary between scene i-1 and scene i is a named, per-boundary choice,
  // authored as `data-exit="…"` on the OUTGOING scene ("how this scene hands
  // off to the next" — the storyboard's vocabulary). The default is the brand
  // crossfade. Like the crossfade always has, a handoff's duration is charged
  // to the INCOMING scene's measured budget (`available = D − handoff`), so the
  // narration stays the clock.
  var TRANSITIONS = {
    cut:  function () { return 0; },
    fade: function (cfg) { return cfg.crossfade; },
    push: function (cfg) { return cfg.pushDuration; },
    zoom: function (cfg) { return cfg.zoomDuration; },
  };

  /** Build the boundary into the master timeline: incoming `el` becomes
   *  visible at `at`; outgoing `prevEl` (null for the first scene) is hidden
   *  by `at + xf`, with any handoff transform cleared once it is offstage. */
  function applyBoundary(master, name, prevEl, el, at, xf, cfg) {
    master.set(el, { visibility: 'visible' }, at);
    if (xf <= 0) {
      // A hard cut: the swap happens on one frame.
      master.set(el, { opacity: 1 }, at);
      if (prevEl) master.set(prevEl, { opacity: 0, visibility: 'hidden' }, at);
      return;
    }
    var inFrom = { opacity: 0 };
    var inTo = { opacity: 1, duration: xf, ease: cfg.enterEase };
    var outTo = { opacity: 0, duration: xf, ease: cfg.enterEase };
    if (name === 'push') {
      inFrom.y = cfg.pushShift; inTo.y = 0;
      outTo.y = -cfg.pushShift;
    } else if (name === 'zoom') {
      inFrom.scale = 1 - cfg.zoomScale; inTo.scale = 1;
      outTo.scale = 1 + cfg.zoomScale;
    }
    master.fromTo(el, inFrom, inTo, at);
    if (prevEl) {
      master.to(prevEl, outTo, at);
      master.set(prevEl, { visibility: 'hidden', clearProps: 'y,scale' }, at + xf);
    }
  }

  // --- the runner ------------------------------------------------------------

  /** Mark the page as a FAILED render. `data-done` still goes up, because it is
   *  the only channel `record.mjs` polls and leaving it down just makes the
   *  recorder burn its 5-minute ceiling and then ship whatever it captured.
   *  `data-done-reason` is what distinguishes a finished render from a broken
   *  one; record.mjs exits non-zero on anything but `complete`. */
  function markFailure(message) {
    try {
      document.body.dataset.error = message;
      document.body.dataset.doneReason = 'error';
      document.body.dataset.done = '1';
    } catch (e) { /* document.body gone — nothing useful left to do */ }
  }

  function run(options) {
    try {
      return runInner(options);
    } catch (err) {
      var msg = String((err && err.message) || err);
      console.error('gsap-explainer: render failed before it could start — ' + msg);
      markFailure(msg);
      throw err;
    }
  }

  function runInner(options) {
    options = options || {};
    var cfg = {};
    Object.keys(DEFAULTS).forEach(function (k) {
      cfg[k] = options[k] == null ? DEFAULTS[k] : options[k];
    });

    var root = options.root || document;
    var declared = options.scenes;
    var sceneEls = declared
      ? declared.map(function (s) {
          var el = s.el || root.querySelector(s.selector || ('[data-scene="' + s.id + '"]'));
          if (!el) throw new Error('gsap-explainer: no element for scene "' + s.id + '"');
          return el;
        })
      : toArray(root, '[data-scene]');

    if (!sceneEls.length) throw new Error('gsap-explainer: no [data-scene] elements found');

    // --- durations: injected wins, then the author's fallback, then a default
    var injected = global.SCENE_DURATIONS;
    var durations;
    if (Array.isArray(injected) && injected.length) {
      durations = injected.slice();
      if (durations.length !== sceneEls.length) {
        console.warn('gsap-explainer: SCENE_DURATIONS has ' + durations.length +
          ' entries but the page has ' + sceneEls.length + ' scenes — ' +
          'the SCRIPT.md row count and the scene count must match.');
      }
    } else {
      durations = (options.fallback || []).slice();
      console.warn('gsap-explainer: no window.SCENE_DURATIONS injected — using the fallback timings.');
    }
    while (durations.length < sceneEls.length) durations.push(4);
    durations = durations.slice(0, sceneEls.length);

    prepare(root === document ? document.body : root);

    var master = gsap.timeline({ paused: true });
    var at = 0;
    var prevEl = null;
    var timelines = [];
    var failure = null;

    function fail(message, err) {
      if (!failure) failure = message;
      console.error('gsap-explainer: ' + message + ((err && err.stack) ? '\n' + err.stack : ''));
    }

    sceneEls.forEach(function (el, i) {
      var D = durations[i];

      // The handoff INTO this scene is authored on the outgoing scene as
      // data-exit. The film's open (i === 0) is always a fade-in.
      var exitName = 'fade';
      if (i > 0 && prevEl.dataset && prevEl.dataset.exit) {
        var authored = prevEl.dataset.exit;
        if (TRANSITIONS[authored]) {
          exitName = authored;
        } else {
          console.warn('gsap-explainer: unknown data-exit="' + authored + '" on scene ' + i +
            ' (' + (prevEl.dataset.scene || prevEl.id || '?') + ') — known: ' +
            Object.keys(TRANSITIONS).join(', ') + '. Using "fade".');
        }
      }
      var xf = Math.min(TRANSITIONS[exitName](cfg), D / 2);
      var available = Math.max(D - xf, 0.1);

      var tl = gsap.timeline({ paused: true });
      var flexes = [];
      var ctx = makeContext(el, tl, available, cfg, flexes);

      var build = declared && declared[i] && declared[i].build;
      // A scene that cannot be built must not be papered over: without this the
      // exception escapes the load handler, `data-done` is never raised at all,
      // and the recorder produces a five-minute video of a broken page and
      // exits 0.
      try {
        if (build) {
          build(tl, ctx);
        } else {
          // Declarative default: enter everything marked [data-enter], then draw
          // everything marked [data-draw].
          if (el.querySelector('[data-enter]')) ctx.enter();
          if (el.querySelector('[data-draw]')) ctx.draw();
        }
      } catch (err) {
        fail('scene ' + (i + 1) + ' (' + (el.dataset.scene || el.id || '?') + ') failed to build: ' +
          String((err && err.message) || err), err);
      }

      timelines.push(tl);
      applyFlex(tl, flexes, available);
      if (tl.duration() > available + 1e-3) {
        // Content is longer than the narration allows — compress rather than
        // spill into the next scene, and say so.
        console.warn('gsap-explainer: scene ' + (i + 1) + ' (' + (el.dataset.scene || el.id || '?') +
          ') needs ' + tl.duration().toFixed(2) + 's but has ' + available.toFixed(2) +
          's — compressing. Shorten the animation or lengthen the narration.');
        tl.timeScale(tl.duration() / available);
      }

      applyBoundary(master, exitName, prevEl, el, at, xf, cfg);
      tl.paused(false);
      master.add(tl, at + xf);

      at += D;
      prevEl = el;
    });

    if (prevEl && prevEl.dataset && prevEl.dataset.exit) {
      console.warn('gsap-explainer: data-exit on the final scene has no effect — ' +
        'the film ends on the tail hold and the done signal, not a handoff.');
    }

    var total = at;
    // Anchor the master's length to the narration total, not to whatever the
    // last scene's animation happened to need.
    master.call(function () {}, null, total);

    var signalled = false;
    function signalDone(reason) {
      if (signalled) return;
      signalled = true;
      if (failure) {
        reason = 'error';
        document.body.dataset.error = failure;
      }
      document.body.dataset.done = '1';
      document.body.dataset.doneReason = reason || 'complete';
      if (options.onDone) options.onDone(reason || 'complete');
    }

    master.eventCallback('onComplete', function () {
      gsap.delayedCall(cfg.tail, function () { signalDone('complete'); });
    });

    // The recorder waits up to 5 minutes for the done flag. If a build threw or
    // a tween stalled, fail fast and visibly instead of burning that timeout.
    global.setTimeout(function () {
      if (!signalled) {
        console.error('gsap-explainer: watchdog fired — the master timeline did not complete in time.');
        signalDone('watchdog');
      }
    }, (total + cfg.tail + cfg.watchdogPad) * 1000);

    global.__explainer = {
      master: master, durations: durations, total: total,
      scenes: sceneEls, timelines: timelines,
      get failure() { return failure; },
    };

    if (failure) {
      // Do not spend the narration's worth of wall-clock recording a render we
      // already know is broken — signal the failure and let record.mjs fail.
      console.error('gsap-explainer: not starting — the render failed to build. ' +
        'record.mjs will exit non-zero rather than ship this.');
      signalDone('error');
      return global.__explainer;
    }

    if (options.autostart === false) return global.__explainer;
    master.play(0);
    return global.__explainer;
  }

  /** Convenience: run once the page (fonts, SVG, injected script) is settled. */
  function boot(options) {
    // `run` has already marked the page failed by the time it rethrows; swallow
    // here so a load handler does not also raise an uncaught error.
    function start() {
      try { return run(options); } catch (e) { return null; }
    }
    if (document.readyState === 'complete') {
      return start();
    }
    global.addEventListener('load', start);
    return null;
  }

  global.GsapExplainer = {
    run: run,
    boot: boot,
    defaults: DEFAULTS,
    hasDrawSVG: hasDrawSVG,
    version: '0.2.0',
  };
})(window);
