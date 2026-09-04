# Newsletter Wiki Ingest Session — 2026-06-18 (Case C0 Recovery)

## Situation

- Newsletter-triage cron job (07:20 UTC) failed with `"failed to parse JSON response from newsletter-triage output"`
- `triage_latest.json` existed at `/opt/data/.hermes/cron/data/newsletter/triage_latest.json` (87KB, saved 07:25)
- But `checkpoint_run_id` was `20260617T071109Z` — YESTERDAY's data
- The triage agent processed yesterday's 6 historical newsletters (all skip, Takes=0)
- Today's ingest (`latest.json`, run_id=20260618T072217Z) had **4 untriaged newsletters**

## Cause

The newsletter-triage pipeline was `context_from` chained to the previous day's checkpoint file (`newsletter_20260617T071109Z.json`). The newsletter-ingest ran at 07:22 (updating `latest.json`), but the triage received the old checkpoint through the chain, not the updated `latest.json`.

## Root Signal

```python
# triage_latest.json had:
"checkpoint_run_id": "20260617T071109Z"

# latest.json had:
"run_id": "20260618T072217Z"
```

Triaging a stale batch while fresh newsletters sit in `latest.json`.

## Recovery Approach (Combined Triage + Wiki Ingest)

### Step 1: Detection
Read `triage_latest.json` and check its `checkpoint_run_id`. If it doesn't match today's date, the file is stale.

### Step 2: Read Today's Ingest
Read `latest.json` at `/opt/data/.hermes/cron/data/newsletter/latest.json`. Extract candidates and inbox pre-triage summary at `~/wiki/raw/inbox/newsletter-ingest/`.

### Step 3: Resolve & Triage (Autonomous)
- For each newsletter, identify the post URL (Substack: `open.substack.com/pub/{handle}/p/{slug}` or `www.{publication}.com/p/{slug}`; Beehiiv: try `curl` on tracking links)
- Use `web_extract`, `curl` + `<article>` tag extraction, or JSON-LD to get content
- Check existing wiki coverage via `find`, `grep`, and `search_files`
- Assign star ratings: ★★★★★ new page, ★★★★☆ existing page update, ★★★☆☆ reference, ★★☆☆☆ skip

In this session, 4 newsletters yielded 2 takes, 1 reference, 1 skip.

### Step 4: Process Takes (Parallel)
Use `delegate_task` with batch mode to create/enrich pages in parallel:
- Batch 1 (3 concurrent): Midjourney entity page, Radical AI entity page, Nathan Lambert enrichment
- Each subagent receives: full article body, exact file paths, formatting requirements

### Step 5: Update Index, Log, Archive
- Add new entity entries to `index.md` in correct alphabetical position
- Update entity count in header AND section header
- Prepend new log entry to `log.md`
- Archive skip/reference items: `python3 ~/ai-topics/scripts/archive_triage.py newsletter --keep-reference`

### Step 6: Fix Tags & Commit
- Subagent-created pages may use non-canonical tags → check and add to SCHEMA.md or fix
- Commit: `git add wiki/ && git commit -m 'wiki: newsletter ingest ...' && git push`

## Files Created (this session)
- `entities/midjourney.md` (105 lines) — Midjourney entity with Medical pivot
- `entities/radical-ai.md` (108 lines) — Radical AI materials science entity
- `raw/articles/2026-06-18_latent-space_midjourney-medical.md` — Raw article
- `raw/articles/2026-06-17_latent-space_radical-ai-self-driving-lab.md` — Raw article

## Files Updated
- `entities/nathan-lambert.md` — Ai2 departure, Arcee/Mercor advising, 70K subs
- `index.md` — 2 new entity entries (entities +2, total pages 2577→2579)
- `log.md` — Recovery and ingest entry prepended
- `SCHEMA.md` — 5 new tags: healthcare, medical-imaging, materials-science, ai-in-science, self-driving-labs

## Commit
`19b3ba7f wiki: newsletter ingest 2026-06-18 — Midjourney Medical, Radical AI, Nathan Lambert career update`
8 files changed, 284 insertions, 6 deletions

## Key Lessons
1. **Always check `checkpoint_run_id`** — don't trust `triage_latest.json` without verifying its timestamp
2. **Substack post body extraction works via `curl` on `open.substack.com` URLs** — even for `isAccessibleForFree: false` posts
3. **Beehiiv Cloudflare challenge is final** — `curl` returns "Just a moment..." and retry won't help
4. **Independent triage is feasible** even without the triage pipeline — the inbox pre-triage summary provides enough metadata to prioritize
