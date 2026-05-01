---
title: Nemotron Cascade 2
created: 2026-05-01
updated: 2026-05-01
type: entity
tags: [model, open-source, nvidia, moe, local-llm, coding-agents, reasoning]
sources: [raw/articles/2026-03-16_nvidia-nemotron-cascade-2.md]
---

# Nemotron Cascade 2

NVIDIA's open-weight 30B Mixture-of-Experts (MoE) model with **3B active parameters per token**, released March 16, 2026. Focuses on "intelligence density" — achieving frontier-level reasoning at a fraction of the parameter scale. The second open-weight LLM to achieve **Gold Medal-level performance** at IMO 2025, IOI 2025, and ICPC World Finals.

Built on the Nemotron-Nano-V3 base model and post-trained using **Cascade RL** and **Multi-Domain On-Policy Distillation**.

## Architecture & Efficiency

- **30B total, 3B active per token** — 10× compute reduction vs dense 30B model
- 24GB VRAM, 256K context window
- Available via Ollama: `ollama run nemotron-cascade-2`
- Compatible with [[entities/claude-code]], [[concepts/openai-codex-superapp|Codex]], OpenCode, [[entities/openclaw]]

## Post-Training Pipeline

1. **SFT:** Meticulously curated dataset
2. **Cascade RL:** Expanded across broad spectrum of reasoning and agentic domains
3. **Multi-Domain On-Policy Distillation:** Strongest intermediate teacher models distill knowledge per domain, efficiently recovering benchmark regressions while sustaining performance gains

## Key Benchmarks

- Outperforms **Qwen3.5-35B-A3B** and **Nemotron-3-Super-120B-A12B** on math, code reasoning, alignment, and instruction following
- Gold-level IMO 2025 (verified by IMO 2015 gold medalist co-author)
- Improves on Nemotron-Nano-V3 on nearly every benchmark

## Operating Modes

- **Thinking Mode:** `<think>` token activates deep reasoning for complex math/code
- **Non-Thinking Mode:** Empty `<think></think>` block for efficient direct responses
- **Tool Calling:** Structured `<tool_call>` tags for agentic workflows with verifiable execution feedback

## Intelligence Density Thesis

Nemotron Cascade 2 embodies NVIDIA's thesis that **specialized reasoning capabilities once thought exclusive to frontier-scale models are achievable at 30B scale through domain-specific reinforcement learning**. This aligns with the broader industry shift from "bigger is better" to "smarter is faster."

By activating only 3B parameters per token, the model achieves competitive or superior results against models with 4-10× the active parameters, dramatically reducing inference cost while maintaining reasoning quality.

## Related
- [[entities/nvidia]] — parent company and broader model family
- [[concepts/mixture-of-experts]] — MoE architecture principles
- [[concepts/local-llm]] — local deployment landscape
- [[entities/gpt-oss]] — OpenAI's open-weight competitor
- [[entities/gemma-4]] — Google's open model family
- [[concepts/reasoning-models]] — reasoning capabilities in LLMs
