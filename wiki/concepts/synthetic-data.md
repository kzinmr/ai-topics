---
title: "synthetic-data"
type: concept
aliases:
  - synthetic-data
  - synthetic-data-augmentation
  - synthetic-pretraining-data
created: 2026-04-25
updated: 2026-05-03
tags:
  - concept
  - pretraining
  - data-engineering
  - scaling
related:
  - [[concepts/autodata-agentic-data-creation]]
  - [[concepts/llm-training-coherence-evolution]]
sources:
  - raw/articles/2026-03-19_megadocs-synthetic-pretraining.md
  - https://arxiv.org/abs/2603.18534
---

# synthetic-data

Synthetic data refers to artificially generated training examples created by AI models (typically LLMs) rather than collected from real-world sources. In the context of LLM pre-training, synthetic data augmentation has emerged as a critical solution to the **"data wall"** — where compute availability outpaces the supply of high-quality web data.

## Key Approaches

### Synthetic Rephrasing (Baseline)

The simplest approach: generate multiple synthetic versions of existing web documents using an LLM. Despite coming from a different distribution than real data, synthetic rephrases improve validation loss on real web data — a surprising finding confirming that diversity of expression aids generalization.

**Efficiency gain:** ~1.48× (at 32 rephrases per document)

### Megadocs (Structured Long-Form Synthetic Data)

Proposed by Kim et al. (2026, arXiv:2603.18534), **Megadocs** transform short synthetic rephrases into long, structured documents via two techniques:

| Technique | Method | Purpose |
|-----------|--------|---------|
| **Stitching** | Concatenate multiple synthetic rephrases of the same original into one long document | Expose model to long-range dependencies |
| **Stretching** | Insert rationales / additional context into a document | Increase depth and semantic richness |

**Efficiency gain:** ~1.80× (at 32 synthetic generations per original)

**Key finding:** The performance gap between Megadocs and simple rephrasing **widens** as synthetic data volume increases, suggesting better compute-loss scaling behavior. Megadocs specifically improve **long-context loss**, which simple rephrasing fails to address.

### Agentic Data Creation

A more advanced paradigm where AI agents actively curate, verify, and generate training data through multi-step processes. See [[concepts/autodata-agentic-data-creation]] for the full framework.

## Pre-training Best Practices

- **Optimal Mixing:** The ratio of real to synthetic data must be carefully tuned; poor mixing can cause divergence
- **Epoching Strategy:** With optimal epoching, more synthetic generations improve accuracy without overfitting
- **Scaling Strategy:** When data-constrained, structure synthetic data into longer formats (Megadocs) rather than generating more short samples

## Distributional Shift Paradox

A counterintuitive finding: synthetic data helps improve validation loss on **real** web data, even though it follows a different distribution. The diversity of synthetic expressions appears to teach models more robust representations than repeated exposure to the same real documents.

## Related Concepts

- [[concepts/autodata-agentic-data-creation]] — Agent-driven data curation and generation
- [[concepts/llm-training-coherence-evolution]] — How training data quality affects model behavior
- [[concepts/harness-engineering]] — Broader context: data as part of the agent infrastructure stack

## Sources

- Kim, Kotha, Choi, Hashimoto, Haber, Liang. "Data-efficient pre-training by scaling synthetic megadocs" (arXiv:2603.18534, March 2026)
- [raw/articles/2026-03-19_megadocs-synthetic-pretraining.md](raw/articles/2026-03-19_megadocs-synthetic-pretraining.md)
