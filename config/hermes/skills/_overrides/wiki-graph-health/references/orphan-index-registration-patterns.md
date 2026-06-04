# Orphan Index Registration — Patterns & Pitfalls

From 2026-05-27 session: 767 orphans processed into 21 index entries.

## Pre-Filter Decision Matrix (767 → 21 candidates)

Apply in order. Each skip is a hard filter — the remaining candidates are the only ones worth processing.

| Step | Criteria | Code | Typical hit rate |
|------|----------|------|------------------|
| 1 | `_index` files (synthesis hubs) | `slug == "_index" or slug.endswith("/_index")` | 10-20 skipped |
| 2 | Date-prefixed slugs (misplaced raw articles) | `re.match(r'^\d{4}-\d{2}-\d{2}', slug)` | 3-5 skipped |
| 3 | @-prefixed slugs (redirect/utility pages) | `slug.startswith("@")` | 1-2 skipped |
| 4 | Subdirectory paths (handled by `_index.md`) | `'/' in slug` | 50-100 skipped |
| 5 | TODO-only stubs | `len(body_text) < 500 and 'TODO' in body_text` | 500-600 skipped |
| 6 | Already indexed (both namespaces) | `f"concepts/{slug}" in existing_wikilinks` | 5-10 skipped |
| 7 | File doesn't exist on disk | `os.path.exists(path)` | 0-5 skipped |
| **Remaining** | Real pages that need index entries | — | **20-30% of original** |

From 2026-05-27: 767 → 214 real candidates (28%). The pre-filter removed 553 false positives.

## Batch-Append for Drifted Sections

When the concepts section has visible non-alphabetical drift (e.g., `agents-that-build-themselves` after `ai-agent-memory-middleware`), individual alphabetical insertion is unreliable. Use batch-append at the section boundary:

```python
# Find section boundary
events_start = content.find('\n## Events')

# Append all entries between last concept entry and next section header
ecs_line = '- [[concepts/ecs-fargate-scaling]]'
pos = content.find(ecs_line)
if pos >= 0:
    eol = content.find('\n', pos)
    content = content[:eol+1] + ''.join(concept_entries) + '\n' + content[eol+1:]
```

Proven on 17 entries in one pass (2026-05-27).

## Fresh-Process Trap

**`execute_code` calls are independent Python processes.** Modifications to `content` in one call do NOT persist to the next. Always write to disk in the same call:

```python
# ✅ CORRECT — write in the SAME call
with open(index_path) as f:
    content = f.read()
content = content.replace(old, new)
with open(index_path, 'w') as f:
    f.write(content)

# ❌ WRONG — next execute_code starts from the original file
with open(index_path) as f:
    content = f.read()
content = content.replace(old, new)
# ... next execute_code call reads original file, not modified content
```

## Quote-Escaping: File-Based Script Approach

When the Python script has complex string operations (multiple `str.replace()` calls with nested quotes, multi-line f-strings, backtick-wrapped URLs like `` `raw/articles/file.md` ``), inline `execute_code` can fail with `SyntaxError`. Write to a temp file instead:

```python
write_file(path="/tmp/fix_index.py", content=python_script)
terminal("python3 /tmp/fix_index.py")
```

This bypasses all quoting / nesting / backtick-substitution issues, because the script is saved to disk first and executed as a standalone program with raw file I/O.

**Proven on**: 17-entry batch + 3 individual insertions + 5 header count updates in one script (2026-05-27).

## Relation to wiki-health-fix Cron

The `wiki-health-fix` job (17:50 UTC) processes orphans as part of auto-fix. It currently applies max 20 orphan_index entries per run. The pre-filter happens first within the session logic.

## Scale Impact

From the 2026-05-27 session: the pre-filter pipeline reduced 767 reported orphans to 21 actual index entries (skipped 546 TODO stubs, 17 `_index` files, 3 date-prefixed, 1 @-prefixed, 8 already-indexed, 0 missing files).