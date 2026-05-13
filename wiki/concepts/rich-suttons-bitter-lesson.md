---
title: "Rich Sutton's Bitter Lesson"
type: concept
aliases:
  - rich-suttons-bitter-lesson
  - the-bitter-lesson
created: 2026-04-25
updated: 2026-05-13
tags:
  - concept
  - methodology
  - architecture
  - scaling
  - ai-agents
  - ai-agent-engineering
  - harness-engineering
  - philosophy
status: complete
sources:
  - "http://www.incompleteideas.net/IncIdeas/BitterLesson.html"
  - "[[raw/articles/2025-07-30_rlancemartin_bitter-lesson-ai-engineering]]"
  - "[[concepts/bitter-lesson-harnessing]]"
---

# Rich Sutton's Bitter Lesson

## TL;DR

> *The biggest lesson that can be read from 70 years of AI research is that general methods that leverage computation are ultimately the most effective, and by a large margin.* — Rich Sutton, 2019

The **Bitter Lesson** states that hand-crafted, domain-specific structure (features, heuristics, rules) inevitably loses to general-purpose methods that leverage raw computation at scale. This pattern has repeated across every major AI domain — chess, Go, computer vision, speech recognition, NLP — and now applies to **AI agent engineering**: as models improve through scale, sophisticated hand-crafted harness patterns become bottlenecks rather than advantages.

## The Original Essay (Rich Sutton, 2019)

Rich Sutton's [essay](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) observes two consistent patterns:

1. **Researchers want to build knowledge into their agents** — This is natural and satisfying, producing visible short-term progress
2. **In the long run, this approach plateaus and inhibits further progress** — Breakthroughs come from methods that scale with computation: search and learning

The "bitter" part: the first approach is what researchers are rewarded for (publishing papers, demonstrating cleverness), while the second approach often looks too simple to be publishable — until it wins decisively.

### Historical Examples

| Domain | Hand-Crafted Approach | What Actually Won | When |
|--------|----------------------|-------------------|------|
| **Chess** | Human-crafted evaluation functions, opening books, endgame tables | Deep search (Deep Blue, then AlphaZero) | 1997, 2017 |
| **Go** | Expert-crafted patterns, territory heuristics | Monte Carlo tree search + deep learning (AlphaGo) | 2016 |
| **Computer Vision** | SIFT, HOG, hand-designed feature detectors | Deep CNNs learning features directly from pixels | 2012 |
| **Speech Recognition** | HMMs with hand-crafted phoneme models, Gaussian mixtures | Deep learning on raw waveforms | 2012-2015 |
| **NLP / Machine Translation** | Grammar rules, parse trees, statistical phrase tables | Large transformer models trained on massive text | 2018+ |

## Hyung Won Chung's Framework: Add Then Remove

