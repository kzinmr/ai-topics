# Page Naming Policy & Stub Cleanup Workflow

## Page Naming Policy (SCHEMA.md § Naming Policy)

Wiki filenames (slugs) must be concise, English-only, and descriptive.

### Rules
| Check | ERROR | WARN |
|---|---|---|
| CJK characters in filename | ✅ | — |
| Date-prefix slug (YYYY-MM-DD) | ✅ | — |
| Word count (hyphen-separated) | ≥11 | ≥8 |
| Hyphen count | ≥11 | ≥8 |

### Enforcement Points
1. **pre-commit hook** (`.githooks/pre-commit`): Blocks NEW files (`--diff-filter=A`) with CJK, date-prefix, or ≥11 hyphens
2. **wiki_health.py** `section_page_name_policy()`: Reports all violations in weekly health digest
3. **SCHEMA.md**: Documents the policy for agent reference

### Critical Pitfall: git core.quotepath

`git diff --cached --name-only` outputs non-ASCII filenames as `\xxx` escape sequences by default (`core.quotepath=true`). This makes `grep -qP '[\x{3040}-\x{309F}...]'` silently fail — the CJK characters are invisible.

**Fix**: Use `git -c core.quotepath=false diff --cached --name-only` in the pre-commit hook to get unquoted UTF-8 filenames.

```bash
# WRONG — CJK filenames become \xxx escapes, grep -P can't match
STAGED=$(git diff --cached --name-only --diff-filter=A | grep -E '^wiki/(entities|concepts)/')

# CORRECT — unquoted UTF-8 filenames
STAGED=$(git -c core.quotepath=false diff --cached --name-only --diff-filter=A | grep -E '^wiki/(entities|concepts)/')
```

## Stub Cleanup Workflow

When cleaning up misplaced or tag-pile stubs (e.g., pages with CJK names, date-prefix slugs, or 10+ word tag piles):

### Step 1: Inventory & Classify
```bash
# Find all violations
python3 scripts/wiki_health.py --json 2>/dev/null | python3 -c "
import json,sys
d=json.load(sys.stdin)
for v in d['page_name_policy']['violations']:
    print(f'{v[\"severity\"].upper():5} {v[\"word_count\"]:2}w {v[\"page\"]}')
"
```

### Step 2: For Each Violation
1. **Read the file** — is it a stub (status: stub, TODO only) or has real content?
2. **Search backlinks** — `grep -rn 'filename-stem' wiki/` to find all inbound wikilinks
3. **Check for canonical page** — does a better-named page already cover the same topic?
4. **Decide action**:
   - **Stub + no backlinks + canonical exists** → DELETE, no link fixes needed
   - **Stub + backlinks exist + canonical exists** → DELETE + redirect backlinks to canonical
   - **Stub + no canonical** → RENAME to concise name (if topic is worth keeping) or DELETE
   - **Rich content** → RENAME or MOVE (e.g., concept → comparisons/)

### Step 3: Execute
```bash
# Delete stubs
git rm wiki/concepts/bad-name.md

# Fix backlinks (Python batch replace)
python3 -c "
import os
old = 'concepts/bad-long-name'
new = 'concepts/good-name'
for f in ['wiki/index.md', 'wiki/concepts/related.md']:
    content = open(f).read()
    if old in content:
        open(f, 'w').write(content.replace(old, new))
        print(f'  Fixed: {f}')
"

# Update index.md counts
# Concepts: NNN → NNN-1
# Entities: NNN → NNN-1 (if entity deleted)
```

### Step 4: Commit
```bash
git add wiki/ && git commit -m "wiki: remove N naming violations — description" && git push
```

## Page Merge Workflow

When two pages cover the same topic (e.g., `eval-tools-comparison.md` + `llm-evaluation-tools.md`):

1. **Read both** — identify unique content in each
2. **Choose canonical** — prefer the better-named, more established, or broader page
3. **Merge unique content** into canonical (use `patch`, not `write_file` for rich pages)
4. **Update frontmatter** — add `aliases` (old filenames), `moved_from`, merge `sources`
5. **Delete the absorbed page** — `git rm`
6. **Batch-fix backlinks** — replace old slug with canonical slug in all referencing files
7. **Remove duplicate index entries** — the absorbed page's entry in index.md
8. **Update counts** — section headers in index.md

### Merging into an existing rich page
- **Never use write_file** — it overwrites accumulated content
- Use `patch` to insert new sections at the right location
- Merge `sources` lists (deduplicate)
- Add old name to `aliases` for backward compatibility
- Add old path to `moved_from` for provenance tracking
