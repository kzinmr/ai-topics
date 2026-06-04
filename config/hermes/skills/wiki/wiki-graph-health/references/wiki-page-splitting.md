# Wiki Page Splitting

Split large (`wc -l > 200`) wiki pages into a concise main page with wikilink cross-references to sub-pages.

## Naming Convention
`entity-name--subsection.md` (double-hyphen separator):
- `entities/karpathy-projects.md`, `entities/karpathy-ideas.md`
- Or subdirectory: `entities/omar-khattab/rlm.md`

## Identification Heuristic
Common splittable subsections:
- Entity: Timeline → `--timeline.md`, Core Ideas → `--core-ideas.md`, Projects → `--projects.md`
- Concept: Architecture → `-architecture.md`, Modules → `-modules.md`, Comparisons → `-comparisons.md`

## Sub-page Frontmatter
```yaml
---
title: "Entity Name — Projects"
type: entity
parent: entity-slug
tags: [relevant-tags]
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

## Main Page Rewrite
1. Keep: frontmatter, bio overview, summary, comparisons, related wikilinks, sources
2. Add: `## Sub-Pages` section with wikilink references
3. Target: under 200 lines

## Backlink Pattern
Every sub-page needs:
- `> Back to main profile: [[entity-slug]]`
- `## See Also` section linking to sibling sub-pages

## Verification
```bash
# Check no main page exceeds 200 lines
for f in entities/andrej-karpathy.md entities/jason-liu.md; do
  echo "$(wc -l < $f) $f"
done
# Run broken link check
python3 scripts/wiki_graph.py
```

## Parallel Execution
Use `delegate_task` with max 3 pages per batch.
