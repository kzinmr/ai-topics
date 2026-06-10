---
title: "Speed as a Scaling Law"
created: 2026-06-10
updated: 2026-06-10
type: concept
tags:
  - inference
  - scaling-laws
  - real-time
  - gpu
  - fused-kernels
  - test-time-scaling
sources:
  - raw/articles/2026-05-21_tilert_speed-as-the-next-scaling-law.md
  - raw/articles/2026-06-08_xiaomi-mimo-tilert-1000tps.md
  - raw/articles/2026-06-08_tilert_breaking-1000-tps.md
related:
  - "[[entities/tilert]]"
  - "[[entities/xiaomi-mimo]]"
  - "[[concepts/glm-5-1]]"
  - "[[concepts/test-time-compute]]"
---

# Speed as a Scaling Law

**Speed as a Scaling Law** is the thesis that inference latency is becoming a primary axis of AI system capability — as fundamental as model size, data, and compute. First articulated by the [[entities/tilert|TileRT]] team in their May 2026 blog post, it argues that as AI moves from chat to agentic to autonomous use cases, **execution speed directly defines the reasoning budget itself**.

## Three Eras of AI Inference

| Era | Period | Primary Value | Demand Driver | Economics |
|-----|--------|--------------|---------------|-----------|
| **Chat Era** | 2023–2024 | Model quality | "Is the answer good?" | value < cost |
| **Agentic Era** | 2025–now | Token throughput | "Can it process enough tokens?" | value ≈ cost |
| **Autonomous Era** | Next 2 years | **SPEED** | "Can it respond fast enough?" | value >> cost |

## Why Speed Matters

### 1. Speed Transmutes into Intelligence
Under fixed latency budgets, faster inference enables:
- More rollouts and deeper reasoning paths (Best-of-N, Tree Search)
- Stronger self-verification and error correction
- Parallel reasoning path exploration within the same wall-clock time

This is especially critical for [[concepts/test-time-compute|Test-Time Scaling]] — the practice of spending more compute at inference to improve output quality.

### 2. Agent Responsiveness
AI coding agents (Cursor, Claude Code, Codex) and tool-use agents require low-latency feedback loops. High latency breaks the interaction cadence and reduces developer productivity.

### 3. Real-Time Decision Loops
Trillion-parameter models entering time-critical scenarios:
- High-frequency quantitative trading signal generation
- Real-time anti-fraud interception
- Surgical assistance and medical imaging analysis
- Intelligent bidding systems

## The Execution Gap

Modern GPUs have enormous theoretical bandwidth (e.g., 8×H200 NVL: ~38 TB/s), but real inference systems deliver only a fraction of theoretical throughput. The gap is not in compute — it's in **execution orchestration**:

- Kernel launch latency
- Cross-kernel synchronization barriers
- Memory spills and round-trips
- Runtime scheduling overhead

Under latency-first workloads, kernel lifetimes collapse into the tens-of-microseconds regime, making these previously hidden overheads dominant.

## Technical Approaches

### Persistent Kernels
Instead of launching individual operators, compile the entire model into a single GPU-resident kernel that executes continuously. See [[entities/tilert|TileRT]].

### Speculative Decoding
Use a lightweight draft model to predict multiple tokens, then verify in parallel with the main model. Advanced variants like **DFlash** (block-level masked parallel prediction) eliminate the serial constraint of autoregressive drafting. See [[entities/xiaomi-mimo|MiMo-V2.5-Pro-UltraSpeed]].

### FP4 Quantization
Reduce parameter precision to 4-bit (MXFP4) for bandwidth-bound inference, selectively applied to high-tolerance components (MoE Experts).

### Heterogeneous GPU Specialization
Different GPUs assume different roles (e.g., sparse indexing vs. attention compute) rather than executing identical logic synchronously.

## Landmark Demonstrations

| System | Speed | Model Scale | Approach |
|--------|-------|-------------|----------|
| GLM-5.1-HighSpeed | 400 tok/s | 744B MoE | TileRT persistent kernels |
| MiMo-V2.5-Pro-UltraSpeed | 1000 tok/s | 1T MoE | TileRT + FP4 + DFlash |
| Cerebras | ~1800 tok/s | Llama 3.1 70B | Wafer-scale hardware |
| Groq | ~750 tok/s | Llama 3.1 70B | Pure SRAM LPU |

## Key Insight

> "Speed is no longer just a systems metric. It is increasingly becoming part of the reasoning budget itself." — TileRT Team

The implication: inference speed is not merely a quality-of-service parameter. It directly determines:
- Reasoning depth (how many paths can be explored)
- Interaction quality (real-time vs. batch)
- Agent responsiveness (tool-call latency)
- Real-world productivity (time-to-completion)

## Related Concepts
- [[concepts/test-time-compute]] — Spending more compute at inference time
- [[concepts/speculative-decoding]] — Draft-then-verify parallel token generation
- [[concepts/persistent-kernel]] — GPU-resident execution model
