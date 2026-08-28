# The seam gate — how to wire it

`tools/seam-gate.mjs` is a **numeric** verifier for scene boundaries. It seeks a
paused timeline to one frame either side of every declared cut, measures what is
actually moving from `getBoundingClientRect`, and fails the boundary if the
measurement disagrees with what you declared. It is the only executable critique
in this skill: everything else here is a rule you obey, this one is a rule that
checks you.

It is vendored (Apache-2.0, from `heygen-com/hyperframes`; see the header of the
script and `LICENSE-hyperframes-Apache-2.0.txt` beside it). Zero npm
dependencies — node ≥ 22 and a local Chrome, which it finds itself in
`~/.cache/puppeteer` or `/Applications`. `CHROME_PATH` overrides.

## What it enforces, per seam

| Row | Rule |
|---|---|
| `ledger` | exit and entry vectors agree **in the plan** (same axis, same sign) |
| `exit-moving` / `entry-moving` | no settled exits, no from-rest entries — the boundary is crossed mid-motion |
| `exit-direction` / `entry-direction` | the measured sign matches what the ledger declared |
| `speed-match` (WARN) | entry velocity ≈ exit velocity, within 3× |
| `zero-overlap` | **one side visible per frame, never both** |
| `z-sign-scan` | on a Z seam, the incoming scene's own entrances do not scale against the seam's sign |
| `carrier-*` | on a match-cut/morph, the carrier's rect is continuous across the cut (12 px centre / 5 % size) |

It checks nothing about content. A film can pass every seam and still be a
slideshow — which is why the render check exists beside it.

## Running it standalone (the wiring that is not in the usage line)

The script was written to drive a HyperFrames preview server. Two flags make it
run against a plain self-contained `explainer.html` instead, and the combination
is discoverable only by reading `ensureServer()`:

```bash
node skills/staging/tools/seam-gate.mjs verify \
  --ledger <film>/seams.json \
  --url http://127.0.0.1:1 \
  --comp-url "file://$PWD/<film>/explainer.html"
```

- `--url` is **required but unused**. Supplying any value skips the server-spawn
  branch entirely. `http://127.0.0.1:1` is a deliberately dead address: if the
  wiring ever regressed to actually fetching it, the run would fail loudly
  rather than quietly reach the network.
- `--comp-url` is what is actually navigated to. A `file://` URL is fine, and
  nothing is fetched.
- **Never pass `--project`.** That branch spawns `npx --yes hyperframes preview`,
  which installs from the network.
- Exit code 0 = gate passed. `--json` for machine output. `--fps 30` default.

## The shim the page must expose

The harness hard-requires three globals before it will run — `window.__player`
with `pause()` / `seek(t)`, plus `window.__playerReady` and
`window.__renderReady`. A house `explainer.html` has none of them. Bridge the
renderer's master timeline in ~15 lines at the end of the boot script:

```js
(function bridge() {
  var ex = window.__explainer;                 // whatever your runtime exposes
  if (!ex || !ex.master) { setTimeout(bridge, 40); return; }
  window.__player = {
    pause: function () { ex.master.pause(); },
    play:  function () { ex.master.play(); },
    seek:  function (t) { ex.master.pause(); ex.master.seek(t); },
    duration: function () { return ex.total; },
  };
  window.__playerReady = true;
  window.__renderReady = true;
})();
```

Purely additive — the recorder never touches it — and it belongs **in the
shipped file**, so the gate is re-runnable by anyone against the delivered
artifact rather than against a private build.

## `crossfade: 0` is not a taste

`zero-overlap` fails any boundary where both scenes are on screen in the same
frame. A 0.2 s crossfade puts both sides up for six frames at every cut, and the
gate reports a dissolve. So a film that intends to pass this gate is cut, not
dissolved — and each side of every cut must carry its own motion, because a hard
cut between two settled frames has no carrier at all.

This is load-bearing, and it is the one place the gate improves the artifact
rather than merely constraining it: it forces you to design the boundary.

## The declared-seam ledger

`seams.json` beside the film. One row per boundary; write it **before** the
master timeline, not after — the ledger is what forces the seam design.

```json
{
  "fps": 30,
  "seams": [
    { "id": "concede->seams", "cut": 19.6, "technique": "cut-the-curve LEFT",
      "exit":  { "selector": "#c-concede", "axis": "x", "dir": -1 },
      "entry": { "selector": "#c-seams",   "axis": "x", "dir": -1 } },

    { "id": "fork->anatomy", "cut": 141.2, "technique": "zoom-through (Z+) — register handoff",
      "exit":  { "selector": "#c-fork",    "axis": "z", "dir": 1 },
      "entry": { "selector": "#c-anatomy", "axis": "z", "dir": 1, "scanRoot": "#c-anatomy" } }
  ]
}
```

- `cut` — seconds on the master clock: the cumulative sum of the durations
  **the page is actually running**. If those are estimates, the ledger is in
  estimate time and says so.
- `axis` / `dir` — `x −1` leftward, `y −1` upward, `z +1` push (growing),
  `z −1` pull (shrinking).
- `selector` — the element that *carries* the seam motion (a per-scene
  `.carrier` wrapper is the easy answer), not the scene section, whose opacity
  the runtime owns.
- `type: "match-cut"` / `"morph"` swaps the vector checks for `carrier`
  continuity; motion may then start at the boundary.

## When to opt a boundary in

Default: **all of them.** A film with 20 boundaries and 4 declared seams has
16 unaudited cuts, and the gate's whole value is that it is exhaustive.

Opt a boundary *out* only when it is genuinely not a cut — an intra-scene step,
or a boundary where the piece deliberately holds a single frame across the join
— and record the reason in the ledger's `_doc`. Reserve `z` rows for boundaries
the **narration** marks as chapter changes (a register handoff, an arrival);
2–3 per film. Spending a reserved vector on an ordinary cut is how a film ends
up with a house style of "everything is dramatic", which is the same failure as
two bold moments.

**Editing note.** Any change to a scene's first or last ~1 s — or to any
duration, which moves every later cut — invalidates that boundary's audit.
Re-derive the cut times and re-run. Say so in the ledger's own `_doc` field.
