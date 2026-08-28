#!/usr/bin/env python3
"""Structural + brand checks for a deck built against a brand contract (brand.toml).

Adapted from create-html-deck's `scripts/check_deck.py` (MIT, (c) tt-a1i). The HARNESS is
the lift: stdlib-only `HTMLParser`, a flat finding accumulator, exit 1 on any error, one
`PASS:` summary line. The RULE TABLE is re-pinned wholesale to the house output shape,
because the upstream table encodes a different house's contract and emits six false errors
against a perfectly good house deck:

  * upstream required `width:1920px` / `height:1080px` / a centred `scale()` transform.
    The house geometry is viewport-fluid (100vw/100vh, `.slide{position:absolute;inset:0}`,
    `@page{size:landscape}`). Those three regexes are removed, and the house geometry is
    required in their place.
  * upstream required `localStorage` slide persistence. A confidential deck deliberately
    does not persist reading position into the viewer's browser profile. Removed.
  * upstream counted only `<article class="slide">`. House skeletons use `<div>`, this
    contender uses `<section>`. The selector is now "any element carrying the `slide`
    class", so the slide count is never silently zero.

Added house invariants: the mandatory `<meta name="deck-footer">` and its two-value class
enum (caught here, BEFORE the PDF renderer hard-errors on it), the per-slide print footer,
the pinned IBM Plex font set, offline-only assets, the closed layout pool, the
key-question and action-title smells, process-language and placeholder leaks, an accent
budget, and `deck.md` <-> `index.html` parity.

Scoped ignores use the house `.impeccable` shape verbatim — a `detector` object carrying
`ignoreRules` / `ignoreFiles` / `ignoreValues[]`, every value entry carrying a `reason`.
No second ignore syntax is invented.

Second re-pin (2026-08-18, packaging into skills/deck-author): the geometry rule now
requires the WINNING house contract from the deck bake-off — a fixed 1280x720 letterboxed
16:9 stage scaled to fit the viewport (brands/medici/deck-skeleton-external.html), NOT the
viewport-fluid geometry the composite contender pinned. Rationale: the fixed stage makes
the presenter's view, a screenshot, and the PDF page the same composition, which is what
the render-and-look gate screenshots depend on. The folio check also accepts the
skeleton's `.slide-no` bare-number markers alongside `.folio` "N / N" pairs.

Third re-pin (2026-08-18, brand parameterization): the brand-specific pins — the footer
enum, the font allowlist, the accent budget, the remote-asset severity, the pure-tone
expectations — now come from a brand.toml CONTRACT instead of constants, so one linter
serves any brand. Resolution order (same as the skill's): --brand <path> → brand.toml
walking up from the deck to the consuming repo's root (nearest .git) → the skill's
shipped default instance (brands/medici/brand.toml) → none. With no contract (or
`--brand none`) every brand gate SKIPs with a printed notice and only the structural
checks rule — and a brand-neutral deck carries no confidentiality footer unless one is
given. TOML parses via stdlib tomllib (python >= 3.11): on an older python an EXPLICIT
--brand is a hard error (exit 2), while a merely-discovered contract downgrades to the
no-contract SKIP path with a notice. The linter stays stdlib-only either way.

Known limit, stated rather than hidden: this is a STATIC parser. A deck whose slides are
built by script (the staged bake-off decks build their DOM from a JS slide array) is
invisible to it — S-SLIDES reports 0 and everything downstream is noise. The deck-author
contract therefore requires slides as static markup; the render-and-look gate, not this
linter, is what exercises the live DOM.

Usage:
    python3 check_deck.py <deck>/index.html [--deck-md <deck>/deck.md]
                          [--brand <brand.toml> | --brand none]
                          [--config .deckcheck.json] [--quiet]

Exit: 0 clean (notices may print), 1 one or more errors, 2 usage/IO problem.
"""

from __future__ import annotations

import argparse
import html as htmlmod
import json
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

