# Cron HOME Path Mismatch Fix for blogwatcher-cli

## Problem

The Hermes cron environment sets `HOME=/opt/data/.hermes/home` (the profile's home directory), but the blogwatcher SQLite database lives at `/opt/data/.blogwatcher/blogwatcher.db`. The `blogwatcher-cli` binary (Hyaxia/blogwatcher v0.0.2) resolves its DB path as `$HOME/.blogwatcher/blogwatcher.db`, so when HOME is wrong, it finds an empty/missing DB and reports "No blogs tracked yet."

## Affected File

`~/.hermes/scripts/daily_inbox_collect.py` (canonical cron copy; NOT `~/ai-topics/scripts/daily_inbox_collect.py` which is a different version)

## Exact Patch (2 changes)

### Change 1: DB path resolution (line ~26)

```python
# BEFORE:
_BW_HOME = Path.home() / ".blogwatcher"

# AFTER:
# Use PROFILE_ROOT instead of Path.home() because cron HOME may differ from the actual user home
_BW_HOME = PROFILE_ROOT / ".blogwatcher"
```

### Change 2: Subprocess environment in run_blogwatcher_scan() (line ~52)

```python
# BEFORE:
env = {**os.environ, "BLOGWATCHER_YES": "1"}

# AFTER:
env = {**os.environ, "BLOGWATCHER_YES": "1", "HOME": str(PROFILE_ROOT)}
```

## Verification

```bash
# Should show 132 blogs (not "No blogs tracked yet")
HOME=/opt/data blogwatcher-cli blogs | head -5

# Run the full ingest
cd /opt/data && HOME=/opt/data /opt/data/.hermes/venv/bin/python ~/.hermes/scripts/blog_ingest.py
```

## Root Cause Detail

- `PROFILE_ROOT` is resolved via `HERMES_PROFILE_ROOT` or `HERMES_SUBPROCESS_HOME` env vars, or `Path.home()` as fallback
- In cron context, `HERMES_HOME=/opt/data/.hermes` so `PROFILE_ROOT = HERMES_HOME.parent = /opt/data`
- But `Path.home()` returns `/opt/data/.hermes/home` (the profile's configured home)
- The blogwatcher DB was created when HOME was `/opt/data`, so it lives at `/opt/data/.blogwatcher/`
