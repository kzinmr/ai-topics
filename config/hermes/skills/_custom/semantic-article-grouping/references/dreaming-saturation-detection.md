# Dreaming-Group Saturation Detection Pattern

**When to use**: The dreaming-collect checkpoint returns `total_articles: 0` or `articles: []`, but `recent_raw_articles` shows a large backlog (100+). The daily pipeline has already consumed all AI-relevant content.

## Quick Detection Steps (5 min)

### Step 1: Check pipeline execution timestamps

```bash
ls -lt ~/.hermes/cron/data/blog_ingest/triage_latest.json \
       ~/.hermes/cron/data/newsletter/triage_latest.json \
       ~/.hermes/cron/data/dreaming/triage_latest.json 2>/dev/null
```

If blog-triage and newsletter-triage timestamps are from **today** and dreaming-triage is from **yesterday**, the daily pipeline ran first — saturation is likely.

### Step 2: Count today's decisions

```bash
python3 -c "
import json
blog = json.load(open('$HOME/.hermes/cron/data/blog_ingest/triage_latest.json'))
nl = json.load(open('$HOME/.hermes/cron/data/newsletter/triage_latest.json'))
for name, data in [('Blog', blog), ('Newsletter', nl)]:
    dec = data.get('decisions', [])
    takes = sum(1 for d in dec if d.get('recommended_action') == 'take')
    refs = sum(1 for d in dec if d.get('recommended_action') == 'reference')
    print(f'{name}: {len(dec)} decisions (take={takes}, ref={refs})')
"
```

If both pipelines show **0 takes**, saturation is confirmed — all AI-relevant content was already processed as `skip` or `reference`.

### Step 3: Count today's wiki log entries

```bash
grep "$(date +%Y-%m-%d)" ~/ai-topics/wiki/log.md | head -20
```

If log shows 10+ entries from blog-wiki-ingest, newsletter-wiki-ingest, active-crawl, and sitemap-monitor — all pipelines ran and enriched pages.

### Step 4: Spot-check 5 recent raw articles for wiki coverage

```bash
ls -lt ~/ai-topics/wiki/raw/articles/ | head -10
# Pick 5 articles, check if wiki pages exist:
for topic in "john-jumper" "spacex-cursor" "norway-ai" "beneficial-rl" "glm-5-2"; do
    find ~/ai-topics/wiki -name "*${topic}*" 2>/dev/null | head -1
done
```

If all 5 have existing wiki pages with today's `updated` date → saturation confirmed.

## Expected Outcome

- **Takes=0** is the CORRECT result, not a failure
- The triage JSON should still be saved (all skips/references) for downstream pipeline confirmation
- The archive should still be run (`archive_triage.py dreaming --keep-reference`)
- The dreaming-wiki-ingest downstream will confirm Takes=0 and skip enrichment — this is the right behavior

## When NOT to force a take

If every article you evaluate already has:
1. A wiki concept/entity page with matching content
2. A log.md entry from today's pipeline run
3. The article's specific claims present in the page body

Then Takes=0 is correct. Forcing a take to avoid "empty output" creates duplicate pages or redundant enrichments.

## Typical saturation volume

| Metric | Active day | Saturation day |
|--------|-----------|---------------|
| Raw articles evaluated | 50-200 | 30-60 |
| Already wiki-covered | 60-80% | 90-96% |
| Non-AI content | 15-25% | 20-30% |
| Takes | 1-5 | 0 |
| References | 3-8 | 1-3 |
| Skips | 40-150 | 25-55 |
