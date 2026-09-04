# Stale Checkpoint + Wrong Upstream Self-Report Recovery (2026-08-17)

Validated in the newsletter-wiki-ingest run of 2026-08-17. The generic render-failure
recovery ("read triage_latest.json directly") has two traps that can silently produce
a no-op run: a **stale** checkpoint file, and a **false "0 candidates" self-report**
embedded in the failed upstream response.

## Symptom

- Pre-run script: `{"ok": false, "error": "failed to parse JSON response from newsletter-triage output", "output_path": ".../2026-08-17_10-50-49.md"}`
- `triage_latest.json` exists and parses fine — but its `checkpoint_run_id` is the
  **previous day** (`20260816T102116Z`), mtime is yesterday, and `git log` shows a
  downstream commit (`7a4a385e`) that already executed that checkpoint's takes.
- The failed output file's embedded agent response says: "Current latest.json
  (run 20260817T104823Z) has **0 candidates** — the Aug 17 newsletter ingest found
  nothing new." This is **WRONG** — the checkpoint actually has 5 newsletters.

## The two traps

### Trap 1: stale triage_latest.json ≠ recovery source
The render-failure variant says "just read triage_latest.json". That is only valid
when the checkpoint is TODAY's run. A previous-day checkpoint that a downstream
commit already consumed is a **duplicate invocation** — re-ingesting it produces
redundant page updates.

Detection (all cheap):
1. `jq .checkpoint_run_id /opt/data/.hermes/cron/data/newsletter/triage_latest.json` (or blog/dreaming) — compare against today's run id from `latest.json`.
2. `git log --oneline --since="<date>" -- wiki/` — find the prior `newsletter-wiki-ingest` commit.
3. `grep -n "<date>" wiki/log.md` — confirm the downstream entry lists the same takes.

### Trap 2: the failed agent's self-report is not evidence
The newsletter-triage agent that failed to render JSON still wrote a natural-language
response claiming the batch was empty ("0 candidates", "nothing new to process").
This was a hallucinated/over-optimistic duplicate-invocation verdict: the agent had
looked at the stale triage file and concluded the whole pipeline was done.

Tells that the self-report is wrong:
- `latest.json` (the ingest checkpoint, NOT the triage checkpoint) has `processed_count: 5` and ~20 `articles` per message.
- File size: today 38KB vs 14KB for a genuinely empty prior day.
- `git log` shows a commit `"triage: newsletter checkpoint 20260817T104823Z — 5 newsletters classified"`.

Rule: **when the failed output and the checkpoint disagree, the checkpoint wins.**
Re-triage from `latest.json` directly: group by message_id, filter substack/beehiiv
noise, resolve the surviving post URLs (redirect-stub → canonical domain), body-read
the substantive articles, cross-check wiki coverage, save a fresh triage JSON, archive,
then ingest.

## What the re-triage produced (2026-08-17 batch)

5 newsletters (uid=510-514), 12 decisions: 3 takes, 1 reference, 8 skips.

Takes:
- `entities/cloudflare.md` — Superintel+ exclusive with CSO Stephanie Cohen:
  Sep 15 2026 default blocking of training/agent crawlers on ad pages, 2B HTTP 402
  responses/day, 9.6:1 crawler-to-visitor ratio, pay-per-crawl → pay-per-use,
  Ceramic/You.com deals. Beehiiv v2/c tracking link (uid=512) resolved to full
  111-paragraph article, `isAccessibleForFree: true`, author Kim "Chubby" Isenberg.
- `concepts/ai-energy.md` — SemiAnalysis "Full of Cold Air - PJM's $12B modeling
  mistake": ~4GW fleet underestimation, $12B ratepayer waste 2025-27, $63.6B auctions
  with only 4.8GW new capacity, Reliability Backstop Auction (Sep 30-Oct 21).
  `isAccessibleForFree: false` in JSON-LD but 116 paragraphs fully accessible via
  `<article>` extraction — confirms the SemiAnalysis intermittent-paywall pattern.
- `entities/anthropic.md` — Theseus Infrastructure (Macquarie Asset Management + GIC)
  + Riot Platforms 20-year $9B deal (Bloomberg Aug 11) added to Compute Partnership
  table. Source: The Signal roundup.

Reference:
- `events/grok-4-6-launch.md` — Grok 4.6 GitHub Copilot availability (github.blog
  changelog Aug 14).

Skips:
- Qwen 3.8 27B newsletter = same-day duplicate of blog-wiki-ingest (simonwillison.net
  dual-publish already ingested to `concepts/qwen-3-8-27b.md` at 10:30).
- Lenny's Podcast Ian Silber (design-career, low AI value).
- Riemann/watermarking/Gemini 3.7 Flash/Grok Bot — already covered.

## Canonical domain additions for redirect-stub discovery

`open.substack.com/pub/{pub}/p/{slug}` returned ~1.3KB stubs whose `<title>` was the
canonical URL (`?triedRedirect=true`). Re-fetch via canonical domain succeeded:
- `www.lennysnewsletter.com` (Lenny's Podcast, pub 10845)
- `thesignal.substack.com` (The Signal, pub 293154)
- `newsletter.semianalysis.com` (SemiAnalysis, pub 6349492) — note the `newsletter.`
  subdomain, NOT the default `semianalysis.substack.com`

Adds to the previously validated list (www.latent.space, www.bensbites.com,
www.lennysnewsletter.com). SemiAnalysis redirect target: `newsletter.semianalysis.com`
(not `open.substack.com/pub/semianalysis`).

## Workflow that worked

1. Read `triage_latest.json` + the failed output tail (`tail -80` of the output md).
2. Check git log + log.md for prior consumption of the stale checkpoint.
3. Read `latest.json` directly — count `processed_messages`, read each newsletter's
   subject + articles array.
4. Read inbox pre-triage summary (`wiki/raw/inbox/newsletter-ingest/<run_id>.json`).
5. Resolve post URLs via curl script to /tmp (cron mode: write_file + terminal python3).
6. Cross-check wiki coverage (grep entities/concepts/events for topic keywords).
7. Save fresh triage JSON → archive_triage.py newsletter --keep-reference → patch
   pages → index.md + log.md → validate_index → commit + push.
