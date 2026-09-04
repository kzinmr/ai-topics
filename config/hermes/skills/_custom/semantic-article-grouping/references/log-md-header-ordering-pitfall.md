# log.md Header Ordering Pitfall After Prepend

## Observed (July 2026)

When prepending a new log entry to `log.md` via Python string concatenation:

```python
with open(log_path, 'r') as f:
    old_content = f.read()       # old_content[0] is '# Wiki Log\n\n...'
with open(log_path, 'w') as f:
    f.write(new_entry + old_content)  # new_entry starts with '## [2026-07-30]...'
```

The result is:

```
## [2026-07-30] Blog wiki ingest — ...
# Wiki Log
_Log of all wiki changes. Newest entries at top._
## [2026-07-29] ...  ← existing entries
```

The `# Wiki Log` header is now below the new entry, not at the top. This is structurally broken — the header should be line 1.

## Fix Options

### Option 1: Include header in new_entry (recommended)
Start `new_entry` with the full header + preamble:

```python
new_entry = """# Wiki Log

_Log of all wiki changes. Newest entries at top._

## [2026-07-30] Title here

...
"""
```

This ensures the header stays at line 1 regardless of what old_content contains.

### Option 2: Two-step (prepend then patch)
Prepend normally, then use `patch()` to swap:

```python
# Step 1: write with bad header position
# Step 2: patch to fix
patch(old_string="## [2026-07-30] ... \n# Wiki Log", 
      new_string="# Wiki Log\n\n_Log..._\n\n## [2026-07-30] ...")
```

### Option 3: Template-based (read body only)
Read old_content, strip the header lines, write header+new_entry+body:

```python
with open(log_path) as f:
    lines = f.readlines()
# Find where the first ## [date] entry starts (usually line 4-5)
first_entry_idx = next(i for i, l in enumerate(lines) if l.startswith('## ['))
header = ''.join(lines[:first_entry_idx])
body = ''.join(lines[first_entry_idx:])
with open(log_path, 'w') as f:
    f.write(header + new_entry + body)
```

## Which to Use

- **Cron mode** (write_file to /tmp/ + terminal): Option 1 is simplest — just include the full header in `new_entry`. Avoids tool restrictions.
- **Non-cron mode** (execute_code available): Option 3 is cleanest — explicitly separates header from body.
