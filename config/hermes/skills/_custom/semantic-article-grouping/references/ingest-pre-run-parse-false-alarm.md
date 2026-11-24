# Ingest pre-run "parse failure" is often a false alarm — and the rebase-blocked push

Two learnings from the 2026-11-22 newsletter-wiki-ingest run (run `20261122T101113Z`), 0 takes / 1 reference / 2 skips.

## 1. Pre-run `ok:false` parse-error does NOT mean "empty batch" — read the checkpoint first

The cron pre-run script injects a block like:

```json
{
  "ok": false,
  "error": "failed to parse JSON response from newsletter-triage output",
  "output_path": "/opt/data/.hermes/cron/output/<job-id>/<ts>.md"
}
```

This is the **markdown wrapper** at `cron/output/<job-id>/<ts>.md` failing to parse — it says nothing about whether the triage produced a valid decision set. In this run the wrapper reported exactly this error, yet `cron/data/newsletter/triage_latest.json` (same `checkpoint_run_id`) parsed cleanly with 3 valid decisions and the batch processed normally (reference appended to `queries/unresolved-newsletter-leads.md`, 2 batch-skips archived, commit `409f1152`).

**Rule for the downstream ingest job:**

1. On a pre-run `ok:false` parse error, do NOT abort, do NOT emit `[SILENT]`, do NOT report "nothing to process".
2. `json.load()` the pipeline checkpoint directly:
   - newsletter: `${HERMES_HOME}/cron/data/newsletter/triage_latest.json`
   - blog: `${HERMES_HOME}/cron/data/blog_ingest/triage_latest.json`
   - dreaming: `${HERMES_HOME}/cron/data/dreaming/triage_latest.json`
3. Verify `checkpoint_run_id` matches the current run (not a stale prior-day file). If it matches and parses, proceed off it.
4. Only treat the batch as genuinely empty if the checkpoint is **absent**, **stale** (wrong run id), or **itself unparseable** — none of which is the same condition as the wrapper failing to parse.

Verify the checkpoint with the no-pipe `python3 -c` pattern (the `cat | python3` form is blocked by `tirith:pipe_to_interpreter`):

```bash
python3 -c "import json,collections; d=json.load(open('/opt/data/.hermes/cron/data/newsletter/triage_latest.json')); print(d['checkpoint_run_id'], len(d['decisions']), collections.Counter(x['recommended_action'] for x in d['decisions']))"
```

Distinct-but-related existing guidance: `references/dreaming-pipeline-recovery.md` and `references/triage-checkpoint-recovery-pattern.md` (those cover a *downstream* parse failure on an agent-wrapped response; this covers the *pre-run script's own* `ok:false` report at ingest entry — same recovery, different trigger point).

## 2. `git pull --rebase` blocked by an unrelated sibling's unstaged file → push directly

The canonical push flow is `git pull --rebase && git add wiki/ && git commit && git push`. During the parallel 07:00–07:50 / sibling-subagent window, a sibling agent may leave an **unrelated** modified file in the working tree (observed: `config/hermes/skills/_custom/dreaming/SKILL.md`, plus an unrelated `wiki/queries/modernization-inner-loop-reading.md`).

`git pull --rebase` then fails with:

```
error: cannot pull with rebase: You have unstaged changes.
```

This is NOT a reason to give up on pushing. Because the commit itself is local-only, the direct `git push` (with no rebase) succeeds — confirmed: `ab25757b..409f1152 main -> main`. The blocked rebase is harmless because you are pushing a fast-forward local commit, not pulling concurrent upstream work.

**Pattern:**
1. Stage ONLY your own files (targeted `git add wiki/<exact paths>`), never `git add wiki/` blanket — leave sibling files untouched.
2. Commit.
3. Try `git pull --rebase`; if it errors on unstaged changes that are NOT yours, **skip the rebase and `git push` directly**.
4. Confirm sync with `git status -sb` (`## main...origin/main` with no ahead/behind) and `git log --oneline -1`.
5. Do NOT `git stash` or `git checkout` the sibling's file to "clean" the tree — it's another agent's in-flight work; the direct push works without it.
