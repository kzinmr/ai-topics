---
title: "Time-Incremental Continued Pretraining — Refreshing Knowledge Without Forgetting"
created: 2026-09-23
updated: 2026-09-23
type: concept
tags: [continual-learning, training, datasets, llm, model-merging, arxiv]
sources:
  - raw/articles/2026-09-23_arxiv_2609.23916_time-incremental-continued-pretraining.md
related:
  - "[[concepts/continual-learning]]"
  - "[[concepts/post-training/on-policy-distillation]]"
  - "[[concepts/sleep-time-compute]]"
---

# Time-Incremental Continued Pretraining — Refreshing Knowledge Without Forgetting

## Definition

**Time-incremental continued pretraining (CPT)** is refreshing a model's knowledge by
continuing to pretrain it on fresh web data drawn strictly from *after* its knowledge cutoff,
rather than retraining from scratch. Öncel, Ali, Ravanelli, Subakan, Yıldız (arXiv:2609.23916,
Sep 2026) argue this regime has been mis-framed: the continual-learning literature assumes
*disjoint* data streams, but real web crawls (FineWeb-Edu snapshots) share heavy URL overlap by
design, which changes the picture entirely.

## Key Findings (four practical questions)

Evaluated on FineWeb-Edu dumps across six open-weight models (OLMo2, Llama-3.1/3.2, Gemma-3-1B)
and four scales (1B–3B–7B–8B):

- **Knowledge is acquired without catastrophic forgetting.** 5 of 6 models *improved* even on
  pre-cutoff factual recall. Gains track pretraining saturation — driven primarily by **token
  budget per parameter**.
- **Cost is near-zero.** The macro-average across a 13-task suite stays within **0.01** of the
  base model for every model.
- **Recipe: quality > quantity.** A curated 6B-token slice matched a broader 40B one. The
  learning-rate optima for *knowledge acquisition* vs. *general capability preservation* are
  separated by ~an order of magnitude, and **LoRA at sufficient rank matches full CPT**.
- **It survives deployment.** CPT gains transfer through SFT; DPO's effect is family-dependent.

## Why It Matters

This directly softens the pessimism of the classic [[concepts/continual-learning|continual
learning]] literature (catastrophic-forgetting dread). The overlap between successive crawl
snapshots — usually treated as a contamination nuisance — turns out to be a *feature*: it acts
as natural replay, so time-incremental updates refresh facts almost for free. This makes
periodic knowledge refresh via CPT (or LoRA CPT) a realistic maintenance loop, adjacent to the
on-policy distillation strategies used to consolidate capability across domains.

## Relationship to Other Ideas

It is a *model-layer* freshness mechanism, contrasted with the *inference-layer*
[[concepts/sleep-time-compute|sleep-time compute]] and the *context-layer* retrieval/RAG
approaches. Where those work around a frozen model, time-incremental CPT updates the weights
themselves. The "learning-rate separation" result is a caution for anyone running
[[concepts/continual-learning|continual-learning]] pipelines: the LR that best injects new
facts is far higher than the LR that preserves existing capability.

## Open Questions

- Does the URL-overlap-as-replay effect hold at frontier scale (the study caps at 8B)?
- Is the "curated 6B ≈ broad 40B" result a data-quality finding or a compute-budget artifact?
- How often should a deployed model run a CPT refresh before drift between refreshes matters?

## Sources

- Time-Incremental Continued Pretraining of LLMs: Knowledge Updates Without Catastrophic Forgetting — arXiv:2609.23916 (2026-09-20), Öncel, Ali, Ravanelli, Subakan, Yıldız
