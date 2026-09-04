# Git Sibling-Process Pitfalls + Post-Recovery Archive Verification

Validated 2026-08-03 (newsletter-wiki-ingest, checkpoint-recovery run).

## Pitfall 1: `git pull --rebase` fails with sibling-process unstaged changes

**Symptom**:
```
error: cannot pull with rebase: You have unstaged changes.
error: Please commit or stash them.
```

**Cause**: In the parallel pipeline window (07:00-07:50 UTC), or whenever skill-sync / skill-drift / other cron jobs run concurrently, sibling processes leave modified files in the working tree (typically `config/hermes/skills/_custom/*/SKILL.md`). `git pull --rebase` refuses to run with unstaged changes.

**Fix** (validated):
```bash
cd ~/ai-topics && git pull --rebase --autostash && git push
```
`--autostash` stashes the sibling changes, rebases, then re-applies them. Works cleanly even when you did NOT touch the offending files. Do NOT `git stash` manually — autostash handles the whole sequence atomically.

## Pitfall 2: Pre-staged sibling changes get swept into your commit

`git add wiki/` stages only wiki/, BUT files already staged by sibling processes before your run (skill updates, raw articles from other pipelines) are included in your commit regardless.

- This is usually acceptable: pre-commit hooks validate ALL staged files (index + tags), so the commit still passes if the swept-in files are clean.
- If a swept-in sibling file violates the tag taxonomy, it blocks your commit — fix it or use `git commit --no-verify` per the SKILL.md Pre-Commit Hook Pitfalls section.
- **Check before committing**: `git status --short` after staging shows exactly what the commit will contain. Distinguish your wiki/ changes from sibling `config/hermes/skills/` / raw-article changes so you can explain the commit contents in the log entry.

## Post-Recovery Archive Verification (render-failure pattern)

When recovering triage JSON from checkpoint after "failed to parse JSON response from {pipeline}-triage output":

1. **Check whether the archive already exists** — the triage agent saves `raw/archived/triage/{source}/{YYYY-MM-DD}_{run_id}.json` BEFORE attempting to render its cron response. The run_id in the archive filename matches the checkpoint's `checkpoint_run_id` (e.g. `2026-08-03_20260803T103004Z.json` for `checkpoint_run_id: 20260803T103004Z`).
2. **If present, DO NOT re-run `archive_triage.py`** — the skip/reference items are already persisted.
3. **Fewer archived decisions than non-take items is NORMAL** — the archive dedups by URL via `archive_index.json`. Batch-skip items sharing a URL with an already-archived reference (e.g. multiple Interconnects/The Signal items pointing at the same post URL) collapse into the reference entry. Verify with:
   ```python
   import json
   idx = json.load(open('/opt/data/ai-topics/wiki/raw/archived/triage/archive_index.json'))
   urls = idx.get('urls', {})
   print('total:', len(urls), 'shared-url-present:', 'https://www.interconnects.ai/p/...' in urls)
   ```
   Validated 2026-08-03: 8 non-take decisions → 5 archived (3 collapsed by shared URLs: Interconnects artifacts#23 ref + 2 batch skips).
