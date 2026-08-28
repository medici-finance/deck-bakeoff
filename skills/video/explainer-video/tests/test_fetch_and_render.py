#!/usr/bin/env python3
"""Stdlib-only tests for fetch-and-render's pure logic (no gh, no network).

Run from anywhere with the repo checked out:

    cd tools/explainer-video
    python3 tests/test_fetch_and_render.py

Not CI-wired (repo CI is lint-only). Covers the parts that decide correctness
without touching GitHub — the gh plumbing (resolve/fetch) is exercised live via
the tool's own --dry-run self-check against a real PR.

Covers:
  a. PR-URL vs bare-number parsing (_PR_URL_RE);
  b. metadata block extraction (slug/title -> name, url-field -> url, fallbacks);
  c. candidate-dir derivation from a changed-file list (de-dup, order, root);
  d. slug sanitising (single component, cap, no trailing hyphen);
  e. render_command: --script/--slides/--name/--url defaults come FIRST and the
     forwarded args come AFTER (so a forwarded flag overrides via argparse
     last-wins) — the whole point of the pass-through;
  f. `--` splitting of argv into (mine, forwarded);
  g. stage_bundle stages cover.png when the bundle carries one (binary bytes
     round-trip identically) and leaves Bundle.cover None when it does not —
     gh calls are faked, no network;
  h. render_command injects a default --out of ~/Downloads/videos that a
     forwarded --out overrides (again by argparse last-wins).
"""
from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

TOOL_ROOT = Path(__file__).resolve().parent.parent


def _load_tool():
    """Import the `fetch-and-render` script (no .py extension) as a module."""
    path = TOOL_ROOT / "fetch-and-render"
    spec = importlib.util.spec_from_loader(
        "fetch_and_render", importlib.machinery.SourceFileLoader("fetch_and_render", str(path))
    )
    mod = importlib.util.module_from_spec(spec)
    # Register before exec so dataclasses (which look the class's module up in
    # sys.modules) resolve during module execution.
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


far = _load_tool()


class PRParsing(unittest.TestCase):
    def test_url_is_self_describing(self):
        m = far._PR_URL_RE.search(
            "https://github.com/medici-finance/assay-site/pull/412")
        self.assertEqual(m.group("owner"), "medici-finance")
        self.assertEqual(m.group("repo"), "assay-site")
        self.assertEqual(m.group("number"), "412")

    def test_bare_number_needs_repo(self):
        self.assertTrue("412".isdigit())
        self.assertIsNone(far._PR_URL_RE.search("412"))


class MetadataExtraction(unittest.TestCase):
    META = (
        '<html><head>'
        '<script type="application/json" id="assay-article">\n'
        '{"title": "Assay and Jira: where the record of done would live",\n'
        ' "category": "how-assay-works", "slug": "assay-and-jira",\n'
        ' "video": "https://youtu.be/x", "status": "published"}\n'
        '</script></head><body>...</body></html>'
    )

    def test_parse_meta(self):
        meta = far._parse_meta(self.META)
        self.assertEqual(meta["slug"], "assay-and-jira")
        self.assertEqual(meta["category"], "how-assay-works")

    def test_name_prefers_slug(self):
        meta = far._parse_meta(self.META)
        self.assertEqual(far._name_from_meta(meta, "some/dir"), "assay-and-jira")

    def test_name_falls_back_to_title_then_dir(self):
        self.assertEqual(
            far._name_from_meta({"title": "Hello, World!"}, "d"), "hello-world")
        self.assertEqual(
            far._name_from_meta({}, "public/blog/x/my-slug"), "my-slug")

    def test_url_falls_back_to_pr_url(self):
        meta = far._parse_meta(self.META)  # no url-ish key present
        self.assertEqual(
            far._url_from_meta(meta, "https://github.com/o/r/pull/9"),
            "https://github.com/o/r/pull/9")

    def test_url_honoured_when_present(self):
        self.assertEqual(
            far._url_from_meta({"canonical": "https://assay.guide/x/"}, "PRURL"),
            "https://assay.guide/x/")

    def test_bad_json_is_empty(self):
        self.assertEqual(far._parse_meta(
            '<script id="assay-article">{not json}</script>'), {})
        self.assertEqual(far._parse_meta("<html>no block</html>"), {})


