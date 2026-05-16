---
title: Cerebras Systems
created: 2026-05-14
updated: 2026-05-16
type: entity
tags: [entity, company, hardware, gpu, ai-infrastructure, inference, mlops]
sources: [raw/newsletters/2026-05-13-cerebras-faster-tokens-please.md, raw/articles/2026-05-10_parallel-web-systems_cerebras-fact-checker.md, raw/newsletters/2026-05-16-ainews-cerebras-60b-ipo-slowly-then-all-at-once.md]
---

# Cerebras Systems

## Overview

Cerebras Systems is a semiconductor and AI infrastructure company based in Sunnyvale, California, specializing in **wafer-scale AI accelerators**. Founded in 2016 by **Andrew Feldman**, **Gary Lauterbach**, **Michael James**, **Sean Lie**, and **Jean-Philippe Fricker** — the same team that previously founded and sold SeaMicro to AMD for $355M — Cerebras builds the largest processors in computing history using an entire silicon wafer as a single chip, eliminating the inter-chip communication bottlenecks of traditional GPU clusters.

As of May 2026, Cerebras is on the verge of its IPO, trading expected under ticker **CBRS** at $125–$135/share, targeting a $26–$27B fully diluted valuation — up from $8.1B in Series G (September 2025). The company reported $510M in 2025 revenue (up 76% YoY) and net income of $238M (47% net margin), rare profitability at this growth stage.

## Technology

### Wafer-Scale Engine (WSE)

Cerebras's core innovation is using an entire 300mm silicon wafer as a single processor, rather than cutting wafers into individual dies. This eliminates the latency of communicating across multiple chips in a cluster.

| Generation | Transistors | Cores | On-chip SRAM | Process | Sparse FP16 | Dense FP16 |
|---|---|---|---|---|---|---|
| WSE-1 (2019) | 1.2T | 400K | 18 GB | ~16nm | — | — |
| WSE-2 (2022) | 2.6T | 850K | 40 GB | 7nm | — | — |
| WSE-3 (2024) | 4T | 900K | 44 GB | 5nm (TSMC) | 125 PFLOPs | ~15.6 PFLOPs |

**Key WSE-3 specs:**
- Die area: **46,225 mm²** — 57× larger than NVIDIA's H100 (826 mm²)
- Memory bandwidth: **21 PB/s** — 7,000× more than H100
- Fabric bandwidth: **214 Pb/s** — 3,715× faster than H100
- External memory: 1.5 TB, 12 TB, or **1.2 PB** (can train models up to 24T parameters in a single logical memory space)
- Supports 8:1 unstructured sparsity (so dense compute is 1/8 of the headline 125 PFLOPs)

### CS-3 System

The **CS-3** is Cerebras's AI supercomputer powered by the WSE-3. Each CS-3 rack delivers 2× the performance of CS-2 at the same power and price. Estimated BOM: ~$450K/rack (including the separate **KVSS node** — a dual-socket AMD CPU with 6TB DDR5 RDIMM for KV cache offload).

Clusters can scale to **2,048 CS-3 systems**, rated at 256 exaflops FP16 (sparse). At ~$2.5M/node, a full cluster costs ~$5–6B with MemoryX.

### Performance Claims

Cerebras claims **21× faster inference** than NVIDIA's DGX B200 Blackwell on Llama 3 70B in a reasoning scenario (1024 input, 4096 output tokens), and **32% lower cost** per token (TCO including capex and energy). This is based on end-to-end latency (TTFT + token generation time).

As SemiAnalysis notes, the sparse FLOPs number (125 PFLOPs) is marketed prominently while dense FLOPs (~15.6 PFLOPs) is not — a pattern they call "Feldman's Formula" (analogous to "Jensen Math" for NVIDIA).

## Business Model

1. **Hardware sales** — CS-3 systems sold to enterprises and hyperscalers
2. **Cloud services** — Cerebras Cloud API for model inference
3. **Multi-year compute contracts** — the OpenAI 750MW deal (see below)
4. **IPO** — May 2026, offering 28M Class A shares, raising $3.5–3.8B

