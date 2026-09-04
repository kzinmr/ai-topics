# Batch Orphan Insertion Pitfalls (2026-06-28 session)

## Background

The Python batch insertion pattern (Approach B in Section A4c) inserts entries into a sorted working copy, then inserts back into the main `lines` array using bottom-up indexing. This session revealed two significant bugs.

## Bug 1: Insertion Index Out of Bounds

**Symptom**: New entries appear at random positions instead of at the correct alphabetical location within the section. They may end up interleaved with existing entries from other sections or after `## Events`.

**Root cause**: The `find_alphabetical_insertion` function returns an index relative to the working copy size, but when entries should sort AFTER all existing entries (e.g., comparisons starting with 'l' or 'o' when existing entries go only up to 'h'), the returned index exceeds the original section bounds. When used with `lines.insert(comp_start + idx, ...)`, this index can be larger than the current lines array length, causing Python's `list.insert(n, x)` to append at the end (which may be past `## Events`).

**When it happens**: Any batch where new slugs sort AFTER all existing entries in the section. For example, adding `llm-*` or `open-*` entries to a section that only goes up to `hermes-*` alphabetically.

**Fix**: After the batch insertion, sort the entire section by slug:

```python
# Instead of computing individual insertion points, insert all at the end
# then sort the whole section
comp_section = lines[comp_start:comp_end]
# Remove entries from main lines
del lines[comp_start:comp_end]
# Rebuild with sorted entries
header_line = comp_section[0]  # blank after ## Comparisons header
old_entries = comp_section[1:]  # skip blank
all_entries = old_entries + new_entries
all_entries.sort(key=lambda e: extract_slug(e))
new_section = [header_line] + all_entries
# Insert back into lines
for i, entry in enumerate(new_section):
    lines.insert(comp_start + i, entry)
```

## Bug 2: `(N pages)` vs `(Updated)` Header Format

**Symptom**: The batch script tries to update `## Concepts (N pages)` but the actual header uses `## Concepts (Updated)`. The `re.match(r'^## Concepts \((\d+) pages\)')` silently returns None, and the count is never updated.

**Fix**: Before updating, check the actual header format:

```python
import re
for i, line in enumerate(lines):
    m_count = re.match(r'^## Concepts \((\d+) pages\)', line)
    m_updated = re.match(r'^## Concepts \((Updated)\)', line)
    if m_count:
        lines[i] = f'## Concepts ({int(m_count.group(1)) + N} pages)'
    elif m_updated:
        # No count to update — header is self-maintaining
        pass
```

## Safer Alternative: Sort-Entire-Section Approach

Instead of computing individual insertion points (which can go out of bounds), use this approach:

1. Isolate the section (including blank line after header + all entries)
2. Add new entries as raw strings
3. Sort ALL entries by extracted slug
4. Reconstruct the section
5. Replace in main lines

This avoids the index bounds issue entirely and guarantees alphabetical order regardless of how many entries are added or what their slugs are.
