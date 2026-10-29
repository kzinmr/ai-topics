# log.md prepend pitfall: no H1 title line (Oct 2026)

## Symptom

After a cron script prepends a log entry to `~/ai-topics/wiki/log.md`, `head -6 wiki/log.md` shows:

```
## [2026-10-25 10:20 UTC] blog-triage | run 20261025T100040Z
- Input: ...
...
- Archive: ...



## [2026-10-25 00:30 UTC] hot-post | Morning 09:30 JST — ...   <-- present in the GOOD case
```

In the BAD case the previous entry's `## [...]` heading is gone and its bullets sit orphaned under your new entry.

## Root cause

This repo's `log.md` has **no `# Wiki Log` H1** — the file starts directly with the newest `## [date] pipeline | title` heading. The common prepend idiom:

```python
for i, l in enumerate(lines[:10]):
    if l.startswith("# "):   # ← matches the newest entry's "## " too
        hdr = i
```

matches the newest entry's own `## ` heading, so `lines[hdr+1:hdr+1] = entry` inserts *below* it and the next write drops it — silently destroying the prior entry's heading (its body survives, so keyword greps still hit).

## Fix

Two safe patterns:

1. **Anchor on the entry-heading form**, not `# `:
   ```python
   idx = next(i for i, l in enumerate(lines) if l.startswith("## ["))
   lines[idx:idx] = entry + [""]
   ```
2. **Rebuild from git** (simplest, self-correcting):
   ```python
   import subprocess
   prior = subprocess.run(["git","show","HEAD~1:wiki/log.md"],
                          capture_output=True, text=True).stdout.splitlines()
   mine = cur[2:11]                      # my heading + bullets from the broken file
   assert mine[0].startswith("## [") and "my-run-id" in mine[0]
   open(p,"w").write("\n".join(mine + [""] + prior) + "\n")
   ```

## Verification (mandatory after every prepend)

```bash
head -6 wiki/log.md        # your heading first, previous ## [...] still present below
git diff --stat -- wiki/log.md   # should be ~ +N lines only, not -1 of a heading
```

If the diff shows a removed `## [` line, restore immediately with pattern 2 and commit as
`wiki: restore <title> heading stripped by log prepend (<run_id>)`.

Validated 2026-10-25, blog-triage run 20261025T100040Z (the hot-post entry heading was stripped
and restored in commit `10fb4343`).

## Related: sibling-parallel commit & push safety

The `startswith("## [")` anchor above is also **robust to sibling subagents prepending their own
entries** between your read and write (it re-finds the first heading at run time). And when a
sibling leaves uncommitted working-tree edits, `git pull --rebase` aborts with "cannot pull with
rebase: You have unstaged changes" — but a clean fast-forward `git push` still succeeds. Trust the
push output (`old..new main -> main`), not the pull error; do not re-run ingest. Full detail +
beehiiv-403 direct-slug recovery re-confirmation: `references/wiki-ingest-log-claim-vs-applied-content.md`.
