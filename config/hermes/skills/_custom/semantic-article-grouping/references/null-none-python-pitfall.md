# null vs None Python Pitfall — Batch Fix Techniques

When building triage JSON dicts in Python scripts (written to `/tmp/` or inline), using `null` instead of `None` raises `NameError`. This is a JS-ism error common when porting JSON-like dict literals.

## Common Sources
- `candidate_wiki_path`, `raw_path`, and any optional field set to `null` instead of `None`
- Copying JSON structure and forgetting to convert `null` → `None`
- The final field in a dict (no trailing comma after `null`)

## Batch Fix Approaches

### Approach A (Preferred — Handles All Whitespace Variants)

Use `sed -i` in terminal, which catches `null` regardless of preceding whitespace or trailing characters:

```bash
sed -i 's/: null,/: None,/g; s/: null/: None/g' /tmp/script.py
```

**Two-pass pattern**: The first pass handles `": null,"` (with comma, mid-dict entries). The second pass handles `": null"` (no comma, last field in dict) and `: null` (unquoted Python in list context). This is the **reliable bulk approach** when 5+ replacements are needed.

**Validation** after fix:
```bash
grep -n 'null' /tmp/script.py  # Should return nothing
python3 /tmp/script.py         # Should run without NameError
```

### Approach B (When `sed` Unavailable or Script Embedded)

Use `patch` with `replace_all=true`:

```
patch(path="...", old_string=": null,", new_string=": None,", replace_all=true)
patch(path="...", old_string=": null", new_string=": None", replace_all=true)
```

**Caveat**: This only catches `": null,"` (with trailing comma) on the first call and `": null"` (no trailing comma) on the second. Instances with different preceding whitespace than the first match may still be missed. If any `null` remains, fall back to Approach A.

## Why `patch` with `replace_all` Can Fail

The `patch` tool's `replace_all=true` performs **exact string matching** — any difference in preceding whitespace (e.g., 8-space indent vs 4-space indent) creates a distinct string pattern. When a triage script has dicts at multiple nesting levels (top-level field, nested dict, list-of-dicts), the whitespace before `null` varies. `sed -i` handles all whitespace levels in one pass.

## Prevention

Always use `None` in Python dict literals, not `null`:
```python
# ✅ Correct
item = {"name": "foo", "url": None}

# ❌ Wrong — NameError
item = {"name": "foo", "url": null}
```

When generating the initial script via `write_file`, do a grep for `null` before running:
```python
# Add to end of script before writing
import re
# ... build decisions ...
# Verify: check for null
def _check_no_null(d):
    if isinstance(d, dict):
        for v in d.values():
            _check_no_null(v)
    elif isinstance(d, list):
        for v in d:
            _check_no_null(v)
# Run _check_no_null(decisions) before json.dumps
```

Validated: July 2026 blog triage (blog_triage_20260725.py: 16 `null` instances survived `patch replace_all`; single `sed -i` pass fixed all).
