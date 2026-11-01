#!/usr/bin/env python3
"""Embed flashcards/*.json into a single self-contained ../flashcards.html."""
import glob
import json
import os
import re
import xml.etree.ElementTree as ET

here = os.path.dirname(os.path.abspath(__file__))
data = {}
for path in sorted(glob.glob(os.path.join(here, "[0-9]*.json"))):
    cards = json.load(open(path, encoding="utf-8"))
    for c in cards:
        svg = c.get("visual")
        if svg:
            ET.fromstring(svg)
    data[os.path.splitext(os.path.basename(path))[0]] = cards

tpl = open(os.path.join(here, "template.html"), encoding="utf-8").read()
payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
out = tpl.replace("/*__DATA__*/{}", payload)
open(os.path.join(here, "..", "flashcards.html"), "w", encoding="utf-8").write(out)
print({k: len(v) for k, v in data.items()}, "cards total:", sum(len(v) for v in data.values()))
