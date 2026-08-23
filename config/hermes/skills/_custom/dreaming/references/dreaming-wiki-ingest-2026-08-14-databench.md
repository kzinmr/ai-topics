# Dreaming Wiki-Ingest Recovery — 2026-08-14 (Hex DataBench)

Session that validated the 2026-08-11 pattern-extension: **an accurate upstream saturation verdict does not cover the sitemap batch.** Commit `11a7ad91`.

## Scenario

- Pre-run script: `failed to parse JSON response from dreaming-group output`; output_path `2026-08-14_18-17-26.md` (4,700 lines).
- Recovery path (Pitfall #12 + #21): `triage_latest.json` (18:15, 11 decisions, all skip) valid on disk; upstream commit `86382089` (18:17) already committed log entry + archive JSON + archive_index.json. Looks like a pure "upstream archive-only, Takes=0" variant — but the downstream probe was still run.
- Upstream verification table was fully ACCURATE for its 11 candidates (all genuinely covered with line refs). Its summary claimed "24 unarchived articles all processed or low-value."

## What the probe found

`python3 config/hermes/skills/_custom/dreaming/scripts/check_archive_index_absence.py` → 4 never-archived files:

| File | Verdict |
|------|---------|
| `blog.voyageai.com--2026-08-13-voyage-code-4--cce0287e.md` | ✅ Covered — blog-wiki-ingest take today → `entities/voyage-ai.md`; archived as skip |
| `johndcook.com--...-constructing-hadamard-matrices--510024ee.md` | ✅ Covered — blog-wiki-ingest take today → `concepts/claude-fable-jacobian-conjecture.md`; archived as skip |
| `2026-08-12_hebbia_...third-bridge...md` | ✅ Covered — Jul 2025 integration announcement; data-source mention `entities/hebbia.md` L57; no technical depth; archived as skip |
| `2026-08-14_hex-technologies_databench-agentic-analytics-benchmark.md` | ❌ **Genuine gap** — sitemap 06:00 scrape, NO pipeline triaged it → created `concepts/ai-benchmarks/databench.md` + enriched `entities/hex-technologies.md` |

Key lesson: upstream's candidate list (from the checkpoint) and the sitemap batch (from `raw/articles/`) are DISJOINT SETS. A perfect verdict on the candidate list says nothing about sitemap articles that never entered the checkpoint.

## Downstream recovery flow (reuse pattern)

1. **Probe first**: run `check_archive_index_absence.py`, read only the never-archived files (skip the 100+ already-covered ones).
2. **Verify each never-archived file**: `find wiki -name "*keyword*"` for pages; `grep -n` the entity page for the article's specific claims. Two of the four were blog-wiki-ingest takes from the same day — the blog-ingest race-condition check (log.md same-day entries) resolves them fast.
3. **Merge new decisions into the EXISTING `triage_latest.json`** (do not overwrite): load JSON, append new decisions with unique `item_id`s (dedupe by item_id), sort take→reference→skip, recompute `total_decisions`/`takes`/`references`/`skips`, append a `[downstream YYYY-MM-DD HH:MM: ...]` note to `summary_ja`. Use a `/tmp/` Python script (cron-safe, JSON with Japanese → write_file, not heredoc).
4. **Re-run archive** `python3 scripts/archive_triage.py dreaming --keep-reference` → yields 14 candidates, 3 new archived, 11 dedup (upstream's URLs already in index). ⚠️ This run MODIFIES the same dated archive JSON that upstream committed (`2026-08-14_20260814T181151Z.json`) plus `archive_index.json` — so git status shows `M` (not `??`) on those files, and they MUST be staged alongside content changes. This differs from the "skip archive re-run" variant (Pitfall #21.7) where upstream already committed everything — here the re-run adds genuinely new URLs.
5. **Create/enrich pages** directly (patch, not write_file for rich pages): new benchmark page `concepts/ai-benchmarks/databench.md` (tags: benchmark, evaluation, agent-evaluation, text-to-sql, data-science, llm-as-judge — all in SCHEMA); enriched `entities/hex-technologies.md` (frontmatter `updated` + sources + DataBench section + related wikilink).
6. **index.md**: add entry alphabetically in the ai-benchmarks section (databench after cybench); bump `## Concepts (N pages)` count.
7. **log.md prepend** via entry-file pattern (leading blank line, italic anchor, trailing `\n\n`, ASCII-only script).
8. **Commit + push**: explicit `git add` of the 6 files; hooks passed cleanly (tag validation 4 files, index clean).

## The DataBench content (what made it a take)

- 100 realistic Q&A/open-ended analytical tasks in Shorelane Commerce synthetic warehouse; GPT-5.6 Sol LLM judge (majority-of-3, 96% agreement); 10 "signature traps."
- Key results: no model <50% floor; GPT-5.6 Luna Pareto frontier (~1/14th cost); Opus 5 effort regressions vs CursorBench's clean test-time curves; Fable 5 the exception (85/100); task breakdown 75/66/54 (judgment gap); "manufacturing certainty" failure mode.
- Hex plans to open-source the Shorelane environment (DataBench stays private to avoid training contamination).
- Nav chrome: ~100 lines of repeated CTA/nav boilerplate before the body — grep for "benchmark"/model names instead of judging by the first 50 lines.
