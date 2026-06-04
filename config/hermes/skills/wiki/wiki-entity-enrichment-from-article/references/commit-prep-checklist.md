# Pre-Commit Tag Validation Checklist

> **⚠️ MANDATORY**: Run this checklist BEFORE `git commit` on any wiki change that touches entity or concept pages. The pre-commit hook (`pre-commit-tag-validator.py`) will block commits with unknown tags, and it validates ALL staged files.

## When This Is Most Likely to Fire

You will hit this when creating pages about topics outside the usual ML/AI engineering domain:
- **Religious/philosophical documents**: `religion` (add to Meta category)
- **Government/policy**: `treaty`, `legislation`, `executive-order`
- **Niche technologies**: `new-db-name`, `new-framework`
- **Cross-domain concepts**: Anything bridging AI + non-tech domains

## Checklist

1. **Before writing frontmatter**: Scan SCHEMA.md tags (lines 31-40) to know what's available
2. **After writing pages, before commit**: For each tag in your new page(s), verify it exists in SCHEMA.md
3. **For missing tags**: Add to the appropriate category in SCHEMA.md, then `git add wiki/SCHEMA.md`
4. **Staging area**: The hook validates EVERY staged file. You own all violations.

## Recovery Flow

```
git commit → BLOCKED: "religion" not in taxonomy
  → patch SCHEMA.md to add "religion" to Meta category
  → git add wiki/SCHEMA.md
  → git commit → ✅ SUCCESS
```

## Real Failure Cases

| Date | New Tag | Domain | Category Added To |
|------|---------|--------|-------------------|
| 2026-05-25 | `religion` | Magnifica Humanitas encyclical | Meta |
| 2026-05-22 | `sqlite`, `datasette`, `plugins`, +7 more | Blog ingest pages + pre-existing violations | Infrastructure, Products, Engineering |

## See Also
- `references/pre-write-verification.md` — full protocol including overwrite prevention and tag validation details
- `wiki/SCHEMA.md` — canonical tag taxonomy