class CandidateDirs(unittest.TestCase):
    def test_dedup_order_and_root(self):
        changed = [
            "public/blog/a/slug1/SCRIPT.md",
            "public/blog/a/slug1/explainer.html",
            "public/blog/a/slug1/index.html",
            "public/blog/b/slug2/SCRIPT.md",
            "top-level.md",
        ]
        self.assertEqual(
            far._candidate_dirs(changed),
            ["public/blog/a/slug1", "public/blog/b/slug2", ""],
        )


class Slug(unittest.TestCase):
    def test_single_component_no_traversal(self):
        s = far._slug("../../etc/passwd")
        self.assertNotIn("/", s)
        self.assertNotIn("..", s)

    def test_cap_and_trailing_hyphen(self):
        s = far._slug("x" * 200)
        self.assertLessEqual(len(s), 100)
        self.assertFalse(s.endswith("-"))
        self.assertEqual(far._slug("!!!"), "explainer")  # empty -> fallback


class RenderCommand(unittest.TestCase):
    def setUp(self):
        # render_command creates its default --out dir (Path.home()/Downloads/
        # videos). Redirect Path.home() at a per-test tempdir so the mkdir side
        # effect never touches the real home.
        self._home = tempfile.TemporaryDirectory()
        self.addCleanup(self._home.cleanup)
        p = mock.patch.object(far.Path, "home",
                              return_value=Path(self._home.name))
        p.start()
        self.addCleanup(p.stop)

    def _bundle(self):
        pr = far.PRRef(repo="medici-finance/assay-site", number=412,
                       url="https://github.com/medici-finance/assay-site/pull/412")
        with tempfile.TemporaryDirectory() as td:
            script = Path(td) / "SCRIPT.md"
            slides = Path(td) / "explainer.html"
            script.write_text("# t")
            slides.write_text("<html></html>")
            return far.Bundle(pr=pr, src_dir="public/blog/x/assay-and-jira",
                              name="assay-and-jira", url=pr.url,
                              script=script, slides=slides)

    def test_defaults_first_forwarded_last(self):
        b = self._bundle()
        cmd = far.render_command(b, ["--profile", "australian-assay", "--out", "./out"])
        # our supplied inputs are present ...
        self.assertIn("--script", cmd)
        self.assertIn("--slides", cmd)
        self.assertEqual(cmd[cmd.index("--name") + 1], "assay-and-jira")
        # ... and everything forwarded is at the TAIL, verbatim and in order
        self.assertEqual(cmd[-4:], ["--profile", "australian-assay", "--out", "./out"])
        # first element is the render entrypoint
        self.assertTrue(cmd[0].endswith("explainer-video"))

    def test_forwarded_override_wins_by_position(self):
        # A forwarded --name/--url comes AFTER our default, so argparse (which the
        # engine uses) takes the last occurrence — the caller's value wins.
        b = self._bundle()
        cmd = far.render_command(b, ["--profile", "x", "--url", "https://override/"])
        our_url_idx = cmd.index("--url")
        their_url_idx = len(cmd) - 2
        self.assertLess(our_url_idx, their_url_idx)
        self.assertEqual(cmd[their_url_idx + 1], "https://override/")

    def test_default_out_injected_and_created(self):
        # With no forwarded --out, our default (~/Downloads/videos, here the
        # sandboxed home) is in the command AND the directory is created.
        b = self._bundle()
        cmd = far.render_command(b, ["--profile", "english-assay"])
        default_out = Path(self._home.name) / "Downloads" / "videos"
        self.assertIn("--out", cmd)
        self.assertEqual(cmd[cmd.index("--out") + 1], str(default_out))
        self.assertTrue(default_out.is_dir(), "default --out dir should be created")

    def test_forwarded_out_overrides_default(self):
        # A forwarded --out lands AFTER our default, so argparse (engine uses a
        # single-value store) takes the last one — the caller's value wins.
        b = self._bundle()
        cmd = far.render_command(b, ["--profile", "x", "--out", "/tmp/custom-out"])
        out_idxs = [i for i, v in enumerate(cmd) if v == "--out"]
        self.assertEqual(len(out_idxs), 2, "our default + the forwarded --out")
        self.assertLess(out_idxs[0], out_idxs[1])
        # ours first (the sandboxed default), theirs last and verbatim at the tail
        self.assertEqual(cmd[out_idxs[0] + 1],
                         str(Path(self._home.name) / "Downloads" / "videos"))
        self.assertEqual(cmd[out_idxs[1] + 1], "/tmp/custom-out")
        self.assertEqual(cmd[-2:], ["--out", "/tmp/custom-out"])


