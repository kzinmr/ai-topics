---
title: "AXPO (Agent eXplorative Policy Optimization)"
created: 2026-05-31
updated: 2026-05-31
type: concept
tags:
  - reinforcement-learning
  - training
  - tool
  - optimization
  - qwen
sources:
  - https://arxiv.org/abs/2605.28774
---

# AXPO (Agent eXplorative Policy Optimization)

**AXPO** (Agent eXplorative Policy Optimization) is a reinforcement learning method for multimodal agentic reasoning, developed by researchers at [[entities/nvidia|NVIDIA]] and [[entities/kaist|KAIST]], published May 27, 2026 (arXiv:2605.28774).

## The Thinking-Acting Gap

AXPO identifies a fundamental asymmetry in agentic reasoning systems:

- **Thinking** (internal reasoning): the self-contained default, highly reliable
- **Tool use** (external actions): a high-variance auxiliary, frequently failing

Under standard RL recipes like [[concepts/post-training/grpo|GRPO]], this gap manifests as:
1. Tool use attempted on only ~30% of rollouts
2. When attempted, tool-using rollouts are all-wrong on ~40% of questions
3. This suppresses the learning signal precisely at the tool calls that need it most

## How AXPO Works

AXPO restructures the rollout distribution at the locus of the Thinking-Acting Gap:

1. **Tool-call resampling**: For all-wrong tool-using subgroups, AXPO fixes the thinking prefix and resamples only the tool call + continuation
2. **Uncertainty-based prefix selection**: Ranks candidates by mean policy probability over tool-call tokens, resampling lowest-confidence prefixes first
3. **Decomposed advantage calculation**: Prevents gradient conflict between failed source rollouts and successful resamples

## Results

Evaluated on [[entities/qwen|Qwen3-VL-Thinking]] models at 2B/4B/8B scales across 9 multimodal benchmarks:

- SFT+AXPO outperforms SFT+GRPO by +1.8pp on both Pass@1 and Pass@4 (8B average)
- **8B with AXPO surpasses 32B Base on Pass@4 with 4x fewer parameters**
- Tool usage rate recovers while accuracy climbs simultaneously
- Avoids the "tool collapse" problem where GRPO-trained models stop using tools

## Significance

AXPO demonstrates that targeted resampling at the point of failure is more effective than increasing total compute budget. By concentrating exploration exactly where the learning signal is being suppressed (tool calls), AXPO achieves outsized gains from a small extra rollout budget.

## Related Pages
- [[concepts/post-training/grpo]] — Group Relative Policy Optimization, baseline RL method
- [[concepts/tool-use-necessity]] — Tool necessity detection from hidden states
- [[concepts/qwen]] — Qwen3-VL model family used for evaluation
- [[entities/nvidia]] — NVIDIA, co-developer of AXPO
