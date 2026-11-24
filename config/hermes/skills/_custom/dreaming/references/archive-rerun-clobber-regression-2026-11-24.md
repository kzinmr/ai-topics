# Archive re-run clobber regression (validated 2026-11-24)

Pitfall #22's merge fix (added 2026-08-23, commit `171e037c`) has **regressed**. Re-running `archive_triage.py dreaming --keep-reference` after the upstream dreaming-group already committed the day's archive rewrote `wiki/raw/archived/triage/dreaming/<date>_<run_id>.json` from 13 decisions down to only the 3 URL-less batch-skip decisions (-86 lines), while `new_archived: 0` and `total_archive_urls` stayed at 3384. The merge branch is not preserving existing decisions — possibly it only merges when genuinely new URL-keyed items exist, or the fix was reverted/lost.

## Rule

**When the upstream dreaming-group already committed today's archive** (`git log` shows a `dreaming: group triage ... archive N new` commit and the dated JSON exists on `main`), **do NOT re-run `archive_triage.py` at all.** The URL index is already complete; a re-run can only clobber the "why dismissed" record.

## Recovery if you already re-ran

```bash
cd ~/ai-topics
git checkout -- wiki/raw/archived/triage/dreaming/<date>_<run_id>.json \
                 wiki/raw/archived/triage/archive_index.json
```

The `archive_index.json` diff in this state is pure timestamp churn (`updated:` field only) — safe to discard along with the clobbered dated file. Verify with `git diff -- wiki/raw/archived/` before checking out: if the index diff touches anything other than the `updated` line, investigate before restoring.

## Detection

`git diff --staged --stat` (or unstaged) on the dated archive JSON showing large deletions (e.g. `86 +---`) against a first-pass log entry that recorded a much higher decision count.

## When re-running IS legitimate

Only when the upstream did NOT commit an archive this cycle (no dreaming-group archive commit in `git log --since=today`), and you have finalized your own triage JSON at `${HERMES_HOME}/cron/data/dreaming/triage_latest.json`.
