---
status: active
created: 2026-04-14
updated: 2026-04-17
tags: reasoning, models, thinking, coherence, hallucination
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

## Distinction from Neurosymbolic AI

Reasoning models use neural architectures with emergent or trained reasoning capabilities, while neurosymbolic AI combines neural networks with explicit symbolic logic systems. These are complementary approaches to improving AI reasoning.

## Key Figures & Projects

- **OpenAI o1/o3** — Reasoning models with hidden chain-of-thought
- **Anthropic Claude 3.x** — Extended thinking / process-based reasoning
- **DeepSeek R1** — Open-weight reasoning model via RL
- **Karpathy's analysis** — "illusion of thinking" critique on reasoning model behavior

## Related wikilinks

- [[concepts/neurosymbolic-ai]] — Alternative reasoning approach (symbolic + neural)
- [[concepts/ai-evals]] — How to evaluate reasoning quality
- [[concepts/illusion-of-thinking]] — Karpathy's critique (if page exists)

## Sources

- OpenAI o1 technical report
- Anthropic Claude reasoning analysis
- Karpathy blog posts on reasoning models
- DeepSeek R1 paper
