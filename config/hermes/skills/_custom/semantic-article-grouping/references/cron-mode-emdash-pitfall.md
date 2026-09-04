# Cron-Mode Patch Pitfall: Em-Dash (U+2014) in Python Scripts

## Problem

When writing Python scripts to `/tmp/` via `write_file` and executing via `terminal python3` in cron mode, Unicode em-dashes (`—`, U+2014) embedded in triple-quoted string literals may trigger:

```
SyntaxError: invalid character '—' (U+2014) (line 60, column 386)
```

This happens because `write_file` preserves raw bytes without explicit encoding declarations, and Python's UTF-8 source parser can reject certain Unicode codepoints depending on positional context within the file. The error appears even though the em-dashes are inside valid Python string literals.

## Fix

1. **Replace em-dashes with two hyphens (`--`) or plain hyphens (`-`)** in Python scripts written via `write_file`. This is safe because the text is destined for JSON or markdown, where hyphens are acceptable alternatives.
2. **Prefer the `patch` tool directly** for entity page body modifications instead of writing a Python script to `/tmp/`. The `patch` tool handles Unicode natively without encoding issues.

## Validated

July 2026: blog-wiki-ingest enrichment script with em-dashes in triple-quoted `better_models_section` variable string failed to parse after `write_file`. Switching from Python script to direct `patch` tool calls for each individual edit resolved the issue cleanly. The entire enrichment (2 entity pages, 8+ text edits) was completed without further Unicode issues.

## Related

- Main SKILL.md Pitfall: "Unicode text in scripts" — covers Japanese text (CJK) via `write_file`, but does not cover em-dashes
- The `patch` tool uses fuzzy matching and handles Unicode natively, making it the preferred approach for entity page edits in cron mode
