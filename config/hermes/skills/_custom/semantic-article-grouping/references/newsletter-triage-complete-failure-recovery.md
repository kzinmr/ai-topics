# Newsletter-Triage Complete Failure Recovery (June 25, 2026)

## Scenario

The upstream `newsletter-triage` job **never started** because of an API key error:

```
RuntimeError: Error code: 401 - {'error': {'message': 'The API key you provided is invalid.'}}
```

No triage checkpoint was saved for today — `triage_latest.json` was from the **previous day** (Jun 24).

## Distinction from Partial Failure

| Failure mode | Checkpoint exists? | Recovery |
|-------------|-------------------|----------|
| JSON parse failure (render error) | ✅ Yes — saved before render | Read checkpoint directly |
| API/auth failure (never started) | ❌ No — job never ran | Perform triage in-place |

## Recovery Procedure (for newsletter-wiki-ingest as fallback)

When `triage_latest.json` is stale (>24h old) and the triage job failed with auth/connection error:

### Step 1: Verify the failure type

```bash
# Check the cron failure output
cat /opt/data/.hermes/cron/output/<job-id>/<timestamp>.md | tail -20
# Look for "401" or "API key" or "connection refused"
```

### Step 2: Check newsletter ingest checkpoint

```bash
# The ingest pipeline ran successfully (it's a no_agent script with its own auth)
python3 -c "
import json
with open('/opt/data/.hermes/cron/data/newsletter/latest.json') as f:
    d = json.load(f)
print(json.dumps(list(d.keys()), indent=2))
print(f'Messages: {len(d.get(\"processed_messages\", []))}')
"
```

### Step 3: Read inbox pre-triage summary (PRIMARY source)

The ingest pipeline also generates a pre-triage summary at:
```bash
ls -lt ~/ai-topics/wiki/raw/inbox/newsletter-ingest/ | head -5
```

This file contains `estimated_topics`, `classification` (critical/high/low), `primary_url` for each newsletter, and `suggested_pages`. It is sufficient for priority ordering and publication identification.

### Step 4: Resolve newsletter post URLs directly

For each critical/high priority newsletter, use the `primary_url` from the inbox summary.

### Step 5: Cross-reference against existing wiki pages

This step is identical to the normal triage workflow — check existing entity/concept pages, check log.md for same-day processing, check raw/articles/ for sitemap-monitor output.

### Step 6: Build and save triage JSON

Use the write_file-to-/tmp/ + terminal approach (execute_code is blocked in cron mode).

### Step 7: Proceed to wiki ingest

After saving the triage JSON, proceed with normal enrichment:
- Process takes (create/update wiki pages)
- Update index.md and log.md
- Archive skip/reference items
- Commit and push

## Effort Estimate

- 3 newsletters → ~45 minutes total (URL resolution, wiki cross-reference, enrichment, commit)
- 5 newsletters → ~60-75 minutes
- The time sinks are: (a) Substack URL HTML extraction for full body text, (b) cross-referencing existing wiki pages, (c) patch tool precision.

## Key Tools Used (cron mode)

| Need | Tool | Notes |
|------|------|-------|
| Read newsletter body | `write_file` to `/tmp/` + `terminal python3` with curl | execute_code blocked in cron |
| Cross-reference wiki | `read_file` + `grep` via terminal | search_files is fine |
| Enrich entities | `patch` | Watch out for partial-read → broad-match pitfall |
| New entity creation | `write_file` or `delegate_task` | delegate_task works for complex pages |
| JSON save | `write_file` to `/tmp/` + `terminal python3` | Can't use execute_code or os.path.expanduser |
| Archive | `python3 scripts/archive_triage.py newsletter --keep-reference` | Path may resolve to ~/.hermes/home/ — verify |

## Pitfall: os.path.expanduser in Cron Terminal Context

When running from terminal in cron mode, `os.path.expanduser("~/.hermes")` may resolve to nested paths like `/opt/data/.hermes/home/.hermes/`.

**Fix**: Always use environment variable or hardcoded path:
```python
hermes_home = os.environ.get('HERMES_HOME', '/opt/data/.hermes')
wiki_root = '/opt/data/ai-topics/wiki'
```

**Applies to**: `archive_triage.py` and any scripts run via `terminal python3 /tmp/script.py` in cron mode.
