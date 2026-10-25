# Parallel sibling jobs + targeted git add (newsletter-wiki-ingest, 2026-10-23)

## The hazard
In the 07:00–11:00 UTC window several cron jobs write to `wiki/` concurrently
(blog-ingest/triage/wiki-ingest, newsletter-ingest/triage/wiki-ingest, dreaming,
x-bookmarks, active-crawl). A sibling subagent may commit **mid-run** and sweep
your *staged* files, or leave a pile of uncommitted changes in the shared working
tree while you are committing. Observed 2026-10-23: at commit time `git status`
showed ~15 uncommitted `wiki/entities/*.md` (anthropic, coreweave, dwarkesh-patel,
gary-marcus, sierra, simon-willison, …) plus ~35 untracked `raw/articles/*` from
the sibling blog pipeline, AND a sibling subagent (`d22a9aa8…`) had just modified
`wiki/index.md` (the exact file I was about to patch).

## The fix: targeted `git add`, never `git add wiki/`
- Stage ONLY the files this run created/modified, by exact path. Never blanket
  `git add wiki/` — that sweeps the sibling's in-progress pages into your commit.
- Run `git status --short` right before staging and eyeball which entries are
  yours (`M ` staged vs ` M` sibling-unstaged).
- This satisfies AGENTS.md's sibling-sweep guardrail at ingest time rather than
  only in the post-recovery section.

## Patching a file a sibling is also editing
- Use anchored `patch` (unique multi-line `old_string`), not `write_file`. An
  anchored patch applies cleanly even if a sibling added unrelated lines elsewhere.
- If `patch` returns the "modified by sibling X but this agent never read it"
  warning, re-read the file first, then patch again — the write still applies but
  the warning means your read was stale.

## Push when rebase is blocked by sibling dirt
- `git pull --rebase` FAILS with "cannot pull with rebase: You have unstaged
  changes" when siblings left the working tree dirty. Do NOT stash/reset (you'd
  clobber their work).
- The commit is already local; a plain `git push` fast-forwards fine as long as no
  new remote commits landed (`78c6f38e..9b086d9f main -> main` succeeded with the
  rebase blocked). Only `git pull --rebase` AFTER the sibling commits settle.

## Commit-message shell safety
Message contained `$16B` / `$1B` — wrapped the whole `-m '...'` in SINGLE quotes so
shell does not expand `$16B`. (AGENTS.md rule; the `$`-dollar variant is just as
dangerous as `&`.)

## Verification before push
`git show --stat HEAD` — every non-skip `candidate_wiki_path` from triage must
appear in the diff. Here: 6 wiki pages (anekha-sokhal.md create + 5 updates) +
index + log + 2 archive files = 10 files, matching the 5 take + 2 ref decisions.
