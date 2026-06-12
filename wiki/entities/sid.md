---
title: SID AI
created: 2026-05-20
updated: 2026-05-20
type: entity
tags:
  - company
  - lab
  - search
  - reinforcement-learning
  - training
  - product
  - platform
sources:
  - raw/articles/2026-05-20_turbopuffer_reinforcement-learning-sid-ai.md
  - raw/articles/2025-12-04_sid-1-agentic-retrieval.md
  - https://www.sid.ai
  - https://www.sid.ai/research/sid-1-technical-report
  - https://docs.sid.ai
---

# SID AI

SID AI is a **research lab for search** that builds agentic retrieval models trained end-to-end with reinforcement learning. Their flagship model, **SID-1**, is the first model trained specifically for agentic, closed-corpus retrieval — outperforming frontier LLMs at dramatically lower latency and cost.

**Founded by**: Max Rumpf (Co-founder), Sam Dauncey (Researcher)
**Website**: [sid.ai](https://sid.ai)
**Research**: [sid.ai/research](https://sid.ai/research)

## SID-1: Agentic Retrieval Model

SID-1 is built on **Qwen3-14B** and trained with a modified version of **GRPO** ([[concepts/post-training/grpo-rl-training]]), using large-scale synchronous RL rollouts. It treats search as a multi-turn, tool-driven process rather than a static pipeline.

### Performance

| Model | Recall | Time/Question | Cost/1k Questions |
|-------|--------|--------------|-------------------|
| **SID-1 (4x)** | **0.84** | 5.5s | $1.40 |
| GPT-5.1 (high) | 0.78 | 131s | $240 |
| **SID-1** | **0.77** | 5.5s | $0.62 |
| Gemini 3 Pro | 0.66 | 156s | $120 |
| Sonnet 4.5 | 0.64 | 35s | $540 |
| Reranker @10 | 0.45 | 0.78s | $0.61 |
| Vector only @10 | 0.44 | 0.15s | $0.0098 |

Key takeaways:
- **~2x recall** over classical retrieval pipelines (0.45 → 0.84)
- **~20x faster** than frontier LLMs (5.5s vs 131-156s)
- **Dramatically cheaper**: 374x less than Sonnet 4.5, 171x less than GPT-5.1

### Training Design

- **Algorithm**: Modified GRPO (introduced by [[entities/deepseek|DeepSeek]])
- **Per step**: 256 questions × 16 attempts = up to 4,096 rollouts
- **Corpora**: Finance, science, legal, email, general knowledge (5k abstracts to internet-scale)
- **Reward**: Document-centric (NDCG) — rewarded for finding correct documents with correct ranking and speed
- **Infrastructure**: Synchronous RL at 1k+ QPS bursts over 10M+ document corpora across >1,000 training steps
- **Search backend**: [[entities/turbopuffer]] (migrated to handle bursty reads and diverse tool indices)

### Key Technical Insights

**TI/TO Pipeline (Critical)**: Using standard OpenAI-style message abstractions in multi-turn RL leads to model collapse. The token→message→token round-trip is "lossy" (erases whitespace around tool calls), creating low-probability tokens that dominate gradients. A strict Tokens-In/Tokens-Out pipeline prevents this.

**Length Bias Solution**: "Length-debiased" GRPO can cause logit collapse when failed rollouts are longer. Fixed via Length Scheduling (short → long rollouts) + soft length penalty.

**Document-Centric Reward**: Unlike Search-R1 or SimpleQA which reward answer correctness, SID-1 is rewarded for finding correct documents (NDCG). This discourages over-reporting while preferring slight over-reporting over missed documents.

### Emergent Capabilities

Through RL training alone, SID-1 developed several capabilities naturally:

1. **Parallel tool use**: Issues 4-8 search queries in a single turn (rewarded on speed → parallelism emerges)
2. **HyDE (Hypothetical Document Embeddings)**: Drafts plausible answer documents and embeds them as search vectors — learned natively, not programmed
3. **Hierarchical retrieval**: Reads excerpts first, uses `read` tool for full content only when needed
4. **Reciprocal Rank Fusion (RRF)**: 4 parallel rollouts fused for max recall at zero additional latency
5. **Mixed BM25 strategies**: Issues both narrow and broad keyword queries simultaneously
6. **Tool preference learning**: Preferences for ANN over BM25 emerge through reinforcement; BM25 is never fully abandoned

### Production Position

SID-1 works as a **composable subagent** for larger frontier LLMs (similar to `swe-grep` in coding agents). It:
- Returns ranked document lists (not synthesized answers) — drop-in compatible with existing retrieval pipelines
- Acts as a context gatekeeper, filtering millions of documents to only the best results
- Enables frontier models with 1M-token limits to feasibly reason over millions of documents
- Separates searching from synthesis — downstream answer generation is a separate concern

## Product: SID Platform

Beyond the research model, SID AI offers a managed retrieval platform at [sid.ai](https://sid.ai):
- Takes data from various sources (servers, Google Mail, Notion, Google Drive, third-party APIs)
- Automatically extracts and structures information
- Hosts information publicly or privately
- Compatible with any AI model via query API

The platform uses multiple query engines (semantic, time-based, metadata-filtered) with a context-aware routing LLM that dynamically selects the appropriate engine per query.

## SID-2 (In Training)

SID-2 is currently in training, expected to extend SID-1's speed and recall advantages beyond the current generation of frontier LLMs. The team sees no intrinsic ceiling to achievable retrieval performance — they can scale by another 3-6 orders of magnitude with more environments, questions, and model size.

## Related Pages
- [[concepts/agentic-search]] — Full agentic search concept page (SID-1 is a core reference implementation)
- [[entities/turbopuffer]] — Search backend used for SID-1 RL training
- [[concepts/post-training/grpo-rl-training]] — GRPO algorithm
- [[raw/articles/2026-05-20_turbopuffer_reinforcement-learning-sid-ai]] — Turbopuffer blog on SID-1 RL training
- [[raw/articles/2025-12-04_sid-1-agentic-retrieval]] — Original SID-1 technical report article

## External Links
- **Website**: https://www.sid.ai
- **Research**: https://www.sid.ai/research
- **Technical Report**: https://www.sid.ai/research/sid-1-technical-report
- **Documentation**: https://docs.sid.ai
- **Waitlist**: https://sid.ai (join waitlist)
