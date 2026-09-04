# Archive Dedup Output Variants

The `archive_triage.py` script produces different JSON output depending on whether the items were already archived by a prior step (e.g., the triage agent pre-archived before its response render).

## Normal (first-time archive)
```json
{"pipeline_name": {"ok": true, "candidates": 13, "new_archived": 13, "dedup_skipped": 0, "archive_path": "...", "total_archive_urls": 391}}
```
- `candidates`: total skip+reference items processed  
- `new_archived`: number actually written  
- `dedup_skipped`: URLs/items already in the archive index  
- `total_archive_urls`: running total

## Pre-archived (triage already ran archive)
```json
{"pipeline_name": {"ok": true, "message": "All items already archived (dedup)", "archived": 0}}
```
- `message`: indicates the triage agent already called `archive_triage.py` before its response render  
- `archived: 0`: nothing newly written; all items already persisted  
- **This is expected behavior** — proceed without re-archiving. The downstream wiki-ingest should not treat this as an error.

## When this happens
The triage cron job (newsletter-triage, blog-triage, dreaming-group) saves the archive **before** attempting its JSON response render. If the render fails, the archive is already committed. The downstream wiki-ingest pipeline (newsletter-wiki-ingest, blog-wiki-ingest, dreaming-wiki-ingest) runs archive again as a safety check — it will hit the dedup and get the `"All items already archived"` variant.

Validated: Jul 6, 2026 (newsletter-wiki-ingest, after triage response render failure).
