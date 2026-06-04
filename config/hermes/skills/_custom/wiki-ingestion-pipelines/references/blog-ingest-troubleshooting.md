# Blog Pipeline Troubleshooting — Full Reference

Debug and re-execute the blog/newsletter cron pipeline chain.

## Checkpoint Locations
| Pipeline | Ingest checkpoint | Triage checkpoint |
|----------|-----------------|-------------------|
| Blog | `~/.hermes/cron/data/blog_ingest/latest.json` | `~/.hermes/cron/data/blog_ingest/triage_latest.json` |
| Newsletter | `~/.hermes/cron/data/newsletter/latest.json` | `~/.hermes/cron/data/newsletter/triage_latest.json` |

## Common Failure: Checkpoint Cascade
- Ingest script times out → checkpoint stale → triage sees 0 → wiki-ingest sees empty → `[SILENT]`
- Diagnosis: Check `latest.json` timestamp vs wall clock

## Re-execution (on demand)
1. List jobs: `cronjob(action='list')`
2. Run ingest first (blog + newsletter concurrently)
3. Run triage next
4. Run wiki-ingest last
5. Verify: check last_run_at, read output files, check git commits

## Script Dual Location
| Location | Purpose |
|----------|---------|
| `~/ai-topics/scripts/blog_ingest.py` | Source of truth (git-tracked) |
| `~/.hermes/scripts/blog_ingest.py` | Cron execution copy |

Fix: edit ai-topics/ version, then cp to .hermes/scripts/

## Stage-Specific Issues

### Ingest: Missing daily_inbox_collect module
Create stub with TODAY, run_blogwatcher_scan(), query_todays_articles()

### Ingest: Wrong DB path
Use `~/.blogwatcher/blogwatcher.db`, NOT `~/.blogwatcher-cli/blogwatcher-cli.db`

### Ingest: Timeout
- Parallelize with ThreadPoolExecutor (max_workers=8, timeout=15s per URL)
- Write empty checkpoint BEFORE scraping (atomic update)
- Filter DB query to only articles not already in `~/wiki/raw/articles/`

### Ingest: Checkpoint reconstruction
If ingest script fails but articles exist on disk, rebuild latest.json from existing files.

### Triage: Empty output
Triage reads from ingest checkpoint. If checkpoint shows 0 articles, triage produces nothing.

### Triage: Produced markdown instead of JSON (parsing failure in wiki-ingest)
Blog-triage may produce a markdown report with embedded JSON and triage tables instead of raw JSON. The downstream `blog-wiki-ingest` job sees this as `"failed to parse JSON response from blog-triage output"`.

**Recovery procedure**:
1. Read the raw triage output markdown file (path in error: `/opt/data/.hermes/cron/output/<job-id>/<timestamp>.md`)
2. Locate the `## Script Output` section — it contains the raw ingest checkpoint JSON with `candidates` array and `unsaved_articles`
3. Locate the triage agent's response after `## Response` — it contains markdown tables with TAKE/REFERENCE/SKIP classifications and wiki page targets
4. Use the triage decisions to identify which candidates to process (filter for TAKE, ordered by star rating)
5. Proceed with wiki-ingest manually: read raw articles → check existing pages → create/enrich/update wiki pages → update index.md and log.md → commit

**Root cause**: The blog-triage cron job writes its own analysis as a markdown response, and the triage decisions are not serialized as a standalone JSON file. The `triage_latest.json` checkpoint only mirrors the ingest checkpoint, not the triage output.

### Triage: Produced markdown instead of JSON (parsing failure in wiki-ingest)

### Wiki-ingest: "No delivery target"
Normal for internal wiki-ingest jobs — they deliver to git, not Discord. Check `git log`.
