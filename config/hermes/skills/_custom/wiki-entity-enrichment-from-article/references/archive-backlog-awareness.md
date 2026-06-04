# Archive & Backlog Awareness for Entity Enrichment

When enriching wiki pages, leverage the triage archive and backlog pipeline for additional context.

## Checking the Archive

Before enriching an entity or concept page, check the triage archive — related articles may have been archived as skip/reference by the daily triage pipeline.

**Archive index**: `wiki/raw/archived/triage/archive_index.json`

```bash
# Check if a URL is archived
python3 -c "
import json
archive = json.load(open('wiki/raw/archived/triage/archive_index.json'))
print('archived' if 'https://example.com/article' in archive['urls'] else 'not archived')
"
```

**Why check the archive**:
- An article rated "skip (non-AI)" by triage may contain relevant context for an entity page (e.g., a security blog about CISA AWS leak → entity enrichment for Krebs/CISA)
- An article rated "reference" may have been noted for a concept page but not yet reflected in the author's entity page
- The archive preserves the `body_excerpt` and `reason_ja` — quick to scan for potential value

## Backlog Pipeline

The `raw-backlog-ingest` cron job (job ID `4e63c6f0d140`) processes ~5 articles every 4 hours using the LAN local LLM (`custom:hermes-llm-serial-gate`, model `qwen36-fast`).

**Tracking file**: `~/.hermes/processed_raw_articles.json`

```python
import json
tracking = json.load(open(os.path.expanduser("~/.hermes/processed_raw_articles.json")))
# Check if an article filename was already processed
if filename in tracking:
    status = tracking[filename]["status"]  # "processing", "done", "skipped", "error"
    decision = tracking[filename].get("decision")  # "take", "reference", "skip"
```

If the backlog agent already processed an article:
- `status: "done"` + `decision: "take"` → wiki page was created/updated — check wiki for the result before duplicating
- `status: "done"` + `decision: "skip"` → was archived — check the archive for the reason
- `status: "processing"` → still being processed — wait or take over if stale (>1 hour)
