# Cron-Mode Log Prepending (When `execute_code` Is Blocked)

## Problem

The `llm-wiki` skill's "Preferred alternative" for log.md prepending recommends using `execute_code` with Python `with open()`:

```python
with open(log_path) as f: content = f.read()
with open(log_path, 'w') as f: f.write(new_entry + content)
```

**This does NOT work in cron mode.** `execute_code` is blocked with:

```
BLOCKED: execute_code runs arbitrary local Python (including subprocess calls
that bypass shell-string approval checks). Cron jobs run without a user
present to approve it.
```

## Solution: `patch` with Multi-Line Anchor

Use `terminal()` + `patch()` instead. The key is to use a **long, unique multi-line anchor** spanning the first chronological entry's header line AND its first content line.

### Step-by-Step (proven 2026-06-01)

```bash
# 1. Read the first chronological entry header + first content line
sed -n '3,4p' ~/ai-topics/wiki/log.md
```

This gives you clean `N|`-free content like:
```
## [2026-06-01] blog-wiki-ingest | 5 articles processed

- **New concept**: [[concepts/ai-agent-video-editing]] — AI agent video editing meta-pattern:
```

```python
# 2. Construct a unique multi-line anchor from the header + first content line
#    new_string = your new entry + the old_string (preserving existing content)
patch(
    old_string="## [2026-06-01] blog-wiki-ingest | 5 articles processed\n\n- **New concept**: [[concepts/ai-agent-video-editing]] — AI agent video editing meta-pattern:",
    new_string="""## [2026-06-01] new-entry | Subject

### Details
- ...

---

## [2026-06-01] blog-wiki-ingest | 5 articles processed

- **New concept**: [[concepts/ai-agent-video-editing]] — AI agent video editing meta-pattern:""",
    path="~/ai-topics/wiki/log.md"
)
```

### Key Rules

1. **Use `sed -n 'N,Mp' path` for reading** — never `read_file` (its `N|` prefix format corrupts patch anchors)
2. **Anchor = header line + first content line** — this provides enough uniqueness without crossing `---` boundaries
3. **Preserve ALL lines from old_string in new_string** — every line in old_string must reappear in new_string, otherwise `patch` silently drops it
4. **Verify after each patch** — `head -5 ~/ai-topics/wiki/log.md` must show:
   ```
   # Wiki Log
   > Chronological record...
   
   ## [YYYY-MM-DD] your_entry | ...
   ```
5. **Never use bare `---` as a patch anchor** — it matches the first occurrence (often YAML frontmatter delimiters, not the intended section separator)

### Why This Works

The multi-line anchor approach works in cron mode because:
- `patch()` is NOT blocked by cron restrictions (it's a file-editing tool, not arbitrary code execution)
- A header + content-line anchor is unique enough that `patch` finds the right insertion point
- The full content of old_string is preserved in new_string, so no lines are dropped
- The `---` anchor trap is avoided entirely
