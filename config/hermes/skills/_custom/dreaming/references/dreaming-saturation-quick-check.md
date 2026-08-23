# Saturation Quick-Check Pattern

When the dreaming checkpoint shows `total_articles: 0` and `triage_latest.json` has decisions from a prior unconsumed run, use this fast-path to determine if filesystem scan (Pattern E) will yield results.

> **Also see**: `references/dreaming-same-day-pipeline-saturation.md` for the variant where today's pipelines have ALREADY run (log.md has 3+ pipeline entries today) — a faster check that skips filesystem scan entirely.

## Pre-flight (2 tool calls)

1. **Read triage_latest.json** via `read_file` (not `cat | python3` — tirith blocks pipes)
2. **Check log.md for dreaming entries today**: `grep "$(date +%F).*dreaming" wiki/log.md | head -3`

If prior triage is unconsumed (no dreaming-wiki-ingest after triage timestamp) AND all decisions are skip → the upstream already processed everything. Filesystem scan is still worth doing for sitemap-monitor articles.

## Batch Coverage Check (efficient pattern)

Instead of individual `search_files` calls per article, batch-check with terminal:

```bash
# Step 1: Find which entity pages exist
find ~/ai-topics/wiki -name "*keyword1*" -o -name "*keyword2*" -type f 2>/dev/null

# Step 2: Grep for specific claims across all found pages
grep -i "specific-detail\|metric\|announcement" ~/ai-topics/wiki/entities/entity1.md ~/ai-topics/wiki/concepts/concept1.md | head -10

# Step 3: For bulk frontmatter source check
grep -h "^  - raw/" ~/ai-topics/wiki/entities/entity1.md | grep "article-filename"
```

This reduces 12+ individual `search_files` calls to 3-4 terminal calls.

## Expected Yield (July 2026 validated)

| Scenario | Scan depth | Expected references | Expected skips |
|----------|-----------|-------------------|----------------|
| Sitemap-heavy batch (Hex, dbt) | 30 files | 1-2 (17%) | 20+ non-AI |
| Mixed RSS + sitemap | 30 files | 3-5 | 15-20 |
| Pure RSS (Simon Willison, blogs) | 20 files | 0-1 | 10-15 |

**Key insight**: Sitemap-monitor scrapes are high-volume but low-AI-relevance (data/analytics marketing blogs batch-skip after reading 1-2 frontmatters). RSS feeds from AI-focused blogs (Simon Willison, swyx, etc.) have higher hit rates but are usually already covered by blog-wiki-ingest.

## Saturation Indicators

When ALL of these are true, declare saturation:
- `archive_triage.py` returns `new_archived: 0` or `dedup_skipped` > 80% of candidates
- All filesystem-scan articles have matching wiki pages with substantive body coverage
- `triage_latest.json` has 0 takes across all decisions
- Log.md shows multiple consecutive dreaming saturation entries

At this point, the dreaming cycle's value is limited to catching rare gaps from sitemap-monitor batches that daily pipelines missed. The archive index (2,466 URLs by Aug 2026) confirms comprehensive coverage.
