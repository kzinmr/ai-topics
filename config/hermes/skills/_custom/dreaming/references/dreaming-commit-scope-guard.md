# Saturated-Day Commit Pattern — Commit-Scope Guard (Validated 2026-08-22)

## When to Use
Whenever you commit a dreaming cycle (saturated day OR a day with genuine enrichments), before running `git commit` / `git push`, verify that the commit does NOT sweep in sibling/cron artifacts that are not part of the dreaming job's output.

## The Guard (one call)
```bash
cd ~/ai-topics && git status --short 2>&1 | grep -E "^(M|\?\?)\s" | grep -vE "wiki/(log\.md|entities/|concepts/|comparisons/|queries/|raw/archived/triage/dreaming/|raw/articles/)"
```
Anything that matches is a file you did NOT intend to stage. If the list is non-empty, you must stage explicitly (never `git add -A` / `git add .` / a broad `git add wiki/`).

## Known sibling/cron artifacts that MUST NOT be committed by dreaming
- `config/hermes/cron/jobs.json` — managed by the cron runner / watchdog; dreaming never touches it
- `config/hermes/skills/**` — skill files; edited by the curator / skill-management jobs, not dreaming
- `AGENTS.md` — repo docs; dreaming does not edit it
- `inbox/**` — newsletter digests; owned by the email pipeline
- `wiki/raw/newsletters/**` — owned by newsletter-ingest
- `wiki/raw/archived/triage/{blog,newsletter}/**` — owned by their respective archives
- `wiki/raw/archived/triage/dreaming/<other-date>*.json` — only stage TODAY's dreaming archive file, not stale ones from prior sessions
- `bin/`, `scripts/` — repo tooling

## Why this matters
The pre-commit hooks (index validate + tag validator + language policy) only check STAGED files. If `git add wiki/` or `git add -A` accidentally stages a sibling file that has a pre-existing tag violation, a CJK block, or a missing index entry, the commit is blocked on a file you never touched. Selective staging sidesteps the failure AND keeps the commit scoped to the job's actual output.

**Validated 2026-08-22**: `git status --short` showed 30+ modified/deleted skill files (`config/hermes/skills/_custom/blog-author-thought-analysis/`, `cross-leader-synthesis/`, `opinion-leader-*`, etc.), `AGENTS.md`, `config/hermes/cron/jobs.json`, plus untracked `wiki/raw/articles/2026-08-22_*` and `wiki/raw/newsletters/2026-08-21_*`. Dreaming staged ONLY: `wiki/entities/decagon.md`, `wiki/log.md`, `wiki/raw/archived/triage/archive_index.json`, `wiki/raw/archived/triage/dreaming/2026-08-22_*.json`. Commit `2ead23f7` passed `✅ Tag validation passed — 2 files, all tags in SCHEMA taxonomy` with NO `--no-verify` needed. Pushed cleanly.

## Interaction with the `--no-verify` guidance in the parent reference
The main `dreaming-saturated-day-commit-pattern.md` reference documents `--no-verify` as the fallback when selective staging still trips hooks (typically `archive_index.json` carrying stale content). That fallback is correct for TRUE archive-only days. But when you DO stage a real enriched entity/concept page + log.md + today's archive, the hooks will pass cleanly — validated 2026-08-22 (`2ead23f7`) and 2026-08-15 (`80bc3d3a`), 2026-08-13 (`7be9e887`), 2026-08-02 (`376e98ca`). Prefer running the hooks; only fall back to `--no-verify` if a specific stale-file violation blocks the commit AND you've confirmed the offending file is not yours to fix.
