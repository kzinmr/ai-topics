# Daily RSS Triage — Full Reference

## Prerequisites
- `blogwatcher-db` skill loaded (database queries)
- `semantic-article-grouping` skill loaded (triage criteria)
- Pre-run script has already executed blogwatcher scan

## Phase 1: Report Generation
1. Parse script JSON output for scan results
2. Generate Japanese summary report (scan stats, failed blogs, articles list, Reddit highlights, newsletter info)
3. Save to `~/ai-topics/inbox/rss-scans/daily-scan-YYYY-MM-DD.md`
4. If article_total == 0 AND no newsletter → `[SILENT]`

## Phase 1.5: Newsjacking Triage Filter
Score 0-5 based on: Trend Surfing, Polarizing Promise, Contrarian Insight, Pattern Interrupt, In-Group Signal

## Phase 2: Triage
Check: Already covered? Substantive? Relevant? Newsjacking score?
Output triage table (Japanese).

## Phase 3: Wiki Ingestion
1. CRITICAL: Check existing entity pages FIRST — index.md may use different filenames
2. Scrape content
3. Determine category (entities, concepts, comparisons, queries)
4. Create or update page
5. Update index and log
6. Commit and push

## Key Pitfalls
- Index filename mismatches: short handles vs full names
- Pre-staged files from previous runs
- Reddit URLs fail with web_extract — use browser fallback
- Git rebase in headless cron: `GIT_EDITOR=true git rebase --continue`
- RSS 429 rate limits: log, don't retry
- Substack redirect URLs: pass full URL, web_extract handles natively
- Context window management: use `[Old tool output cleared]` pattern mid-run
