# newsletter-wiki-ingest recovery: upstream "failed to parse JSON" is a FALSE ALARM

Validated 2026-11-19 (run 20261119T101014Z).

## Symptom
The ingest cron's pre-run script injects:
```json
{"ok": false, "error": "failed to parse JSON response from newsletter-triage output",
 "output_path": "/opt/data/.hermes/cron/output/<triage-job-id>/<ts>.md"}
```
This is the **cron wrapper** failing to extract a bare JSON block from the triage agent's *markdown* report (`## Response` section is a Japanese triage report, not raw JSON). It does NOT mean the triage failed or produced nothing.

## Why it's a false alarm
The triage agent commits/pushes its own `triage_latest.json` checkpoint independently of the wrapper's JSON-extraction step. The wrapper only parses the *displayed response text*; the canonical downstream artifact lives at:
```
/opt/data/.hermes/cron/data/newsletter/triage_latest.json
```
Always check this file's mtime against the ingest run time. If it was written just before the ingest run (and its `checkpoint_run_id` matches `latest.json`'s `_checkpoint.run_id`), the triage succeeded and the wrapper error is cosmetic.

## Recovery procedure
1. **Read the checkpoint directly**, do not trust the `ok:false`:
   ```bash
   python3 -c "import json;d=json.load(open('/opt/data/.hermes/cron/data/newsletter/triage_latest.json'));print(d['checkpoint_run_id']);print(len(d['decisions']))"
   ```
   Verify the `checkpoint_run_id` equals the `_checkpoint.run_id` in `cron/data/newsletter/latest.json` — same run => fresh, processable.
2. **Process takes** as normal (BODY-READING MANDATE still applies: the raw newsletter file often contains only tracking URLs, so re-fetch the canonical post body via `open.substack.com/pub/<pub>/p/<slug>` curl+`<article>`/`<p>` extraction before editing -- do NOT rely on the raw digest's URL dump).
3. **Archive may already be done.** If the triage already ran `archive_triage.py`, your call returns:
   ```json
   {"ok": true, "message": "All items already archived (dedup)", "archived": 0}
   ```
   This is EXPECTED, not a failure -- the triage committed skips/references + the archive index. Do not re-run or panic.

## Git hygiene notes confirmed this run
- `git pull --rebase` was **blocked by sibling subagents' unstaged skills files** (`config/hermes/skills/_custom/*` modified by parallel jobs). The `git push` still succeeded as a fast-forward (`main -> main`) because there was nothing to rebase. => If pull --rebase fails on unrelated unstaged files, just `git push`; only escalate to `git stash` if push is actually rejected.
- Pre-commit hooks (`validate_index.py` + tag validator) passed; new tags `superintelligence`, `philosophy` were already in SCHEMA taxonomy -- grep SCHEMA.md before assuming a new tag is needed.

## Decision-quality reminder
A take can be valid even when the inbox pre-triage summary recommended something different (inbox suggested a new `events/black-october-2026.md`; the correct landing spot was an enrichment of the existing `entities/dean-ball.md`). Trust the body read over the inbox's new-page suggestion when the essay is a long-form philosophical statement rather than an acute event.
