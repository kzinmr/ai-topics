---
title: "Drew Breunig — Core Ideas & Philosophy"
type: entity
parent: drew-breunig
created: 2026-04-10
updated: 2026-04-10
tags:
  - person
  - context-engineering
  - spec-driven-development
  - ai
  - philosophy
sources: []
---

# Drew Breunig: Core Ideas & Philosophy

Back to main profile: [[drew-breunig]]

## Context Engineering as a Discipline

Breunig is perhaps best known for coining and popularizing the term **"context engineering"** to describe the systematic management of LLM context windows. His work emerged in mid-2025, coinciding with Andrej Karpathy's similar articulation of the concept. Breunig argued that as context windows grew from 4K to 1M+ tokens, simply stuffing more information into prompts was counterproductive — it introduced new failure modes that required dedicated engineering discipline.

His framework identifies four primary context failures:

- **Context Poisoning**: When a hallucination or error enters the context and is repeatedly referenced, compounding over time. The Gemini 2.5 team documented this when their agent playing Pokémon would hallucinate and then repeatedly reference its own error.
- **Context Distraction**: When the context overwhelms the model's training, causing it to focus on provided information at the expense of its general knowledge. Databricks research showed Llama 3.1 405B correctness began falling around 32K tokens.
- **Context Confusion**: When irrelevant or contradictory information in the context leads to degraded responses. A quantized Llama 3.1 8B model failed with 46 tools but succeeded with 19.
- **Context Clash**: When tool descriptions or instructions contradict the rest of the prompt, creating internal confusion.

His mitigation framework includes six tactics: **RAG**, **Tool Loadout**, **Context Quarantine**, **Context Pruning**, **Context Summarization**, and **Context Offloading**.

> "Programming the LLM to, as Karpathy says, 'pack the context windows just right' — smartly deploying tools, information, and regular context maintenance — is the job of the agent designer."

See also: [[concepts/context-engineering]]

## The 3 AI Use Cases: Gods, Interns, and Cogs

In October 2024, Breunig proposed a taxonomy for understanding AI applications that cut through the hype:

- **Gods**: Models used for their creative and generative capabilities — writing, brainstorming, ideation. The model is the product.
- **Interns**: Models used to augment human work — coding assistants, research aides. The human is still in the loop.
- **Cogs**: Models used for automated, repetitive tasks — classification, extraction, routing. The model is a component in a larger system.

## Sober AI and Quiet AI

Breunig has been a consistent voice for measured, practical AI adoption. In "A Plea for Sober AI" (May 2024), he argued the hype prevents us from appreciating genuine AI advances. He advocates for **"quiet AI"** — AI features that work invisibly to improve user experience rather than demanding attention through chatbots and interfaces. His "Be Better, Not Smaller" essay (July 2024) argued against the trend of building smaller, dumber models.

## Spec-Driven Development and the SDD Triangle

Breunig is a pioneer of **Spec-Driven Development (SDD)** — using coding agents to implement software from detailed text specifications and test suites, without writing code directly. His `whenwords` project (late 2024) was a landmark demonstration: a software library distributed as a Markdown specification and YAML test suite, with no code at all.

From this experience, he developed the **Spec-Driven Development Triangle**:

```
        Spec
       /    \
      /      \
    Tests -- Code
```

The triangle represents a feedback loop where:
- The **spec** defines what tests need to pass and what code should do
- The **tests** validate both the spec's requirements and the code's behavior
- The **code** is the implementation, but also reveals gaps in both spec and tests

> "Spec-driven development is a feedback loop, not a straight line."

He built `plumb` (2026) as a proof-of-concept tool to manage this triangle.

See also: [[concepts/spec-driven-development]]

## Recursive Language Models (RLMs)

Breunig is an advocate for **Recursive Language Models**, a pattern developed by Alex Zhang and Omar Khattab that gives LLMs a REPL environment to explore, analyze, and reason over large contexts. He implemented RLM support in [[concepts/dspy]] and documented extensive use cases. The key insight: RLMs maintain two distinct context pools — tokenized context (what fills the window) and external context (what the model can explore).

> "If you run them on the same task several times, you're generating emergent agent discovery patterns."

See also: [[concepts/recursive-language-models]]

## The Two Beliefs About Coding Agents

In February 2026, Breunig articulated two observations from watching the AI coding ecosystem mature:

1. **Most talented developers don't appreciate the impact of their intuitive knowledge on coding agents.** The same agent given to a junior developer would produce different results.
2. **Most work people share are incredible personal tools, but not capital-P Products.** "Code today is free, as in puppies."

## Agentic Development: Clones → Reimaginings

In April 2026, Breunig identified a shift in open-source AI coding projects:

- **Phase 1 (Clones/Ports)**: Using agents to reimplement existing software. Low-hanging fruit because existing test suites provide ground truth.
- **Phase 2 (Reimaginings)**: Attacking old problems with modern tactics, unconstrained by legacy architecture.

> "Coding agents make reimagining practical because the cost to perform them is so, so much lower. Code is cheap."

## The Software Crisis Revisited

At the MLOps Community conference (March 2026), Breunig drew a historical parallel: the initial Software Crisis was our inability to manage complex codebases new computers allowed; our current crisis is our inability to manage complex codebases new models allow. He characterized the current moment as: "Waterfall volume at the cadence of agile."

## Geospatial Standardization and GERS

Breunig has been a leading advocate for the **Global Entity Reference System (GERS)**, a persistent identifier system developed by the Overture Maps Foundation. GERS assigns a stable 128-bit, 32-character ID to every entity in Overture's dataset, enabling simple column joins across disparate geospatial datasets without complex spatial operations.

> "Standardizing location with WGS 84 hasn't proven sufficient. Every organization can benefit from geospatial intelligence."

See also: [[concepts/overture-maps-foundation]]

## Anthropological Lens on Technology

Breunig's background in cultural anthropology shapes his approach to technology analysis. He consistently examines how systems shape human behavior and culture, rather than treating technology as purely technical. His early writings explored how Facebook Timeline, Chat Roulette, and Google Glass were changing social dynamics.

> "Do Algorithms Find Depression or Cause Depression?" (2016) — examining whether crowdsourced workers' depression in ML training data was discovered or induced by the work itself.

## See Also

- [[drew-breunig--projects|Projects]]
- [[drew-breunig--timeline|Timeline]]
- [[drew-breunig--writings|Writings & Speaking]]
