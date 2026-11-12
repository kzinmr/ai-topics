# triage_ok_but_wiki_ingest_failed — 503 / truncation triage (2026-11-12)

Watchdog alert `└ \`blog\` chain broken: triage_ok_but_wiki_ingest_failed` (same for `newsletter`) is USUALLY transient infra, not data loss.

## Diagnostic recipe
1. Read the failing job's last output file: `~/.hermes/cron/output/<wiki-ingest-job-id>/<date>.md` — tail for the `## Error` block.
2. Common transient causes observed:
   - `RuntimeError: HTTP 503: Local LLM server is busy; Hermes should fall back to the external provider.`
   - `RuntimeError: Response truncated due to output length limit`
3. Confirm the triage stage actually succeeded: read the triage job output's final `COST_REPORT`/report section AND verify it wrote `~/.hermes/cron/data/blog_ingest/triage_latest.json` / `cron/data/newsletter/triage_latest.json` + archive file + a git commit.
4. If triage artifacts exist and are committed → NO action; the next wiki-ingest run re-consumes the fresh `triage_latest.json`. Log as transient in wiki/log.md.

## Checkpoint staleness false positives
- `cron/data/triage/latest.json` and `cron/data/newsletter-triage/latest.json` are STALE legacy pointers (2026-07-08 / 2026-05-11 as of 2026-11-12). The REAL triage checkpoints are `cron/data/blog_ingest/triage_latest.json` and `cron/data/newsletter/triage_latest.json`. Never flag staleness from the `latest.json` files in `triage/` or `newsletter-triage/` dirs.

## Other verified facts (2026-11-12)
- `wiki_health.py --json` takes ~2-4 min at 3,400+ pages — use terminal timeout ≥400s, NOT 60s (60s execute_code default times out).
- Cron job IDs: blog-wiki-ingest=9a7d1e3c4b20, newsletter-wiki-ingest=a1f4d9c3e672, blog-triage=58c2f4a7e1bd, newsletter-triage=4e8b0d92c6a1 (verify in `~/.hermes/cron/jobs.json` before reruns).
- Header count reconciliation: Queries header can lag live `- [[queries/` line count by 1 — recompute per-section from index lines (see watchdog-session references).
