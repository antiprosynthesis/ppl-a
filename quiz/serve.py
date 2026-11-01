#!/usr/bin/env python3
"""Serve the quiz locally. "Save to repo" writes results/<name>.md, then git add/commit/push
using your own git login (gh auth / credential helper) - no token needed.

Usage: python3 quiz/serve.py [port]
"""
import json, re, subprocess, sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS, RESULTS = ROOT / "docs", ROOT / "results"


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(DOCS), **kw)

    def reply(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if self.path != "/api/save":
            return self.reply(404, {"message": "not found"})
        data = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))))
        name = data.get("name", "")
        if not re.fullmatch(r"quiz-[0-9-]+\.md", name):
            return self.reply(400, {"message": "bad file name"})
        RESULTS.mkdir(exist_ok=True)
        path = RESULTS / name
        path.write_text(data["content"], encoding="utf-8")
        git("add", str(path))
        c = git("commit", "-m", f"Add quiz result {name}", "--", str(path))
        p = git("push")
        if c.returncode or p.returncode:
            err = (c.stderr + c.stdout + p.stderr).strip()[-300:]
            return self.reply(200, {"message": f"Saved results/{name} locally; git failed: {err}"})
        self.reply(200, {"message": f"Saved and pushed results/{name}"})


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print(f"Quiz at http://localhost:{port}/quiz.html  (Ctrl+C to stop)")
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
