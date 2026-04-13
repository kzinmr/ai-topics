---
title: "gm8xx8"
handle: "@gm8xx8"
created: 2026-04-10
updated: 2026-04-14
tags: [person, ml-infrastructure, llm-serving, cuda, systems-research, linear-attention, farcaster, web3]
aliases: ["gm8xx8"]
---

# gm8xx8 (@gm8xx8)

| | |
|---|---|
| **X** | [@gm8xx8](https://x.com/gm8xx8) |
| **Farcaster** | [gm8xx8](https://warpcast.com/gm8xx8) (132K followers) |
| **GitHub** | [gm8xx8](https://github.com/gm8xx8) |
| **HuggingFace** | [gm8xx8](https://huggingface.co/gm8xx8) |
| **ENS** | gm8xx8.eth |
| **Lens** | gm8xx8.lens |
| **Role** | AI Infrastructure Researcher / Systems Engineer |
| **Known for** | cuLA (CUDA linear attention kernels), amplifying frontier ML systems research, active contributor across 10+ OSS projects |
| **Bio** | Prolific open-source contributor and ML systems analyst with ~7K followers on X and 132K on Farcaster. Works at the intersection of attention mechanism alternatives, GPU kernel optimization, and LLM serving efficiency. Known for surfacing cutting-edge systems research and providing technical analysis that bridges theory and practice. |

## Overview

**gm8xx8** is a prominent voice in the AI infrastructure and systems research community, operating across X (formerly Twitter), Farcaster, and GitHub. Despite maintaining a pseudonymous identity — no public personal website or real name disclosure — gm8xx8 has established themselves as a critical node in the ML systems information network through a consistent pattern of:

1. **Amplifying frontier research** — surfacing and analyzing papers on attention alternatives, KV cache optimization, and inference efficiency
2. **Hands-on contributions** — active GitHub contributor to 10+ projects spanning CUDA kernels, evaluation frameworks, agent infrastructure, and robotics
3. **Technical discourse** — engaging in detailed debates about reproducibility, novelty, and practical impact of ML systems research

Their follower count discrepancy (~7K on X vs. 132K on Farcaster) suggests they may be more actively engaged in the decentralized social/crypto-AI community, where they maintain ENS and Lens identities.

## Core Philosophy

### Efficiency as First-Class Constraint

gm8xx8's activity reveals a consistent philosophical thread: **the bottleneck in AI progress is not model capability but systems efficiency**. This manifests across several dimensions:

- **Attention alternatives**: Regular engagement with non-quadratic attention mechanisms (FFT-based, linear attention, state space models) reflects a belief that O(n²) self-attention is fundamentally unsustainable for long-context LLMs
- **Hardware-aware design**: Contributions to cuLA targeting specific GPU architectures (Blackwell SM10X, Hopper SM90) show a conviction that kernel-level optimization, not just algorithmic improvement, is essential
- **Memory systems focus**: Amplification of HCache (KV cache state restoration) and engagement with CXL (Compute Express Link) research indicate deep interest in the memory hierarchy as the primary bottleneck for LLM serving

### The "Practitioner-Researcher" Model

gm8xx8 embodies the pattern Karpathy identified: rather than purely theorizing or purely implementing, they operate at the boundary — reading papers, providing technical analysis, then contributing code to make the ideas practical. As evidenced by their pattern: *"surfacing a paper → sparking community discussion → contributing to related implementations."*

> *"Physics strikes back, same as it did with stable diffusion."* — gm8xx8's framing of the FFT attention paper, connecting theoretical physics concepts to practical ML breakthroughs.

This quote reveals a worldview grounded in **first principles** — seeing ML efficiency gains not as incremental engineering but as rediscoveries of fundamental mathematical and physical properties that had been overlooked in the rush toward transformer dominance.

## Key Contributions

### cuLA (CUDA Linear Attention) — InclusionAI/Ant Group

The most significant project gm8xx8 contributes to. **cuLA** provides hand-tuned CUDA kernels for linear attention variants (GDA, GDN, Lightning Attention) targeting NVIDIA Blackwell (SM10X) and Hopper (SM90) GPUs.

| Aspect | Detail |
|---|---|
| **Purpose** | Drop-in replacement for flash-linear-attention (FLA) with one-line import change |
| **Target Hardware** | NVIDIA Blackwell SM10X, Hopper SM90 |
| **Technologies** | CuTe DSL, CUTLASS C++, TMA-accelerated kernels |
| **Integration** | SGLang PR #22107 — KDA prefill backend achieving 0.895 GSM8K score on Kimi-Linear-48B |
| **Status** | Early stage (v0.1.0, April 2026); decode kernel not yet implemented |
| **Stars** | 318+ |

The cuLA contribution is significant because it represents the **practical realization** of the theoretical efficiency work gm8xx8 amplifies: moving from papers about linear attention to production-grade CUDA kernels that can actually replace transformers in serving systems.

### MiroMindAI Ecosystem

gm8xx8 contributes across multiple projects in the MiroMindAI (Singapore-based deep research company) ecosystem:

| Project | Description | gm8xx8's Role |
|---|---|---|
| **MiroEval** | Benchmark for deep research agents (100 tasks, 70 text + 30 multimodal) across 13 systems | Contributor |
| **trace-blame** | Go CLI for analyzing PyTorch Profiler traces — reimplementation of Meta's HolisticTraceAnalysis optimized for agent use | Contributor |
| **MiroRL** | MCP-first RL framework for deep research agents | Contributor |
| **MiroThinker** | Deep research agent (88.2 on BrowseComp) | Ecosystem participant |

The trace-blame project is particularly notable: it rewrites Meta's HolisticTraceAnalysis as a single Go binary with SQLite intermediate state, explicitly designed for **agent consumption** — including `install-skill` support for Claude Code and similar agents. This reflects gm8xx8's interest in making ML infrastructure **agent-native**.

### Other Notable Contributions

| Project | Organization | Description |
|---|---|---|
| **cap-x** | CapGym (NVIDIA/UC Berkeley/Stanford) | Framework for benchmarking coding agents in robot manipulation |
| **GLM-skills** | ZAI Organization | Skills framework for GLM models |
| **DIAL** | XPeng Robotics | Dialogue and interaction learning for robotics |
| **MyPhoneBench** | FreedomIntelligence | Mobile device AI benchmarking |
| **varex-bench** | UDI Barzilai | Variational reasoning benchmark |
| **Bonsai-demo** | PrismML Engineering | Demo infrastructure |
| **florence2_ros2_wrapper** | J.E. Dominguez Vidal | ROS2 integration for Florence-2 vision model |

This breadth — from CUDA kernels to robot manipulation benchmarks to mobile AI — suggests a **generalist systems engineer** comfortable working across the full stack from silicon to application.

## Research Amplification & Analysis

gm8xx8 serves as a critical information filter and synthesizer for the ML systems community. Their X posts consistently achieve high engagement:

| Date | Topic | Engagement | Significance |
|---|---|---|---|
| Feb 2025 | "The FFT Strikes Back" (arXiv:2502.18394) | 52K views, 676 likes, 72 reposts | Sparked community-wide debate on frequency-domain attention vs. FNet (2021) |
| Sep 2025 | HCache (arXiv:2410.05004) — Fast State Restoration | 553 likes | Highlighted KV cache management as the bottleneck for LLM serving |
| Mar 2026 | M2RNN paper (arXiv:2603.14360) by Mishra, Tan, Stoica, Gonzalez, Dao | Upvoted on HF | Matrix-valued RNN states for scalable LM — alternative to transformers |
| Mar 2026 | GDN models (open-lm-engine) | Liked 13 models | Gated Delta Networks — linear attention variant |
| Apr 2026 | Tina: Tiny Reasoning Models via LoRA | 9K views, 180 likes | LoRA-RL on 1.5B models achieving +20% gains at $9 total cost |
| Apr 2026 | LLM Knowledge Boundary Cognition | 3K views, 67 likes | How LLMs distinguish known from unknown across languages |

### Pattern: The "Signal Filter" Role

gm8xx8's research amplification follows a consistent pattern:

1. **Surface** — Share arXiv paper with minimal framing
2. **Engage** — Participate in technical discussion in replies
3. **Validate** — Like/upvote related models, collections, and implementations
4. **Contribute** — If the idea has legs, contribute to implementation (as with cuLA)

This "signal filter" role is valuable because the ML research ecosystem produces far more papers than any single practitioner can evaluate. gm8xx8's judgment — *"this paper is worth attention"* — carries weight due to their demonstrated ability to connect theory to implementation.

## HuggingFace Activity Analysis

gm8xx8's HuggingFace activity (77K+ score, though only 6 followers and no public models/datasets) reveals their interests through curation:

### Recent Model Likes (March–April 2026)
- **M2RNN family** (open-lm-engine): 14 models spanning 400M dense to 7B MoE variants
- **GDN models**: Gated Delta Networks at 400M and 7B scales
- **Hybrid architectures**: hybrid-gdn-m2rnn, hybrid-m2rnn configurations
- **LongCat-Flash-Prover** (meituan-longcat): 561B parameter model
- **LongCat-Next** (meituan-longcat): Next generation
- **Nemotron-Personas-France** (nvidia): 1M synthetic personas

### Paper Upvotes
- **V₀.₅: Generalist Value Model** — Sparse RL rollouts
- **GLM-OCR Technical Report** — OCR capabilities
- **InternAgent-1.5** — Unified agentic framework for autonomous scientific discovery
- **Training Foundation Models on Full-Stack AMD Platform** — Compute, networking, and system design

### Collections Upvoted
- **M2RNN Collection** — Complete model family
- **InternAgent Collection** — AI+X research across domains
- **Dr.Kernel Collection** — Kernel optimization
- **LateOn-Code** — Late interaction code retrieval models
- **OpenEarthAgent** — Geospatial reasoning
- **GLiClass-Instruct** — Zero-shot sequence classification

This activity pattern confirms gm8xx8's focus on **efficiency-first architectures** — non-transformer models, kernel-level optimization, and agent-capable systems.

## X Activity Themes

| Theme | Description | Evidence |
|---|---|---|
| **Attention mechanism alternatives** | FFT-based, linear, kernelized, delta-rule | FFT paper, cuLA, M2RNN engagement |
| **LLM serving optimization** | KV cache, state restoration, inference efficiency | HCache, CXL, memory system posts |
| **CUDA/GPU programming** | Kernel optimization, Blackwell/Hopper, CuTe DSL | cuLA contributions |
| **Reasoning models** | Small models with RL achieving outsized performance | Tina ($9 training cost), knowledge boundaries |
| **Agent infrastructure** | MCP, evaluation, tool use | MiroMindAI contributions, InternAgent |
| **Robotics & multimodal** | Vision-language-action models, mobile benchmarks | cap-x, DIAL, MyPhoneBench |
| **Community technical discussion** | Reproducibility, novelty, practical impact | Engages with @MrCatid, @SergioGaitanC |

## Related People

- **[xjdr](./xjdr.md)** — Works on inference optimization (Entropix); gm8xx8's interest in attention efficiency complements this
- **[Grad](./grad.md)** — Both contribute to ML efficiency/speedrun community
- **[Shiwei Gao, Youmin Chen, Jiwu Shu](https://arxiv.org/abs/2410.05004)** — Tsinghua HCache authors whose work gm8xx8 amplified
- **[@MrCatid](https://x.com/MrCatid)** — Frequent interlocutor on technical analysis of attention papers; questioned FFT paper reproducibility
- **[@karpathy](https://x.com/karpathy)** — gm8xx8 engages with the llm.c / modded-nanogpt ecosystem
- **Keller Jordan** — Modded-nanogpt speedrun; shares ML efficiency community
- **@fernbear.bsky.social** — NanoGPT speedrun contributor; related optimization community
- **Chaofan Yu (InclusionAI)** — cuLA lead; contact: chaofanyu@gmail.com
- **Max Fu (NVIDIA/UC Berkeley)** — cap-x lead author; robot manipulation benchmarking
- **Boris Cherny** — Both work on agent infrastructure; gm8xx8 contributes to GLM-skills while Cherny works on Claude Agent SDK

## Concepts

- [[linear-attention]] — cuLA implements KDA, GDN, Lightning Attention kernels
- [[kv-cache-optimization]] — HCache amplification, CXL memory interconnects
- [[cuda-kernel-optimization]] — CuTe DSL, CUTLASS, TMA-accelerated kernels
- [[m2rnn]] — Matrix-valued RNN states as transformer alternative
- [[agent-evaluation]] — MiroEval benchmark, process-centric assessment
- [[harness-engineering]] — trace-blame as agent-skill infrastructure

## Timeline

| Date | Event |
|---|---|
| Aug 2022 | GitHub account created (joined: 2022-08-20) |
| Dec 2021 | ENS domain gm8xx8.eth registered |
| Nov 2023 | Farcaster account created (now 132K followers) |
| Feb 2025 | Amplified "FFT Strikes Back" paper — 52K views, 676 likes |
| Sep 2025 | Amplified HCache paper on KV cache state restoration |
| Mar 2026 | Began contributing to InclusionAI/cuLA, MiroMindAI ecosystem |
| Mar 2026 | Active in open-lm-engine M2RNN/GDN model evaluation (liked 13 models) |
| Apr 2026 | cuLA v0.1.0 released; SGLang integration PR #22107 |
