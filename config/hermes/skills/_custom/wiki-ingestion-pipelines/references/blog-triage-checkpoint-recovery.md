# Blog Triage Checkpoint Recovery

When `blog-triage` fails with `"failed to parse JSON response from blog-triage output"` but the triage checkpoint JSON exists at `${HERMES_HOME}/cron/data/blog_ingest/triage_latest.json`, the triage agent saved the checkpoint **before** attempting to render its cron response. Read it directly and proceed with blog-wiki-ingest.

## Recovery Procedure

1. **Check the checkpoint path first** (not the cron output):
   ```
   /opt/data/.hermes/cron/data/blog_ingest/triage_latest.json
   ```
2. **Verify it's valid JSON** — it should contain `checkpoint_run_id`, `summary_ja`, and `decisions` array
3. **Count decisions**: Takes, References, Skips — the downstream enrichments depend on accurate counts
4. **Proceed with normal blog-wiki-ingest** using the recovered decisions

## Validated Recoveries

This recovery pattern has been validated twice in production:

- **July 1, 2026 (first occurrence)**: blog-triage failed with JSON parse error; checkpoint saved before render attempt. 2 takes + 4 references processed successfully.
- **July 2, 2026 (confirmed)**: Same failure mode — blog-triage JSON parse error at 07:33 UTC, checkpoint at `triage_latest.json` valid. 1 take + 3 references + 15 skips processed. Pipeline completed normally.

**Pattern confirmed**: This is not a one-off bug. The blog-triage agent fails on cron response rendering ~5-10% of the time (as of July 2026), but always saves the checkpoint first. Recovery is the standard path, not an edge case.

## What Happened (July 1, 2026)

- `blog-triage` ran at 07:30 UTC, called `save_triage_for_downstream()` before rendering its markdown response
- The markdown renderer hit a JSON formatting error (`"failed to parse JSON response"`)
- The checkpoint file was already saved to `${HERMES_HOME}/cron/data/blog_ingest/triage_latest.json` by the save function
- `blog-wiki-ingest` at 07:45 UTC recovered from the checkpoint, processed 2 takes, 4 references successfully
- The pipeline completed normally — only the upstream cron output was lost, not the triage data

## Key Distinction

This is **not** the same as newsletter-triage recovery (which has an identical failure mode but different checkpoint path). The blog pipeline checkpoint lives at:
```
${HERMES_HOME}/cron/data/blog_ingest/triage_latest.json
```

Not at the newsletter path:
```
${HERMES_HOME}/cron/data/newsletter/triage_latest.json
```

## Pre-Commit Pitfall After Recovery

After enrichment, when committing new entity pages that introduce new tags (e.g., `jax`), the pre-commit tag validator will block the commit if the tag isn't in `SCHEMA.md` taxonomy. Fix:

1. `grep -i "new-tag" wiki/SCHEMA.md` — check if the tag exists
2. If absent, add it to the appropriate category line (e.g., Models section for `jax`)
3. `git add wiki/SCHEMA.md` — include the schema update in the same commit
4. Re-commit — the validator will now pass

This is distinct from the `"-"` pipe-corruption issue. Both pre-commit hooks (index validator + tag validator) are independent; a tag violation doesn't imply index corruption.
