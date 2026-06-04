# Duplicate Cron Log Entry Recovery

When cascading `execute_code` log.md prepend attempts produce 3+ identical watchdog entries.

## Root Cause

The recommended alternative to `patch` is `execute_code` with Python `with open()`. But this pattern has its own failure cascade:

1. **First write**: `f.write(new_entry + content)` — buries the `# Wiki Log` header
2. **Recovery attempt**: Tries to find `# Wiki Log` at its new position and reconstruct — but the corrupted content is still in the file, so the reconstruction produces 1 good + 2 duplicate entries
3. **Result**: 3 identical log entries from 3 write attempts

## Detection

```bash
grep -c "watchdog |\|active-crawl\|enrich |" ~/wiki/log.md
# If count > expected, check for duplicates

# Find a specific entry and count occurrences
grep -c "specific action description" ~/wiki/log.md
```

Or scan for any duplicated entry header:

```python
import re
from collections import Counter

with open("~/wiki/log.md") as f:
    content = f.read()

# Find all ## [YYYY-MM-DD] headers
headers = re.findall(r'^## (?:\[)?\d{4}-\d{2}-\d{2}.*', content, re.MULTILINE)
dups = {h: c for h, c in Counter(headers).items() if c > 1}
print(f"Found {len(dups)} duplicate headers:")
for h, c in dups.items():
    print(f"  {c}x: {h}")
```

## Recovery Procedure

1. **Find all duplicate entry positions**:
```python
log_path = "~/wiki/log.md"
with open(log_path) as f:
    lines = f.readlines()

dup_indices = []
for i, line in enumerate(lines):
    if "unique entry identifier" in line:  # e.g., "watchdog | Auto-fix"
        dup_indices.append(i)
```

2. **Keep the first, remove subsequent duplicates**:
```python
indices_to_remove = set()
for idx in dup_indices[1:]:  # Skip the first
    j = idx
    while j < len(lines):
        if j > idx and lines[j].startswith('## ['):
            break
        indices_to_remove.add(j)
        j += 1

# Remove bottom-up
for idx in sorted(indices_to_remove, reverse=True):
    lines.pop(idx)

with open(log_path, 'w') as f:
    f.writelines(lines)
```

3. **Verify**:
```python
remaining = [i for i, l in enumerate(lines) if "unique entry identifier" in l]
assert len(remaining) == 1, f"Expected 1 entry, got {len(remaining)}"
print("✅ Dedup successful")
```

4. **Confirm header integrity**:
```bash
head -1 ~/wiki/log.md  # must be "# Wiki Log"
grep -c '^# Wiki Log' ~/wiki/log.md  # must be exactly 1
```

## Prevention

This pattern triggers when you use `f.write(new_entry + content)` in `execute_code` — it prepends before the header. Always use the **header/chrono splitting pattern** instead:

```python
with open(log_path) as f:
    lines = f.readlines()

# Find where chrono entries start (first ## [YYYY-MM-DD] or ## YYYY-MM-DD)
chrono_start = None
for i, line in enumerate(lines):
    if line.startswith('## ['):
        chrono_start = i
        break
    if line.startswith('## ') and len(line) > 5 and line[3:7].isdigit():
        chrono_start = i
        break

header_block = lines[:chrono_start]
chrono_entries = lines[chrono_start:]

# Build new entry
new_entry = ["## [YYYY-MM-DD] action | subject\n", "\n", "...\n", "\n", "---\n", "\n"]

# Insert AFTER header block
lines = header_block + new_entry + chrono_entries

with open(log_path, 'w') as f:
    f.writelines(lines)

# ALWAYS verify header is intact
assert open(log_path).readline().strip() == '# Wiki Log'
```

## Pitfall — Duplicate Check on the Same Content Pattern

If the duplicate entries are *identical* (same header, same body), the loop that removes subsequent copies works correctly because each entry occupies a contiguous block of lines. The key insight: each duplicate starts at position `dup_indices[N]` and extends to the next `## [` header or end-of-file.

If the duplicates are NOT identical (e.g., different sub-items under the same header), you may need manual inspection to determine which copy to keep and what content to merge.
