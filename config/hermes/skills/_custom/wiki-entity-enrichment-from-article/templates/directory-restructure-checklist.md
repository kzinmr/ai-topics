# Wiki Directory Restructuring — Quick Reference

See `references/wiki-directory-restructuring.md` for full procedure.

## Quick Checklist

1. Plan move map (old path → new path)
2. `mkdir -p` target directories
3. `git mv` all files
4. Python script to update `[[old_path` → `[[new_path` across all .md files
5. Handle entity→concept merges (change frontmatter type, merge content)
6. Create `index.md` MOC for each subdirectory
7. Update `wiki/index.md` (remove old entries, add new)
8. Update `wiki/log.md`
9. Stage individually (not `git add wiki/`) and commit

## User Preferences (2026-06-10)

- **Full prefix in subdirectories**: `gpt/gpt-5-5.md` not `gpt/5-5.md`
- **Exception**: Files with distinctive prefix already (`chatgpt-*`, `decoder-only-*`)
- **Platform split**: Models+features in `vendor/`, APIs+SDK+business in `company/`
  - gpt/ (models) + openai/ (platform)
  - claude/ (models) + anthropic/ (platform)
