# wiki_health.py Performance Optimization (2026-05-13)

## Before: 3-5+ minutes (estimated)

```python
# load_l2_pages() — Read 1: frontmatter only, discard content
def load_l2_pages():
    for p in collect_md_files(d):
        fm = parse_frontmatter(p)  # reads file, parses YAML, discards text

# section_unprocessed_raw() — Read 2: re-read ALL files for substring search
def section_unprocessed_raw(l2, raw_articles):
    l2_content_parts = []
    for cat, pages in l2.items():
        for path, _ in pages:
            l2_content_parts.append(path.read_text(...))  # 2nd read!
    l2_blob = "\n".join(l2_content_parts)  # ~10MB string
    
    for raw_path in raw_articles:  # 5,868 iterations
        if raw_path.stem not in l2_blob:  # O(blob_size) linear search
            unprocessed.append(raw_path)
```

**Problems:**
- Double read of ~1,800 files
- O(N×M) substring search: 5,868 × 10MB = ~53 billion character comparisons

## After: 0.28 seconds (wall clock)

```python
# Single-pass read: frontmatter + full content retained
PageRecord = dict  # {path, fm, content, category, slug}

def load_l2_pages():
    for p in collect_md_files(d):
        text = p.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text)
        pages.append({"path": p, "fm": fm, "content": text, ...})

# Set-based reference extraction
def _build_referenced_stems(l2) -> set[str]:
    stems = set()
    for rec in l2_pages:
        content = rec["content"]
        for prefix in ("raw/articles/", "articles/"):
            idx = 0
            while True:
                idx = content.find(prefix, idx)
                if idx == -1: break
                # Extract stem after prefix
                start = idx + len(prefix)
                end = start
                while end < len(content) and content[end] not in (" ", "\n", ")", "]", "|", ">"):
                    end += 1
                ref = content[start:end]
                if ref.endswith(".md"):
                    ref = ref[:-3]
                if ref:
                    stems.add(ref)
                idx = end
    return stems

# O(1) set lookup instead of O(N) substring search
referenced = _build_referenced_stems(l2)
for raw_path in raw_articles:
    if raw_path.stem not in referenced:  # O(1) set membership
        unprocessed.append(raw_path)
```

**Key improvements:**

| Metric | Before | After |
|--------|--------|-------|
| File reads | 2× per page (~3,600) | 1× per page (~1,800) |
| Unprocessed check | O(N×M) substring | O(1) set lookup |
| Wall time | ~minutes | 0.28s |
| Memory | 2× peak (discard+re-read) | 1× peak (retain) |

## General Pattern: Single-Pass Read + Set-Based Matching

Applicable to any script that:
1. Iterates files to extract structured data
2. Later needs file content for cross-referencing

```python
# Read once, keep everything
records = []
for path in files:
    text = path.read_text()
    fm = parse_frontmatter(text)
    records.append({"path": path, "fm": fm, "content": text})

# Build lookup structures from retained data
refs = build_set(records)  # extract from .content, not re-read

# O(1) lookups
for item in items:
    if item in refs:
        ...
```
