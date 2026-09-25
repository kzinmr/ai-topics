---
title: Weekly Wiki Graph Analysis 2026-09-25
created: 2026-09-25
updated: 2026-09-25
type: query
tags: [knowledge-management, wiki]
sources: []
confidence: high
---

# Weekly Wiki Graph Analysis — 2026-09-25

Full-corpus recursive graph scan (3,112 pages) vs. baseline [[queries/wiki-graph-analysis-weekly-2026-09-18]]. Methodology unchanged: recursive walk over `entities/ concepts/ comparisons/ queries/ events/`, wikilink + `related:` field resolution, redirect-aware duplicate grouping. State snapshot persisted to `_meta/graph-analysis-state.json` for next-week delta diffing (first time this has been done — future runs can report true set-deltas, not just counts).

## Summary (delta vs 09-18)

| Metric | 09-18 | 09-25 | Δ | Notes |
|---|---|---|---|---|
| Total pages | 3,079 | 3,112 | +33 | entities 935 (+9), concepts 2,099 (+19), events 35 (+2), comparisons 35, queries 8 |
| Orphans (no inbound) | 446 | 465 | +19 | content-rich (≥50L): 303 → 316 |
| Broken wikilink targets | 1,758 | 1,993 | +235 | refs 2,810 → 3,512 (+702) |
| Real duplicate groups | 8 (person/tool) | 8 + 48 (dir-collision) | — | 09-18's 8 groups all STILL unresolved; new taxonomy below |
| Oversized (>200L) | 243 | 315 | +72 | >600L: 10 pages |
| Stale (>90d) | 1,661 | 2,230 | +569 | 2026-06 batch crossed the 90d line; see caveat |
| Missing frontmatter | n/a | 9 | — | all `sources:` field missing (local-llm cluster) |
| Contested / low-confidence | — | 1 / 2 | — | healthy |

Note: prior report's "2,810 refs" counted per-file occurrences; this run's 3,512 is same-definition. The +235 broken targets are mostly fresh ingests guessing slugs (see §1).

## 1. Broken links — dominant structural debt (3,512 refs)

| Category | Refs | Example |
|---|---|---|
| path-missing | 974 | `[[concepts/context-engineering]]` (no `_index.md`), `[[concepts/claude-code/claude-code]]` (35 refs) |
| raw/transcripts-as-wikilink | 666 | provenance pointers, not pages — lint-exempt candidate |
| bare-missing | 279 | `[[agent-evaluation]]` (24 refs, actual page is `concepts/evaluation/agent-evaluation`?) |
| related-field broken | 74 | `related:` frontmatter entries pointing at nonexistent files |

**Top single lever unchanged since 09-18:** `concepts/context-engineering` dir-hub — **188 refs** point at it, `concepts/context-engineering/index.md` (377L) exists but Obsidian/linters don't resolve `[[concepts/context-engineering]]` → `index.md` in path-qualified conventions. Creating a 1-line `_index.md` (or renaming) kills the largest cluster. Next hubs: `concepts/gemini` (23), `concepts/post-training` (14), `concepts/coding-agents` (10), `concepts/evaluation` (8), `concepts/training` (8) — 18 dir-hub targets total.

## 2. Duplicates — two distinct classes (this is the refined taxonomy)

**Class A — true duplicates needing merge (8, ALL carried over unresolved from 09-18):**
1. `entities/eugeneyan` vs `entities/eugene-yan`
2. `entities/lilianweng` vs `entities/lilian-weng`
3. `entities/gilesthomas` vs `entities/giles-thomas`
4. `entities/deliberate-coder` vs `entities/deliberatecoder`
5. `concepts/deerflow` vs `concepts/deer-flow`
6. `concepts/alphaproof-nexus` vs `concepts/alpha-proof-nexus`
7. `concepts/dspyrlm` (stub) vs `concepts/dspy-rlm`
8. `concepts/open-claw-ecosystem` (stub) vs `concepts/openclaw-ecosystem`

