# Git Pre-Commit Hook: Tag Validation Workaround

## Problem

The repo's `pre-commit` hook runs tag validation across ALL staged files. When you stage your wiki changes alongside files modified by other agents/cron jobs, the hook may block YOUR commit due to tag violations in files you didn't touch.

## Symptom

```
🚨 TAG TAXONOMY VIOLATIONS — COMMIT BLOCKED
⚠️  TAGS NOT IN SCHEMA.md TAXONOMY (N):
   wiki/concepts/some-other-page.md:  some-other-tag
   ...
```

But the listed files are NOT yours. Your own files pass validation.

## Solution

Unstage the offending files before committing:

```bash
cd ~/ai-topics
# Identify which staged files are NOT yours
git status --short wiki/

# Unstage only the files with violations you didn't create
git reset HEAD wiki/concepts/offending-file.md wiki/entities/another-one.md

# Verify only your files remain staged
git status --short wiki/

# Now commit
git commit -m "wiki: your summary"
git push
```

## Important

- Only unstage files you didn't create/modify in this session
- If a file WAS yours and has a tag violation, fix it by adding the tag to `SCHEMA.md` first
- The hook validates ALL staged files — it doesn't know which ones are "yours"
- `git commit --no-verify` is a last resort; prefer fixing the staging area
