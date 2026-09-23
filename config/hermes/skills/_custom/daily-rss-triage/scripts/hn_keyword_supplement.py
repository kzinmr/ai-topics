# HN Algolia keyword supplement (AI stories beyond the front page)

Companion to `hn_algolia_supplement.py` (front-page scan). The front_page tag decays
within ~24h and high point thresholds filter out mid-size controversies, so run this
keyword sweep too on trending-topics runs. Verified 2026-09-14: it surfaced Bengio's
"Why are AI agents lying, cheating and coordinating?" (625pts), Claude 18+ (673pts),
Garry Tan distillation (390pts), Tell HN OpenAI opt-in (482pts) — none on the
front-page scan.

Usage: extract the Python block below and run as a clean script. `python3 hn_kw_run.py [days] [min_points]` (defaults 4, 80).

Tip (VERIFIED 2026-09-21): extend the query list below with topic keywords from the wiki's currently-hot sources (`config/hot-topics.yaml`, recent log.md, today's blog_ingest titles — e.g. a hot model/person name like "Jev"). Generic keywords alone miss same-day ecosystem clusters (clone/toolkit waves around one launch) whose stories rank below threshold; one targeted keyword surfaced the whole Jev→Kev/Jev-Leftpad/CUA-S1 wave.

```python
import urllib.request, urllib.parse, json, sys, datetime
def get(url):
    req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
    return json.loads(urllib.request.urlopen(req, timeout=20).read())
days = int(sys.argv[1]) if len(sys.argv) > 1 else 4
minpts = int(sys.argv[2]) if len(sys.argv) > 2 else 80
cutoff = int(datetime.datetime.now(datetime.UTC).timestamp()) - days*86400
seen = set()
# Extend this list per-run with today's hot topic keywords (see tip above).
queries = ["AI agent", "Claude", "OpenAI", "LLM", "open weights", "model release",
           "prompt injection", "AI safety", "coding agent", "MCP", "Anthropic"]
for q in queries:
    try:
        d = get(f"https://hn.algolia.com/api/v1/search?query={urllib.request.quote(q)}"
                f"&tags=story&numericFilters=created_at_i%3E{cutoff},points%3E{minpts}")
    except Exception as e:
        print(q, "ERR", e); continue
    for h in d.get('hits', [])[:5]:
        oid = h.get('objectID')
        if oid in seen: continue
        seen.add(oid)
        print(f"[{h.get('created_at','')[:10]} {h.get('points')}pts/{h.get('num_comments')}c] {h.get('title')}")
        print(f"    ext: {h.get('url')}")
        print(f"    hn : https://news.ycombinator.com/item?id={oid}")
```

Caveats:
- `%3E` encoding for `>` in numericFilters is mandatory (else 400).
- Dedup by objectID across the front-page scan output too, or the same story appears twice.
- `url` is None for Ask HN / Tell HN text posts — cite the `hn :` item link only.
- Queries overlap heavily (an "AI agent" hit reappears under "LLM") — the seen-set handles it.
