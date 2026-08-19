---
title: "Cerebras CS-4 — Product page (Nexus Platform Architecture)"
type: article
source: https://www.cerebras.ai/cs4
publisher: Cerebras Systems
published: 2026-08
fetched: 2026-08-19
fetched_by: active-crawl
---

# Cerebras CS-4 (product page, fetched 2026-08-19)

_Source: https://www.cerebras.ai/cs4 (HN front page Aug 18 2026, 305 pts)_

## Marketing claims (verbatim)

- "The Cerebras CS-4 delivers revolutionary AI performance, replacing hundreds of GPUs with a single wafer-scale chip."
- "Introducing CS-4: The Fastest AI Accelerator in the Industry"
- "The Fastest AI Just Got Faster. Introducing the all new Cerebras CS-4, a revolutionary rack-scale solution that delivers up to 30x faster inference compared to GPUs, enhanced economics, and a simple path to deploy hyperscale capacity. It is the architecture for frontier AI."
- "Three WSE-3 Turbo per System. Each wafer delivers up to 2x the speed of the previous generation."
- "Powered by WSE-Turbo, CS-4 delivers up to 30x faster inference compared to GPU systems, setting a new record for the fastest inference available in production."
- "The CS-4 solution shifts the inference Pareto frontier, delivering up to 10x more throughput per watt than CS-3 while generating tokens up to 30x faster than production GPU systems."
- "By reducing wafer-to-wafer interconnect latency to 2 microseconds, CS-4 delivers more than 1,000 tokens per second on models exceeding 10 trillion parameters, preserving interactive decode performance at unprecedented scale."

## Architecture

- **First iteration of the Cerebras Nexus Platform Architecture** — modular design around Compute, Power, and I/O
- **Wafer-Scale Backpack**: self-contained assembly folding wafer, power conversion, direct liquid cooling, high-speed I/O, and control electronics into a compact 3D package with 50% fewer components; simplifies manufacturing, deployment "from days to hours"
- **High-density power delivery**: power delivery ~0.5 mm from the processor (~100x closer than ~50 mm on conventional GPU boards) → nearly eliminates board-level power loss, doubles power to the WSE-3T, enabling higher frequencies
- **Next-gen wafer I/O interface**: programmable I/O subsystem; doubles I/O bandwidth, reduces latency; Wafer I/O Module links wafers within/across racks *without a switch* → wafer-to-wafer latency as low as **2 microseconds**
- **Deploy infrastructure then compute**: separates stable power/cooling/network layer from modular wafer-scale compute; Cerebras PowerRack installed and facility-qualified before compute arrives; compute backpacks slide in

## Status

- "First CS-4 shipments begin this quarter." (Q3 2026, per page wording as fetched)

## Caveats

- All performance figures are vendor claims; no independent benchmarks found as of fetch date
- WSE-3 Turbo per-wafer specs (transistors, SRAM, FLOPs) not published on this page; "2x the speed of the previous generation" is relative to WSE-3 (4T transistors, 44 GB SRAM, 125 PFLOPs sparse FP16 per prior wiki coverage)
