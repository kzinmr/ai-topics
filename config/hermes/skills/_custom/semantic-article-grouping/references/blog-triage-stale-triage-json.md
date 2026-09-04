# Stale triage_latest.json — Blog Pipeline Already Completed

## Pattern

When blog-triage runs at 07:30 UTC, the blog-ingest → blog-wiki-ingest pipeline may have **already completed** for the same batch of 20 candidates. The log.md shows comprehensive processing ("20 new articles processed, 3 wiki pages created/updated") but `triage_latest.json` at `${HERMES_HOME}/cron/data/blog_ingest/triage_latest.json` is **stale** (from a previous day).

## Root Cause

The intermediate blog-triage step in the pipeline may not persist `triage_latest.json` when blog-ingest → blog-wiki-ingest runs as a combined sequence. The log.md is the authoritative record; the triage file is a downstream-consumed artifact that can fall behind.

## Detection

1. **Check log.md for today's date first** — do NOT check triage_latest.json's freshness as a proxy for "has the pipeline run?"
2. Look for lines like `"## [2026-07-24] Blog ingest — 20 new articles processed, 3 wiki pages created/updated"`
3. Verify which articles are explicitly listed vs. unaccounted
4. Only then check triage_latest.json's timestamp

## Action Plan

1. **Read log.md entries** for today to understand which articles mapped to which wiki pages
2. **Cross-reference** log.md against the candidate list — identify any unaccounted articles (typically 2-5 short Simon Willison quote posts)
3. **Read unaccounted articles** for body_excerpts and independent triage
4. **Produce fresh triage_latest.json** with all 20 decisions — even though takes are already wiki-processed, the downstream pipeline reads this file to confirm completion
5. **Run archive_triage.py** — skip+reference items must be persisted

## Validated Yield (July 24, 2026)

- 20 candidates from 8 sources
- log.md explicitly accounts for 15 articles (3 wiki pages created/updated + 5 AI-relevant raw saved + 9 non-AI raw saved)
- 5 unaccounted: all short Simon Willison posts (2 quote posts, orchestrions, Nativ, sea lions)
- Final: 4 takes, 2 references, 14 skips
- Archive: 16 items (all skip+reference), total archive URLs: 1,881
