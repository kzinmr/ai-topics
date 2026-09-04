# `read_file()` Pipe Display Ambiguity

## The Problem

When using `execute_code` with `str.replace()` for batch enrichment of wiki entity pages, anchors built from `read_file` output can silently fail to match.

`read_file` displays content with line-number prefixes:

```
    50|| **2026-05-17** | Publishes "Article Title" — summary |
```

But the actual file content on disk is:

```
| **2026-05-17** | Publishes "Article Title" — summary |
```

The `    50|` prefix is a display artifact — it does NOT exist in the actual file. Using the `||` version (which includes the visible pipe from the line-number prefix) as an `old_string` anchor in `str.replace()` will silently fail to match, leaving the file unchanged.

## Discovery (2026-05-22 blog-wiki-ingest session)

While enriching `entities/seangoedecke-com.md` via execute_code, a timeline entry replacement failed silently. The `read_file` showed `|| **2026-05-17**` at the start of the line, but the actual file had `| **2026-05-17**`. The extra `|` came from the `    50|` line-number prefix display artifact.

## Fix

Before building `old_string` anchors, use `sed` via terminal to get the exact line content:

```bash
sed -n '50p' wiki/entities/seangoedecke-com.md | cat -A
```

This shows raw bytes with `$` at line endings. The content starts immediately — no line-number prefix.

## Prevention

Always include a pre-replacement assertion in your execute_code enrichment script:

```python
assert old_string in content, f"Anchor not found! Verify with: sed -n 'LINEp' path"
```

## new_string Contamination (June 2026)

The same read_file display artifacts can contaminate **new_string** in patch operations — not just old_string matching failures.

**What happens**: When you build `new_string` from read_file output (which shows `72|- Content`), the `|` from the line-number prefix can end up in `new_string`. The patch tool writes it into the file as `|- Content` instead of `- Content`.

**Real-world case (June 24, 2026)**: `concepts/sakana-fugu.md` — patching the Benchmark Performance section:

- read_file showed `72|- Shoulder-to-shoulder with...` (the `72|` is display-only)
- new_string inadvertently used `|- Shoulder-to-shoulder...` instead of `- Shoulder-to-shoulder...`
- Result: the file had `|- Shoulder-to-shoulder...` which is invalid markdown list syntax
- Detected by re-reading the file; fixed with a second patch

**Detection**: After every patch that targets content read via read_file, `read_file` the patched area and scan for lines starting with `|- ` instead of `- `. The pipe prefix is invalid markdown list syntax.

**Fix**: A second patch replacing `|-` with `-` for the affected lines.

**Prevention**:
- **NEVER copy `new_string` directly from read_file output.** The line-number prefix (`N|`) is not part of the file content
- Build `new_string` from scratch using your knowledge of the file content, or verify with `sed -n 'LINEp' FILE | cat -A` to see raw bytes
- After any patch to markdown list content (bullet points, index entries), always verify the result

## Related Pitfalls

- **`read_file` line-number corruption** (llm-wiki skill): When `read_file` output is pasted directly into wiki files, the `     1|...` prefixes corrupt the markdown.
- **Patch-Based Index Insertion** (llm-wiki skill): Always use visually-confirmed anchor lines, never programmatic insertion points.
