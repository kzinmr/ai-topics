---
title: OpenAI o1 System Card (December 2024)
created: 2026-06-10
updated: 2026-06-10
type: concept
tags: [openai, system-card, gpt, ai-safety, evaluations, preparedness-framework, reasoning-model, deliberative-alignment, frontier-models]
sources: [https://openai.com/index/openai-o1-system-card/]
---

# OpenAI o1 System Card (December 2024)

The **o1 System Card** ([page](https://openai.com/index/openai-o1-system-card/)) documents OpenAI's first reasoning model family — o1, o1-preview, and o1-mini. Published December 2024, it introduced **deliberative alignment** as a new safety paradigm and established the reasoning model series that would later become GPT-5 Thinking.

## Model Overview

| Variant | Description |
|---|---|
| **o1** | Full reasoning model, trained with large-scale RL for chain-of-thought |
| **o1-preview** | Earlier checkpoint, initially released Sep 2024 |
| **o1-mini** | Smaller, faster reasoning variant |

### Training Approach

Four pillars of reasoning training:
1. **Reinforcement Learning** — Large-scale RL on reasoning tasks
2. **Chain of Thought** — Internal reasoning before response
3. **Self-Refinement** — Models learn to recognize and correct mistakes
4. **Extended Thinking Time** — More compute at inference improves quality

## Key Benchmarks

| Benchmark | o1 | o1-preview | GPT-4o |
|---|---|---|---|
| AIME 2024 | 94.8% | — | — |
| Codeforces | 93rd percentile | — | — |
| GPQA Diamond | — | 78.0% | 53.6% |

## Deliberative Alignment

The o1 system card introduced **deliberative alignment** — a training approach where the model explicitly reasons about safety specifications during its chain of thought before producing an answer.

| Aspect | Traditional Alignment | Deliberative Alignment |
|---|---|---|
| Safety reasoning | Implicit in model weights | Explicit in CoT |
| Adaptation | Static after training | Context-sensitive |
| False positive rate | Higher (overrefusal) | Reduced |
| False negative rate | Variable | Reduced |

This approach became foundational for all subsequent o-series and GPT-5 Thinking models.

## Preparedness Framework Assessment

First model family to be assessed under the original Preparedness Framework:

| Category | Level |
|---|---|
| Cybersecurity | Medium |
| Chemical & Biological | Medium |
| Persuasion | Medium |
| Model Autonomy | Low |

- First models to reach Medium across multiple categories simultaneously
- Cybersecurity Medium was notable — reasoning capabilities enhanced cyber-offensive potential

## External Assessments

- **ARC (Alignment Research Center)**: Evaluated for autonomous replication — concluded Low risk
- **External red teamers**: Tested across multiple domains and languages
- **Academic reviewers**: Reviewed safety evaluations and methodology

## Safety Evaluations

### Internal Testing
- Standard refusal evaluation: strong performance
- Robustness testing: resilient against common jailbreaks
- Over-refusal testing: reduced false positives vs GPT-4o

### Red Teaming
- Internal red teaming across safety categories
- External red teaming with domain experts
- Multilingual safety evaluation

## Significance

The o1 system card established several patterns that define all subsequent OpenAI reasoning model cards:

1. **Deliberative alignment** — reasoning about safety in context, not just following rules
2. **Reasoning-safety synergy** — the same capabilities that improve task performance also improve safety reasoning
3. **CoT monitorability** — chain of thought enables safety monitoring (later formalized in GPT-5)
4. **Test-time compute scaling** — more thinking time → better safety, not just better capability

## Historical Context

- **Sep 2024**: o1-preview released (first public reasoning model)
- **Dec 2024**: o1 full release + system card
- **Dec 2024**: o3 announced (previewed during 12 Days of OpenAI)
- **Jan 2025**: o3-mini released
- **Apr 2025**: o3/o4-mini system card (Preparedness Framework v2)
- **Aug 2025**: o3 absorbed into GPT-5 as "Thinking" mode

See [[concepts/gpt/gpt-o-series-gpt5-unification]] for the full o-series → GPT-5 timeline.

## See Also

- [[concepts/gpt/gpt-o3-o4-mini-system-card]] — Next iteration (Apr 2025, Preparedness v2)
- [[concepts/gpt/gpt-o-series-gpt5-unification]] — o-series → GPT-5 unification
- [[concepts/gpt/gpt-5-system-card]] — Where o1 reasoning was absorbed as "Thinking" mode
- [[concepts/gpt/gpt-system-card-milestones]] — Timeline of all milestones
- [[concepts/gpt/gpt-deployment-safety-hub]] — Full index
