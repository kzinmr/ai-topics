# Pre-Commit Tag Taxonomy Workflow

## Pattern

Every wiki commit runs a pre-commit hook that validates all tags against `wiki/SCHEMA.md`. New tags introduced on wiki pages MUST be added to SCHEMA.md BEFORE the commit will pass.

This means the typical ingest workflow is:

```
write pages → git add → git commit → BLOCKED (tag violation)
  → add tags to SCHEMA.md → git add → git commit → ✅
```

## Common Tag Categories to Add

Tags most frequently need adding to SCHEMA.md:

| Category | SCHEMA Section | Example Additions This Session |
|----------|---------------|-------------------------------|
| Evaluation benchmarks | Techniques | `niah`, `beir`, `mteb` |
| Retrieval techniques | Techniques | `retrieval`, `position-interpolation`, `context-extension`, `rope`, `position-encoding` |
| Context phenomena | Techniques | `needle-in-haystack`, `context-rot`, `context-degradation`, `query-expansion` |
| Programming languages | Engineering | `rust` |
| Geographic | People/Orgs | `france` |

## Quick Fix Command

```bash
# After commit blocked:
# 1. Read the error output for exact tag names
# 2. Patch SCHEMA.md to add them under the right section
# 3. Retry:
cd /opt/data/ai-topics && git add wiki/ && git commit -m "..." && git push
```

## Pitfall: Distillation vs Knowledge-Distillation

The tag `distillation` already exists in SCHEMA.md. Don't create `knowledge-distillation` as a separate tag — just use `distillation`.

## Pitfall: CJK Range False Positives for Tag Names

The CJK unified range (`\u4E00-\u9FFF`) catches Chinese characters. If a Chinese proper name (like 肖涵 for Han Xiao) triggers the Japanese content pre-commit hook, remove the CJK characters from the body and use the romanized form only.

## Pre-Commit Hook Order

The `.githooks/pre-commit` runs checks in this order:
1. `wiki/index.md` validation (clean format check)
2. **Tag taxonomy validation** (`pre-commit-tag-validator.py`) — blocks if any tag not in SCHEMA.md
3. **Japanese content check** (`pre-commit-jp-check.py`) — blocks if JP introduced to clean file

If both fail, they fail sequentially — fix the tag issue first, then the JP issue.
