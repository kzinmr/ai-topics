# Large Index File Operations

## Problem
When `index.md` exceeds ~100KB (typically 1000+ pages), standard `patch` operations become unreliable:
- Token limits cause silent failures on read_file/write_file
- Line-number prefix corruption from pasting tool output
- Anchor line matching fails with subtle whitespace differences
- Header count math drifts over time (discrepancies of 100+ pages observed)

## Solution: Programmatic Python via execute_code

```python
import os
from pathlib import Path

WIKI = Path(os.path.expanduser("~/wiki"))
INDEX = WIKI / "index.md"

# 1. Find section boundaries
content = INDEX.read_text()
section_start = content.find(f"## {section_name}")
next_section = content.find("## ", section_start + 1)

# 2. Parse existing entries in section
section_text = content[section_start:next_section if next_section != -1 else None]
entries = [line for line in section_text.split('\n') if line.startswith('- [[')]

# 3. Insert new entry alphabetically
new_entry = f"- [[concepts/new-topic]] — description"
all_entries = sorted(entries + [new_entry], key=str.lower)

# 4. Rebuild and write
new_section = '\n'.join(all_entries)
new_content = content[:section_start] + new_section + content[next_section if next_section != -1 else len(content):]
INDEX.write_text(new_content)

# 5. Update header counts
# Count actual files, not relying on header numbers
total = len(list(WIKI.glob('entities/*.md'))) + len(list(WIKI.glob('concepts/*.md'))) + len(list(WIKI.glob('comparisons/*.md')))
# Patch just the count line
```

## Verification After Operations

```python
# Always verify file exists and is reasonable size
assert INDEX.exists()
assert INDEX.stat().st_size > 1000

# Verify entry count
actual_entries = content.count("- [[")
print(f"Total entries: {actual_entries}")
```

## When to Use This
- Active crawl sessions creating 5+ pages
- Any session where index.md exceeds 100KB (check: `wc -c ~/wiki/index.md`)
- When `search_files` returns unreliable results

## Pitfalls
- **Never use patch on files >50KB** — silent failures are common
- **Never paste read_file output** — line number prefixes corrupt markdown
- **Always verify counts** — header math drifts, verify with filesystem
- **Use absolute paths** — `~/wiki/index.md`, not relative paths in subagents
