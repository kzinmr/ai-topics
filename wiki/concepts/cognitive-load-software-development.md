---
title: "Cognitive Load in Software Development"
type: concept
aliases:
  - cognitive-load-theory
  - zakirullin-cognitive-load
created: 2026-04-16
updated: 2026-05-26
tags:
  - concept
  - methodology
  - software-engineering
  - psychology
  - agentic-engineering
status: active
sources:
  - "https://minds.md/zakirullin/cognitive#long"
  - "https://github.com/zakirullin/cognitive-load"
---

# Cognitive Load in Software Development

Artem Zakirullin's **"Cognitive load is what matters"** — A systematic framework for cognitive load in software design, with 12,000+ stars on GitHub.

## Core Theorem

> "Confusion costs time and money. Confusion is caused by high cognitive load. It's not some fancy abstract concept, but rather **a fundamental human constraint.**"

- Developers spend far more time **reading** code than writing it
- The human working memory can hold only about **4 chunks**
- Exceeding this threshold causes confusion (🤯), degrading productivity and quality

## The Two Types of Cognitive Load

| Type | Description | Controllability |
|------|-------------|-----------------|
| **Intrinsic Load** | Inherent difficulty of the task/domain | Cannot be reduced |
| **Extraneous Load** | Presentation method, unnecessary abstractions, author's quirks | **Reducible (this is where to focus)** |

### Load Notation
- 🧠 = Fresh working memory, zero load
- 🧠++ = Holding 2 facts, load increasing
- 🤯 = Cognitive overload, 4+ facts

## Links to Sub-Pages

This framework is broken down into the following three sub-pages:

### [[concepts/cognitive-load-theory]] — Theory
Core theorem, the two types of cognitive load, mental models and onboarding (40-minute rule), theoretical insights from HN comments (mental model dependency, Programming as Theory-building).

### [[concepts/cognitive-load-patterns]] — Patterns
Code-level anti-patterns (complex conditionals, nested ifs, deep inheritance chains) and architecture-level insights (Deep vs Shallow Modules, SRP reinterpretation, microservice pitfalls, layer architecture, DDD scope), language and dependency choices, pattern discussions from HN comments.

### [[concepts/cognitive-load-tool-support]] — Tool Support
Implications for Agentic Engineering (4 ways agents transfer cognitive load), tooling recommendations (4 personas, cyclomatic complexity, early return linting), practical insights from HN comments.

## Implications for Agentic Engineering (Overview)

Zakirullin's cognitive load framework gains **new dimensions** in the age of AI coding agents:

1. **Agents "transfer" cognitive load** — As [[concepts/cognitive-cost-of-agents]] (Simon Willison) points out, agents don't reduce work; they redistribute it
2. **AGENTS.md should be a Deep Module** — The AGENTS.md pattern from [[concepts/harness-engineering]] aligns with Zakirullin's deep module principle
3. **Symphony throughput and cognitive overload** — In the era of thousands of PRs per day, human reviewers are prone to 🤯 states
4. **"Boring" agent pipelines win** — Simple interfaces + complex internal encapsulation

See [[concepts/cognitive-load-tool-support]] for details.

## HN Thread Analysis (Overview)

[HN Thread](https://news.ycombinator.com/item?id=45074248) — Score: 1,582, 104 top-level comments. Key insights distributed across sub-pages:

- **Theory-related**: Mental model dependency (weiliddat), Programming as Theory-building (physidev) → [[concepts/cognitive-load-theory]]
- **Pattern-related**: Readability vs correctness (hackrmn), mountains of ifs (Buttons840), early return debate (mattmanser), house organization analogy (gnramires) → [[concepts/cognitive-load-patterns]]
- **Tool-related**: Noyce's Law (pessimizer), 4 personas (noen), cyclomatic complexity (safety1st), "perfect idea" delusion (0xbadcafebee), multi-language domain hierarchies (RossBencina), corporate environment (atomicnumber3), practical data modeling (sfn42), concise summary (nathane280) → [[concepts/cognitive-load-tool-support]]

## Related Concepts

- [[comparisons/aposd-vs-clean-code]] — Ousterhout vs Martin design philosophy comparison. Integrates Deep/Small, comments, TDD/Bundling from cognitive load perspective
- [[concepts/cognitive-cost-of-agents]] — Willison's cognitive debt theory (cognitive cost in the agent era)
- [[concepts/harness-engineering]] — Lopopolo's agent environment design
- [[concepts/context-window-management]] — Managing context constraints
- [[concepts/harness-engineering/agentic-workflows/agent-first-design]] — Code design for agents

## Sources

- Artem Zakirullin, ["Cognitive load is what matters"](https://minds.md/zakirullin/cognitive#long) (2025-10, GitHub 12k+ stars)
- [HN Discussion](https://news.ycombinator.com/item?id=45074248) (Score: 1,582, 104 top-level comments, 362 total)
- John Ousterhout, "A Philosophy of Software Design" (deep/shallow modules)
- Carson Gross, "Codin' Dirty" (important things should be big)
- Rob Pike, "Less is exponentially more" (choice overload)
- Hyrum's Law (implicit behaviors as dependencies)

