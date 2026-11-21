# Watchdog session 2026-11-18 — newsletter chain-break triage + max_tokens root cause

## Context
Pre-run script flagged: `newsletter chain broken: triage_ok_but_wiki_ingest_failed`.

## Verified ground truth
- index.md: 0 pipe/line-number/triple-bracket corruption; validate_index.py exit 0 (3521 lines).
- L2 pipe-prefix scan (entities/+concepts/): 0. No-frontmatter scan: 0. log.md header OK (line 1).
- sources gap: scanner reported "4 missing" (openai, simon-willison, harvey, gary-marcus) — ALL FALSE POSITIVES. These are huge pages (65-174 KB); the probe read only the first 3000 chars, and simon-willison's inline `sources: [...]` list exceeds that window. Lesson: for `sources:` presence checks, parse the full frontmatter block (read whole file or scan until closing `---`), not a fixed byte window.
- Index header counts: Entities 972 = 972 lines, Concepts 2372 = 2372 lines. Consistent (small dir-vs-index deltas from redirect stubs / dir-hubs — normal).

## Newsletter chain-break: soft, not actionable
- newsletter-wiki-ingest (a1f4d9c3e672) failed today with `HTTP 503: Local LLM server is busy` (last 7 runs: 6 FAILED / 1 OK — FAILURES ARE CHRONIC).
- Failure modes across the week: 503 (×2) and `Response truncated due to output length limit` (×4).
- Root cause found: job had `max_tokens: 2048` — the lowest of all wiki-ingest jobs (blog-wiki-ingest also 2048; triage/health-fix 2048; active-crawl 3072; trending 6144; triage/graph-analysis 8192). The truncated-output failures are the job burning its 2048-token budget before finishing.
- Data loss: NONE. Triage committed (64e28d10, 699f6c86), raws saved, and all 4 newsletter topics (Datasette Lite SW, NVIDIA chip-plot-twist, free-tools digest, Productiv-icky) covered by sibling jobs (blog-ingest 9ee370b2, trending 7793a757, hot-post 3e23f6f9). 2026-11-17 log line confirms prior watchdog ruled same alert "soft".

## Fix applied (cron config, not wiki)
`~/.hermes/cron/jobs.json` job a1f4d9c3e672: `max_tokens: 2048 → 8192`, `model: null → deepseek-v4-flash` (known-good for heavy wiki jobs per unified-pipeline precedent). Backup: `jobs.json.bak-watchdog-2026-11-18-pre-fix` (also `-2026-11-18` pre-edit copy). Validate after edit: `python3 -c "import json; json.load(open('jobs.json'))"`.
Per 2026-11-13 reference: 503-no-fallback is normally NEEDS-HUMAN, no force-rerun — raising output budget + pinning model is the config-side mitigation; do NOT force-rerun the failed job.

## llm-wiki "not found" notice
Confirmed BENIGN name collision: `research/llm-wiki` (identical 20113-byte SKILL.md at both `~/.hermes/skills/research/llm-wiki/` and the home mirror) shadows the `_overrides/llm-wiki` the cron skill-field expects. No action.

## Other
30 empty-wikilink Related lines (`- — ` / `-  — `) persist — residual known class, manual fix has no reliable mapping; leave.
