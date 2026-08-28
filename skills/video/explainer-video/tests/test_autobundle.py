#!/usr/bin/env python3
"""Tests for the orchestrator's auto-bundle step (the un-bundled-deck fix).

Run from the tool venv (PyYAML — the tool's only Python dep — installed):

    cd tools/explainer-video
    python3 tests/test_autobundle.py

Not CI-wired (repo CI is lint-only); run before touching the orchestrator's
_has_unbundled_slots / maybe_bundle_slides.

Background — the incident this covers:
    A deck's explainer.html ships with un-inlined `<!-- gsap-explainer:inline …
    -->` slots until `renderers/gsap/bundle.mjs` fills them with the GSAP runtime.
    A human passed an UN-bundled deck to --slides: window.GsapExplainer was
    undefined, nothing animated, document.body.dataset.done was never set, and
    record.mjs burned its full timeout before failing. The fix auto-bundles the
    WORK COPY of the slides at render time so the deck renders whether or not the
    author pre-bundled — and never touches the author's source deck.

Covers:
  a. _has_unbundled_slots detection: True for the shipped template (placeholder
     slots), False for a bundled deck (real payload), False for a hand-rolled
     deck (no slots) — the decision is static, needing no node_modules;
  b. maybe_bundle_slides on an un-bundled work copy inlines the runtime in place,
     leaving it self-contained (GsapExplainer present, gsap core present) with
     exactly one SCENE_DURATIONS literal (skipped without the gsap node_modules);
  c. maybe_bundle_slides is idempotent and leaves an already-bundled deck
     byte-for-byte untouched (no double-bundle);
  d. maybe_bundle_slides operates on ctx.slides_rendered only — the author's
     ctx.slides source deck is never modified.
"""
from __future__ import annotations

import importlib.machinery
import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOL / "pipeline"))

# The orchestrator is an extensionless script ("explainer-video"); load it as a
# module so its helpers can be exercised directly.
_spec = importlib.util.spec_from_loader(
    "explainer_video_cli",
    importlib.machinery.SourceFileLoader("explainer_video_cli", str(TOOL / "explainer-video")),
)
ev = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ev)

from lib import Profile, RunContext, Scene  # noqa: E402

GSAP_DIR = TOOL / "renderers" / "gsap"
TEMPLATE = GSAP_DIR / "template.html"
GSAP_INSTALLED = (GSAP_DIR / "node_modules" / "gsap" / "dist" / "gsap.min.js").exists()
HAVE_NODE = shutil.which("node") is not None


def _bundled_template_html() -> str:
    """A minimal deck with a FILLED inline slot — a real payload, not a
    placeholder. Large enough (> _FILLED_SLOT_MIN_BYTES) to read as bundled."""
    payload = "/* real inlined source */\n" + ("x" * 1000)
    return (
        "<!doctype html><html><body>\n"
        "<section data-scene=\"a\"><h1 data-enter>A</h1></section>\n"
        "<!-- gsap-explainer:inline runtime -->\n"
        f"<script>{payload}</script>\n"
        "<!-- /gsap-explainer:inline -->\n"
        "<script>window.SCENE_DURATIONS = [];</script>\n"
        "</body></html>\n"
    )


def _hand_rolled_html() -> str:
    """A deck predating the GSAP adapter — its own JS, no inline slots."""
    return (
        "<!doctype html><html><body>\n"
        "<section class=\"scene\"><h1>Hand-rolled</h1></section>\n"
        "<script>/* bespoke per-deck animation */ document.body.dataset.done = '1';</script>\n"
        "<script>window.SCENE_DURATIONS = [];</script>\n"
        "</body></html>\n"
    )


class DetectionTest(unittest.TestCase):
    def test_template_is_detected_as_unbundled(self):
        self.assertTrue(ev._has_unbundled_slots(TEMPLATE.read_text()),
                        "the shipped template has placeholder slots and must read as un-bundled")

    def test_bundled_deck_is_not_flagged(self):
        self.assertFalse(ev._has_unbundled_slots(_bundled_template_html()),
                         "a slot holding real source must not read as un-bundled")

    def test_hand_rolled_deck_is_not_flagged(self):
        self.assertFalse(ev._has_unbundled_slots(_hand_rolled_html()),
                         "a deck with no inline slots must be left alone")

    def test_empty_slot_is_flagged(self):
        html = ("<body><!-- gsap-explainer:inline gsap --><!-- /gsap-explainer:inline -->"
                "<script>window.SCENE_DURATIONS=[];</script></body>")
        self.assertTrue(ev._has_unbundled_slots(html),
                        "a truly-empty slot must read as un-bundled")


