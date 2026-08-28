#!/usr/bin/env python3
"""HN Algolia targeted point-score queries for trending-topic ★ calibration.

Verified working in cron mode 2026-08-15 (direct urllib fetch, no curl pipe).
Usage:
    python3 scripts/hn_calibrate.py                       # default query list
    python3 scripts/hn_calibrate.py --days 7              # wider window (weekly mode)
    python3 scripts/hn_calibrate.py "Gemini 3.7 Flash" "xAI Cursor acquisition"

Prints per query: [created] points/comments | title | url (newest first).
Use the points to calibrate ★ ratings: >400pts consistently correlates with
★★★★☆+; cross-check created_at is inside the analysis window (HN model-name
queries return OLD high-point stories — see SKILL.md pitfall).
"""
import urllib.request, urllib.parse, json, time, sys

DEFAULT_QUERIES = [
    "Gemini 3.7 Flash",
    "DeepSeek Harness",
    "Anthropic risk report",
    "Responsible Scaling Policy",
    "malicious skill files",
    "GPT-5.6 Sol ultrafast",
    "Ultrafast mode",
    "GLM-5.3",
    "xAI Cursor acquisition",
    "OpenAI IPO",
    "Anthropic IPO",
    "AI text watermarking EU",
    "agent skill supply chain",
]

def hn_search(query, days=5, hits=8):
    """search_by_date endpoint; numericFilters created_at_i must use %3E (not >)."""
    since = int(time.time()) - days * 86400
    url = ("https://hn.algolia.com/api/v1/search_by_date?query=" +
           urllib.parse.quote(query) +
           f"&tags=story&hitsPerPage={hits}&numericFilters=created_at_i%3E{since}")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research script)"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            data = json.loads(r.read().decode())
        out = []
        for hit in data.get("hits", []):
            out.append({
                "title": hit.get("title", "")[:110],
                "points": hit.get("points") or 0,
                "comments": hit.get("num_comments") or 0,
                "created": hit.get("created_at", "")[:10],
                "url": (hit.get("url") or "")[:80],
            })
        return out
    except Exception as e:
        return [{"error": str(e)}]

def main():
    args = sys.argv[1:]
    days = 5
    if "--days" in args:
        i = args.index("--days")
        days = int(args[i + 1])
        del args[i:i + 2]
    queries = args or DEFAULT_QUERIES
    for q in queries:
        print(f"=== {q} ===")
        res = hn_search(q, days=days)
        if not res:
            print("  (no hits)")
        for h in res:
            if "error" in h:
                print(f"  ERROR: {h['error']}")
            else:
                print(f"  [{h['created']}] {h['points']}pts/{h['comments']}c | {h['title']} | {h['url']}")
        time.sleep(1)  # be polite to the API

if __name__ == "__main__":
    main()
