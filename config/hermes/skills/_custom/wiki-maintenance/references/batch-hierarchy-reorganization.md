# Batch Hierarchy Reorganization Workflow

When performing multiple sequential directory reorganizations in one session (e.g., creating 5+ new subdirs and moving 50+ pages total), follow this workflow to stay organized.

## Session Checklist

1. **Run detect_hierarchy_candidates.py** to identify clusters
2. **Present analysis to user** — show candidate clusters with page counts, titles, tags
3. **User decides** which to move, which to keep flat, which to merge
4. **Execute moves in batches** — one subdir at a time:
   a. Move files
   b. Run link-update script (covers ALL moves, not just current batch)
   c. Create/update _index.md
   d. Commit and push
5. **Verify** after each batch — no broken links, no double-display bugs

## Link Update Script Pattern

For bulk moves covering multiple target directories, use a single unified slug→path mapping:

```python
moves = {}
# Add all moves from all batches
for s in ["slug-a", "slug-b"]:
    moves[s] = f"concepts/target-dir-1/{s}"
for s in ["slug-c", "slug-d"]:
    moves[s] = f"concepts/target-dir-2/{s}"

# Single regex matching all moved slugs
slugs_pattern = "|".join(re.escape(s) for s in moves)
pattern = re.compile(rf"\[\[(?:concepts/)?({slugs_pattern})(?:\|([^\]]+))?\]\]")
```

## Pitfalls

1. **"Context Context Engineering" bug**: When slug already contains the display name prefix, the regex must NOT add another prefix. After bulk update, search for `Double Double|Context Context|Prefix Prefix` to catch duplicates.

2. **File rename within subdir**: If user wants `anxiety.md` → `context-anxiety.md` inside `context-engineering/`, the link update must target the SHORT slug (anxiety) not the full path. Re-run link update after rename.

3. **Merging into _index.md**: When a flat page covers the same topic as the subdir's _index.md, merge content first (read both, patch unique content into _index.md), then delete the flat page. Update links to point to the _index path.

4. **SCHEMA.md tag violations**: Pre-commit hook checks tag taxonomy. If moving pages introduces new tags, add them to SCHEMA.md first.

5. **Japanese content in wiki pages**: Pre-commit hook blocks JP content in non-raw/ files. Write all wiki content in English.
