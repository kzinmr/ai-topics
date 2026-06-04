---
name: wiki-page-splitting
category: wiki
description: "Split large wiki entity/concept pages (300-544 lines) into main overview (under 200 lines) + sub-pages, following established naming conventions. Use when a health check reports pages over the 200-line threshold."
---

# Wiki Page Splitting

Split large (`wc -l > 200`) wiki pages into a concise main page with wikilink cross-references to sub-pages.

## When to Use

- A wiki-health check reports **pages over 200 lines** that need splitting
- Someone says "this entity/concept page is too long"
- You manually notice `wc -l > 300` on a content page (not `_index.md`, `log.md`, or `index.md` which are intentionally large)

## Naming Convention

Use **`entity-name--subsection.md`** (double-hyphen separator):

| Original | Sub-page |
|----------|----------|
| `entities/andrej-karpathy.md` | `entities/karpathy-projects.md`, `entities/karpathy-ideas.md` |
| `entities/boris-cherny.md` | `entities/boris-cherny--core-ideas.md` |

For sub-pages with many entries (Omar Khattab's publications), use a **subdirectory**:

| Main | Sub-page |
|------|----------|
| `entities/omar-khattab.md` | `entities/omar-khattab/rlm.md`, `entities/omar-khattab/dspy.md` |

## Identification Heuristic

Common splittable subsections in entity pages:
- **Timeline / Career History** → `entity-name--timeline.md`
- **Core Ideas / Philosophy** → `entity-name--core-ideas.md`
- **Projects / Key Work** → `entity-name--projects.md` or `entity-name--key-work.md`
- **Writings / Blog Posts** → `entity-name--writings.md`
- **Quotes** → `entity-name--quotes.md`
- **Sources** → `entity-name--sources.md`
- **Specific sub-topics** (e.g., `Instructor` library in Jason Liu) → `entity-name--instructor.md`

For concept pages:
- **Architecture** → `concept-name-architecture.md`
- **Modules / Components** → `concept-name-modules.md`
- **Optimization** → `concept-name-optimization.md`
- **Comparisons** → `concept-name-comparisons.md`
- **Theory** → `concept-theory.md`
- **Patterns** → `concept-patterns.md`
- **Tool Support** → `concept-tool-support.md`

## Sub-page Frontmatter Pattern

Each sub-page gets proper YAML frontmatter:

```yaml
---
title: "Andrej Karpathy — Projects"
type: entity
parent: andrej-karpathy
tags: [karpathy, projects, llm]
status: active
created: 2026-04-27
updated: 2026-04-27
sources:
  - url: https://github.com/karpathy
```

- `parent:` field links back to the main page
- `type:` matches the original page type
- Remove `status: skeleton` when enrichment is done

## Main Page Rewrite Pattern

After extracting sub-pages, rewrite the main page to:

1. **Keep**: YAML frontmatter, bio overview, info table, key metrics summary, comparisons, related wikilinks, sources
2. **Add**: A `## Sub-Pages` section with wikilink references:
   ```markdown
   ## Sub-Pages
   - [[entities/karpathy-projects|Projects & Repositories]] — llm.c, NanoGPT, etc.
   - [[entities/karpathy-ideas|Core Ideas & Philosophy]]
   ```
3. **Use inline wikilinks** in the overview text:
   ```markdown
   His [[entities/karpathy-projects|projects]] include llm.c, while his
   [[entities/karpathy-ideas|core ideas]] emphasize the Bitter Lesson.
   ```
4. Target: **under 200 lines** (preferably 80-150)

## Backlink Pattern

Every sub-page should have a backlink at the top:

```markdown
> Back to main profile: [[andrej-karpathy]]
```

And a `## See Also` section linking to sibling sub-pages:

```markdown
## See Also
- [[entities/karpathy-ideas|Core Ideas & Philosophy]]
- [[entities/karpathy-projects|Projects]]
```

## Verification

After splitting, verify:

```bash
cd ~/ai-topics/wiki
# Check no main page exceeds 200 lines
for f in entities/andrej-karpathy.md entities/jason-liu.md; do
  echo "$(wc -l < $f) $f"
done

# Check no broken wikilinks introduced
python3 -c "
import os, re
from collections import Counter

valid_targets = set()
for root, dirs, files in os.walk('.'):
    if 'raw' in root or '.git' in root: continue
    for f in files:
        if not f.endswith('.md'): continue
        slug = os.path.splitext(os.path.relpath(os.path.join(root, f), '.'))[0]
        valid_targets.add(slug)

broken = Counter()
wikilink_re = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')
for root, dirs, files in os.walk('.'):
    if 'raw' in root or '.git' in root: continue
    for f in files:
        if not f.endswith('.md'): continue
        path = os.path.join(root, f)
        try:
            content = open(path, errors='ignore').read()
        except: continue
        for m in wikilink_re.finditer(content):
            target = m.group(1).strip()
            if target not in valid_targets and not target.startswith('http'):
                broken[target] += 1

print(f'Broken: {len(broken)} unique, {sum(broken.values())} instances')
for t, n in broken.most_common(10):
    print(f'  [[{t}]] — {n}x')
"
```

## Parallel Execution Strategy

For splitting 10+ pages efficiently, use `delegate_task` with batch processing (max 3 tasks per batch):

```python
# Send 3 pages per batch to delegate_task
tasks = [
    {"goal": "Split entities/andrej-karpathy.md ...", "toolsets": ["terminal", "file"]},
    {"goal": "Split entities/jason-liu.md ...", "toolsets": ["terminal", "file"]},
    {"goal": "Split entities/mitchell-hashimoto.md ...", "toolsets": ["terminal", "file"]},
]
```

## Common Pitfalls

- **Sub-pages don't exist yet** — create them from scratch using `write_file`; don't try to rename existing files
- **Frontmatter `type:` field** — must match original (entity/page stays `type: entity`, concept stays `type: concept`)
- **`_index.md` files are intentionally large** — skip them (they're directory indexes)
- **`log.md`, `log-2026.md` are intentionally large** — skip them (they're change logs)
- **`index.md` is intentionally large** — skip it (it's the main wiki index)
- **Don't lose content** — every line of the original page must be preserved across the sub-pages
- **Backlinks matter** — each sub-page needs a link back to the main page so the graph isn't orphaned
- **Cross-links between sub-pages** — connect sibling sub-pages to each other in See Also sections
