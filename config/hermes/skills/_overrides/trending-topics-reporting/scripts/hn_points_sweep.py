#!/usr/bin/env python3
"""HN Algolia points-only recent sweep — the weekend/second-pass discovery query.

Companion to scripts/hn_calibrate.py (which is keyword-per-query). On weekend
runs, and whenever the day's lead stories are policy/finance/ops pieces whose
titles match no AI keyword list, run THIS instead of (better: in ADDITION to)
the keyword pass. Verified 2026-10-31: yielded 6 of the trending run's 8 topics
(CPC bailout resolution 644p, SRE deskilling 605p, Blackstone rating 311p,
Proton reversal 277p, Northflank, Cisco) that the keyword pass missed entirely.

Usage:
    python3 scripts/hn_points_sweep.py                 # last 24h, points>150
    python3 scripts/hn_points_sweep.py --hours 36 --min-points 120
    python3 scripts/hn_points_sweep.py --hours 24 --grep "AI|LLM|agent|model"

Output per story: points/comments | title | url | hn item link.
Dedup by objectID against the hn_calibrate.py keyword output.
"""
import urllib.request, urllib.parse, json, time, sys, argparse, re

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research script)"})
    with urllib.request.urlopen(req, timeout=25) as r:
        raw = r.read()
    if raw[:2] == b'\x1f\x8b':
        import gzip; raw = gzip.decompress(raw)
    return json.loads(raw.decode("utf-8", "replace"))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=int, default=24)
    ap.add_argument("--min-points", type=int, default=150)
    ap.add_argument("--hits", type=int, default=40)
    ap.add_argument("--grep", default="", help="optional case-insensitive title regex filter")
    a = ap.parse_args()
    since = int(time.time()) - a.hours * 3600
    # CRITICAL: '>' must be %3E-encoded or Algolia returns 400.
    nf = f"created_at_i%3E{since},points%3E{a.min_points}"
    url = (f"https://hn.algolia.com/api/v1/search?tags=story"
           f"&numericFilters={nf}&hitsPerPage={a.hits}")
    data = fetch(url)
    pat = re.compile(a.grep, re.I) if a.grep else None
    seen = set()
    for h in data.get("hits", []):
        oid = h.get("objectID")
        if oid in seen:
            continue
        seen.add(oid)
        title = h.get("title") or ""
        if pat and not pat.search(title):
            continue
        print(f"{h.get('points')}p/{h.get('num_comments')}c | {title} | "
              f"{h.get('url')} | hn: https://news.ycombinator.com/item?id={oid}")

if __name__ == "__main__":
    main()
