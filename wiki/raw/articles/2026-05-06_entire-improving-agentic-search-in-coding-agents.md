---
title: "How We Improved Agentic Search"
source: "https://entire.io/blog/improving-agentic-search-in-coding-agents"
date: 2026-05-06
author: Evis Drenova
company: Entire
scraped: 2026-05-08
tags: [agentic-search, coding-agents, pgr, ripgrep, fff, MCP, search-quality, benchmarking]
---

## TL;DR

We analyzed real coding-agent traces, built public benchmarks, and compared `ripgrep`, `fff`, and `pgr` to see what actually improves agentic code search. The clearest result was that faster search alone only modestly helps, while better-ranked results improve first-query retrieval and help agents find the right code sooner.

## How Do Agents Search?

At Entire, we capture AI agent traces and make them searchable and shareable across agents and teammates. We call each trace a **checkpoint**. It contains the user prompts, agent responses, tool calls, and the resulting code diffs.

Public dataset from `entireio/cli`:
- **Total checkpoints analyzed:** 1,983
- **Total tool calls analyzed:** 202,142
- **Search-related tool calls:** 98,555 (48.8% of all tool calls)

Search-related tool call breakdown:
| Category | Count | Percentage |
|----------|-------|-----------|
| Read / file retrieval | 48,322 | 49.0% |
| Bash search fallback | 23,180 | 23.5% |
| Grep / content search | 23,136 | 23.5% |
| Other | 3,917 | 4.0% |

Key findings:
1. **Search is a first-order operation of agent behavior.** Nearly half of all tool calls were search-related.
2. **The search workflow is fragmented.** Agents bounce between file reads, bash-based search, and grep-style content search.

## Faster Search Wasn't the Bottleneck

60-task search-sensitive benchmark comparing baseline (ripgrep) vs fff (stateful MCP search server with bigram index, mmap, SIMD):

| Metric | Baseline (ripgrep) | fff |
|--------|-------------------|-----|
| Avg wall clock per run | 38.57s | 36.99s |
| Avg tool calls | 19.12 | 17.90 |
| Avg total tool execution time per run | 0.140s | 0.055s |
| Tool execution share of wall clock | 0.4% | 0.1% |
| Avg search_code duration | 15.5ms | 5.7ms |
| Median search_code duration | 14.7ms | 1.7ms |

**Key insight**: Tool execution was only ~0.4% of total wall clock time. The agent spends most of its time in model inference, result interpretation, and next-step planning — not waiting for search.

## The Systems Tested

1. **Baseline: raw ripgrep** — plain ripgrep with minimal post-processing, no ranking layer
2. **fff** — stateful MCP search server with bigram index, mmap, SIMD-accelerated scanning, frecency ranking (optimized for speed)
3. **pgr** — Entire's agent-oriented search tool: definitions first, source files before tests/vendor, grouped and trimmed output, richer result presentation

## Broad Mixed-Workload Benchmark (60 tasks)

| Metric | Baseline | fff | pgr |
|--------|----------|-----|-----|
| Avg wall clock | 34.98s | 34.97s (-0.0%) | 33.67s (-3.8%) |
| Avg tool calls | 18.45 | 18.72 (+1.4%) | 18.90 (+2.4%) |
| Avg cost | $0.4030 | $0.3797 (-5.8%) | $0.3698 (-8.2%) |
| Avg search calls | 6.12 | 5.70 (-6.8%) | 5.53 (-9.5%) |

## Offline Retrieval Quality (First-Search Replay)

| Metric | Baseline | fff | pgr |
|--------|----------|-----|-----|
| MRR | 0.3177 | 0.3059 | 0.4053 |
| Hit@1 | 26.0% | 18.0% | 34.0% |
| Hit@3 | 34.0% | 42.0% | 42.0% |
| Avg output chars | 6565.9 | 1427.0 | 1587.1 |

**Where gains were strongest**: Implementation prompts — MRR 0.3061 → 0.5000, Hit@1 14.3% → 42.9%

## What Actually Held Up

1. **Faster search was not the main bottleneck** — fff's dramatic speed-up only modestly improved end-to-end
2. **Ranking clearly improved retrieval quality** — pgr consistently outperformed on first-result relevance
3. **Strongest effect was local improvement, not universal efficiency win** — better search helps agents find better candidates earlier

## What Did NOT Hold Up

Better code search does NOT reliably mean fewer tool calls and lower cost across ALL coding-agent tasks. Task variance was large enough to swamp small local improvements.

## Systems & Repositories

- **[pgr](https://github.com/entireio/pgr)** — Rust MCP search tool (agent-oriented, definitions-first ranking)
- **[fff](https://github.com/dmtrKovalenko/fff)** — Stateful MCP search server (bigram index, SIMD, frecency)
- **[entireio/cli](https://github.com/entireio/cli)** — Open source Entire CLI (source of benchmark data)
- **[Benchmark data](https://github.com/entireio/pgr/blob/main/public_release/data/entireio_cli_checkpoints_2026_04_15/summary.json)**
