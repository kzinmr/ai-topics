# Log Rotation Procedure

## When to Rotate

`log.md` should be rotated when it exceeds 500 entries or ~1000 lines. The daily lint check should include this verification.

## Rotation Procedure

```bash
# 1. Archive the current log
mv ~/ai-topics/wiki/log.md ~/ai-topics/wiki/log-YYYY.md

# 2. Initialize a fresh log with the standard header
cat > ~/ai-topics/wiki/log.md << 'EOF'
# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [YYYY-MM-DD] rotate | Rotated log-YYYY.md (N lines → log-YYYY.md archived)
- Previous entries archived to log-YYYY.md
- Fresh log.md initialized

---

EOF

# 3. Add rotation entry to the archived log (before it was moved)
# This is done by appending to the old file before moving, or by editing after

# 4. Commit both files
cd ~/ai-topics && git add wiki/log.md wiki/log-YYYY.md && git commit -m "chore: rotate log.md (N lines → log-YYYY.md)" && git push
```

## Post-Rotation Verification

- Confirm `log.md` starts with the correct header and has the rotation entry
- Confirm `log-YYYY.md` contains all previous entries
- Verify the archive file is properly tracked in git
- Update any scripts that read the last N lines of log.md (they now read the fresh file)

## Automated Rotation via Cron

The daily lint check should include a line count check:

```python
import os

log_path = "/opt/data/ai-topics/wiki/log.md"
with open(log_path) as f:
    lines = f.readlines()

if len(lines) > 500:
    # Trigger rotation
    from datetime import datetime
    year = datetime.now().year
    archive_path = f"/opt/data/ai-topics/wiki/log-{year}.md"
    
    # Move current to archive
    os.rename(log_path, archive_path)
    
    # Create fresh log with header + rotation entry
    with open(log_path, 'w') as f:
        f.write(f"""# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [{datetime.now().strftime('%Y-%m-%d')}] rotate | Rotated log-{year}.md ({len(lines)} lines → archived)
- Previous entries archived to log-{year}.md
- Fresh log.md initialized

---

""")
```

## Common Pitfalls

- **Don't forget the `---` separator** at the end of the rotation entry
- **Always commit both files** in the same commit to maintain git history continuity
- **Update the archived log** with the rotation entry before moving (or append to the new log after)
- **Yearly rotation**: If a log-YYYY.md already exists for the current year, append to it rather than creating a new file

### Duplicate Header After Rotation (Known Failure Mode)

**Symptom**: Fresh `log.md` contains two copies of the header block:

```
# Wiki Log
...
## [2026-05-09] rotate | ...
---
# Wiki Log   <-- SECOND COPY
...
## [2026-05-09] rotate | ...  <-- SECOND COPY
```

**Cause**: The rotation process writes the header + rotate entry + `---` separator as the fresh file content, and then **appends** another full copy of the header + rotate entry. The result is a stacking: fresh content → `---` → duplicate header → duplicate rotate entry → legit next entry.

**Detection**: `grep -c "^# Wiki Log" wiki/log.md` — if >1, duplicates exist. **⚠️ Do NOT use `str.count('# Wiki Log')`** — the string can appear in log entry body text (e.g., "Removed duplicate `# Wiki Log` header"), producing false count of 3+ when only 1 real header exists. The `grep -c` regex with `^` anchor is the correct approach.

**Fix**: Remove the second copy of the header block (everything from the second `# Wiki Log` through its matching rotate entry). Verify with `grep -c "^# Wiki Log"` → must return 1.

```python
import re
with open("wiki/log.md") as f:
    content = f.read()

# Find all occurrences of the header
lines = content.split('\n')
header_indices = [i for i, l in enumerate(lines) if l == '# Wiki Log']

if len(header_indices) > 1:
    # Keep lines before the second header
    content = '\n'.join(lines[:header_indices[1]])
    with open("wiki/log.md", 'w') as f:
        f.write(content.strip() + '\n')
    print(f"Removed duplicate header block (lines {header_indices[1]}-{len(lines)})")
```

**Post-fix verification**: 
1. `grep -c "^# Wiki Log" wiki/log.md` → 1
2. `grep "^## \\[" wiki/log.md | head -3` — first entry should be the rotate entry
3. No blank lines immediately after the rotate entry's `---` separator