def _make_ctx(out_dir: Path, slides_src: Path, name: str = "fixture") -> RunContext:
    profile = Profile(name="testprof", engine="orpheus", model="m", voice="v")
    work = out_dir / f".work-{name}-{profile.name}"
    work.mkdir(parents=True, exist_ok=True)
    return RunContext(
        script=out_dir / "SCRIPT.md", slides=slides_src, profile=profile,
        out_dir=out_dir, name=name, scenes=[Scene("a", "n", "s")], work=work,
    )


@unittest.skipUnless(HAVE_NODE and GSAP_INSTALLED,
                     "needs node + `npm install` in renderers/gsap (the bundler's gsap sources)")
class BundleIntegrationTest(unittest.TestCase):
    """Drives the real bundle.mjs against the shipped template, exactly as the
    orchestrator does at render time."""

    def _prepare(self, td: Path):
        # The author's source deck: a copy of the (un-bundled) shipped template.
        src = td / "explainer.html"
        shutil.copy(TEMPLATE, src)
        ctx = _make_ctx(td / "out", src)
        # Mimic inject_durations writing the work copy from the source.
        html = src.read_text()
        html = ev._SD_RE.sub("window.SCENE_DURATIONS=[3.0, 4.0];", html, count=1)
        ctx.slides_rendered.write_text(html)
        return ctx, src

    def test_unbundled_workcopy_becomes_self_contained(self):
        with tempfile.TemporaryDirectory() as td:
            ctx, src = self._prepare(Path(td))
            src_before = src.read_text()

            ev.maybe_bundle_slides(ctx)

            out = ctx.slides_rendered.read_text()
            # The runtime is now inlined: its global and the gsap core are present.
            self.assertIn("window.GsapExplainer", out,
                          "runtime was not inlined — the work copy is still un-bundled")
            self.assertIn("gsap", out.lower())
            self.assertFalse(ev._has_unbundled_slots(out),
                             "work copy still reads as un-bundled after bundling")
            # Exactly one SCENE_DURATIONS ASSIGNMENT survives (the pipeline
            # rewrites the first match; a second would silently steal the
            # injection). Count assignments with the pipeline's own regex, not the
            # bare string — the inlined runtime mentions window.SCENE_DURATIONS in
            # its comments/warnings, which is exactly why the contract is about the
            # `= [...]` assignment, not the identifier.
            self.assertEqual(len(ev._SD_RE.findall(out)), 1,
                             "bundling must preserve exactly one SCENE_DURATIONS assignment")
            self.assertIn("[3.0, 4.0]", out, "the injected durations were lost")
            # The author's source deck must be untouched.
            self.assertEqual(src.read_text(), src_before,
                             "maybe_bundle_slides modified the author's source deck")

    def test_bundling_is_idempotent(self):
        with tempfile.TemporaryDirectory() as td:
            ctx, _src = self._prepare(Path(td))
            ev.maybe_bundle_slides(ctx)
            once = ctx.slides_rendered.read_text()
            # A now-bundled deck is detected as such and skipped — byte-identical.
            ev.maybe_bundle_slides(ctx)
            twice = ctx.slides_rendered.read_text()
            self.assertEqual(once, twice, "second auto-bundle changed the file — not idempotent")

    def test_already_bundled_deck_is_left_untouched(self):
        """A fresh bundle re-run through the real bundler is byte-identical, so an
        already-bundled deck renders exactly as before."""
        with tempfile.TemporaryDirectory() as td:
            work = Path(td) / "slides.html"
            shutil.copy(TEMPLATE, work)
            # Bundle it once so it is genuinely self-contained.
            subprocess.run(["node", str(GSAP_DIR / "bundle.mjs"), str(work)], check=True)
            bundled = work.read_text()
            self.assertFalse(ev._has_unbundled_slots(bundled))

            profile = Profile(name="p", engine="orpheus", model="m")
            ctx = RunContext(
                script=Path(td) / "SCRIPT.md", slides=Path(td) / "explainer.html",
                profile=profile, out_dir=Path(td) / "out", name="n",
                scenes=[Scene("a", "n", "s")], work=Path(td),
            )
            # work == ctx.slides_rendered? No — point slides_rendered at our file.
            # RunContext.slides_rendered = work/"slides.html"; work=td so it is our file.
            ev.maybe_bundle_slides(ctx)
            self.assertEqual(work.read_text(), bundled,
                             "an already-bundled deck was modified by the auto-bundle step")


if __name__ == "__main__":
    unittest.main(verbosity=2)
