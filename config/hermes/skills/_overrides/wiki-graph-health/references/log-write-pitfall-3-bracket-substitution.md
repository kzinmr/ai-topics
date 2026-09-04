# Log Write Pitfall 3: Bash `[[` Command Substitution on Wikilink Brackets

**Discovered**: 2026-07-11 during wiki-watchdog-fix cron run

## Symptom

After writing a log entry via `terminal("python3 -c \"...\"")` where the inline Python string contains `[[slug]]` or `[[namespace/slug]]` wikilink syntax, the brackets are silently dropped. The output shows:

```
- Fixed **87 bare wikilinks** (e.g.,  → ,  → , ...)
```

The text between the intended `[[anthropic]] → [[entities/anthropic]]` is lost. The log entry is corrupted.

## Root Cause

When Python code is passed inline through `terminal("python3 -c \"...\"")`, bash evaluates the string BEFORE Python sees it. The `[[...]]` pattern (without surrounding spaces around the inner brackets) triggers bash's `[[ expression ]]` keyword. Bash attempts to evaluate:

- `[[anthropic]]` → "command not found" (bash tries to run `anthropic` as a test command)
- `[[entities/anthropic]]` → same failure

Results: The failed command is replaced with empty string in the output, and the error message appears in stderr.

## Comparison to Existing Pitfalls

| Failure | Trigger | Signal |
|---------|---------|--------|
| **F1** (2026-05-13) | `---` as `old_string` in `patch` | Content split/corrupted at wrong location |
| **F2** (2026-05-20) | Backticks `` ` `` in Python string via bash | Content swallowed, `command not found` |
| **F3** (2026-07-11) | `[[...]]` brackets in Python string via bash | `[[anthropic]]: command not found`, brackets dropped |

All three share the same root cause: **inline Python-in-bash-strings** (`terminal("python3 -c \"...\"")`) exposes Python content to bash evaluation of special characters.

## Prevention

Always use one of these safe alternatives when the log entry content contains `[[`, backticks, or `---`:

### Option A: write_file + python3 (preferred for complex entries)

```python
write_file(path='/tmp/append_log.py', content="""\
import os
log_path = os.path.expanduser("~/wiki/log.md")
with open(log_path) as f: content = f.read()
new_entry = "## [2026-07-11] watchdog | Auto-fixed 87 bare wikilinks\\n\\n### Changes\\n- Fixed 87 bare wikilinks (e.g., [[anthropic]] → [[entities/anthropic]])\\n\\n---\\n\\n"
with open(log_path, 'w') as f: f.write(new_entry + content)
print("OK")
""")
terminal(command='python3 /tmp/append_log.py')
terminal(command='rm /tmp/append_log.py')
```

### Option B: cat >> with single-quoted heredoc (safe for non-Unicode content)

```bash
cat >> ~/wiki/log.md << 'EOF'
## [2026-07-11] watchdog | Auto-fixed 87 bare wikilinks

### Changes
- Fixed 87 bare wikilinks (e.g., [[anthropic]] → [[entities/anthropic]])
---
EOF
```

The single-quoted delimiter `'EOF'` prevents ALL shell expansion — no `[[`, backtick, or variable evaluation.

### Option C: patch() targeting last unique line

Find a genuinely unique line near the end of log.md and use it as `old_string`. Verify uniqueness with `grep -c "line" wiki/log.md`. Do NOT use `---` as the anchor.