# ---------------------------------------------------------------- brand contract

GENERIC_FONTS = {
    # The generic fallback stack any brand may resolve to.
    "ui-monospace",
    "sfmono-regular",
    "menlo",
    "monospace",
    "system-ui",
    "sans-serif",
    "serif",
    "-apple-system",
    "blinkmacsystemfont",
    "inherit",
    "initial",
}


class Brand:
    """The parsed brand contract. `None` in its place means: brand gates SKIP."""

    def __init__(self, data: dict, path: Path) -> None:
        self.path = path
        ident = data.get("identity", {}) or {}
        self.org = str(ident.get("org", "")).strip()
        self.footer_enum: dict[str, str] = {}
        if ident.get("footer_internal"):
            self.footer_enum[str(ident["footer_internal"]).strip()] = "internal"
        if ident.get("footer_external"):
            self.footer_enum[str(ident["footer_external"]).strip()] = "external"

        typ = data.get("type", {}) or {}
        families = [typ.get("sans"), typ.get("mono"), *typ.get("extra_families", [])]
        self.font_allow = GENERIC_FONTS | {str(n).strip().lower() for n in families if n}

        pal = data.get("palette", {}) or {}
        self.canvas = str(pal.get("canvas", "")).strip().lower()
        self.text_primary = str(pal.get("text_primary", "")).strip().lower()

        rules = data.get("rules", {}) or {}
        self.accent_budget = int(rules.get("accent_budget", MAX_ACCENT_PER_SLIDE))
        self.no_remote = bool(rules.get("no_remote_assets", True))


def load_brand(path: Path) -> Brand:
    try:
        import tomllib
    except ImportError as exc:  # python < 3.11
        raise RuntimeError(
            "parsing brand.toml needs stdlib tomllib (python >= 3.11); "
            "upgrade python or run with --brand none"
        ) from exc
    with path.open("rb") as fh:
        return Brand(tomllib.load(fh), path)


def resolve_brand(arg: str | None, deck_path: Path) -> tuple[Brand | None, str]:
    """The skill's resolution order. Returns (brand-or-None, how-it-resolved)."""
    if arg == "none":
        return None, "brand gates skipped by --brand none"
    if arg:
        path = Path(arg).expanduser().resolve()
        if not path.is_file():
            raise RuntimeError(f"brand contract not found: {path}")
        return load_brand(path), f"explicit --brand {path}"
    # walk up from the deck to the consuming repo's root (nearest .git)
    probe = deck_path.parent
    while True:
        candidate = probe / "brand.toml"
        if candidate.is_file():
            try:
                return load_brand(candidate), f"discovered at {candidate}"
            except RuntimeError as exc:
                return None, f"found {candidate} but could not parse it ({exc}) — brand gates SKIP"
        if (probe / ".git").exists() or probe.parent == probe:
            break
        probe = probe.parent
    # the skill's shipped default instance
    shipped = Path(__file__).resolve().parent.parent / "brands" / "medici" / "brand.toml"
    if shipped.is_file():
        try:
            return load_brand(shipped), f"shipped default instance {shipped}"
        except RuntimeError as exc:
            return None, f"shipped default present but unusable ({exc}) — brand gates SKIP"
    return None, "no brand contract discoverable — brand gates SKIP"


# ---------------------------------------------------------------- structural constants

LAYOUT_POOL = {
    "L-COVER",
    "L-STATEMENT",
    "L-TWO-COL",
    "L-TABLE",
    "L-CODE",
    "L-DIAGRAM",
    "L-STAT-ROW",
    "L-COMPARE",
    "L-SEQUENCE",
    "L-CLOSING",
}

# Layouts that carry no action title / key question by design.
CHROME_LAYOUTS = {"L-COVER", "L-CLOSING"}

VOID_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input", "link",
    "meta", "param", "source", "track", "wbr",
}

