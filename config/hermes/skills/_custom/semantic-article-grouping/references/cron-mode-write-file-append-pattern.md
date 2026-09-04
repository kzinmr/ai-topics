# Cron-Mode Write-File Append Pattern

## Problem: `#` Comments Inside Dict/List Literals

When building a triage JSON by writing the entire decisions list as one Python dict literal with embedded `#` section headers (e.g., `# === TAKES ===`), the `write_file` linter may fail with:

```
SyntaxError: unterminated string literal (detected at line N)
```

The string in question is correctly quoted. Root cause: the linter's parser gets confused by `#` comments nested **inside** a complex multi-level dict/list literal (10+ items deep). This is a **linter limitation**, not a Python syntax error.

## Fix: Append Pattern

Instead of one monolithic dict literal with inline comments:

```python
# ❌ Triggers linter error
output = {
    "checkpoint_run_id": "...",
    "decisions": [
        # === TAKES ===
        {"item_id": "...", "recommended_action": "take"},
    ]
}
```

Build the list incrementally:

```python
# ✅ Works with linter
output = {"checkpoint_run_id": "...", "decisions": []}

# === TAKES ===
output["decisions"].append({"item_id": "...", "recommended_action": "take"})

# === REFERENCES ===
output["decisions"].append({"item_id": "...", "recommended_action": "reference"})
```

## Why

- `#` comments stay at **script top level**, not inside a nested literal
- Linter parses each `.append()` independently
- Individual items can be commented out during development

## Detection

If `write_file` reports `SyntaxError: unterminated string literal` and the quoted string is correct, look for `# comments` inside the dict/list literal.

## Observed

- **Jul 2, 2026**: newsletter-triage cron. 11-item array with 3 section-header comments inside the literal. Linter flagged line 21 (a correctly-quoted `body_excerpt`). Actual cause: `# === REFERENCE (4) ===` on line 23. Switching to `.append()` resolved it.
