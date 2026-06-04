# Pre-commit Pitfalls for Wiki Ingestion

## Tag Taxonomy Violations

The pre-commit hook (`pre-commit-tag-validator.py`) blocks commits if any tag in frontmatter doesn't appear in `wiki/SCHEMA.md`.

**Symptom**: `🚨 TAG TAXONOMY VIOLATIONS — COMMIT BLOCKED`

**Fix**:
1. Read the error output — it lists the exact tags and files
2. Add missing tags to the appropriate category line in `wiki/SCHEMA.md`:
   - Products → product names (chatgpt, figma, etc.)
   - Engineering → technical concepts (ci-cd, frontend, etc.)
   - People/Orgs → company names (skyscanner, dagster, etc.)
   - Meta → case-study, event, etc.
3. `git add wiki/SCHEMA.md && git commit` (the hook runs again and should pass)

## Index.md Section Misplacement

Concept entries can end up under wrong section headers (e.g. concept pages listed under `## Events`).

**Detection**:
```bash
awk '/^## Entities/{s="entities"} /^## Concepts/{s="concepts"} /^## Events/{s="events"} /^## Comparisons/{s="comparisons"} /^## Queries/{s="queries"} /^- \[\[/{counts[s]++} END{for(k in counts) print k": "counts[k]}' index.md
```

**Fix**: Move misplaced entries to the correct section, update section header counts.

## Section Header Count Mismatch

Section headers like `## Concepts (1519 pages)` may have stale counts.

**Fix**: Count actual entries per section and update headers to match.

## CJK Characters in Wiki Pages

Pre-commit blocks wiki pages containing Japanese/CJK characters (regex: `[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]`).

**Exception**: `raw/` directory, `log.md`, and `index.md` are exempt.

**Fix**: Translate Japanese content to English before committing wiki concept/entity/event pages.
