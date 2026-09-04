# Cron-Mode Enrichment Execution Pitfalls

Session-verified patterns for running wiki enrichment scripts in cron mode. These apply when executing `semantic-article-grouping` post-verification enrichment steps.

## hermes_tools Not Available in Subprocess Scripts

`from hermes_tools import read_file, patch, terminal` fails with `ModuleNotFoundError` when running a Python script via `write_file` → `terminal python3`. The `hermes_tools` module is only available inside `execute_code` blocks.

**Pattern**: Use direct agent tool calls (`read_file`, `patch`, `terminal`) from the agent's own API instead of subprocess imports. Restrict `/tmp/` scripts to pure-Python operations (JSON manipulation, file prepend, string replacement, git commands).

### What Works in Cron-Mode Subprocess Scripts

```python
# ✅ Pure Python — works
import json, os, re
data = json.load(open('/opt/data/.hermes/cron/data/dreaming/triage_latest.json'))

# ❌ Hermes tools — FAILS
from hermes_tools import read_file, patch

# ✅ Direct agent tools from agent session — works
# (Use read_file(), patch(), terminal() directly, not from a script)
```

### Workflow

1. Use `write_file` to write the pure-Python script to `/tmp/` (JSON processing, file prepend, git staging)
2. Use **direct tool calls** (`patch`, `read_file`) from the agent session for wiki page edits
3. Use `terminal` to run the pure-Python script (archiving, log prepend, git commit/push)

## Pipe-Prefix Corruption in Entity/Concept Page Patches

Same pattern as the documented index.md pitfall, but applies to YAML frontmatter in any wiki page. When using `read_file` output as `old_string` for `patch`, the `N|` line-number prefix can get baked in as leading `|` characters:

```
|---         ← WRONG — pipe from read_file display
title: "..." 
```

**Symptoms**: Frontmatter starts with `|---` instead of `---`, pre-commit hook or YAML parser may fail.

**Fix**: Before patching YAML frontmatter:
1. Use `terminal("grep -n 'pattern' file.md")` to confirm exact line content
2. Write `old_string` from scratch, not by copying `read_file` display output
3. If you accidentally bake in pipes, remove with a targeted `patch`:
   ```
   old_string: "|---"
   new_string: "---"
   path: file.md
   ```
   Use enough context (3+ lines) to make the match unique.

## Parallel Enrichment via Direct Tool Calls (Cron Mode)

When running 2+ enrichment tasks in cron mode, you cannot use `delegate_task` for independent parallel enrichment because `delegate_task` is blocked in cron mode. Instead:
1. **Serial enrichment**: Apply each `patch` + `read_file` call sequentially
2. **Batched frontmatter updates**: Update all frontmatter fields first, then add body sections, to minimize `read_file` re-reads
3. **Verify each file after each patch**: Re-read the affected area (not the full file) to confirm the patch applied correctly before moving to the next

**Anti-pattern**: Writing a single large script to `/tmp/` that tries to do all enrichment in one `terminal` call. This fails if any `hermes_tools` import is present.

## Log.md Prepend via Subprocess Script

Since log.md is append-only (newest-first), use a Python script to prepend:

```python
# write_file → /tmp/prepend_log.py
# terminal → python3 /tmp/prepend_log.py

with open(log_path) as f:
    original = f.read()
with open(log_path, 'w') as f:
    f.write(new_entry + original)
```

This works in cron mode because it uses only Python stdlib. No `hermes_tools` needed.

## Files Created This Session

- `2026-06-21_cloudflare_temporary_accounts.md` — Documenting `wrangler deploy --temporary` for cloudflare-agents.md enrichment
- `2026-06-21_elevenlabs_voice_eval.md` — Documenting 6-pillar voice agent evaluation framework for elevenlabs.md enrichment
