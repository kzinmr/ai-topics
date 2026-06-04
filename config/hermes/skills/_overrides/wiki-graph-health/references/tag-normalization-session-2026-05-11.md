# Tag Normalization Session - 2026-05-11

## Overview
Comprehensive tag audit performed on wiki (1,754 files) during routine health check.

## Statistics
- **Unique tags found in use**: 268
- **Canonical tags in SCHEMA.md taxonomy**: 224
- **Non-canonical tags**: 148
- **Composite tags (3+ hyphens)**: 4

## Top Non-Canonical Tags (by frequency)

| Tag | File Count | Suggested Action |
|-----|-----------|------------------|
| `telegram` | 2 | Add to SCHEMA.md (legitimate messaging platform) |
| `pipeline` | 2 | Map to `automation` or `observability` |
| `logic` | 2 | Map to `symbolic-ai` (add to taxonomy) |
| `symbolic-ai` | 1 | Add to SCHEMA.md (legitimate AI paradigm) |
| `deep-agents` | 1 | Map to `agentic-engineering` |
| `agentic-coding` | 1 | Map to `agentic-engineering` |
| `human-in-the-loop` | 1 | Decompose to `human-feedback` |

## Composite Tags (3+ hyphens)

These are ALWAYS errors per schema rules:
1. `human-in-the-loop` → should be `human-feedback`
2. `agents-self-improvement-learning` → should be `agentic-engineering` + `self-improvement`
3. (2 additional similar patterns)

## Key Insight

Tag taxonomy drift is **inevitable at scale**. With 268 unique tags vs 224 canonical, ~15% of tags are non-compliant. This grows over time as new concepts emerge. Regular audits (weekly cron) + pre-commit hooks are essential to maintain taxonomy integrity.

## Remediation Procedure

1. Add legitimate new tags to SCHEMA.md taxonomy
2. Map non-canonical tags to canonical equivalents in `TAG_normalization.py`
3. Decompose composite tags into component canonical tags
4. Re-run audit to verify cleanup
5. Commit changes and push
