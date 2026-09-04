# Log.Header Two-Step Failure Trap (2026-07-25)

## Discovery

After a successful `# Wiki Log` header burial fix (restoring the header from line 762 to line 1),
a subsequent log-entry prepend immediately buried it again. The same mistake happened **twice
in the same session** — first during the initial run, then again during recovery from backup.

## Root Cause

The `# Wiki Log` header restoration and the new log entry write are **two separate operations**.
After restoring the header to line 1, the natural next step is to add a log entry documenting
the fix. But `f.write(new_entry + content)` **prepends** the entry before the header, pushing
`# Wiki Log` below.

## Mandatory Prevention

After **every** log.md modification, run:

```bash
head -1 ~/wiki/log.md | grep -q '^# Wiki Log' || echo "⚠️ HEADER BURIED"
```

## Mandatory Safety Net

Before any log.md modification:

```python
import shutil
shutil.copy2(log_path, log_path + '.bak')
```

## Recovery If Header Gets Buried Again

```python
import shutil, os
log_path = os.path.expanduser("~/ai-topics/wiki/log.md")
bak_path = log_path + '.bak'
if os.path.exists(bak_path):
    shutil.copy2(bak_path, log_path)
    print("Restored from backup")
```

Then redo the insertion **after** the header, not with a prepend.

## Correct Insertion Pattern (Insert After Header)

```python
log_path = os.path.expanduser("~/ai-topics/wiki/log.md")
with open(log_path) as f:
    content = f.read()

lines = content.split('\n')

# Find the header
header_idx = None
for i, line in enumerate(lines):
    if line.rstrip() == '# Wiki Log':
        header_idx = i
        break

# Find the first entry after header block
first_entry_idx = None
for i in range(header_idx + 1, len(lines)):
    if lines[i].startswith('## ['):
        first_entry_idx = i
        break

# Split: header block, rest
header_block = lines[:first_entry_idx]
rest = lines[first_entry_idx:]

# New entry (use the correct format)
new_entry = [
    "## [YYYY-MM-DD] action | title",
    "",
    "- [FIX] Description of fix",
    "",
    "---",
    "",
]

result = '\n'.join(header_block) + '\n' + '\n'.join(new_entry) + '\n'.join(rest)
with open(log_path, 'w') as f:
    f.write(result)

# IMMEDIATE VERIFICATION
with open(log_path) as f:
    first = f.readline().rstrip()
assert first == '# Wiki Log', f"First line is now: [{first}]"
```