PROCESS_LEAK = [
    "option a", "option b", "option c", "preview.md", "deck.md", "index.html",
    "skill.md", "audience:", "slide map", "style preset", "bold option",
    "safe option", "for internal sharing", "generated from",
]

PLACEHOLDER = [
    "lorem ipsum", "todo", "fixme", "acme corp", "john doe", "jane doe",
    "placeholder", "your company", "xxx", "tbd",
]

MAX_ACCENT_PER_SLIDE = 2
DECKMD_COVERAGE_FLOOR = 0.85

ERROR = "error"
NOTICE = "notice"


# ---------------------------------------------------------------- findings + ignores


class Findings:
    """Flat accumulator. Errors fail the run; notices report and pass."""

    def __init__(self, config: dict) -> None:
        detector = (config or {}).get("detector", {}) or {}
        self.ignore_rules = {r.lower() for r in detector.get("ignoreRules", [])}
        self.ignore_values = [
            (str(e.get("rule", "")).lower(), str(e.get("value", "")).lower())
            for e in detector.get("ignoreValues", [])
            if e.get("reason")  # an entry with no written reason is not an ignore
        ]
        self.rows: list[tuple[str, str, str]] = []
        self.suppressed: list[str] = []

    def _suppressed(self, rule: str, value: str | None) -> bool:
        rule_l = rule.lower()
        if rule_l in self.ignore_rules:
            return True
        val_l = (value or "").lower()
        return any(r == rule_l and (v == val_l or v in val_l) for r, v in self.ignore_values)

    def add(self, severity: str, rule: str, message: str, value: str | None = None) -> None:
        if self._suppressed(rule, value):
            self.suppressed.append(f"{rule}: {message}")
            return
        self.rows.append((severity, rule, message))

    def error(self, rule: str, message: str, value: str | None = None) -> None:
        self.add(ERROR, rule, message, value)

    def notice(self, rule: str, message: str, value: str | None = None) -> None:
        self.add(NOTICE, rule, message, value)

    @property
    def errors(self) -> list[tuple[str, str, str]]:
        return [r for r in self.rows if r[0] == ERROR]

    @property
    def notices(self) -> list[tuple[str, str, str]]:
        return [r for r in self.rows if r[0] == NOTICE]


# ---------------------------------------------------------------- parser


class Slide:
    def __init__(self, index: int, attrs: dict) -> None:
        self.index = index
        self.attrs = attrs
        self.layout = (attrs.get("data-layout") or "").strip()
        self.question = (attrs.get("data-question") or "").strip()
        self.title = ""
        self.text_parts: list[str] = []
        self.accent_hits = 0

    @property
    def text(self) -> str:
        return " ".join(" ".join(self.text_parts).split())


class DeckParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.html_lang = ""
        self.has_viewport = False
        self.title_text = ""
        self._in_title = 0
        self.deck_footer: str | None = None
        self.ids: list[str] = []
        self.images: list[tuple[str, str | None]] = []
        self.slides: list[Slide] = []
        self.folios: list[str] = []

        self._stack: list[tuple[str, int]] = []          # (tag, line) for unclosed-tag check
        self._slide_depth: int | None = None
        self._cur: Slide | None = None
        self._svg_depth = 0
        self._heading_depth: int | None = None
        self._folio_depth: int | None = None
        self._folio_buf = ""
        self._in_style = 0
        self._in_script = 0

    # -- helpers
    @staticmethod
    def _classes(values: dict) -> set[str]:
        return set((values.get("class") or "").split())

    def handle_starttag(self, tag: str, attrs) -> None:
        values = {k: (v or "") for k, v in attrs}
        classes = self._classes(values)

        if tag not in VOID_TAGS:
            self._stack.append((tag, self.getpos()[0]))

        if tag == "html":
            self.html_lang = values.get("lang", "").strip()
        elif tag == "meta":
            name = values.get("name", "").lower()
            if name == "viewport":
                self.has_viewport = bool(values.get("content", "").strip())
            elif name == "deck-footer":
                self.deck_footer = htmlmod.unescape(values.get("content", "")).strip()
        elif tag == "title":
            self._in_title += 1
        elif tag == "style":
            self._in_style += 1
        elif tag == "script":
            self._in_script += 1

        if values.get("id"):
            self.ids.append(values["id"])
        if tag == "img":
            self.images.append((values.get("src", ""), values.get("alt")))

        if tag == "svg":
            self._svg_depth += 1

        if "slide" in classes and self._slide_depth is None:
            self._cur = Slide(len(self.slides) + 1, values)
            self.slides.append(self._cur)
            self._slide_depth = len(self._stack)

        if self._cur is not None:
            # first heading inside a slide is its title
            if tag in {"h1", "h2"} and not self._cur.title and self._heading_depth is None:
                self._heading_depth = len(self._stack)
            # accent budget: class-driven accent uses, outside the brand mark
            if self._svg_depth == 0 and ({"kicker", "accent"} & classes):
                self._cur.accent_hits += 1

        if ({"folio", "slide-no"} & classes) and self._folio_depth is None:
            self._folio_depth = len(self._stack)
            self._folio_buf = ""

    def handle_endtag(self, tag: str) -> None:
        if tag == "title" and self._in_title:
            self._in_title -= 1
        if tag == "style" and self._in_style:
            self._in_style -= 1
        if tag == "script" and self._in_script:
            self._in_script -= 1
        if tag == "svg" and self._svg_depth:
            self._svg_depth -= 1

        depth = len(self._stack)
        # unwind to the matching open tag
        for i in range(len(self._stack) - 1, -1, -1):
            if self._stack[i][0] == tag:
                del self._stack[i:]
                break

        if self._heading_depth is not None and depth <= self._heading_depth:
            self._heading_depth = None
        if self._folio_depth is not None and depth <= self._folio_depth:
            self.folios.append(" ".join(self._folio_buf.split()))
            self._folio_depth = None
        if self._slide_depth is not None and depth <= self._slide_depth:
            self._slide_depth = None
            self._cur = None

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_text += data
        if self._in_style or self._in_script:
            return
        if self._folio_depth is not None:
            self._folio_buf += data
        if self._cur is not None:
            self._cur.text_parts.append(data)
            if self._heading_depth is not None:
                self._cur.title += data

    @property
    def unclosed(self) -> list[tuple[str, int]]:
        return [t for t in self._stack if t[0] not in {"html", "head", "body", "p", "li"}]


# ---------------------------------------------------------------- helpers


def strip_style_script(raw: str) -> str:
    out = re.sub(r"(?is)<style.*?</style>", " ", raw)
    return re.sub(r"(?is)<script.*?</script>", " ", out)


def visible_words(raw: str) -> set[str]:
    text = re.sub(r"(?s)<[^>]+>", " ", strip_style_script(raw)).lower()
    text = htmlmod.unescape(text)
    return set(re.findall(r"[a-z][a-z0-9\-]{2,}", text))


def local_asset(deck_path: Path, source: str) -> Path | None:
    parsed = urlparse(source)
    if parsed.scheme in {"http", "https", "data", "mailto"} or source.startswith("#"):
        return None
    if parsed.scheme == "file":
        return Path(unquote(parsed.path))
    return (deck_path.parent / unquote(parsed.path)).resolve()


