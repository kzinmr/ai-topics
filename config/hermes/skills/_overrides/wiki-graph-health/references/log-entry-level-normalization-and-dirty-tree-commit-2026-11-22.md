# Log.md Entry-Level Normalization & Dirty-Tree Commit Recipe (2026-11-22)

Health-fix cron session notes. Two lessons complement `log-prepend-header-burial-and-cron-tool-blocks-2026-11-02.md`.

## 1. `fix_log_header_burial.py` fixes the H1 header, NOT entry levels

The script restores a buried `# Wiki Log` header to line 1 but leaves recent entries at whatever heading level the prepending pipeline wrote them. Observed 2026-11-22: watchdog and active-crawl jobs prepend entries as `# [YYYY-MM-DD] ...` (H1) instead of the canonical `## [YYYY-MM-DD] action | title` (H2). After running the burial fixer, log.md had 1 correct H1 header but 2 stray `# [` H1 entries.

**Detection (run every health-fix session):**
```bash
grep -c '^# Wiki Log' wiki/log.md   # must be exactly 1
grep -c '^# \[' wiki/log.md          # must be 0 — any hits are mis-leveled entries
grep -c '^## \[' wiki/log.md          # canonical entry count (report this number)
```

**Fix (one-shot, H1 log entries → canonical H2):**
```python
import re, os
p = os.path.expanduser("~/ai-topics/wiki/log.md")
c = open(p).read()
fixed = re.sub(r'^# \[(\d{4}-\d{2}-\d{2})\] (.*)$', r'## [\1] \2', c, flags=re.MULTILINE)
open(p, 'w').write(fixed)
```

**Order of operations (2026-11-22 proven sequence):**
1. `python3 ~/ai-topics/config/hermes/skills/_overrides/wiki-graph-health/scripts/fix_log_header_burial.py` (restore header if buried)
2. Normalize `# [` entries → `## [` (snippet above)
3. Prepend your own health-fix entry (write_file → /tmp/x.py → terminal python3)
4. Re-run `fix_log_header_burial.py` LAST (your prepend re-buries the header — guaranteed)
5. Verify: `head -3` shows `# Wiki Log`, `grep -c '^# \['` = 0, then commit

## 2. Dirty working tree from sibling cron jobs — skip pull, scope-stage, still push

`git pull --rebase` fails with `cannot pull with rebase: You have unstaged changes` when sibling ingestion jobs (dreaming, blog-wiki-ingest, watchdog, semantic-article-grouping) are mid-run holding uncommitted SKILL.md / references/ edits.

**Do NOT** stash, reset, or commit the siblings' files — they own that work.

**Do:**
1. Skip the pull (origin/main is a fine base; your wiki files were unaffected)
2. Scope-stage only your files: `git add wiki/log.md` (never `git add -A`)
3. `git commit` (pre-commit tag validator runs and passes on scope-staged set)
4. `git push` — fast-forwards off origin/main fine even with a dirty tree; verified 2026-11-22 (commit c1bb1cdd7 pushed with 10 sibling files still dirty)

## 3. Digest-vs-live header counts

The wiki_health digest `## Concepts` counts can lag what a same-day watchdog job already corrected (digest said 2381, watchdog had bumped header to 2385, live section count = 2385). Always recount from index SECTION slices (`^\|?- [[ns/` between `## Concepts` and next `^## `) before trusting either the digest or the header.
