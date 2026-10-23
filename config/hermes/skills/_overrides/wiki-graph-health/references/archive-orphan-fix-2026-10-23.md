# Archive Orphan Fix — 2026-10-23 session

Digest reported 2 orphans under `concepts/gpt/_archive/`. The blanket rule "`_archive/` files are intentionally not in the index" is WRONG as an auto-skip — two distinct fix classes exist:

## Fix classes

1. **Zero-content TODO stub** (`< 500 B`, body is only `> **TODO**: Enrich this page.` + generic stub headings) → **delete**. Example: `2026-04-24-ainews.md` (440 B, `status: stub`, malformed frontmatter with `sources: []` above the tags list).

2. **Real content page** (enriched, has `sources:` with raw refs) → **register twice**:
   - Parent hub page `concepts/<dir>/index.md` → `## See Also` entry with dated description
   - Main `wiki/index.md` in the Concepts section, alphabetically adjacent to the sibling entries (e.g. right after `[[concepts/gpt/index]]`)
   The recursive not-linked scanner counts a page as linked if EITHER the hub or main index references it, but the digest orphan checker only reads main index.md — so the main-index entry is what silences it.

## Hub filename trap

This wiki's hub files use BOTH conventions: `concepts/gpt/index.md`, `concepts/openai/index.md`, `concepts/gemini/index.md`, `concepts/ai-benchmarks/index.md`, `concepts/context-engineering/index.md` use `index.md`; `concepts/inference/_index.md`, `concepts/post-training/_index.md` etc. use `_index.md`. `ls concepts/gpt/_index.md` failing does NOT mean the hub is missing — check `index.md` too.

## Header count reconciliation formula

Correct per-section header count = number of index list lines, NOT filesystem count and NOT the stale header:

```python
n = len(re.findall(r'^- \[\[concepts/', index_content, re.M))
```

2026-10-23 drift observed: Entities header 953 / lines 954 / files 953; Concepts header 2202 / lines 2222 / files 2203; Events 41 / 42; Queries 40 / 37 (lines, 37 files — 3 list lines are redirects or duplicates). Use list-line count; validate_index.py passed with those values.

## Commit

`wiki: auto-fix health issues (orphans cleared, index counts)` — 4 files, pre-commit tag validator + validate_index.py both passed, pushed as c609f209.
