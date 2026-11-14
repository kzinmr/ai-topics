---
title: "smolmaxxing"
created: 2026-11-14
updated: 2026-11-14
type: entity
tags:
  - edge-ai
  - on-device
  - local-llm
  - quantization
  - open-source
  - simd
  - inference-speed
  - memory-efficiency
confidence: medium
sources:
  - https://github.com/hyperionaidev/smolmaxxing
  - raw/articles/2026-11-13_hyperionaidev_smolmaxxing-readme.md
  - raw/articles/2026-11-13_hyperionaidev_smolmaxxing.md
related:
  - concepts/local-llm/llama-cpp
  - concepts/local-llm/gguf
  - concepts/edge0
---

# smolmaxxing

**smolmaxxing** (MIT, ~501 stars at capture, November 2026) is an open-source project by Hyperion AI ("maxxing the ability to run different LLMs on the smallest devices possible") that runs the largest feasible LLM on consumer hardware never intended for it — a $50-class Android TV box, a 2013 iPad Air, a mid-range Android phone. Every published number was measured on the device itself. It hit HN front page on 2026-11-13 (390 pts, item 50468888) and sits in the same "LLMs on resurrected hardware" wave as Edge0 and Needle2.

## Headline results

| | Xiaomi TV Box S (3rd Gen) | iPad Air (2013) | OnePlus Nord CE 2 (2022) |
|---|---|---|---|
| Chip | Amlogic S7D, 4× Cortex-A55 | Apple A7, 2 cores | Dimensity 900 (2× A78 + 6× A55) |
| Usable RAM | ~1 GB (of 1.9) | ~700 MB (of 1) | ~3 GB free (of 7.4) |
| Everyday model | Qwen3.5-2B @ 7.7 tok/s | Bonsai-1.7B 1-bit @ 24–26 tok/s | Qwen3.6-35B-A3B @ 4.9–5.7 tok/s |
| Biggest model | Ling-mini-2.0 16B @ 5.1 tok/s | Ling-mini-2.0 16B @ 2.6–4.5 tok/s | Qwen3-Next-80B-A3B @ 2.6–3.1 tok/s |

16B MoE models on ~1 GB of RAM; an 80B-A3B MoE on a phone with ~3 GB free.

## Techniques (all a patch on llama.cpp)

- **Chip-specific kernels**: a 1-bit lookup-table kernel and repacked 2-bit/ternary formats for Cortex-A55, plus A7 variants for a chip with no dot-product instructions. The 1-bit kernel needs only basic NEON.
- **MoE expert paging from flash**: keep popular experts in RAM, read cold experts on demand, prefetch the next layer's — the mechanism behind 16B-on-1GB. Dense models bigger than RAM stream at full flash speed.
- **Vocabulary head pruning**: most of a small model's vocabulary is rarely used, so rarely-used output rows are dropped (stock llama.cpp cannot load the pruned-head files). A "headless" mode also stops the launcher/Google services on the TV while a model runs.

The repo includes a 165-experiment lab notebook (EXPERIMENT.md, failures included) and a community contribution path for new devices. The HN thread surfaced the adjacent ecosystem: ps2-llm (10M params on a PlayStation 2), iiama2.c (stories15M on a Wii GPU), esp32-ai (per-layer embeddings), and a 3.16M-param INT4 transformer fully on-chip on a KV260 FPGA at ~60K tok/s. The recurring skeptical question — "are they useful?" — got the honest answer from the author: mostly not yet for general tasks, but fine-tuned 1–2B models on narrow customer data look promising, and the goal is to exhaust the kernel/memory-design search space that frontier labs have no incentive to explore.

## Positioning

Complements rather than competes with [[concepts/edge0|Edge0]] (aggressive quantization of usable models) and [[concepts/local-llm/needle2-agentic-edge-llm|Needle2]] (a purpose-built 14MB agentic model): smolmaxxing attacks the *runtime* — kernels, paging, head pruning — on arbitrary existing checkpoints.

## Related

- [[concepts/local-llm/llama-cpp]] — the codebase it patches
- [[concepts/local-llm/gguf]] — the quant formats it repacks
- [[concepts/edge0]] — same week, same "tiny hardware LLM" news cycle
