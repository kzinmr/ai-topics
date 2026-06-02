# Rethinking Search as Code Generation

**Source:** Perplexity Research
**URL:** https://research.perplexity.ai/articles/rethinking-search-as-code-generation
**Date:** June 1, 2026
**Authors:** Perplexity Research Team

## Abstract

Perplexity introduces **Search as Code (SaC)**, a new search architecture that replaces monolithic search APIs with composable, atomized search primitives exposed as an SDK. Agents generate Python code to orchestrate retrieval, ranking, filtering, fanouts, and aggregation within secure sandboxes — shifting search from a fixed pipeline to a programmable substrate.

## Key Claims

- Traditional search (query → pipeline → resultset) is a bottleneck for agent workflows that need hundreds or thousands of retrieval operations per task
- SaC gives models direct control over each search step via generated code in sandboxes
- The Agentic Search SDK exposes individual building blocks: retrieval, ranking, filtering, fanouts, rendering
- Models assemble primitives on-demand into task-specific pipelines
- SDK optimized via continuous autoresearch loop (iterative SDK improvements validated against latency, codegen quality, task performance)
- Filesystem-based serde preferred over REPL for intermediate state management across turns
- Agent Skills (under 2000 tokens) teach models to use the SDK effectively
- 85.1% token reduction on CVE vendor advisory task (288.7K → 42.9K tokens), 100% accuracy vs <25% for baselines

## Benchmark Results

| Benchmark | Perplexity (SaC) | OpenAI Responses | Anthropic Managed | Exa Agent | Parallel Tasks |
|-----------|-----------------|-----------------|-------------------|-----------|---------------|
| DSQA | **0.871** | 0.733 | 0.815 | 0.530 | 0.810 |
| BrowseComp | **0.805** | 0.720 | 0.598 | 0.380 | 0.560 |
| HLE | 0.612 | **0.614** | 0.566 | 0.387 | 0.515 |
| WideSearch | **0.651** | 0.522 | 0.590 | 0.471 | 0.584 |
| WANDR | **0.386** | 0.130 | 0.152 | 0.057 | 0.126 |

- SaC outperforms all systems on 4/5 benchmarks; tied on HLE
- WANDR: SaC leads next-best by 2.5×
- New WANDR benchmark focuses on "wide research" tasks requiring orchestration of search, compute, and model reasoning

## Architecture

Three layers:
1. **Models** — control plane: decompose tasks, decide retrieval strategies, generate code
2. **Compute Sandboxes** — deterministic execution: secure code runtime with SDK access
3. **Agentic Search SDK** — composable primitives: retrieval, ranking, filtering, fanouts, rendering

## Connection to PTC

SaC is essentially **Programmable Tool Calling at the search layer**: instead of the model calling a fixed `search()` function, it generates code that orchestrates SDK primitives directly. This bypasses the function-calling roundtrip overhead and enables nonlinear/asynchronous control flow (fan-outs, parallel fetching, deduplication) within a single inference turn.

## Relation to Existing Agentic Search Work

- **SID-1** (Dec 2025): RL-trained retrieval model. SID-1 learns parallel tool use emergently; SaC provides the primitives explicitly via SDK
- **DCI** (May 2026): Direct corpus interaction via grep/bash. SaC generalizes this: instead of raw terminal tools, agents get purpose-built search primitives
- **Turnbull's Two-Loop Architecture**: Inner loop (agent) + outer loop (harness validation). SaC implements this at the SDK level — models control the inner loop directly
- **Cao et al. Level 3** (coding agents as retrieval interface): SaC is the next step — agents don't just use existing tools (grep), they compose custom search pipelines from primitives
