## 7. Duplicate Tags in Frontmatter

**What it looks like**: YAML list has the same tag twice:
```yaml
tags:
  - podcast
  - podcast    # accidental duplicate
  - content-creator
```

**Root cause**: When using `patch` to replace a bad tag (e.g. `live-show` → `podcast`), if the old_string only matches the tag name and there's already a `podcast` tag elsewhere in the list, you end up with two copies.

**Fix**: After any tag replacement, re-read the frontmatter and verify no duplicates. Duplicates won't block the commit but degrade the index.

## 8. Losing Existing Tags During Patch

**What it looks like**: A tag like `open-source` disappears from a page after a tag-related patch.

**Root cause**: When using `patch` to replace a multi-line tag block, if `old_string` includes tags you want to keep and `new_string` omits them, they're silently dropped.

**Example that went wrong**:
```
old: "- planning\n  - agent-harness\n  - agent-skills\n  - open-source"
new: "- agent-harness\n  - agent-skills\n  - agent-design-patterns"   # lost open-source!
```

**Fix**: Always include ALL tags from the old block in the new block. When replacing a subset, use a more targeted `old_string` that only captures the tags being changed, not the whole block.

## 9. Batch Tag Validation (Pre-Flight Check)

**Pattern**: Before `git add && git commit`, validate all new/modified pages at once:

```bash
cd ~/ai-topics
# Extract all tags from staged files and check against SCHEMA.md
grep -rh "^  - " wiki/entities/ wiki/concepts/ | sort -u | while read tag; do
  tag_clean=$(echo "$tag" | sed 's/^  - //')
  if ! grep -q "$tag_clean" wiki/SCHEMA.md; then
    echo "MISSING: $tag_clean"
  fi
done
```

Or simpler: just run the commit and let the pre-commit hook catch violations — but then you need to fix + re-commit, which costs a round trip. Pre-validation saves that round trip when creating 5+ pages.
