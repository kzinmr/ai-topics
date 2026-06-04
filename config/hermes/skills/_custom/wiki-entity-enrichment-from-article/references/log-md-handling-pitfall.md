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

## Rule of Thumb

- `write_file` → safe for **new files** (raw articles, new wiki pages)
- `patch` → safe for **section updates** in existing pages (entity enrichments, concept updates)
- **Shell prepend** → the ONLY safe way to update log.md
