# Tag Taxonomy Pre-Commit Validation Pitfall

## Problem

The git pre-commit hook (`pre-commit-tag-validator.py`) blocks `git commit` if any wiki page uses tags not in `wiki/SCHEMA.md` taxonomy. This catches you at commit time, not at write time.

## Common Offenders

Domain-specific tags invented on the fly that don't exist in SCHEMA.md:
- `ai-marketer` → `content-creator`
- `agent-operations` → `agent-architecture` or `devops`
- `growth-marketing` → `strategy` or `startup`
- `web3-marketing` → `startup`
- Any role-specific tag (e.g., `python-developer` → `python` + `person`)

## Fix Workflow

1. The error message lists the offending tags and file paths
2. `patch` the entity page frontmatter to replace non-canonical tags with SCHEMA.md equivalents
3. `git add` the fixed file
4. Retry `git commit`

## Tag Selection Heuristic

For **person entity pages**, prefer these existing canonical tags:
- `person` (always)
- `content-creator` (for writers/bloggers/publishers)
- `entrepreneur` (for founders/co-founders)
- `startup` (for startup-affiliated)
- `ai-product` (for product builders)
- `agent-architecture` (for agent infrastructure builders)
- `researcher` (for academic/research backgrounds)
- `educator` (for tutorial/educational content creators)
- `company` (for organizational entities)

## Never Do This

Do NOT use `git commit --no-verify` except in genuine emergencies where the tag taxonomy itself needs updating.

## Browse Available Tags

```bash
grep "^  -" wiki/SCHEMA.md | head -50
```
