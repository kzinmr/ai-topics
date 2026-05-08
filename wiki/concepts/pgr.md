---
title: pgr
type: concept
created: 2026-05-08
updated: 2026-05-08
status: L2
tags: [agentic-search, coding-agents, MCP, search-tool, rust, ripgrep, tool-calls]
sources:
  - "[[raw/articles/2026-05-06_entire-improving-agentic-search-in-coding-agents]]"
  - https://github.com/entireio/pgr
related:
  - ripgrep
  - fff
  - MCP
---

# pgr — Agent-Oriented Code Search

`pgr` is an open-source Rust MCP search tool built by [Entire](https://entire.io) that improves how coding agents search codebases. Unlike traditional grep-based search that returns results in filesystem order, `pgr` re-ranks results to prioritize what the agent most likely needs — definitions first, source files before tests and vendor directories, with grouped and trimmed output.

## Core Design

- **Definitions-first ranking**: Struct definitions, function signatures, and type declarations are surfaced before implementation details
- **Path-aware prioritization**: Source files rank above test files, vendor directories, and generated code
- **Grouped and trimmed output**: Results are organized and pruned to reduce token burden and help the agent decide the next step faster
- **MCP interface**: Speaks JSON-RPC over stdio — `initialize`, `tools/list`, `tools/call` (search_code)
- **Written in Rust**: Performance parity with `ripgrep` at the scan layer

## Why Ranking > Speed

Entire's public benchmark study (60 tasks, `entireio/cli` repo) compared three search backends:

| Backend | Type | Speed Focus | Ranking |
|---------|------|------------|---------|
| `ripgrep` (baseline) | Standard grep | Moderate | None |
| `fff` | Bigram index + SIMD | Extreme | Frecency |
| `pgr` | Definitions-first | Moderate | Path-aware |

**Key finding**: `fff` drove median `search_code` latency from 14.7ms to 1.7ms, but end-to-end wall clock only improved 38.57s → 36.99s (1.6%). Tool execution is only ~0.4% of total agent runtime — the agent spends most time in model inference, result interpretation, and planning.

In contrast, `pgr` improved **first-query retrieval quality**:
- MRR: 0.3177 → 0.4053 (+27.6%)
- Hit@1: 26.0% → 34.0% (+8 points)
- On implementation prompts: Hit@1 14.3% → 42.9% (+28.6 points)

## Agent Search Behavior

Entire's analysis of 1,983 real coding-agent checkpoints (~202K tool calls) from the open-source `entireio/cli` repo found:

| Search Category | Tool Calls | % of Search |
|----------------|-----------|------------|
| Read / file retrieval | 48,322 | 49.0% |
| Bash search fallback | 23,180 | 23.5% |
| Grep / content search | 23,136 | 23.5% |
| Other | 3,917 | 4.0% |

**48.8% of all agent tool calls are search-related** — search is the most frequent tool operation in coding agents.

## Architecture

```
Agent (Claude Sonnet, etc.)
    │
    ▼
search_code(query="CheckpointStore", max_files=5)
    │
    ▼
MCP Server (pgr, ripgrep, or fff)
    │
    ▼
Ranked & formatted results
    │
    ▼
Agent reads top file(s)
```

The `search_code` tool presents a unified interface regardless of backend. The agent issues the same call structure; only result ranking and formatting change.

## Benchmark Results

### Broad Mixed-Workload (60 tasks, Claude Sonnet)

| Metric | Baseline (ripgrep) | fff | pgr |
|--------|-------------------|-----|-----|
| Avg wall clock | 34.98s | 34.97s | 33.67s |
| Avg tool calls | 18.45 | 18.72 | 18.90 |
| Avg cost | $0.4030 | $0.3797 | $0.3698 (-8.2%) |
| Avg search calls | 6.12 | 5.70 (-6.8%) | 5.53 (-9.5%) |

### Offline Retrieval Quality (first-search replay, 50 queries)

| Metric | Baseline | fff | pgr |
|--------|----------|-----|-----|
| MRR | 0.3177 | 0.3059 | 0.4053 |
| Hit@1 | 26.0% | 18.0% | 34.0% |
| Hit@3 | 34.0% | 42.0% | 42.0% |

## Limitations

- **Does not universally reduce tool calls**: On broad mixed workloads, task variance swamps local improvements. Total tool call counts remained noisy.
- **Held model fixed (Claude Sonnet)**: Effects may differ across models — some planners may be more sensitive to ranking quality.
- **Lexical, not semantic**: `pgr` re-ranks lexical grep matches. It does not use embedding-based semantic search (future work).

## Relation to Other Agent Search Approaches

| Tool | Approach | Goal |
|------|----------|------|
| `ripgrep` | Lexical grep, filesystem order | Fast content matching |
| `fff` | Bigram index + SIMD + frecency | Maximum speed |
| `pgr` | Definitions-first, path-aware ranking | Agent relevance |
| Semantic search (future) | Embedding-based retrieval | Meaning-based matching |

## See Also

- [[entities/entire]] — Company behind pgr
- [[entities/evis-drenova]] — Author of the study
- `ripgrep` — The baseline search tool
- `fff` — Fast indexed MCP search server by Dmitry Kovalenko
