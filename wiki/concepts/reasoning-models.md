---
status: skeleton
created: 2026-04-14
tags: reasoning, models, thinking
---

# Reasoning Models

LLM architectures designed for explicit step-by-step reasoning, including chain-of-thought, process supervision, and test-time compute scaling.

## Key Points

- **o1-style reasoning**: Models that generate intermediate reasoning steps before producing answers
- **Process Reward Models (PRM)**: Evaluate individual reasoning steps rather than just final output
- **Test-time compute scaling**: Trading more inference compute for better accuracy
- **Chain-of-thought (CoT)**: Explicit reasoning trace generation
- **Self-correction**: Models that can revise their own reasoning

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