class StageBundleCover(unittest.TestCase):
    """stage_bundle stages cover.png when present, with a binary round-trip; gh
    plumbing (_content_exists / _fetch_raw) is faked from an in-memory repo."""

    # Bytes spanning 0x00..0xFF: not valid UTF-8, proves the path is binary.
    PNG = bytes(range(256)) * 4

    def _stage(self, repo_files: dict) -> tuple:
        """Run stage_bundle against a fake head repo (path -> bytes). Returns
        (bundle, cover_bytes) — cover bytes read while the workdir is alive."""
        pr = far.PRRef(repo="medici-finance/assay-site", number=57,
                       url="https://github.com/medici-finance/assay-site/pull/57")
        src_dir = "public/blog/x/my-slug"

        def fake_exists(repo, path, ref):
            return path in repo_files

        def fake_fetch(repo, path, ref, dest):
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(repo_files[path])

        with mock.patch.object(far, "_content_exists", fake_exists), \
                mock.patch.object(far, "_fetch_raw", fake_fetch), \
                tempfile.TemporaryDirectory() as td:
            b = far.stage_bundle(pr, pr.repo, "d" * 40, src_dir, Path(td))
            cover_bytes = b.cover.read_bytes() if b.cover else None
            cover_name = b.cover.name if b.cover else None
            return b, cover_bytes, cover_name

    def _base_files(self) -> dict:
        s = "public/blog/x/my-slug"
        return {
            f"{s}/SCRIPT.md": b"# title\n",
            f"{s}/explainer.html": b"<html></html>",
        }

    def test_cover_staged_when_present_binary_roundtrip(self):
        files = self._base_files()
        files["public/blog/x/my-slug/cover.png"] = self.PNG
        b, cover_bytes, cover_name = self._stage(files)
        self.assertIsNotNone(b.cover, "cover should be staged when present")
        self.assertEqual(cover_name, "cover.png")
        # bytes identical — the PNG round-trips through the binary fetch path
        self.assertEqual(cover_bytes, self.PNG)

    def test_cover_absent_is_graceful(self):
        b, cover_bytes, _ = self._stage(self._base_files())  # no cover.png
        self.assertIsNone(b.cover, "cover stays None when the bundle has none")
        self.assertIsNone(cover_bytes)
        # the required files still staged
        self.assertTrue(b.script.exists() or b.script.name == "SCRIPT.md")


class ArgSplit(unittest.TestCase):
    def test_split_on_double_dash(self):
        mine, fwd = far._split_forwarded(
            ["412", "--repo", "o/r", "--", "--profile", "australian-assay"])
        self.assertEqual(mine, ["412", "--repo", "o/r"])
        self.assertEqual(fwd, ["--profile", "australian-assay"])

    def test_no_double_dash(self):
        mine, fwd = far._split_forwarded(["412", "--dry-run"])
        self.assertEqual(mine, ["412", "--dry-run"])
        self.assertEqual(fwd, [])


if __name__ == "__main__":
    unittest.main()
