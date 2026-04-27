---
title: "Draft & Verify: Lossless Large Language Model Acceleration via Self-Speculative Decoding"
url: "https://arxiv.org/abs/2309.08168"
source: "arxiv"
authors: ["Jun Zhang", "Jue Wang", "Huan Li", "Lidan Shou", "Ke Chen", "Gang Chen", "Sharad Mehrotra"]
published: "2023-09-15"
crawled: "2026-04-18"
type: "paper_summary"
tags: [inference, optimization, speculative-decoding, self-speculative]
---

# Draft & Verify: Self-Speculative Decoding (Zhang et al., ACL 2024)

## Core Innovation
Self-speculative decoding eliminates the need for a separate draft/auxiliary model by leveraging the target LLM itself for drafting through selective layer skipping.

## Two-Stage Pipeline
1. **Drafting:** Skip certain intermediate layers of the main LLM to generate tokens rapidly
2. **Verification:** Run full LLM on drafted tokens in a single forward pass to validate/correct

## Key Properties
- Zero auxiliary models needed
- No additional training or fine-tuning required
- Zero extra memory footprint during inference
- 100% output equivalence to standard autoregressive decoding
- Up to 1.99× speedup on LLaMA-2

## Architecture Details
- Uses LLaMA-2 and variants
- Draft phase: skip intermediate layers (fast, slightly lower quality)
- Verification phase: full model forward pass (exact match guarantee)
- Maintains mathematical equivalence while reducing compute

## Deployment Implications
- Immediately deployable for production LLM inference
- No retraining needed — just modify forward pass
- Dramatically reduces compute latency without quality degradation
