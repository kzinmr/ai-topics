# Inbox Summary `wiki_action` Misalignment Due to Parallel Pipelines

## Pattern

The inbox pre-triage summary (from `~/wiki/raw/inbox/newsletter-ingest/`) may recommend `wiki_action: "create_or_update"` for a topic that **other pipelines have already processed** by the time newsletter-triage runs. This is not a bug — the inbox summary is generated before blog-ingest/blog-wiki-ingest complete, so it cannot know what those pipelines decided.

## Concrete Example (2026-07-17)

| Component | Time | Event |
|-----------|------|-------|
| blog-ingest | 07:00 UTC | Scraped Kimi K3 from Simon Willison's blog |
| blog-wiki-ingest | ~07:05 UTC | Created `concepts/kimi-k3.md` with full benchmarks/pricing |
| newsletter-ingest | 07:10 UTC | Collected AINews Kimi K3 newsletter |
| Inbox summary | ~07:12 UTC | Classified Kimi K3 as **critical**, recommended `create_or_update` (correct at this instant) |
| **newsletter-triage** | **07:20 UTC** | Found Kimi K3 page **already exists** on disk. Downgraded to `reference` — enrichment opportunity for KDA/Attention Residuals |

## What Happened

The inbox summary's `wiki_action` ("create_or_update") was correct at the moment the summary was generated (07:12 UTC, no wiki page existed). By the time newsletter-triage ran (07:20 UTC), blog-wiki-ingest had created the page. The inbox summary had no way to know this — it only checks the subject line and newsletter sender, not the actual wiki state.

## Detection

When the inbox summary recommends `create_or_update` for a model/company release topic:

1. **Check if blog-wiki-ingest ran today**: `grep "$(date +%F)" ~/ai-topics/wiki/log.md | grep -i "blog-wiki-ingest"`
2. **Check for the entity/concept page**: `find ~/ai-topics/wiki/{concepts,entities} -name "*keyword*" -mtime -1`
3. **The page may already be comprehensive** — do not assume the inbox summary's urgency applies

## Resolution

- If the page exists and covers the topic well → downgrade `take` to `reference` (enrichment for architectural details the newsletter may add)
- If the page exists but is incomplete → upgrade back to `take` (enrich the existing page)
- The inbox summary's `wiki_action` is a **hint, not a ground truth** — always verify against actual wiki state

## Related

- `scheduling-race-condition.md` in main skill — blog-triage runs AFTER newsletter-triage
- `blog-triage-coverage-verification.md` — cross-pipeline dedup patterns
