# Dreaming wiki-ingest — 503-upstream saturation, 2026-08-27

## Failure signature
- Pre-run `dreaming.py` returned `{"ok": false, "error": "failed to parse JSON response from dreaming-group output", "output_path": "..."}`.
- The cron output file (4,729 lines / 341KB) was NOT a completed analysis — `L1` said `# Cron Job: dreaming-group (FAILED)` and the tail (L4725-4728) ended in `## Error` → `RuntimeError: HTTP 503: Local LLM server is busy`. The large size was just the prompt + skills + injected checkpoint, **no Theme Clusters section to recover**.
- `triage_latest.json` was STALE (prior day, consumed). No dreaming commit today (`git log --since="TODAY 00:00"` showed only trending/active-crawl/blog-ingest/slack commits).

**Detection**: when the output file is huge but its tail is an `## Error` block (503 / render failure) rather than `## Theme Clusters`, the upstream LLM never produced analysis. Do NOT read the tail expecting clusters. This is distinct from Pitfall #12's "output file contains completed analysis" variant (where the tail HAS `## Theme Clusters`).

## Recovery path (503-upstream variant)
1. Confirm no partial triage: `git log --oneline -15` (no dreaming commit today) + `triage_latest.json` mtime is prior-day.
2. Checkpoint: `latest.json` payload → `total_articles: 0`, `recent_raw_articles: ~195` → Pattern E.
3. **Run BOTH probes** (see SKILL.md 503-upstream variant note):
   - `python3 config/hermes/skills/_custom/dreaming/scripts/check_archive_index_absence.py` → the DECISIVE "never-triaged" list (URLs absent from `archive_index.json`). 08-27: 103 recent raw articles.
   - `python3 scripts/raw_backlog_collect.py --count 12 --dry-run` → older backlog candidates; 08-27 it ranked a 2025 GPT-OSS post first and a same-day already-processed HF post second — both `archive_status: null`. Used only to find genuine older gaps, not as the primary signal.
4. Cross-check top candidates against today's `git log` + `wiki/log.md` (today was dense: OpenAI HF post-mortem, NVIDIA $13B HF acquisition, AWS/DuckLabs, GLM-5.3-Flash, WebMCP, Qwen3.8-Flash-Next, etc.).
5. The 06:00 sitemap batch (Glean, Harvey, Hebbia, Pinecone, ElevenLabs, Fireworks, Factory) was the genuinely-untriaged pool. Read the most AI-substantive bodies; most were marketing/nav-chrome → batch-skip.
6. **One genuine gap**: `fireworks-ai_post-training-kimi-k3-with-harvey-for-long-horizon-legal-work` — Fireworks × Harvey post-trained a Kimi K3 base (async RL on Training API) into Harvey Tenet. `entities/fireworks-ai.md` had the June train/serve-numerics + batch-invariance infra section but NO K3×Harvey application section. `entities/harvey.md` L436-447 already had the Harvey-side GSPO methodology → do NOT duplicate. Enriched `entities/fireworks-ai.md` with the application section (LAB all-pass 19.7% vs 10.8%, APEX 58.8→74.0, Redline cross-harness 49.3→55.5, $5.92 vs $5.62/task).
7. Triage JSON: `source: "dreaming"`, Takes=0, Ref=1, Skip=2 (two URL-less batch skips). Saved to `${HERMES_HOME}/cron/data/dreaming/triage_latest.json`.
8. `python3 scripts/archive_triage.py dreaming --keep-reference` → 1 URL newly archived (total_archive_urls 2803→2804); the 2 URL-less batch skips are written to the dated JSON but NOT URL-indexed (expected).
9. log.md via `config/hermes/skills/_custom/dreaming/scripts/repair_log_md_header.py wiki/log.md /tmp/dreaming_log_entry_<date>_<time>.md` (healthy header this run: 1 header L1, italic L3; entry landed L6, blank count stable ~1463).
10. **Selective staging** (see below). Commit `55afadcd` passed tag + index + language hooks cleanly. `git push` succeeded directly (no `pull --rebase`).

## Selective staging on a dirty sibling tree
`git status --short` showed **482** changed files (config/hermes/skills/*, AGENTS.md, jobs.json, other-pipeline artifacts). Do NOT `git add wiki/`. Stage exactly the dreaming cycle's 4 files:
```
git add wiki/entities/fireworks-ai.md wiki/log.md \
  wiki/raw/archived/triage/archive_index.json \
  wiki/raw/archived/triage/dreaming/2026-08-27_20260827T180502Z.json
```
Diff stat was clean (+104/−2). This is the "saturated-day WITH reference enrichment" variant: no new page, no index.md change needed (`entities/fireworks-ai` already in index.md L311 with a descriptive summary — an in-page enrichment does NOT require an index edit).

## CJK / language check
Enriched page content was English-only; CJK-range scan (`[\u3040-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF]`) returned 0 lines before commit.

## Lessons
- 503 at the dreaming-group step = no analysis to recover; fall straight through to Pattern E. The output-file tail is the discriminator (`## Error` + 503 vs `## Theme Clusters`).
- `raw_backlog_collect.py` (ai-hint ranking, `skipped_processing_fresh=0`) is NOT a dedup signal — it surfaces same-day already-processed files. `check_archive_index_absence.py` (archive-index URL-absence) is.
- A dual-entity post (Fireworks×Harvey) can have its two halves already split across pages: Harvey-side methodology in `entities/harvey.md`, Fireworks-side infra in `entities/fireworks-ai.md`, with the **application + concrete numbers** being the genuine gap on only one side. Verify each side before deciding which to enrich.
