"""Shared context for the explainer-video pipeline.

Resolves a voice profile from voices/registry.yaml and parses a product
`SCRIPT.md` (which lives in the product's deck repo, passed in as a path) into
an ordered list of scenes. Every pipeline step (gen_tts, assemble_audio,
gen_subs, encode) operates against a single RunContext so the tool stays a thin
wrapper: product content is INPUT, never baked into this repo.
"""
from __future__ import annotations

import re
from datetime import datetime, timezone
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

try:
    import yaml
except ImportError as exc:  # pragma: no cover - surfaced to the user
    raise SystemExit(
        "PyYAML is required. Activate the tool venv and `pip install -r requirements.txt`."
    ) from exc

TOOL_ROOT = Path(__file__).resolve().parent.parent
REGISTRY = TOOL_ROOT / "voices" / "registry.yaml"


@dataclass
class Scene:
    id: str
    narration: str
    subtitle: str  # falls back to narration when the script has no subtitle column


@dataclass
class Profile:
    name: str
    engine: str
    model: str
    voice: Optional[str] = None
    ref_audio: Optional[Path] = None
    ref_text: Optional[str] = None
    params: dict = field(default_factory=dict)

    @property
    def has_reference(self) -> bool:
        return self.ref_audio is not None


def load_profile(name: str, registry: Path = REGISTRY) -> Profile:
    data = yaml.safe_load(registry.read_text())
    profiles = (data or {}).get("profiles", {})
    if name not in profiles:
        known = ", ".join(sorted(profiles)) or "(none)"
        raise SystemExit(f"unknown voice profile '{name}'. Known: {known}")
    p = profiles[name] or {}
    profile_dir = registry.parent / name

    ref_audio = None
    if p.get("ref_audio"):
        ref_audio = (profile_dir / p["ref_audio"]).resolve()
        if not ref_audio.exists():
            raise SystemExit(f"profile '{name}': ref_audio not found: {ref_audio}")

    ref_text = None
    if p.get("ref_text_file"):
        ref_text_path = (profile_dir / p["ref_text_file"]).resolve()
        if not ref_text_path.exists():
            raise SystemExit(f"profile '{name}': ref_text_file not found: {ref_text_path}")
        ref_text = ref_text_path.read_text().strip()

    engine = p.get("engine")
    if not engine:
        raise SystemExit(f"profile '{name}': missing 'engine'")
    if engine == "qwen" and ref_audio is None:
        raise SystemExit(
            f"profile '{name}' is engine=qwen but has no ref_audio "
            "(it is a scaffold — add a reference clip, see voices/<profile>/README.md)."
        )

    return Profile(
        name=name,
        engine=engine,
        model=p.get("model", ""),
        voice=p.get("voice"),
        ref_audio=ref_audio,
        ref_text=ref_text,
        params=p.get("params") or {},
    )


ORPHEUS_US_MODEL = "mlx-community/orpheus-3b-0.1-ft-bf16"
# Orpheus-3b built-in voice presets (US accents). In-repo corroboration:
# pipeline/alternates/gen_orpheus.py renders with voice "leo".
ORPHEUS_US_VOICES = ("tara", "leah", "jess", "leo", "dan", "mia", "zac", "zoe")


def us_orpheus_profile(voice: str) -> Profile:
    """Synthesize a US-accent Orpheus profile in memory: built-in voice preset,
    no registry entry and no reference clip. Backs the CLI's --us-voice flag.
    max_tokens 4096 mirrors the qwen profiles — the mlx_audio default (1200)
    silently truncates long scenes."""
    raw = voice
    voice = voice.strip().lower()
    if voice not in ORPHEUS_US_VOICES:
        known = ", ".join(ORPHEUS_US_VOICES)
        raise SystemExit(f"unknown Orpheus voice '{raw}'. Known: {known}")
    return Profile(
        name=f"us-orpheus-{voice}",
        engine="orpheus",
        model=ORPHEUS_US_MODEL,
        voice=voice,
        params={"max_tokens": 4096},
    )


# --- SCRIPT.md parsing -------------------------------------------------------
#
# Expected format (lives in the product deck repo's video/ dir): a Markdown
# table whose header row contains columns named (case-insensitive, substring
# match) "id", "narration", and optionally "subtitle". One row per scene, in
# order. Example:
#
#   | # | id    | narration                        | subtitle              |
#   |---|-------|----------------------------------|-----------------------|
#   | 1 | title | "Every DeFi platform ..."        | No liquidations.      |
#
# Surrounding quotes and **bold** markers are stripped. If no subtitle column
# is present, the narration text is reused as the subtitle.

_BOLD = re.compile(r"\*\*(.+?)\*\*")


def _clean(cell: str) -> str:
    cell = cell.strip()
    cell = _BOLD.sub(r"\1", cell)
    if len(cell) >= 2 and cell[0] in "\"'" and cell[-1] == cell[0]:
        cell = cell[1:-1]
    return cell.strip()


