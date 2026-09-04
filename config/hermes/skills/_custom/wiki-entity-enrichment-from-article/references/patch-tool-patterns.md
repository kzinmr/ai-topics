# Patch Tool Patterns for Wiki Editing

> Practical patterns for using the `patch` tool on wiki files. Based on session experience with large multi-section concept pages.

## Mode Selection

The `patch` tool has two modes. Choose based on the edit:

### `replace` mode (default, PREFERRED for wiki edits)
- **Use when**: Targeting a unique string in a single file
- **Parameters**: `mode='replace'`, `path`, `old_string`, `new_string`
- **Strengths**: Fuzzy matching (9 strategies), auto syntax check, unique match required
- **Wiki pattern**: Best for frontmatter updates, adding sections between known anchors, fixing specific lines

```
patch(mode='replace', path='wiki/concepts/foo.md',
      old_string='updated: 2026-06-04',
      new_string='updated: 2026-06-05')
```

### `patch` mode (V4A multi-file)
- **Use when**: Applying multiple coordinated changes across one or more files
- **Parameters**: `mode='patch'`, `patch=<V4A format string>`
- **Strengths**: Multi-file, multi-hunk in one call
- **Weakness**: Context hints (`@@ hint @@`) require **exact line content** from the file

## V4A Pitfalls (Common Failures)

### Pitfall 1: Context hint mismatch
```
*** Begin Patch
*** Update File: wiki/concepts/rlm.md
@@ Context Rot @@
+## Context Rot: The Core Problem
*** End Patch
```
**Fails** because `@@ Context Rot @@` is a section title hint — the tool looks for that exact text in the file. If the actual line is `## Context Rot` (no colon), or if there's no line matching at all, the hunk is rejected.

**Fix**: Use `replace` mode instead for targeted edits. Or use a context hint that matches an actual existing line near the insertion point.

### Pitfall 2: Addition-only hunks
V4A format requires at least one `-` (removed line) per hunk. Pure additions (`+` only) may fail if the context hint can't be resolved.

**Fix**: For additions, use `replace` mode with `old_string` set to the line BEFORE the insertion point, and `new_string` including that line plus the new content.

### Pitfall 3: Multi-hunk on large files
When applying 3+ hunks to a large file (500+ lines), V4A patch mode becomes fragile because each hunk's context must independently resolve. One failing hunk blocks the entire patch.

**Fix**: Apply changes as separate `replace` calls, one per edit point. This is more reliable and gives better error messages.

## Replace-Mode Pitfalls

### Pitfall 4: `read_file` pipe-ambiguity corrupts `old_string` anchors

**When**: You build `old_string` by copying line content from `read_file` output, and the file content starts with `- `, `|`, or `#` — characters that blur with the `read_file` display format.

**What happens**: `read_file` displays lines as `LINE_NUM|CONTENT` where `|` is the separator. When content starts with `- ` (a common markdown list bullet), you see:
```
352|- nesbitt.io — Personal blog and portfolio
```
The first `|` after digits is the separator. The actual file content is `- nesbitt.io — Personal blog and portfolio` (no leading pipe). But it's easy to misread the display as `|- ` and include the phantom pipe in your `old_string`.

**The fuzzy-matching trap**: The patch tool's 9-strategy fuzzy matching may silently accept your pipe-prefixed `old_string` (`|- OSS Summit...`) even though the actual file has `- OSS Summit...` (no pipe). The `patch` succeeds — but it writes the pipe into the file, corrupting the list item with an extra `|` character:

```
# Before (correct):
- OSS Summit NA 2026 panel: "The Impact of Funding"

# After (corrupted):
|- OSS Summit NA 2026 panel: "The Impact of Funding"
```

This is invisible in a quick glance because `read_file` re-displays it as `||- content` — the double pipe looks like a `read_file` artifact but is actually a real corruption.

**Real-world case (2026-06-06)**: While enriching `entities/andrew-nesbitt.md`, both the Sources (which use `- ` list format) and References (which use `- ` format) sections got extra `|` prefixes because `old_string` was built from the displayed `|- ` appearance. Three rounds of fix-patches were needed to clean up.

**Detection**: After any patch that adds/changes lines in list sections:
1. `sed -n 'LINEp' path | cat -A` to check raw bytes — lines with `|` prefix will show `|content` instead of just `content`
2. Or `read_file` the patched region and visually scan for `||` — that indicates the pipe separator PLUS a real `|` in the content

### Prevention
1. **Never trust the pipe in `read_file` display** — always verify with `cat -A` when the `old_string` starts with punctuation
2. For Sources/References sections, use a `sed` one-liner to confirm exact bytes:
   ```bash
   sed -n '352,370p' entities/andrew-nesbitt.md | cat -A
   ```
3. Build `old_string` from `terminal` output, not `read_file` display, for any string starting with `-`, `|`, `+`, or `#`
4. After the patch, re-read the affected lines and verify the diff removed lines match what you expected
5. When in doubt, include MORE context — extend `old_string` to cover an entire paragraph rather than a single line — so the match is unambiguous

