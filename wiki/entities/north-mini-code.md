---
title: North Mini Code
created: 2026-06-10
updated: 2026-06-10
type: entity
tags:
  - model
  - code-model
  - open-source
  - cohere
  - agentic-engineering
  - reinforcement-learning
  - rlvr
  - coding-agents
sources:
  - https://huggingface.co/blog/CohereLabs/introducing-north-mini-code
  - https://x.com/cohere/status/2064378058329526556
---

# North Mini Code

North Mini Code is Cohere's first open-source coding model, released June 9, 2026. A 30B-parameter sparse Mixture-of-Experts model with 3B active parameters, specifically designed and trained for agentic software engineering tasks. Available under Apache 2.0 license.

## Specifications

| Feature | Detail |
|---------|--------|
| Architecture | Sparse MoE, 30B total / 3B active |
| Experts | 128 experts, 8 activated per token |
| Attention | Interleaved sliding-window (RoPE) + global (no PE), 3:1 ratio |
| Activation | SwiGLU FFN, sigmoid router with top-k |
| Context | 128K tokens |
| License | Apache 2.0 |
| Weights | BF16 and FP8 (quantized) |

## Benchmarks

North Mini Code outperforms both same-size and substantially larger open-source models on Artificial Analysis' Coding Index (score: 33.4):

| Benchmark | North Mini Code | vs Competitors |
|-----------|----------------|----------------|
| AA Coding Index | 33.4 | Beats Qwen3.5 (35B-A3B), Gemma 4 (26B-A4B), Devstral Small 2 (24B Dense) |
| SWE-Bench Verified | pass@1 via SWE-Agent | Outperforms Nemotron 3 Super (120B), Mistral Small 4 (119B), Devstral 2 (123B) |
| Terminal-Bench v2 | pass@1 via ReAct/Harbor | Strong agentic terminal performance |
| SWE-Bench Verified (SFT, pass@10) | 80.2% | Before RLVR fine-tuning |
| Terminal-Bench v2 (SFT, pass@10) | 55.1% | Before RLVR fine-tuning |
| mini-SWE-Agent | 61.0% pass@1 | Cross-harness transfer (free improvement) |

## Training Pipeline

### Two-Stage SFT
1. **Stage 1** (64K context): Code 70% of tokens, 43% agentic tool-use, 27% competitive/scientific programming
2. **Stage 2** (128K context): 4.5B token mixture, code 61%, only agentic + reasoning-driven samples

"Long-to-longer" cascade approach — avoids 20B non-code tokens dominating 1.5B high-quality code data.

### Asynchronous RL (RLVR)
- **Algorithm**: CISPO (log-likelihood + token-level importance sampling correction, from MiniMax-M1)
- **Environments**: Terminal tasks (Harbor/Tmux) + SWE tasks (SWE-Agent)
- **Scale**: 512 rollouts/batch, 128K context, 70k+ verifiable tasks across ~5k repos
- **Async architecture**: Trainer + vLLM sidecar, windowed FIFO queue for stragglers
- **Gains**: +7.9% Terminal-Bench v2, +3.0% SWE-Bench absolute pass@1
- **Human eval**: 66.1% win rate vs SFT-only checkpoint (especially code editing tasks)

### Cross-Harness Robustness
Trained on multiple scaffolds (SWE-Agent, mini-SWE-Agent, OpenCode, Terminus 2) rather than optimizing for a single one. 6% cross-harness data yields 10% gain on OpenCode without degrading SWE-Agent performance.

## Availability

- **HuggingFace**: [CohereLabs/North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) (BF16), [CohereLabs/North-Mini-Code-1.0-fp8](https://huggingface.co/CohereLabs/North-Mini-Code-1.0-fp8)
- **Demo**: [North Mini Code Demo Space](https://huggingface.co/spaces/CohereLabs/North-Mini-Code-1.0)
- **Cohere API**
- **OpenCode** integration

## Significance

- Cohere's first model specifically for developers/coding
- First model in the "North" family — signals a new product line
- Demonstrates that small MoE models can compete with 4-40× larger dense models on agentic coding
- Cross-harness training is a differentiator — most competitors optimize for a single benchmark harness
- Apache 2.0 license aligns with Cohere's sovereign AI/open strategy

## Related Pages

- [[entities/cohere]] — Parent company
- [[entities/command-a-plus]] — Cohere's frontier general model (218B MoE)
- [[concepts/mixture-of-experts]] — MoE architecture
- [[concepts/ai-benchmarks/swe-bench]] — Key evaluation benchmark
- [[concepts/agentic-engineering]] — Agentic coding paradigm
- [[concepts/rlm]] — Reinforcement Learning from Execution Feedback (related RLVR approach)