### OpenAI Partnership

In January 2026, Cerebras signed a deal with OpenAI to deliver **750 MW of AI compute capacity** through 2028, one of the largest AI infrastructure contracts ever disclosed. Valued at **$24.6B in remaining performance obligations** (RPO), this deal transformed Cerebras's financials and enabled its IPO. The capacity will come online in multiple tranches.

In May 2026, Cerebras CFO **Bob Komin** confirmed that Cerebras is serving **trillion-parameter models**, including internal **OpenAI 5.4 and 5.5** models, and stated there is **"no limit"** to the model sizes Cerebras can serve. This directly links Cerebras's wafer-scale architecture to frontier model inference at OpenAI — not just training. TSMC wafer supply constraints remain a key risk through at least 2028.

OpenAI's stated rationale: "Cerebras adds a dedicated low-latency inference solution to our platform. That means faster responses, more natural interactions, and a stronger foundation to scale real-time AI."

### Other Notable Customers

GSK, G42, AstraZeneca, AbbVie, TotalEnergies, Jasper, nference, Argonne National Lab, Lawrence Livermore National Lab, Pittsburgh Supercomputing Center, Leibniz Supercomputing Centre, National Energy Technology Laboratory.

## Key People

- **Andrew Feldman** — Co-founder & CEO. Previously co-founded SeaMicro (sold to AMD for $355M). BA + MBA from Stanford.
- **Gary Lauterbach** — Co-founder & CTO. Previously co-founded SeaMicro.
- **Sean Lie** — Co-founder & Chief Hardware Architect.
- **Jean-Philippe Fricker** — Co-founder & Chief System Architect.
- **Dhiraj Mallick** — COO.
- **Bob Komin** — CFO (led the IPO process).

## History

- **2016** — Founded in Sunnyvale, CA by the SeaMicro team
- **2019** — Announced WSE-1 and CS-1
- **2022** — WSE-2 and CS-2
- **2024** — WSE-3 and CS-3; named a TIME Best Invention of 2024
- **Sep 2025** — Raised $1.1B Series G at $8.1B valuation
- **Oct 2025** — Withdrew IPO registration to focus on revenue growth
- **Jan 2026** — Signed 750MW OpenAI compute deal ($10B+ initially, expanded to $24.6B RPO)
- **May 2026** — IPO completed. Stock (CBRS) ended first trading day at **$280/share**, giving Cerebras a **market capitalization of $60 billion** — more than double the expected $125–135/share range and $26–27B valuation. 28M Class A shares offered, raising ~$7.8B (vs planned $3.5–3.8B). One of the largest AI hardware IPOs in history.

## Strategic Positioning

Cerebras positions itself against NVIDIA's GPU-centric approach on two fronts:

1. **Speed/latency** — Wafer-scale architecture eliminates inter-chip communication overhead, enabling real-time inference at scale. The KVSS node with separate CPU + DDR5 for KV cache offload is a key architectural choice for fast inference.
2. **Cost efficiency** — Lower TCO per token, fewer systems needed, less power and cooling infrastructure vs. GPU clusters.

However, the WSE-3 has a key limitation: **on-chip SRAM is only 44 GB** — tiny compared to HBM on GPU clusters. Cerebras compensates with massive bandwidth (21 PB/s) and external memory tiers, but this constrains model sizes that can fit entirely on-chip. Cerebras is also pursuing hybrid bonding of wafer-scale optical transceivers onto the WSE compute engine, targeting HPC workloads that NVIDIA has deprioritized by reducing FP64 on GPUs.

## Relationship to Other Wiki Entities

- [[entities/openai]] — Major customer, 750MW compute deal
- [[entities/nvidia]] — Primary competitor in AI accelerators
- [[concepts/karpathy-loop]] — Cerebras experiments on autoresearch loop optimization
- [[concepts/compute-scaling-bottlenecks]] — SRAM vs HBM tradeoffs
- [[entities/dylan-patel]] — SemiAnalysis coverage of Cerebras IPO and economics
- [[entities/anthropic]] — Cerebras per-token pricing lower than Claude API
