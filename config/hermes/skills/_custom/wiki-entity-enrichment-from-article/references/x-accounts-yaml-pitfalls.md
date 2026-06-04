# x-accounts.yaml Addition Pitfalls

When adding new entries to `~/ai-topics/config/feeds/x-accounts.yaml` during entity enrichment:

## YAML Quoting (CRITICAL)

The file uses **single-quoted** YAML strings for the `notes` field. Inside single-quoted YAML strings:
- ✅ Use `''` (two single quotes) to escape a literal single quote: `Amdahl''s Argument`
- ❌ Do NOT use `\'` (backslash-escape) — this is invalid YAML and will break parsing

Example:
```yaml
# WRONG
notes: 'CEO of SID.ai. Writer on Amdahl\'s Argument for AI.'

# CORRECT  
notes: 'CEO of SID.ai. Writer on Amdahl''s Argument for AI.'
```

## Verification

After adding an entry, always verify YAML validity:
```python
import yaml
with open("/opt/data/ai-topics/config/feeds/x-accounts.yaml") as f:
    data = yaml.safe_load(f)
```

If the YAML parser throws `ParserError: expected <block end>, but found '<scalar>'`, the issue is almost always an unescaped single quote in a single-quoted string.

## `sed -i 'N r file'` Semantics

`sed -i 'N r file'` inserts content AFTER line N, not before. To insert before target line T, use `sed -i 'T-1 r file'`.

After any sed insertion, re-grep surrounding lines to verify correct placement — line numbers shift after each insertion.
