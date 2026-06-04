# Wiki Commit Pitfalls Reference

## Git Pre-Commit Hook Blocks Unrelated Staged Files

### Symptom
```
🚨 TAG TAXONOMY VIOLATIONS — COMMIT BLOCKED
⚠️  TAGS NOT IN SCHEMA.md TAXONOMY (10):
   wiki/concepts/some-other-page.md:  some-tag
```

Even though YOUR files pass validation, the commit is blocked because OTHER files staged in the index (from previous sessions) have tag violations.

### Root Cause
The pre-commit hook (`pre-commit-tag-validator.py`) scans **all staged files in the git index**, not just the subset you intend to commit. Files staged by previous sessions accumulate and their violations persist.

### Fix
```bash
# 1. See which files have tag violations
# (shown in the error output above)

# 2. Unstage the problematic files
git reset HEAD wiki/concepts/problem-file.md wiki/entities/another.md

# 3. Verify only your intended files remain staged
git status --short wiki/

# 4. Commit again
git commit -m "wiki: ..." && git push
```

### Prevention
After committing your own changes, leave the index clean for the next session:
```bash
# If there are still unstaged modified files you didn't intend to stage:
git checkout -- wiki/concepts/unrelated.md   # discard changes you didn't make
```

## Duplicate Skill Names Blocking skill_view

### Symptom
```
Ambiguous skill name 'wiki-comparison-page-routing': 2 skills match
  - /opt/data/.hermes/skills/wiki/wiki-comparison-page-routing/SKILL.md
  - /opt/data/ai-topics/config/hermes/skills/wiki/wiki-comparison-page-routing/SKILL.md
```

### Workaround
Use `skill_manage(action='patch')` instead — it resolves by name through a different mechanism that doesn't error on duplicates. For reading skills, use terminal to `read_file` the SKILL.md directly.