**Class B — flat-vs-subdir collisions (48 real pairs, mostly NOT true dups):**
The wiki grew nested topic dirs (`harness-engineering/`, `local-llm/`, `sandbox/`, `context-engineering/`, `post-training/`) and pages migrated or were re-created there while thin stubs (many exactly 25L) remained at the old flat path. **Path-qualified wikilinks still resolve both**, so bare `[[vllm]]` links are ambiguous. Worst offenders by combined size: `advanced-tool-use` (113/182), `agent-skills` (224/113), `agentic-engineering` (388/237), `context-engineering` (365/25), `model-quantization` (434/154), `context-window-management` (271/119), `managed-agents` (130/298), `symphony` (207/209), `subagents` (143/153), `writing-tools-for-agents` (163/159). Fix pattern: convert the thin flat copy into a redirect (like samuelcolvin/martin-fowler already do), or merge if content genuinely diverges. ~22 of the 48 are 25-line stubs — pure redirect candidates.

**Class C — by-design (exclude from dup counts):** entity+concept pairs (cline, qwen), concept+comparison pairs (agent-harnesses, evals-skills, llm-integration-patterns), dir `index.md` hubs.

## 3. Orphans (465; 316 content-rich)

Top content-rich orphans to attach inbound links to: `concepts/ai-energy` (329L, up from 284L — actively updated but still zero inbound), `concepts/multi-objective-policy-distillation` (279L), `entities/openenv` (234L), `concepts/claude/system-card-milestones` (231L), `entities/ibrahim-diallo` (227L), `concepts/symphony` (208L — note: its subdir twin is also rich; see dup §2B). Same root cause as last week: subdir pages rarely receive inbound links from flat pages. The `ai-energy` case is notable — sibling crons keep *editing* it without any page linking to it.

## 4. Stale (>90d): 2,230 — mostly artifact, not rot

The +569 jump is the June ingest batch crossing the 90-day line, dominated by the long-tail blogger entity cohort (2026-04-10 batch onward). These pages are expected to be infrequently updated. **Recommendation:** adopt a staleness policy note in `wiki-maintenance` (entity pages: 180d threshold; concept pages: 90d) rather than batch-touching 2,230 files.

## 5. Frontmatter gaps (9)

`sources:` field entirely missing on: `concepts/llama-cpp`, `concepts/ollama`, `concepts/ollama-local-llm-runner`, `concepts/gguf`, `concepts/gguf-quantization`, `concepts/model-quantization-for-local-llms`, `concepts/mechanistic-interpretability`, `concepts/local-llm/llama-cpp` (+1). Small local-llm cluster; trivial fix.

## 6. Oversized (315; +72)

>600L: `concepts/agentic-search` (1,191L), `entities/simon-willison` (977L), `entities/harvey` (960L), `entities/ed-zitron` (918L), `entities/anthropic` (863L), `concepts/rlm-recursive-language-models` (742L), `entities/fireworks-ai` (740L), `concepts/dspy-rlm` (698L). Growth rate (+72/week) outpaces splitting; suggest wiki-health-fix claim one per run.

## Recommended actions (priority)

- **[HIGH] Create `concepts/context-engineering/_index.md`** — 188 broken refs, 5-minute fix, largest single lever for the 4th consecutive week. Then the remaining 17 dir hubs.
- **[HIGH] Resolve the 8 Class-A duplicates** — carried over a second week; stubs → redirect with alias preserved.
- **[MEDIUM] Convert ~22 flat 25L stubs in Class-B collisions to redirects** — removes `[[bare-slug]]` ambiguity graph-wide.
- **[MEDIUM] Register `[[raw/...]]`/`[[transcripts/...]]` (666 refs) as lint-exempt** in the watchdog, or convert to inline links.
- **[MEDIUM] Attach inbound links to top-10 content-rich orphans** (start with `ai-energy` — it's actively maintained yet unreachable in the graph).
- **[LOW] Add `sources:` to the 9 local-llm pages**; adopt 180d staleness policy for entity pages.
- **[NEW] State snapshot** now persisted at `_meta/graph-analysis-state.json` — next run should diff sets (which orphans/dups are new/resolved), not just counts.
