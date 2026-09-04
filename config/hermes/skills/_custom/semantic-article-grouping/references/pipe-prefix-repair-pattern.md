# Pipe-Prefix Index Repair Pattern

## Problem

When the `read_file` tool's line-number display (`1198|- ...`) is accidentally copied into a `patch()` call's `new_string`, the index.md ends up with `|-` prefixes instead of `-`. This triggers the pre-commit hook's Pitfall 1 (pipe-prefixed list items) on the NEXT commit.

## Detection

The pre-commit hook flags the issue. Also visible as visual corruption: `|- [[concepts/foo]]` instead of `- [[concepts/foo]]`.

## Repair

Use `patch()` with `replace_all=true` to bulk-fix all instances:

```python
patch(
    path="/opt/data/ai-topics/wiki/index.md",
    old_string="|- ",
    new_string="- ",
    replace_all=True
)
```

**Note the trailing space in both strings** (`"|- "` not just `"|-"`) — this prevents accidentally matching non-index patterns like markdown table separators or code blocks that happen to contain `|-`.

## Verification

```bash
head -5 ~/ai-topics/wiki/index.md  # Confirm first lines start with bare `-`
grep -n '^|- ' ~/ai-topics/wiki/index.md | head -5  # Should return 0 matches
```

If the grepped pattern returns results, run the patch again — some instances may have been missed.

## Prevention

Always verify `new_string` content before passing to `patch()` by checking with an explicit `sed` or `cat -A`:

```bash
sed -n '120,125p' ~/ai-topics/wiki/index.md | cat -A
```

The `cat -A` output shows tab/space/line-ending characters and reveals true leading characters.

## Instrumented Example (Jul 2026)

In a newsletter-wiki-ingest session, an index.md patch accidentally introduced `|-` on 3 lines. The fix:
```python
patch(path="wiki/index.md", old_string="|-", new_string="-", replace_all=true)
```
Then also applied to the sub-index:
```python
patch(path="wiki/concepts/claude/index.md", old_string="|-", new_string="-", replace_all=true)
```
Both files repaired successfully. The pre-commit hook passed on the next commit.
