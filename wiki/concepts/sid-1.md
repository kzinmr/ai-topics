---
title: SID-1
type: concept
aliases: [SID-1 model, sid-1-retrieval]
created: 2026-05-13
updated: 2026-05-13
status: L2
sources: [https://www.sid.ai/research/sid-1, https://www.sid.ai/research/sid-1-technical-report, https://x.com/maxrumpf, https://ycombinator.com/companies/sid]
tags:
  - model
  - search
  - reinforcement-learning
  - training
  - rag
  - agentic-engineering
  - ai-agents

---

# SID-1

SID-1 is the first model end-to-end reinforcement-learned (RL) for **agentic retrieval**, announced by SID.ai in December 2025. It discards the conventional fixed pipeline of embedding → retrieval → re-ranking, adopting an agentic approach that iteratively "searches → reads → refines queries" like a human.

## Overview

| Item | Detail |
|------|------|
| Release Date | December 4, 2025 |
| Developer | SID.ai (CEO: [[entities/max-rumpf|Max Rumpf]]) |
| Training Method | Modified [[grpo|GRPO]] by Magistral, no SFT (cold-start RL) |
| Availability | API, AWS Bedrock, self-hosted |
| Compute Resources | Provided by NVIDIA |

## Architecture

### Agentic Retrieval
Traditional search pipelines pre-define each step:
1. Query rewriting
2. Search (vector / BM25)
3. Re-ranking (cross-encoder)

SID-1 performs all of these iteratively as a single model. It takes additional search steps as needed, adaptively adjusting compute based on difficulty.

### Training Method
- **GRPO (Magistral modified)**: Cold-start RL without an SFT phase
- **Multi-turn, multi-environment RL**: Optimizes interactive search across multiple environments via RL
- **Synthetic data generation**: Trained on difficult problems that would take human researchers an hour or more
- **Reward Design**: Rule-based reward + search accuracy-based

**Practical Challenges** (from Max Rumpf's X posts):
> "Using OpenAI-style messages for env interaction generates slightly different tokens during parsing and re-tokenization. Debugging this problem wasted more H100 hours than any other challenge."

## Performance

Evaluated across diverse retrieval benchmarks (general knowledge, finance, science, law, email).

| Model | Recall | Time | Cost/Question |
|--------|--------|----------|------------|
| **SID-1 (4x)** | **0.84** | 5.5s | $0.0014 |
| SID-1 (1x) | 0.77 | 5.5s | $0.00062 |
| GPT-5.1 (high) | 0.78 | 131s | $0.24 |
| GPT-5.1 (auto) | — | 38.5s (estimated 7x SID-1) | — |
| Gemini 3 Pro | 0.66 | 156s | $0.12 |
| Sonnet 4.5 | 0.64 | 35s | $0.54 |
| Reranker @10 | 0.45 | 0.78s | $0.00061 |
| Vector only @10 | 0.44 | 0.15s | $0.0000098 |

### Cost Efficiency
- **3-4 orders of magnitude cheaper** than GPT-5.1 ($0.24 → $0.0014)
- **24x faster** than GPT-5.1 (131s → 5.5s)
- **1.87x recall** vs. traditional re-ranking pipeline (0.45 → 0.84)
- **1.91x recall** vs. embedding-only search (0.44 → 0.84)

### Adaptive Compute
Low-difficulty questions are answered with fewer steps and fewer tokens, automatically saving latency and cost.

## Integration

- **Drop-in compatible**: Replaces existing embedding-only / RAG search systems. Typically integrates in "half an afternoon."
- **Sub-agent operation**: Designed as a sub-agent for frontier models like GPT-5 and Sonnet.
- **Tool usage**: Multi-step process of calling search, reading results, and refining queries.

## Strategic Significance

SID.ai cites historical patterns where step-change improvements in search created new winners:

> "Claude Code was better at finding the right file, unlocking larger code bases and driving massive adoption for Anthropic. Open Evidence made retrieving over medical research easier and took doctors by storm. Relational was better than hierarchical for databases, creating Oracle. Better web search created Google."

Positioning SID-1 in this lineage and bringing it to market as a "step-change in search."

## Key Contributions of the Technical Report

1. **Demonstration of RL training for agentic search**: The first end-to-end RL for retrieval
2. **Practical GRPO challenges**: Issues with common GRPO formulations, tokenization instability, multi-turn RL infrastructure problems
3. **Feasibility of SFT-free training**: Demonstrates a training path without human cold-start data
4. **Reward Design**: Design principles for reward functions that directly optimize search accuracy

## Limitations & Future Directions

- Specialized for closed corpus retrieval
- Currently compute-constrained, rolling out gradually
- Hiring research interns for Summer 2026

## Related Pages

- [[entities/max-rumpf]] — SID.ai CEO / SID-1 developer
- [[grpo]] — Group Relative Policy Optimization, the training algorithm
- [[concepts/agentic-retrieval]] — Agentic information retrieval paradigm
- [[rag]] — Retrieval-Augmented Generation, the conventional approach SID-1 aims to replace
- [[magistral]] — Developer of the modified GRPO
- [[concepts/test-time-compute]] — Test-time compute optimization
- [[search-r1]] — Similar approach (RL for agentic search)
