#!/usr/bin/env python3
"""HN Algolia supplement for low-article-day fallback (daily-rss-triage Phase 1b).

Fetches (1) the current front page and (2) recent AI-relevant stories from the
last N days via keyword search. Works in cron (urllib only, no deps).

Usage:
    python3 /tmp/hn_algolia_supplement.py [--days N] [--min-points N]

Notes:
- Uses urllib.parse.urlencode so the `>` in numericFilters is URL-encoded
  automatically (raw `>` returns 400 Bad Request — see SKILL.md pitfall #4).
- Dedupes by objectID across keyword queries; skips stories below min points.
- ALWAYS prints the HN item link (item?id=objectID) next to every story, even
  when an external URL exists — the objectID is needed when citing the HN
  discussion in a wiki page's sources (see SKILL.md pitfall #17).
- Output is stdout text; pipe nothing into python — run the file directly.
Verified 2026-08-16 in trending-topics run; item-link output added 2026-08-17.
"""
import json, urllib.request, urllib.parse, datetime, time, argparse

BASE = "https://hn.algolia.com/api/v1/search"

def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": "hermes-trending/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))

def fmt_hit(hit, tag=""):
    oid = hit.get("objectID")
    pts = hit.get("points", 0)
    item_url = "https://news.ycombinator.com/item?id=" + str(oid)
    ext_url = hit.get("url") or item_url
    ts = (hit.get("created_at") or "")[:10]
    line = f"  [{ts} {pts:>4}pts/{hit.get('num_comments', 0):>3}c] {hit.get('title', '')}"
    if tag:
        line += f"  (q={tag})"
    return line + f"\n    ext: {ext_url}\n    hn : {item_url}"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=2)
    ap.add_argument("--min-points", type=int, default=20)
    args = ap.parse_args()

    # 1. Front page now
    try:
        d = fetch(BASE + "?tags=front_page&hitsPerPage=30")
        print("=== HN FRONT PAGE (%s) ===" % datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d %H:%M"))
        for hit in d.get("hits", []):
            print(fmt_hit(hit))
    except Exception as e:
        print("FRONT PAGE ERROR:", e)

    # 2. Recent AI-relevant stories (keyword loop)
    cutoff = int(time.time()) - args.days * 86400
    queries = ["AI", "LLM", "agent", "GPT", "Claude", "OpenAI", "Anthropic",
               "Gemini", "model", "GPU", "inference", "Open Source AI"]
    seen = set()
    print(f"\n=== HN RECENT AI STORIES (last {args.days}d, keyword search) ===")
    for q in queries:
        try:
            qurl = BASE + "?" + urllib.parse.urlencode({
                "query": q, "tags": "story",
                "numericFilters": f"created_at_i>{cutoff}",
                "hitsPerPage": 8,
            })
            d = fetch(qurl)
            for hit in d.get("hits", []):
                oid = hit.get("objectID")
                if oid in seen:
                    continue
                pts = hit.get("points", 0)
                if pts < args.min_points:
                    continue
                seen.add(oid)
                print(fmt_hit(hit, tag=q))
        except Exception as e:
            print(f"  query '{q}' ERROR: {e}")
        time.sleep(0.3)

if __name__ == "__main__":
    main()
