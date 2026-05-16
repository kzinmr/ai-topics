---
title: Elastic Training (Once-For-All)
created: 2026-05-16
updated: 2026-05-16
type: concept
tags: [training, optimization, model, mixture-of-experts, distillation]
sources: [raw/articles/the-decoder.com--baidu-ernie-5-1-94-percent-cost-reduction--2026-05-16.md]
---

# Elastic Training (Once-For-All)

**Elastic training** refers to frameworks that optimize an entire family of differently-sized models in a single training run, rather than running separate pre-training passes for each model size. The key insight: amortize the heavy compute across a "super-model" and extract smaller sub-models at near-zero marginal training cost.

## Baidu's Once-For-All Framework

Baidu introduced this approach with the Ernie 5.x family, calling it the **"Once-For-All elastic training framework."** The framework simultaneously varies three dimensions:

1. **Elastic Depth**: Number of active transformer layers
2. **Elastic Width**: Number of expert blocks available
3. **Elastic Sparsity**: How many experts activate per query (Top-K routing)

The models share weights across the family but differ in which subset activates for a given query. Baidu selected what it considered the optimal configuration from this family for Ernie 5.1.

### Results
- Ernie 5.1 pre-training cost: **6%** of comparable models (94% reduction)
- ~1/3 the total parameters of Ernie 5.0
- ~1/2 active parameters per query
- 4th place on Search Arena Leaderboard

## Relationship to Other Techniques

| Technique | What It Optimizes | When |
|-----------|------------------|------|
| **Elastic training** | Multi-model family in one run | Pre-training |
| **Distillation** | Smaller model from larger teacher | Post-training |
| **Pruning** | Remove redundant weights | Post-training |
| **Quantization** | Reduce weight precision | Post-training |
| **MoE routing** | Per-token expert activation | Inference |

Elastic training is complementary to all of these — it produces the base model family that can then be distilled, pruned, or quantized.

## Industry Significance

If elastic training becomes widely adopted, it could reshape the economics of model development:
- Labs could ship entire model families (tiny to large) from a single training run
- Pre-training costs could drop by an order of magnitude for smaller variants
- The "train once, extract many" paradigm could become standard

## See Also

- [[entities/baidu]]
- [[concepts/mixture-of-experts]]
- [[concepts/training]]
- [[concepts/distillation]]
- [[concepts/optimization]]
