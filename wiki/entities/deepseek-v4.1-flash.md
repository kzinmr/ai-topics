---
title: "DeepSeek-V4.1-Flash"
created: 2026-09-29
updated: 2026-10-17
type: entity
tags:
  - model
  - open-weight
  - inference
  - architecture
  - moe
confidence: high
sources:
  - raw/articles/2026-09-29_arxiv_2609.19969_deepseek-v4.1-flash-kv-cache-compression.md
  - raw/articles/2026-09-15_fireworks-ai_DeepSeek-V4.1-Flash-Astra.md
  - raw/articles/2026-10-17_deepseek-api-docs_deepseek-v4.1-flash-1017-release-news.md
related:
  - deepseek
  - test-time-compute
  - test-time-interaction-scaling
---

# DeepSeek-V4.1-Flash

**DeepSeek-V4.1-Flash** is a multimodal Mixture-of-Experts (MoE) model from [[entities/deepseek|DeepSeek]] with **552B backbone parameters** and support for **up to 1M-token contexts**. Its headline contribution is pushing **KV cache compression** to a new level, targeting the compute/storage/bandwidth bottleneck created by long-horizon *agentic* workloads. Checkpoints are open-weight (Hugging Face: `deepseek-ai/DeepSeek-V4.1-Flash`).

> Tech report: "DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression" (arXiv:2609.19969, 2026-09-17).

## The Bottleneck It Targets

Long-horizon agents make workloads increasingly **input-heavy** (prefill-dominated). Even after long-context compute has been optimized, three costs remain the primary deployment bottleneck:

- **Compute** — prefill stays expensive
- **Storage** — large KV caches strain HBM and SSD capacity
- **Bandwidth** — moving KV data is costly

DeepSeek-V4.1-Flash attacks all three with a purpose-built architecture rather than only model-quality gains.

## Architecture

| Component | Effect |
|-----------|--------|
| **Causal Encoder-Decoder (CED)** | Activates **16B** params/token at *decode* but only **8B** at *prefill* — cheaper on input-heavy agent workloads |
| **Compressed Sparse Attention 2 (CSA2)** | Cross-layer KV cache reuse |
| **FP4 KV caching** | Halves KV precision for storage/bandwidth |
| **SWA Bounded Replay** (deployment opt) | Slashes persistent (SSD/host-memory) KV footprint |

### KV footprint numbers

- **Global KV (always in HBM):** **890 bytes/token**, ≈ **1/4** of DeepSeek-V4-Flash.
- **Persistent KV (SSD / host memory):** ≈ **1/8** of DeepSeek-V4-Flash (via SWA Bounded Replay).

Despite the much smaller KV footprint, the report claims *substantially better* performance than the baseline.

## Training

- Pretrained on a **45T-token multimodal corpus**.
- Comprehensive post-training across text-based and multimodal **agentic** scenarios.
- Several efficient architectural extensions streamline the DeepSeek-V4 lineage.

## Deployment Perspective

Third-party hosts positioned V4.1-Flash as near-frontier agentic coding at a fraction of the cost — e.g. Fireworks AI's "Astra-level DeepSWE at 1/15th the cost." This is the practical payoff of the KV-compression work: long-horizon coding agents become affordable to serve.

^Confidence high on architecture/spec facts (DeepSeek's own tech report + corroborating deployment blog). Performance-vs-baseline claims are the vendor's own and not independently benchmarked here.

## DeepSeek-V4.1-Flash-1017 (2026-10-17 refresh)

On 2026-10-17 DeepSeek released **DeepSeek-V4.1-Flash-1017**, an MIT-licensed open-weight checkpoint positioned as a "minor update" but with substantial agentic gains (see [event page](../events/2026-10-17-deepseek-v4.1-flash-1017-release.md) for full benchmarks and reception). Key deltas:

- **Vendor-reported agentic gains**: Terminal-Bench 4.0 31.2→42.3, ProgramBench 20.3→29.1, DeepSWE v1.1 74.2→77.0, Apex Bench 64.6→72.1 — top of the compared field (vs GLM-5.3, GPT-5.6 Sol; exceeding Opus 5 on several). All vendor-self-reported; independent verification pending.
- **RL with self-feedback** for end-to-end project development ("Wish-Driven Programming"): full games and 3D scenes built from scratch.
- **Shorter outputs + faster task completion** — cost-per-task improvement on top of unchanged API pricing ($0.15/$0.60 per M tokens on OpenRouter, 1M context).
- **Harness co-release**: optimized for DeepSeek Harness v0.2.1-rc.1, Tencent CodeBuddy, WorkBuddy.
- **Prompt encoding toolchain change**: no Jinja chat template; ships `encoding.py` reference + `deepseek-recipe` (Rust/Python) toolkit covering Messages / Chat Completions / Responses API conversion, thinking mode, tool calling, interleaved images.
- Shipped alongside the **Search & Fetch APIs** opening to everyone at $0.75/1k calls — see [[concepts/agentic-search]].

## Related

- [[entities/deepseek]] — the lab
- [[events/2026-10-17-deepseek-v4.1-flash-1017-release]] — the 1017 refresh + Search/Fetch API event
- [[concepts/test-time-compute]] — long-horizon agents are exactly the workloads that make inference/test-time compute expensive
- [[concepts/test-time-interaction-scaling]] — agent interaction budgets are what strain KV caches this model compresses

## Sources

- [DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression](https://arxiv.org/abs/2609.19969) — arXiv:2609.19969, 2026-09-17
- Fireworks AI blog: "DeepSeek-V4.1-Flash: Astra-level DeepSWE at 1/15th the cost" (2026-09-15) — third-party deployment
