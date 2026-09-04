# Python `content.replace()` Pitfall on Markdown Content

## Symptom

Python `str.replace(old, new)` on markdown file content returns the string **unchanged** despite the `old` and actual file content appearing identical:

```python
old_table = "|| [Build Your Own Deep Research Agent](...) | Ivan Leo | ..."
if old_table in content:
    content = content.replace(old_table, new_table)  # ← NEVER EXECUTES
    print("✓ Added row")  # ← NEVER PRINTS
```

The script silently skips the replacement and continues with a stale file. No error is raised.

## Root Cause

Markdown files from real sources (Substack newsletters, blog posts, web extraction) frequently contain **invisible Unicode character differences** that `in` and `str.replace()` treat as different strings even though they look identical in your editor and terminal:

| Character | Visible As | Unicode Problem |
|-----------|-----------|-----------------|
| → (U+2192) | `→` | Versus `->` or `→` from a different font/encoding |
| — (U+2014) em-dash | `—` | Versus `--` (two hyphens) or `—` from copy-paste |
| × (U+00D7) multiplication | `×` | Versus `x` or `X` |
| " (U+201C) / " (U+201D) smart quotes | `"..."` | Versus `"..."` (ASCII U+0022) |
| ' (U+2018) / ' (U+2019) smart apostrophes | `'...'` | Versus `'` (ASCII U+0027) |
| — (U+2013) en-dash | `–` | Versus `-` (hyphen) |
| ZERO WIDTH SPACE (U+200B) | invisible | Completely invisible; copy-paste artifact |
| NON-BREAKING SPACE (U+00A0) | looks like space | Versus regular space (U+0020) |
| TRAILING WHITESPACE | invisible | `"text "` vs `"text"` (invisible space at line end) |

## When This Happens

Most commonly when:

1. **Building markdown tables from editor-typed strings**: you type a `→` or `×` in your Python script, but the actual file uses a different Unicode code point or ASCII equivalent
2. **Copy-pasting content from web_extract output**: the extracted content may use Unicode characters that look like their ASCII equivalents but aren't
3. **Using `read_file` output as the source of truth**: the line-number display format (`N|`) can mask subtle differences
4. **Patching table rows dynamically**: table content is more susceptible than plain paragraphs because of pipe (`|`) characters and unicode symbols

## The Fix: Use `patch` With Fuzzy Matching

The `patch` tool uses 9 fuzzy-matching strategies that handle Unicode variants, whitespace differences, and encoding mismatches:

```python
# ❌ FAILS silently (Python str.replace)
old = "→ | Ivan Leo | From raw Gemini API"
if old in content:
    content = content.replace(old, new)  # May NOT execute

# ✅ WORKS (patch with fuzzy matching)
patch(
    path="entities/hugo-bowne-anderson.md",
    old_string="→ | Ivan Leo | From raw Gemini API",
    new_string=old + "\n| [New row]..."
)  # Fuzzy matching handles any Unicode variant
```

## Prevention

### 1. Always try `patch` first for markdown table edits

Before writing any enrichment script that uses `str.replace()` on markdown content, check if `patch` can do the job. `patch` is preferred because:
- It has fuzzy matching for Unicode/homoglyph characters
- It produces a visible `diff` so you can verify correctness
- It's less code to write (no file open/read/write boilerplate)

### 2. If you must use Python, verify with a hex dump

When `old_string in content` is False but you're certain the content exists:

```bash
# Check if the target line really exists with exact Unicode
grep -n "Deep Research Agent" entities/hugo-bowne-anderson.md | xxd | head -5
# Compare against your Python string
python3 -c "print('→'.encode('utf-8').hex())"
```

Compare the hex bytes. If they differ, your Python string has different Unicode characters than the file.

### 3. The safe alternative: line-based replacement

If you know the line number, use line-indexed replacement instead of string matching:

```python
lines = content.split('\n')
for i, line in enumerate(lines):
    if 'Build Your Own Deep Research Agent' in line:
        # Only match a substring, not the full Unicode-dependent line
        lines[i] = new_row
        break
content = '\n'.join(lines)
```

This avoids the full-line Unicode match problem entirely by matching only an ASCII-only substring.

### 4. Extract `old_string` directly from the file

When using `patch`, get the exact text from the file using terminal:

```bash
# Get exact bytes of lines around your target
sed -n '248,249p' entities/hugo-bowne-anderson.md | cat -A
# This shows all invisible chars, trailing spaces, and exact Unicode
```

Then use this output (without `cat -A` markers) as your `old_string`.

## Real Failure (2026-07-28)

Newsletter-wiki-ingest run: Enriching `entities/hugo-bowne-anderson.md` with a new O'Reilly harness guide row in the Key Collaborations table.

```python
# The Python script used:
old_table = "|| [Build Your Own Deep Research Agent](...) | Ivan Leo | From raw Gemini API call → clarifying questions..."
# This failed silently — content returned unchanged.

# The fix was `patch`:
patch(
    path="entities/hugo-bowne-anderson.md",
    old_string="|| [Build Your Own Deep Research Agent](...) | Ivan Leo | From raw Gemini API call → clarifying questions...",
    new_string="|| [Build Your Own Deep Research Agent](...) | Ivan Leo | ...\n|| [How to Build an Effective Agent Harness](...) | O'Reilly Lightning Lesson | ..."
)
# This succeeded: diff showed the correct row was added.
```

**Root cause**: The file's Unicode right-arrow `→` (U+2192) was different from the Python string's `→` — they looked identical in the terminal but had different byte sequences. The `patch` tool's fuzzy matching handled this transparently.

**Lesson**: When Python `str.replace()` on markdown content silently fails:
1. Try `patch` first — it handles Unicode variants via fuzzy matching
2. If `patch` also fails, use substring matching with line-indexed replacement
3. Never assume the visible characters are the actual Unicode bytes in the file
