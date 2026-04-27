#!/usr/bin/env python3
"""Pre-run script: fetch X bookmarks via xurl, output JSON for the agent.

Requires OAuth2 user authentication (bookmarks are user-private data, Bearer/app-only won't work).
Dedups against ~/.hermes/processed_x_bookmarks.json.
"""
import json, os, subprocess, sys
from pathlib import Path

XURL = os.environ.get("XURL_PATH", "/opt/data/bin/xurl")

HERMES_HOME = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
DB = HERMES_HOME / "processed_x_bookmarks.json"

def run(*args):
    return subprocess.run([XURL, "--auth", "oauth2", *args], capture_output=True, text=True, check=True).stdout

processed = set(json.loads(DB.read_text()).get("tweet_ids", [])) if DB.exists() else set()

try:
    resp = json.loads(run("bookmarks", "-n", "100"))
except subprocess.CalledProcessError as e:
    print(json.dumps({"error": e.stderr, "new_bookmarks": []}), file=sys.stderr)
    sys.exit(1)

new = [t for t in resp.get("data", []) if t["id"] not in processed]

for t in new:
    t["external_urls"] = [
        u["expanded_url"]
        for u in t.get("entities", {}).get("urls", [])
        if u.get("expanded_url", "").startswith(("http://", "https://"))
        and "x.com" not in u["expanded_url"]
        and "twitter.com" not in u["expanded_url"]
    ]

print(json.dumps({"new_bookmarks": new}, indent=2))

# Unbookmark each new bookmark from X (removes from X's list so next run sees only fresh bookmarks)
unbookmark_failures = 0
for t in new:
    try:
        run("unbookmark", t["id"])
    except subprocess.CalledProcessError as e:
        unbookmark_failures += 1
        print(f"warn: unbookmark failed for {t['id']}: {e.stderr}", file=sys.stderr, flush=True)

# Update dedup DB (safety net — if unbookmark fails, this prevents re-processing)
processed.update(t["id"] for t in new)
DB.parent.mkdir(parents=True, exist_ok=True)
DB.write_text(json.dumps({
    "tweet_ids": sorted(processed),
    "unbookmark_failures": unbookmark_failures
}, indent=2))
