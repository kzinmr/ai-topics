# Archive Pipeline Flow

Triage decisions (skip/reference) are persisted to `wiki/raw/archived/triage/` via `scripts/archive_triage.py` so they can be re-evaluated later. Nothing is silently discarded.

## Directory Structure

```
wiki/raw/archived/
├── ARCHIVE.md                          # Archive conventions and schema
└── triage/
    ├── archive_index.json              # URL dedup index: {"urls": [...], "updated": "..."}
    ├── blog/                           # blog-triage skip/reference saves
    │   └── {YYYY-MM-DD}_{run_id}.json
    ├── newsletter/                     # newsletter-triage skip/reference saves
    │   └── {YYYY-MM-DD}_{run_id}.json
    └── dreaming/                       # dreaming-group skip/reference saves
        └── {YYYY-MM-DD}_{run_id}.json
```

## Archive Entry Format

```json
{
  "archived_at": "ISO8601",
  "triage_run_id": "20260519T070026Z",
  "source": "blog",
  "summary_ja": "...",
  "decisions": [
    {
      "item_id": "blog-1",
      "title": "...",
      "url": "https://...",
      "raw_path": "/opt/data/ai-topics/wiki/raw/articles/...",
      "recommended_action": "skip",
      "reason_ja": "非AI — ...",
      "body_excerpt": "本文冒頭300字..."
    }
  ]
}
```

## Script: archive_triage.py

```bash
# Archive blog triage skip+reference items
python3 ~/ai-topics/scripts/archive_triage.py blog --keep-reference

# Archive newsletter triage
python3 ~/ai-topics/scripts/archive_triage.py newsletter --keep-reference

# Archive all three pipelines at once
python3 ~/ai-topics/scripts/archive_triage.py --all --keep-reference
```

The script:
- Reads `triage_latest.json` from each pipeline's checkpoint directory
- Extracts items with `recommended_action: skip` or `reference` (when `--keep-reference`)
- Adds `body_excerpt` by reading the raw article files
- Saves date-stamped archive files
- Updates `archive_index.json` for URL deduplication

## Auto-Integration in Checkpoint Scripts

The three checkpoint scripts (`blog_triage_checkpoint.py`, `newsletter_triage_checkpoint.py`, `dreaming_group_checkpoint.py`) now automatically call `archive_triage.py` after saving the triage JSON. The archive result is included in the output as `_archive`.

## Raw Backlog Cross-Reference

The `raw_backlog_collect.py` script (used by `raw-backlog-ingest` cron job) cross-references `archive_index.json` to detect already-archived articles:

```python
archive = load_archive_index()
archived_urls = set(archive.get("urls", []))
# Each candidate gets archive_status: "already_archived" | "not_archived"
```

This prevents the backlog agent from re-processing articles that were already triaged and archived by the main daily pipeline.

## Comparison Workflow

When the `raw-backlog-ingest` agent processes an article:
1. If `archive_status: "already_archived"` → skip with reason "already archived by daily triage"
2. The agent can still decide to re-evaluate archived articles if the archive decision seems questionable
3. New decisions are also archived via the same mechanism

## Policies

- **Never delete**: Archive preserves full context for later re-evaluation
- **URL dedup**: Same URL won't be archived twice
- **Re-evaluation**: Archived items can be revisited — e.g., a "non-AI" article might become relevant later
- **Body excerpts**: Every archived entry includes the opening body text that informed the decision
