# Newsletter Triage Checkpoint Recovery

## Problem
The newsletter-triage cron job fails with `"failed to parse JSON response from newsletter-triage output"` (response render failure), but the downstream wiki-ingest needs the triage decisions.

## Root Cause
The triage agent saves its checkpoint JSON to `triage_latest.json` as the **last action before rendering its cron response**. When the response render fails (e.g., model output formatting issue, JSON serialization boundary), the checkpoint survives because saving happened first.

## Recovery Procedure (for newsletter-wiki-ingest and blog-wiki-ingest)

### Step 1: Read the checkpoint directly
```python
import json
path = "/opt/data/.hermes/cron/data/newsletter/triage_latest.json"
with open(path) as f:
    data = json.load(f)
print(f"Decisions: {len(data['decisions'])} | Takes: {sum(1 for d in data['decisions'] if d['recommended_action']=='take')}")
```

### Step 2: Skip any JSON-extraction workarounds
Do NOT attempt to extract JSON from the failed job's markdown output at `${HERMES_HOME}/cron/output/<job-id>/<timestamp>.md`. The checkpoint file is the authoritative source.

### Step 2.5: Re-fetch article bodies for takes (CRITICAL)
The triage agent's `web_extract` calls truncate at ~5,000 chars. While sufficient for triage decisions (topic, entity identification), the `body_excerpt` in `triage_latest.json` is **not** the full article body. For wiki enrichment, you need the complete article text.

**For newsletter post URLs (Substack):** Use the curl + `<article>` tag extraction pattern (see `references/newsletter-wiki-ingest.md` § "Cron-Mode Article Body Extraction"). Save each fetched article as `~/wiki/raw/articles/YYYY-MM-DD_source-slug.md`.

**For beehiiv tracking URLs:** If triage decisions reference beehiiv articles but the tracking tokens have expired (403), the inbox summary's `articles[].summary` and `articles[].key_claims` fields are the richest available content. Triaged items from 403-expired newsletters are typically assessed at the topic level only — do NOT re-attempt URL resolution for these.

**Why this matters**: Newsletter roundups synthesize multiple sources in dense paragraphs. The 5K-char triage excerpt captures section headings and first paragraphs but misses the technical details (benchmark numbers, model architecture specs, price comparisons) that make wiki pages valuable. Confirmed Jul 2026: the Poolside Laguna S 2.1 AINews article body (26K chars) contained benchmark comparisons and Reddit community quotes not present in the 2K-char triage excerpt.

### Step 3: Verify each take independently
Before creating/updating wiki pages, check:
1. Does the `candidate_wiki_path` page exist on disk?
2. If it exists, read its content sections — does it already contain the article's specific claims?
3. If it exists but lacks the content → enrich (not create)
4. If it doesn't exist → create

### Step 4: Archive pre-handoff verification
The triage agent also runs `archive_triage.py` before attempting its response render. If the downstream wiki-ingest runs:
```bash
python3 ~/ai-topics/scripts/archive_triage.py newsletter --keep-reference
```
and receives `"All items already archived (dedup)"`, proceed without re-archiving. This is expected.

### Step 5: Parallel enrichment
Use `delegate_task` with a `tasks` array for parallel enrichment. Each subagent reads the entity page and patches (never write_file for pages >40 lines).

## Validated Incidents
- Jun 17, 2026 — dreaming pipeline (checkpoint recovered)
- Jun 22, 2026 — newsletter pipeline (checkpoint recovered)
- Jul 6, 2026 — newsletter pipeline (checkpoint recovered, all 3 validated takes enriched, all skip/reference items already archived)
- Jul 24, 2026 — newsletter pipeline (checkpoint recovered, 4 takes re-fetched and enriched, 19 items archived, article bodies re-extracted from Substack URLs)
- Jul 26, 2026 — newsletter pipeline (checkpoint recovered, Takes=0 but Refs=1: enriching existing-concept page + creating skeleton entity + updating SCHEMA.md tag taxonomy). Validates the references-only triage enrichment pattern: even without takes, reference enrichment is valuable.
- Jul 29, 2026 — newsletter pipeline (checkpoint recovered, 3 takes + 3 references: created events/2026-07-29-rsi-pace-letter.md, enriched opus-5.md, openai-codex.md, nvidia.md, open-weight-ai-regulation.md, agentic-engineering.md). Direct git push succeeded despite sibling-agent unstaged changes in config/. Validated tag registration pattern: new event page used 'rsi' tag -- pre-commit hook blocked, fixed by adding 'rsi' to SCHEMA.md taxonomy alongside existing 'recursive-self-improvement'.

## Related
- `semantic-article-grouping` skill § "Pipeline Resilience: Cron Output Format"
- `semantic-article-grouping` skill § "Post-Recovery Verification"
