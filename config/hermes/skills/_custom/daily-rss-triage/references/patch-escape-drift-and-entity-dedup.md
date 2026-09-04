# Patch Escape-Drift & Entity Dedup Patterns (Verified 2026-08-17)

## Patch Escape-Drift Detection

The `patch` tool reports "Escape-drift detected" when `old_string` and `new_string` contain literal `\"` sequences that don't match the actual file content. This happens when content has apostrophes or quotes that get serialized differently.

### Symptom
```
Escape-drift detected: old_string and new_string contain the literal sequence `\"`
but the matched region of the file does not. This is almost always a tool-call
serialization artifact where an apostrophe or quote got prefixed with a spurious backslash.
```

### Root Cause
When content contains smart quotes, apostrophes, or mixed quote types, the tool serialization layer may escape them as `\"` in the JSON parameters, but the actual file content has the unescaped character.

### Workaround
Instead of matching the full paragraph containing the problematic quote, match a DIFFERENT unique substring that doesn't contain quotes:

```
# Instead of matching (fails due to escape-drift):
old_string: '> *"While the world\'s been watching physical supply chains, a different kind of supply chain attack has been escalating in the open source ecosystem."*\n\n## Related'

# Match a different unique boundary:
old_string: 'escalating in the open source ecosystem."*\n\n## Related'
```

### Real Failure (2026-08-17)
Patching `entities/martin-alderson.md` to add a new section before `## Related`. The blockquote contained `world's` (apostrophe) and double quotes. First attempt with the full blockquote triggered escape-drift. Second attempt matching just the last phrase + section header succeeded.

## Entity Deduplication Checklist (Blog-Wiki-Ingest)

When processing blog articles that mention people/companies, follow this checklist BEFORE creating any entity file:

1. **Search index with plain text** (not regex): `search_files(path="wiki/index.md", pattern="firstname", target="content")`
2. **Search index with last name**: `search_files(path="wiki/index.md", pattern="lastname", target="content")`
3. **Terminal find for filename**: `terminal("find ~/ai-topics/wiki/entities -name '*pattern*' 2>/dev/null")`
4. **Check index entry format**: Index may use `entities/martin-alderson` while you'd expect `entities/martinalderson-com`
5. **If found**: Read existing file, use `patch` to add new content, update `updated:` in frontmatter
6. **If NOT found**: Safe to create with `write_file`

### Common Filename Patterns in the Wiki

| Article source | Expected filename | Index format |
|---|---|---|
| garymarcus.substack.com | `gary-marcus.md` | `entities/gary-marcus` |
| martinalderson.com | `martin-alderson.md` | `entities/martin-alderson` |
| daringfireball.net | `daringfireball-net.md` | `entities/daringfireball-net` |
| simonwillison.net | `simon-willison.md` | `entities/simon-willison` |
| seangoedecke.com | `seangoedecke-com.md` | `entities/seangoedecke-com` |

Pattern: Substack author → `firstname-lastname.md`; custom domain → `domain-com.md`

## Pre-Commit Content Regression Hook Recovery

When the pre-commit hook blocks a commit due to content regression (page shrunk by >50 lines AND >50%):

```bash
# 1. Restore the original file
git checkout HEAD -- wiki/entities/<file>.md

# 2. Re-read the original to find insertion point
read_file(path="wiki/entities/<file>.md", offset=N, limit=20)

# 3. Use patch to add your new content to the existing file
patch(mode="replace", path="wiki/entities/<file>.md", old_string="...", new_string="...")

# 4. Re-stage and commit
git add wiki/entities/<file>.md
git commit -m "..."
```

**Real failure (2026-08-17)**: Wrote `daringfireball-net.md` from scratch (55 lines) when existing file had 173 lines of curated content. Pre-commit hook blocked. Restored via `git checkout HEAD --`, found the "Recent Themes" section, and used `patch` to add the new watermarking article as a bullet point.