6. **Use UNIQUE multi-line anchors**: Instead of a divider line alone, include:
   - The last visible paragraph before the divider
   - The divider itself
   - The heading after the divider
   All three as one `old_string`. This ensures the match only hits your target.

### Pitfall: Multiline old_string matched across separate file regions (fuzzy overreach)

When the `old_string` contains text from two different sections of the file that never appear consecutively, the patch tool's fuzzy matching may **combine them into one match**, matching part of the string at one location and the rest at another.

**Real failure (Jul 2026, geoffrey-litt.md)**: The old_string was the last bullet of X Activity Themes (`7. **Notion & Productivity Software**...`) followed by `## Blog / Recent Posts`. In the actual file, these two text fragments appeared at opposite ends of the file (bullet at line 164, heading at line 131) — **never adjacent**. The patch tool inserted the new section content inside the Academic & Conference Work section (at line 129), leaving a corrupted dangling bullet.

**Detection**: After any multiline patch targeting the end of a file:
1. Read 20 lines before AND after the intended edit point
2. Check that the text before the insertion still leads naturally into the insertion
3. Look for orphan content (bullets that look like they belong in a different section)

**Prevention**:
1. Verify the `old_string` appears as a contiguous block before patching: `grep -n "first-anchor" file && grep -n "second-anchor" file` — if the line numbers are far apart, the string is NOT contiguous.
2. For additions at the END of a file, use the very last line as the anchor: `tail -1 path/to/file`. Then `old_string = last_line_content`, `new_string = last_line_content + \n\nnew_section`.
3. After patching, always re-read the affected area. If content appears in the wrong section, undo with `git checkout -- path/to/file` and retry with a tighter anchor.

### Recovery
If patch inserted content in the wrong location:
```bash
git checkout -- path/to/file.md  # Full restore
# Then retry with a better anchor (tail -1 or grep -n to verify uniqueness)
```

**Related**: `references/read_file-pipe-ambiguity.md` covers the same ambiguity for `execute_code` + `str.replace()` enrichment workflows.

## Wiki-Specific Patterns

### Adding sources to frontmatter
```python
patch(mode='replace', path='wiki/concepts/X.md',
      old_string='  - existing-source-url\n---',
      new_string='  - existing-source-url\n  - new-source-url\n---')
```

### Updating `updated` date
```python
patch(mode='replace', path='wiki/concepts/X.md',
      old_string='updated: 2026-06-04',
      new_string='updated: 2026-06-05')
```

### Adding a section before an existing heading
```python
patch(mode='replace', path='wiki/concepts/X.md',
      old_string='## Existing Section',
      new_string='## New Section\n\nContent here.\n\n## Existing Section')
```

### Adding cross-links at end of Related section
```python
patch(mode='replace', path='wiki/concepts/X.md',
      old_string='- [[entities/last-link]] — description',
      new_string='- [[entities/last-link]] — description\n- [[entities/new-link]] — new description')
```

### Pitfall 6: Truncated old_string retry — fuzzy match corrupts content

**When**: A `patch` call fails with "Could not find a match for old_string". You truncate `old_string` (remove trailing characters) and retry, assuming a shorter anchor will match more easily.

**What actually happens**: The patch tool's 9-strategy fuzzy matching may match the **truncated prefix** of `old_string` against the **full, longer content** in the file. The replacement then overwrites the full content with your truncated version, corrupting the line.

**Real-world case (Jul 2026, blog-wiki-ingest session)**:
- Goal: Fix `||` → `|` pipe prefix on a line
- First attempt: `old_string="||Source: [[raw/articles/simonwillison.net--2026-jul-12-bump--178b751a.md]]"` → failed (because the actual file had single-pipe `|`, not `||`)
- **Wrong retry**: Truncated to `old_string="||Source: [[raw/articles/simonwillison.net--2026-jul-12-directly"` — a URL ending mid-string at `directly` instead of `directly-responsible-individuals--dd90e0f3.md]]`
- Result: The fuzzy matcher matched the prefix `|Source: [[raw/articles/simonwillison.net--2026-jul-12-directly` (with the `|` from the content, not `||` from the old_string because of fuzzy normalization) against the actual source line, replacing the full correct URL with the truncated version
- Recovery: Had to restore the URL with a follow-up patch

**Why this is dangerous**: Truncating `old_string` turns it into a **generic prefix**. The fuzzy matcher considers the first N characters sufficient to identify the match location, then replaces the entire matched span (which is longer than your truncated string) with your `new_string`. This removes content you didn't intend to change.

