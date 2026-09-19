---
title: "Edge AI Strategy — Quantize-Big vs Build-Tiny"
description: The two competing routes to on-device LLMs in 2026: compress frontier-scale models via extreme quantization (Prism ML / Bonsai) versus build natively tiny agentic models (Cactus Compute / Needle 2). Shared principle, divergent bets.
type: concept
created: 2026-09-19
updated: 2026-09-19
aliases:
  - edge-LLM strategy
  - quantize-big vs build-tiny
tags:
  - edge-ai
  - quantization
  - on-device
  - inference
  - architecture
sources:
  - wiki/raw/articles/2026-07-15_bonsai-27b-prism-ml.md
  - wiki/raw/articles/2026-08-10_needle2-agentic-llm.md
confidence: high
---

# Edge AI Strategy — Quantize-Big vs Build-Tiny

Two 2026 startups solved the same constraint — frontier-adjacent intelligence inside a phone/watch/MCU memory budget — from **opposite ends of the parameter spectrum**. They agree on the mechanism that matters (quantization baked into training, never post-hoc) and disagree on where the intelligence should live before it is squeezed.

## The two routes

| Dimension | Quantize-Big | Build-Tiny |
|-----------|--------------|------------|
| Representative | [[entities/prism-ml]] (Bonsai 27B) | [[entities/cactuscompute]] (Needle 2) |
| Starting point | 27B frontier-scale teacher (Qwen3.6-27B) | 45M params, native from pretrain |
| Deployed size | ~4 GB (1-bit variant) | 14 MB single binary |
| Session RAM | ~6 GB (12 GB iPhone budget) | ~28 MB deterministic ceiling |
| Target task | general chat + reasoning | agentic tool-calling only |
| Accuracy story | 95% (ternary) / 90% (1-bit) of full-precision | trades with 230–270M baselines at 5–70× smaller |
| Compute/token | full transformer + quantized weights | 70 MFLOPs (vs 164 same-shape, 460–540 for LFM2.5) |

## Where they agree

Both reject post-hoc quantization. Cactus states it bluntly: *"The 2-bit model you deploy is the model that was trained"* — [[concepts/model-quantization|quantization-aware training]] runs pretrain→post-train across weights, activations, and KV cache. Prism ML runs the same discipline from the other side: QAT base → 8-bit → 4-bit → ternary/1-bit, BF16 LoRA at each stage, 30K-step end-to-end pass. Both ship Apache 2.0 weights on [[entities/hugging-face]].

Both also lean on **grammar-constrained decoding** to recover quality lost to compression — Cactus compiles a byte-level grammar from declared tool schemas and skips up to 98% of vocab projection on structural tokens.

## Where the bets diverge

- **Compress-big** bets that capability is *transferable* through extreme bit-reduction: keep a 27B model's world knowledge and reasoning, throw away the mantissa. Cost of the bet: biggest benchmark drops land exactly where agents need it most — agentic/tool-calling and instruction-following.
- **Build-tiny** bets that *agentic tool-calling needs no world knowledge* — mapping a messy sentence onto declared device functions doesn't require billions of params. It moves the residual knowledge out of weights entirely (Engram hashed n-gram tables) rather than compressing it. Cost of the bet: purpose-built, so it can't chat or reason generally.

## The unifying observation

The two routes are converging on the **same hardware-first design rule**: benchmark backwards from FLOPs/token and bytes/token budgets, never forward from a fixed architecture. Prism ML can't ship 27B without breaking the FP mantissa; Cactus can't ship a same-shape transformer without breaking the FLOPs budget. Neither is "better" — they occupy different rungs of the same [[concepts/edge-ai|on-device ladder]] (phone ↔ wearable/MCU).

## Open question

Whether the routes meet in the middle: does a natively-tiny model with Engram-style off-weight knowledge eventually match a compressed big model on reasoning, or is there a floor below which general reasoning can't be recovered regardless of quantization scheme? Neither company's benchmarks cover this head-to-head.

## Related

- [[concepts/edge-ai]] — broader on-device inference landscape
- [[concepts/model-quantization]] — QAT / ternary / 1-bit methods
- [[concepts/bonsai-27b]] — flagship compress-big artifact
- [[entities/prism-ml]] / [[entities/cactuscompute]] — the two entities
- [[entities/ericmigi]] — Pebble founder; Index 01/Ring ship Needle 2 in production

## Sources

- Bonsai 27B announcement (raw: 2026-07-15_bonsai-27b-prism-ml.md)
- Needle 2: 14MB Agentic LLM (raw: 2026-08-10_needle2-agentic-llm.md)
