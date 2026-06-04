---
name: blog-ingest-troubleshooting
description: Debug and fix the full blog/newsletter cron pipeline chain — ingest, triage, wiki-ingest stages, checkpoint cascade failures, and re-execution on demand.
version: 2.0.0
author: Hermes
tags: [blog-ingest, newsletter-ingest, cron, troubleshooting, blogwatcher, pipeline]
---

# Cron Pipeline — Troubleshooting & Re-execution Guide

## Pipeline Architecture

Both blog and newsletter pipelines follow the same three-stage dependency chain:

```
ingest ──checkpoint──▶ triage ──checkpoint──▶ wiki-ingest
```

| Stage | Blog | Newsletter |
|-------|------|-----------|
| **Ingest** | `blog-ingest` (07:00 UTC) — RSS fetch via blogwatcher, scrape articles, save to `wiki/raw/articles/` | `newsletter-ingest` (07:10 UTC) — IMAP poll, extract links, save digests to `wiki/raw/newsletters/` |
| **Triage** | `blog-triage` (07:30 UTC) — read ingest checkpoint, group by topic, recommend take/skip | `newsletter-triage` (07:20 UTC) — read ingest checkpoint, group by topic, recommend take/skip |
| **Wiki-ingest** | `blog-wiki-ingest` (07:50 UTC) — consume triage checkpoint, create/update wiki pages | `newsletter-wiki-ingest` (07:40 UTC) — consume triage checkpoint, create/update wiki pages |

**Key insight:** Each stage reads a CHECKPOINT file (`~/.hermes/cron/data/<pipeline>/latest.json` or `triage_latest.json`) produced by the PREVIOUS stage. If the checkpoint isn't updated, downstream stages see nothing to process.

### Checkpoint File Locations

| Pipeline | Ingest checkpoint | Triage checkpoint |
|----------|-----------------|-------------------|
| Blog | `~/.hermes/cron/data/blog_ingest/latest.json` | `~/.hermes/cron/data/blog_ingest/triage_latest.json` |
| Newsletter | `~/.hermes/cron/data/newsletter/latest.json` | `~/.hermes/cron/data/newsletter/triage_latest.json` |

### Most Common Failure Pattern: "Checkpoint Cascade"

- **Ingest script times out** → checkpoint stays stale (showing 0 new articles from yesterday)
- **Triage reads old checkpoint** → sees 0 articles, outputs nothing
- **Wiki-ingest reads triage output** → sees empty, says "[SILENT]"

**Diagnosis:** Check `latest.json` timestamp vs wall clock. If it's from a previous day but new articles exist in `wiki/raw/articles/`, the ingest script ran but checkpoint wasn't updated.

## Re-executing a Pipeline on Demand

When the user asks to re-run the full pipeline chain:

### Step 1: Discover and Map

```bash
cronjob(action='list')
```

Identify all jobs by name, their `job_id`, and their dependency order. Independent pipelines (blog vs newsletter) can run concurrently.

### Step 2: Run in Reverse Order (Ingest First)

Run ingest jobs first, then triage, then wiki-ingest. Parallelize independent pipelines:

```python
# Run independent ingests concurrently
cronjob(action='run', job_id='<blog-ingest-id>')
cronjob(action='run', job_id='<newsletter-ingest-id>')

# Wait for both to complete
import time
time.sleep(60)  # or check cronjob list for last_run_at

# Run triage stages (both can run concurrently too)
cronjob(action='run', job_id='<blog-triage-id>')
cronjob(action='run', job_id='<newsletter-triage-id>')

time.sleep(60)

# Run wiki-ingest stages
cronjob(action='run', job_id='<blog-wiki-ingest-id>')
cronjob(action='run', job_id='<newsletter-wiki-ingest-id>')
```

**⚠️ `cronjob(run)` is async — it may return "ok triggered" but the job never actually executes.** Common reasons:
- The cron scheduler is down or stuck
- The job's pre-run script (`blog_ingest.py`) exists but the cron daemon has a stale reference path
- A previous run left the job in a broken state

