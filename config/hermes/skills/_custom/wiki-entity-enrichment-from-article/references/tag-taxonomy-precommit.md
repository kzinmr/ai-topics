# Tag Taxonomy Pre-Commit Validation

The `.githooks/pre-commit` hook runs `pre-commit-tag-validator.py` and blocks commits when any page's `tags:` frontmatter contains tags NOT in `wiki/SCHEMA.md`'s Tag Taxonomy.

## Error Format

```
======================================================================
🚨 TAG TAXONOMY VIOLATIONS — COMMIT BLOCKED
======================================================================

⚠️  TAGS NOT IN SCHEMA.md TAXONOMY (N):
   wiki/some-page.md:  bad-tag-1
   wiki/other-page.md:  bad-tag-2

   Fix options:
   1. Add 'bad-tag' to SCHEMA.md taxonomy (if it's a valid new category)
   2. Map it to an existing canonical tag in scripts/tag_normalization.py
   3. Use an existing SCHEMA tag instead

   To override (emergency only):
   git commit --no-verify
======================================================================
```

## Common Violation Patterns

### 1. Using concept names as tags
`contextmaxxing`, `context-lock-in`, `tokenmaxxing` are page TITLES, not canonical tags. Replace with existing tags like `context-management`, `enterprise-ai`, `memory-systems`, `vendor-lock-in`.

### 2. Using entity names as tags
`sentra-app`, `claude-code` are entity slugs, not tags. Use category tags like `company`, `product`, `coding-agent`.

### 3. Using project-specific jargon
Terms coined in a single article that aren't widely adopted. Either add to SCHEMA.md or map to general category tags.

## Fix Workflow

1. **Read the error output** — note all violating tags and file paths
2. **Decide**: genuine new category → add to SCHEMA.md; name-as-tag → remove and use existing tags
3. **Patch SCHEMA.md** if adding new tags — insert into the correct taxonomy line (Meta, Engineering, AI Agents, etc.)
4. **Patch each violating page** — remove bad tags, optionally add canonical replacements
5. **`git add wiki/SCHEMA.md`** — required if SCHEMA.md was modified
6. **Retry commit** — `git commit` (no `--no-verify` needed if tags are fixed)

## Example: This Session

Violations: `vendor-lock-in`, `platform-economics` (new, valid categories) + `contextmaxxing`, `context-lock-in` (concept names as tags)

Fix: Added `vendor-lock-in` and `platform-economics` to SCHEMA.md Meta line. Removed `contextmaxxing` from `context-lock-in.md` tags. Removed `context-lock-in` from `sentra-app.md` tags.

## SCHEMA.md Insertion Point Reference

Tags are organized by category line. When adding, insert in the alphabetically-correct position within the appropriate comma-separated list:

- **Meta** line: `comparison, timeline, ..., economics, platform-economics, vendor-lock-in, privacy, ...`
- **AI Agents** line: `ai-agents, multi-agent, ..., enterprise-ai, knowledge-graph, ...`
- **Engineering** line: `agentic-engineering, harness-engineering, ..., context-management, ...`
