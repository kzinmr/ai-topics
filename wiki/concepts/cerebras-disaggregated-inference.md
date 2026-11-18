---
title: "Cerebras Disaggregated Inference"
type: concept
created: 2026-11-18
updated: 2026-11-18
tags: [inference, cerebras, gpu, vllm, sglang, token-economics, hardware]
sources:
  - raw/articles/2026-11-17_cerebras_disaggregated-inference.md
confidence: medium
related:
  - "[[concepts/epd-disaggregation]]"
  - "[[entities/cerebras-systems]]"
  - "[[concepts/cerebras-cs4]]"
  - "[[concepts/deepinfer]]"
---

# Cerebras Disaggregated Inference

**Disaggregated inference** is Cerebras' production architecture (announced Nov 17, 2026) in which **GPUs handle prompt processing (prefill)** and **Cerebras wafer-scale systems handle response generation (decode)**. The company reports **5× more tokens per megawatt** at unchanged ultrafast decode speeds versus a CS-3-only configuration, measured on a shared GPT-OSS-120B endpoint on the Cerebras Inference Cloud (Nov 14, 2026).

> All throughput figures are Cerebras' own production measurements ("third-party benchmarking or internal testing" per the post's disclaimer) — treat as vendor-reported, not independent.

## Why split prefill from decode?

- **Decode is autoregressive**: one token at a time, re-reading model data from memory each step → *memory-bandwidth-bound*. SRAM-centric chips win here; Cerebras claims tens of GB of on-wafer SRAM and tens of PB/s bandwidth — **350× the SRAM capacity and 5,400× the memory bandwidth of a typical GB300 GPU** (vendor figure).
- **Prefill is compute-bound** and maps well to conventional accelerators — in the production deployment, **AMD Instinct GPUs** process prompts while **Cerebras CS-3 systems** generate responses.
- Alternative splits exist (draft–target, attention–FFN), but prefill/decode separation is "uniquely advantageous" for *highly interactive* (agentic) inference, Cerebras argues. The motivation is explicitly power-constrained scaling: agentic apps (Muse, Copilot, Codex) need interactive speeds, and Goldman Sachs research forecasts agent usage boosting tech cash flow — the industry must deliver more tokens per megawatt.

## Product forms

1. **Cerebras Inference Cloud** — disaggregation applied broadly across hundreds of MW by end of 2027.
2. **Partner reference architecture** — partners co-locate their own prefill accelerators with Cerebras systems. Two integration levels:
   - **End-to-end stack**: routing framework between prefill/decode pools + a prefill engine (vLLM or SGLang) + Cerebras decode engine + **KV Portal** software that transfers KV caches over RDMA.
   - **Decode-only SDK**: partners bring their own framework/prefill engine; includes a mock Cerebras decode replica and a reference integration.

Early-access partners: **Amazon Web Services, Fireworks AI, Gimlet Labs, General Compute**.

## Context

- Sits in the same design space as [[concepts/epd-disaggregation]] (Encoder-Prefill-Decode for VLMs in SGLang) — prefill/decode separation is becoming the industry-standard serving topology; Cerebras' twist is pairing *commodity GPUs for prefill* with *wafer-scale SRAM machines for decode* rather than homogeneous GPU pools.
- Complements [[concepts/cerebras-cs4]] (CS-4 / Nexus, trillion-param deployments) and Cerebras' claimed 700 MW datacenter pipeline.
- Related economics angle: tokens-per-megawatt is the new unit of inference competition (see [[concepts/token-economics]], [[concepts/gpu-bubble-ai-inference]]).

## See Also

- [[entities/cerebras-systems]] — the company
- [[concepts/deepinfer]] — DeepSeek's engine where disaggregation remains closed-source
