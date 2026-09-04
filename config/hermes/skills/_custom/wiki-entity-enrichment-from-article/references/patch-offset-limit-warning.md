# Patch Offset/Limit Warning (Advisory Only)

## The Warning

When using `patch()` on a file that was previously read with `read_file(offset=N, limit=M)` (partial/offset-paginated read), the tool issues:

```
_warning: /path/to/file was last read with offset/limit pagination (partial view).
Re-read the whole file before overwriting it.
```

## Behavior

- **The patch STILL SUCCEEDS** — this warning is **advisory only**, not a blocking error
- The warning exists because `patch` uses fuzzy matching against the file's current on-disk content, not against the in-memory partial read — so the tool is warning you that your `old_string` was constructed from a partial view and may match differently than expected
- In practice, as long as your `old_string` uniquely identifies the target text, the patch works correctly regardless of this warning
- The diff output confirms success: `"files_modified": ["/path/to/file"]`

## When This Happens

Common when enriching long entity pages (500+ lines):

| File | Typical Length | Why Partial Read |
|------|---------------|------------------|
| `entities/simon-willison.md` | 640+ lines | Full read exceeds tool output limits; need offset/limit to find insertion point |
| `entities/andrej-karpathy.md` | 500+ lines | Similar — need to navigate specific sections |
| `wiki/index.md` | 2800+ lines | Effectively always read via offset/limit |

## Workflow That Triggers This

```python
# Step 1: Read a specific section to find the insertion point
content = read_file("entities/simon-willison.md", offset=630, limit=20)
# Find the last section marker

# Step 2: Patch with new content — warning fires
patch(path="entities/simon-willison.md",
      old_string="...last existing line...",
      new_string="...last existing line...\n\n**New entry**...")
```

## Verification After Warning

After getting the warning, verify the patch actually succeeded:

```bash
# Check the file has the expected number of lines
wc -l entities/simon-willison.md

# Check the new content is present
tail -20 entities/simon-willison.md

# Or grep for a unique string from the new content
grep "unique-keyword" entities/simon-willison.md
```

If the line count increased as expected and the new content is present, the patch worked.

## What NOT to Do

- ❌ **Do NOT re-read the file as a workaround**: `read_file(path, offset=1, limit=2000)` then retrying the patch doesn't change the tool's internal state — the warning fires based on offset/limit being set regardless
- ❌ **Do NOT switch to write_file**: The warning does not mean `patch` failed. Switching to `write_file` risks overwriting the entire rich page (see `pre-write-verification.md`)
- ❌ **Do NOT get alarmed**: The word "warning" is strong but the actual risk is minimal. Your `old_string` already targets specific text; the warning is about the context in which you constructed it, not about execution

## When the Warning Signals a Real Problem

Rare edge case: if you constructed `old_string` from the **offset/limit display lines** (which include `N|` line-number prefixes), the patch may match incorrectly. See `references/pre-write-verification.md#markdown-list-content-corruption-read_file-pipe-prefix-trap-validated-2026-07-12` for the pipe-prefix trap.

If you used terminal `sed -n 'LINE,LINEp'` or `head -N` to read raw content (safe — no `N|` prefix), the warning is harmless.

## Real Example (2026-07-28)

```python
# Read entities/simon-willison.md (639 lines) to find the end of July 2026 Updates
read_file(path="entities/simon-willison.md", offset=630, limit=20)

# Patch to add a new entry at the end
patch(path="entities/simon-willison.md",
      old_string='Source: [[raw/articles/simonwillison.net--2026-jul-26-relay-market--f93ad63e.md]]',
      new_string='Source: [[raw/articles/simonwillison.net--2026-jul-26-relay-market--f93ad63e.md]]\n\n**New entry**\nSource: ...'
)

# Warning fired, patch succeeded, file grew from 639 to 642 lines
```