def _split_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def parse_script(path: Path) -> list[Scene]:
    lines = [ln for ln in Path(path).read_text().splitlines()]
    header = None
    col = {}
    rows: list[list[str]] = []
    for ln in lines:
        if "|" not in ln:
            if header is not None and rows:
                break  # table ended
            continue
        cells = _split_row(ln)
        # separator row like |---|---|
        if all(set(c) <= set("-: ") and c for c in cells):
            continue
        if header is None:
            header = [c.lower() for c in cells]
            for i, h in enumerate(header):
                if "id" in h and "id" not in col:
                    col["id"] = i
                if "narration" in h:
                    col["narration"] = i
                if "subtitle" in h:
                    col["subtitle"] = i
            if "id" not in col or "narration" not in col:
                header = None  # not the scenes table; keep scanning
                col = {}
            continue
        rows.append(cells)

    if header is None:
        raise SystemExit(
            f"no scenes table found in {path}. Expected a Markdown table with "
            "'id' and 'narration' columns (see tools/explainer-video/README.md)."
        )

    scenes: list[Scene] = []
    for cells in rows:
        try:
            sid = _clean(cells[col["id"]])
            narration = _clean(cells[col["narration"]])
        except IndexError:
            continue
        if not sid or not narration:
            continue
        subtitle = narration
        if "subtitle" in col and col["subtitle"] < len(cells):
            sub = _clean(cells[col["subtitle"]])
            if sub:
                subtitle = sub
        scenes.append(Scene(id=sid, narration=narration, subtitle=subtitle))

    if not scenes:
        raise SystemExit(f"scenes table in {path} parsed to zero rows.")
    return scenes


# --- `## Description` parsing ----------------------------------------------
#
# Optional authored section in SCRIPT.md: an H2 named `Description` whose
# verbatim body (everything until the next `## ` heading or EOF) is the
# YouTube-ready description for the rendered video. Authored prose — never
# generated from the scenes table. Scripts without the section keep working
# unchanged: parse_description simply returns ''.

_DESCRIPTION_H2 = re.compile(r"^##\s+Description\s*$", re.IGNORECASE)
_ANY_H2 = re.compile(r"^##\s")


def parse_description(path: Path) -> str:
    """Verbatim body of the script's optional `## Description` section.

    The body runs from the line after the heading to the next `## ` H2 (or
    EOF), with leading/trailing blank lines stripped and everything in
    between kept verbatim — interior blank lines, links, `### ` subheadings
    (which do not match `## ` followed by a space) all survive. Returns ''
    when the script has no such section (or its body is empty); the first
    matching section wins.
    """
    body: list[str] = []
    in_section = False
    for ln in Path(path).read_text().splitlines():
        if in_section:
            if _ANY_H2.match(ln):
                break
            body.append(ln)
        elif _DESCRIPTION_H2.match(ln):
            in_section = True
    while body and not body[0].strip():
        body.pop(0)
    while body and not body[-1].strip():
        body.pop()
    return "\n".join(body)


_TITLE_LINE = re.compile(r"^#\s+(.+)")
_TITLE_CLEAN = re.compile(r"[^\w\s-]")


def _parse_title_raw(script: Path) -> str:
    """Extract the raw H1 title text (unslugified) for MP4 metadata."""
    for line in Path(script).read_text().splitlines():
        m = _TITLE_LINE.match(line)
        if m:
            return m.group(1).strip()
    return ""


def _slugify(raw: str, cap: int = 100) -> str:
    """Reduce arbitrary text to one lowercase filename component.

    `_TITLE_CLEAN` drops every character outside `[\\w\\s-]`, which includes
    `/` and `.` — so a slug can never introduce a second path component or a
    `..` traversal, whatever the input. Returns '' if nothing usable survives.
    """
    # Remove quotes, punctuation, and special characters; collapse
    # whitespace and join with hyphens.
    slug = _TITLE_CLEAN.sub("", raw).strip().lower()
    slug = re.sub(r"\s+", "-", slug)
    # Collapse runs of hyphens from removed multi-char punctuation like `--`
    slug = re.sub(r"-{2,}", "-", slug)
    slug = slug.strip("-")
    # Cap so the filename stays well under the 255-byte component limit — for
    # the delivered `<name>.mp4` and for the internal `.work-<name>-<profile>`
    # dir, which still carries the `-<profile>` suffix (N1); re-strip in case
    # the cut landed mid-word on a hyphen.
    return slug[:cap].strip("-")


def parse_title(script: Path) -> str:
    """Slugified first-H1 title of the script — the default output basename.

    Reads the same H1 as `_parse_title_raw`, so the output filename and the
    embedded MP4 title always describe the same heading. Falls back to the deck
    directory name, then the script stem, when there is no H1 or the title
    slugifies to nothing (e.g. a title of only punctuation: '!!!'). The result
    is never empty.
    """
    script = Path(script)
    slug = _slugify(_parse_title_raw(script))
    return slug or script.parent.parent.name or script.stem


