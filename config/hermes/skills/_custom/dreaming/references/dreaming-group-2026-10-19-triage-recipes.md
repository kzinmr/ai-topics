# Dreaming-group Pattern E triage recipes — 2026-10-19 validation

Context: checkpoint `20261019T180026Z` had `total_articles: 0` / `recent_raw_articles: 203`,
and BOTH fallback files were stale (`triage_latest.json` from Sep 19, `grouped_themes_latest.json`
from Jun 30). No upstream dreaming commit after 18:00 UTC (`git log` confirmed). The
`check_archive_index_absence.py` probe (2,836 archived URLs, 77 recent files, 53 never-archived)
was the ONLY candidate list. Final verdict: Takes=0, References=4, Skips=6.

## Workflow that worked

1. Read the real checkpoint at `${HERMES_HOME}/cron/data/dreaming/latest.json` →
   `payload["articles"]: []`, `recent_raw_articles: 203` → Pattern E trigger.
2. `git log --oneline --since=midnight` — enumerate today's adjacent-job commits
   (newsletter-triage, blog-triage, blog-wiki-ingest, active-crawl, trending-topics,
   watchdog). Confirm no upstream dreaming commit exists → this run owns the triage.
3. `python3 config/hermes/skills/_custom/dreaming/scripts/check_archive_index_absence.py`
   → never-archived list. Work top-down.
4. For each candidate: read raw body (past nav chrome) + read target wiki page body →
   classify with the four discriminators below.
5. Build triage JSON via `write_file /tmp/...py` + `terminal python3` (cron mode:
   execute_code blocked, no pipes). Field name is `recommended_action` (NOT `action`).
   Verify with hardcoded-path `python3 -c` (no pipe).
6. Do NOT run `archive_triage.py` from the GROUP job — that is the downstream
   dreaming-wiki-ingest's step (it archives after enrichment finalizes decisions).

## Four coverage-check discriminators

### 1. Same-source raw file = content check, not date check
`entities/aspire-nvidia.md` (created 2026-10-17) had in its `sources:` frontmatter the EXACT
raw file the probe surfaced (`nvidia-aspire-agentic-skills-discovery-robotics-2026.md`).
The right call is still skip — but only AFTER reading the page body and diffing the article's
specific claims (LIBERO-Pro benchmark, model suite GPT-6 Astra / Opus 5.5 / Kimi K3 / Qwen 3.8,
Rubik's-cube sim-to-real tasks) against the page, which covered all of them. A `sources:`
match is a hypothesis of coverage, not proof.

Same pattern: Alderson "How the AI boom might really end: 5 scenarios" — `entities/martin-alderson.md`
L330–340 already carried Haiku 5.5 90%-cheaper/5x-past-100K, GPT-6 Luna 1.5–2x past 272K, the
DeepSeek open-weight price inversion, DWDM/telecom efficiency-overshoot analogy, GPU spot price
as the equilibrium tell, TSMC record revenue vs chip selloff, CoreWeave CDS distress, and the
consumer-surplus conclusion. Verified by grepping for the article's specific proper nouns
(`grep -c "Haiku 5.5" page.md` etc.), not by topic keyword.

### 2. Non-English sitemap mirrors are batch-skips
sitemap-monitor scraped 10 `glean.com/fr/blog/*` files in one 06:00 UTC run
(ngp-sales-launch, ngp-engineering-launch, glean-service-cloud-launch, apps-actions,
prompting-guide ×2, enterprise-agent-development-lifecycle, ...). Detection signals:
- URL path contains `/fr/` (or `/de/`, `/es/`, `/ja/`)
- Body begins with ~40 lines of French nav chrome: "Vue d'ensemble de la plateforme",
  "Découvrez comment fonctionne", "Ancrez l'IA dans le contexte de l'entreprise"
- `type: "sitemap"` frontmatter + `lastmod` timestamps

One frontmatter+chrome read of one file confirms the pattern for the whole batch →
single batch-skip decision citing the English `entities/glean.md` as coverage anchor.

### 3. Tweet-embed raw files are dedup signals
`x.com--finkd-status-2110778025629347999--d99d7a99.md` was Zuckerberg's
"Muse Spark Open -- weights releasing today -- runs great on new Mac Studios thanks to work
with @johnternus and Apple" quote, scraped via daringfireball. Before treating it as a gap,
grep the quote's key nouns (`Muse Spark Open`, `Mac Studio`) across `wiki/entities` +
`wiki/concepts` — `entities/muse-spark.md` L94–117 and `concepts/mlx.md` L57 already had the
full M5 Ultra ×2 / MLX / RDMA cluster story. Skip.

### 4. Curator weekly digests: skip on structure when the lead is non-AI
Pluralistic (Cory Doctorow) weekly digest format: "Today's links" + named sections +
"Hey look at this" + "Object permanence" link dumps. When the lead section is non-AI
(2026-10-19: ad-tech technopolitics / Langdon Winner "Do Artifacts Have Politics?"),
skip without deep-reading the link dumps; only mine them if a section heading names an
AI/LLM/agent topic.

## Probe output caveat

`python3 scripts/raw_backlog_collect.py --count 12 --dry-run` ends its stdout with a trace
history JSON blob (per-session `trace_file`, `llm_calls`, `llm_duration_ms` entries).
`tail -50` therefore shows useless trace data, not candidates — the candidate list is higher
up in stdout. Treat the archive-index absence probe as PRIMARY (3-day window); use
raw_backlog_collect only to reach older-than-3-day candidates the absence probe's window
cannot see.

## Report format that worked

The delivered report used: Duplicate Check Summary (with git-log commit hashes of adjacent
jobs), Consolidation Summary (Takes/Refs/Skips counts), a References table with per-candidate
"specific claims absent from page [line range]" text, a Skips verification table with line
references, and a Notes-for-downstream section warning about the dirty tree
(`wiki/entities/martin-alderson.md` was modified-uncommitted by a sibling session — stage
explicitly, never `git add wiki/`).
