# Stale Un-Popped Stashes: Verify Supersession Before Dropping

Applies to every commit-capable wiki cron (active-crawl, newsletter-wiki-ingest,
blog-wiki-ingest, x-accounts-scan, hot-post). These crons sometimes `git stash push -u -m "..."`
to push cleanly past sibling WIP; if the pop step is skipped (crash, context exhaustion), the
stash sits un-popped for days. Do NOT silently drop it and do NOT silently keep it forever.

## Verification recipe (read-only until the final decision)

1. `git stash list --date=iso` — check the age.
   - **<24h old**: treat as live sibling WIP — leave it alone entirely this run.
   - **Multi-day old**: supersession candidate, continue.
2. `git stash show --name-only stash@{0}` — list the files the stash touched.
3. Per file, see whether the file evolved after the stash was created:
   `git log --oneline $(git rev-parse stash@{0}^)..HEAD -- <file>`.
   Commits there mean later runs touched the same files.
4. Compare stash content against HEAD:
   - `git diff stash@{0}^ stash@{0} -- <file> | head` — what the stash would add.
   - `git show HEAD:<file> | grep '<added line>'` — is it already on main?
5. Cross-check the current working tree: if any file in the stash list is ALSO currently
   modified (`git status --porcelain`), another pipeline is actively editing it — do not
   touch the stash this run.
6. Decision:
   - **Every stash-only hunk already on main** → fully superseded. Still: in an unattended
     cron, do NOT drop. Report to the user with `git stash drop` + `git stash show -p stash@{0}`
     so they can eyeball first.
   - **Any hunk absent from HEAD and from the working tree** → unique work remains. Leave the
     stash; flag it for pop (or manual recovery), never drop.

A less conservative alternative, valid when you have verified unique work remains and the tree is otherwise idle: `git stash pop` immediately followed by the conflict-resolution recipe below.

## Session evidence (2026-10-02 active-crawl): pop + conflict resolution worked

The same Sep-28-era stash was still sitting there a few days later (still "active-crawl: sibling pipeline WIP"). This run popped it instead of dropping, because steps 3–4 showed unique hunks absent from HEAD (ai-control's trace-integrity / instrumental-monitor-evasion Related-Concepts links had NOT been re-committed — the 09-30 run's supersession conclusion was wrong for that file).

Pop hit a conflict: a later commit had added a "Quantifying the Stack" section + reliability-theory link to the same Related-Concepts block. Both sides were purely additive, so resolution = keep both, delete conflict markers via `patch`. Then:

1. `git add <resolved-file>` to clear the unmerged path (fixes the "could not write index" pop error).
2. `git reset -q` — unstage everything so the restored sibling WIP stays working-tree-only and isn't committed under your message.
3. `git stash drop` — pop keeps the entry when the merge needed resolution; it does NOT auto-drop. Verify with `git stash list` (empty).

Pop-vs-drop decision shortcut: if the stash's unique hunks are still absent from HEAD, pop-and-resolve; if every hunk is already on main, report-the-drop per the conservative recipe above.

## Prevention: make stash round-trip atomic

The pop must happen in the same tool-call chain as the push that motivated the stash. If compaction or context exhaustion interrupts between `git push` and `git stash pop`, the next commit-capable cron run must check `git stash list` FIRST — a non-empty stash with your own pipelines' message means you owe the pop before doing anything else.