**Prevention**:
1. **Never truncate `old_string` after a failed match** — truncation makes the match less specific, increasing the risk of fuzzy overreach
2. Instead, **verify the actual file content** with `sed -n 'LINEp' PATH | cat -A` to see exact bytes
3. Build a **longer, more specific** `old_string` that includes surrounding context, not a shorter one
4. If you suspect the issue is a pipe-prefix display artifact (see Pitfall 4), verify the raw bytes before retrying — the content may already be correct

**Recovery**:
```bash
# 1. Find the corrupted line
grep -n "truncated-content" path/to/file.md
# 2. Read surrounding context to reconstruct the correct content  
sed -n 'LINE-2,LINE+2p' path/to/file.md | cat -A
# 3. Patch with full, correct old_string and new_string
patch(path='path/to/file.md',
      old_string='corrupted-content-line',
      new_string='correct-full-content-line')
```

## Anti-pattern: Overwriting Rich Pages

**NEVER** use `write_file` on entity/concept pages with 40+ lines. The pre-commit hook blocks 50%+ content reduction. Always:
1. `read_file` the existing page
2. `patch` to add/update specific sections
3. Verify the diff shows only intended changes

## Pitfall: Partial Read + Broad Match → Accidental Deletion

### What happens
You call `read_file(path, offset=N, limit=M)` to inspect a section, then call `patch()` on the same file. The tool warns:
```
was last read with offset/limit pagination (partial view).
Re-read the whole file before overwriting it.
```
If you proceed, the `patch` may match more content than intended, **silently deleting text between the `old_string` start and the actual replacement target**.

### Real failures (this session, 2026-06-25)

**Case 1 — Key Insight paragraph deleted from meta-harness.md (215→267 lines)**
- Goal: Add a 4th section before `## Cross-Cutting Themes`
- `old_string`: `"|\n\n## Cross-Cutting Themes"` → 6 matches (`|---` appears 6 times)
- Fixed by adding more context, but then the `<old_string>` accidentally matched from `### Key Insight` through `## Cross-Cutting Themes`, deleting the Key Insight paragraph (3 lines) in the replacement
- Root cause: the `|` divider + `## Cross-Cutting Themes` pattern was common, but the additional context (`### Key Insight ... The model weights stay fixed`) expanded the match region instead of narrowing it

**Case 2 — openai.md tags block (14 lines) accidentally deleted**
- Goal: Only update `updated:` date, but `old_string` matched too broadly
- `old_string`: `"updated: 2026-06-25\ntags:\n  - company\n..."` replaced the ENTIRE tags block with nothing (14 lines vanished)
- Root cause: the tags block matched as a multi-line string, and `new_string` was shorter than expected — the tool consumed tags lines as part of the match

### Why this happens
1. **Partial read = stale mental model**: You last read lines 60-66, but `patch` operates on the full file on disk. Content before/after your viewport may match in unexpected ways.
2. **Fuzzy matching**: The tool's 9 strategies may silently absorb adjacent lines into the `old_string` match, especially when `old_string` starts mid-line or on a common divider.
3. **Divider characters (`|---`, `---`, `---`) are dangerous anchors**: These appear many times in wiki files. Using them as the sole `old_string` anchor almost always produces multiple matches or excess match.

### Prevention
1. **After any offset/limit read_file, re-read the full file before patching**:
   ```python
   # Before patching, force a full read:
   read_file(path)  # no offset/limit = full read
   # Now patch is safe
   ```
   Or skip the read_file step entirely and use terminal `grep -n` to find line numbers, then `sed` to check content.

   **Note**: Even without re-reading, `patch` usually succeeds — the warning is advisory. See `references/patch-offset-limit-warning.md` for when the warning matters vs when it's harmless.

2. **Build old_string from terminal output, not read_file display**:
   ```bash
   # Use sed to extract EXACT file content for your anchor:
   sed -n '140,145p' path/to/file
   ```
   Then paste that exact output into `old_string`. This avoids the `N|` display formatting and gives you precise byte-for-byte content.

## Wiki-Specific Patterns

### Adding sources to frontmatter
   # Good: unique anchor spanning 3 distinct structural elements
   old_string="""4. The harness code becomes the search space: context strategies, retrieval methods, tool definitions

---

## Cross-Cutting Themes"""
   
   # Bad: divider alone — 6 matches
   old_string="|---\\n\\n## Cross-Cutting Themes"
   ```

4. **Verify the diff BEFORE confirming**: After the patch runs, check what was actually replaced:
   ```bash
   # Compare lines around the edit point
   sed -n '140,200p' path/to/file
   ```
   If content is missing that should be there, do an immediate recovery patch before continuing.

### Recovery
If `patch` accidentally deleted content:

```bash
# Find the content in git history
git show HEAD:path/to/file.md | grep -n "lost-text"
# Restore just the lost lines with a targeted patch
# OR: stage your other changes, then
git checkout -- path/to/file.md  # restore original
# Re-apply your patch with correct old_string
```

**When recovering, read and include the FULL affected section in old_string — not just the line you lost.** The accidental deletion happened because the match was imprecise; the fix must be more precise, not less.
