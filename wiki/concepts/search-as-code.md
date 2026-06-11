---
title: Search as Code (SaC)
created: 2026-06-02
updated: 2026-06-02
type: concept
tags:
  - search
  - programmatic-tool-calling
  - harness-engineering
  - agent-sdk
  - sandbox
  - orchestration
  - inference
  - code-act
aliases: [SaC, programmable-search, composable-search]
related: [concepts/programmatic-tool-calling, concepts/agentic-search, concepts/codeact, concepts/agent-harness, concepts/code-mode, concepts/rlm-recursive-language-models]
sources: [raw/articles/2026-06-01_perplexity-rethinking-search-as-code-generation.md]
---

# Search as Code (SaC)

**Search as Code (SaC)** is Perplexity's reference architecture for **programmable search** — replacing monolithic search APIs with composable, atomized search primitives exposed as an SDK. Agents generate Python code to orchestrate retrieval, ranking, filtering, fanouts, and aggregation within secure sandboxes, achieving orders-of-magnitude efficiency gains over traditional query → pipeline → resultset patterns.

Announced June 1, 2026, in Perplexity Research: [Rethinking Search as Code Generation](https://research.perplexity.ai/articles/rethinking-search-as-code-generation).

## Core Architecture

SaC involves three tightly coupled layers:

| Layer | Role | Technology |
|-------|------|------------|
| **Models** | Control plane: decompose tasks, decide retrieval strategies, generate code | Frontier LLMs (GPT 5.5 tested) |
| **Compute Sandboxes** | Deterministic execution: secure code runtime with SDK access | Python execution environment |
| **Agentic Search SDK** | Composable primitives: retrieval, ranking, filtering, fanouts, rendering | Purpose-built library, not wrapped API |

```
User/Agent Request
        ↓
  Model generates Python code
        ↓
  Sandbox executes code
        │
  ┌─────┴─────┐
  │ SDK       │  ← retrieval, ranking, filtering, fanouts, rendering
  │ Primitives│  ← atomic building blocks, not monolithic endpoints
  └─────┬─────┘
        │
  Only final result → Model formats answer
```

## Why SaC? Three Failure Modes of Traditional Search

Traditional search (query → pipeline → resultset) creates three recurring failure modes for agent workflows:

1. **Coarse context** — Monolithic pipelines force suboptimal retrieval across all queries. A model needing one surgical fact gets recall-optimized results full of noise. Multiple queries against the same pipeline balloon costs and pollute context.

2. **Failure to leverage domain knowledge** — The model may know it should blend lexical and semantic signals in a particular way, prioritize certain sources, or aggregate results by a specific key. A rigid search interface prevents the model from acting on this knowledge.

3. **Inefficient control flow and context pollution** — Many search workflows need fan-out over query variants, parallel fetching, deduplication, and nonlinear/asynchronous operations. Forcing these through repeated model turns adds latency and fills context with noisy intermediate state.

SaC solves all three by giving agents **direct code-level control** over search pipeline internals.

## Connection to Programmatic Tool Calling (PTC)

SaC is essentially **PTC applied to the search layer**. Both architectures share the same pattern:

| Dimension | PTC (AWS) | SaC (Perplexity) |
|-----------|-----------|------------------|
| **Control** | LLM generates Python code | LLM generates Python code |
| **Execution** | Sandboxed environment (Docker/AgentCore) | Sandboxed environment |
| **Tool access** | Arbitrary external tools via IPC | Search primitives via SDK |
| **Intermediate data** | Never enters context | Never enters context |
| **Token reduction** | 87-92% | 85.1% (CVE task) |
| **Parallelism** | `asyncio.gather()` | Concurrent SDK calls |
| **Result** | Only `print()` output returns to LLM | Filtered results enter context |

The key difference: PTC is a **general-purpose** pattern (any tool), while SaC provides a **domain-specific** SDK optimized for search operations. SaC's SDK exposes retrieval, ranking, filtering, fanouts, and rendering as atomic primitives — whereas PTC intercepts arbitrary tool calls via a generic IPC protocol.

## Connection to Agentic Search

SaC represents an evolution of the harness patterns documented in [[concepts/agentic-search]]:

| Agentic Search Stage | What the Agent Controls | SaC's Position |
|---------------------|------------------------|----------------|
| **Level 0** — Keyword search | User types query | Pre-SaC baseline |
| **Level 1** — LLM query understanding | Agent rewrites query | Still monolithic pipeline |
| **Level 2** — Tool calling | Agent picks tools sequentially | Function calling / MCP |
| **Level 3** — Harness loops | Agent retries, validates (Ralph loop) | Turnbull's steering patterns |
| **Level 4** — DCI (Direct Corpus Interaction) | Agent uses grep/bash on filesystem | Cao et al.'s coding agents |
| **Level 5** — **Search as Code** | **Agent composes search primitives in code** | **SaC** |

SaC generalizes DCI (which is limited to local filesystem operations) to the full search stack, while preserving the code-level control that makes DCI effective.

## Agentic Search SDK Design Decisions

### Why Python Runtime?
Perplexity evaluated Python, Rust, TypeScript, and Bash. Python won because:
- Ubiquity in the data processing ecosystem
- Natural fit for async/parallel orchestration (`asyncio`)
- Agents are already trained on Python (CodeAct pattern)
- Rich ecosystem of filtering, deduplication, and aggregation libraries

### SDK as Primitives, Not Wrapped APIs
Unlike traditional search SDKs that package REST endpoints as library calls, Perplexity's Agentic Search SDK exposes individual building blocks:
- `sdk.search.web_many()` — parallel search with concurrency control
- `sdk.llm.extract_many()` — structured extraction from results
- Individual retrieval, ranking, filtering, and rendering primitives

High-level search pipelines still exist but serve as **shorthand** for common patterns — agents can bypass them and compose primitives directly.

### Autoresearch-Driven SDK Optimization
Perplexity runs a continuous autoresearch loop over the SDK:
- Proposes SDK improvements (structure, aesthetics, naming)
- Validates against metrics: latency, codegen quality, task performance
- Has already made numerous changes with significant gains across all dimensions

### Agent Skills for SDK Consumability
Since custom SDKs aren't in pretraining data, Perplexity develops optimized Agent Skills (under 2000 tokens) that teach models to:
- List available SDK building blocks (via runtime reflection)
- Compose primitives into complex patterns
- Use few-shot examples for orchestration strategies

### Intermediate State Management: Filesystem vs REPL
SaC tested two approaches for persisting state across turns:

| Approach | Pros | Cons | Verdict |
|----------|------|------|---------|
| **Filesystem + serde** | Explicit, traceable, reliable on long trajectories | Latency overhead from serialization code | **Selected** |
| **REPL** | Token-efficient, no serde code needed | Cluttered namespace, hard to track state | Rejected |

Perplexity found filesystem-based serde provides better reliability on long trajectories, conjecturing that requiring models to convey state declaratively helps them manage it more effectively.

## Code Generation as Gap Filler

Beyond orchestration, code serves as a **gap-filler** for capabilities not present in the SDK:

> *Instead of bloating the SDK with niche subroutines (e.g., complex regex patterns), agents generate custom code to collect a superset of results, deduplicate via SDK, then apply their own filtering logic deterministically.*

This is a key design principle: the SDK provides fundamental primitives, agents build task-specific components on the fly.

## Case Study: CVE Vendor Advisories

A real-world task from Perplexity's testing suite: identify and characterize 200+ high-severity CVEs from 2023-2025, citing official vendor advisories with product and fix version.

| Metric | Non-SaC Baseline | SaC | Improvement |
|--------|-----------------|-----|-------------|
| Accuracy | <25% | **100%** | 4x+ |
| Token usage | 288.7K | **42.9K** | 85.1% reduction |

The SaC agent generated code that:
1. Faned out over vendor-specific advisory formats with parallel SDK calls
2. Used an LLM as intermediate planning to identify coverage gaps
3. Synthesized refinements for sparse vendor-year pairs
4. Verified CVE-to-version binding via structured extraction

## Benchmark Results

| Benchmark | Perplexity (SaC) | OpenAI Responses | Anthropic Managed | Exa Agent | Parallel Tasks |
|-----------|-----------------|-----------------|-------------------|-----------|---------------|
| DSQA | **0.871** | 0.733 | 0.815 | 0.530 | 0.810 |
| BrowseComp | **0.805** | 0.720 | 0.598 | 0.380 | 0.560 |
| HLE | 0.612 | **0.614** | 0.566 | 0.387 | 0.515 |
| WideSearch | **0.651** | 0.522 | 0.590 | 0.471 | 0.584 |
| WANDR | **0.386** | 0.130 | 0.152 | 0.057 | 0.126 |

**SaC outperforms all systems on 4/5 benchmarks; tied on HLE.** WANDR is a new "wide research" benchmark emphasizing complex orchestration — SaC leads the next-best system by 2.5x.

## Cost-Performance Frontier

On DSQA:
- **Low reasoning**: Cheaper than all other systems, outperforms two of them
- **Medium reasoning**: Best performance at under $1 per task
- **High reasoning**: Top performance with competitive cost

On WideSearch: similarly shaped frontier — low reasoning achieves competitive performance at lower cost, medium and high outperform all non-SaC systems.

## Toward a New Architecture of Computing

Perplexity positions SaC as evidence of a broader architectural shift:

> *Search is a natural proving ground for hybrid compute: models decide what evidence is needed and how uncertainty should be resolved. Deterministic runtimes handle batching, parallelism, filtering, ranking, and aggregation. Search infrastructure serves as universal I/O.*

The future direction Perplexity envisions:
1. **SDK + Skills co-optimization** via shared autoresearch loops
2. **Models trained to leverage search primitives** directly (not just code generation)
3. **Coevolving SDK design during model training** — SDKs as part of the model's inductive bias

## Open Questions

- **Generalization**: Can SaC's SDK-first approach work for non-search domains (code execution, data analysis, API orchestration)?
- **Security**: What are the failure modes when agents generate code with unrestricted SDK access?
- **Cost of sandboxes**: While token costs drop dramatically, sandbox compute costs become the new bottleneck
- **SDK fragmentation**: If every provider builds their own Agentic Search SDK, do agents need per-provider Skills, or will a standard emerge?
- **Autoresearch dependency**: SaC's SDK improvements come from continuous autoresearch — is this sustainable without massive compute investment?

## Related Concepts

- [[concepts/programmatic-tool-calling]] — General pattern of code-orchestrated tool calls (PTC is SaC's cousin)
- [[concepts/agentic-search]] — Broader agentic search landscape that SaC advances
- [[concepts/coding-agents/codeact]] — Code-as-action pattern that SaC builds upon
- [[concepts/code-mode]] — Model code generation as primary interaction mode
- [[concepts/harness-engineering/agent-harness]] — SaC implements harness patterns at the SDK level
- [[concepts/rlm-recursive-language-models]] — Context-as-variable pattern that SaC's sandbox state management addresses
- [[concepts/harness-engineering/agent-vs-pipeline-architecture]] — SaC is an agent pattern that recovers pipeline-like efficiency through code orchestration

## Sources

- [Rethinking Search as Code Generation](https://research.perplexity.ai/articles/rethinking-search-as-code-generation) — Perplexity Research (June 1, 2026)
- [Programmatic Tool Calling on AWS Bedrock](raw/articles/2026-05-19_aws_ptc-bedrock-agentcore.md) — AWS ML Blog (May 2026)
- [SID-1 Technical Report: Test-Time Compute for Retrieval](https://www.sid.ai/research/sid-1-technical-report) — SID Research (December 2025)
- [Cao et al. — Coding Agents as Retrieval Interface](https://arxiv.org/abs/2603.20432) — Microsoft Research (March 2026)
- [Beyond Semantic Similarity: Direct Corpus Interaction](https://arxiv.org/abs/2605.05242) — Li, Zhang, Wei, Lu, Nie et al. (May 2026)