def parse_deck_md(path: Path) -> list[tuple[int, str]]:
    """`## S07 · <action title>` (also accepts an em dash or hyphen separator)."""
    rows: list[tuple[int, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^##\s+S(\d+)\s*[·—–-]\s*(.+?)\s*$", line)
        if m:
            rows.append((int(m.group(1)), m.group(2)))
    return rows


# ---------------------------------------------------------------- rules


def check_structure(f: Findings, raw: str, p: DeckParser) -> None:
    if not re.search(r"<!doctype\s+html", raw, re.IGNORECASE):
        f.error("S-DOCTYPE", "missing HTML5 doctype")
    if not p.html_lang:
        f.error("S-LANG", 'missing <html lang="…">')
    if not p.has_viewport:
        f.error("S-VIEWPORT", "missing viewport meta tag")
    if not p.title_text.strip():
        f.error("S-TITLE", "missing non-empty <title>")
    if len(p.slides) < 2:
        hint = (
            " — if slides are built by script, this static linter cannot see them; "
            "the deck-author contract requires static slide markup"
            if len(p.slides) == 0 and re.search(r"(?i)class(?:name)?\s*=+\s*['\"]?slide", raw)
            else ""
        )
        f.error("S-SLIDES", f'expected >=2 elements with class "slide", found {len(p.slides)}{hint}')

    dupes = sorted(i for i, n in Counter(p.ids).items() if n > 1)
    if dupes:
        f.error("S-DUP-ID", f"duplicate element ids: {', '.join(dupes)}")

    if p.unclosed:
        detail = ", ".join(f"<{t}> (line {ln})" for t, ln in p.unclosed[:6])
        f.error("S-UNCLOSED", f"unclosed tags: {detail}")


def check_footer(f: Findings, raw: str, p: DeckParser, brand: Brand | None) -> str | None:
    footer = p.deck_footer
    if not footer:
        if brand is None:
            f.notice(
                "H-FOOTER-META",
                "SKIP (no brand contract): no deck-footer meta — this deck carries NO "
                "confidentiality footer; give one via a brand contract if it needs one",
            )
            return None
        f.error(
            "H-FOOTER-META",
            'missing <meta name="deck-footer" content="…"> — the house PDF renderer '
            "hard-errors without it, by design",
        )
        return None
    if brand is None:
        f.notice(
            "H-FOOTER-CLASS",
            f"SKIP (no brand contract): footer wording {footer!r} not checked against a brand enum",
        )
    elif footer not in brand.footer_enum:
        f.error(
            "H-FOOTER-CLASS",
            f"deck-footer {footer!r} is not one of the brand's footer strings: "
            + " | ".join(repr(k) for k in brand.footer_enum),
            value=footer,
        )
        return footer

    if not re.search(r"\.slide::after\s*\{", raw):
        f.error("H-FOOTER-PRINT", "no `.slide::after` print rule — the footer will not land on every PDF page")
    else:
        block = re.search(r"\.slide::after\s*\{(.*?)\}", raw, re.S)
        content = re.search(r'content\s*:\s*"([^"]*)"', block.group(1) if block else "")
        printed = htmlmod.unescape(content.group(1)) if content else ""
        if printed.strip() != footer:
            f.error(
                "H-FOOTER-PRINT",
                f"print footer {printed!r} does not match the declared deck-footer {footer!r}",
            )
    return footer


def check_geometry(f: Findings, raw: str) -> None:
    # The winning house contract: a fixed 1280x720 board, letterboxed (scaled to fit),
    # so screen, screenshot, and PDF page share one composition. See the skill's
    # "six skeleton decisions" — this replaced the composite contender's viewport-fluid pin.
    required = {
        "H-GEOMETRY": [
            (r"width\s*:\s*1280px", "the fixed 1280px stage width"),
            (r"height\s*:\s*720px", "the fixed 720px stage height"),
            (r"transform\s*:[^;}]*scale\(", "the letterbox scale-to-fit transform on the stage"),
            (r"position\s*:\s*absolute", "absolutely-positioned slides"),
            (r"inset\s*:\s*0", "`inset: 0` on the slide box"),
            (r"@media\s+print", "@media print block"),
            (r"@page\s*\{[^}]*size\s*:\s*1280px\s+720px", "@page { size: 1280px 720px }"),
            (r"page-break-after\s*:\s*always|break-after\s*:\s*page", "one page per slide in print"),
        ]
    }
    for rule, patterns in required.items():
        for pattern, label in patterns:
            if not re.search(pattern, raw, re.IGNORECASE | re.S):
                f.error(rule, f"missing house geometry: {label}", value=label)


def check_fonts(f: Findings, raw: str, deck_path: Path, brand: Brand | None) -> None:
    if brand is None:
        f.notice("H-FONT-PIN", "SKIP (no brand contract): font-family declarations not pinned")
    else:
        for decl in re.findall(r"font-family\s*:\s*([^;}\n]+)", raw, re.IGNORECASE):
            for token in decl.split(","):
                name = token.strip().strip("'\"").lower()
                if not name or name.startswith("var("):
                    continue
                if name not in brand.font_allow:
                    f.error(
                        "H-FONT-PIN",
                        f"font-family {name!r} is outside the brand contract's pinned set "
                        f"({', '.join(sorted(brand.font_allow - GENERIC_FONTS)) or 'none declared'})",
                        value=name,
                    )

    remote = _remote_reporter(f, brand)
    for url in re.findall(r"url\(\s*['\"]?([^'\")]+)['\"]?\s*\)", raw):
        if urlparse(url).scheme in {"http", "https"}:
            remote(f"remote asset in url(): {url}", url)
            continue
        path = local_asset(deck_path, url)
        if path is not None and not path.is_file():
            f.error("H-ASSET-EXISTS", f"missing local asset: {path}")


def _remote_reporter(f: Findings, brand: Brand | None):
    """Remote assets are an error unless the brand contract explicitly allows them
    (rules.no_remote_assets = false → notice). No contract keeps the error: the
    offline requirement is structural — the render pipeline copies the file."""
    if brand is not None and not brand.no_remote:
        return lambda msg, value=None: f.notice("H-NO-REMOTE", msg, value)
    return lambda msg, value=None: f.error("H-NO-REMOTE", msg, value)


def check_offline(f: Findings, raw: str, deck_path: Path, p: DeckParser, brand: Brand | None) -> None:
    remote = _remote_reporter(f, brand)
    for attr, url in re.findall(r'\b(src|href)\s*=\s*"([^"]+)"', raw):
        if urlparse(url).scheme in {"http", "https"}:
            remote(f"remote {attr}: {url}", url)
    if re.search(r"@import\s+url\(\s*['\"]?https?:", raw, re.IGNORECASE):
        remote("remote @import in stylesheet")

    for src, alt in p.images:
        if alt is None:
            f.error("H-ALT", f"image missing alt attribute: {src}")
        path = local_asset(deck_path, src)
        if path is not None and not path.is_file():
            f.error("H-ASSET-EXISTS", f"missing image asset: {path}")


def check_slides(f: Findings, p: DeckParser, brand: Brand | None) -> None:
    accent_budget = brand.accent_budget if brand else MAX_ACCENT_PER_SLIDE
    for s in p.slides:
        tag = f"slide {s.index:02d}"
        if not s.layout:
            f.error("H-LAYOUT-POOL", f"{tag}: no data-layout declared")
        elif s.layout not in LAYOUT_POOL:
            f.error(
                "H-LAYOUT-POOL",
                f"{tag}: data-layout {s.layout!r} is outside the closed pool "
                f"({', '.join(sorted(LAYOUT_POOL))})",
                value=s.layout,
            )

        content_slide = s.layout not in CHROME_LAYOUTS
        title = " ".join(s.title.split())
        if content_slide:
            if not s.question:
                f.notice("H-QUESTION", f"{tag}: no data-question — what job does this slide do?")
            if title and len(title.split()) < 4:
                f.notice(
                    "H-ACTION-TITLE",
                    f"{tag}: title {title!r} smells like a topic label, not a takeaway",
                    value=title,
                )
            if not title:
                f.error("H-ACTION-TITLE", f"{tag}: no <h1>/<h2> title found")

        if s.accent_hits > accent_budget:
            f.notice(
                "H-ACCENT-BUDGET",
                f"{tag}: accent used {s.accent_hits}x (budget {accent_budget})",
            )

        low = s.text.lower()
        for needle in PROCESS_LEAK:
            if needle in low:
                f.error("H-PROCESS-LEAK", f"{tag}: process language rendered on a slide: {needle!r}", value=needle)
        for needle in PLACEHOLDER:
            if needle in low:
                f.error("H-PLACEHOLDER", f"{tag}: placeholder content on a slide: {needle!r}", value=needle)


def check_folios(f: Findings, p: DeckParser) -> None:
    """Accepts either form: `.folio` "N / N" pairs, or the skeleton's `.slide-no` "NN"."""
    if not p.folios:
        f.error("H-FOLIO", "no `.folio` / `.slide-no` markers found — every slide needs its number")
        return
    pairs: list[tuple[int, int | None]] = []
    for text in p.folios:
        m = re.match(r"^(\d+)\s*/\s*(\d+)$", text)
        if m:
            pairs.append((int(m.group(1)), int(m.group(2))))
            continue
        m = re.match(r"^(\d+)$", text)
        if m:
            pairs.append((int(m.group(1)), None))
            continue
        f.error("H-FOLIO", f"unparseable folio marker: {text!r}")
        return
    n = len(p.slides)
    totals = {t for _, t in pairs if t is not None}
    if [c for c, _ in pairs] != list(range(1, n + 1)) or (totals and totals != {n}):
        f.error("H-FOLIO", f"folio sequence does not match {n} slides: {pairs}")


def check_deck_md(f: Findings, raw: str, p: DeckParser, deck_md: Path) -> list[str]:
    rows = parse_deck_md(deck_md)
    if not rows:
        f.error("P-DECKMD-COUNT", f"no `## S<N> · <title>` slide rows found in {deck_md.name}")
        return []
    if len(rows) != len(p.slides):
        f.error(
            "P-DECKMD-COUNT",
            f"{deck_md.name} declares {len(rows)} slides; index.html renders {len(p.slides)}",
        )
    rendered = visible_words(raw)
    title_words: set[str] = set()
    for _, title in rows:
        title_words |= set(re.findall(r"[a-z][a-z0-9\-]{2,}", title.lower()))
    if title_words:
        covered = len(title_words & rendered) / len(title_words)
        if covered < DECKMD_COVERAGE_FLOOR:
            missing = sorted(title_words - rendered)[:10]
            f.error(
                "P-DECKMD-COVER",
                f"only {covered:.0%} of deck.md title vocabulary appears in the render "
                f"(floor {DECKMD_COVERAGE_FLOOR:.0%}); missing e.g. {missing}",
            )
    return [t for _, t in rows]


def check_pure_tones(f: Findings, raw: str, brand: Brand | None) -> None:
    black_hint = (
        " — expected: this brand's contract pins the canvas at #000000; ignore with a reason"
        if brand and brand.canvas in {"#000", "#000000"}
        else " — universal dark-theme craft prefers a softened black; keep it only as a deliberate pin"
    )
    white_hint = (
        " — expected: this brand's contract pins text_primary at #ffffff; ignore with a reason"
        if brand and brand.text_primary in {"#fff", "#ffffff"}
        else " — consider a softened white unless the brand pins it"
    )
    if re.search(r"#000\b|#000000\b", raw, re.IGNORECASE):
        f.notice("C-PURE-BLACK", f"pure #000 present{black_hint}", value="#000000")
    if re.search(r"#fff\b|#ffffff\b", raw, re.IGNORECASE):
        f.notice("C-PURE-WHITE", f"pure #fff present{white_hint}", value="#ffffff")


# ---------------------------------------------------------------- main


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("deck", type=Path, help="the deck's index.html")
    ap.add_argument("--deck-md", type=Path, default=None, help="sibling deck.md (defaults to <deck-dir>/deck.md)")
    ap.add_argument(
        "--brand",
        default=None,
        help="brand contract (brand.toml) path, or 'none' to skip brand gates; "
        "default: auto-discover (deck dir up to repo root, then the skill's shipped default)",
    )
    ap.add_argument("--config", type=Path, default=None, help="scoped-ignore config (defaults to .deckcheck.json beside the skill)")
    ap.add_argument("--quiet", action="store_true", help="suppress the ghost deck")
    args = ap.parse_args()

    deck_path = args.deck.expanduser().resolve()
    if not deck_path.is_file():
        print(f"ERROR: deck not found: {deck_path}", file=sys.stderr)
        return 2

    config: dict = {}
    candidates = [args.config] if args.config else [
        deck_path.parent / ".deckcheck.json",
        deck_path.parent.parent / ".deckcheck.json",
    ]
    config_used = None
    for candidate in candidates:
        if candidate and candidate.is_file():
            try:
                config = json.loads(candidate.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                print(f"ERROR: bad ignore config {candidate}: {exc}", file=sys.stderr)
                return 2
            config_used = candidate
            break

    try:
        brand, brand_source = resolve_brand(args.brand, deck_path)
    except RuntimeError as exc:
        if args.brand:  # an explicit contract that cannot be used is a hard error
            print(f"ERROR: {exc}", file=sys.stderr)
            return 2
        brand, brand_source = None, f"{exc} — brand gates SKIP"
    if brand is None:
        print(
            "NOTICE [BRAND] no brand contract in force"
            f" ({brand_source}); brand gates (footer wording, font pin) SKIP —"
            " structural checks still rule. A brand-neutral deck carries no"
            " confidentiality footer unless one is given."
        )

    raw = deck_path.read_text(encoding="utf-8")
    parser = DeckParser()
    parser.feed(raw)
    parser.close()

    f = Findings(config)
    check_structure(f, raw, parser)
    check_footer(f, raw, parser, brand)
    check_geometry(f, raw)
    check_fonts(f, raw, deck_path, brand)
    check_offline(f, raw, deck_path, parser, brand)
    check_slides(f, parser, brand)
    check_folios(f, parser)
    check_pure_tones(f, raw, brand)

    deck_md = args.deck_md or (deck_path.parent / "deck.md")
    if deck_md.is_file():
        check_deck_md(f, raw, parser, deck_md)
    else:
        f.notice("P-DECKMD-COUNT", f"no deck.md beside the deck ({deck_md}) — story parity not checked")

    for severity, rule, message in f.errors:
        print(f"ERROR  [{rule}] {message}", file=sys.stderr)
    for severity, rule, message in f.notices:
        print(f"NOTICE [{rule}] {message}")

    if not args.quiet:
        print("\nGHOST DECK — read these as one paragraph; they must carry the argument alone:")
        for s in parser.slides:
            title = " ".join(s.title.split()) or "(no title)"
            print(f"  {s.index:02d} [{s.layout or '?'}] {title}")
        print()

    if f.suppressed:
        print(f"SUPPRESSED: {len(f.suppressed)} finding(s) via {config_used}")

    if f.errors:
        print(
            f"FAIL: {len(f.errors)} error(s), {len(f.notices)} notice(s) "
            f"across {len(parser.slides)} slides",
            file=sys.stderr,
        )
        return 1

    if brand is not None:
        footer_class = brand.footer_enum.get(parser.deck_footer or "", "unknown")
        brand_bit = f"brand {brand.org or brand.path.name} ({brand_source}); footer class {footer_class}"
    else:
        brand_bit = "brand NONE — brand gates skipped"
    print(
        f"PASS: {len(parser.slides)} slides; {brand_bit}; "
        f"{len(parser.images)} images; {len(f.notices)} notice(s); contract present"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
