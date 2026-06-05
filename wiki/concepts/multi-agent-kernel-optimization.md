---
title: "Multi-Agent Kernel Optimization"
type: concept
created: 2026-06-05
updated: 2026-06-05
tags:
  - multi-agent
  - gpu
  - harness-engineering
  - coding-agents
  - optimization
  - nvidia
  - cursor
  - fused-kernels
sources:
  - raw/articles/2026-06-05_cursor_multi-agent-kernels.md
related:
  - concepts/harness-engineering
  - concepts/cursor-ide
  - concepts/ai-agent-engineering
  - entities/cursor-3
  - entities/nvidia
---

# Multi-Agent Kernel Optimization

**Multi-Agent Kernel Optimization** refers to the application of multi-agent AI systems to automatically optimize GPU compute kernels — the low-level programs that execute on GPU hardware. A landmark demonstration by [[entities/cursor-3|Cursor]] and [[entities/nvidia|NVIDIA]] in June 2026 showed that a [[concepts/harness-engineering|multi-agent harness]] could autonomously optimize 235 CUDA kernels across 124+ production open-source models, achieving a 38% geomean speedup over a single-agent PyTorch baseline.

## Summary

- **Collaboration**: Cursor × NVIDIA
- **Scope**: 235 CUDA kernels from 124+ production open-source models (DeepSeek, Qwen, Gemma, Kimi, Stable Diffusion)
- **Hardware**: 27× NVIDIA Blackwell B200 GPUs
- **Duration**: 3 weeks of fully autonomous operation
- **Results**: 38% geomean speedup vs single-agent PyTorch baseline; 63% of problems improved (149/235); 19% of problems saw 2×+ improvement (45/235)

### SOL-ExecBench

The system uses SOL-ExecBench, a problem generation and benchmarking pipeline that validates CUDA kernel optimizations against theoretical hardware limits (SOL — "Speed Of Light"). This benchmark defines what is physically achievable on the hardware, providing an upper bound against which the agents' progress can be measured.

### Multi-Agent Harness

The optimization harness follows a [[concepts/harness-engineering|harness engineering]] pattern with two tiers of agents:

1. **Planner Agent** — Distributes kernel optimization problems across a pool of autonomous worker agents and dynamically rebalances work based on progress
2. **Worker Agents** — Independently optimize individual CUDA kernels, proposing code changes, running benchmarks, and refining solutions

### Coordination Mechanism

All agents coordinate through a **single markdown file** that specifies:
- Output format requirements
- Optimization rules and constraints
- Test harness invocation commands

This minimal protocol keeps agent communication lightweight while ensuring all workers produce compatible, verifiable output.

### Self-Healing Loop

A critical emergent behavior: the system independently learns to call the benchmarking pipeline in response to its own code changes, creating a continuous **test → debug → optimize** loop without human intervention. This [[concepts/ai-agent-engineering|agent engineering pattern]] of autonomous eval-driven iteration is what enabled the system to operate for 3 weeks without human supervision.

## Optimization Strategies

Three distinct kernel optimization strategies were demonstrated:

| Strategy | Model / Framework | Improvement | SOL Score |
|----------|------------------|-------------|-----------|
| BF16 Grouped Query Attention with Paged Prefill | SGLang / Llama 3.1 8B | 84% geomean speedup over FlashInfer | 0.9722 |
| NVFP4 MoE Linear with Gating | DeepSeek | Novel FP4 quantized MoE gating optimization | — |
| BF16 Matrix Multiplication | General | Standard matmul optimization | — |

### Implementation Languages

The optimized kernels were written in two complementary languages:
- **CUDA C with inline PTX** — Provides lowest-level hardware access for manual register-level optimization
- **CuTe DSL** — NVIDIA's high-level composable abstraction layer for expressing GEMM-like operations and tiling strategies

## Significance

This work demonstrates several important principles for multi-agent systems applied to hardware-level optimization:

1. **Autonomous iteration at scale** — A multi-agent system can operate for weeks on 27 GPUs, making thousands of optimization attempts without human guidance
2. **Emergent coordination** — A simple shared protocol (single markdown file) enables effective coordination without complex agent middleware
3. **Self-healing behavior** — Agents can bootstrap their own testing infrastructure, closing the eval loop autonomously
4. **Practical impact** — Production models from major AI labs (DeepSeek, Qwen, Gemma, Kimi, Stability AI) showed measurable throughput improvements

## Public Resources

Cursor released the optimized kernels as a public repository containing all 235 solutions. The work is notable for achieving what previously required teams of expert CUDA engineers over months — now accomplished by a multi-agent system in 3 weeks.

## Related Concepts

- [[concepts/harness-engineering]] — The multi-agent coordination pattern enabling autonomous optimization
- [[concepts/cursor-ide]] — The Cursor IDE platform that hosts the agent infrastructure
- [[concepts/ai-agent-engineering]] — Engineering patterns for autonomous agent execution and eval loops
- [[concepts/autonomous-component-optimization]] — The broader concept of self-improving systems

## References

- Cursor × NVIDIA, "Multi-Agent Kernel Optimization" (June 2026) → [[raw/articles/2026-06-05_cursor_multi-agent-kernels.md]]
