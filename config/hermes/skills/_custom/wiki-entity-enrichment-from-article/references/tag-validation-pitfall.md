# Tag Validation Pitfall: Pre-Commit Hook Blocks Commits

## Problem

When creating new wiki pages with tags not in `wiki/SCHEMA.md` taxonomy, the pre-commit hook `.githooks/pre-commit-tag-validator.py` blocks the commit:

```
🚨 TAG TAXONOMY VIOLATIONS — COMMIT BLOCKED
⚠️  TAGS NOT IN SCHEMA.md TAXONOMY (1):
   wiki/concepts/sdar-self-distilled-agentic-rl.md:  multi-turn
```

## Root Cause

SCHEMA.md defines ~340 canonical tags. Any tag used in a page's frontmatter YAML `tags:` field must exist in SCHEMA.md's taxonomy. New tags like `multi-turn`, `agent-training`, etc. that aren't registered will trigger the hook.

## Fix (Two Options)

### Option 1: Remove Unrecognized Tags (Fast)
Remove the unrecognized tag from the page's frontmatter. This is preferred for one-off concept pages where the existing taxonomy already covers the domain.

Example: `multi-turn` and `agent-training` are not in SCHEMA.md. Replace with existing tags like `reinforcement-learning`, `training`, `post-training`, `distillation`, `grpo` which already cover the same territory.

### Option 2: Add Tag to SCHEMA.md (Thorough)
If the tag represents a genuinely new category not covered by existing tags, add it to `wiki/SCHEMA.md` under the appropriate section. This is more involved but necessary for recurring categories.

## Verification

After fixing, re-run:
```bash
cd ~/ai-topics && git add wiki/ && git commit -m "..." && git push
```

The pre-commit hook will re-validate and should pass.

## Prevention

Before creating a new page, check if your planned tags exist in SCHEMA.md:
```bash
grep "planned-tag-name" wiki/SCHEMA.md
```

Only use tags that already appear in the tag taxonomy sections of SCHEMA.md.
