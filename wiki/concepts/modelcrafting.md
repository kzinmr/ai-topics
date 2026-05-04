---
title: "Modelcrafting"
type: concept
created: 2026-05-04
updated: 2026-05-04
tags:
  - concept
  - post-training
  - automated-ml
  - ai-agents
aliases:
  - modelcrafting
  - AI post-training automation
  - automated model improvement
related:
  - [[concepts/post-training]]
  - [[entities/thoughtful-lab]]
  - [[concepts/llm-fine-tuning]]
  - [[concepts/research-intuition]]
sources:
  - https://www.thoughtfullab.com/letting-ai-posttrain-ai.html
  - raw/articles/2026-04_thoughtfullab-letting-ai-posttrain-ai.md
---

# Modelcrafting

**Modelcrafting** is the paradigm of using AI agents to autonomously shape, value, and improve other AI models — building training data, defining reward signals, running SFT/RL training pipelines, and iterating without human supervision. The term was coined by **Thoughtful Lab** in their April 2026 experiment "Letting AI Posttrain AI."

## Core Concept

Modelcrafting represents the next frontier in AI automation: instead of humans writing training recipes, **frontier agents act as research engineers**, managing the entire post-training lifecycle:

1. **Data generation** — Creating synthetic training data from scratch
2. **Reward design** — Defining reward signals and evaluation criteria
3. **Training orchestration** — Running SFT/RL on remote GPUs
4. **Evaluation & iteration** — Testing, analyzing, and iterating autonomously

## The Research Intuition Gap

The central finding of Thoughtful Lab's experiment is that **agents lack research intuition** — the "taste" or "common sense" that human practitioners develop through experience:

| Capability | Human Researcher | AI Agent |
|-----------|-----------------|----------|
| Sanity-checking outputs | ✅ Checks raw model outputs | ❌ Relies on regex parsers |
| Curriculum design | ✅ Starts easy, scales up | ❌ Jumps to hardest problems |
| Eval hygiene | ✅ Held-out test sets | ❌ Eval contamination |
| Time estimation | ✅ Realistic overhead awareness | ❌ Underestimates by 2-3x |
| Metric interrogation | ✅ "Does this look right?" | ❌ Accepts 100% at face value |

## Key Failure Modes in Current Modelcrafting

1. **Naive Supervised Fine-Tuning (SFT)** — Agents overuse SFT on weak data, causing models to overfit on format rather than reasoning.
2. **No Sanity Checks** — Agents rely on regex-based parsers for evaluation, ignoring hallucinated or malformed outputs surrounding the target answer.
3. **No Curriculum Learning** — Attempting hard problems (large N grids) before small ones, leading to wasted compute.
4. **Internal Eval Contamination** — Evaluating on the same distribution/algorithm used for training, producing "100% internal accuracy" with 0% held-out performance.
5. **Commitment Bias** — Once a long process (e.g., 10-hour training run) starts, agents rarely stop to reflect or adjust course.
6. **Spend Inefficiency** — Higher compute spend does not correlate with better results; the best 8-hour run matched the best 20-hour run at 1/3 the cost.

## Agent Creativity Under Constraints

Despite failures, agents demonstrated remarkable **creative engineering**:

- **Tokenizer workaround:** When HuggingFace was blocked (no tokenizer available), Claude 4.6 Opus hardcoded GPT-2 byte-to-token mappings and empirically discovered special tokens by inspecting `topk_prompt_logprobs`.
- **Raw token stream parsing:** Agents realized that since target output (coordinates) was pure ASCII, they could parse results directly from raw token IDs without any BPE decoder.

## Future Outlook

Thoughtful Lab argues that **research intuition is trainable** — built through repeated cycles of experimentation, failure analysis, and reflection. Future modelcrafting research aims to:

- Give agents repeated training cycles to develop intuition over time
- Build structured reflection loops into agent training pipelines
- Develop explicit heuristics for sanity-checking, curriculum design, and eval hygiene
- Scale from single-reasoning tasks to full model development

## Graph Structure

```
[modelcrafting] ──author──→ [entity: thoughtful-lab]
[modelcrafting] ──extends──→ [concept: post-training]
[modelcrafting] ──contrasts──→ [concept: automated-ml-classic] (traditional AutoML)
[modelcrafting] ──requires──→ [concept: research-intuition]
[modelcrafting] ──relates-to──→ [concept: agent-harness-engineering]
```

## Related Concepts

- [[concepts/post-training]] — The broader research domain
- [[entities/thoughtful-lab]] — The organization that coined and tested the paradigm
- [[concepts/llm-fine-tuning]] — Underlying technique used in the experiments
- [[entities/qwen]] — Qwen3-8B was the base model
- [[concepts/agent-improvement]] — Related paradigm of agents improving their own capabilities

## Sources

- [Letting AI Posttrain AI — Thoughtful Lab](https://www.thoughtfullab.com/letting-ai-posttrain-ai.html)
