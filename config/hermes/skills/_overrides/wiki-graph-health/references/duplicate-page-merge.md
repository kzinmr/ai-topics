# Duplicate Page Merge Workflow

Procedure for detecting and merging duplicate wiki pages across namespaces (primarily entities/ ↔ concepts/).

## Detection Script

```python
#!/usr/bin/env python3
"""Find duplicate pages between entities/ and concepts/ namespaces."""
import os, re
from pathlib import Path
from collections import defaultdict

WIKI_ROOT = Path("/opt/data/ai-topics/wiki")

def normalize_name(name):
    if "/" in name:
        name = name.split("/")[-1]
    return re.sub(r'[-_]', '', name.lower())

def find_entity_concept_duplicates():
    pages = []
    for ns in ["entities", "concepts"]:
        ns_dir = WIKI_ROOT / ns
        if not ns_dir.exists():
            continue
        for md_file in ns_dir.rglob("*.md"):
            if md_file.name.startswith("_"):
                continue
            rel_path = md_file.relative_to(WIKI_ROOT)
            page_name = str(rel_path).replace(".md", "")
            pages.append((ns, page_name, md_file))

    groups = defaultdict(list)
    for ns, page_name, file_path in pages:
        groups[normalize_name(page_name)].append((ns, page_name, file_path))

    return {k: v for k, v in groups.items()
            if len({"entities", "concepts"} & {ns for ns, _, _ in v)}) == 2 and len(v) > 1}
```

## Pitfall: Doubled Namespace in `page_name`

**CRITICAL**: `str(rel_path).replace(".md", "")` returns `entities/apertus` (already namespaced). When constructing references, do NOT prepend the namespace again:

```python
# WRONG — produces [[entities/entities/apertus]]
old_ref = f"[[{ns}/{page_name}]]"

# CORRECT — page_name already includes namespace
old_ref = f"[[{page_name}]]"
```

This bug is silent: `content.replace(old_ref, new_ref)` simply finds no match, so index.md is not updated. The deletion (`file_path.unlink()`) still works because it uses the original `md_file` object, not the constructed path.

**Detection**: After merge, always run ghost entry detection to catch any stale references the script missed.

## Merge Strategy

1. **Sort by file size** (largest first) — keep the largest file per pair
2. **⚠️ PRESERVE CONTENT from deleted page** — BEFORE deleting, recover content from the deleted page and merge unique sections into the kept page. NEVER just delete the smaller file without merging.
3. **Delete smaller files** via `file_path.unlink()`
4. **Update index.md** references from deleted → kept page
5. **Re-run ghost detection** to verify no stale references remain
6. **Commit** with detailed message listing deleted files

### Content Preservation Procedure (CRITICAL)

**User correction (2026-07-05)**: The initial merge deleted 33 files without preserving content. The user explicitly required content preservation. All content was recovered via `git show` and merged properly (+1,439 lines recovered across 28 pairs).

**Technique**: Section-level dedup merge:
1. Parse both files into sections (split on `##`/`###` headers)
2. Identify sections in the deleted file NOT present in the kept file (by header text)
3. Append unique sections to the kept file
4. If no section-level differences, fall back to line-level dedup (skip lines already in kept file, append unique lines under a `## Merged Content` header)

