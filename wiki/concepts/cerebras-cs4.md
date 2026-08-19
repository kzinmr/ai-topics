---
title: Cerebras CS-4 (Nexus Platform)
created: 2026-08-19
updated: 2026-08-19
type: concept
tags: [concept, hardware, ai-hardware, inference, cerebras, wafer-scale-integration, data-center]
sources: [raw/articles/2026-08-19_cerebras_cs4-product-page.md]
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
