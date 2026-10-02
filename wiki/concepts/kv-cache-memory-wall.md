---
title: "KV Cache Memory Wall"
created: 2026-09-30
updated: 2026-09-30
type: concept
tags: [kv-cache, inference, ai-infrastructure, performance, long-context, arxiv, hardware]
confidence: medium
sources:
  - raw/articles/arxiv-2609.30854-the-kv-cache-is-the-new-memory-wall.md
related:
  - "[[concepts/kv-cache]]"
  - "[[concepts/kv-cache-compression]]"
  - "[[concepts/kv-cache-compaction]]"
---

# KV Cache Memory Wall

At long context, autoregressive LLM inference is bounded by **memory bandwidth, not arithmetic throughput** — and the binding resource shifts from model weights to the **KV cache** as sequence length grows. This systematization-of-knowledge paper unifies a fragmented literature in which compression gains are reported under inconsistent workloads, hardware, and quality metrics, making cross-paper comparison impossible.

> "The KV Cache Is the New Memory Wall" (arXiv:2609.30854, cs.DC, Sept 2026) — Tejinder Singh.

## The Crossover, In Concrete Numbers

For **Llama-3-70B in BF16**: the ~**140 GB** weight footprint already exceeds the **80 GB HBM** of a single accelerator, and **one 128k-token sequence adds ~42 GB** of KV cache. Arithmetic intensity is derived in closed form as a **decaying function of context length**, parameterized by hardware topology (NVIDIA H100, NVIDIA B200, AMD MI300X — including per-die bandwidth partitioning), with explicit **crossover lengths where KV traffic overtakes weight traffic**.

## The Three-Regime Structure (Central Finding)

| Regime | Dominant traffic | Implication for KV compression |
|--------|------------------|--------------------------------|
| Below hardware-specific crossover | weights | KV compression yields **negligible** speedup |
| Beyond crossover | KV cache | each technique trades quality for bandwidth, approaching the roofline |
| Lossless-but-different-axis | capacity, not bandwidth | paging / prefix sharing free space but do **not** cut bandwidth |

Within the second regime the paper finds:
- **Quantization and eviction** cut bandwidth directly; degradation **accelerates below 4-bit precision** and eviction turns **discontinuous on position-sensitive tasks**.
- **Paging and prefix sharing** are lossless but address *capacity*, not bandwidth — a category error when the wall is bandwidth.
- **Tiering** converts the bandwidth wall into an *interconnect* problem bounded by PCIe/NVLink rather than HBM.

## Method Discipline

The paper's distinguishing contribution is methodological: a protocol that **strictly separates derived claims from reported claims**, evaluating one method per domain at 128k context under a single protocol. Five domains are classified: **quantization, token eviction, KV paging, prefix caching, heterogeneous tiering**. The authors close with **design rules for selecting a compression domain** given hardware, context length, and quality budget.

## Why It Matters

Much KV work in this wiki is algorithmic (scoring which tokens matter — see [[concepts/kv-cache-compression]]) or agent-level (multi-agent attention-matching compaction — see [[concepts/kv-cache-compaction]]). This paper supplies the missing **roofline layer**: it tells you *whether* compression can help at all on your hardware/context combination, before you pick an algorithm. It is the natural citation for "context engineering has a physical cost floor," and grounds the agent-side observation that long-horizon context pressure is not merely a prompting problem — see [[concepts/context-policy-evolution]].

## Related

- [[concepts/kv-cache]] — the underlying caching mechanism
- [[concepts/kv-cache-compression]] — algorithm-side survey this paper provides the roofline for
- [[concepts/kv-cache-compaction]] — agent-level compaction, capacity-framed
- [[concepts/context-policy-evolution]] — learned retention policies under the same pressure
- [[concepts/serving-llms-vllm]] — serving-system view (paged attention) where these walls bind
