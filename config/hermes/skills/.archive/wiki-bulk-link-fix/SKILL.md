---
name: wiki-bulk-link-fix
category: wiki
description: Large-scale wikilink auditing and fixing for wiki health maintenance
---

# Wiki Bulk Link Fix

Systematic approach to auditing and fixing broken wikilinks across the entire wiki.

## Workflow

### Phase 1: Analyze (always start here)
```python3
import os, re
wikilink_re = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')
valid = set()
for root, dirs, files in os.walk('.'):
    if 'raw' in root.split(os.sep): continue
    for f in files:
        if f.endswith('.md'):
            rel = os.path.relpath(os.path.join(root, f), '.')
            if '_index.md' in rel:
                t = rel.replace('/_index.md', '')
            else:
                t = re.sub(r'^(entities|concepts)/', '', rel)
                t = re.sub(r'\.md$', '', t)
            valid.add(t)

valid_lower = {v.lower(): v for v in valid}
broken = {}
for root, dirs, files in os.walk('.'):
    if 'raw' in root.split(os.sep): continue
    for f in files:
        if not f.endswith('.md'): continue
        path = os.path.join(root, f)
        try:
            content = open(path, 'r', errors='ignore').read()
        except: continue
        for m in wikilink_re.finditer(content):
            target = m.group(1).strip()
            if target not in valid:
                if target not in broken:
                    broken[target] = set()
                broken[target].add(path)
```

### Phase 2: Categorize

Brokne links fall into **5 distinct categories**, each requiring different fix strategy:

| Category | Pattern | Fix Strategy |
|----------|---------|--------------|
| **entities/ prefix** | `[[entities/samuel-colvin]]` | Strip prefix → `[[samuel-colvin]]` |
| **concepts/ prefix** | `[[concepts/agentic-engineering]]` | Strip prefix → `[[agentic-engineering]]` |
| **Case sensitivity** | `[[Anthropic]]` vs `[[anthropic]]` | Normalize to lowercase match |
| **Relative paths** | `[[../agentic-engineering]]` in subdir files | Resolve to absolute path |
| **Subdirectory/_index** | `[[harness-engineering/_index]]` | → `[[harness-engineering]]` |

**Truly missing** (no page exists):
- High-frequency (≥5 refs): Create stub page
- Low-frequency (<5 refs): Either create stub or leave for later
- **Raw article links** (link rot): Not fixable via wikilink changes — re-scrape or remove

### Phase 3: Fix by Category

**Prefix stripping (highest volume):**
```python3
# Strip entities/ prefix
for root, dirs, files in os.walk('.'):
    if 'raw' in root: continue
    for f in files:
        if not f.endswith('.md'): continue
        path = os.path.join(root, f)
        content = open(path).read()
        new = re.sub(r'\[\[entities/', '[[', content)
        if new != content:
            open(path, 'w').write(new)
```

**Subdirectory/_index normalization:**
```python3
for root, dirs, files in os.walk('.'):
    if 'raw' in root: continue
    for f in files:
        if not f.endswith('.md'): continue
        path = os.path.join(root, f)
        content = open(path, 'r', errors='ignore').read()
        new_content = re.sub(
            r'\[\[([^\]]*/_index)\]\]', 
            lambda m: '[[' + m.group(1).replace('/_index', '') + ']]', 
            content
        )
        if new_content != content:
            open(path, 'w').write(new_content)
```

### Phase 4: Stub Creation for Missing Pages

For high-frequency missing pages, create stub pages that **redirect to subdirectory content**:
```markdown
---
title: "Vibe Coding"
tags: [concept, harness-engineering]
status: skeleton
---

# Vibe Coding

> This stub redirects to [[harness-engineering/agentic-workflows/vibe-coding]].

See: [[harness-engineering]], [[agentic-engineering]]
```

**Pattern**: If content exists at `concepts/harness-engineering/agentic-workflows/vibe-coding.md` but links reference `[[vibe-coding]]`, create `concepts/vibe-coding.md` as a stub redirect.

## Key Findings

1. **Prefix wikilinks are the biggest category** — 698 unique targets (1,381 instances) from `entities/` and `concepts/` prefixes alone
2. **Subdirectory/_index links** are common in nested concepts (harness-engineering, inference, openclaw, etc.)
3. **Case sensitivity is rare** — only ~7 unique links after prefix fixes
4. **"Missing" pages often exist in subdirectories** — always check `concepts/[name]/` before creating stubs
5. **Raw article link rot is not fixable** via wikilink edits — requires re-scraping or link removal

## Verification

After fixing, re-run the analysis script to confirm:
```bash
python3 -c "
# ... same analysis code ...
print(f'Total broken: {len(broken)} unique, {sum(len(v) for v in broken.values())} instances')
print(f'Raw articles: {sum(len(v) for k,v in broken.items() if \"raw/\" in k)}')
"
```

## Cron Integration

Run weekly or after bulk wiki changes:
```
0 2 * * 0 cd ~/ai-topics && python3 ~/scripts/run_wiki_link_audit.py >> ~/logs/wiki-link-audit.log 2>&1
```

## Related Skills

- `wiki-graph-health` — entity deduplication and concept link gap detection
- `wiki-entity-dedup` — merge duplicate entity pages