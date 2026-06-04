# Wiki Lint Diagnostics

Working diagnostic scripts from the 2026-05-08 lint session. Run these during every lint to catch corruption early.

## 1. Index Corruption Detection

```python
import os
import re
from collections import defaultdict

WIKI = os.path.expanduser("~/ai-topics/wiki")
INDEX = os.path.join(WIKI, "index.md")

with open(INDEX) as f:
    index_lines = f.readlines()

# Count corruption types
corrupted = sum(1 for l in index_lines if re.match(r'^\s*\d+\|', l))
pipe_table = sum(1 for l in index_lines if l.strip().startswith('|-'))
clean = sum(1 for l in index_lines if l.strip() and not re.match(r'^\s*\d+\|', l) and not l.strip().startswith('|-'))

print(f"Index corruption report:")
print(f"  Total lines: {len(index_lines)}")
print(f"  Corrupted (line# prefix): {corrupted}")
print(f"  Pipe-table ('|- [['): {pipe_table}")
print(f"  Clean: {clean}")

# Check section headers
sections_clean = re.findall(r'(?<!\d\|)##\s+(.+)', ''.join(index_lines))
sections_corrupt = re.findall(r'^\s*\d+\|##\s+(.+)', ''.join(index_lines), re.MULTILINE)
print(f"  Clean section headers: {sections_clean}")
print(f"  Corrupted section headers: {sections_corrupt}")
```

## 2. File Count Verification

```python
import os
from collections import defaultdict

WIKI = os.path.expanduser("~/ai-topics/wiki")
INDEX = os.path.join(WIKI, "index.md")

# Count actual files
sections = defaultdict(int)
for root, dirs, files in os.walk(WIKI):
    if 'raw/' in root:
        continue
    for f in files:
        if f.endswith('.md') and f not in ('SCHEMA.md', 'index.md', 'log.md'):
            section = os.path.dirname(os.path.relpath(os.path.join(root, f), WIKI))
            sections[section if section else '(root)'] += 1

print("Actual file counts:")
for section, count in sorted(sections.items()):
    print(f"  {section}: {count}")

# Compare with index header
with open(INDEX) as f:
    index_content = f.read()

import re
header_total = re.search(r'Total pages:\s*(\d+)', index_content)
if header_total:
    actual_total = sum(sections.values())
    reported = int(header_total.group(1))
    print(f"\nDiscrepancy: header says {reported}, actual is {actual_total} (diff: {actual_total - reported})")
```

## 3. Broken Wikilink Detection

```python
import os
import re
from collections import defaultdict

WIKI = os.path.expanduser("~/ai-topics/wiki")

# Build case-insensitive page index
existing_pages = set()
for root, dirs, files in os.walk(WIKI):
    if 'raw/' in root:
        continue
    for f in files:
        if f.endswith('.md'):
            rel = os.path.relpath(os.path.join(root, f), WIKI)
            existing_pages.add(rel.lower().replace('.md', ''))
            existing_pages.add(f.lower().replace('.md', ''))

# Scan for broken links
broken = []
for root, dirs, files in os.walk(WIKI):
    if 'raw/' in root:
        continue
    for f in files:
        if f.endswith('.md') and f not in ('SCHEMA.md', 'index.md', 'log.md'):
            fpath = os.path.join(root, f)
            source = os.path.relpath(fpath, WIKI)
            with open(fpath, encoding='utf-8', errors='replace') as fh:
                content = fh.read()
            for m in re.finditer(r'\[\[([^\]]+)\]\]', content):
                link_text = m.group(1)
                target = link_text.split('|')[0].strip() if '|' in link_text else link_text.strip()
                if target.lower() not in existing_pages:
                    broken.append((source, target))

print(f"Broken wikilinks: {len(broken)}")
# Deduplicate and show top broken targets
from collections import Counter
target_counts = Counter(t for _, t in broken)
print(f"Unique broken targets: {len(target_counts)}")
print("Top 20 most-referenced broken targets:")
for target, count in target_counts.most_common(20):
    print(f"  [[{target}]] — {count} references")
```

## 4. Tag Taxonomy Audit

```python
import os
import re
from collections import Counter

WIKI = os.path.expanduser("~/ai-topics/wiki")
SCHEMA = os.path.join(WIKI, "SCHEMA.md")

# Extract schema tags
with open(SCHEMA) as f:
    schema_content = f.read()
schema_tags = set(re.findall(r'`([a-z][a-z0-9-]+)`', schema_content))

# Extract all used tags
all_tags = []
tag_files = 0
for root, dirs, files in os.walk(WIKI):
    if 'raw/' in root:
        continue
    for f in files:
        if f.endswith('.md'):
            fpath = os.path.join(root, f)
            with open(fpath, encoding='utf-8', errors='replace') as fh:
                content = fh.read(500)
            m = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if m:
                tag_files += 1
                fm = m.group(1)
                tags_m = re.search(r'tags:\s*\[(.*?)\]', fm, re.DOTALL)
                if tags_m:
                    tags = [t.strip().strip("'\"") for t in tags_m.group(1).split(',') if t.strip()]
                    all_tags.extend(tags)

tag_counts = Counter(all_tags)
undefined = set(all_tags) - schema_tags
one_off = sum(1 for c in tag_counts.values() if c == 1)
composite = [t for t in tag_counts if t.count('-') >= 3]

print(f"Tag audit:")
print(f"  Files with frontmatter: {tag_files}")
print(f"  Unique tags in use: {len(tag_counts)}")
print(f"  Tags in SCHEMA taxonomy: {len(schema_tags)}")
print(f"  Undefined tags: {len(undefined)}")
print(f"  One-off tags: {one_off}")
print(f"  Composite tags (3+ hyphens): {len(composite)}")
```

## 5. Index Section Completeness Check

```python
import os
import re

WIKI = os.path.expanduser("~/ai-topics/wiki")
INDEX = os.path.join(WIKI, "index.md")

with open(INDEX) as f:
    index_lines = f.readlines()

# Find all sections (including corrupted ones)
sections = {}
current_section = None
for i, l in enumerate(index_lines):
    # Match both clean and corrupted section headers
    m = re.search(r'##\s+(Entities|Concepts|Comparisons|Queries)', l)
    if m:
        current_section = m.group(1)
        sections[current_section] = {'start': i, 'entries': 0}
    elif current_section and ('- [[' in l or '|- [[' in l):
        sections[current_section]['entries'] += 1

print("Index section completeness:")
for section, info in sections.items():
    # Count actual files
    dir_path = os.path.join(WIKI, section.lower())
    if os.path.isdir(dir_path):
        actual = len([f for f in os.listdir(dir_path) if f.endswith('.md')])
    else:
        actual = 0
    print(f"  {section}: {info['entries']} entries in index, {actual} actual files")

# Check for missing sections
required = ['Entities', 'Concepts', 'Comparisons', 'Queries']
for section in required:
    if section not in sections:
        print(f"  MISSING: {section} section")
```

## Corruption Recovery Priority

When corruption is detected:
1. **index.md line-number corruption** — Most critical, affects 80%+ of lines at scale
2. **Missing section headers** — Comparisons/Queries often disappear
3. **Pipe-table corruption** — Secondary issue, 21 lines typically
4. **Tag taxonomy drift** — Grows exponentially, needs regular pruning

Use the `Git Merge Corruption Recovery` procedure from the main SKILL.md for log.md issues.
For index.md issues, the corruption is usually from `read_file` output being accidentally written back.
The fix requires careful removal of line number prefixes while preserving the actual content.
