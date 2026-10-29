# Blog-Ingest Stage — 2026-10-28 session notes

## Log-prepend: assert on header STRUCTURE, not on "# Wiki Log" occurrence count

The naive 3-invariant assertion set from `log-prepend-header-repair.md` includes `assert c.count("# Wiki Log") == 1`. This **false-fires** on the real log.md: historical entries and self-referential repair notes quote the literal string (e.g. a line reading "Fixed `wiki/log.md`: `# Wiki Log` header was buried at line 4..."). Confirmed 2026-10-28 — the assertion aborted the script after the header was already fine; required `git checkout HEAD -- wiki/log.md` and a rewrite.

**Working pattern (validated 2026-10-28, terminal heredoc, no execute_code):**

```python
with open(log_path) as f:
    lines = f.read().split("\n")
assert lines[0] == "# Wiki Log"          # structural, not occurrence-count
out = "\n".join(lines[:4]) + "\n" + new_entry + "\n".join(lines[4:])
with open(log_path, "w") as f:
    f.write(out)
# post-write verify: startswith the exact header block + entry present
with open(log_path) as f:
    c = f.read()
assert c.startswith("# Wiki Log\n\n_Log of all wiki changes")
assert "<unique-substring-of-new-entry>" in c
```

Header block is the first 4 lines: `# Wiki Log`, ``, `_Log of all wiki changes. Newest entries at top._`, ``. Never assert `count("# Wiki Log") == 1` — instead assert `startswith("# Wiki Log")` and that the entry substring is present.

## Run shape confirmed again (per 2026-10-27 notes)

~10 terminal/skill calls total: verify saved raw files with one `stat` loop → `git add wiki/raw/articles/` → commit → push → prepend log (above) → commit log → push. No Layer-2 page edits. Sweep untracked `wiki/raw/articles/` backlog from prior failed runs; never stage sibling-pipeline modifications outside `wiki/raw/`.

## Checkpoint quirks re-confirmed

`scan.total_new` (36) = DB-wide new count; `articles.total` (20) = per-run fetch cap subset saved; `blogs_scanned=0` with nonzero total_new is the known cosmetic bug — DB count match means no re-scan needed. `unsaved_articles` empty = clean run.
