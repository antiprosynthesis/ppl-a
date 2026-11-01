#!/usr/bin/env python3
"""Merge quiz/questions + quiz/explanations into a self-contained docs/quiz.html
(and copy the flashcards page + a small landing page into docs/ for GitHub Pages)."""
import glob
import json
import os
import shutil

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
bank = []
missing = 0
for path in sorted(glob.glob(os.path.join(here, "questions", "*.json"))):
    sub = json.load(open(path, encoding="utf-8"))
    ex_path = os.path.join(here, "explanations", os.path.basename(path))
    ex = json.load(open(ex_path, encoding="utf-8")) if os.path.exists(ex_path) else {}
    for q in sub["questions"]:
        e = ex.get(q["id"])
        if not e:
            missing += 1
            continue
        assert len(e["why"]) == len(q["options"]), q["id"]
        q["topic"] = e["topic"]
        q["why"] = e["why"]
        if e.get("note"):
            q["note"] = e["note"]
    bank.append(sub)

tpl = open(os.path.join(here, "template.html"), encoding="utf-8").read()
payload = json.dumps(bank, ensure_ascii=False).replace("</", "<\\/")
docs = os.path.join(root, "docs")
os.makedirs(docs, exist_ok=True)
open(os.path.join(docs, "quiz.html"), "w", encoding="utf-8").write(tpl.replace("/*__DATA__*/[]", payload))
if os.path.exists(os.path.join(root, "flashcards.html")):
    shutil.copy(os.path.join(root, "flashcards.html"), os.path.join(docs, "flashcards.html"))
open(os.path.join(docs, "index.html"), "w", encoding="utf-8").write(
    """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>PPL(A) study</title><style>body{font-family:system-ui;background:#0f1419;color:#e6edf3;max-width:560px;margin:40px auto;padding:0 16px}
a{display:block;background:#1a2129;border:1px solid #2c3744;border-radius:12px;padding:18px;margin:12px 0;color:#4f9dff;text-decoration:none;font-size:18px}
a small{display:block;color:#8b98a5;font-size:14px}</style></head><body><h1>✈️ PPL(A) study</h1>
<a href="quiz.html">📝 Quiz trainer<small>20 questions, explanations, re-study report</small></a>
<a href="flashcards.html">🃏 Visual flashcards<small>1,300+ cards with diagrams</small></a>
<a href="https://github.com/jonathanva/ppl-a/blob/main/Quick_Reference.md">📄 Cheat sheets &amp; notes<small>on GitHub</small></a></body></html>
"""
)
print("subjects:", len(bank), "questions:", sum(len(s["questions"]) for s in bank), "without explanation (excluded):", missing)
