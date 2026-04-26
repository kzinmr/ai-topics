---
title: "Speculative Decoding"
created: 2026-04-18
updated: 2026-04-18
type: concept
tags: [inference, optimization, technique, architecture]
sources: [raw/articles/crawl-2026-04-18-speculative-decoding.md]
---

# Speculative Decoding

A technique to accelerate LLM inference by using a smaller "draft" model to generate candidate tokens, which are then verified in parallel by a larger "target" model. Reduces per-token latency by 2-4x for output-heavy workloads.

## How It Works

1. **Draft phase:** Small draft model generates multiple tokens sequentially (fast, low cost)
2. **Verification phase:** Target model evaluates all draft tokens in parallel using forward passes
3. **Accept/reject:** Target model accepts matching tokens, rewrites rejected ones
4. **Repeat:** Continue until end of sequence

### Key Insight

The target model can verify multiple draft tokens in a single forward pass (same computation cost as verifying one token). This creates a throughput multiplier: if the average acceptance rate is α, the speedup ≈ 1 / (1 - α).

## Two Main Approaches

### Draft-and-Verify (Traditional)
- Requires a separate smaller model (e.g., 7B draft + 70B target)
- Draft model must be trained/finetuned for the same domain
- Best acceptance rates when draft model is well-aligned with target

### Self-Speculative Decoding
- Uses early layers of the *same* model as the draft
- No additional model training needed
- Example: Llama-3 8B's first 4 layers can draft for the full 8B model
- More practical for most deployments

## Performance Characteristics

| Scenario | Speedup | Acceptance Rate | Best For |
|----------|---------|-----------------|----------|
| Well-matched draft | 2-4x | 70-90% | Code generation, creative writing |
| Self-speculative | 1.5-2.5x | 50-70% | General purpose, no extra model needed |
| Poor draft match | 1.1-1.3x | 20-40% | Specialized domains, domain mismatch |

## Token Economics Connection

Speculative decoding directly impacts [[token-economics]]:
- **Cost reduction:** 2-4x throughput = 50-75% fewer GPU hours per output
- **Latency improvement:** Critical for interactive applications (chat, coding assistants)
- **Memory efficiency:** No additional GPU memory needed beyond draft model

## Implementation Requirements

- **vLLM support:** Built-in speculative decoding since v0.4
- **TGI support:** Text Generation Inference supports it natively
- **Custom implementations:** Require careful tuning of draft token count and acceptance thresholds
- **Hardware considerations:** Works best on GPUs with high memory bandwidth (H100, A100)

## Limitations

- **Overhead:** If acceptance rate is too low, the draft generation overhead outweighs benefits
- **Non-determinism:** Results vary based on draft model quality and token count
- **Domain sensitivity:** Works best when draft and target models share training data distribution
- **Streaming incompatibility:** Harder to implement with streaming outputs (must wait for full draft sequence)

## Related

- [[token-economics]] — Throughput optimization and cost reduction
- [[attention-mechanism-variants]] — Different attention mechanisms affect speculative decoding performance
- [[local-llm/model-quantization]] — Quantization can be combined with speculative decoding
- [[local-llm]] — Inference optimization techniques

## Sources

-  — vLLM and speculative decoding analysis
- Sebastian Raschka, "A Visual Guide to Attention Mechanisms" (Ahead of AI, 2026)
