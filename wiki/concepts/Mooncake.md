---
title: "Mooncake"
type: concept
status: incomplete
description: "Mooncake is a KVCache-centric disaggregated architecture for serving large language models, used by Moonshot AI's Kimi chatbot."
created: 2026-04-27
updated: 2026-04-28
tags: [concept, llm-serving, inference, kv-cache, architecture, moonshot]
aliases: [Mooncake Architecture, Mooncake KVCache]
related: [[concepts/inference/vllm]], [[concepts/inference/sglang]], [[concepts/kvcache]], [[entities/moonshot-ai]]
sources: [https://arxiv.org/abs/2407.00079]
---

# Mooncake

## Summary

**Mooncake** is the serving platform for **Kimi**, a leading LLM service by Moonshot AI. It introduces a KVCache-centric disaggregated architecture that separates prefill and decoding clusters while leveraging underutilized CPU, DRAM, and SSD resources of GPU clusters for disaggregated KVCache storage. Mooncake won the **Best Paper award at USENIX FAST 2025**.

## Key Ideas

- **Prefill/Decoding Separation**: Mooncake physically disaggregates the prefill (prompt processing) and decoding (token generation) stages onto separate clusters, allowing independent scaling of each.
- **KVCache-Centric Scheduler**: The core scheduler balances maximizing effective throughput while meeting latency-related Service Level Objectives (SLOs). Unlike traditional studies that assume all requests will be processed, Mooncake handles highly overloaded scenarios.
- **Disaggregated KVCache Pool**: Uses CPU DRAM and SSD as a secondary cache tier for KVCache blocks, enabling larger effective cache capacity than GPU memory alone allows.
- **Prediction-Based Early Rejection**: When the system is overloaded, a predictive policy rejects requests early to maintain SLOs for accepted requests.
- **Tiered Storage**: GPU HBM → CPU DRAM → NVMe SSD form a multi-tier KVCache hierarchy, trading storage for computation.

## Architecture

Mooncake Store provides:
1. **Fast, scalable, and fault-tolerant KVCache storage and transfer** across nodes
2. **Efficient P&D (Prefill and Decode) disaggregation** via dedicated networking
3. **KVCache reuse** across requests with shared prefixes
4. **Flexible scheduling** of cache placement decisions

## Significance

Mooncake demonstrated that carefully architecting the LLM serving stack around KVCache locality and reuse can dramatically improve throughput in long-context scenarios — a critical capability for production chatbots like Kimi that handle documents with hundreds of thousands of tokens. The architecture has been integrated into open-source serving frameworks including [[concepts/inference/vllm]].

## Related Concepts

- [[concepts/inference/vllm]] — PagedAttention-based serving engine that also optimizes KVCache
- [[concepts/inference/sglang]] — Structured generation LLM serving
- [[concepts/kvcache]] — The key-value cache mechanism underlying transformer inference
- [[entities/moonshot-ai]] — The company behind Kimi and Mooncake

## Sources

- [Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving (arXiv:2407.00079)](https://arxiv.org/abs/2407.00079)
- [USENIX FAST 2025 Best Paper — Mooncake Presentation](https://www.usenix.org/conference/fast25/presentation/qin)
- [Ruoyu Qin et al., Moonshot AI & Tsinghua University](https://www.usenix.org/system/files/fast25_slides-qin.pdf)
