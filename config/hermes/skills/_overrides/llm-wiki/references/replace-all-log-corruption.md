# Log Corruption via `patch` with `replace_all=True`

## Symptom

After using `patch(old_string="...", new_string="...", path="wiki/log.md", replace_all=True)`, the log file shows corruption across dozens of sections:
- Repeated `- **Sources**: ...` lines injected into historical entries
- Section headers (`## [YYYY-MM-DD]`) replaced or duplicated
- Entire entry narratives spliced with content from other dates

The diff shows 50+ changes across the file when only 1 was intended.

## Root Cause

Patterns that appear in a single `new_string` (e.g., `- **Sources**: blog triage checkpoint 20260601T071331Z`) may also appear as fragments in many historical entries. With `replace_all=True`, EVERY occurrence is replaced — not just the target insertion point.

Common matching patterns that cause this:
- `- **Sources**: blog triage checkpoint...` — appears in every ingestion log entry
- `## [YYYY-MM-DD] wiki-ingest` — a common header prefix appears on many dates
- `---` — section separator used hundreds of times
- `--` — em-dash in article titles, appears everywhere

## Recovery

The only safe recovery is `git checkout`:

```bash
cd /opt/data/ai-topics
git checkout -- wiki/log.md
```

Do NOT try to fix in-place via further `patch` calls — the corruption is too widespread and compound replacements will cascade.

## Prevention

1. **Never use `replace_all=True` on log.md** — The log is structured with repetitive patterns that match across dozens of entries.
2. If `patch` returns "Found N matches" (N > 1), **do NOT use replace_all**. Instead:
   - Use a more specific multi-line `old_string` (include 2-3 surrounding lines)
   - Or switch to the Python script pattern: write script to `/tmp/`, run via `terminal("python3 /tmp/script.py")`
3. **Preferred approach for log.md mutations**: Always use the header/chronological-split Python pattern (read lines, find first `## [YYYY-MM-DD]` entry, insert after header block, write back). This is safe and precise.

## Python Script Pattern (Safe Alternative)

```python
path = "/opt/data/ai-topics/wiki/log.md"
with open(path) as f:
    lines = f.readlines()

# Find first non-backtick chrono entry
chrono_start = None
for i, line in enumerate(lines):
    if line.startswith('## [') and not line.startswith('> '):
        chrono_start = i
        break

# Insert new entry after header block
header = lines[:chrono_start]
chrono = lines[chrono_start:]
new_entry = ["## [2026-06-01] entry | subject\n", "\n", ...]

with open(path, 'w') as f:
    f.writelines(header + new_entry + ["\n", "---\n", "\n"] + chrono)

# Verify
with open(path) as f:
    assert f.readline().strip() == '# Wiki Log'
```
