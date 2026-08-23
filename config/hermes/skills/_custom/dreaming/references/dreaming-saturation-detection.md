# Dreaming Saturation Detection — Quick Checklist (Validated June-July 2026)

## When to Use
When the dreaming cycle finds `total_articles: 0` in the checkpoint but `recent_raw_articles > 0` on disk, the daily pipeline stack may have already consumed all AI-relevant articles. This reference provides a quick 5-minute saturation detection checklist.

## 5-Minute Saturation Detection Checklist

### Step 1: Pipeline Timestamp Check (~1 min)
```bash
# Check which pipelines ran today
grep "$(date +%F)" ~/ai-topics/wiki/log.md | head -20
```

Expected daily pipeline window (07:00-18:00 UTC):
- blog-ingest (07:00) → blog-triage (07:30) → blog-wiki-ingest (07:50)
- newsletter-ingest (07:10) → newsletter-triage (07:20) → newsletter-wiki-ingest (07:40)
- active-crawl (11:00)
- x-bookmarks-ingest (11:30)
- skeleton-enrich-daily (19:00)

If all 3 main pipelines (blog, newsletter, active-crawl) ran → saturation is likely.

### Step 2: Decision Count Verification (~1 min)
```bash
# Blog triage decisions
python3 -c "import json; d=json.load(open('/opt/data/.hermes/cron/data/blog_ingest/triage_latest.json')); print(f'Blog: {len(d.get(\"decisions\",[]))} decisions')"

# Newsletter triage decisions
python3 -c "import json; d=json.load(open('/opt/data/.hermes/cron/data/newsletter/triage_latest.json')); print(f'Newsletter: {len(d.get(\"decisions\",[]))} decisions')"

# Prior dreaming triage (may be stale)
python3 -c "import json; d=json.load(open('/opt/data/.hermes/cron/data/dreaming/triage_latest.json')); print(f'Dreaming: {len(d.get(\"decisions\",[]))} decisions, takes={sum(1 for x in d[\"decisions\"] if x[\"recommended_action\"]==\"take\")}')"
```

If blog + newsletter triage together have 20+ decisions → high saturation.

### Step 3: Cross-Pipeline Dedup (~2 min)
```python
import json, os, glob, time

# Collect all processed identifiers
processed = set()
for path in [
    os.path.expanduser('~/.hermes/cron/data/blog_ingest/triage_latest.json'),
    os.path.expanduser('~/.hermes/cron/data/newsletter/triage_latest.json'),
    os.path.expanduser('~/.hermes/cron/data/dreaming/triage_latest.json'),
]:
    if os.path.exists(path):
        d = json.load(open(path))
        for dec in d.get('decisions', []):
            if isinstance(dec, dict):
                for key in ['url', 'title', 'raw_path']:
                    val = dec.get(key, '')
                    if val:
                        if key == 'raw_path':
                            processed.add(os.path.basename(val))
                        else:
                            processed.add(val.lower()[:50] if key == 'title' else val)

# Count unprocessed raw articles
raw_dir = os.path.expanduser('~/ai-topics/wiki/raw/articles')
cutoff = time.time() - 3*86400
unprocessed = []
for f in sorted(glob.glob(os.path.join(raw_dir, '*.md')), key=os.path.getmtime, reverse=True):
    if os.path.getmtime(f) > cutoff:
        fname = os.path.basename(f)
        if not any(fname == p or fname in p for p in processed):
            size = os.path.getsize(f)
            if size > 400:
                unprocessed.append((fname, size))

print(f"Unprocessed articles (>400B, last 3 days): {len(unprocessed)}")
```

Expected yield in saturation scenario: 200+ raw articles → 8-15 genuinely unprocessed (~4-7%).

### Step 4: Spot-Check Key Articles (~1 min)
Read 2-3 of the largest unprocessed articles to assess AI relevance. **Check articles from the last 2-3 days, not just today** — the checkpoint date range only covers collected articles, but `raw/articles/` may have unprocessed sitemap-scraped files from prior days that no pipeline consumed. **Validated July 2026**: Checkpoint range was July 4-11, filesystem scan found 1 reference from July 10 (Fireworks LangChain Deep Agents) that all pipelines missed.
- If all are non-AI (personal blogs, vintage computing, non-tech) → full saturation
- If 1-2 are AI-relevant → proceed with normal dreaming triage

## Saturation Levels

| Unprocessed | AI-Relevant | Saturation Level | Action |
|---|---|---|---|
| <10 | <3 | ~95% | Report Takes=0, archive skips |
| 10-20 | 3-5 | ~85% | Normal dreaming cycle, expect 1-2 takes |
| 20-50 | 5-10 | ~70% | Full dreaming cycle needed |
| 50+ | 10+ | <70% | Pipeline gap — investigate why articles weren't processed |

## What Dreaming Adds in Saturation Scenario (Takes=0)

When Takes=0 after saturation, the dreaming cycle still provides value:

1. **Non-AI content filtering**: Identifying and archiving the ~20-30% of raw articles that are non-AI blog content
2. **Entity enrichment references**: Finding the 3-5 articles that provide enrichment opportunities for existing entity pages
3. **Coverage verification**: Confirming that the day's pipeline coverage is complete
4. **Archive maintenance**: Running `archive_triage.py dreaming --keep-reference` to persist skip/reference decisions

## Stale Triage JSON Detection

When `triage_latest.json` exists with decisions from a prior run:

```bash
# Check if prior triage was consumed
grep "Dreaming wiki-ingest\|dreaming.*consolidation" ~/ai-topics/wiki/log.md | head -5
```

- If dreaming-wiki-ingest entry exists AFTER the triage timestamp → prior triage consumed → safe to overwrite
- If no entry exists → prior triage may be pending → use it as-is

## Validated Examples

### July 11, 2026 (Pattern E, checkpoint range vs filesystem scope)
- Checkpoint: `total_articles: 1` (non-AI ATP podcast) → effectively 0
- `recent_raw_articles: 164` on disk
- Filesystem scan found 4 reference enrichments (Cohere DSD, Fireworks MiniMax M3 Blackwell, Hebbia data integrations, Fireworks LangChain Deep Agents)
- Key finding: checkpoint date range (Jul 4-11) didn't bound filesystem scope — July 10 articles from sitemap-monitor were unprocessed by all pipelines
- Prior triage (6 decisions, 0 takes, 1 ref, 5 skips) consumed by Jul 10 dreaming-wiki-ingest
- Archive: 15 candidates, 3 new, 12 dedup (1519 total URLs)
- Takes=0 correct: all candidates were entity page enrichments, not new concept pages

### July 2, 2026 (Saturation ~85%)
- 104 raw articles, 52 unprocessed after dedup
- 1 take (Pinecone Nexus), 5 references, 3 batch skips (38 articles)
- Prior dreaming triage (50 decisions) confirmed consumed via log.md
- Archive: 7 new items, 1330 total URLs

### June 29, 2026 (Mode 1b Recovery)
- Checkpoint had 0 articles, 211 raw articles on disk
- Cross-pipeline dedup yielded 9 themes (1 take, 7 references, 1 skip)
- blog-triage + newsletter-triage + active-crawl already consumed most content
