#!/usr/bin/env python3
"""Stdlib-only tests for output naming + work-dir cleanup (PR #14 review).

Run from the tool venv (PyYAML — the tool's only Python dep — installed):

    cd tools/explainer-video
    python3 tests/test_naming.py

Not CI-wired (repo CI is lint-only); run before touching parse_title,
sanitize_name, or the orchestrator's work-dir cleanup.

Covers:
  a. parse_title slugifies the first H1, and never returns an empty string —
     punctuation-only titles and missing H1s fall back to the deck dir name,
     then the script stem (R2);
  b. the slug is capped at 100 chars and never ends on a hyphen (N1);
  c. parse_title and _parse_title_raw read the SAME heading, so the filename
     and the embedded MP4 title cannot describe different headings;
  d. sanitize_name rejects any --name that is not a single path component —
     'x/../../renders' is what steers the work dir outside --out (N3);
  e. assert_safe_work_dir refuses to rmtree anything that is not a '.work-*'
     child of --out, including the traversal above (N3).
"""
from __future__ import annotations

import os
import sys
import tempfile
import unittest
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOL / "pipeline"))

from lib import (  # noqa: E402
    Profile,
    RunContext,
    Scene,
    _parse_title_raw,
    parse_title,
    sanitize_name,
)

SCENES = [Scene(id="s1", narration="n", subtitle="s")]


def write_script(root: Path, deck: str, body: str) -> Path:
    """Create <root>/<deck>/video/SCRIPT.md — the real deck layout."""
    d = root / deck / "video"
    d.mkdir(parents=True, exist_ok=True)
    p = d / "SCRIPT.md"
    p.write_text(body)
    return p


def make_ctx(root: Path, name: str, work: Path | None = None) -> RunContext:
    out_dir = (root / "out").resolve()
    return RunContext(
        script=Path("unused"), slides=Path("unused"),
        profile=Profile(name="testprof", engine="qwen", model=""),
        out_dir=out_dir, name=name, scenes=SCENES,
        work=work if work is not None else out_dir / f".work-{name}-testprof",
    )


class ParseTitleTest(unittest.TestCase):
    def test_slugifies_first_h1(self):
        with tempfile.TemporaryDirectory() as td:
            p = write_script(Path(td), "assay-decks",
                             "# Assay explainer — the assay office\n")
            self.assertEqual(parse_title(p), "assay-explainer-the-assay-office")

    def test_no_h1_falls_back_to_deck_dir(self):
        with tempfile.TemporaryDirectory() as td:
            p = write_script(Path(td), "assay-decks", "no heading here\n## sub\n")
            self.assertEqual(parse_title(p), "assay-decks")

    def test_empty_slug_falls_back_to_deck_dir(self):
        """R2: an H1 that survives slugification as '' must not become ''."""
        for title in ("# !!!\n", "# ..\n", "#    \n", "# ---\n"):
            with self.subTest(title=title), tempfile.TemporaryDirectory() as td:
                p = write_script(Path(td), "assay-decks", title)
                self.assertEqual(parse_title(p), "assay-decks")

    def test_never_returns_empty(self):
        """Deck-dir fallback can itself be empty near the filesystem root.

        `parse_title` never resolves its `script` argument, so a *relative*
        path one directory level down makes `script.parent.parent` genuinely
        `.` — and `Path('.').name == ''` regardless of where the real cwd
        sits — pinning the case the docstring describes instead of the
        cwd's actual parent (which is essentially never empty, so the prior
        fixture using an absolute `Path(td) / "SCRIPT.md"` never reached the
        `or script.stem` arm at all: deleting that arm still left all 12
        tests green).
        """
        cwd = os.getcwd()
        with tempfile.TemporaryDirectory() as td:
            os.chdir(td)
            try:
                rel = Path("sub/SCRIPT.md")
                rel.parent.mkdir(parents=True, exist_ok=True)
                rel.write_text("# !!!\n")
                # fixture invariant: the deck-dir arm really is empty here
                self.assertEqual(rel.parent.parent.name, "")
                result = parse_title(rel)
                self.assertTrue(result, "parse_title returned an empty name")
                # falls all the way through to the script stem arm
                self.assertEqual(result, rel.stem)
            finally:
                os.chdir(cwd)

    def test_traversal_is_neutralised(self):
        with tempfile.TemporaryDirectory() as td:
            p = write_script(Path(td), "assay-decks", "# ../../etc/passwd\n")
            slug = parse_title(p)
            self.assertEqual(slug, "etcpasswd")
            self.assertEqual(Path(slug).name, slug)

    def test_length_cap_and_no_trailing_hyphen(self):
        """N1: cap at 100, and a cut landing on a hyphen must be stripped."""
        with tempfile.TemporaryDirectory() as td:
            p = write_script(Path(td), "assay-decks", "# " + ("A" * 300) + "\n")
            self.assertEqual(len(parse_title(p)), 100)

            p2 = write_script(Path(td), "b", "# " + ("a" * 99) + " tail words\n")
            slug = parse_title(p2)
            self.assertLessEqual(len(slug), 100)
            self.assertFalse(slug.endswith("-"), f"trailing hyphen in {slug!r}")

    def test_filename_and_metadata_read_the_same_heading(self):
        """A first H1 that slugs empty must not let the two diverge."""
        with tempfile.TemporaryDirectory() as td:
            p = write_script(Path(td), "assay-decks",
                             "# !!!\n\ntext\n\n# Real Second Title\n")
            self.assertEqual(_parse_title_raw(p), "!!!")
            # falls back to the deck dir — NOT the second heading
            self.assertEqual(parse_title(p), "assay-decks")


