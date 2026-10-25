---
title: Cerebras CS-4 (Nexus Platform)
created: 2026-08-19
updated: 2026-10-25
type: concept
tags: [concept, hardware, ai-hardware, inference, cerebras, wafer-scale-integration, data-center]
sources: [raw/articles/2026-08-19_cerebras_cs4-product-page.md, raw/articles/2026-10-22_cerebras_trillion-parameter-deployment.md]
---

# Cerebras CS-4 (Nexus Platform)

The **CS-4** is Cerebras's fourth rack-scale AI supercomputer generation, announced in August 2026. It is the first iteration of the new **Nexus Platform Architecture** — a modular design separating Compute, Power, and I/O so hyperscalers can deploy power/cooling/network infrastructure first and slide in compute "backpacks" later. Cerebras claims **up to 30× faster inference than production GPU systems** and **>1,000 tokens/sec on models exceeding 10 trillion parameters**.

## Architecture (vendor claims, fetched 2026-08-19)

| Component | Detail |
|---|---|
| **Wafers per system** | 3 × WSE-3 Turbo ("WSE-3T"), each ~2× the speed of WSE-3 |
| **Wafer-to-wafer interconnect latency** | **2 µs** — wafers linked within/across racks *without a switch* (new Wafer I/O Module) |
| **Power delivery** | ~0.5 mm from processor (vs ~50 mm on GPU boards) → nearly eliminates board-level loss; ~2× power to WSE-3T |
| **Wafer-Scale Backpack** | self-contained 3D package: wafer + power conversion + direct liquid cooling + I/O + control; **50% fewer components**; deploy "from days to hours" |
| **I/O** | new programmable subsystem; doubles I/O bandwidth, reduces latency |
| **PowerRack** | power/cooling/network layer installed and facility-qualified *before* compute arrives |
| **Throughput** | up to 10× more throughput-per-watt than CS-3; "up to 30× faster inference vs GPUs" |

## Context & positioning

- Successor to CS-3 (WSE-3: 4T transistors, 44 GB SRAM, 125 PFLOPs sparse FP16; see [[entities/cerebras-systems]])
- Targets the **ultrafast-interactivity** regime: 2 µs inter-wafer latency is what lets a single system serve 10T+-parameter models with interactive decode (Cerebras's core "speed is a capability" thesis — cf. Big Chip Club series on agents)
- First shipments began **Q3 2026** (per product page)
- HN front page Aug 18 2026 (305 pts); SemiAnalysis also covered the generation (newsletter digest 2026-08-19)

## Caveats

- All figures are **vendor claims** — no independent benchmark as of Aug 19 2026. WSE-3T's transistor count / SRAM / FLOPs not published on the product page
- The "30× vs GPUs" baseline (which GPU system, which model, which metric — TTFT vs tokens/s) is not specified on the page
- Cerebras's known marketing pattern (per SemiAnalysis): sparse-FLOP headline numbers over dense ("Feldman's Formula") — apply the same skepticism to the 30× figure until independent testing

## Related

- [[concepts/inference-hardware]] — wafer-scale vs GPU-cluster silicon comparison
- [[concepts/inference-speed-development]] — latency as a product capability, not just an optimization
- [[entities/cerebras-systems]] — CS-4 as the first Nexus generation
- [[entities/nvidia]] — GPU-cluster baseline the 30× claim targets
- [[concepts/compute-scaling-bottlenecks]] — SRAM vs HBM tradeoffs; inter-wafer interconnect

## Trillion-Parameter Model Deployment on WSE-3T (Oct 22 2026)

Cerebras published the arithmetic behind serving **multi-trillion-parameter models at 1000-2000+ tok/s** on wafer-scale chips, using open-weight **Kimi K3 (~3T params, 69 linear-attention + 24 dense layers)** as the worked example:

- A WSE-3T wafer has **44 GB on-chip SRAM**. At 4-bit weights, 3T params ≈ 1.5 TB raw payload; ÷ 93 layers ≈ **16 GB/layer**.
- **Dense layers**: one per wafer (the remaining ~28 GB goes to that layer's KV cache for all active requests). **Linear-attention layers**: two per wafer (2×16 GB) — they keep a small fixed-size state per request instead of a KV cache, so no extra room is needed. Total for Kimi K3: 69/2→35 + 24 = **59 wafers**.
- Wafers run as an **assembly-line pipeline**; only activations cross wafer boundaries via **RDMA over Ethernet (~2 µs/hop)**. Weights never move because whole layers fit in one wafer's SRAM.
- Concurrency comes from **pipeline fill**: each stage works on a different request (× micro-batch), so requests-in-flight ≈ stages × micro-batch size. Smaller micro-batches → lower per-request latency; larger → higher throughput. KV-cache SRAM budget caps max concurrent requests.
- The post cites Kimi K3 at **88.3% Terminal-Bench 2.1** (vs GPT-5.6 Sol 88.8%) and **91.2% BrowseComp** (vs 90.4%) — an open model nudging frontier proprietary scores, reinforcing Cerebras's open-model-fast-serves positioning.

Sources: raw `raw/articles/2026-10-22_cerebras_trillion-parameter-deployment.md`; HN https://news.ycombinator.com/item?id=50227356 (204pts, Oct 25 2026).
