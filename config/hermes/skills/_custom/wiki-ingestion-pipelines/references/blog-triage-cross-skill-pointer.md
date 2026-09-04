# Blog Triage — Cross-Skill Pointer

The detailed blog triage workflow (body-reading mandate, cross-pipeline dedup, stale `triage_latest.json` handling) lives in:

→ **[[skills/semantic-article-grouping]]** (Input Sources C → Blog-Ingest Checkpoint section, plus `references/blog-triage-stale-triage-json.md`)

The relevance heuristics (which articles are wiki-worthy vs raw-save) are in:

→ **`references/blog-triage-relevance-heuristics.md`** (this skill)

## Stale triage_latest.json Pattern (validated July 24, 2026)

When blog-triage runs and log.md shows "20 new articles processed, 3 wiki pages created/updated" for today's date, but `triage_latest.json` at `${HERMES_HOME}/cron/data/blog_ingest/triage_latest.json` is from a previous day:

1. **Do NOT assume pipeline hasn't run** — the log.md is the authoritative record
2. **Confirm** which articles are wiki-processed by reading log.md
3. **Read** any unaccounted articles for body_excerpts  
4. **Still produce fresh triage_latest.json** so downstream pipeline file is current
5. **Archive skip+reference items** via `archive_triage.py blog --keep-reference`
