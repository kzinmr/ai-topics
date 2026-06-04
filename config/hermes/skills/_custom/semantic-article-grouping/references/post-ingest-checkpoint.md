# Post-Ingest Checkpoint Update

After the downstream wiki-ingest job (e.g., `dreaming-wiki-ingest` or `newsletter-wiki-ingest`) finishes creating/enriching pages, overwrite `triage_latest.json` with a completion-status version. This makes the checkpoint a record of **what was actually done**, not just what was recommended.

## Why This Matters

- Lets the next pipeline in the chain (e.g., daily report generation) distinguish "already processed" from "not yet triaged"
- Gives human reviewers a clear audit trail: which recommended actions were taken vs skipped
- Prevents the triage JSON from being accidentally re-consumed by a retry or downstream job

## Format

```json
{
  "checkpoint_run_id": "20260522T180035Z",
  "summary_ja": "Summary in Japanese of what was accomplished",
  "total_raw_scanned": 141,
  "new_gaps_found": 6,
  "new_pages_created": 1,
  "pages_enriched": 6,
  "already_captured": 135,
  "clusters": [
    {
      "cluster_id": "agent-execution-tax",
      "topic_ja": "Agent Execution Tax",
      "status": "completed",
      "action": "created concepts/agent-execution-tax.md ✓"
    },
    {
      "cluster_id": "entity-enrichment-may-2026",
      "topic_ja": "Entity enrichments (4 pages)",
      "status": "completed",
      "actions": [
        "enriched entities/ed-zitron.md ✓",
        "enriched entities/anthropic.md ✓",
        "enriched entities/harvey.md ✓",
        "enriched entities/elevenlabs.md ✓"
      ]
    }
  ]
}
```

## Key Fields

- **`new_pages_created`** / **`pages_enriched`**: Distinguish between page types — new concept pages vs existing-page enrichments have different downstream implications
- **`clusters[].status`**: Use `"completed"`, `"partial"`, or `"skipped"` for each cluster
- **`clusters[].actions[]`**: List specific files touched, each with a ✓/✗ indicator

## Where to Save

Overwrite the same path the triage job saved to:

| Pipeline | Path |
|----------|------|
| Newsletter | `${HERMES_HOME}/cron/data/newsletter/triage_latest.json` |
| Blog | `${HERMES_HOME}/cron/data/blog_ingest/triage_latest.json` |
| Dreaming | `${HERMES_HOME}/cron/data/dreaming/triage_latest.json` |

## Implementation (execute_code)

```python
import json, os
output = {
    "checkpoint_run_id": "...",
    "summary_ja": "...",
    "new_pages_created": 1,
    "pages_enriched": 6,
    "clusters": [...]
}
path = f"{os.environ.get('HERMES_HOME', os.path.expanduser('~/.hermes'))}/cron/data/dreaming/triage_latest.json"
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
```

## Verification

After writing, verify in the same `execute_code` block:

```python
with open(path) as f:
    d = json.load(f)
print(f"Written: {len(d.get('clusters', []))} clusters, {d.get('new_pages_created', 0)} new pages, {d.get('pages_enriched', 0)} enrichments")
```
