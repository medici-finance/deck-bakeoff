# fetch-and-render

The **orchestration** half of the explainer-video tool. Where
[`explainer-video`](./explainer-video) is the render *engine* — it takes a
`SCRIPT.md` + `explainer.html` already on disk — `fetch-and-render` does the step
before it: it reads one or more **PRs**, pulls every explainer **bundle** out of
them, and fires the engine once per bundle, forwarding your extra render args
verbatim.

It is read-only against the PRs (`gh pr view` / `gh api .../contents`) and never
uploads anything: like a person running `explainer-video` by hand, it only
orchestrates the render. Whatever the engine writes into `--out` (the mp4, its
`.vtt`, the `.description.txt`) is all that happens.

## A "bundle"

Any directory in the PR that holds **both** a `SCRIPT.md` and an
`explainer.html` — the shape an assay-site blog article ships in:

```
public/blog/<category>/<slug>/
├── SCRIPT.md        # the narration (the engine's scene table)
├── explainer.html   # the self-contained branded slides
├── index.html       # <script type="application/json" id="assay-article"> … </script>
├── cover.png  thumb.png  teaser.html
```

A single PR may carry **several** bundles, and you can pass **several** PRs; every
bundle found across all of them is rendered.

Staged to disk per bundle: `SCRIPT.md` and `explainer.html` (always), plus
`index.html` and `cover.png` **when the bundle carries them** (both optional).
`cover.png` is binary and is copied byte-for-byte.

### name + URL

Per bundle, from the sibling `index.html`'s `assay-article` metadata block:

- **name** (→ engine `--name`, the output basename): the block's `slug`, else its
  slugified `title`, else the bundle directory name.
- **URL** (→ engine `--url`, embedded as mp4 metadata): the first url-ish field in
  the block (`url` / `canonical` / `permalink` / `link` / `page`), else — since
  the current block carries none — the **PR URL**.

## Usage

```
fetch-and-render <PR> [<PR> ...] [--repo OWNER/REPO] [--workdir DIR] [--dry-run]
                 [-- <extra render args forwarded verbatim to explainer-video>]
```

- `<PR>` — a PR **number** (resolved against `--repo`) or a full PR **URL**
  (`https://github.com/OWNER/REPO/pull/N`, self-describing — it can name a
  different repo than `--repo`, so you can mix repos in one invocation).
- `--repo OWNER/REPO` — repo for bare PR numbers. Bundles normally live in
  `medici-finance/assay-site`.
- `--workdir DIR` — where fetched bundles are staged (default `./out/.fetched`).
- `--dry-run` — still fetches and discovers (a real self-check of the fetch), but
  prints the render command for each bundle **instead of** running the engine.
- `--` — **everything after a literal `--` is forwarded verbatim** to
  `explainer-video`. This is where the voice selection goes — the engine
  *requires* `--profile` **or** `--us-voice` — along with any of its other flags
  (`--out`, `--dry-run`, a `--url`/`--name` override, …).

### How the pass-through works

For each bundle the composed command is:

```
explainer-video --script <staged>/SCRIPT.md --slides <staged>/explainer.html \
                --name <bundle-name> --url <bundle-url> \
                --out ~/Downloads/videos  <your forwarded args…>
```

Our `--name`/`--url`/`--out` defaults come **first** and your forwarded args come
**after**, so — because the engine's argparse takes the *last* value of a
repeated option — anything you forward overrides the default. The pass-through is
verbatim and order-preserving.

Output defaults to `~/Downloads/videos/` (created if absent); an explicit
forwarded `--out` still wins, since it lands after our default and argparse takes
the last `--out`.

## Examples

```bash
# Render every bundle in assay-site PR #57 with an Australian Assay voice.
./fetch-and-render 57 --repo medici-finance/assay-site -- --profile australian-assay

# Two PRs at once, by URL, a US built-in Orpheus voice, custom output dir.
./fetch-and-render \
    https://github.com/medici-finance/assay-site/pull/57 \
    https://github.com/medici-finance/assay-site/pull/74 \
    -- --us-voice leo --out ./out

# See exactly what it found and the command it WOULD run — no render.
./fetch-and-render 57 --repo medici-finance/assay-site --dry-run -- --profile english-assay
```

Example dry-run output:

```
PR medici-finance/assay-site#57  (https://github.com/medici-finance/assay-site/pull/57)
  head: medici-finance/assay-site@2cbb42e8
  found 1 bundle(s): public/blog/learnings/clean-is-not-a-scan-result
  - clean-is-not-a-scan-result
      from : medici-finance/assay-site :: public/blog/learnings/clean-is-not-a-scan-result
      url  : https://github.com/medici-finance/assay-site/pull/57
      staged: …/out/.fetched/pr-medici-finance_assay-site-57/clean-is-not-a-scan-result
    would run: …/explainer-video --script …/SCRIPT.md --slides …/explainer.html \
               --name clean-is-not-a-scan-result --url …/pull/57 \
               --out ~/Downloads/videos --profile english-assay

SUMMARY: 1 bundle(s) across 1 PR ref(s); would render 1
```

## Requirements

- `gh` (GitHub CLI), authenticated with read access to the PR's repo(s).
- Python 3 (stdlib only — no extra deps beyond what the engine already needs).
- Actually rendering additionally needs everything
  [`explainer-video`](./README.md#setup) needs (Apple-Silicon, the venv, node +
  Playwright). Where that is unavailable, `--dry-run` (or forwarding the engine's
  own `--dry-run`) still exercises the full fetch + command composition.

## Tests

Pure logic (PR parsing, bundle discovery, metadata → name/URL, command
composition, `--` splitting) is covered stdlib-only:

```bash
python3 tests/test_fetch_and_render.py
```

The `gh` plumbing (resolve / fetch) is exercised live by the tool's own
`--dry-run` against a real PR.
