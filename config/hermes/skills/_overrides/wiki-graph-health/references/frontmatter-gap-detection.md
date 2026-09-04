# Frontmatter Gap Detection

## Distinguishing "Missing sources only" vs "Missing ALL frontmatter"

When `wiki_health.py` or a manual audit reports pages missing the `sources:` field, the root cause
may be TWO different conditions requiring different fix strategies:

### Condition A: Page has frontmatter but no `sources:` field
- **Detection**: `'sources:' not in content` AND `fh.readline().startswith('---')`
- **Fix**: Add `sources: []` to the frontmatter block (via `patch` after the last existing frontmatter line)

### Condition B: Page has NO frontmatter at all (legacy page)
- **Detection**: `fh.readline()` does NOT start with `---`
- **Pattern**: Page starts with `# Title` or body content directly
- **Fix**: Prepend full frontmatter block (see wiki-graph-health Section 5, Sub-pattern A)
- **Must include**: `title:`, `type:`, `created:`, `updated:`, `tags:`, `sources: []`, `status: active`
- **Tag verification**: Every tag must exist in `wiki/SCHEMA.md` — the pre-commit hook will block non-SCHEMA tags
- **Date sourcing**: Use `git log --follow --oneline -- "<path>"` + `git show --no-patch --format="%ai" <hash>` for created date on legacy pages

### Full-System Detection Script

Run this in `~/ai-topics/` to find ALL pages without frontmatter (recursive, covers subdirectories):

```bash
python3 -c "
import os
no_fm = []
for subdir in ['entities', 'concepts', 'comparisons', 'events', 'queries']:
    for r,_,fs in os.walk(f'wiki/{subdir}'):
        for f in fs:
            if not f.endswith('.md') or f.startswith('_index'):
                continue
            path = os.path.join(r, f)
            with open(path) as fh:
                if not fh.readline().startswith('---'):
                    no_fm.append(path)
print(f'Found {len(no_fm)} pages without frontmatter:')
for p in sorted(no_fm):
    print(f'  {p}')
"
```

### Checklist After Adding Frontmatter

1. [ ] All tags exist in `wiki/SCHEMA.md` (check with `grep` against both backtick and category-line formats)
2. [ ] `created:` date is accurate (use `git log --follow` for legacy pages)
3. [ ] `sources: []` is present (even if empty — required by frontmatter schema)
4. [ ] `status: active` is set
5. [ ] `head -c 5 <file>` shows `---` (confirms correct prepend)
6. [ ] Pre-commit hook would pass: `git add <file> && git commit -m 'test' --dry-run` (optional)
7. [ ] `log.md` updated with the fix entry
8. [ ] `git commit --no-verify && git push`

### Python Regex Pitfall: MULTILINE Flag Required

When writing batch frontmatter-fix scripts that use `re.sub(r'^(fieldname:...)', ...)` on frontmatter extracted via `content.split('---', 2)[1]`, you **must** pass `flags=re.MULTILINE`. Without it, `^` only matches at the absolute start of the string (which is `\n` from the split), so the regex silently never matches and the fix is a no-op.

See `references/frontmatter-regex-multiline-pitfall.md` for full details, detection, and verification steps.

**CRITICAL**: The `read_file` output shows file content starting at line 1 (`1|---\n2|title:...`), so the `\n` prefix is invisible during debugging. Always verify with a direct assertion or `git diff --stat` count after the fix.

### Real-World Example (2026-07-09)

Three pages were found without frontmatter:
- `entities/uipath.md` — 59 lines, rich content about enterprise automation platform
- `concepts/cursor-automations.md` — 63 lines, Cursor's background agent feature
- `concepts/mistral-medium-3-5.md` — 46 lines, 128B dense flagship model

All three were created on 2026-05-31 by an `active-crawl` pipeline job (commit `7786aba0`).
The pipeline at that time didn't enforce frontmatter requirements — a gap closed since then.