def sanitize_name(name: str) -> str:
    """Validate an operator-supplied ``--name`` as a single path component.

    ``--name`` is used verbatim (it is deliberately not slugified, so callers
    keep their own casing), which makes it the one route by which a separator
    or a ``..`` can reach ``RunContext.work`` — the directory ``run()`` deletes
    recursively before each run. ``--name 'x/../../renders'`` resolves the work
    dir outside ``--out`` entirely; rejecting it here keeps that impossible.
    """
    cleaned = name.strip()
    if not cleaned:
        raise SystemExit("--name must not be empty")
    if cleaned in (".", "..") or cleaned != Path(cleaned).name:
        raise SystemExit(
            f"--name must be a single filename component (no '/' or '..'), got {name!r}"
        )
    return cleaned


@dataclass
class RunContext:
    script: Path
    slides: Path
    profile: Profile
    out_dir: Path
    name: str
    scenes: list[Scene]
    work: Path
    title_raw: str = ""       # raw H1 title from SCRIPT.md (for MP4 metadata)
    url: str = ""             # product URL (for MP4 metadata)
    generated_at: str = ""    # ISO 8601 generation timestamp (for MP4 metadata)
    description: str = ""     # verbatim `## Description` body from SCRIPT.md ('' = none)

    # The DELIVERED artifacts are named by the clean base (`--name`/slug) only —
    # the voice/profile is deliberately NOT in the filename (an operator asked
    # for `reading-a-verification-record.mp4`, not `…-australian-assay.mp4`).
    # The profile still disambiguates the INTERNAL `.work-*` dir (see
    # `build_context`), so concurrent renders of the same article in different
    # voices don't corrupt each other's intermediates. Two voices rendered into
    # the SAME `--out`, however, resolve to the same delivered name and so
    # clobber (last writer wins) — the same last-writer-wins behaviour a re-run
    # of one profile already has (`ffmpeg -y`, and the .vtt/.description.txt
    # publish overwrites). Render distinct voices into distinct `--out` dirs.
    @property
    def out_mp4(self) -> Path:
        return self.out_dir / f"{self.name}.mp4"

    @property
    def out_vtt(self) -> Path:
        # same stem as out_mp4 — external subtitles for web <track> elements
        return self.out_dir / f"{self.name}.vtt"

    @property
    def out_description(self) -> Path:
        # same stem as out_mp4 — the cut-and-paste YouTube description
        return self.out_dir / f"{self.name}.description.txt"

    @property
    def narration_wav(self) -> Path:
        return self.work / "narration_full.wav"

    @property
    def slides_rendered(self) -> Path:
        return self.work / "slides.html"

    @property
    def rec_dir(self) -> Path:
        return self.work / "rec"

    @property
    def subtitles_srt(self) -> Path:
        return self.work / "subtitles.srt"

    @property
    def subtitles_vtt(self) -> Path:
        return self.work / "subtitles.vtt"

    def scene_wav(self, scene: Scene) -> Path:
        return self.work / f"{scene.id}.wav"

    def assert_safe_work_dir(self) -> Path:
        """Guard the recursive delete in `run()`.

        `run()` calls `shutil.rmtree(ctx.work)`, so `work` must provably be our
        own scratch directory and nothing else. It is only ever safe when it is
        a direct child of `--out` named `.work-*`. `sanitize_name` should make
        that unconditional; this re-checks it at the point of deletion so the
        guarantee does not rest on a validator somewhere upstream continuing to
        hold. Returns the resolved path.
        """
        work = self.work.resolve()
        out_dir = self.out_dir.resolve()
        if work.parent != out_dir or not work.name.startswith(".work-"):
            raise SystemExit(
                f"refusing to clean unexpected work dir: {self.work} "
                f"(resolves to {work}; expected a '.work-*' child of {out_dir})"
            )
        return work


def build_context(script: Path, slides: Path, profile_name: Optional[str],
                  out_dir: Path, name: Optional[str], url: str = "",
                  profile_override: Optional[Profile] = None) -> RunContext:
    script = Path(script).resolve()
    slides = Path(slides).resolve()
    for label, p in (("script", script), ("slides", slides)):
        if not p.exists():
            raise SystemExit(f"--{label} not found: {p}")
    profile = profile_override if profile_override is not None else load_profile(profile_name)
    scenes = parse_script(script)
    # default name = the script's H1 title, slugified;
    # e.g. "# Assay explainer — the assay office" -> "assay-explainer"
    name = sanitize_name(name) if name else parse_title(script)
    out_dir = Path(out_dir).resolve()
    work = out_dir / f".work-{name}-{profile.name}"
    title_raw = _parse_title_raw(script)
    description = parse_description(script)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return RunContext(
        script=script, slides=slides, profile=profile,
        out_dir=out_dir, name=name, scenes=scenes, work=work,
        title_raw=title_raw, url=url, generated_at=generated_at,
        description=description,
    )
