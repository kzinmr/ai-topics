# Sources Field Bulk Population

When `wiki-graph-analysis` reports pages missing the `sources:` frontmatter field (e.g., "684 pages (31%) missing sources"), bulk-add `sources: []` to all affected pages.

## Script

```python
#!/usr/bin/env python3
"""Add sources: [] to pages missing the field in YAML frontmatter."""
import os, re
from pathlib import Path

WIKI_ROOT = Path("/opt/data/ai-topics/wiki")
NAMESPACES = ["entities", "concepts", "comparisons", "queries", "events"]

def has_sources_field(content):
    m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not m: return False
    return bool(re.search(r'^sources:', m.group(1), re.MULTILINE))

def add_sources_field(content):
    m = re.match(r'^(---\n)(.*?)(\n---)', content, re.DOTALL)
    if not m: return content
    fm_start, fm_body, fm_end = m.group(1), m.group(2), m.group(3)
    # Insert after tags: line if present (maintains YAML field order)
    if re.search(r'^tags:', fm_body, re.MULTILINE):
        fm_body = re.sub(r'(^tags:.*$)', r'\1\nsources: []', fm_body, count=1, flags=re.MULTILINE)
    else:
        fm_body = fm_body.rstrip() + '\nsources: []'
    return fm_start + fm_body + fm_end + content[m.end():]

def main():
    fixed = 0
    for ns in NAMESPACES:
        ns_dir = WIKI_ROOT / ns
        if not ns_dir.exists(): continue
        for md_file in sorted(ns_dir.rglob("*.md")):
            try:
                with open(md_file) as f: content = f.read()
            except: continue
            if not content.startswith("---\n") or has_sources_field(content):
                continue
            new_content = add_sources_field(content)
            with open(md_file, 'w') as f: f.write(new_content)
            fixed += 1
    print(f"Fixed: {fixed} pages")

if __name__ == "__main__":
    main()
```

## Pitfalls

1. **Insertion point matters**: Place `sources:` after `tags:` (not before `title:`) to maintain conventional YAML field order: title → created → updated → type → tags → sources.

2. **Skip files without frontmatter**: Pages starting without `---` are not wiki pages (possibly raw content or index files).

3. **Scale**: Expect 100s–1000s of pages. The 2026-07-05 run fixed 752 pages. Commit in a single batch.

4. **Pre-commit hook**: The tag validator may emit warnings about Japanese content in already-translated files. This is a false positive — the script only adds `sources: []` which is English.

## Session Example (2026-07-05)

- Input: 684 pages missing `sources:` (31% of wiki)
- Output: 752 pages fixed (some pages had no frontmatter, so count differs slightly)
- Commit: single batch, 752 files changed, 752 insertions
