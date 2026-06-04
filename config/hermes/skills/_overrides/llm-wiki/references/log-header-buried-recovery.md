# Log Header Buried Recovery

When `# Wiki Log` header is still present in log.md but buried at line N > 1 (e.g., line 37), it was caused by prepending content *before* the header block rather than inserting *after* it. This is a distinct failure from the "Missing `# Wiki Log` header" pitfall (where the header is deleted entirely).

## Detection

```bash
head -1 wiki/log.md
# Expected: '# Wiki Log'
# Bug symptom: '## [YYYY-MM-DD] ...' instead
```

```bash
grep -c '^# Wiki Log' wiki/log.md
# Must be exactly 1
```

```bash
grep -n '^# Wiki Log' wiki/log.md
# If line > 1, the header is buried
```

## Recovery Procedure (Buried Header)

When `# Wiki Log` exists but is NOT at line 1:

```python
log_path = "/opt/data/ai-topics/wiki/log.md"
with open(log_path) as f:
    all_lines = f.readlines()

# Find where # Wiki Log header lives
for i, line in enumerate(all_lines):
    if line.strip() == "# Wiki Log":
        header_line = i
        break

# Everything before # Wiki Log = misplaced content (prepended entry + separator)
misplaced = all_lines[:header_line]
# Everything from # Wiki Log onward = header + original chrono entries
rest = all_lines[header_line:]

# Find the first chronological ## [ or ## YYYY entry IN rest to separate header from chrono
first_chrono = None
for i, line in enumerate(rest):
    if line.startswith('## ['):
        first_chrono = i
        break
    if line.startswith('## ') and len(line) > 5 and line[3:7].isdigit():
        first_chrono = i
        break

# header_part = just the # Wiki Log block
header_part = rest[:first_chrono]
# old_entries = the original chronological entries
old_entries = rest[first_chrono:]

# Reconstruct: header → new entry → separator → old entries
final = list(header_part)
# Ensure blank line after header
if final[-1].strip() != '':
    final.append('\n')

# Add the misplaced content as a proper chrono entry (skip stray separators)
for line in misplaced:
    clean = line.rstrip('\n')
    if clean == '---' and final and final[-1].strip() == '':
        continue  # skip separator that was at boundary
    final.append(line)
if final[-1][-1] != '\n':
    final[-1] += '\n'

# Add separator and old entries
final.append('\n---\n\n')
final.extend(old_entries)

with open(log_path, 'w') as f:
    f.writelines(final)

# Verify
with open(log_path) as f:
    first_line = f.readline()
assert first_line.strip() == '# Wiki Log', f"Header still buried: {first_line.strip()}"
print(f"Recovered: # Wiki Log at line 1, {len(final)} total lines")
```

## Prevention

Always insert AFTER the `# Wiki Log` header block — never prepend before it.
Also guard against the backtick-wrapped `## [` in the `> Format:` metadata line — it is NOT a real chronological entry.

```python
# WRONG — buries the header AND matches Format line as false positive chrono
with open(path) as f: content = f.read()
with open(path, 'w') as f:
    f.write(new_entry + content)  # Header ends up at line 3+

# WRONG — matches backtick-wrapped ## [ in Format metadata line
chrono_start = content.find("## [")  # Matches first occurrence, inside > Format: `## [...]

# RIGHT — insert after header, skip Format line
with open(path) as f: lines = f.readlines()
chrono_start = None
for i, l in enumerate(lines):
    # ⚠️ Skip > Format: `## [YYYY-MM-DD] action | subject` — not a real entry
    if l.startswith('## ['):  
        chrono_start = i
        break
    # Also handles ## YYYY-MM-DD format
    if l.startswith('## ') and len(l) > 5 and l[3:7].isdigit():
        # Double-check: skip > blockquote lines (Format metadata)
        if i > 0 and lines[i-1].strip().startswith('>'):
            continue
        chrono_start = i
        break
if chrono_start is None:
    # Fallback: find first ## line that isn't Format metadata
    for i, l in enumerate(lines):
        if l.startswith('## ') and not l.strip().startswith('> `##'):
            chrono_start = i
            break
header_block = lines[:chrono_start]
chrono_entries = lines[chrono_start:]
result = header_block + new_entry_lines + ['\n---\n\n'] + chrono_entries
with open(path, 'w') as f: f.writelines(result)

# Verify both header position AND Format line integrity
with open(path) as f:
    lines_4 = [f.readline() for _ in range(4)]
assert lines_4[0].strip() == '# Wiki Log', f"Header buried: {lines_4[0].strip()}"
# Line 4 (index 3) should be complete Format line, not truncated
assert 'Format:' not in lines_4[3] or '`##' in lines_4[3], f"Format line truncated: {lines_4[3].strip()}"
```

## Contrast with "Missing Header" (Deleted)

If `grep -c '^# Wiki Log'` returns 0 (header was deleted, not buried), use the recovery in the SKILL.md "Missing # Wiki Log header" pitfall instead: a large `patch` that inserts the header block + your entry before the first `## [YYYY-MM-DD]` entry.
