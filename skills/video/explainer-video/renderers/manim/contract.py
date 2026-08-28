"""The pipeline↔renderer timing contract — pure stdlib, no Manim.

This is the half of the adapter that has to be *right*: the arithmetic that maps
the pipeline's measured narration onto video frames. It deliberately imports
nothing beyond the standard library so it can be unit-tested (and CI-gated)
on a machine with no Manim, no cairo/pango and no ffmpeg — see
`tests/test_contract.py`. `pipeline_contract.py` adds the Manim-dependent
`BrandScene` on top and re-exports everything here.

The audio timeline
------------------
`pipeline/assemble_audio.py` concatenates::

    LEAD_S silence | clip_0 | GAP_S | clip_1 | GAP_S | ... | clip_n | TAIL_S

and prints, on stdout::

    SCENE_DURATIONS [4.212, 10.017, 3.981]

where ``SCENE_DURATIONS[i] = clip_i + (TAIL_S if last else GAP_S)``. The
**lead-in is not part of any entry**, so::

    total narration = LEAD_S + sum(SCENE_DURATIONS)

`pipeline/gen_subs.py` agrees: its first cue starts at ``cum = LEAD_S``. Scene
*i*'s narration therefore begins at ``LEAD_S + sum(durations[:i])``, and
`pipeline/encode.sh` muxes video and audio at a common t=0 with no offset.

The rendered video must consequently be ``LEAD_S + sum(durations)`` long, with
the first ``LEAD_S`` spent holding before scene 0's storyboard starts. A
renderer that emits ``sum(durations)`` puts every picture 0.35s ahead of its
narration and its subtitle, for the whole video — which is why the lead-in is
modelled here rather than left to each storyboard to remember.

Frame boundaries
----------------
Scene *i* owns frames ``round((lead + sum(d[:i])) * fps)`` …
``round((lead + sum(d[:i+1])) * fps)``. Deriving each boundary from the
*cumulative* timeline (rather than rounding each duration independently) means
every scene absorbs the previous scenes' rounding residue, so the concatenated
video's total error against the narration stays under half a frame however many
scenes there are.

Accepted JSON shapes
--------------------
::

    [4.212, 10.017, 3.981]

    {"scene_durations": [4.212, 10.017, 3.981],
     "scenes": ["TitleCard", "SplitMaths", "ClosingCard"],
     "lead_in": 0.35,
     "fps": 30}

When the object form carries a ``scenes`` list, a scene resolves by *name* first
and falls back to ``scene_index`` — so a reordered storyboard fails loudly
(unknown name) instead of silently rendering to the wrong narration slot.
``lead_in`` (or ``leadIn``) overrides the default; an explicit ``0`` is honoured.

Where the durations come from, in priority order:
  1. ``MEDICI_SCENE_DURATIONS`` env var — a path to a JSON file (what
     `render.sh` sets).
  2. ``scene-durations.json`` in the current working directory.
  3. ``scene-durations.json`` next to this module.
  4. Nothing found -> each scene's ``fallback_duration``, and **no lead-in**:
     that is the documented standalone-development path
     (``manim render scenes/demo.py TitleCard``), which is never muxed against
     a pipeline narration.

This module writes the JSON too::

    python contract.py --from-log assemble.log --out scene-durations.json
    python contract.py --durations 4.2,10.0,4.0 --out scene-durations.json

so the pipeline's stdout can be turned into the contract file without editing
anything under `pipeline/` — and without a Manim install.
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import sys
from pathlib import Path

DURATIONS_ENV = "MEDICI_SCENE_DURATIONS"
DURATIONS_FILENAME = "scene-durations.json"

#: Silence the pipeline prepends before scene 0's narration. Must match
#: ``LEAD_S`` in `pipeline/assemble_audio.py` and `pipeline/gen_subs.py`.
LEAD_IN_DEFAULT = 0.35

_LOG_RE = re.compile(r"^SCENE_DURATIONS\s+(\[[^\]]*\])\s*$", re.MULTILINE)


class Contract:
    """A parsed scene-durations file."""

    __slots__ = ("durations", "scenes", "lead_in", "fps", "source")

    def __init__(self, durations: list[float], scenes: list[str] | None,
                 lead_in: float, fps: float | None, source: Path | None) -> None:
        self.durations = durations
        self.scenes = scenes
        self.lead_in = lead_in
        self.fps = fps
        self.source = source

    def __bool__(self) -> bool:
        return bool(self.durations)


EMPTY = Contract([], None, 0.0, None, None)


# --- reading -----------------------------------------------------------------


def _candidate_paths(explicit: str | Path | None) -> list[Path]:
    if explicit:
        return [Path(explicit)]
    paths = []
    env = os.environ.get(DURATIONS_ENV)
    if env:
        paths.append(Path(env))
    paths.append(Path.cwd() / DURATIONS_FILENAME)
    paths.append(Path(__file__).resolve().parent / DURATIONS_FILENAME)
    return paths


def _positive_floats(values, source: Path) -> list[float]:
    out = []
    for i, v in enumerate(values):
        try:
            f = float(v)
        except (TypeError, ValueError):
            raise SystemExit(f"{source}: scene_durations[{i}] is not a number: {v!r}") from None
        if not (f > 0) or f != f or f in (float("inf"), float("-inf")):
            raise SystemExit(f"{source}: scene_durations[{i}] must be a positive finite number, got {v!r}")
        out.append(f)
    return out


def load_contract(path: str | Path | None = None) -> Contract:
    """Read the first contract file that exists. Returns `EMPTY` if none do."""
    for candidate in _candidate_paths(path):
        if not candidate.is_file():
            continue
        try:
            raw = json.loads(candidate.read_text())
        except json.JSONDecodeError as exc:
            raise SystemExit(f"{candidate}: not valid JSON — {exc}") from None

        if isinstance(raw, list):
            return Contract(_positive_floats(raw, candidate), None, LEAD_IN_DEFAULT, None, candidate)

        if isinstance(raw, dict):
            durations = raw.get("scene_durations")
            if durations is None:
                durations = raw.get("SCENE_DURATIONS")
            if durations is None:
                raise SystemExit(
                    f"{candidate}: object form needs a 'scene_durations' key holding an "
                    "array of seconds (this renderer's shape is NOT the Motion Canvas "
                    "adapter's — see README §Scene-duration contract)"
                )
            if not isinstance(durations, list):
                raise SystemExit(f"{candidate}: 'scene_durations' must be an array, got {type(durations).__name__}")

            names = raw.get("scenes")
            if names is not None:
                if not isinstance(names, list) or not all(isinstance(n, str) for n in names):
                    raise SystemExit(
                        f"{candidate}: 'scenes' must be an array of Manim Scene class NAMES "
                        "(strings). An array of objects is the Motion Canvas adapter's shape."
                    )
                if len(names) != len(durations):
                    raise SystemExit(
                        f"{candidate}: 'scenes' has {len(names)} names but 'scene_durations' "
                        f"has {len(durations)} entries"
                    )

            lead = raw.get("lead_in", raw.get("leadIn", LEAD_IN_DEFAULT))
            try:
                lead = float(lead)
            except (TypeError, ValueError):
                raise SystemExit(f"{candidate}: 'lead_in' is not a number: {lead!r}") from None
            if lead < 0:
                raise SystemExit(f"{candidate}: 'lead_in' must be >= 0, got {lead}")

            fps = raw.get("fps")
            return Contract(
                _positive_floats(durations, candidate),
                (list(names) if names else None),
                lead,
                float(fps) if fps else None,
                candidate,
            )

        raise SystemExit(f"{candidate}: expected a JSON array or object")
    return EMPTY


def resolve_index(scene_name: str, scene_index: int,
                  contract: Contract | None = None) -> tuple[Contract, int, bool]:
    """Locate a scene in the contract. Returns (contract, index, resolved_by_name)."""
    c = load_contract() if contract is None else contract
    if not c:
        return EMPTY, -1, False

    if c.scenes:
        if scene_name not in c.scenes:
            raise SystemExit(
                f"{c.source}: scene {scene_name!r} not in 'scenes' {c.scenes}. "
                "Either add it or drop the 'scenes' key to resolve by index."
            )
        idx = c.scenes.index(scene_name)
    else:
        idx = scene_index

    if idx < 0 or idx >= len(c.durations):
        raise SystemExit(
            f"{c.source}: scene {scene_name!r} resolves to index {idx} but only "
            f"{len(c.durations)} durations were supplied — the storyboard and the "
            "SCRIPT.md scene list have diverged."
        )
    return c, idx, bool(c.scenes)


def _boundary(cumulative: float, lead_in: float, fps: float) -> int:
    """Frame index at which `cumulative` seconds of narration have elapsed."""
    return round((lead_in + cumulative) * fps)


def resolve_budget(scene_name: str, scene_index: int, fallback: float, fps: float,
                   contract: Contract | None = None) -> tuple[float, float, str]:
    """Resolve one scene's frame budget.

    Returns ``(storyboard_seconds, lead_in_seconds, provenance)``.

    ``storyboard_seconds`` is the narration window the scene's beats must fill
    (and the scaling numerator). ``lead_in_seconds`` is the extra hold the FIRST
    scene renders *before* its storyboard, covering the pipeline's lead silence;
    it is 0 for every other scene and whenever no contract file was found. The
    clip a scene must emit is therefore ``lead_in + storyboard`` seconds long.
    """
    c, idx, by_name = resolve_index(scene_name, scene_index, contract)
    if idx < 0:
        return fallback, 0.0, "fallback (no durations file)"

    start = _boundary(sum(c.durations[:idx]), c.lead_in, fps)
    end = _boundary(sum(c.durations[: idx + 1]), c.lead_in, fps)
    budget = (end - start) / fps
    lead_in = start / fps if idx == 0 else 0.0
    how = "by name" if by_name else "by index"
    lead_note = f", lead-in {lead_in:.3f}s" if lead_in else ""
    return budget, lead_in, f"{c.source.name}[{idx}] {how}, frames {start}–{end}{lead_note}"


def total_length(fps: float, contract: Contract | None = None) -> float:
    """Full video length the contract demands, frame-quantised: lead + all scenes.

    `render.sh` asserts the concatenated video against this. A renderer that
    silently drops the lead-in, truncates a scene, or loses a clip in the concat
    produces a shorter file than this and must fail rather than hand a
    desynchronised video to `encode.sh`.
    """
    c = load_contract() if contract is None else contract
    if not c:
        raise SystemExit("no scene-durations file found — nothing to check the render against")
    return _boundary(sum(c.durations), c.lead_in, fps) / fps


# --- writing -----------------------------------------------------------------


def durations_from_log(text: str) -> list[float]:
    """Pull the last `SCENE_DURATIONS [...]` line out of pipeline stdout."""
    matches = _LOG_RE.findall(text)
    if not matches:
        raise SystemExit(
            "no 'SCENE_DURATIONS [...]' line found. Capture the output of the "
            "pipeline's assemble step, e.g. `explainer-video ... 2>&1 | tee assemble.log`."
        )
    values = ast.literal_eval(matches[-1])
    if not values:
        raise SystemExit("the 'SCENE_DURATIONS [...]' line parsed to zero entries")
    return [float(x) for x in values]


def write_contract(durations: list[float], out: Path, scenes: list[str] | None = None,
                   fps: int | None = None, lead_in: float = LEAD_IN_DEFAULT) -> None:
    payload: dict = {"scene_durations": [round(d, 3) for d in durations]}
    if scenes:
        payload["scenes"] = scenes
    # Always written, never inferred: the lead-in is the field a reader is most
    # likely to assume away, and the value is load-bearing for A/V sync.
    payload["lead_in"] = round(lead_in, 3)
    if fps:
        payload["fps"] = fps
    out.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"WROTE {out}: {payload['scene_durations']} lead_in={payload['lead_in']}")


# --- CLI ---------------------------------------------------------------------


def build_parser(prog: str = "contract.py") -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog=prog,
        description="Write the scene-durations contract file the Manim renderer reads, "
                    "or report the video length it demands.",
    )
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--from-log", metavar="FILE",
                     help="file containing the pipeline's 'SCENE_DURATIONS [...]' line ('-' for stdin)")
    src.add_argument("--durations", metavar="A,B,C", help="comma-separated seconds")
    src.add_argument("--total-length", action="store_true",
                     help="print the video length (seconds) the resolved contract demands, "
                          "including the lead-in, frame-quantised to --fps; used by render.sh")
    src.add_argument("--scene-order", metavar="MODULE",
                     help="print a scenes module's SCENE_ORDER, one per line, and exit "
                          "(requires Manim — run via pipeline_contract.py)")
    ap.add_argument("--scenes", metavar="A,B,C",
                    help="comma-separated Manim Scene class names, in order (enables name resolution)")
    ap.add_argument("--fps", type=int, default=None)
    ap.add_argument("--lead-in", type=float, default=LEAD_IN_DEFAULT,
                    help=f"pipeline lead silence before scene 0 (default {LEAD_IN_DEFAULT}, "
                         "matching assemble_audio.py LEAD_S)")
    ap.add_argument("--out", default=DURATIONS_FILENAME)
    return ap


def run(args: argparse.Namespace) -> None:
    """Handle every mode that does not need Manim. Returns normally when done."""
    if args.total_length:
        if not args.fps:
            raise SystemExit("--total-length needs --fps")
        print(f"{total_length(float(args.fps)):.6f}")
        return

    if args.from_log:
        text = sys.stdin.read() if args.from_log == "-" else Path(args.from_log).read_text()
        durations = durations_from_log(text)
    else:
        durations = [float(x) for x in args.durations.split(",") if x.strip()]
        if not durations:
            raise SystemExit("--durations parsed to zero entries")

    scenes = [s.strip() for s in args.scenes.split(",")] if args.scenes else None
    if scenes and len(scenes) != len(durations):
        raise SystemExit(f"--scenes has {len(scenes)} names but {len(durations)} durations were given")
    if args.lead_in < 0:
        raise SystemExit("--lead-in must be >= 0")
    write_contract(durations, Path(args.out), scenes, args.fps, args.lead_in)


def main() -> None:
    args = build_parser().parse_args()
    if args.scene_order:
        raise SystemExit(
            "--scene-order needs Manim to import the storyboard: run it through "
            "pipeline_contract.py (the adapter venv), not contract.py"
        )
    run(args)


if __name__ == "__main__":
    main()
