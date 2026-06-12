---
title: "Instruction Hierarchy"
type: concept
created: 2026-04-30
updated: 2026-05-27
tags:
  - agent-safety
  - openai
sources: []
---

# Instruction Hierarchy

The **Instruction Hierarchy** for large language models is a framework that defines the priority of instructions from different sources. Systematic research was conducted using OpenAI's IH-Challenge benchmark.

## Definition

Priority order defined by the OpenAI Model Spec:

| Priority | Source | Trust Level |
|--------|--------|--------|
| 1 (Highest) | System | Most Trusted |
| 2 | Developer | High Trust |
| 3 | User | Medium |
| 4 (Lowest) | Tool | Least Trusted |

Lower-priority instructions are not followed when they conflict with higher-priority constraints. This design improves resistance to prompt injection.

## IH-Challenge

RL training dataset released by OpenAI in April 2026. Design principles:

1. **Instruction-following-simple** — Simply evaluates instruction fidelity
2. **Objectively gradable** — Evaluable with Python scripts alone
3. **No trivial shortcuts** — No easy workarounds to obtain high rewards

**GPT-5 Mini-R** results:

| Evaluation | GPT-5-Mini | GPT-5 Mini-R | Δ |
|------|------------|--------------|---|
| Gandalf Password (dev-user) | 0.98 | 1.00 | +0.02 |
| TensorTrust (sys-user) | 0.86 | 0.94 | +0.08 |
| System <> User Conflict | 0.84 | 0.95 | +0.11 |
| Developer <> User Conflict | 0.83 | 0.95 | +0.12 |

No capability degradation (verified with GPQA, AIME, and preference benchmarks).

## Advantages

- **Safety steerability**: Improves refusal rates via category-specific system prompts, no decrease in helpfulness
- **Prompt injection robustness**: Significant improvements on CyberSecEval 2, etc.
- **Overrefusal avoidance**: No complex instructions or subjective judgments required

## Limitations

- OpenAI proprietary implementation
- Compatibility with other models not verified
- Relies on known attacks like "Gandalf"

## Related

- [[concepts/prompt-injection]]
- [[concepts/post-training/rlhf]]
- [[concepts/chain-of-thought]]
- [[entities/openai]] — Developer
- [[concepts/gandalf]] — Vulnerability benchmark

## Sources

- [OpenAI — Improving instruction hierarchy in frontier LLMs](https://openai.com/index/instruction-hierarchy-challenge/) (Apr 2026)
- [arXiv:2603.10521 — Instruction Hierarchy Paper](https://arxiv.org/abs/2603.10521)
- [IH-Challenge on Hugging Face](https://huggingface.co/datasets/openai/ih-challenge)
- [openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md](../raw/articles/openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md)
