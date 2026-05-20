---
title: Lance Martin
created: 2026-05-20
updated: 2026-05-20
type: entity
tags:
  [person, anthropic, langchain, ai-agent-engineering, context-engineering, researcher, blogger]
sources:
  [raw/articles/2025-06-23_lancemartin_context-engineering-for-agents.md, raw/articles/2026-01-09_lancemartin_agent-design-patterns.md, https://rlancemartin.github.io/, https://substack.com/@lancemartin]
---

# Lance Martin

**Lance Martin** is a Member of Technical Staff at [[anthropic]], known for his influential writing on **context engineering** and **agent design patterns**. He synthesizes practical patterns observed across the AI agent ecosystem, bridging academic research and production engineering.

## Background

- **Current**: Member of Technical Staff, Anthropic (Applied AI)
- **Previous**: Software/ML at [[langchain|LangChain]] (May 2023 – 2025), where he worked on open-source LLM frameworks
- **Earlier**: Tech Lead Manager at Nuro (autonomous vehicles), Perception Lead at Ike (acquired by Nuro), Truck Perception Lead at Uber ATG
- **Education**: PhD + MS from Stanford University (computational biology / protein-RNA interaction software), BE + BS from Dartmouth College
- **Research**: 20+ publications and patents; early work at Stanford and Lawrence Berkeley National Laboratory

## Key Contributions

### Context Engineering Taxonomy

Lance Martin's most cited contribution is a **4-strategy taxonomy** for context engineering, published in June 2025:

- **Write** — Save context outside the window (scratchpads, memories)
- **Select** — Pull relevant context into the window (RAG, memory retrieval)
- **Compress** — Keep only necessary tokens (summarization, trimming)
- **Isolate** — Split context across sub-agents/environments

This framework has been widely adopted as a mental model for thinking about [[context-engineering]].

### Agent Design Patterns (January 2026)

A follow-up piece surveying production patterns: multi-layer action spaces, progressive disclosure, filesystem offloading, prompt caching, the Ralph Wiggum loop, and continual learning in token space.

### Anthropic Work

- Co-authored "Scaling Managed Agents: Decoupling the brain from the hands" (Anthropic Engineering Blog)
- Contributed to Anthropic's managed agents architecture: session-based durable context, sandbox-based computation, meta-harness design

## Philosophy

Lance Martin's approach emphasizes **observing what works in production** and extracting generalizable patterns. He tracks the tension between hand-crafted context engineering and **The Bitter Lesson** — the prediction that model scaling will eventually absorb many of these techniques. He has written:

> "Context management can include hand-crafted prompting for compression, spawning sub-agents, determining when / what context to offload, and how to evolve context for learning over time. The Bitter Lesson predicts that compute / model scaling often overtakes such hand-crafted approaches."

## Notable Writing

| Date | Title | Key Insight |
|---|---|---|
| 2025-06 | [Context Engineering for Agents](https://rlancemartin.github.io/2025/06/23/context_engineering/) | 4-strategy taxonomy (Write/Select/Compress/Isolate) |
| 2026-01 | [Agent Design Patterns](https://rlancemartin.github.io/2026/01/09/agent_design) | 7 production patterns from Claude Code, Manus, Cursor |
| 2025-09 | [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Anthropic's official framework (co-author) |
| — | [Scaling Managed Agents](https://www.anthropic.com/engineering/managed-agents) | Anthropic meta-harness architecture (co-author) |

## External Links

- Blog: [rlancemartin.github.io](https://rlancemartin.github.io/)
- Substack: [@lancemartin](https://substack.com/@lancemartin)
- Latent Space interview: [Context Engineering for Agents](https://www.latent.space/p/context-engineering-for-agents-lance)
- The Org: [Anthropic profile](https://theorg.com/org/anthropic/org-chart/lance-martin)

## See Also

- [[context-engineering]] — The concept page synthesizing his framework with Anthropic's
- [[anthropic]] — His current organization
- [[langchain]] — Previous organization
- [[managed-agents]] — Anthropic's meta-harness architecture (co-authored)
