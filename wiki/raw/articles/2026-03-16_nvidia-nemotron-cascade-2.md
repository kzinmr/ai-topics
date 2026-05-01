# Nemotron-Cascade 2: Post-Training LLMs with Cascade RL and Multi-Domain On-Policy Distillation

**Source:** https://research.nvidia.com/labs/nemotron/nemotron-cascade-2/
**Published:** March 16, 2026
**Authors:** Zhuolin Yang, Zihan Liu, Yang Chen, Wenliang Dai, Boxin Wang, et al. (NVIDIA)

## Overview
Nemotron-Cascade 2 is an open-weight 30B Mixture-of-Experts (MoE) model with 3B active parameters per token. It focuses on "intelligence density" — achieving frontier-level reasoning at a fraction of the parameter scale.

Built on Nemotron-Nano-V3 base model, it uses Cascade RL (reinforcement learning) and Multi-Domain On-Policy Distillation for post-training.

## Key Results
- **Gold Medal performance** at IMO 2025, IOI 2025, and ICPC World Finals
- Reviewed and verified by an IMO 2015 gold medalist co-author
- Outperforms Qwen3.5-35B-A3B and Nemotron-3-Super-120B-A12B on math, code reasoning, alignment, and instruction following
- Improves on Nemotron-Nano-V3 on nearly every benchmark

## Technical Approach
1. SFT on meticulously curated dataset
2. Expanded Cascade RL covering broad spectrum of reasoning and agentic domains
3. Multi-Domain On-Policy Distillation: strongest intermediate teacher models for each domain distill knowledge efficiently, recovering benchmark regressions while sustaining gains

## Operating Modes
- **Thinking Mode:** `<think>` token activates deep reasoning for complex math/code
- **Non-Thinking Mode:** Empty `<think></think>` block for efficient direct responses
- **Tool Calling:** Structured `<tool_call>` tags for agentic workflows with verifiable execution

## Deployment
- 24GB VRAM, 256K context window
- Available via Ollama: `ollama run nemotron-cascade-2`
- Compatible with Claude Code, Codex, OpenCode, OpenClaw
- Open-weight release under NVIDIA Open Model License
