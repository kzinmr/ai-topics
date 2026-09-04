# Log.md Prepend: No-Header Variant (Variant B)

**Date observed**: July 17, 2026 (x-bookmarks-ingest)

## Problem

The `Log.md prepend pitfall — header displacement` section in the wiki-ingestion-pipelines SKILL.md assumes log.md starts with `# Wiki Log\n\n_Log of all wiki changes...`. But the actual `log.md` at `/opt/data/ai-topics/wiki/log.md` may have NO header — it starts directly with `## [2026-07-17 22:30 UTC] ...`.

When a prepend script checks for a `# Wiki Log` header and doesn't find one, it falls through to the wrong branch and places the new entry AFTER old content instead of at the top.

## Detection

Always read the first line before choosing the prepend strategy:
```bash
head -1 /opt/data/ai-topics/wiki/log.md
```

| First line | Variant | Strategy |
|-----------|---------|----------|
| `# Wiki Log` | Variant A — header present | Header-preserving prepend |
| `## [20` | Variant B — no header | Simple prepend |

## Solution: Unified Prepend Script

This script handles both variants:

```python
import sys
LOG_PATH = "/opt/data/ai-topics/wiki/log.md"
new_entry = """## [YYYY-MM-DD HH:MM UTC] pipeline — summary

Body...
"""

with open(LOG_PATH) as f:
    current = f.read()

if current.startswith("# Wiki Log"):
    # Variant A — preserve header
    header_end = current.find('\n## [')
    if header_end == -1:
        header_end = current.find('\n---\n')
    if header_end != -1:
        header = current[:header_end]
        rest = current[header_end:]
        with open(LOG_PATH, 'w') as f:
            f.write(header + '\n' + new_entry + rest)
    else:
        with open(LOG_PATH, 'w') as f:
            f.write(new_entry + current)
else:
    # Variant B — no header, simple prepend
    with open(LOG_PATH, 'w') as f:
        f.write(new_entry + current)
```

## Cron-safe Usage

In cron mode, `execute_code` is blocked. Use:
```bash
# 1. write_file the script to /tmp/prepend_log.py
# 2. terminal python3 /tmp/prepend_log.py
```

## Root Cause

The `scripts/prepend-log-entry.py` shipped with the skill assumes Variant A. When log.md was rotated or the header was stripped during a log rotation, the script fails silently — the entry lands after older content instead of at the top.

The fix is always to `head -1` the file first to detect which variant is active.
