---
title: "Slow Search"
type: concept
created: 2026-06-15
updated: 2026-06-15
tags:
  - concept
  - search
  - agentic-retrieval
  - performance-engineering
aliases:
  - slow-search
  - Slow Search
  - searching fast and slow
related:
  - entities/josh-barrow
  - concepts/agentic-retrieval
  - concepts/hornet
  - concepts/deep-research
sources:
  - https://jbarrow.ai/2026-06-12-searching-fast-and-slow/
  - https://jbarrow.ai/field_notes/obliq-bench/
  - raw/articles/2026-06-12_jbarrow_searching-fast-and-slow.md
---

# Slow Search

**Slow Search** is the paradigm of deliberately trading per-query latency for higher retrieval quality, predicated on the insight that search consumers may not care about immediate response times if the results are significantly better. Originally proposed for human searchers in 2013 (Teevan et al.), the concept has found renewed relevance in the age of **agentic retrieval**, where AI agents are infinitely patient and can use slower, higher-quality search to reduce overall task completion time.

## The Original Slow Search Paper (2013)

Teevan, Collins-Thompson, White, Dumais, and Kim published ["Slow Search: Information Retrieval without Time Constraints"](https://www.microsoft.com/en-us/research/publication/slow-search-information-retrieval-without-time-constraints/) at the Symposium on Human-Computer Interaction and Information Retrieval. The paper posed two questions:

1. What would search look like if we didn't care about latency?
2. Under what circumstances would users accept waiting longer for better results?

**Key finding**: Only 25.5% of participants could imagine waiting for the best possible results longer than they actively searched. 61% had difficulty envisioning a search engine that would sacrifice speed for quality. This finding drove decades of relentless focus on search latency in the IR community.

Notably, the paper proposed **search agents** as an example of slow search — answering queries "in the background as [searchers] engage in other tasks, search-related or otherwise." This was prescient by 12 years.

## Slow Search in the Agentic Era

Josh Barrow (@jbarrowai) revisited Slow Search in June 2026, identifying **two competing philosophies** for agentic retrieval:

| Philosophy | Claim | Validity |
|-----------|-------|----------|
| **Latency doesn't matter** | User is already willing to wait; models don't care about latency | ✅ Correct for per-query latency |
| **Agents are more sensitive to latency** | Agents issue far more queries than humans | ✅ Correct for throughput and "whole task time" |

The resolution: **both are right at different granularities**. Per-query, agents can wait. At scale, latency compounds into throughput and cost.

## Why Slower Search Can Actually Be Faster

The counterintuitive insight: **better retrieval can reduce total task time**. Evidence:

- **Reason-ModernColBERT** (Antoine Chaffin, LightOn AI): Better retrieval is a rising tide that lifts all model sizes. On BrowseComp-Plus, improved retrieval directly helps all agents regardless of model size.
- **Direct Corpus Interaction (DCI)** paper (Li et al., 2026): Giving agents direct access to grep/bash yielded similar performance increases but with **more than double the tool calls and double the cost**.

For agentic retrieval, time and cost are primarily driven by the LLM itself — every tool call means paying cached input cost and waiting for generation time. So **lower-latency search can paradoxically increase total wait time** if it produces poorer results that trigger more agent iterations.

## The Pareto Frontier of Retrieval Quality

There exists a tradeoff curve between retrieval quality and compute/time:

```
High Quality ──────────────────────────
                  ↗
                ↗
              ↗
            ↗  (LLM reranker, multivector)
          ↗
        ↗  (ColBERT, late-interaction)
      ↗
    ↗  (BM25, inverted index)
  ↗
Low Quality ──────────────────────────
  Fast                    Slow →
```

Moving up and right requires:
- Better models (larger, more capable)
- More complex infrastructure (multivector, two-stage retrieval, LLM reranking)
- More engineering effort

## Obliq-Bench

Josh Barrow created [Obliq-Bench](https://jbarrow.ai/field_notes/obliq-bench/), a benchmark designed to evaluate oblique/indirect query resolution — the kind of search that agents perform when working through multi-step reasoning problems. This represents a concrete research direction for slow search in the agentic era.

## Research Opportunity

Barrow argues the IR community should do **more slow search research**:

> "Agents are the perfect slow searchers; they're infinitely patient, and cheaper/better to run if you can give them better results. So we as a research community should be thinking about how to satisfy this new customer. Try some out-there but slow ideas!"

This connects directly to Ben Clavie's call for an **"LLM moment" in IR** — tolerance for early-stage research that lacks production infrastructure but points toward transformative directions.

## Connection to Hornet

[Hornet](hornet.md) is betting that retrieval engines for agents should focus on **throughput rather than latency**. The core thesis: "agents issue more queries than humans and aren't as latency sensitive." This is the practical implementation of slow search principles.

## Key Sources

- Teevan et al. (2013). "Slow Search: Information Retrieval without Time Constraints." Proc. Symposium on HCI and IR.
- Josh Barrow (2026). "Searching, Fast and Slow." https://jbarrow.ai/2026-06-12-searching-fast-and-slow/
- Josh Barrow (2026). Obliq-Bench. https://jbarrow.ai/field_notes/obliq-bench/
- Chaffin (2025). Reason-ModernColBERT. https://huggingface.co/lightonai/Reason-ModernColBERT
- Li et al. (2026). "Beyond semantic similarity: Rethinking retrieval for agentic search via direct corpus interaction." arXiv:2605.05242.
