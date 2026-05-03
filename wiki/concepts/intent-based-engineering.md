---
title: "Intent-Based Engineering"
tags: [articulation-gap, prompt-engineering, evals, ai-engineering]
created: 2026-05-03
updated: 2026-05-03
type: concept
aliases: [intent-based-engineering, articulation-gap]
---

# Intent-Based Engineering

A concept articulated by [[entities/daniel-miessler|Daniel Miessler]] (April 2026) identifying the **articulation gap** as the new primary bottleneck in AI development. The core thesis: engineering is shifting from "how to build" to "how to describe what good looks like."

## The Articulation Gap

The primary bottleneck in AI is no longer technical capability — models can now execute complex workflows reliably. The bottleneck is **intent clarity**: most leaders and domain experts cannot clearly state what they want in terms verifiable by an AI.

> The new elite skill is articulating intent clearly enough that it becomes verifiable for an AI to "hill-climb" toward.

## The Skill: Reverse-Engineering Intent

The core practice: taking a fuzzy business requirement or creative vision and reverse-engineering it into **discrete, testable ideal state criteria**:

- Each criterion is **8–12 words maximum**
- Each is **binary**: pass/fail, measurable
- Collectively they form a verifiable specification the AI can optimize toward

## Why This Matters Now

| Era | Bottleneck | Skill |
|-----|-----------|-------|
| Pre-2024 | AI capability (models were too weak) | Technical implementation |
| 2024-2025 | Prompt engineering (getting models to do what you want) | Prompt design, chain-of-thought |
| **2026+** | **Intent articulation** (knowing what you want well enough to specify it) | Reverse-engineering fuzzy goals into verifiable criteria |

## Key Implications

1. **Most leaders cannot specify intent** — Miessler observes that most leaders cannot clearly state what they want in testable terms
2. **Binary criteria = competitive advantage** — Teams that master this can leverage AI far more effectively
3. **Evals become primary interface** — The quality of the eval defines the quality of the outcome
4. **Domain expertise becomes even more valuable** — You must deeply understand the domain to know what "good" looks like

## Relationship to Other Concepts

- [[concepts/autonomous-component-optimization]] — The cycle that consumes intent-based criteria as input to its Map phase
- [[concepts/ai-evals]] — Intent-based engineering produces the eval criteria that drive optimization
- [[concepts/resilient-prompt-engineering]] — Prompt engineering as enabling reliable AI interaction; intent-based engineering is the higher-level framing of what to ask for
- [[concepts/critique-shadowing]] — The LLM-as-Judge methodology that validates whether criteria are met
- [[concepts/harness-engineering/system-architecture/evals-for-ai-agents]] — Anthropic's evals framework

## References

- Daniel Miessler, "The Most Important Ideas in AI Right Now (April 2026)" → [[raw/articles/2026-04_daniel-miessler_most-important-ideas-in-ai.md]]
