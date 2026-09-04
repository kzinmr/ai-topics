# Structural Corruption in `_index.md` Files

## Problem

The `entities/_index.md` file (and potentially other `_index.md` files) accumulates two types of structural corruption over time:

### 1. Line Number Prefix Corruption

Lines develop prefixes like `              22|` or `    120|` at the start, breaking markdown list syntax.

**Pattern**: `^\s*\d+\|` at line start

**Fix**:
```bash
sed -i 's/^\s*[0-9]\+|//g' wiki/entities/_index.md
```

### 2. Pipe Table Corruption

Lines starting with `|- [[` instead of `- [[`. This happens when markdown table syntax leaks into list items.

**Fix**:
```bash
sed -i 's/^\|- /- /g' wiki/entities/_index.md
```

## Why This Happens

- The `_index.md` files are often edited programmatically (batch enrichment, entity generation scripts)
- Some scripts use `read_file` which prefixes lines with `N|` format
- When these prefixed lines are written back without stripping the prefix, corruption propagates
- Pipe characters from table syntax (`|-`) can leak into list items during batch operations

## Verification

After fixing, verify with:
```bash
# Check for remaining line number prefixes
grep -cP '^\s*\d+\|' wiki/entities/_index.md

# Check for remaining pipe table prefixes  
grep -cP '^\|- \[\[' wiki/entities/_index.md

# Should both return 0
```

## Prevention

- Always strip `read_file` line number prefixes (`N|`) when processing `_index.md` content
- Use `patch()` for targeted edits instead of bulk file rewrites
- Verify structural integrity after any programmatic modification
- The watchdog auto-fix job should scan ALL `_index.md` files, not just `index.md`
