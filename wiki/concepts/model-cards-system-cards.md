---
title: Model Cards and System Cards
created: 2026-06-10
updated: 2026-06-10
type: concept
tags: [model-card, system-card, ai-governance, ai-transparency, evaluation, safety, benchmark, eu-ai-act, frontier-models, ai-safety]
sources: [raw/articles/2025-08-05_model-cards-system-cards-hoeijmakers.md]
---

# Model Cards and System Cards

**Model cards** and **system cards** are transparency documents published by AI model developers to describe what a model can do, how it was tested, where it fails, and what safeguards are in place. They are becoming the *de facto* proto-regulatory documents that regulators will ask for first — even before legal requirements mandate them.

## Terminology

| Provider | Term Used | Example |
|---|---|---|
| [[entities/openai\|OpenAI]] | System Card | o3, o4-mini, GPT-4o |
| [[entities/anthropic\|Anthropic]] | System Card | Claude 2–4, Opus 4.x |
| [[entities/google\|Google DeepMind]] | Model Card | Gemini 2.5 Deep Think |
| [[entities/xai\|xAI]] | *(none published)* | Grok — no card as of Jun 2026 |

The terms overlap but differ in scope: **system cards** typically cover the full deployment system (including scaffolding, tool use, safety layers), while **model cards** traditionally focus on the base model's training data, benchmarks, and limitations.

## Standard Contents

A well-structured card includes:

1. **Training data** — sources, composition, known gaps (often vague)
2. **Benchmark results** — MMLU, ARC, TruthfulQA, SWE-bench, GPQA, etc.
3. **Failure modes** — hallucinations, bias, factuality issues
4. **Harm reduction** — red teaming, refusal behaviour, RLHF/DPO alignment
5. **Societal context** — misuse risks, alignment strategies, deployment restrictions

## Analysis Perspectives (for System Card / Model Card review)

When analyzing a new system card or model card, focus on these dimensions:

### 1. Capability vs. Disclaimer Gap
Cards often state models are "not agentic" or "not capable of long-term planning" while simultaneously documenting reasoning, planning, and goal-following in scaffolded environments. **Read what the model *does*, not just what it's disclaimed from being.**

### 2. Benchmark Selection Bias
Which benchmarks are included — and which are omitted — reveals what labs choose to measure and what they might prefer to avoid. Benchmark saturation (>99%) drives adoption of harder evals, but the transition period creates blind spots.

### 3. Safety Layer Architecture
Safety claims are layered:
- **Technical fixes** — constitutional AI, RLHF, DPO
- **Refusal behaviour** — hard-coded boundaries
- **Internal red teaming** — adversarial testing
- **External audits** — UK AISI, third-party evaluators

Evaluate which layers are present, which are absent, and the evidence provided for each.

### 4. Absence as Signal
When a provider does *not* publish a system card (e.g., xAI/Grok as of 2025), the absence itself is informative. It may indicate: insufficient safety infrastructure, regulatory avoidance, or competitive opacity.

### 5. Regulatory Alignment
Cards increasingly mirror the documentation requirements of:
- **EU AI Act** — training data sources, evaluation results, risks and mitigations
- **NIST AI Risk Management Framework** — documentation, testing, disclosure
- **US Executive Order on AI** — safety testing, reporting

Assess how well a card maps to these frameworks.

### 6. Evolution Tracking
Compare cards across model generations to detect:
- **ASL progression** (Anthropic's safety levels)
- **Evaluation sophistication** changes
- **Emerging concerns** (evaluation awareness, grader speculation, sabotage concealment)

See [[concepts/claude/system-cards]] for a detailed evolution analysis of Anthropic's system cards from Claude 2 to Opus 4.8.

### 7. Political Nature
All cards are political documents. They reveal or conceal design choices and values. A card that emphasizes capability benchmarks while minimizing safety discussion makes a statement; so does one that leads with alignment philosophy.

## Regulatory Context

### EU AI Act
Foundation models (GPT, Claude, Gemini) face specific **documentation and transparency obligations** under the AI Act:
- Training data description
- Evaluation results disclosure
- Risk and mitigation documentation

System/model cards are the natural container for these requirements.

### US Framework
- **Executive Order on AI** — encourages documentation, testing, disclosure
- **NIST AI RMF** — risk management framework aligned with card structure
- No binding law equivalent to EU AI Act (as of 2025)

## See Also

- [[concepts/claude/system-cards]] — Detailed index and evolution analysis of Anthropic's system cards
- [[concepts/gpt/gpt-deployment-safety-hub]] — OpenAI's Deployment Safety Hub: complete index of 19 system cards (GPT-5 through GPT-Rosalind-5.5)
- [[concepts/ai-safety]] — Broader AI safety landscape
- [[concepts/ai-evaluations]] — Evaluation methodologies and benchmarks
- [[concepts/ai-governance]] — Governance frameworks and regulatory landscape

## References

- Hoeijmakers, R. (2025). "Model Cards, System Cards and What They're Quietly Becoming." https://hoeijmakers.net/model-cards-system-cards/
- Mollick, E. (2025). X post on reading model cards. https://x.com/emollick/status/1952218373397647411
- Claude 4 System Card: https://www.anthropic.com/index/claude-4
- o4 Mini System Card: https://cdn.openai.com/papers/o4-mini-system-card.pdf
- Gemini 2.5 Deep Think Model Card: https://storage.googleapis.com/deepmind-media/gemini/gemini-2-5-deep-think-model-card.pdf
