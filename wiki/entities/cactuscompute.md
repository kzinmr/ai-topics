---
title: "Cactus Compute"
description: Edge-AI startup and developer of Needle 2, a 14MB / 45M-parameter agentic LLM for phones, wearables, smart-home devices and robots; YC-backed, creator of Cactus Quants 2-bit quantization.
type: entity
created: 2026-09-18
updated: 2026-09-19
aliases:
  - Cactus
  - Cactus Compute
  - cactuscompute
  - Cactus Quants
tags:
  - company
  - startup
  - ycombinator
  - on-device
  - edge-ai
  - open-source
  - inference
  - quantization
sources:
  - "wiki/raw/articles/2026-08-10_needle2-agentic-llm.md"
  - "https://cactuscompute.com/needle"
  - "https://cactuscompute.com/"
  - "https://github.com/cactus-compute/"
  - "https://news.ycombinator.com/item?id=43888777"
---

# Cactus Compute

**Cactus Compute** is an edge-AI startup (Y Combinator-backed) building extremely small **agentic language models** that run locally on sub-$200 smartphones, wearables, smart-home devices, robots, and even microcontrollers. Its central bet is that **agentic tool-calling does not require frontier-scale weights** — mapping a messy sentence onto a device's declared functions needs no world knowledge or open-ended prose, so a ~45M-parameter model suffices where chat needs billions.

## Needle 2 (Flagship, August 2026)

**Needle 2** is an open, purpose-built **45M-parameter agentic model** for tool calling, device use, and structured extraction. The whole model ships as a **single 14 MB binary** that runs a full session in **28 MB of RAM**.

| Attribute | Detail |
|-----------|--------|
| Params | 45M (35M matmul-active) |
| File size | 14 MB (single dependency-free C++ binary) |
| Session RAM | ~28 MB (deterministic ceiling, not a growth curve) |
| Quantization | CQ2-bit (Cactus Quants), avg ~2 bit |
| License | Apache 2.0 (weights on Hugging Face) |
| Speed | 500+ tok/s decode on Raspberry Pi 5; 400–1,500 tok/s on Meta Quest 3S / Apple Vision Pro; 300–700 on sub-$200 phones |
| Runs on | Cortex-M → x86 → WebAssembly; ESP32-S3/P4 microcontrollers |

Needle 2 trades wins with much larger small-model baselines (FunctionGemma 270M, LFM2.5 230M, Apple FM) at **5×–70× smaller** and 2-bit against their f16.

### The "Simple Attention Network" architecture

Needle's design is benchmarked backwards from constrained-hardware budgets (FLOPs/token and bytes/token):

- **Hadamard MLP** — replaces dense up/down projections with a fixed Walsh-Hadamard transform + learned diagonals, so channel mixing costs almost no parameters.
- **Engram memory** — moves world knowledge out of the weight stack into hashed n-gram tables read a few rows per token; capacity is nearly free at decode time.
- **Multi-lane residual streams** — give a 27-layer, 512-wide network routing flexibility at the cost of a few dot products.
- **Bounded KV cache** — 256-token sliding window + pinned system-prompt/tool sinks so a tool-calling model can never forget its tools.
- **Grammar-constrained decoding** — a byte-level grammar compiled from declared schemas constrains every token; the engine skips up to 98% of vocab projection on structural tokens.

**Energy argument:** Needle spends 70 MFLOPs/token vs 164 for a same-shape transformer and 460–540 for LFM2.5/FunctionGemma — 7×–85× fewer FLOPs than benchmarked models.

### Quantization thesis: Cactus Quants

Needle never quantizes post-hoc — small models break under it. Instead it **trains against Cactus Quants (CQ2-bit) from pretrain through post-train** across weights, activations, and KV cache. "The 2-bit model you deploy is the model that was trained." Weights never decompress into RAM: 2-bit codes expand inside vector registers and stay int8 end-to-end.

### Edge-cloud collaboration

Every response carries a **learned confidence score**; off-topic requests return the empty call (the empty call = refusal). Above a threshold the device acts; below it re-asks or escalates to cloud — keeping the default path private, instant, and free.

## Production Users

- **Pebble** (Eric Migicovsky, founder) runs Needle locally in the **Index 01** app and the **Index Ring** — a screenless wearable where spoken requests must turn into actions with or without a network connection.

## Positioning & Related

Cactus Compute sits in the **on-device / edge-AI** movement. It is a deliberate foil to [[entities/prism-ml]] (Prism ML), which attacks phone-deployment from the opposite direction — extreme quantization of large models (Bonsai 27B) rather than a natively tiny model:

| Strategy | Representative | Approach |
|----------|---------------|----------|
| Compress big models down | [[entities/prism-ml]] (Bonsai) | Ternary/1-bit QAT of 8B–27B models |
| Build tiny models natively | [[entities/cactuscompute]] (Needle 2) | 45M / 14MB purpose-built agentic model |

Both bake quantization into training (QAT) rather than post-hoc.

- [[concepts/edge-ai]] — on-device / edge deployment category
- [[concepts/model-quantization]] — quantization methods (Cactus Quants / QAT)
- [[concepts/advanced-tool-use]] — agentic tool-calling capability Needle 2 targets
- [[concepts/llama-cpp]] — local inference runtime ecosystem (contrast: Cactus ships its own engine)
- [[entities/prism-ml]] — contrasting edge-LLM strategy (extreme quantization of big models)
- [[entities/ericmigi]] — Eric Migicovsky — Pebble founder; Index 01 / Index Ring ship Needle 2

## Community

- **Website**: https://cactuscompute.com/
- **Needle page / playground**: https://cactuscompute.com/needle
- **GitHub**: https://github.com/cactus-compute/
- **Hacker News**: https://news.ycombinator.com/item?id=43888777

## Sources

- [Needle 2: 14MB Agentic LLM for Tiny Devices](https://cactuscompute.com/needle) — [raw](wiki/raw/articles/2026-08-10_needle2-agentic-llm.md)
- [Cactus Compute website](https://cactuscompute.com/)
- [Cactus Compute GitHub](https://github.com/cactus-compute/)
- [Hacker News discussion](https://news.ycombinator.com/item?id=43888777)
