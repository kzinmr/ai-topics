# Blog-Wiki-Ingest Recovery & Commit Patterns (2026-08-13)

Validated in the 2026-08-13 blog-wiki-ingest run (triage render-failure recovery → enrichment → commit/push).

## 1. Checkpoint recovery + archive-already-done check

The triage agent saved `triage_latest.json` (valid, 20 decisions: 1 take, 3 refs, 16 skips) BEFORE its cron response failed JSON parse. Recovery:

1. Read `${HERMES_HOME}/cron/data/blog_ingest/triage_latest.json` directly — no extraction, no re-run.
2. **Check `git log --oneline -3` + `wiki/raw/archived/triage/blog/` BEFORE running `archive_triage.py` again.** In this run the triage agent had ALREADY archived (commit `94c2c47b "blog-triage 2026-08-13 - ... + archive 15 skip/reference items"`, file `2026-08-13_20260813T101840Z.json`). Re-archiving is idempotent but wasteful — verify first, skip if present.
3. Validate field completeness: `python3 -c` reading the JSON directly (no pipes — `tirith:pipe_to_interpreter` blocks `cat | python3`). Every decision needs `body_excerpt` + `reason_ja`.

## 2. Cron-mode dirty-worktree push (git pull --rebase fails)

Symptom:
```
error: cannot pull with rebase: You have unstaged changes.
```
Cause: cron worktree always has unrelated changes — sibling pipelines modify `config/hermes/skills/`, and untracked raw articles (sitemap-monitor, blog-ingest) accumulate in `wiki/raw/articles/`. These are NOT yours to commit/stash.

Fix:
```bash
git fetch origin
git rev-list --left-right --count HEAD...origin/main   # "1  0" = ahead only
git push                                               # safe when remote is behind (0 on right)
```
Only pull --rebase when the right side is non-zero. Do not use `--no-verify` for this.

## 3. Small enrichment batches: direct patch, not delegate_task

With 1 take + 3 references (4 page edits), direct `patch` calls beat delegate_task:
- Faster (no subagent spawn/verify round-trip)
- No early-commit hazard (subagents committing log.md entries mid-run)
- No tag-taxonomy violations from subagent frontmatter

The skill's parallel-delegate_task guidance is for **4-6+ takes**. Threshold observed: ≤4 page edits → direct patch; >4 → delegate in blocks of 3.

## 4. Verification checklist used (all genuine gaps confirmed)

- Take (deepseek-v4.md): page had V4-Pro/V4-Flash/V4-Flash-0731 but zero "0813" → genuine gap. Grep `0813` returned nothing.
- Ref (openai-huggingface-incident): page had Black Hat timeline but zero "RLVR" → genuine gap.
- Ref (simon-willison.md): August 2026 Updates had no "alchemy-utils" → genuine gap.
- Ref (cognitive-debt.md): page had Xe Iaso/Osmani sections but zero "Herrengt" → genuine gap.

Each enrichment: frontmatter `updated` bump + `sources` addition + body section + index.md entry + log.md prepend (tmp+merge, never write_file over log.md).

## 5. Commit flow

```bash
git add wiki/<pages> wiki/index.md wiki/log.md   # targeted add, not `git add wiki/` (avoids sweeping sibling untracked raws into your commit)
git commit -m 'wiki: ...'                         # pre-commit hooks: index validate + tag taxonomy
git fetch origin && git rev-list --left-right --count HEAD...origin/main && git push
```
