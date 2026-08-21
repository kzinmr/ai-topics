---
title: "Reasoning Models"
tags:
  - reasoning
  - model
  - evaluation
sources:
  - raw/papers/2025-04-14_2504.09762_stop-anthropomorphizing-intermediate-tokens.md
created: 2026-04-14
updated: 2026-08-21
type: concept
---

# Reasoning Models

LLM architectures designed for explicit step-by-step reasoning, including chain-of-thought, process supervision, and test-time compute scaling.

## Key Points

- **o1-style reasoning**: Models that generate intermediate reasoning steps before producing answers
- **Process Reward Models (PRM)**: Evaluate individual reasoning steps rather than just final output
- **Test-time compute scaling**: Trading more inference compute for better accuracy
- **Chain-of-thought (CoT)**: Explicit reasoning trace generation
- **Self-correction**: Models that can revise their own reasoning

## The Coherence Problem (2026-04)

Giles Thomas demonstrated that LLMs achieve syntactic coherence surprisingly early in training (~1/3 through), but **coherence ≠ correctness**. Full training is essential for factual grounding. This has direct implications for reasoning models: they can produce plausible-sounding reasoning traces that are factually wrong.

See: [[concepts/llm-training-coherence-evolution]]

## The Illusion Problem (2026-04)

The Signal newsletter covered three key angles on reasoning model hallucination:

1. **"The real danger of AI hallucination"** — Hallucination is a fundamental property of probabilistic models, not a bug
2. **"Your AI is lying to your face"** — Chain-of-thought is a performance, not transparent internal computation
3. **"Understanding Reasoning Models via Problem Complexity"** — Reasoning capability is problem-dependent, not universally improving with scale

See: [[concepts/illusion-of-thinking]]

## The Kambhampati Position: Stop Anthropomorphizing Thinking Traces (2025, trended Aug 2026)

A position paper by **Subbarao Kambhampati et al. (arXiv:2504.09762**, Arizona State University AI planning group) — which returned to the HN front page in August 2026 (250 pts) as products shipped user-visible "thinking" traces — argues that calling intermediate tokens "reasoning traces" or "thinking traces" is actively harmful:

- **No causal theory** links the semantics of intermediate tokens to the final solution; any human-readable meaning may be a spurious coincidence inherited from training data.
- **Counterexample — DeepSeek R1-Zero**: when DeepSeek fine-tuned R1-Zero (which emitted mixed English/Chinese intermediate tokens) onto curated English traces, solution accuracy **worsened** with no improvement in trace validity. Plausible-looking traces are not more valid traces.
- **Danger**: stylistically-plausible ersatz reasoning engenders **false user trust** in answers users cannot verify — "designing powerful AI systems that potentially exploit the cognitive flaws of users to convince them of the validity of incorrect answers."
- **Call to action**: stop using human interpretation of traces as a proxy for solution trustworthiness; trust should come from **verification of the solution itself** (verifiers, third parties). Free research to optimize intermediate tokens purely for accuracy — including **non-linguistic intermediate representations** (arbitrary embedding-space vectors).
- **Reframe — intermediate tokens as learned prompt augmentations**: for task T, an augmentation PA such that P(Sol(LLM(T+PA), T)) > P(Sol(LLM(T), T)); the LRM's job is learning the mapping T → PA, and the natural-language appearance of PA is incidental.

The paper complements the existing "illusion of thinking" critique (user-facing traces are a performance, not transparent computation) by attacking the *research methodology* that treats trace readability as a signal.

Source: [[raw/papers/2025-04-14_2504.09762_stop-anthropomorphizing-intermediate-tokens]] — [arXiv:2504.09762](https://arxiv.org/abs/2504.09762)

## Distinction from Neurosymbolic AI

Reasoning models use neural architectures with emergent or trained reasoning capabilities, while neurosymbolic AI combines neural networks with explicit symbolic logic systems. These are complementary approaches to improving AI reasoning.

## Key Figures & Projects

- **OpenAI o1/o3** — Reasoning models with hidden chain-of-thought
- **Anthropic Claude 3.x** — Extended thinking / process-based reasoning
- **DeepSeek R1** — Open-weight reasoning model via RL
- **Karpathy's analysis** — "illusion of thinking" critique on reasoning model behavior

## Related wikilinks

- [[concepts/neurosymbolic-ai]] — Alternative reasoning approach (symbolic + neural)
- [[concepts/evaluation/ai-evals]] — How to evaluate reasoning quality
- [[concepts/illusion-of-thinking]] — Karpathy's critique (if page exists)

## Sources

- OpenAI o1 technical report
- Anthropic Claude reasoning analysis
- Karpathy blog posts on reasoning models
- DeepSeek R1 paper
