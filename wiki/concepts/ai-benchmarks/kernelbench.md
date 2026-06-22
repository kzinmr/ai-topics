---
title: "KernelBench"
type: concept
created: 2026-04-25
updated: 2026-06-15
tags:
  - benchmark
  - code-model
  - performance-engineering
  - hardware
aliases:
  - kernelbench
status: active
sources:
  - https://github.com/ScalingIntelligence/KernelBench
related_concepts:
  - concepts/ai-benchmarks/perfcodebench
---

# KernelBench

**KernelBench** is a benchmark for evaluating LLMs on **CUDA kernel optimization**. It focuses on generating efficient GPU kernels for common deep learning operations, testing models' ability to write performance-critical accelerator code.

**GitHub**: [ScalingIntelligence/KernelBench](https://github.com/ScalingIntelligence/KernelBench)

## What It Measures

- **Domain**: GPU kernel optimization for deep learning operations
- **Task type**: Code generation for CUDA kernels
- **Key focus**: Performance-critical accelerator code generation
- **Evaluation**: Correctness and performance of generated CUDA kernels

## Relevance

KernelBench is closely related to [[concepts/ai-benchmarks/perfcodebench]], which also evaluates GPU optimization capabilities. However, KernelBench focuses specifically on CUDA kernels for deep learning operations, while PerfCodeBench covers broader system-level optimization across multiple languages and domains.

## Key Findings

- GPU optimization remains extremely challenging for current LLMs
- CUDA kernel generation requires understanding of parallel decomposition, memory hierarchy, and synchronization
- Performance gap between CPU and GPU tasks is significant across all models

## Related Benchmarks

- [[concepts/ai-benchmarks/perfcodebench]] — System-level high-performance code optimization benchmark
- [[concepts/ai-benchmarks/livecodebench]] — Contest-style code evaluation
- [[concepts/ai-benchmarks/swe-bench]] — Real-world software engineering tasks
