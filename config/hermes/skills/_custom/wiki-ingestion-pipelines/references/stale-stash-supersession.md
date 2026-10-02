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

## Session evidence (2026-09-30 active-crawl)

A Sep-28 stash ("active-crawl: sibling pipeline WIP", 10 files: ai-control trace-integrity
links, ai-energy, ai-skepticism-movement, space-gpus, odyssey-ml, dimillian, agent-skills,
x-account-enrichment SKILL.md + refs, wiki-watchdog override) survived 2 days. Steps 3-4
confirmed all content had been re-committed to main by later runs (e.g. the stash's
agent-trace-integrity / instrumental-monitor-evasion links on ai-control existed in later
commits). Concluded fully superseded; reported with the drop command rather than dropping
autonomously.
