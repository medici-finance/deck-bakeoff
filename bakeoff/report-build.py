#!/usr/bin/env python3
"""Build report.html from report.body.html: inline fonts + downscaled image data URIs."""
import base64, io, os, re, sys
from PIL import Image

ROOT = "/Users/iholsman/jojig/Lending/rwa-bakeoff"
FONTS = os.path.join(ROOT, "skills/design/canvas-design/canvas-fonts")
BODY = os.path.join(ROOT, "bakeoff/report.body.html")
OUT = os.path.join(ROOT, "report.html")

MAXW = 1200
JPEG_Q = 82

def font_uri(name):
    with open(os.path.join(FONTS, name), "rb") as f:
        return "data:font/ttf;base64," + base64.b64encode(f.read()).decode()

def img_uri(relpath):
    p = os.path.join(ROOT, relpath)
    if not os.path.exists(p):
        raise SystemExit("MISSING IMAGE: " + p)
    im = Image.open(p).convert("RGB")
    if im.width > MAXW:
        h = round(im.height * MAXW / im.width)
        im = im.resize((MAXW, h), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=JPEG_Q, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

def main():
    with open(BODY, encoding="utf-8") as f:
        html = f.read()

    fonts = set(re.findall(r"\{\{FONT:([^}]+)\}\}", html))
    for name in fonts:
        html = html.replace("{{FONT:%s}}" % name, font_uri(name))

    # winner explainer frames: use winner/shots only if winner/READY exists at render time
    ready = os.path.exists(os.path.join(ROOT, "winner/READY"))
    scene_dir = "winner/shots" if ready else "shots/canvas-design/brand/staging"
    if ready:
        note = ("Frames captured from the winner&rsquo;s own build, "
                "<span class=\"m\">winner/shots/scene-NN.png</span>, verified present at render time.")
    else:
        note = ("<strong>Note.</strong> The winner&rsquo;s own frame set "
                "(<span class=\"m\">winner/shots/</span>) was not present at render time &mdash; no "
                "<span class=\"m\">winner/READY</span> marker &mdash; so these nine frames are taken from the "
                "identical source track, <span class=\"m\">shots/canvas-design/brand/staging/scene-NN.png</span>. "
                "Same film, same scenes; a re-render once the marker lands will substitute the winner&rsquo;s frames.")
    print("winner/READY present:", ready, "-> scene dir:", scene_dir)
    for n in range(1, 10):
        cand = "%s/scene-%02d.png" % (scene_dir, n)
        if not os.path.exists(os.path.join(ROOT, cand)):
            alt = "%s/scene-%d.png" % (scene_dir, n)
            if os.path.exists(os.path.join(ROOT, alt)):
                cand = alt
        html = html.replace("{{SCENE:%02d}}" % n, "{{IMG:%s}}" % cand)
        html = html.replace("{{SCENEPATH:%02d}}" % n, cand)
    html = html.replace("{{SCENENOTE}}", note)

    imgs = sorted(set(re.findall(r"\{\{IMG:([^}]+)\}\}", html)))
    total = 0
    for rel in imgs:
        uri = img_uri(rel)
        total += len(uri)
        html = html.replace("{{IMG:%s}}" % rel, uri)

    leftover = re.findall(r"\{\{[A-Z]+:[^}]+\}\}", html)
    if leftover:
        raise SystemExit("UNRESOLVED TOKENS: " + ", ".join(sorted(set(leftover))[:10]))

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print("fonts inlined:", len(fonts))
    print("images inlined:", len(imgs), "approx image payload MB: %.2f" % (total / 1024 / 1024))
    print("report.html bytes: %d (%.2f MB)" % (len(html), len(html) / 1024 / 1024))

if __name__ == "__main__":
    main()
