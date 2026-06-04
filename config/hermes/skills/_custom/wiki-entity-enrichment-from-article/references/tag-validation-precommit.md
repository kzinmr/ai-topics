# Tag Validation in Pre-Commit Hook

## What Happens

When committing wiki changes, the git pre-commit hook (`scripts/pre-commit-tag-validator.py`) checks that all tags in every modified page's frontmatter exist in `wiki/SCHEMA.md`'s tag taxonomy. Unknown tags block the commit.

## Error Message Pattern

```
🚨 TAG TAXONOMY VIOLATIONS — COMMIT BLOCKED
⚠️  TAGS NOT IN SCHEMA.md TAXONOMY (N):
   wiki/entities/example.md:  my-new-tag

   Fix options:
   1. Add 'my-new-tag' to SCHEMA.md taxonomy (if it's a valid new category)
   2. Map it to an existing canonical tag in scripts/tag_normalization.py
   3. Use an existing SCHEMA tag instead
```

## Recovery Steps (in order of preference)

1. **Add the tag to SCHEMA.md**: Find the appropriate category section (Models/People/Products/Techniques/Engineering/AI Agents/Infrastructure/Meta/Domain Concepts) and insert the tag alphabetically.
2. **Use an existing canonical tag**: Check if a similar tag already exists in SCHEMA.md and use that instead.
3. **Emergency override**: `git commit --no-verify` (only for genuine emergencies — the validator exists for a reason).

## Common New Tags and Where They Go

| Tag | Category |
|-----|----------|
| `python`, `rust`, `go`, `typescript` | Engineering |
| `programming-language` | Engineering |
| Company names (e.g., `sentry`, `vercel`) | People/Orgs |
| `blogger`, `content-creator` | Meta |
| `person` | Core Types |

## Validation Commands

```bash
# Check what tags a file uses
grep '^tags:' wiki/entities/example.md
grep '^tags:' wiki/concepts/example.md

# Check if a tag is in SCHEMA.md
grep -c 'my-tag' wiki/SCHEMA.md

# Run the validator manually (dry run)
python3 scripts/pre-commit-tag-validator.py
```
