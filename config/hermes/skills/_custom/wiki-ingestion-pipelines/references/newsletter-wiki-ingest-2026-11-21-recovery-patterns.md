# newsletter-wiki-ingest recovery patterns — 2026-11-21

## Context
`newsletter-triage` (job 4e8b0d92c6a1) failed at 10:30 UTC with
`RuntimeError: HTTP 503: Local LLM server is busy` and emitted NO triage JSON.
The ingest wrapper passed `{"ok": false, "error": "failed to parse JSON response from newsletter-triage output"}`.
This is the full-crash variant of the triage-recovery path (not the markdown-wrapped variant).

## What worked (validated 2026-11-21, run 20261121T101055Z)

1. **The inbox pre-triage summary is a complete recovery source.**
   `~/wiki/raw/inbox/newsletter-ingest/<run_id>.json` (schema 2.0, committed by the
   newsletter-ingest job itself, e.g. commit 65e9d079) contains per-newsletter
   `subject`, `publisher`, `primary_url`, `importance`, `suggested_wiki_targets`, and
   crucially a `downstream_action` field. Here it even carried an explicit
   "Do NOT fabricate content from the subject line alone" instruction for the
   unresolvable beehiiv item — honour that: unreachable subject-line-only items go to
   `queries/unresolved-newsletter-leads.md` as reference, never as take.

2. **`latest.json` with 0 candidates does NOT mean the batch is empty.**
   The checkpoint's `candidates` array was empty (0) yet two raw newsletter digests
   existed at `wiki/raw/newsletters/` with mtime matching the run. Trust the inbox
   summary + raws on disk over the candidates array when triage crashed.

3. **Rebuild triage_latest.json yourself before editing.** Built a 4-decision JSON
   (1 take, 1 ref, 2 batch skips) via write_file to /tmp + terminal (cron mode),
   saved to `cron/data/newsletter/triage_latest.json`, then ran
   `python3 scripts/archive_triage.py newsletter --keep-reference` normally.
   Note the dedup key warning from the skill: use item_id-style uniqueness — here only
   3 URL-bearing items archived (the beehiiv batch skip registers 1 representative URL
   for all 20 trackers, which is intended).

4. **The Signal resolution**: `thesignal.substack.com/p/<slug>` (custom domain) returned
   full 54-paragraph `<article>` body on first curl (200, 217KB). `open.substack.com`
   form was not needed. The raw digest's Link 7/8 `app-link/post?publication_id=293154&post_id=225782936`
   gave the slug. Saved full body as `raw/newsletters/<date>_the-signal_<slug>-full.md`.

5. **Beehiiv v2/c/ Cloudflare kill switch**: 3/3 sampled links returned HTTP 200 with
   title "Just a moment..." (7045 bytes) — skip immediately, no retry, reference lead.

## Coverage-gap note (dual-source Anthropic IPO)
Existing `events/anthropic-nasdaq-debut-2026.md` had pricing ($83) and HN reception but
lacked: day-one peak $111.53, the Nov2→Nov10 RSP "imminently"→"met" 8-day flip, >90%
Claude-written codebase, NRR ~900%, GM 29%→85%+, +$6.6B 9M OCF, SpaceX $120.5B compute,
"Anthropic Direct", ~$132B cash. The specialized explainer (The Signal) carried the
specific numbers the Techmeme-sourced page lacked → take as existing-page update, not skip.

## Tags
`anthropic-ipo` and `responsible-scaling-policy` are already in SCHEMA.md taxonomy
(Meta/Models lines) — no SCHEMA edit needed for Anthropic financial pages.
