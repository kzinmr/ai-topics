# Dreaming-group triage — 2026-10-20 validation (4 genuine gaps in a 64-file never-archived pool)

Context: checkpoint `20261020T180026Z`, `total_articles: 0` / `recent_raw_articles: 236`. `triage_latest.json` was stale (Oct 19 18:17, consumed by yesterday's downstream), `grouped_themes_latest.json` from Jun 30. No upstream dreaming commit in today's `git log` (last were active-crawl `97510378` + trending-topics `f4d1b238`). This run owned the triage.

Verdict: **Takes=0, References=4, Skips=6 batch decisions** covering ~64 never-archived files.

## The 4 references (all verified as genuine gaps by grepping the SPECIFIC proper noun in the target page)

| Candidate | Target page | Gap signal |
|---|---|---|
| Together Post-Training (RL env rewards + SFT custom-model service) | `entities/together-ai.md` (150 lines) | page lists "Fine-Tuning Platform" only, zero "Post-Training" |
| Harvey Graph (knowledge+context graph, LAB rubric +30%, cost -50%, 0%->75% case, memory 93%/50% survey) | `entities/harvey.md` (959 lines) | `grep -c "Harvey Graph"` = 0 despite Harvey II/Tenet section existing |
| Modal NVIDIA Vera CPU sandboxes (Arm, 2x throughput, P50 bursting) | `entities/modal-labs.md` | zero "Vera"/"Arm" hits |
| Factory x Databricks partnership | `entities/factory.md` | zero "Databricks" hits - but raw scrape FAILED (21 lines: date+nav only) -> downgrade to 3-star light one-line enrichment; downstream may re-fetch URL |

Key lesson: a 959-line entity page can still have a genuine zero-hit gap on the article's core proper noun. Always `grep -c "<exact product name>"` on the page - page size and topic overlap are not coverage proof.

## Batch skips that worked (structure-based, no deep read needed)

- **Hex marketing batch x6**: all SEO comparison posts (Looker/Power BI/Tableau alternatives, "what is an AI analytics platform"). Distinguish from the Oct 14 DataBench take by body content - these have no benchmark/model results. Batch-skip after title scan.
- **Glean `/fr/blog` x10**: French sitemap mirrors, same recipe as 2026-10-19.
- **Non-AI blog batch ~30**: dfarq/johndcook/daringfireball Apple-hardware/math/link-digests, pluralistic weekly, LinkedIn photo post, Obama political X thread (via daringfireball).
- **Already-covered batch**: redact.dev WhatsApp hidden-AI-instructions, MiniMax M3.1 Flash, Simon Willison obituary post (all trending-topics `f4d1b238`); DeepInfer, Stealthium ROME weight-tampering, Beacon company world models, Cloudflare Clairic, Anthropic employment (all active-crawl `97510378`). Match raw basenames against today's commit messages + `existing_wiki_pages` list from the checkpoint.

## Process notes

- Ran ONLY the archive-index absence probe (`check_archive_index_absence.py`, full path under `config/hermes/skills/_custom/dreaming/scripts/`) - it was the sole candidate list, per the 10-19 recipe.
- Built triage JSON via `write_file /tmp/...py` + `terminal python3`; field `recommended_action`; verified with hardcoded-path `python3 -c` (no pipes).
- Did NOT run `archive_triage.py` (downstream dreaming-wiki-ingest's step).
- Made zero wiki edits -> `git status --short -- wiki/` clean -> no commit this run; the triage JSON at `${HERMES_HOME}/cron/data/dreaming/triage_latest.json` is the sole output for the 18:20 downstream.
