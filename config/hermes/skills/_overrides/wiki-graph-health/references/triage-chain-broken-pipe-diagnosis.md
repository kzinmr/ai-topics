# Triage Chain Broken-Pipe Diagnosis (2026-08-08)

## Symptom

`pipeline_watchdog` alert file shows:

```
• PIPELINE blog: unhealthy
• PIPELINE newsletter: unhealthy
  └ `blog` chain broken: ingest_ok_but_triage_failed
  └ `newsletter` chain broken: ingest_ok_but_triage_failed
```

`ingest_ok_but_triage_failed` = ingest layer OK, triage stage failed. Almost always a
**transient LLM streaming error** (`RuntimeError: [Errno 32] Broken pipe`), NOT wiki
corruption. Do NOT auto-fix wiki pages for this.

## Diagnostic sequence

1. **Ingest OK?** `~/.hermes/cron/data/blog_ingest/latest.json` and
   `~/.hermes/cron/data/newsletter/latest.json` — mtime today, `"ok": true`,
   `total_new` / `processed_count` populated.
2. **Triage failed?** Latest output in `~/.hermes/cron/output/<job-id>/`:
   - File header reads `# Cron Job: <name> (FAILED)` (not the plain title)
   - Body ends with `## Error` + `RuntimeError: [Errno 32] Broken pipe`
   - There is NO `## Response` section.
3. **Checkpoints stale because** `blog_triage_checkpoint.py` / `newsletter_triage_checkpoint.py`
   call `extract_response_text()` which searches for the `## Response` marker. A FAILED
   output has `## Error` instead → returns `""` → `extract_json_blob` → None → checkpoint
   NOT rewritten (`triage_latest.json` keeps the previous day's mtime). That stale
   checkpoint is the visible symptom in cron data.
4. **Downstream wiki-ingest** (`blog-wiki-ingest`, `newsletter-wiki-ingest`) reads the stale
   `triage_latest.json` and may ALSO fail with broken pipe. Raw articles/newsletters
   (Layer 1) stay intact — no data loss.
5. **Partial success possible**: an early/unscheduled run may have committed content before
   the scheduled run failed (e.g. 2026-08-08 commit `c5ce224b` at 10:19 processed blog
   triage enrichment, then the 10:29 scheduled run died).

## Job IDs / schedule (from `~/.hermes/cron/jobs.json`)

| Job | ID | Schedule |
|---|---|---|
| blog-ingest | `1bf4c6492c1e` | 10:00 UTC |
| blog-triage | `58c2f4a7e1bd` | 10:20 UTC |
| blog-wiki-ingest | `9a7d1e3c4b20` | 10:40 UTC |
| newsletter-ingest | `3293c14f4352` | 10:10 UTC |
| newsletter-triage | `4e8b0d92c6a1` | 10:30 UTC |
| newsletter-wiki-ingest | `a1f4d9c3e672` | 10:50 UTC |
| pipeline-watchdog | `696ec6b0ecc7` | 0,6,12,18 UTC |
| wiki-watchdog-fix | `459ec1a09b8d` | 17:35 UTC |
| wiki-health-fix | `6f3525ec4d9a` | 17:50 UTC |

Note: wiki-watchdog-fix (17:35) runs BEFORE wiki-health-fix (17:50) — the watchdog cannot
assume health-fix already ran; it must live-verify all claims (validate_index.py, grep
corruption counts, header counts).

## Action

- Report as transient pipeline failure; recommend re-run:
  `/opt/hermes/.venv/bin/hermes cron run <job-id>` (hermes binary is NOT on cron shell
  PATH — use the absolute path; also at `/opt/hermes/bin/hermes`).
- Next scheduled run retries the next day automatically.

## Side observation — `grep -c` exit-code trap in verification chains

`grep -c` exits 1 when count == 0 (the DESIRED result for corruption checks), which kills
`&&` chains. Run counts as separate calls or append `|| true`.
