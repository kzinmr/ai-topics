---
title: "Walden Yan"
tags: [person]
created: 2026-04-24
updated: 2026-04-13
type: entity
---


# Walden Yan — Cognition Co-Founder & Chief Product Officer

| | |
|---|---|
| **Role** | Co-Founder & Chief Product Officer (CPO), Cognition AI |
| **Organization** | Cognition AI — maker of Devin |
| **Previous** | Co-Founder & CEO at DeepReason (2022–2023); Early Engineer at Anysphere/Cursor (2023); Managing Partner at Inverted Agency (2020–2021) |
| **Education** | Harvard University — B.A. Computer Science and Economics (2020–2024) |
| **Notable Achievements** | IOI 2020 Gold Medalist (USA), MIT PRIMES Researcher |
| **Location** | San Francisco Bay Area |
| **X/Twitter** | [@walden_yan](https://x.com/walden_yan) |
| **LinkedIn** | [waldenyan](https://linkedin.com/in/waldenyan) |
| **Website** | [waldenyan.com](https://waldenyan.com) |
| **Years Active** | 2018 – Present |

## Overview

Walden Yan is a **Co-Founder and Chief Product Officer (CPO)** at Cognition AI, where he leads product strategy and has become one of the most influential voices in the emerging field of **context engineering** for AI agents.

Yan is a former competitive programming prodigy who won a **gold medal at the 2020 International Olympiad in Informatics (IOI)** representing the United States (ranked 19/343, score 505.38/600). Alongside Scott Wu and Steven Hao, he co-founded Cognition AI in late 2023 after recognizing the potential for AI systems to autonomously complete complex engineering tasks.

His June 2025 blog post **"Don't Build Multi-Agents"** became one of the most debated and cited articles in the AI agent community, establishing Cognition's philosophical stance that **context continuity** is more important than parallelism in agent architecture.

## Timeline

| Date | Event |
|------|-------|
| 2018–2020 | MIT PRIMES Researcher — cryptography and machine learning research |
| 2020 | Wins gold medal at IOI 2020 (Singapore, ranked 19th globally, USA team) |
| 2020–2024 | Harvard University — B.A. Computer Science and Economics |
| 2020–2021 | Managing Partner at Inverted Agency (IT consulting, 11-50 employees) |
| 2022–2023 | Co-Founder & CEO at DeepReason (security systems startup, 1-10 employees) |
| Jun–Aug 2023 | Early Engineer at Anysphere (building Cursor) |
| Nov 2023 | Co-founds Cognition AI with Scott Wu and Steven Hao |
| Mar 2024 | Devin 1.0 launch — Yan contributes to core product architecture |
| Apr 2024 | Cognition raises $21M Series A (Founders Fund) |
| Jun 2025 | Publishes "Don't Build Multi-Agents" — defining statement on context engineering |
| Feb 2025 | DeepWiki by Cognition launches (Yan listed as maker on Product Hunt) |
| 2025 | Named CPO of Cognition AI |
| Apr 2026 | Devin reaches general availability; Cognition acquires Windsurf/Codeium |

## Core Philosophy

### Context Engineering

Yan coined and popularized the term **"context engineering"** as the central discipline for building reliable AI agents. His core thesis: the fundamental challenge in agent development is not model intelligence, but **how context is managed, compressed, and propagated** through the agent's decision loop.

Two foundational principles:

> *"Principle 1: Share context, and share full agent traces, not just individual messages. Sub-agents must inherit the complete history of what happened before them."*

> *"Principle 2: Actions carry implicit decisions, and conflicting decisions carry bad results. Parallel agents operating on isolated context make incompatible outputs."*

Yan argues that current multi-agent frameworks (OpenAI's Swarm, Microsoft's AutoGen) are fundamentally flawed because they treat agents as independent workers, ignoring the **context loss problem** that occurs during handoffs:

> *"When you hand off work between agents, you're not just passing context — you're passing responsibility. And responsibility doesn't serialize well."*

### Don't Build Multi-Agents (June 2025)

In his landmark blog post, Yan makes the case against naive multi-agent architectures for production systems:

**The Problem with Multi-Agents:**
- Each agent has to rebuild understanding from scratch
- Parallel agents make conflicting implicit decisions without awareness of each other's work
- The cost of coordination exceeds the benefit of parallelism for most coding tasks
- Integration of outputs from isolated agents produces fragile, inconsistent results

**What Works Instead:**
- **Single-threaded agents** with full context continuity
- **Context compression** — LLM-based summarization of actions, decisions, and reasoning history
- **Full agent traces** — every sub-agent sees the complete decision chain
- **Specialized models for compression** — Cognition fine-tunes smaller models specifically for context summarization

> *"I would argue that Principles 1 & 2 are so critical, and so rarely worth violating, that you should by default rule out any agent architectures that don't abide by them."*

### The "HTML/CSS Era" of Agent Development

Yan compares the current state of agent development to early web development:

> *"We're still playing with raw HTML & CSS and figuring out how to fit these together to make a good experience. No single approach to building agents has become the standard yet."*

He predicts that, just as React eventually standardized component-based web development, a unifying framework for agent architecture will emerge — but only after the community masters the fundamentals of context management.

### Humility in Agent Design

Despite Cognition's success, Yan advocates for intellectual humility:

> *"Our theories are likely not perfect, and we expect things to change as the field advances, so some flexibility and humility is required as well."*

## Background

### Competitive Programming (IOI Gold Medalist)

Yan's competitive programming career peaked at **IOI 2020** (held in Singapore), where he scored 505.38/600 points and ranked 19th globally among 343 contestants, earning a gold medal for the United States. This places him in the same elite category as Cognition co-founders Scott Wu (3× IOI Gold) and Steven Hao.

The IOI background is central to Cognition's identity — the founding team collectively holds 10 IOI gold medals, and Wu has stated this gives Cognition a unique advantage in AI: *"Teaching an AI to be a programmer is a very deep algorithmic problem that requires the system to make complex decisions."*

### MIT PRIMES Research (2018–2020)

During high school, Yan conducted research at MIT's PRIMES program in **cryptography and machine learning**. Key work included:
- Designing and benchmarking NPS (Neural Probabilistic Sketch) models, beating state-of-the-art
- Collaborating on a compiler library for optimized fully homomorphically encrypted (FHE) programs integrated with LLVM

This early exposure to both **security/privacy** (FHE) and **ML optimization** shaped his later interest in building reliable, verifiable AI systems.

### Entrepreneurial Journey

Before Cognition, Yan had already founded two companies:

1. **Inverted Agency (2020–2021)**: IT consulting firm that sourced leads, built web applications, and managed digital media for clients. Grew to 11-50 employees before acquisition.

2. **DeepReason (2022–2023)**: Security systems startup focused on automated reasoning and verification. The company's work on verifiable AI systems directly influenced Yan's later focus on agent reliability.

3. **Anysphere/Cursor (Jun–Aug 2023)**: Brief stint as an early engineer at Anysphere, where he worked on Cursor — the AI-powered code editor. This experience gave him firsthand insight into developer tooling and AI-assisted coding, directly informing his later work on Devin.

## Key Publications

### "Don't Build Multi-Agents" (Cognition Blog, June 2025)

The most cited article on context engineering, establishing Cognition's architectural philosophy. The article:
- Critiques OpenAI Swarm and Microsoft AutoGen for promoting naive multi-agent patterns
- Introduces two principles of context engineering
- Proposes context compression as the solution to long-context limitations
- Acknowledges that parallelism may emerge organically as single-agent capabilities improve

Impact: The article was widely discussed on X/Twitter, LinkedIn, and in AI engineering communities. Jason Liu's "Notes on Context Engineering" summary post received 2.6K+ views on Threads alone.

### Maven Course: "Why Devin Does Not Use Multi-Agents"

Yan delivered a public lecture expanding on his blog post, covering:
- The specific failure modes of multi-agent architectures in production
- How Cognition's internal "Managed Devins" system works (single-agent orchestration with conditional sub-agent spawning)
- The relationship between context window limits and agent reliability

## Cognition's Technical Architecture (Yan's Contributions)

As CPO, Yan oversees product architecture. Key design decisions he has championed:

- **Single-threaded core agent**: Devin operates as a single persistent agent with context continuity
- **Context compression layer**: Fine-tuned smaller models summarize agent history for extended sessions
- **Conditional sub-agent spawning**: Sub-agents are only used for well-defined, isolated queries — never for parallel code writing
- **Full trace propagation**: Every agent action includes the complete decision history
- **Knowledge file system**: Devin's equivalent of AGENTS.md — persistent project conventions and context

## Key Quotes

> *"I think the most important insight from Cognition is that context continuity beats parallelism."*

> *"When you hand off work between agents, you're not just passing context — you're passing responsibility. And responsibility doesn't serialize well."*

> *"We're still playing with raw HTML & CSS and figuring out how to fit these together to make a good experience."* — On the current state of agent development

> *"Our theories are likely not perfect, and we expect things to change as the field advances, so some flexibility and humility is required as well."*

> *"In 2025, the models out there are extremely intelligent. But even the smartest human won't be able to do their job effectively without the context of what they're being asked to do."*

## Related

- [[concepts/cognition-devin-philosophy]] — Cognition's approach to building AI agents
- [[concepts/context-engineering]] — Yan's framework for managing agent context
- [[scott-wu]] — Cognition CEO and co-founder
- [[nader-dabit]] — Cognition Growth Engineer, cloud agent advocate

## Sources

- [Don't Build Multi-Agents](https://cognition.ai/blog/dont-build-multi-agents) — Walden Yan, Cognition AI (Jun 2025)
- [LinkedIn Profile](https://linkedin.com/in/waldenyan)
- [Product Hunt Profile](https://www.producthunt.com/@walden_yan1)
- [IOI 2020 Statistics](https://stats.ioinformatics.org/people/7322)
- [Cognition AI — Wikipedia](https://en.wikipedia.org/wiki/Cognition_AI)
- [Notes on Context Engineering](https://www.threads.com/@sung.kim.mw/post/DMLzfwzTfmm/) — Jason Liu's summary of conversation with Yan
- [Walden Yan — waldenyan.com](https://waldenyan.com)
