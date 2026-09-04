# Log.md Prepend: Script Path Pitfall

## Problem

The `wiki-ingestion-pipelines` SKILL.md references `scripts/prepend-log-entry.py` as a reusable script:

```
python3 ~/.hermes/skills/wiki-ingestion-pipelines/scripts/prepend-log-entry.py LOG_PATH
```

**This path does not exist on the filesystem.** The script is only accessible via `skill_view(name='wiki-ingestion-pipelines', file_path='scripts/prepend-log-entry.py')` — it's embedded in the skill system, not on disk. Running `python3` on the path fails with `No such file or directory`.

This failure recurs every session that needs to prepend to log.md (newsletter-wiki-ingest, blog-wiki-ingest, dreaming-wiki-ingest, x-bookmarks-ingest, etc.).

## Reliable Workaround

Write the prepend logic to `/tmp/` and execute from there:

```python
# /tmp/prepend_log.py
HEADER = "# Wiki Log\n\n_Log of all wiki changes. Newest entries at top._\n\n"

def prepend_log_entry(log_path, new_entry):
    with open(log_path) as f:
        content = f.read()

    header_idx = content.find("# Wiki Log")
    if header_idx == -1:
        with open(log_path, 'w') as f:
            f.write(HEADER + new_entry.strip() + "\n\n" + content.strip() + "\n")
        return

    rest = content[header_idx:]
    existing = rest[len(HEADER):] if rest.startswith(HEADER) else rest

    with open(log_path, 'w') as f:
        f.write(HEADER + new_entry.strip() + "\n\n" + existing.strip() + "\n")

if __name__ == "__main__":
    import sys
    prepend_log_entry(sys.argv[1], sys.argv[2])
```

Usage:
```bash
# 1. write_file the log entry to /tmp/log_entry.txt
# 2. write_file the script above to /tmp/prepend_log.py
# 3. Run:
python3 /tmp/prepend_log.py /opt/data/ai-topics/wiki/log.md "$(cat /tmp/log_entry.txt)"
```

## Prevention

- Do NOT use `sed -i '1i...'` — fails on large files (>300KB log.md) with embedded special characters
- Do NOT use `tail -r` or pipe chains — blocked by the pipe-to-interpreter scanner in cron mode
- Do NOT use `execute_code` in cron mode (it's blocked) — always use `write_file` + `terminal python3`
- The `cat /tmp/entry.txt log.md > merged && mv merged log.md` pattern also works for simple cases but the Python script handles the header preservation edge case correctly

## Sessions Affected

- 2026-08-03: x-bookmarks-ingest — Shared Discovery Paradox
- All prior sessions using the prepend pattern
