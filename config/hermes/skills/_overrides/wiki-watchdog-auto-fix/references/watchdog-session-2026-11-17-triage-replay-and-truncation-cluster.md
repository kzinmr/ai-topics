# Watchdog session 2026-11-17 — triage-replay recipe + recurring truncation cluster

## Pipeline alerts (both chain breaks) resolved as soft/stale — replay-before-rerun

Pre-run context reported `blog chain broken: triage_ok_but_wiki_ingest_failed` + `newsletter chain broken: ingest_ok_but_triage_failed`. Both were soft:

1. **Blog chain**: `blog-wiki-ingest` died 10:48 UTC with `RuntimeError: Response truncated due to output length limit` (3rd consecutive day). Triage checkpoint survived at `/opt/data/.hermes/cron/data/blog_ingest/triage_latest.json`. Of 6 take/reference decisions, **3 were already completed by a PARTIAL run before truncation** (geohot Empire of Dirt, micahflee open-weights, llm 0.37.3, stratechery obituaries already had target-page content, bumped `updated:`, and raw cited in sources).
   - **Recipe**: before enriching anything, grep each target page for the raw-article basename / title keyword and check `updated:` date. Only complete genuinely-missing items; skip covered ones.
   - Completed inline: gary-marcus + ai-bubble-economics (Marcus "Game over, man"), NEW `entities/paul-christiano.md` from the 114KB Dwarkesh transcript.
   - delegate_task: 1 of 2 subagents died on the SAME 503 the cron jobs die on; the other succeeded. Failed one done inline in ~6 tool calls — this is the proven pattern (retry once, then inline).
2. **Newsletter chain**: `newsletter-triage` "failed" per scheduler with 503, **but its checkpoint exists and all 4 items were already covered by sibling jobs** (qwen-4-max, claude-sheets raw+coverage, Import AI log line; Muse digest scraped at 10:57 during the retry, 7 min after the failure timestamp).
   - **Pitfall**: `hermes cron list` "Last run ... error" reflects the FIRST attempt; a later retry may still have produced the checkpoint/output. Cross-check checkpoint mtime and coverage grep before declaring a backlog.
   - One-call coverage check: `grep -n "<subject key words>" wiki/log.md` + `ls wiki/raw/articles/ | grep <slug>`.

## Structural fixes applied this run
- Header-count drift again: Events 54→55, Queries 58→59 (recompute from `^\|?- [[ns/` lines; Entities/Concepts/Comparisons were accurate — check each header, don't blanket-fix).
- **Corruption variant**: duplicate `> Last updated:` lines in the index.md header (11-15 AND 11-14 stacked). Dedup to one line with today's date. Check: `[(i,l) for i,l in enumerate(lines) if 'Last updated' in l]` — expect exactly 1.
- Empty `[[]]` links: 0 (was 47 on 11-13) — fixed upstream, don't re-fix.
- `metR` "unindexed" is a FALSE POSITIVE: indexed via redirect-syntax `[[entities/met|entities/metR]]` alias entry — do NOT add a second entry.
- log.md prepend buried `# Wiki Log` at line 21 exactly as the wiki-graph-health guarantee predicts; run `fix_log_header_burial.py` LAST before commit (237 entries preserved).

## Escalation-worthy pattern (3-day cluster, report don't fix)
Every morning 10:30–11:00 UTC: `*-wiki-ingest` jobs → `Response truncated due to output length limit`; `newsletter-triage`/Weekly digest → 503-no-fallback. Also hits skeleton-enrich-daily, jp-to-en-translation, llm-pricing-monitor. Root cause is cron-agent output-limit + `hermes-llm-serial-gate` fallback config — NEEDS-HUMAN; escalate if the backlog compounds (day 4+).

## Working-tree hygiene
107 dirty files at start (skill edits + entity WIP from sibling pipelines). `git stash push` → `git pull --rebase` → `git stash pop` worked cleanly. Stage only the files you touched (6 this run); leave sibling WIP dirty.

## Tool notes (cron mode)
- `hermes` not on PATH → `export PATH="/opt/hermes/bin:$PATH"`.
- tirith blocks `cmd | python3` pipes (even `hermes cron list | python3`) → write output to /tmp file first, or `hermes cron list > /tmp/x.txt` then grep.
- Run python heredocs with `/opt/data/.hermes/venv/bin/python` (has PyYAML).