Hyung Won Chung (OpenAI) provides a practical methodology for applying the Bitter Lesson in research and engineering ([talk](https://youtu.be/orDKvo8h71o)):

> **Add structures needed for the given level of compute and data available. Remove them later, because these shortcuts will bottleneck further improvement.**

This is a two-phase approach:
1. **Add structure** — When compute/data are limited, impose inductive biases to make models work at all
2. **Remove structure** — As compute/data scale, strip away those shortcuts to unlock further gains

The critical insight: most practitioners succeed at phase 1 but **fail at phase 2** — they get attached to the structures they built and never remove them, creating long-term bottlenecks.

## The Bitter Lesson in AI Agent Engineering

Lance Martin ([blog post](https://rlancemartin.github.io/2025/07/30/bitter_lesson/), Jul 2025) applies the Bitter Lesson directly to the craft of building AI applications.

### Case Study: open-deep-research

Martin's experience building [open-deep-research](https://github.com/langchain-ai/open_deep_research) illustrates the add-then-remove cycle:

**Phase 1 — Adding Structure (late 2024)**: When tool calling was unreliable and context windows were small, Martin imposed explicit structure:
- Orchestrator-worker workflow (decompose request → parallel workers → combine)
- No tool calling (avoided due to unreliability)
- Fixed decomposition strategy (always break into report sections)
- Parallel section writing (for speed)

**Phase 2 — Bottlenecks Emerge (early 2025)**: As tool calling improved and MCP gained momentum, this structure became a liability:
- No tool calling → couldn't leverage MCP ecosystem
- Rigid decomposition → inappropriate for non-report queries
- Parallel sections → disjoint, incoherent reports

**Phase 3 — Removing Structure (mid 2025)**: Martin moved to a flexible multi-agent system, then further simplified:
- Removed per-agent section writing → single agent writes final report from collected context
- Achieved 43.5 on Deep Research Bench (top 10) as a small open-source effort

### Three Lessons for AI Engineering

1. **Understand your application structure** — Identify which LLM performance assumptions are baked into your design. Martin avoided tool calling because it was unreliable in 2023-2024 — an assumption that became obsolete within months.

2. **Re-evaluate structure as models improve** — Jared Kaplan (Anthropic co-founder) notes it can be beneficial to [build things that don't quite work yet](https://x.com/jaredqkaplan) because models will catch up quickly. The corollary: what doesn't work today may work tomorrow, and your structure must adapt.

3. **Make it easy to remove structure** — Both Walden Yan (Cognition) and Harrison Chase (LangChain) warn that agent abstractions can make it harder to remove structure. Martin's approach: use frameworks like LangGraph for useful infrastructure (checkpointing) but stick to **low-level building blocks** (nodes, edges) that enable easy reconfiguration.

### Agent Abstractions as Structure

The Bitter Lesson applies to agent frameworks themselves:
- High-level abstractions (pre-built agent classes, opinionated pipelines) are **structure** — they accelerate initial development but risk becoming bottlenecks
- Low-level primitives (nodes, edges, state graphs) are closer to **general computation-leveraging methods** — more flexible as models evolve
- Boris (Claude Code lead) [cited](https://www.youtube.com/watch?v=Lue8K2jqfKk) the Bitter Lesson as a core influence: complexity should *decrease* as models improve

## Bitter Lesson Applied to Agent Harnesses

The concept extends naturally to agent harness design. See [[concepts/bitter-lesson-harnessing]] for the full treatment.

Key dynamic:
- **When models improve rapidly**: Free-form context engineering wins — harness patterns become obsolete before they stabilize
- **When models stabilize**: Framework-based harnessing becomes valuable — you can optimize for known model behavior
- **Ultimate trajectory**: As models absorb complexity, the harness shrinks to minimal orchestration

> *The most effective harness is the one that becomes unnecessary as models improve.*

## The Prediction

As Hyung Won Chung emphasizes, the one thing we **can** predict is that models will get much better. The winning strategy for AI engineering is not to build the most sophisticated structure, but to design systems that can **shed structure** as the underlying models evolve. This means:

- Favoring composable, low-level primitives over monolithic abstractions
- Making assumptions explicit so they can be revisited
- Building for model improvement, not for current model limitations
- Accepting that today's clever engineering may be tomorrow's bottleneck

## Related Pages

- [[concepts/bitter-lesson-harnessing]] — How model capability evolution affects harness engineering importance
- [[concepts/bitter-lesson-agent-harnesses]] — Bitter Lesson implications for agent harness design
- [[concepts/reduce-offload-isolate]] — Lance Martin's context management framework (influenced by the Bitter Lesson)
- [[entities/lance-martin]] — Author of the AI engineering application
- [[concepts/harness-engineering]] — The broader discipline
- [[concepts/ai-agent-engineering]] — AI engineering craft and methodology

## References

- [The Bitter Lesson — Rich Sutton (2019)](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)
- [Learning the Bitter Lesson — Lance Martin (2025)](https://rlancemartin.github.io/2025/07/30/bitter_lesson/)
- [Hyung Won Chung — "Large Language Models (in 2023)" talk](https://youtu.be/orDKvo8h71o)
- [The Bitter Lesson Across Domains — arXiv:2410.09649](https://arxiv.org/html/2410.09649v1)
- [Don't Build Multi-Agents — Walden Yan, Cognition](https://cognition.ai/blog/dont-build-multi-agents)
- [Building Effective Agents — Anthropic (2024)](https://www.anthropic.com/engineering/building-effective-agents)
