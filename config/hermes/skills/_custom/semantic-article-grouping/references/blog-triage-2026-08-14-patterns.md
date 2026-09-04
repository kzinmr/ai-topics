# Blog Triage 2026-08-14 Patterns

Run `20260814T102115Z` (blog-ingest 10:21 UTC). 19 candidates + 1 unsaved. Result: **Takes=3, References=2, Skips=15** (20 decisions). Archive: 17 new (total 2,634 URLs). Commit `7e6ba774`.

## Takes (all ★★★★☆ existing-page updates — zero new pages needed)

1. **voyage-code-4** (Voyage AI, Aug 13) → enrich `entities/voyage-ai.md`.
   - Next-gen code embedding model purpose-built for coding agents. New "agentic code retrieval" benchmark (19 datasets built from issue-fixing PRs — query = issue description, relevant docs = files the merged fix touched) beats Cohere Embed v4 / Gemini Embedding 2 by 28.25% / 31.03%; on the 28 legacy code-retrieval datasets beats voyage-code-3 / Cohere / Gemini / OpenAI v3 large by 13.98% / 19.21% / 16.01% / 40.06%.
   - $0.12/1M tokens (third below voyage-code-3). Matryoshka dims 2048/1024/512/256, float32/int8/binary quantization. Training corpus from natural-language queries to code (hundreds of languages).
   - Gap check: entity page covered voyage-code-3 in Key Products but had NO voyage-code-4 section (updated 2026-08-09). log.md had zero "voyage-code" hits → genuine gap.

2. **Gemini 3.7 Flash release, detected via plugin release note** (simonwillison.net "Release: llm-gemini 0.33", Aug 13) → update `concepts/gemini/index.md` (Recent Updates section) or create `concepts/gemini/gemini-3-7-flash.md`.
   - **Plugin release notes are model-release signals.** The post's value is not the plugin — it confirms "today's Gemini 3.7 Flash release" plus gemini-3.6-flash, gemini-3.5-flash-lite, gemini-embedding-2, gemini-embedding-001 support; LLM 0.32 compat (reasoning traces, server-side tools `-T CodeExecution`).
   - Model-specific delta worth capturing: "minimal" thinking effort option (present in 3.6 Flash) was REMOVED in 3.7 — high/medium/low remain.
   - Gap check: `concepts/gemini/` has per-flash pages (3-1-flash-lite, 3-2-flash, 3-5-flash) + index.md whose "Gemini Drops (July 2026)" section covers 3.6 Flash / 3.5 Flash-Lite but nothing about 3.7. Grep "gemini-3-7|3.7 flash|3.7-flash" across wiki → zero hits → genuine gap.

3. **Same-actor follow-up discovery — Alpöge Hadamard matrix order 668** (johndcook.com "Constructing Hadamard matrices", Aug 13) → enrich `concepts/claude-fable-jacobian-conjecture.md` with an August 2026 follow-up section.
   - Math post mentions in passing: "Yesterday Levent Alpöge announced that he and his collaborators found an example of size 668 and filled in all remaining gaps below 2000" — 668 was the smallest multiple of 4 with no known Hadamard matrix; discovered **using Claude AI**.
   - KEY RECOGNITION: Alpöge is the SAME Anthropic mathematician behind the Fable 5 Jacobian Conjecture counterexample (July 20, 2026) — the existing page `concepts/claude-fable-jacobian-conjecture.md` documents him. A passing mention in a non-AI article is therefore a genuine follow-up to an existing AI-math event page → take (enrich), not skip.
   - In a multi-post series (sphere-packing / constructing / mariner-9), the concrete detail lived in the construct/how-to post (blog-6), NOT the application posts — check each post before deciding which carries the claim.
   - General rule: when a non-AI article names a researcher doing an AI-assisted discovery, grep that name (with diacritic variants) against events/concepts BEFORE skipping.

## References (★★★☆☆)

4. **Supplier Security Questionnaire** (nesbitt.io, Aug 13) → add reference entry to `entities/andrew-nesbitt.md`.
   - Satirical fictional "annual supplier security assessment" from an OSS maintainer's perspective (Ecosyste.ms founder). Section 5 (Artificial Intelligence) is the AI core: AI-generated-code model disclosure, prompt-injection controls for maintainers, distinguishing autonomous-agent contributions from "organic intelligences", training-data consent, AI co-maintainer appointment consent.
   - Pattern: OSS-supply-chain satire with an explicit AI-governance section is reference-worthy for the author's entity page, not a take — the humor carries no benchmarkable data.

5. **sqlite-utils 4.2.1** (simonwillison.net, Aug 13) → reference entry on `entities/simon-willison.md`.
   - Reusable dev-workflow nugget: `uv run --isolated --no-default-groups sqlite-utils --help` as a smoke test that CLI works without dev-dependency groups (`--isolated` ignores `.venv/` extras). Cause: typing_extensions not declared as a real dependency, only present via dev group.
   - sqlite-utils 4.2 itself (transform() schema-preservation improvements, 5 external contributors) = skip: minor release, entity already tracks the tool trajectory, 4.1.1 was previously skipped.

## Pitfalls validated

- **Unicode diacritic grep pitfall**: `grep -i "alpoge"` returns NOTHING for text containing "Alpöge" — ö ≠ o even case-insensitively. When grepping researcher names with diacritics, use the exact unicode form or a character class (`alp[oö]ge`). This cost a false "no matches" on the sphere-packing file that actually contained the mention.
- **Rescue-exception refinement (unsaved_articles)**: the Aug 13 rescue (curl + `<article>` extraction on curleable domains) does NOT apply when the unsaved article is a patch release of an already-documented project. alchemy-utils 0.1a1: 0.1a0 was already referenced in `entities/simon-willison.md` (Aug 12 entry) → patch release = skip even if body were recoverable. Also: curl extraction CAN fail on simonwillison.net (page returned title-only, no `<article>` tag found) — one attempt suffices, don't over-invest.
- **Truncated raw_path filenames**: blog checkpoint raw_paths can be truncated in the on-disk filename (e.g. `shkspr.mobi--...dressing-r--05084e00.md`); read_file with the full guessed path fails with "File not found" even though the file exists. Use `find wiki/raw/articles -name "*<fragment>*"` to locate before treating as missing.
- **Targeted commit on dirty tree**: working tree carried many pre-existing modified/deleted skill files under `config/hermes/skills/` (not from this run). Target `git add` to ONLY this run's artifacts (19 raw articles + archive JSON + archive_index.json) — do not sweep other pipelines' files (sitemap-monitor articles, newsletter raws, inbox summaries) into the blog-triage commit; their owning pipelines commit them.

## Yield note

3 takes / 2 refs / 15 skips from 19+1 candidates ≈ 15% takes — consistent with the composition-shift note (mixed batches of vendor technical explainers + math + culture + tool release notes produce ~15-25% takes, NOT the over-scoring ~5% baseline for homogeneous opinion-blog batches).