class SanitizeNameTest(unittest.TestCase):
    def test_accepts_plain_component_verbatim(self):
        for name in ("medici-decks", "My_Deck", "deck.v2"):
            with self.subTest(name=name):
                self.assertEqual(sanitize_name(name), name)

    def test_rejects_separators_and_traversal(self):
        """N3: these are the names that steer the work dir outside --out."""
        for name in ("x/../../renders", "../evil", "a/b", "..", ".", "/abs", ""):
            with self.subTest(name=name):
                with self.assertRaises(SystemExit):
                    sanitize_name(name)


class WorkDirGuardTest(unittest.TestCase):
    def test_accepts_the_real_work_dir(self):
        with tempfile.TemporaryDirectory() as td:
            ctx = make_ctx(Path(td), "fixture")
            self.assertEqual(ctx.assert_safe_work_dir(), ctx.work.resolve())

    def test_refuses_traversal_out_of_out_dir(self):
        """The exact escape: out/.work-x/../../renders-testprof."""
        with tempfile.TemporaryDirectory() as td:
            root = Path(td).resolve()
            out_dir = root / "out"
            (out_dir / ".work-x").mkdir(parents=True)
            bystander = root / "renders-testprof"
            bystander.mkdir()
            (bystander / "keep.mp4").write_text("months of renders\n")

            ctx = make_ctx(root, "x/../../renders",
                           work=out_dir / ".work-x/../../renders-testprof")
            # sanity: without the guard this really does resolve onto bystander
            self.assertEqual(ctx.work.resolve(), bystander)

            with self.assertRaises(SystemExit):
                ctx.assert_safe_work_dir()
            self.assertTrue((bystander / "keep.mp4").exists())

    def test_refuses_out_dir_itself_and_foreign_children(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td).resolve()
            for work in (root / "out", root / "out" / "renders", root / "elsewhere"):
                with self.subTest(work=work):
                    ctx = make_ctx(root, "fixture", work=work)
                    with self.assertRaises(SystemExit):
                        ctx.assert_safe_work_dir()


if __name__ == "__main__":
    unittest.main(verbosity=2)
