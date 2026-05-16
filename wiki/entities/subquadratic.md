---
title: Subquadratic (SubQ)
created: 2026-05-16
updated: 2026-05-16
type: entity
tags: [company, model, long-context, inference, ai]
sources: [raw/articles/whatllm.org--new-ai-models-may-2026-subq-subquadratic--2026-05-16.md]
---

# Subquadratic (SubQ)

**Subquadratic** is an AI company that launched **SubQ 1M-Preview** in May 2026 — the first commercially available LLM built on subquadratic attention rather than standard transformer attention. The company raised $29M in seed funding.

## Key Facts

- **Founded**: ~2025-2026
- **Funding**: $29M seed (May 2026)
- **First model**: SubQ 1M-Preview (May 5, 2026)
- **Key innovation**: End-to-end subquadratic sparse attention

## SubQ 1M-Preview

- **Architecture**: Sparse, subquadratic attention — not a standard transformer. Standard transformer attention is O(n²) in context length; SubQ's approach avoids this quadratic cost ceiling.
- **Context window**: Native 12 million tokens — designed for repo-wide code analysis, long document processing, and multi-document research.
- **Cost claims**: ~1/5 the cost of frontier models on long-context workloads (vendor figure)
- **Speed claims**: Up to 52x faster attention at scale (vendor figure, awaiting independent verification)
- **Products**: API access + SubQ Code (repo-wide coding agent leveraging the full context)

## Significance

SubQ represents the first commercial attempt to break the O(n²) attention ceiling at production scale. Previous subquadratic approaches — Mamba, RWKV, Hyena, BASED — showed promise in research but plateaued when pushed to frontier scale. Whether SubQ can succeed where others plateaued remains unverified; no third-party benchmarks (MRCR, RULER) have been published yet.

## See Also

- [[concepts/subquadratic-attention]]
- [[concepts/long-context]]
- [[concepts/transformer-architecture]]
- [[concepts/mixture-of-experts]]