```python
def parse_sections(content):
    """Parse markdown into sections (h2/h3 boundaries)."""
    lines = content.split('\n')
    sections = []
    current_header = None
    current_lines = []
    for line in lines:
        if re.match(r'^##\s', line) or re.match(r'^###\s', line):
            if current_header is not None:
                sections.append((current_header, '\n'.join(current_lines)))
            current_header = line
            current_lines = []
        else:
            current_lines.append(line)
    if current_header is not None:
        sections.append((current_header, '\n'.join(current_lines)))
    return sections

def merge_content(deleted_content, kept_content):
    """Merge unique sections from deleted into kept."""
    deleted_sections = parse_sections(deleted_content)
    kept_section_headers = set(h.strip() for h, _ in parse_sections(kept_content))
    
    unique_sections = []
    for header, body in deleted_sections:
        if header.strip() not in kept_section_headers:
            if body.strip() and len(body.strip()) > 20:
                unique_sections.append((header, body))
    
    if unique_sections:
        merge_block = "\n"
        for header, body in unique_sections:
            merge_block += f"\n{header}{body}\n"
        return kept_content.rstrip() + merge_block
    
    # Fallback: line-level dedup
    m = re.match(r'^---\n.*?\n---\n', deleted_content, re.DOTALL)
    if m:
        deleted_content = deleted_content[m.end():]
    deleted_lines = deleted_content.strip().split('\n')
    kept_lines_set = set(l.strip() for l in kept_content.split('\n') if l.strip())
    unique_lines = [l for l in deleted_lines if l.strip() and l.strip() not in kept_lines_set and len(l.strip()) > 10 and l.strip() not in ('---', '...', '===')]
    
    if unique_lines and len(unique_lines) >= 3:
        return kept_content.rstrip() + "\n\n## Merged Content (from deleted duplicate)\n\n" + '\n'.join(unique_lines)
    return None  # Nothing unique to merge
```

**Recovery from git** (if content was already deleted without merging):
```bash
# Recover deleted file content from parent commit
git show PARENT_COMMIT:path/to/deleted/file.md > /tmp/deleted_content.md
```

### Post-Merge Ghost Detection

After deleting duplicate files, ALWAYS check index.md for stale references the script missed:

```bash
cd ~/ai-topics && python3 -c "
import os, re
wiki_base = '/opt/data/ai-topics/wiki'
with open(f'{wiki_base}/index.md') as f:
    content = f.read()
ghost = []
for m in re.finditer(r'- \[\[([^\]]+)\]\]', content):
    target = m.group(1).split('|')[0].strip()
    if target.startswith(('entities/', 'concepts/', 'comparisons/', 'queries/', 'events/')):
        target_clean = re.sub(r'\.md$', '', target)
        if not os.path.exists(f'{wiki_base}/{target_clean}.md'):
            ghost.append(target_clean)
print(f'Ghost entries: {len(ghost)}')
for g in ghost:
    print(f'  {g}')
"
```

## Post-Merge Verification

```bash
cd ~/ai-topics && python3 -c "
import os, re
wiki_base = '/opt/data/ai-topics/wiki'
with open(f'{wiki_base}/index.md') as f:
    content = f.read()
ghost = []
for m in re.finditer(r'- \[\[([^\]]+)\]\]', content):
    target = m.group(1).split('|')[0].strip()
    if target.startswith(('entities/', 'concepts/', 'comparisons/', 'queries/', 'events/')):
        target_clean = re.sub(r'\.md$', '', target)
        if not os.path.exists(f'{wiki_base}/{target_clean}.md'):
            ghost.append(target_clean)
print(f'Ghost entries: {len(ghost)}')
for g in ghost:
    print(f'  {g}')
"
```

## Merge Decision Matrix

| Scenario | Action |
|----------|--------|
| entities/ = person, concepts/ = their framework/tool | **Keep both** — different types |
| Both are stubs (< 500 bytes) | **Keep entities/**, delete concepts/ |
| One is rich, one is stub | **Keep richer** |
| Both are substantial (> 1KB) | **Keep larger**, review for unique content in smaller to transfer |
| naming variant (e.g., `martinfowler` vs `martin-fowler`) | **Keep canonical name**, delete variant |

## Session Example (2026-07-05)

33 entity-concept duplicate pairs merged. Key cases:
- `concepts/openclaw` (3.9KB) → kept `entities/openclaw` (17.6KB)
- `entities/dspy` (5.3KB) → kept `concepts/dspy` (12.7KB) — concept page was richer
- `concepts/agent-memory` (432B stub) → kept `entities/agentmemory` (9.9KB)
- One post-merge ghost fix needed: `entities/show-us-your-agent-skills` → `concepts/show-us-your-agent-skills`

**Content preservation (second pass)**: After initial merge deleted files without preserving content, recovered from git (`d4da1bff`) and merged unique sections. 28 of 33 pairs had unique content (+1,439 lines). 5 had fully overlapping content.
