# Wrong Section Header Detection

## Pattern
Entries in `index.md` with `[[concepts/` or `[[entities/` prefix appear under a section header they don't belong to. Most commonly: concept entries living under `## Events (N pages)` or `## Comparisons (N pages)`.

## Detection
```python
import re
section_clusters = {}
current_section = None
for line in open('wiki/index.md'):
    m = re.match(r'^## (\w+) \(\d+ pages\)', line)
    if m:
        current_section = m.group(1)
        section_clusters[current_section] = []
    elif line.startswith('- [[') and current_section:
        ns_m = re.match(r'- \[\[(\w+)/', line)
        if ns_m and ns_m.group(1) != current_section.lower():
            section_clusters[current_section].append((ns_m.group(1), line.rstrip()))
```

## Real-World Example (2026-05-26)
In `wiki/index.md`, the `## Events (6 pages)` section (line 1329) was followed by 21 concept entries:
- Lines 1330-1350: `[[concepts/chatgpt-memory-bitter-lesson]]` through `[[concepts/code-intelligence-for-llms]]`
- Line 1352 onwards: the actual 6 event entries with `[[events/` prefix

The 21 concept entries should have been in the Concepts section. This happened when batch-insertions landed at the Concepts/Events boundary but ended up on the wrong side of the section header.

## Fix
1. Read the full index.md
2. Identify the misplaced entries (wrong namespace prefix for the section)
3. Remove them from the wrong section
4. Determine insertion points in the correct section (alphabetical)
5. Insert using `execute_code` with Python batch insertion
6. Update section header counts
7. Verify with `validate_index.py`

### Python Fix Script
```python
import os, re

index_path = 'wiki/index.md'
with open(index_path) as f:
    lines = f.readlines()

# Find section boundaries
def find_section(lines, name):
    start = end = None
    for i, line in enumerate(lines):
        if re.match(f'^## {name} \(\\d+ pages\)', line):
            start = i
        elif start is not None and re.match(r'^## \w+ \(\d+ pages\)', line):
            end = i
            break
    return start, end

# Remove misplaced entries from Events section
ev_start, ev_end = find_section(lines, 'Events')
if ev_start:
    misplaced = []
    kept = [lines[ev_start]]  # keep the header
    for line in lines[ev_start+1:ev_end]:
        if line.startswith('- [[concepts/'):
            misplaced.append(line)
        else:
            kept.append(line)
    # Insert kept back, replacing the section
    lines[ev_start:ev_end] = kept
    
# Insert misplaced entries into Concepts section
con_start, con_end = find_section(lines, 'Concepts')

# Build alphabetical insertion helpers
def find_insertion(section_lines, entry_slug, prefix):
    for i, line in enumerate(section_lines):
        m = re.search(r'\[\[\w+/(' + re.escape(entry_slug.split('/')[-1])[:3] + ')', line)
        m2 = re.match(r'- \[\[\w+/([^\]|]+)', line)
        if m2 and entry_slug.lower() < m2.group(1).lower():
            return i
    return len(section_lines)

concept_section = lines[con_start+1:con_end]
for entry in misplaced:
    slug_match = re.match(r'- \[\[(\w+)/([^\]|]+)\]\]', entry)
    if slug_match:
        idx = find_insertion(concept_section, slug_match.group(2), slug_match.group(1))
        concept_section.insert(idx, entry)

# Rebuild concepts section
lines[con_start+1:con_end] = concept_section

with open(index_path, 'w') as f:
    f.writelines(lines)
```

## Verification
```bash
python3 scripts/validate_index.py
# Must pass with 0 issues
grep -c '^- \\[\\[concepts/' wiki/index.md
# Should match concept file count (not includes misplaced in other sections)
```

## Prevention
When inserting entries near section boundaries in `index.md`, always verify the 3-5 surrounding lines include the **correct** section header. A common mistake: reading `grep -n` output for the last concept entry, finding a line number near the Concepts/Events boundary, and inserting the new entry in the Events section instead. Use the section header as a directional anchor: if your insertion line is AFTER the Events header, you're in the wrong section.
