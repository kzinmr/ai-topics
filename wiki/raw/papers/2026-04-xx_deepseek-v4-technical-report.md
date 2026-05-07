---
title: "DeepSeek-V4 Technical Report: Towards Highly Efficient Million-Token Context Intelligence"
source: "DeepSeek-AI"
url: "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf"
date: 2026-04
type: technical-report
tags: [deepseek, mixture-of-experts, long-context, hybrid-attention, fp4, speculative-decoding, agent]
---

# DeepSeek-V4 Technical Report

## Summary

DeepSeek-V4 is a series of highly efficient MoE models with 1M-token context: **V4-Pro** (1.6T/49B active) and **V4-Flash** (284B/13B active). Key innovations: Hybrid Attention (CSA+HCA+SWA), Manifold-Constrained Hyper-Connections (mHC), Muon Optimizer, MegaMoE Expert Parallelism, TileLang DSL, On-Policy Distillation, FP4 QAT, Interleaved Thinking.

## Key Innovations

### Hybrid Attention (CSA + HCA + SWA)
- **CSA (Compressed Sparse Attention)**: KV cache compressed by factor m (typically 4), queries attend only to top-k compressed entries via DeepSeek Sparse Attention (DSA)
- **HCA (Heavily Compressed Attention)**: Compression rate m' up to 128, maintains dense attention
- **SWA (Sliding Window Attention)**: Window size 128, preserves local fine-grained dependencies

### Manifold-Constrained Hyper-Connections (mHC)
Upgrades residual connections by constraining mapping onto doubly stochastic matrices. Spectral norm bounded by 1 → increased numerical stability.

### Muon Optimizer
Replaces AdamW for most modules. Uses Hybrid Newton-Schulz Iterations for orthogonalization. Faster convergence, improved stability.

## Training Infrastructure
- **32T+ tokens** pre-training
- **Anticipatory Routing**: Decouples backbone/routing updates using historical parameters θ_{t-Δt} to prevent loss spikes
- **SwiGLU Clamping**: Clamps linear component to [-10, 10] to eliminate outliers
- **MegaMoE**: Fine-grained Expert Parallelism — fuses communication and computation into single pipelined kernel. 1 GBps interconnect bandwidth hides communication for 6.1 TFLOP/s compute
- **TileLang DSL**: Fused kernel development. Host codegen reduces CPU overhead from hundreds of μs to <1μs. Deterministic kernels ensure bitwise reproducibility

## Efficiency (vs V3.2 at 1M context)
| Metric | V4-Pro | V4-Flash |
|--------|--------|----------|
| Single-Token FLOPs | 27% (3.7x lower) | 10% (10x lower) |
| KV Cache Size | 10% (10x smaller) | 7% (14x smaller) |

## Post-Training
1. **Specialist Training**: Domain-specific experts (Math, Code, Agent) via SFT + GRPO
2. **On-Policy Distillation (OPD)**: Student learns from full-vocabulary logit distributions of multiple teacher experts
3. **Interleaved Thinking**: Reasoning traces preserved across user message boundaries in tool-calling
4. **FP4 QAT**: FP4 precision for MoE expert weights and CSA indexer path

## Benchmarks (V4-Pro-Max)
- **Codeforces**: 3206 rating (23rd among humans)
- **Knowledge**: SimpleQA 57.9%, Chinese-SimpleQA 84.4%
- **White-Collar Tasks**: 63% non-loss rate vs Claude Opus 4.6
- **Code Agents**: 67% pass rate (Claude Opus 4.5: 70%)
- **Chinese Writing**: 62.7% win rate vs Gemini-3.1-Pro
