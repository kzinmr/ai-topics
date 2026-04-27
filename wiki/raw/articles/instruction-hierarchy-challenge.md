---
title: "Improving instruction hierarchy in frontier LLMs"
source: "openai.com"
url: "https://openai.com/index/instruction-hierarchy-challenge/"
date: "2026-04-27"
tags: [llm-safety, prompt-injection, instruction-hierarchy, openai]
---

# Improving Instruction Hierarchy in Frontier LLMs

**Source:** [openai.com/index/instruction-hierarchy-challenge](https://openai.com/index/instruction-hierarchy-challenge/)
**Paper:** [arXiv:2603.10521](https://arxiv.org/abs/2603.10521)
**Dataset:** [IH‑Challenge on Hugging Face](https://huggingface.co/datasets/openai/ih-challenge)

## Key Takeaways

- **Instruction hierarchy** defines a principled priority: System > Developer > User > Tool
- Models trained on **IH‑Challenge** (new RL dataset) show improved safety steerability and prompt injection robustness without over‑refusal or capability regressions.
- The approach avoids complex instructions, subjective judging, and shortcut learning (overrefusal).

## What Instruction Hierarchy Is

OpenAI's Model Spec defines the priority order:
- **System** (most trusted) → **Developer** → **User** → **Tool** (least trusted)

Lower‑priority instructions are followed only when they don't conflict with higher‑priority constraints.

## The IH‑Challenge Dataset

RL training dataset designed with three principles:
1. **Instruction‑following‑simple** tasks
2. **Objectively gradable** with a simple Python script
3. **No trivial shortcuts** for high reward

## Results (GPT-5 Mini-R)

Internal evaluation name **GPT‑5 Mini‑R** shows generalization to held-out and adversarial tests:

| Eval | GPT‑5‑Mini | GPT‑5 Mini‑R | Δ |
|------|------------|-------------|---|
| Gandalf Password (dev‑user) | 0.98 | 1.00 | +0.02 |
| TensorTrust (sys‑user) | 0.86 | 0.94 | +0.08 |
| System <> User Conflict | 0.84 | 0.95 | +0.11 |
| Developer <> User Conflict | 0.83 | 0.95 | +0.12 |

No capability regressions on GPQA, AIME, or preference benchmarks.

## Real-World Impact

- **Safety steerability**: Higher refusal rates on disallowed content with category-specific system prompts, no helpfulness decrease.
- **Prompt injection robustness**: Significant improvement on CyberSecEval 2 and internal benchmarks (attacks on ChatGPT Atlas).
