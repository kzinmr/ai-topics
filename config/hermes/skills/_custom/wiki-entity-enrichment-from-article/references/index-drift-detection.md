# Index Drift Detection — Related Entity Pages Missing from index.md

## Problem

When creating a new entity page for a tool/product/service developed by a known company, the parent company's entity page often exists as a FILE (e.g., `entities/vercel.md`) but is ABSENT from `wiki/index.md`. This is "wiki drift" — files accumulated from bulk imports (`build_x_wiki.py`, `build_blog_wiki.py`) or prior pipelines that were never indexed. A single entity creation often surfaces 2-3 missing index entries.

## Detection (run BEFORE committing)

```bash
# 1. Grep index.md for the parent company entity
grep -n "entities/<company-slug>" /opt/data/ai-topics/wiki/index.md

# 2. Find ALL related entity files
ls /opt/data/ai-topics/wiki/entities/<company-prefix>*.md

# 3. Cross-check each file against index.md
for f in /opt/data/ai-topics/wiki/entities/vercel*.md; do
  slug=$(basename "$f" .md)
  if ! grep -q "entities/$slug" /opt/data/ai-topics/wiki/index.md; then
    echo "MISSING from index: entities/$slug ($(wc -l < "$f") lines)"
  fi
done
```

## Fix: Add Missing Entries to index.md

When adding entries to the Entities section of `index.md`:
1. Find the alphabetically-correct insertion point via `grep -n "entities/" index.md`
2. Insert ALL missing entries in one `patch` call
3. Each entry format: `- [[entities/slug]] — One-line summary`

## Concrete Example (June 2026)

Creating `entities/vercel-eve.md` surfaced three missing entries:
- `entities/vercel.md` (78 lines) — present since May 2026, never indexed
- `entities/vercel-sandbox.md` (96 lines) — present since May 2026, never indexed  
- `entities/vercel-labs.md` (20 lines) — lightweight stub, added for completeness

All three were added to index.md alongside the new `vercel-eve.md` entry in a single `patch` between `entities/simon-willison` and `entities/warp-terminal`.

## Related: Malformed `related:` Frontmatter Cleanup

When discovering old entity pages during index drift detection, their frontmatter may have legacy formatting issues. Example from vercel.md:

```yaml
# BEFORE (malformed — literal "]]" in strings):
related:
  - "concepts/harness-engineering]]"
  - "entities/openai]]"

# AFTER (corrected):
related:
  - concepts/harness-engineering
  - entities/openai
  - entities/vercel-eve
```

Fix these during the same commit session — they're low-risk corrections adjacent to the index fix.