**Workaround: Run the script directly from terminal instead of via cronjob(run).** This bypasses the scheduler entirely and gives you real-time error output.

**Note:** Only the *ingest* stages have standalone scripts. Triage and wiki-ingest stages embed their logic in the cron job prompt. If those fail via cronjob(run), you must either:
- Re-run the triage/wiki-ingest logic manually (the existing `newsletter-wiki-ingest` skill covers this workflow)
- Or directly create a triage checkpoint file with `take` decisions to feed into wiki-ingest

| Pipeline | Script path |
|----------|-------------|
| Blog ingest | `python3 ~/.hermes/scripts/blog_ingest.py` (or `~/ai-topics/scripts/blog_ingest.py`) |
| Newsletter ingest | `python3 ~/scripts/process_email.py` |

After running directly, verify the checkpoint was written:
```bash
cat ~/.hermes/cron/data/blog_ingest/latest.json | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'Articles: {len(d.get(\"saved_articles\",[]))} unsaved: {len(d.get(\"unsaved_articles\",[]))}')"
```

If the checkpoint still looks wrong, proceed to [checkpoint reconstruction](#checkpoint-reconstruction-when-ingest-script-times-out).

### Step 3: Verify Each Stage

Check that `last_run_at` timestamps updated after each `cronjob(run)`:

```python
jobs = cronjob(action='list')  # returns JSON
for job in jobs['jobs']:
    print(f"{job['name']}: last_run_at={job['last_run_at']}, status={job['last_status']}")
```

### Step 4: Read Output Files

Each cron job writes output to `~/.hermes/cron/output/<job_id>/YYYY-MM-DD_HH-MM-SS.md`. The Response section tells you what happened:

- `[SILENT]` = no new data to process (expected if nothing changed)
- Error messages = diagnose from the script output section
- Page creation reports = wiki actually updated

### Step 5: Diagnose Failures

**Pattern: Ingest ran but checkpoint shows 0 articles**
```
Checkpoint timestamp: yesterday → articles exist in wiki/raw/articles/ → stale checkpoint
Cause: ingest script timed out before writing checkpoint, or pre-run script failed
Fix: Run ingest script directly to update checkpoint, or investigate the timeout
```

**Pattern: Triage failed ("failed to parse JSON response from blog-triage output")**
```
Cause: The triage job ran but its output format didn't match what wiki-ingest expects
Fix: Check the triage output file for format mismatch. May need to re-run triage or clear stale output.
```

## Cron Pre-Run Script Dual Location

`blog_ingest.py` (and other pre-run scripts) live in **two locations** that must be kept in sync:

| Location | Purpose | Git-tracked? |
|----------|---------|-------------|
| `~/ai-topics/scripts/blog_ingest.py` | Source of truth | ✅ Yes (commit + push) |
| `~/.hermes/scripts/blog_ingest.py` | Cron execution copy | ❌ No |

**When fixing a script:**
1. Edit `~/ai-topics/scripts/blog_ingest.py` and test
2. Copy to cron location: `cp ~/ai-topics/scripts/blog_ingest.py ~/.hermes/scripts/blog_ingest.py`
3. Git commit + push: `cd ~/ai-topics && git add scripts/ && git commit -m "scripts: ..." && git push`

**Legacy note:** Some old cron jobs may still reference `/opt/data/.hermes/scripts/` — check `cronjob(action='list')` output for `script:` field and sync accordingly.

## Stage-Specific Troubleshooting

### Ingest Issues

### 1. Missing `daily_inbox_collect` module

If `blog_ingest.py` fails with `ModuleNotFoundError: No module named 'daily_inbox_collect'`:

Create `/opt/data/.hermes/scripts/daily_inbox_collect.py` with:
- `TODAY` — today's UTC date string
- `run_blogwatcher_scan()` — runs `blogwatcher-cli scan --workers N`, parses output
- `query_todays_articles()` — queries SQLite DB for article list

### 2. Wrong DB path

The blogwatcher DB is at `~/.blogwatcher/blogwatcher.db`, NOT `~/.blogwatcher-cli/blogwatcher-cli.db`.
Verify with:
```bash
python3 -c "import sqlite3; c=sqlite3.connect(str(Path.home()/'/.blogwatcher/blogwatcher.db')); print(c.execute('SELECT COUNT(*) FROM articles').fetchone()[0])"
```

### 3. Missing Python dependencies

`pip` is not installed in the container. Install via:
```bash
python3 /tmp/get-pip.py --user --break-system-packages
```
Then install deps:
```bash
python3 -m pip install httpx beautifulsoup4 readability-lxml --user --break-system-packages
```

### 4. Pre-run script timeout — script runs but checkpoint not updated

**Symptom:** `latest.json` shows yesterday's data (or is empty), but `wiki/raw/articles/` has today's files. Cron output says "Script timed out after 120s".

**First diagnostic step:** Run the script directly from terminal (see Step 2 workaround). If it succeeds with a fresh checkpoint, the cron scheduler itself was the problem — not the script.

**If the script also times out in terminal:** Read below for `4a` / `4b` fixes.

**Fallback: Checkpoint reconstruction** — if you can't fix the timeout immediately but need to unblock the pipeline, rebuild `latest.json` from existing articles on disk:

```python
from pathlib import Path
import json, re, datetime

articles_dir = Path.home() / "wiki" / "raw" / "articles"
today = datetime.date.today()
page_size = 80  # standard article file size

# Find articles created today (or within expected range)
candidates = []
for f in sorted(articles_dir.iterdir()):
    if not f.name.endswith(".md"):
        continue
    mtime = datetime.date.fromtimestamp(f.stat().st_mtime)
    if mtime == today:
        content = f.read_text()
        article = {"title": f.name.replace(".md",""), "url": "", "path": str(f)}
        candidates.append(article)

# Group by source (detect from file naming pattern)
# Write minimal checkpoint
checkpoint = {
    "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
    "saved_articles": candidates,
    "unsaved_articles": []
}
Path.home().joinpath(".hermes/cron/data/blog_ingest/latest.json").write_text(json.dumps(checkpoint, indent=2))
```

This creates a valid checkpoint that downstream triage can consume, even though article content URLs and metadata won't be in the triage context (triage works from the article file paths).

**Two root causes:**

#### 4a. Checkpoint file not written after successful article saves

**Symptom:** Articles exist on disk in `wiki/raw/articles/` with today's timestamp, but `latest.json` shows yesterday's date or is completely empty. Ingest script ran to completion for scraping, but crashed or timed out during checkpoint write.

**Root causes:**
- Script times out during final JSON serialization/write step (after all scraping is done)
- Script hits an exception in the checkpoint write section (e.g., JSON encoding error, permission issue)
- The cron scheduler kills the process at exactly 120s, right as the script is finishing scraping but before writing checkpoint

**Observed example (2026-04-29):** Script saved 35 articles (33 berthub.eu + 2 evanhahn.com) to disk, but `latest.json` remained at 2026-04-27 timestamp. The scrape completed within ~3 minutes but checkpoint write failed or was interrupted.

**Fix:** Add atomic checkpoint write at the START of the script (before any scraping), then update it incrementally as articles are saved:
```python
# Write initial checkpoint BEFORE scraping begins
output = {"ok": True, "saved_articles": [], "unsaved_articles": [], "date": TODAY, ...}
LATEST_PATH.write_text(json.dumps(output, indent=2))

# Then scrape, updating the checkpoint after each batch
for batch in chunks(articles, batch_size=10):
    saved = scrape_batch(batch)
    output["saved_articles"].extend(saved)
    LATEST_PATH.write_text(json.dumps(output, indent=2))  # atomic update
```

#### 4c. Sequential URL scraping too slow (most likely)

`blog_ingest.py` scrapes each article URL sequentially with httpx (`scrape_url()`). With 15+ articles at ~7-10s each, total scraping time exceeds the 120s pre-run script timeout. This is **exacerbated during LLM server reasoning load** — if the server is generating reasoning tokens for 90+ minutes, CPU/memory competition makes HTTP scraping even slower.

**Note:** The blogwatcher scan phase itself (`run_blogwatcher_scan()`) is also a major time consumer. With 83 blogs tracked, the scan takes 60-90+ seconds alone, leaving very little time for the scraping phase within the 120s timeout. Consider splitting the pipeline: run blogwatcher scan as a separate earlier cron job, then `blog_ingest.py` only needs to query the DB and scrape content.

**Fix:** Parallelize scraping with `ThreadPoolExecutor`:
```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def _scrape_item(item: dict) -> tuple:
    url = item.get("url", "").strip()
    if not url:
        return (item, None)
    return (item, scrape_url(url))

def persist_blog_articles(articles: dict) -> tuple[list[dict], list[dict]]:
    items = articles.get("blog_articles", [])
    if not items:
        return [], []
    saved, unsaved = [], []
    max_workers = min(8, len(items))
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(_scrape_item, item): item for item in items}
        for future in as_completed(futures):
            item, raw = future.result()
            ...
    return saved, unsaved
```

Also reduce per-URL timeout from 30s to **15s** to fail fast under load:
```python
with httpx.Client(timeout=15, ...) as client:
```

With 8 workers and 15s timeout, even 16 articles complete in ~35-45s — well within 120s.

**If the fix still times out**, also write the checkpoint **before** scraping (atomic update) to ensure downstream stages have data, then append saved articles:
```python
# Write empty checkpoint first
output["saved_articles"] = []
output["unsaved_articles"] = []
LATEST_PATH.write_text(json.dumps(output))

# Then scrape and update
saved, unsaved = persist_blog_articles(articles)
output["saved_articles"] = saved
output["unsaved_articles"] = unsaved
LATEST_PATH.write_text(json.dumps(output))
```

#### 4d. Large article sets from blogwatcher DB

**The DB can contain thousands of articles (2187+). `query_todays_articles()` returns ALL articles, causing `blog_ingest.py` to timeout trying to scrape every URL.**

Fix: Filter `query_todays_articles()` to only return articles NOT already in `~/wiki/raw/articles/`. Compare by URL against existing filenames (MD5 digest in filename). Or add a `LIMIT` / date filter.

**Always check `~/wiki/raw/articles/` for existing files before scraping.**

### Triage Issues

- Triage reads from the ingest checkpoint (`latest.json`). If ingest checkpoint shows 0 articles, triage produces no output.
- Triage output goes to `triage_latest.json` in the same checkpoint directory.
- The triage JSON format must be parseable by the wiki-ingest job — incorrect JSON structure causes wiki-ingest to fail with "failed to parse JSON response".

### Wiki-Ingest Issues

- Wiki-ingest reads from `triage_latest.json` in the pipeline's checkpoint directory.
- If triage produced no `take` decisions, wiki-ingest responds `[SILENT]` and no wiki pages are created.
- The `last_delivery_error: "no delivery target resolved for deliver=None"` is NORMAL for internal wiki-ingest jobs — they don't deliver to Discord, they just commit to the repo.
- After wiki-ingest, verify with `cd ~/ai-topics && git log --oneline -3` to confirm commit was pushed.

## Verification Steps

After re-running the full pipeline:

1. **Check ingest checkpoint:** `cat ~/.hermes/cron/data/blog_ingest/latest.json` — should show today's date
2. **Check raw articles exist:** `ls ~/wiki/raw/articles/ | sort` — newly scraped articles should have today's timestamps
3. **Check triage decisions:** `cat ~/.hermes/cron/data/blog_ingest/triage_latest.json` — should have `recommended_action: "take"` entries if anything was found
4. **Check wiki commits:** `cd ~/ai-topics && git log --oneline -3` — should show recent wiki commits
5. **Check log reports:** `read_file ~/wiki/log.md offset=-30` — should show ingest/triage/wiki-ingest activity
