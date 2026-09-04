# Off-Schedule Newsletter Triage: Same-Day Blog-Triage Cross-Reference

**Validated**: July 25, 2026 — newsletter-triage ran at 10:12 UTC (not scheduled 07:20)

## Context

The daily pipeline schedule has blog-ingest (07:00) → blog-triage (07:30) → blog-wiki-ingest (07:50) and newsletter-ingest (07:10) → newsletter-triage (07:20) → newsletter-wiki-ingest (07:40). At scheduled times, blog-triage has NOT yet run when newsletter-triage executes.

But when pipelines run **off-schedule** (delays, manual triggers, catch-up runs), blog-triage may have already completed before newsletter-triage starts. In this case, the same-day blog-triage JSON IS valid for cross-pipeline dedup.

## Decision Flow

1. **Check blog-triage JSON timestamp** (`${HERMES_HOME}/cron/data/blog_ingest/triage_latest.json`)
2. If `triage_timestamp` or `checkpoint_run_id` contains **today's date AND a time earlier than newsletter-triage's start** → decisions are valid cross-reference sources
3. If timestamp is **yesterday's date** → NOT valid, fall back to `raw/articles/` and `log.md`

## Concrete Example (2026-07-25)

| Pipeline | Scheduled | Actual Run |
|----------|-----------|------------|
| blog-ingest | 07:00 | ~07:00 |
| blog-triage | 07:30 | 10:09 UTC |
| newsletter-ingest | 07:10 | ~07:10 |
| newsletter-triage | 07:20 | 10:12 UTC |

Blog-triage had already rated "Introducing Claude Opus 5" as **reference** (★★★☆☆ → update entities/simon-willison.md and concepts/claude/models.md). Newsletter-triage used this decision to correctly downgrade the AINews Claude Opus 5 topic from take to reference, avoiding a redundant take decision.

**Newsletter-triage had also processed these 4 other newsletters:**
- SemiAnalysis AMD vs CUDA — no blog overlap (new entity/concept pages needed)
- Hugo Bowne-Anderson Production AI Agent — no blog overlap (new entity/concept pages)
- Simon Willison OpenAI cyberattack — already covered by event page (blog-bridge: Simon's blog articles used as event page sources)
- Beehiiv Voice AI — Cloudflare blocked, no content to compare

## Key Insight

The original rule ("newsletter-triage cannot rely on same-day blog-triage JSON") was written for the 07:20 scheduled window. It is correct for that window. But it is too absolute for off-schedule runs. The timestamp check makes the distinction clean: if blog-triage has already completed today, trust it. If not, don't.

## Cross-Pipeline Items Detected

| Blog-Triage Decision | Newsletter Equivalent | Action Taken |
|---------------------|----------------------|-------------|
| Claude Opus 5: reference (entities/simon-willison, concepts/claude/models) | AINews Claude Opus 5: was candidate for take | Downgraded to reference |
| Boris Cherny Opus 5 PI resistance: reference (entities/boris-cherny) | No newsletter equivalent | N/A |
| General blog articles (skip) | No newsletter equivalent | N/A |
