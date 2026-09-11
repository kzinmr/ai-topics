# Concurrent Wiki Writers: Clobber Detection & Recovery

Multiple cron pipelines (newsletter-wiki-ingest, blog-wiki-ingest, active-crawl,
dreaming, wiki-watchdog) write to `~/wiki` — often as sibling subagents in the
same session. Collisions are real and have silently destroyed content.

## Known collision modes (observed)

1. **Full-file clobber via write_file.** A sibling subagent wrote a 36-line stub
   over a 951-line entity page (`entities/simon-willison.md`). Detected only
   because `git status` showed a huge modified file. The stub looked plausible —
   content sanity requires a size/line-count check, not just existence.
2. **Silent external modification mid-session.** The `patch` tool returns
   `_warning: "... was modified by sibling subagent '<id>' but this agent never
   read it"`. Treat this as: RE-READ the file before re-applying your edit;
   do not assume your prior read is still valid.
3. **Shared /tmp path collisions.** Scratch files like `/tmp/logentry.md` can be
   overwritten by another subagent writing the same path. Use session-unique
   tmp names (`/tmp/<jobid>_logentry.md`) or append idempotently with a
   grep-before-append guard (e.g. `grep -q "<unique heading>" log.md || cat /tmp/entry.md >> log.md`).

## Pre-write guard (before any write_file on a wiki page)

```bash
cd ~/wiki
git status --short <path>          # unexpected 'M'? someone else touched it
wc -l <path>                       # plausibility vs your last read
git diff <path> | head -40         # inspect foreign changes before overwriting
```

If `git diff` shows changes you didn't make: read the current file, merge
semantically, or `git checkout -- <path>` to restore the committed version and
re-apply ONLY your additive edit via `patch` (never write_file over a page you
didn't fully re-read).

## Recovery

- `git checkout -- <path>` restores the last committed version — this is the
  undo for a clobber, as long as you hadn't committed the damage.
- ALWAYS run `git diff --stat` before `git add` in the commit step. A single
  entity page showing thousands of deleted lines = stop and investigate.
- Commit EARLY in a long crawl session (one commit per topic cluster, not one
  at the very end). The 2026-09-05 active-crawl run hit its tool budget with
  an uncommitted Astra source recovery sitting on disk; a crash between writes
  would have lost it AND made clobber detection harder. Commit after each
  topic cluster, push at the end with the retry loop.

## Serialization note

If repeated collisions are observed, prefer delegate_task batches that touch
DISJOINT files, or serialize page writes in the parent rather than fanning them
out to subagents. Cross-cutting files (`index.md`, `log.md`) should only ever be
written by the parent agent, once, near the end of the run.

## Index-edit pitfalls (index.md is the highest-contention file)

- The `patch` tool can partially corrupt an index line when old_string matches a
  prefix of a longer line — an observed result was a truncated entry. Always
  include a full line + the next line as context in old_string, and verify with
  `sed -n '<line>p' index.md | cut -c1-120` after each index patch.
- Index header counts (`Total pages`, per-section counts) drift constantly in
  multi-writer sessions; recompute with `find entities concepts comparisons queries -name '*.md' | wc -l` at commit time rather than incrementing from a remembered value.
