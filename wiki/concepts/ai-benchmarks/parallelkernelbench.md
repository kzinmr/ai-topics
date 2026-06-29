---
title: "ParallelKernelBench (PKB)"
created: 2026-06-24
updated: 2026-06-24
type: concept
tags:
  - benchmark
  - multi-gpu
  - inference
  - infrastructure
sources:
  - raw/articles/together.ai--blog-parallelkernelbench--2db40b9c.md
---

# ParallelKernelBench (PKB)

## Overview

**ParallelKernelBench (PKB)** is a benchmark and evaluation framework for **multi-GPU kernel generation**, developed by [[entities/together-ai.md|Together AI]]. While large language models have grown surprisingly capable at writing single-GPU CUDA kernels (see [[concepts/ai-benchmarks/kernelbench.md|KernelBench]]), PKB is the first systematic benchmark to test whether they can handle the substantially harder problem of writing performant multi-GPU kernels that communicate directly over NVLink.

The benchmark contains **87 problems** drawn from real production codebases — Megatron-LM, DeepSpeed, DeepEP, TensorRT-LLM, [[entities/nvidia.md|NVIDIA]] NeMo-RL, and others — covering LLM training, inference, and a long tail of non-LLM workloads. Each problem provides a standard PyTorch + NCCL implementation and requires the model to replace it with a custom CUDA kernel that moves data over symmetric memory across GPUs.

PKB is released as an open benchmark to drive progress in AI-driven distributed infrastructure optimization.

## Key Metrics

- **87 problems** from real codebases (Megatron-LM, DeepSpeed, TensorRT-LLM, NeMo-RL, plus GNN routing, distributed FFTs, Gaussian splatting, and more)
- **GPT-5.5**: fast@3 = **31%** (best model in zero-shot evaluation)
- **Gemini 3 Pro**: **24/87** single-shot correct; **35/87** with agentic harness (20 iterations); 26 of those 35 beat the PyTorch + NCCL baseline
- **Fewer than 1 in 4** correct solutions beat the PyTorch + NCCL baseline
- **Communication overhead accounts for 20%+** of inference latency in production, and the gap widens as compute scales faster than interconnect bandwidth
- All evaluations conducted across **4 H100 GPUs** with 100 randomized runs per problem

## Coverage

PKB's 87 problems are organized around a taxonomy of distributed parallelism strategies:

| Parallelism Type | Communication Pattern |
|---|---|
| Tensor Parallelism | All-reduce / all-gather across sharded weights |
| Context Parallelism | All-to-all across sequence dimension (Ulysses-style) |
| Data Parallelism | All-reduce for gradient sync |
| Expert Parallelism | Token dispatch and combine |
| Sequence Parallelism | Ring-based communication |
| FSDP / ZeRO | Gather-scatter for sharded optimizer states |

Beyond LLM workloads, PKB covers **non-LLM distributed workloads** including graph neural network (GNN) routing, distributed fast Fourier transforms (FFTs), and 3D Gaussian splatting — ensuring the benchmark tests general distributed computing capability, not just transformer-specific patterns.

## Key Findings

### Successes
- **Collective primitives**: Models perform reasonably well on standard patterns like all-reduce and all-gather
- **Tensor-parallel GEMMs**: Matrix-multiply kernels with communication fused into compute
- **Ulysses-style context parallelism**: Sequence-split attention with all-to-all communication — patterns well-represented in open-source training code

### Failures
- **Rank coordination**: Stronger reasoning models often produce kernels that compile but return incorrect results or deadlock — deeper reasoning failures beyond CUDA syntax
- **Data partitioning**: Models struggle to correctly shard tensors across ranks
- **Collective ordering**: The sequence and dependency ordering of distributed operations is frequently wrong
- **Narrow mechanism selection**: Generated kernels almost exclusively use copy engines or SM load/store instructions; **TMA (tensor memory accelerator)** and **NVLS (NVLink switch)** mechanisms are nearly absent, likely due to data scarcity in training corpora

### Agentic Harness Results
- Wrapping Gemini 3 Pro in an agentic loop (compile → test → benchmark → revise) improved correct solutions from **24 → 35 out of 87**
- Gains came primarily from fixing syntax errors, shape mistakes, and simple runtime bugs
- Performance **plateaued after ~20 refinement iterations** — the model stopped improving on harder reasoning failures around rank coordination and communication ordering

### Discovered Kernels
Three net new kernels were discovered — solutions faster than any publicly available reference:

1. **NeMo vocab-parallel log-prob with top-k/top-p filtering** (Gemini 3 Pro): Replaces vocabulary-gathering NCCL collectives with symmetric memory, fusing log-softmax, token extraction, and target gather into a single warp-shuffle reduction. Achieves significant speedup across sequence lengths for [[entities/nvidia.md|NVIDIA]] NeMo-RL's GRPO training loop.

2. **Hyena forward context parallelism** (GPT-5.5): Packs FFT convolution inputs into a single symmetric allocation and streams remote slices over NVLink, computing gating and reindexing in a unified pass — replacing repeated `all_to_all` calls.

3. **SAM 3 all-gathered mask IoU suppression** (GPT-5.5): Collapses variable-length `all_gather` collectives into a pipeline of symmetric-memory kernels that bitpack masks and compute pairwise overlap with hardware popcount — for cross-GPU duplicate suppression in video segmentation.

## Relation to Other Benchmarks

PKB is a direct extension of single-GPU kernel generation benchmarks into the multi-GPU regime. See also:

- **[[concepts/ai-benchmarks/kernelbench.md|KernelBench]]** — Standard benchmark for single-GPU CUDA kernel generation. PKB inherits its evaluation methodology (correctness + wall-clock speedup) but adds multi-GPU communication and rank coordination.
- **PerfCodeBench** — Broader code optimization benchmark that includes some GPU targets, but without the multi-GPU communication focus that defines PKB.

PKB fills a critical gap: while single-GPU kernel benchmarks have driven impressive LLM progress, the production bottleneck has already shifted to inter-GPU communication. PKB provides the infrastructure to measure and drive progress on that harder problem.

## Future Directions

The benchmark is intentionally scoped to **intra-node NVLink** in its initial release. Planned extensions include:
- **Inter-node fabrics** (RoCE, InfiniBand)
- **Other accelerators and topologies** (TPUs, etc.)
- **Higher-level programming models** — PKB already accepts Triton and ParallelKittens solutions; emerging interfaces like NCCL GIN and NVSHMEM are targets for future research

The broader goal is to enable LLM systems that can **autonomously optimize and manage large-scale distributed infrastructure** — ultimately bridging the gap to AI agents capable of handling end-to-end research engineering for distributed systems.
