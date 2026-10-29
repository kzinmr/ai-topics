# When the cron-output fallback directory is missing

## Symptom

The `semantic-article-grouping` skill's "Fallback (if downstream encounters a JSON parse failure)"
section tells you to read `${HERMES_HOME}/cron/output/<job-id>/<timestamp>.md` as a secondary
recovery source. On the newsletter pipeline this directory can be **entirely absent**:

```
$ ls /opt/data/.hermes/cron/output/newsletter-triage/
(no such directory / empty)
$ ls /opt/data/.hermes/cron/output/newsletter-wiki-ingest/
(empty)
```

Observed 2026-10-24 during newsletter-triage (`run_id 20261024T101037Z`).

## What this means

It is **not** evidence that the job failed or that output was lost. The `cron/data/newsletter/`
checkpoint directory is the authoritative artifact — it carries both:

- `latest.json` — the upstream collection checkpoint (`run_id`, `collected_at`, `candidates[]`)
- `triage_latest.json` — the triage output (`checkpoint_run_id`, `decisions[]`)
- `newsletter_<run_id>.json` — an immutable per-run snapshot of the collection checkpoint

The snapshot files are the best historical record when the output dir is missing: compare
`newsletter_<run_id>.json`'s `run_id` with `triage_latest.json`'s `checkpoint_run_id` to learn
which batch the current triage actually consumed.

## Decision recipe

1. Never treat a missing `cron/output/<job>/` as a blocker — proceed with the checkpoint path.
2. To answer "did a prior invocation already consume this batch?", use, in order:
   a. `triage_latest.json` `checkpoint_run_id` vs `latest.json` `run_id` (authoritative)
   b. `git show --stat <prior-commit-sha>` — which files did the prior run actually commit
   c. `wiki/log.md` same-day entries (weakest — pipelines write log entries for raw saving too)
3. Do **not** infer consumption from a commit message alone. On 2026-10-24 the commit
   `wiki: newsletter triage report 20261024T101037Z` contained **only**
   `wiki/raw/inbox/newsletter-ingest/20261024T101037Z.json` — the inbox pre-triage summary, which
   is upstream input to this very job, not its output.

## Related

- `semantic-article-grouping` → `references/newsletter-triage-2026-10-24-patterns.md`
  (full session pattern set, incl. empty-`<title>` substack curl extraction and the
  same-topic-but-different-numbers coverage test).
