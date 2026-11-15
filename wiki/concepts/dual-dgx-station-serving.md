---
title: "Dual DGX Station Serving (GLM-5.3 over ConnectX-8 RDMA)"
created: 2026-11-15
updated: 2026-11-15
type: concept
tags: [inference, vllm, distributed-systems, ai-hardware, glm]
sources:
  - raw/articles/2026-11-13_nvidia-glm-5.3-dgx-vllm.md
  - https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/
confidence: high
---

# Dual DGX Station Serving

NVIDIA's November 2026 developer-blog recipe (HN 138 pts) demonstrates serving **GLM-5.3 NVFP4** — Z.ai's frontier MoE model — across **two DGX Stations (GB300)** as a single OpenAI-compatible endpoint, and it doubles as the canonical worked example of the **memory-wall** problem in local frontier inference.

## The memory-wall arithmetic

| Quantity | Value |
|---|---|
| GLM-5.3 NVFP4 total parameters | **753 B** (MoE) |
| Activated per token | **40 B** (sparse routing) |
| Checkpoint size | **~464 GB** |
| GB300 HBM3e per GPU | **252 GB** |

Sparse activation cuts *compute*, but all expert weights must stay GPU-resident because any token can route to any expert — so 464 GB simply does not fit on one GB300. CPU weight offload is disabled (it would destroy throughput).

## Architecture

- Two GB300 DGX Stations linked over **ConnectX-8 RDMA** (validated with the "Connect Two DGX Stations" playbook, incl. GPU-memory RDMA test on both rails).
- **Tensor parallelism TP=2**: each GPU holds and computes ~half of every tensor; both Stations compute every request; Station A returns the answer through one endpoint.
- **vLLM** launches the distributed service across both Stations, enabling **multi-token prediction**, **FP8 KV-cache storage**, and **prefix caching** under concurrent load.

## Benchmarks (NVIDIA-reported, AIPerf on SPEED-Bench Coding)

- Peak output throughput **607.8 tok/s at concurrency 16**.
- **385.0 tok/s at concurrency 32**, mean request latency 453.5 s — the concurrency cliff shows inter-GPU RDMA sync becoming the bottleneck past 16.

## Significance

- First mainstream "two desktop-class AI workstations = one frontier server" pattern: DGX Station (~127 GB GPU memory each) marketed for local deployment, now explicitly documented as *not* single-node-capable for frontier MoE.
- A concrete data point for [[concepts/llm-price-collapse-2026]] debates: self-hosting frontier MoE requires ~1 TB of HBM-class memory regardless of sparsity.
- The NVFP4 checkpoint continues the format's march from inference-only into [[concepts/end-to-end-4bit-training]]-native territory.

## Related

- [[concepts/inference/vllm]] — the serving engine
- [[concepts/glm-5-3]] — the model
- [[concepts/nvfp4-4bit-floating-point]] — checkpoint format
- [[concepts/mixture-of-experts]] — why sparsity doesn't shrink memory
- [[concepts/local-llm/dgx-spark-nim]] — smaller-box local serving contrast
