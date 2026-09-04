# Blog Triage Checkpoint Recovery (Case C: Cron Response Render Failure)

Validated: June 21, 2026

## Pattern

The blog-triage agent's cron output failed to parse as JSON:
```
"failed to parse JSON response from blog-triage output"
```

However, `/opt/data/.hermes/cron/data/blog_ingest/triage_latest.json` contained a **clean, valid decisions array** with:
- 1 take (johndcook.com Z3/Python Claude article)
- 1 reference (lcamtuf AI slop detection)
- 13 skips

## Root Cause

Same as the dreaming pipeline variant (June 17): the triage agent saved the checkpoint file (`triage_latest.json`) to disk *before* attempting to render its cron response. The response rendering then failed during Hermes's JSON parse of the wrapped markdown output, but the checkpoint was already persisted cleanly.

## Recovery Procedure (for downstream wiki-ingest)

1. **Read the checkpoint directly** — do NOT attempt to extract JSON from the cron output `.md` file
2. **Verify the decisions array** — check that `recommended_action`, `reason_ja`, `body_excerpt`, and `candidate_wiki_path` fields are present
3. **Check `checkpoint_run_id`** against today's date — rule out stale data (Case C0)
4. **Check `git log --oneline -3`** — rule out inline commit (Case C1)
5. **Proceed with wiki ingestion** as if the triage succeeded normally

## Detection

The downstream error `"failed to parse JSON response from blog-triage output"` does NOT mean the triage failed. It means the cron output render failed. Always check:
```
ls -la /opt/data/.hermes/cron/data/blog_ingest/triage_latest.json
```
before assuming the triage agent did not produce valid decisions.

## Pipeline Scope

This pattern has now been validated for:
- **Dreaming pipeline** (June 17, 2026)
- **Blog pipeline** (June 21, 2026)
- Likely applies to **Newsletter pipeline** as well (same cron architecture)

## Related

- `semantic-article-grouping` skill: "Pipeline Resilience: Cron Output Format" section
- `wiki-ingestion-pipelines` skill: Section E — "Case C2: Triage produced decisions only, no inline commit"
