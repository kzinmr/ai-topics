# Newsletter Wiki Ingest — 2026-08-23 Patterns (Takes=0 Recovery Run)

Session: newsletter-wiki-ingest cron (job 4e8b0d92c6a1). Upstream newsletter-triage
failed JSON render (pre-run script error: `failed to parse JSON response from
newsletter-triage output`). Recovered via checkpoint + inbox summary; produced 0
takes, 3 skips.

## Key pattern: Takes=0 is a legitimate recovery outcome

When the upstream triage fails to render JSON but the checkpoint is valid AND the
inbox pre-triage summary rates the batch as low-value/unconfirmed-AI, the correct
downstream behavior is:

1. **Read `triage_latest.json`** — verify it's today's run (`checkpoint_run_id`
   matches `latest.json`'s `run_id`).
2. **Read the inbox pre-triage summary** at
   `wiki/raw/inbox/newsletter-ingest/<run_id>.json` — this is the PRIMARY content
   source when all beehiiv URLs are Cloudflare-blocked.
3. **If the inbox summary rates the topic as UNCONFIRMED AI** (e.g., "likely
   crypto/markets given 'Run' + 'Biggest Run' framing") AND all links are
   unresolvable (HTTP 403), do NOT force a take. The body is unreachable and the
   topic relevance is unconfirmed.
4. **Produce a triage JSON with 0 takes** — this is valid. The downstream
   `newsletter-wiki-ingest` should still archive the skips and update `log.md`.
5. **Archive the skips** via `archive_triage.py newsletter --keep-reference`.
6. **Update `log.md`** with a clear "0 takes" entry explaining the Cloudflare block
   and the inbox summary's topic rating.
7. **Commit + push** — even a no-op run leaves an audit trail.

## Why this is different from a "stale checkpoint" recovery

- **Stale checkpoint** (2026-08-17 pattern): the checkpoint is from the previous
  day and was already consumed by a prior downstream commit. Re-ingesting it would
  produce redundant updates. The fix is to re-triage from `latest.json` directly.
- **Takes=0 recovery** (this pattern): the checkpoint is from today, is valid, and
  was NOT yet consumed. The issue is that the content is genuinely low-value or
  unreachable, so the correct outcome is to archive the skips and move on.

Detection: `checkpoint_run_id` matches today's `latest.json` `run_id` → valid
checkpoint. If it's yesterday's → stale, use the 2026-08-17 recovery path.

## Concrete example (2026-08-23)

- **Checkpoint**: `latest.json` run `20260823T101026Z` — 1 newsletter: "Nobody Knows
  How Big the Biggest Run Is" (beehiiv uid=543, 2026-08-22, 18 links).
- **Inbox summary**: `wiki/raw/inbox/newsletter-ingest/20260823T101317Z.json` —
  rated the topic as "UNCONFIRMED as AI" (likely crypto/markets), all 18 links
  Cloudflare-blocked (HTTP 403).
- **Decision**: 0 takes, 3 skips (newsletter body + tracking links + UI noise).
- **Archive**: 3 skips archived → `wiki/raw/archived/triage/newsletter/2026-08-23_20260823T101026Z.json`.
- **Log entry**: `## [2026-08-23] newsletter-wiki-ingest | beehiiv uid=543 issue
  fully Cloudflare-blocked - 0 takes, 3 skips archived`.
- **Commit**: `c42926c1`.

## Pitfall: Don't confuse "Cloudflare-blocked" with "needs browser-based resolution"

The inbox summary may recommend "use browser_navigate on the main post to read the
issue and confirm whether it is actually AI/LLM content." In a cron job, this is
often not feasible (no browser tools available). The correct fallback is:

1. Trust the inbox summary's topic rating (UNCONFIRMED AI → low priority).
2. If the topic is clearly non-AI (e.g., "crypto/markets"), skip the entire issue.
3. If the topic is ambiguous but plausibly AI, note it in `log.md` for manual
   follow-up but do NOT force a take.

## 3rd consecutive Cloudflare-blocked beehiiv issue

This was the 3rd consecutive run with a fully Cloudflare-blocked beehiiv issue
(2026-08-19, 2026-08-20, 2026-08-22). The inbox summary flags this as a standing
recommendation: "consider a browser-based beehiiv resolver as a standing
capability." For now, the Takes=0 recovery path is the correct default.

## Workflow that worked

1. Read `triage_latest.json` + the failed output tail.
2. Check `checkpoint_run_id` against today's `latest.json` `run_id` → valid.
3. Read inbox pre-triage summary → topic UNCONFIRMED AI, all links Cloudflare-blocked.
4. Produce triage JSON with 0 takes, 3 skips.
5. Archive skips via `archive_triage.py newsletter --keep-reference`.
6. Update `log.md` with a clear "0 takes" entry.
7. Commit + push.
