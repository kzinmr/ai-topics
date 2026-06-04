# Wiki Bulk Link Fix

Large-scale wikilink auditing and fixing.

## Phase 1: Analyze
```python
import os, re
wikilink_re = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')
valid = set()
for root, dirs, files in os.walk('.'):
    if 'raw' in root.split(os.sep): continue
    for f in files:
        if f.endswith('.md'):
            rel = os.path.relpath(os.path.join(root, f), '.')
            if '_index.md' in rel: t = rel.replace('/_index.md', '')
            else: t = re.sub(r'^(entities|concepts)/', '', rel); t = re.sub(r'\.md$', '', t)
            valid.add(t)
```

## Phase 2: Categorize
| Category | Pattern | Fix Strategy |
|----------|---------|--------------|
| entities/ prefix | `[[entities/samuel-colvin]]` | Strip prefix |
| concepts/ prefix | `[[concepts/agentic-engineering]]` | Strip prefix |
| Case sensitivity | `[[Anthropic]]` vs `[[anthropic]]` | Normalize |
| Relative paths | `[[../agentic-engineering]]` | Resolve |
| _index links | `[[harness-engineering/_index]]` | → `[[harness-engineering]]` |

## Phase 3: Fix by Category
Prefix stripping: `re.sub(r'\[\[entities/', '[[', content)`
_index normalization: `re.sub(r'\[\[([^\]]*/_index)\]\]', lambda m: '[[' + m.group(1).replace('/_index', '') + ']]', content)`

## Phase 4: Stub Creation
For high-frequency missing pages where content exists in subdirectories:
```markdown
---
title: "Vibe Coding"
tags: [concept, harness-engineering]
status: skeleton
---
# Vibe Coding
> This stub redirects to [[harness-engineering/agentic-workflows/vibe-coding]].
```

## Key Findings
1. Prefix wikilinks are the biggest category (698 unique targets, 1381 instances)
2. Subdirectory/_index links common in nested concepts
3. Case sensitivity is rare (~7 unique after prefix fixes)
4. "Missing" pages often exist in subdirectories

## Cron Integration
Weekly: `0 2 * * 0 cd ~/ai-topics && python3 ~/scripts/run_wiki_link_audit.py`
