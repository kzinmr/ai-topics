---
title: "Skeleton enrichment run — 2026-11-19 (stub backlog: AI-core concept cluster — 5 pages)"
type: query
created: 2026-11-19
updated: 2026-11-19
tags:
  - query
  - knowledge-management
sources: []
---

# Skeleton enrichment run — 2026-11-19

> Snapshot note from the `skeleton-enrich-daily` cron run (2026-11-19 19:0x UTC).
> The `status: skeleton` backlog remains **empty** (streak since 2026-10-17): frontmatter scans
> across `wiki/entities/` and `wiki/concepts/` return **0** live markers. As in the 2026-11-11/12/13/15/18
> runs, productive action was taken on the `status: stub` backlog — this time the 5 highest-value
> AI/agent-shaped concept stubs: how-coding-agents-work, just-large-models, prompt-driven-development,
> agent-security-patterns, retrieval-augmented-generation.

## Actions this run (5 enriched, 0 new pages, 0 redirects)

| Page | Before | After |
|------|--------|-------|
| `concepts/how-coding-agents-work.md` | 324 B stub | ~6.8 KB — canonical agent-loop explainer: harness loop ASCII diagram, tool-surface table, context management (rot/compaction/agentic search/AGENTS.md), verification loops, 5 failure modes with mitigations |
| `concepts/just-large-models.md` | 304 B stub | ~4.6 KB — scale-first product thesis as applied bitter lesson: elicitation vs compensation scaffolds, harness-tax depreciation, for/against table, practitioner heuristics; grounded in gwern scaling-hypothesis raw article |
| `concepts/prompt-driven-development.md` | 336 B stub | ~4.9 KB — PDD as methodology (prompt corpus as primary artifact); positioning table vs vibe coding / spec-driven dev / harness engineering; anti-patterns; cross-linked (not duplicated) with harness-engineering sub-page |
| `concepts/agent-security-patterns.md` | 328 B stub | ~5.6 KB — pattern catalog vs lethal trifecta: isolation, egress proxy, secret injection/token brokerage, untrusted-content handling, audit/canaries; capability→pattern decision heuristic; residual risks (confused deputy, side channels, supply chain) |
| `concepts/retrieval-augmented-generation.md` | 356 B stub | ~4.8 KB — umbrella RAG page: pipeline stage→wiki-component table, why-RAG vs long context, failure modes (chunk amnesia, lost-in-middle, query mismatch), naive→agentic evolution linking agentic-rag / agentic-retrieval / contextual-retrieval |

## Verification performed

- Git-history richness check: all 5 last touched by 2026-08-15 stub-era bulk commit `da4a8f13` — no richer historical versions
- All wikilinks machine-verified to resolve; dead targets redirected (bitter-lesson→rich-suttons-bitter-lesson, context-rot→context-engineering/context-rot, context-engineering→harness-engineering/system-architecture/, rlvr→post-training/rlvr, llm-evaluation-harness→evaluation/, evals-vs-monitoring→evaluation/evals-vs-monitoring-debate) or demoted to plain text (absorption-frontier, chunking, grounding, neural-reranking, etc.)
- Tags all pre-registered in SCHEMA.md taxonomy — no SCHEMA edits required; pre-commit hook passed clean
- index.md: 5 description updates, 0 new entries, page counts unchanged
- log.md entry prepended via `sed -i '4r'` from temp file

## Remaining backlog

~394 `status: stub` pages. Next-run candidates: `ai-evals-people` (human-evaluator stratum, referenced by benchmark-ceiling/drmaciver), `inference-hardware` (umbrella over the gpu-* cluster + local-llm duplicates), entity-shaped stubs misplaced in `concepts/` (`alex-hall`, `bozavlado`, `brainchop`, `hack-club`, `colin`, `jay-v`), and long-tail devtools stubs.
