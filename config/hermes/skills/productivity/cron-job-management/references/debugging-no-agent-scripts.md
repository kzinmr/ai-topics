# Debugging no_agent Python Script Cron Failures

Workflow for diagnosing and fixing `no_agent=True` Python script cron jobs that show `last_status: error`.

## Pattern Recognition

When `cronjob(action='list')` shows a `no_agent` job with `last_status: error`:

```
{
  "job_id": "c7890b6e0e19",
  "name": "sitemap-monitor",
  "last_status": "error",
  "no_agent": true,
  "script": "sitemap_monitor.py"
}
```

## Diagnostic Workflow

### Step 1: Run the script directly

```bash
# The cron runner calls the script; reproduce manually to see the error
/opt/data/.hermes/venv/bin/python3 ~/.hermes/scripts/<name>.py 2>&1; echo "EXIT_CODE=$?"
```

**Common result**: `ModuleNotFoundError: No module named 'httpx'` or similar.

### Step 2: Check venv vs system Python

The most common failure cause: the script's shebang uses `#!/usr/bin/env python3` (system python), but dependencies (httpx, beautifulsoup4, lxml, readability-lxml) are installed in `/opt/data/.hermes/venv/`. The system python has no modules and no pip.

```bash
# Verify deps are in venv
/opt/data/.hermes/venv/bin/pip list | grep -iE "httpx|beautifulsoup|lxml|readability"

# Check where cron's python resolves
which python3  # usually /usr/bin/python3 (system, no deps)
```

### Step 3: Fix the shebang

```python
# Change FROM:
#!/usr/bin/env python3
# TO:
#!/opt/data/.hermes/venv/bin/python3
```

This ensures the cron runner uses the venv with all dependencies.

### Step 4: Install missing dependencies (if any)

```bash
/opt/data/.hermes/venv/bin/pip install httpx beautifulsoup4 lxml readability-lxml
```

### Step 5: Verify the fix

```bash
/opt/data/.hermes/venv/bin/python3 ~/.hermes/scripts/<name>.py 2>&1; echo "EXIT_CODE=$?"
# Should show EXIT_CODE=0 with normal output
```

### Step 6: Sync to git repo

Scripts live in TWO locations:

| Location | Purpose | Git-tracked? |
|----------|---------|-------------|
| `~/.hermes/scripts/` | Cron execution | ❌ No |
| `~/ai-topics/scripts/` | Source of truth | ✅ Yes |

After fixing `~/.hermes/scripts/<name>.py`, sync to the repo:

```bash
cp ~/.hermes/scripts/<name>.py ~/ai-topics/scripts/<name>.py
cd ~/ai-topics && git add scripts/<name>.py && git commit -m "fix: <summary>" && git push
```

### Step 7: Verify cron status

```bash
# Trigger a manual run
cronjob(action='run', job_id='<job_id>')

# Check status updated
cronjob(action='list')  # find the job, check last_status
```

### Step 8: Check partial output

Even failed runs may produce checkpoint data:

```bash
ls ~/.hermes/cron/data/sitemap_monitor/
ls ~/.hermes/cron/output/<job_id>/
```

Checkpoint JSONs can reveal which sources succeeded/failed before the error.

## Real Example: sitemap_monitor.py (2026-05-10)

**Symptom**: `sitemap-monitor` cron job `last_status: error`, no output files.

**Root cause**: `#!/usr/bin/env python3` shebang → system python lacks `httpx`.

**Secondary fixes applied after shebang fix**:
1. Removed Adept Blog (Cloudflare 403 block)
2. Removed Scale AI Blog (blog URLs not in sitemap)
3. Fixed ElevenLabs: changed sitemap_url from root index to `articles__en.xml` sub-sitemap
4. Fixed Arc.net: changed url_pattern from `/blog/` to `/blog` (no trailing slash in sitemap)
5. Added sitemap index support (recursive sub-sitemap fetching)

**Result**: `EXIT_CODE=0`, 530 new articles discovered (529 ElevenLabs + 1 Arc.net).

## Source-Specific Fix Patterns for Sitemap Monitor

When individual sources show `total_in_sitemap: 0` or errors:

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `403 Forbidden` | Cloudflare/WAF blocking | Remove source |
| `total_in_sitemap: 0` | Sitemap is an index (not flat) | Add index support OR use specific sub-sitemap URL |
| `total_in_sitemap: 0` | url_pattern doesn't match | Check actual sitemap URLs with `curl -sL <sitemap> | grep '<loc>'` |
| Blog URLs exist but not in sitemap | JS-rendered / client-side blog | Remove from sitemap monitor; use RSS/blogwatcher instead |
