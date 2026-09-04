# Ingest-Stage Git Sync (raw articles commit + push)

Gotchas from running the Layer-1 ingest stages (`blog-ingest`, `newsletter-ingest`)
that save raw articles to `wiki/raw/articles/` and then commit/push to
`github.com/kzinmr/ai-topics`.

Note: a dedicated `wiki-git-sync` skill is listed in the skills catalog. As of
2026-08-25 it STILL fails to load via `skill_view` ("Skill not found") despite
appearing in the catalog's `available_skills` list — re-confirmed a second
time on 2026-08-25 in the blog-ingest cron run (first failure 2026-08-23, x-accounts-scan).
The catalog/disk drift persists. **This reference remains the authoritative
write-up.** Do not retry `skill_view(name='wiki-git-sync')` in the same
session after the first failure; treat it as unavailable and rely on this
reference.

## Two commit flavors — know which you're in

The repo has two distinct commit patterns. Do NOT confuse them:

| Flavor | What's in the commit | Pre-commit hook expectation |
|---|---|---|
| **Raw-only** (ingest stages) | `wiki/raw/articles/` only | index.md NOT validated (raw-only commit is clean) |
| **Wiki-content** (wiki-ingest / x-accounts-scan / trending / dreaming) | entity/concept pages + `index.md` + `log.md` + (sometimes) a new raw article | index.md **IS** validated + tag taxonomy check runs on all staged files |

Everything below under "Core rules" 1–3 applies to the **raw-only** flavor.
The **wiki-content** flavor (the one most wiki-cron jobs use) is covered in the
"Wiki-content commits" section near the end of this reference.

## Core rules

1. **Commit raw articles ONLY — not index.md / log.md.**
   The ingest stage saves immutable Layer-1 sources. Real wiki pages,
   `wiki/index.md`, and `wiki/log.md` are owned by the downstream
   `*-triage` → `*-wiki-ingest` stages. Committing only `wiki/raw/articles/`
   is expected and keeps the pre-commit hook (which validates index.md) clean.
   Do not run the pre-commit index validation expectation against a raw-only commit.

2. **Scope the `git add` to the ingest dir.**
   `git add wiki/raw/articles/` (not a bare `git add -A`), so unrelated
   working-tree changes — `config/hermes/skills/**`, `config/hermes/cron/jobs.json`,
   `AGENTS.md` — are NOT swept into the ingest commit. Those belong to their own
   commits.

3. **Mixed-provenance raw files are normal.**
   `wiki/raw/articles/` is shared across pipelines. A single `git add
   wiki/raw/articles/` can pick up untracked raw files from OTHER pipelines that
   were sitting uncommitted:
     - `blog-ingest` naming: `domain--slug--md5[:8].md`
       (e.g. `simonwillison.net--2026-aug-19-...--50e1e147.md`)
     - `newsletter-ingest` naming: `YYYY-MM-DD_<source>_<slug>.md`
       (e.g. `2026-08-20_elevenlabs_what-is-aiuc-1.md`)
   This is usually fine — all are Layer-1 sources meant to be committed. Just note
   the mixed provenance in the commit message when a batch of foreign files rides
   along (e.g. "19 blog + 5 newsletter raw articles").

## Wiki-content commits (wiki-ingest / x-accounts-scan / trending / dreaming)

Most wiki-cron jobs do NOT produce raw-only commits — they create/update entity +
concept pages AND bump `index.md` + `log.md` in the same working unit (per AGENTS.md
"index.md 即時更新 / log.md 即時追記"). Commit all of them together.

### Procedure (validated 2026-08-23 x-accounts-scan run)

```bash
cd ~/ai-topics
# Stage the SPECIFIC files you touched — do NOT `git add -A` (sweeps in unrelated
# AGENTS.md / config/hermes/cron/jobs.json / skill edits that belong to their own commits).
git add \
  wiki/entities/<touched-pages>.md \
  wiki/index.md wiki/log.md \
  wiki/raw/articles/<new-raw>.md      # only if you saved a new raw this run
git commit -m "wiki: <pipeline> <date> — <one-line summary>"
git push origin main
# Post-push verify:
git rev-list --left-right --count origin/main...HEAD   # expect "0 0"
```

- The pre-commit hook runs index.md validation + tag taxonomy on staged files. A clean
  "✓ wiki/index.md clean" + "✅ Tag validation passed" is the success signal. If tags
  fail, fix the tag to an existing SCHEMA taxonomy entry (or add it to SCHEMA first) —
  do NOT `--no-verify`.
- Commit message convention: `wiki: <pipeline> <YYYY-MM-DD> — <summary>` (e.g.
  `wiki: x-accounts scan 2026-08-23 — Breunig 'Fable & The End of the Free Lunch'`).

### Sibling-subagent concurrent-edit hazard (CRITICAL for wiki-content commits)

`index.md` and `log.md` are SHARED across all wiki pipelines and are frequently edited
by sibling subagents / other cron jobs at the same time. Two concrete failure modes:

