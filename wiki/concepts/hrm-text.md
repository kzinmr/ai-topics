---
title: HRM-Text
created: 2026-05-19
updated: 2026-05-19
type: concept
tags: [concept, reasoning, non-transformer, hierarchical, recurrent, latent-space, open-source, edge-ai, training-efficiency, neurosymbolic]
sources: [raw/articles/2026-05-18_sapient-intelligence-hrm-text.md, https://www.prnewswire.com/news-releases/sapient-intelligence-launches-hrm-text-challenging-the-llm-monopoly-with-a-brain-inspired-foundation-model-trained-on-up-to-1000x-fewer-tokens-302774638.html]
---

# HRM-Text

**HRM-Text** (Hierarchical Reasoning Model for Text) is a 1B-parameter open-source reasoning language model by [[entities/sapient-intelligence]], released May 18, 2026. It challenges the Transformer monopoly with a brain-inspired hierarchical architecture that achieves competitive reasoning performance using **~1000× fewer training tokens** than standard LLMs.

## Architecture Innovation

Unlike Transformers that do a single forward pass per token, HRM-Text runs **two stacks in a nested recurrence** in continuous latent space before any output token is generated:

- **8 internal recurrent steps** per forward pass: 2 high-level + 6 low-level updates
- **Multi-timescale reasoning**: Different levels of the hierarchy handle different temporal scales of reasoning
- **Latent-space reasoning**: Reasoning happens in continuous latent space — adjusts computation depth to task complexity without generating long visible reasoning chains
- **Separates reasoning from language generation**: Mirrors the brain's natural approach

> "Instead of one stack doing a single forward pass (the standard Transformer approach), HRM-Text runs two stacks in a nested recurrence in a continuous latent space, before any output is produced." — Sapient Intelligence

## Training Efficiency

| Metric | HRM-Text | Typical LLM | Ratio |
|--------|----------|-------------|-------|
| Parameters | 1B | 7B–405B | — |
| Training tokens | ~40B | 4T–36T | 100–900× less |
| Training cost | ~$1,000 | $10M–$100M+ | 10,000×+ less |
| Training time | ~1 day (16 GPUs) | Weeks–months | — |
| Deployment size (int4) | ~0.6 GiB | 4–200+ GiB | Fits on smartphone |

Training approach: **task-completion** rather than next-token prediction, using structured tasks in mathematics, logic, and general knowledge.

## Performance

| Benchmark | HRM-Text | Notes |
|-----------|----------|-------|
| MATH | 56.2% | Multi-step mathematical reasoning |
| ARC-Challenge | 81.9% | Science reasoning and commonsense |
| DROP | 82.2% | Numerical reasoning over text |
| MMLU | 60.7% | Broad general knowledge |

For a 1B model trained on $1,000, these scores are remarkable — competitive with much larger models on reasoning benchmarks.

## Prior Work

In June 2025, Sapient's original HRM (predecessor) outperformed DeepSeek R1 and OpenAI o3 on ARC-AGI Challenge despite "tens of thousands of times fewer parameters."

## Implications

HRM-Text demonstrates that **the scaling hypothesis is not the only path to reasoning**. A fundamentally different architecture can achieve competitive results with radically less compute. If this approach scales, it could democratize AI training — bringing model development costs from hundreds of millions to thousands of dollars.

## Related

- [[entities/sapient-intelligence]] — Company behind HRM-Text
- [[concepts/reasoning]] — Broader reasoning in LLMs
- [[concepts/neurosymbolic]] — Neurosymbolic approaches
- [[concepts/training-efficiency]] — Efficient training methods
- [[concepts/scaling]] — Scaling laws and their limitations
