---
title: "MiMo-V2.5-Pro — Xiaomi's Trillion-Parameter Open-Source Agent Model"
source: https://mimo.xiaomi.com/mimo-v2-5-pro/
date: 2026-04-23
publisher: Xiaomi
---

Xiaomi released MiMo-V2.5-Pro, its most capable model to date, delivering significant improvements in general agentic capabilities, complex software engineering, and long-horizon tasks.

## Specifications
- Architecture: Mixture-of-Experts (MoE) with hybrid attention
- Total parameters: 1.02T (1.02 trillion)
- Active parameters: 42B
- Context window: 1M tokens (native 32K, extended to 1M)
- Training data: 27T tokens, FP8 mixed precision
- License: MIT (permissive open-source)

## Architecture
- Interleaves sliding-window attention (SWA) and global attention (GA) at 6:1 ratio with 128-token window
- KV-cache storage reduced by nearly 7x while preserving long-context performance
- Post-training: 3-stage paradigm — SFT → Domain-Specialized Training → Multi-Teacher On-Policy Distillation (MOPD)

## Performance
- SWE-bench Pro: comparable to Claude Opus 4.6
- GDPVal-AA Elo: 1581, surpassing Kimi K2.6 and GLM 5.1
- Can autonomously complete professional tasks involving 1000+ tool calls
- Pricing: $1/M input, $3/M output (up to 256K context)

## Family
- MiMo-V2.5 (310B total, 15B active): native multimodal (video, audio, image, text)
- MiMo-V2.5-Pro (1.02T, 42B): agentic coding specialist
- Both released April 23, 2026 under MIT license
