---
title: "AI Engineering Skills Map"
type: concept
created: 2026-08-18
updated: 2026-08-18
tags:
  - ai-software-engineering
  - career
  - eval-loops
  - agentic-engineering
  - context-engineering
  - coding-agents
  - product-management
  - continuous-learning
sources:
  - raw/articles/2026-08-14_andrewyng_ai-engineering-skills-map.md
---

# AI Engineering Skills Map

## Overview

The **AI Engineering Skills Map** is a framework published by [[entities/andrew-ng]] (August 2026) that identifies the four most important competencies for developers in the LLM era. Based on analysis of 10,000+ job postings, dozens of structured interviews with AI experts/hiring managers/recruiters, and survey data, it provides a data-driven answer to "what should developers learn next?"

The map explicitly targets **all developers** — not just those with an "AI Engineer" title — paralleling how cloud skills became universal despite only a fraction of engineers holding "Cloud Engineer" roles.

## The Four Skills

### 1. Building and Deploying AI Applications

The defining characteristic of AI applications: **unpredictable outputs**. When you prompt an LLM or train a deep learning model, you don't know exactly what you'll get back. This distinguishes AI software from traditional deterministic systems.

**Core competencies:**
- Understanding AI building blocks: LLMs, [[concepts/context-engineering]], RAG, agentic workflows, ML/DL fundamentals
- Using statistical techniques to measure, steer, and govern AI systems for predictable behavior
- Driving disciplined [[concepts/evals-and-evaluation|evals]] and error analysis loops

**Connection to existing wiki concepts:** This skill directly maps to [[concepts/ai-engineering]] as the central discipline, and to [[concepts/agentic-engineering]] for workflow design.

### 2. Software Engineering Fundamentals

Deep understanding of how software works enables effective building. The key insight: **recognizing what tradeoffs exist** (cost, scalability, reliability, speed, security, privacy) leads to better decisions across the entire stack.

**Why this matters for AI specifically:**
- Inexperienced developers who "vibe code" without understanding tradeoffs get poor results from coding agents — they don't know what context to provide
- Software engineering fundamentals let you **steer coding agents using the precise language of software engineering**
- This is the antidote to "prompt and pray" development

**Connection:** Relates to [[concepts/software-engineering]], [[concepts/vibe-coding]], and the [[concepts/ai-engineer-roadmap-2026]] emphasis on systems architecture over thin API wrappers.

### 3. Using Coding Agents

Agentic coding is now a **core skill for every developer**, not just AI specialists. The skill requires:

- A good **mental model** for how agents work — their limitations and how to work around them
- Knowing **how much to intervene vs leave agents alone** — the steering calibration problem
- Managing a coding agent's **context** — what to provide, what to withhold
- Making tradeoffs between **planning and execution** — when to spec in detail vs when to let the agent iterate
- Helping agents **autonomously close loops** by providing verifiers or evals
- Working with a **clear spec** (and knowing when not to bother)
- Orchestrating **multiple agents** that work together
- Avoiding pitfalls (e.g., agent messing up production databases)
- **Continuous tool evolution** — routines to try new tools and evolve workflows as best practices change

**Connection:** Maps directly to [[concepts/coding-agents]], [[concepts/agentic-engineering]], and [[concepts/harness-engineering]]. The "intervene vs leave alone" calibration echoes the inner/outer loop pattern described in [[concepts/ai-engineering]].

### 4. Shaping the Build

As coding agents improve at executing specs, the engineer's value shifts to **deciding what goes in the spec**. This is the product-sense + ownership skill.

**Key aspects:**
- Engineers can no longer expect pixel-perfect designs to simply implement
- Effective AI engineering requires **product sense**, understanding business context and customer goals
- **Ownership and agency**: AI gives engineers the opportunity to identify problems and execute solutions, not just respond to tickets
- Knowing when to **quickly build an MVP** for user testing vs when to **slow down and build carefully**

**Connection:** This resonates with [[concepts/ai-engineering]]'s "Forward Deployed Engineers" trend and the shift from implementation to specification. Relates to [[concepts/product-management]] for engineers.

## Underlying Mindset: Continuous Learning

All four skills rest on a foundation of **continuous learning**. AI evolves rapidly — today's best practices become tomorrow's anti-patterns. Developers need routines (not just motivation) to keep adopting emerging practices.

## Methodology

Ng describes the process as "akin to running clustering on a massive dataset of jobs and expert interviews":
- 10,000+ job postings analyzed
- Dozens of structured interviews with AI experts, hiring managers, recruiters
- Survey data collection
- Other online data synthesis
- Skills identified as important "not just today but also in the near future"

## Comparison with Other Roadmaps

| Dimension | Ng's Skills Map (2026) | Rohit's Roadmap (Jan 2026) | swyx's AI Engineer (2023) |
|-----------|----------------------|---------------------------|--------------------------|
| **Scope** | All developers | Career-changers | AI specialists |
| **Approach** | Data-driven (10K+ job postings) | Project-based (5 projects) | Definition-driven |
| **Key insight** | Skills > Role title | Production shipping > tutorials | New developer category |
| **Agent focus** | Coding agents as core skill | Self-improving agent project | Agent as application |
| **Product sense** | Explicit ("shaping the build") | Implicit (project selection) | Not addressed |

## Related Pages

- [[entities/andrew-ng]]
- [[concepts/ai-engineering]]
- [[concepts/ai-engineer-roadmap-2026]]
- [[concepts/agentic-engineering]]
- [[concepts/context-engineering]]
- [[concepts/coding-agents]]
- [[concepts/evals-and-evaluation]]
- [[concepts/harness-engineering]]
- [[concepts/vibe-coding]]
- [[concepts/software-engineering]]
