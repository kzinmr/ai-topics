# Subagent Tag Taxonomy Violations

## Problem

Subagents enriching entity/concept pages may add tags to YAML frontmatter that don't exist in `SCHEMA.md` tag taxonomy (~766 canonical tags). This blocks the git commit via the pre-commit tag validator hook (`pre-commit-tag-validator.py`).

## Concrete Example (June 2026)

A subagent added `model-quantization` and `ml-research` tags to `entities/martin-alderson.md` during blog-wiki-ingest enrichment. Neither existed in `wiki/SCHEMA.md`. Results:

| Tag | Status | Fix |
|-----|--------|-----|
| `model-quantization` | Not in SCHEMA | Changed to existing canonical tag `quantization` |
| `ml-research` | Not in SCHEMA | Removed entirely |

The commit was blocked with: `TAGS NOT IN SCHEMA.md TAXONOMY (2): wiki/entities/martin-alderson.md: model-quantization, ml-research`

## Prevention

Include explicit tag taxonomy instructions in subagent enrichment context:

```
SCHEMA.md tag taxonomy constraint: Only use tags present in wiki/SCHEMA.md
(~766 canonical tags). Do NOT invent new tags. If a tag doesn't exist in
SCHEMA.md, use an existing canonical tag or skip the tag entirely.
Check with: grep -i 'keyword' wiki/SCHEMA.md
```

## Detection After the Fact

If a commit is blocked by tag violations:

1. Note which tags are violating (`TAGS NOT IN SCHEMA.md TAXONOMY (N): <files>`)
2. For each bad tag, find the closest canonical tag: `grep -i 'keyword' wiki/SCHEMA.md`
3. Common mappings: `model-quantization` → `quantization`, `ml-research` → (no equivalent, remove)
4. Fix the tags in the file with `patch`
5. `git add` the fixed file and re-commit

## Root Cause

Subagent context instructions often say "check existing tags format first" or "add tags" without constraining the tag vocabulary. Since subagents don't have access to SCHEMA.md in their context, they guess — and these guesses often fail the taxonomy validator.

## Permanent Fix

When writing subagent enrichment tasks, do NOT tell subagents to "add relevant tags" to frontmatter. Instead:
- Omit tag additions from subagent scope entirely (let the parent agent handle tag taxonomy compliance)
- OR include the exact tag names to add as concrete values in the context instructions