1. **patch-tool warning "modified by sibling subagent ... but this agent never read it"**
   — appears when a sibling wrote the file between your `read_file` and your `patch`.
   The fuzzy-matching edit usually STILL SUCCEEDS (it re-matches current on-disk content),
   but treat the warning as a signal to **re-read the affected region and verify your
   edit landed** before committing. In the 2026-08-23 run both index.md patches
   succeeded despite the warning — the edits were correct.

2. **Stale base / non-fast-forward push** — if a sibling committed between your read and
   your commit, push may be rejected. Resolve: `git status --short <file>` to confirm
   your version is the staged one → on rejection, `git stash` (unrelated files only) →
   `git pull --rebase origin main` → re-apply your wiki edits → `git push` →
   `git stash pop`.

Bottom line: for wiki-content commits, always (a) `git status --short wiki/` immediately
before `git add` to see the live state, (b) stage explicit paths not `-A`, and
(c) confirm `git rev-list --left-right --count origin/main...HEAD` == `0 0` after push.

## Push mechanics

- **`git pull --rebase` fails on a dirty tree.** It errors with
  `error: cannot pull with rebase: You have unstaged changes.` when unrelated
  files (skills, config, AGENTS.md) are modified. This is NOT a blocker for the
  ingest commit.

- **Hermes runtime drift is PERMANENT, not transient.** The working tree
  reliably carries uncommitted Hermes-managed files between commits —
  `AGENTS.md`, `config/hermes/cron/jobs.json`, `config/hermes/skills/**`, and
  `scripts/*` (observed in 5+ cron runs across 2026-08). Do NOT `git add -A`
  or blanket-stash these into a wiki commit — they are owned by the
  hermes-repo-sync workflow, not by the ingest stage. Stash (path-scoped:
  `git stash push -m "<note>" -- AGENTS.md config/hermes/ scripts/`) only as a
  last resort for a real non-fast-forward rebase, and restore the tree
  immediately after the push.

- **Run a plain `git push origin main` instead.** Its output is the divergence
  signal:
  - Fast-forward, up to date: `ee208447..3b323da9  main -> main` — done, no rebase
    needed.
  - Real divergence: `! [rejected] ... (non-fast-forward)` — THEN stash the
    unrelated changes, `git pull --rebase origin main`, push, `git stash pop`.

  Don't stash-and-rebase the whole tree just to push raw articles; if the remote
  remote hasn't moved, a direct push is correct.

### Path-scoped stash for rebase (validated 2026-08-25 blog-ingest)

When a genuine non-fast-forward rejection forces `git pull --rebase`, the
dirty tree is exactly the Hermes runtime drift listed above. Stash only that
path set so it can't be swept into the rebase:

```bash
git stash push -m "hermes runtime drift - <job> <date>" -q -- AGENTS.md config/hermes/ scripts/
git pull --rebase origin main
git push origin main
git stash pop
```

`git stash apply` then `git stash drop` is equivalent if you want to verify
the apply succeeded before dropping. Verify afterwards that the drift files
are back in the working tree (they should remain UNCOMMITTED).

### `git stash` applies to TRACKED files only

`git stash` never touches untracked files. Untracked Layer-1 sources
(`wiki/raw/articles/**`) are left in place during any rebase — that is
expected and safe (raw files from different runs do not conflict). But it also
means a stash-based rebase workflow cannot be a substitute for scoping the
commit: the raw files are already staged, not stashed.

## Post-push verification

```bash
cd ~/ai-topics
git status --short wiki/raw/articles/        # should be empty (clean)
git log -1 --oneline                          # confirm your commit
git rev-list --left-right --count origin/main...HEAD   # should read "0 0"
```

**Always run the `git rev-list --left-right --count origin/main...HEAD` check after
a wiki-content push — a successful `git push` output does NOT prove the commit is
on the remote.** In the 2026-08-27 trending-topics run the `git push` succeeded
(`e2e5de4c..8aea6ea2 main -> main`) but this check was skipped; a sibling
`active-crawl` job was concurrently committing, so the one-step
`git show --stat HEAD` + `git status --short` verification (used instead) only
proves the LOCAL commit shape, not remote sync. When a sibling is active, the
`rev-list` `0 0` check is the only signal that your pushed commit is actually
ahead-and-synced with `origin/main`.

## Checkpoint handoff (not a git concern, but part of the stage)

The ingest script writes `${HERMES_HOME}/cron/data/<pipeline>/latest.json`
(e.g. `blog_ingest/latest.json`) with `saved_articles[]` (each has `raw_path`)
and `unsaved_articles[]` (scrape failures, e.g. bot-blocked 403s). The
downstream `*-triage` stage reads `latest.json` — so a successful ingest =
checkpoint written + raw files committed + all articles marked read in the
source DB (blogwatcher / email IMAP `\Seen`+Processed). A scrape failure leaves
the URL in `unsaved_articles` and marks it read so it won't retry forever.
