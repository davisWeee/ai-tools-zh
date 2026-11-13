#!/usr/bin/env python3
"""Usage: python3 fill_links.py links.json   (e.g. {"PDFMATHTRANSLATE":"https://pan.quark.cn/s/xxx", ...})
Replaces {{QUARK_LINK_<TOOL>}} in README.md and docs/*.html, then commit & push."""
import json, sys, glob
m = json.load(open(sys.argv[1]))
for f in ["README.md"] + glob.glob("docs/*.html"):
    s = open(f).read()
    for k, v in m.items(): s = s.replace("{{QUARK_LINK_%s}}" % k, v)
    open(f, "w").write(s)
