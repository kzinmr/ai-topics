---
title: "Nemotron 3 Ultra (NVIDIA)"
created: "2026-06-06"
updated: "2026-06-06"
type: concept
tags: [model, open-source, mixture-of-experts, moe, frontier-models, nvidia, reasoning, coding-agents, hybrid-architecture]
sources:
  - "raw/articles/2026-06-05_fireworks-ai_nemotron-3-ultra.md"
  - https://fireworks.ai/blog/nemotron-3-ultra
  - https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf
---

# Nemotron 3 Ultra

Nemotron 3 Ultra is NVIDIA's open frontier reasoning and orchestration model, designed specifically for long-running autonomous agents. Released June 4, 2026, it uses a hybrid **Transformer-Mamba Mixture of Experts (MoE)** architecture — 550B total parameters with 55B active per token — and supports up to 1M token context windows.

## Architecture

| Property | Value |
|----------|-------|
| **Total parameters** | 550B |
| **Active parameters** | 55B per token |
| **Architecture** | Hybrid Transformer-Mamba MoE |
| **Context window** | Up to 1M tokens |
| **License** | Open model |
| **Inference speed** | 5× faster than comparable open models (NVIDIA claim) |
| **Cost efficiency** | Up to 30% lower cost for agentic tasks |

The hybrid Mamba-Transformer design combines the efficiency of state-space models (Mamba) for long-context processing with the reasoning capabilities of Transformer attention, routed through a Mixture of Experts sparsity mechanism.

## Design Philosophy

Nemotron 3 Ultra was built specifically for **agentic workloads** — not single-prompt benchmarks. Key design decisions:

- **Unit of measurement is task completion cost**, not per-token cost: agents execute hundreds of steps (planning, tool calls, sub-agent spawning, error correction), so total task cost matters more than single-response latency
- **Optimized for orchestration**: designed as the orchestrator model in multi-component agent systems, coordinating sub-agents, tool selection, and error recovery
- **Fast inference for long runs**: 5× faster speeds mean agents iterate faster across hundreds of environment interactions

## Use Cases

- **Coding agents**: Multi-file software engineering, debugging, and PR generation
- **Deep research**: Multi-step investigation with web search, file analysis, and synthesis
- **Enterprise workflows**: Complex business process automation requiring tool use and judgment
- **Factory AI integration**: Factory (YC) uses Nemotron 3 Ultra as one of its model options for autonomous code generation in enterprise software factories

## Deployment

- Available on **Fireworks AI** with day-zero support on dedicated GPU deployments (B300, B200)
- Fireworks' FireAttention custom kernels provide up to 4× higher throughput while preserving quality
- Supports post-training (SFT, DPO) via LoRA or full-parameter training on the same platform
- Deployable with single-command on-demand GPU deployments, billed per GPU-second

## Comparison with Other Nemotron Models

| Model | Architecture | Active Params | Context | Focus |
|-------|-------------|---------------|---------|-------|
| Nemotron 3 Ultra | Transformer-Mamba MoE | 55B | 1M | Agentic reasoning |
| Nemotron-Nano 2VL | Vision-language | Small | — | Multimodal |
| Nemotron-Nano 3 | Dense | Small | — | Lightweight inference |

## Significance

Nemotron 3 Ultra represents NVIDIA's strategic entry into the open frontier reasoning model space, directly competing with DeepSeek V4, Qwen 3.6, and other open models optimized for long-running agent tasks. Its hybrid Mamba-Transformer design signals the growing adoption of non-transformer architectures in large-scale models, particularly for applications requiring efficient long-context processing.

## Related Pages

- [[entities/nvidia]] — NVIDIA entity
- [[concepts/mixture-of-experts]] — Mixture of Experts architecture
- [[concepts/mamba]] — Mamba state-space models
- [[concepts/agentic-loop]] — Agent execution cycles
- [[entities/fireworks-ai]] — Fireworks AI inference platform
- [[concepts/hybrid-architecture]] — Hybrid model architectures
