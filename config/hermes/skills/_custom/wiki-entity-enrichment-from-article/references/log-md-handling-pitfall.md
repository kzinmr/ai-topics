# log.md Handling Pitfall

## Problem

`write_file` on `wiki/log.md` **OVERWRITES** the entire file — it destroys all log history. Log entries are prepended (newest first).

## Safe Method — Shell Prepend

```bash
# Create entry file first (use write_file for this since /tmp/ is safe)
# Then prepend:
cat /tmp/entry.md log.md > /tmp/new_log.md && mv /tmp/new_log.md log.md
```

## Recovery (if overwritten)

Use Python + git to recover:

```python
from hermes_tools import terminal
# Read original from git
result = terminal("cd ~/ai-topics && git show HEAD:wiki/log.md", timeout=10)
original = result['output']

# Prepend your new entry
with open("wiki/log.md", "w") as f:
    f.write(my_new_entry + original)
```

This is safer than `git checkout -- wiki/log.md` because it preserves uncommitted changes to other files in the repo.

## Why `read_file` Doesn't Work for Recovery

`read_file` truncates content beyond ~5000 lines. If log.md is large (it often is, 1000+ lines), `read_file` will only give you a partial view — you'll silently lose data when you write it back.

## ⚠️ Structure Pitfall: Header Is NOT at the Top (2026-08-09)

`log.md` does **NOT** start with the `# Wiki Log` header. It starts directly with dated entries (`## [YYYY-MM-DD] ...`), newest first; the header/description block sits further DOWN the file after a `---` separator.

A prepend script that "preserves the first 3 lines as header" (splitting on the first few newlines) inserts the new entry **MID-FILE after the previous day's entry** — present but not at the top. Fixing it requires removing the misplaced duplicate and re-prepending, which can double-insert if not careful.

**Correct pattern — always prepend at position 0**:

```python
with open("wiki/log.md", "r") as f:
    content = f.read()
with open("wiki/log.md", "w") as f:
    f.write(entry + content)   # NOT header-preserving split
```

**Verification**: `head -3 wiki/log.md` — the new `## [YYYY-MM-DD]` line must be line 1. Also `grep -c "\[YYYY-MM-DD\] <job-name>" wiki/log.md` should return exactly 1.

## Rule of Thumb

- `write_file` → safe for **new files** (raw articles, new wiki pages)
- `patch` → safe for **section updates** in existing pages (entity enrichments, concept updates)
- **Shell prepend** → the ONLY safe way to update log.md
