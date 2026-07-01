---
title: "Together AI at ICML 2026: frontier research across the full stack"
date: 2026-06-30
type: raw_article
sources:
  - https://www.together.ai/blog/icml-2026
source: web-extract
---
# Together AI at ICML 2026: Frontier Research Across the Full Stack

**Date:** June 30, 2026
**Conference:** ICML 2026, Seoul

## Overview

Together AI presented nine accepted papers at ICML 2026, spanning the full AI stack from agents at the top to kernels at the bottom. The research is organized by where it sits in the stack.

## Papers by Layer

### Layer 1: Agents (Top of Stack)
1. **DSGym: A Holistic Framework for Evaluating and Training Data Science Agents**
   - 1,000+ data-science tasks across 10+ domains
   - Unified evaluation and training API
   - Self-contained execution environments
   - Authors: Fan Nie, Junlin Wang, Harper Hua, Federico Bianchi, et al. (with Stanford, Duke, Harvard)

2. **ThunderAgent: A Simple, Fast and Program-Aware Agentic Inference System**
   - 1.5–3.6× higher serving throughput for agent workloads
   - Three lines of code to adopt
   - Makes the inference engine "agent-aware" — recognizes multi-turn agent workflows
   - Fixes up to 7.14× latency inflation under load
   - Authors: Hao Kang, Ziyang Li, et al. (with Georgia Tech, CMU, UIUC)

### Layer 2: Reasoning & Training
3. **TTT-Discover: Learning to Discover at Test Time**
   - SOTA discoveries across math, GPU kernels, algorithms, biology — with open 120B model
   - RL at test time on single problems, not search over frozen models
   - Authors: Mert Yuksekgonul, Daniel Koceja, et al. (with Stanford, NVIDIA, UCSD)

4. **RARO: Escaping the Verifier — Learning to Reason via Demonstrations**
   - 25% win rate vs 5.9% for SFT, with no verifier
   - RL-grade reasoning on tasks without checkers (poetry, financial analysis)

### Layer 3: Inference Optimization
5. **Opportunistic Expert Activation** — MoE decode optimization
6. **Speculative Decoding** — Adaptive to live traffic, cutting per-token costs
7. **KV Cache & Context** — Longer context, bigger batches, faster MoE decode

### Layer 4: Kernels & Hardware (Bottom)
8-9. Kernel-level optimizations turning raw hardware into usable speed

## Production Impact
- 31% more TPS than next-fastest OSS engine for production coding agent workloads
- 40+ models chosen for production on Together platform
- B200 GPUs now available on-demand via Together GPU Clusters
