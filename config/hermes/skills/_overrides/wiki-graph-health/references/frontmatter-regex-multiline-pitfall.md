# Frontmatter Regex MULTILINE Pitfall

## Symptom

A batch frontmatter fix script using `re.sub()` reports "fixed N files" but the files are **unchanged** — `type:` / `tags:` / `sources:` fields remain missing despite a supposedly successful regex run.

## Root Cause

When extracting frontmatter via `content.split('---', 2)[1]`, the result **always starts with `\n`**:

```python
content = "---\ntitle: Foo\ncreated: 2026-01-01\n---\n\nbody..."
parts = content.split('---', 2)
fm = parts[1]
# fm == '\ntitle: Foo\ncreated: 2026-01-01\n'
#      ^^ leading newline
```

A regex like `r'^(title:.*\n)'` uses `^` which, **without `re.MULTILINE`**, only matches at the **absolute start of the string** — which is the `\n`, not `title:`. The regex silently finds no match, `re.sub` returns the original string unchanged, and the script reports no error because `new_fm == fm` is the comparison that detects "no change" — but the regex never matched in the first place.

## Detection

```python
# WRONG — silently no-op:
new_fm = re.sub(r'^(title:.*\n)', r'\1type: entity\n', fm, count=1)

# RIGHT — with MULTILINE flag:
new_fm = re.sub(r'^(title:.*\n)', r'\1type: entity\n', fm, count=1, flags=re.MULTILINE)

# WRONG — same issue, different pattern:
re.sub(r'^(type:.*\n)', r'\1tags: []\n', fm)  # no MULTILINE → no-op on \n-prefixed fm

# RIGHT:
re.sub(r'^(type:.*\n)', r'\1tags: []\n', fm, flags=re.MULTILINE)
```

## Occurrence Pattern

This bug surfaced in the 2026-07-09 health fix run:

1. **First pass (entities)**: Used `re.sub(r'^(title:.*\n)', ..., count=1)` without `flags=re.MULTILINE`. The script printed "type fixes=8, tags fixes=10" but the actual files were **not modified** — the regex silently failed on all files with `\n`-prefixed frontmatter (every file extracted via `split('---', 2)`).

2. **Second pass (concepts)**: Used `flags=re.MULTILINE` — correctly fixed all 26 concept pages in one pass.

3. **Third pass (entities, retry)**: Added `flags=re.MULTILINE` — correctly fixed all 16 remaining entity pages.

## Prevention

**Always use `flags=re.MULTILINE`** on any `re.sub` that uses `^` anchor on frontmatter extracted via `content.split('---', 2)[1]`.

**Checklist before running batch frontmatter fix**:
1. Does your regex use `^`? → Add `flags=re.MULTILINE`
2. Does your regex use `$`? → Add `flags=re.MULTILINE`
3. Are you extracting frontmatter via `split('---', 2)`? → The result is `\n`-prefixed, MULTILINE is required

## Verification After Fix

```python
# Check a few files to confirm the regex actually modified content
with open(path) as fh:
    content = fh.read()
parts = content.split('---', 2)
if len(parts) >= 3:
    fm = parts[1]
    assert 'type:' in fm, f'type: still missing in {path}'
    assert 'tags:' in fm, f'tags: still missing in {path}'
```

Also verify with `git diff --stat HEAD` — the file count should match expectations, not be suspiciously smaller than `print("Fixed N")` claimed.
