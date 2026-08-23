# Same-Day Pipeline Saturation Check

When the dreaming checkpoint shows `total_articles: 0` + `recent_raw_articles > 0` AND today's date has extensive log.md entries, the daily pipelines may have already saturated all AI-relevant content. Use this 3-step check BEFORE launching a full filesystem scan (Pattern E).

## When to use

- Checkpoint `total_articles: 0` (or effectively 0 — only non-AI articles)
- `recent_raw_articles > 0` (raw articles exist on disk)
- Today's date likely has pipeline activity (weekday, not holiday)

## 3-Step Verification (5 calls total, ~2 minutes)

### Step 1: log.md pipeline census (1 call)

```bash
grep "$(date +%F)" wiki/log.md | head -30
```

Count distinct pipeline entries: blog-wiki-ingest, newsletter-wiki-ingest, active-crawl, x-bookmarks-ingest, raw-backlog-ingest. If 3+ pipelines ran today with takes/refs, saturation is likely.

### Step 2: Triage JSON staleness (1 call)

```bash
python3 -c "import json; d=json.load(open('/opt/data/.hermes/cron/data/dreaming/triage_latest.json')); print(f'ts: {d.get(\"triage_timestamp\",\"?\")}, decisions: {len(d.get(\"decisions\",[]))}')"
```

If timestamp is yesterday's date, the prior triage was consumed by downstream. Today's dreaming needs fresh decisions.

### Step 3: Spot-check 3-5 raw articles (3-5 calls)

Pick the most promising AI-relevant raw articles from `ls -lt wiki/raw/articles/` and check:

```bash
# For each candidate, check if today's pipelines already handled it
grep -i "article-topic-keyword" wiki/log.md | grep "$(date +%F)"
```

If all spot-checked articles have matching log.md entries from today's pipelines → saturation confirmed. Skip filesystem scan.

## When saturation is confirmed

1. Save triage JSON with all-skip decisions
2. Run `archive_triage.py dreaming --keep-reference`
3. Update log.md with saturation entry
4. Commit (selective staging: log.md + archive files only)
5. Takes=0 is the correct outcome — do NOT force takes

## Validated: Aug 2026

- Checkpoint: 206 raw articles, 0 collected
- log.md showed 7 distinct pipeline runs today:
  - blog-wiki-ingest: 3 takes (Dark Hours, GitHub Models, sycophancy)
  - newsletter-wiki-ingest: 6 takes (TileRT, Claude Code 5, Lambert, Hark, Seedance, Eve)
  - active-crawl: 4 concepts (AI Agent Permission, LLM-Assisted Learning, WeatherNext, Genesis)
  - x-bookmarks-ingest: 2 bookmarks (Qwen-MM-Plugins, Graph Engineering)
  - raw-backlog-ingest: 4 batches (Paul Graham, Muse Spark, Harness design, Alignment researcher)
  - watchdog: auto-fixes
  - tag-audit-weekly: 7 tag violations
- Spot-checked 5 articles (Jeff Dean, Gary Marcus, Muse Glimmer, Sierra Context Engine, Krebs Snowflake) — all covered
- Result: 10-skip triage, archived 8 new URLs (2 dedup), commit `a9606145`

## Distinction from Pattern E (Filesystem Scan)

| Aspect | Same-Day Saturation | Pattern E Filesystem Scan |
|--------|-------------------|--------------------------|
| Trigger | Checkpoint 0 articles + today's log has 3+ pipelines | Checkpoint 0 articles + no today's pipeline entries |
| Goal | Confirm pipelines covered everything | Find gaps pipelines missed |
| Scan depth | Spot-check 3-5 articles | Full scan of 20-30 recent files |
| Expected outcome | Takes=0 (saturation confirmed) | 1-5 references, rest skip |
| Archive yield | Low (2-8 new URLs) | Medium (10-20 new URLs) |
