---
title: "Han Lee (Hanchung Lee)"
created: 2026-05-15
updated: 2026-05-15
type: person
tags:
  - person
  - researcher
  - ai-infrastructure
  - agent-runtime
  - ml-engineering
  - technical-debt
aliases: [Hanchung Lee, Han-chung Lee, leehanchung]
sources:
  - "https://leehanchung.github.io/about/"
  - "https://www.linkedin.com/in/hanchunglee"
  - "https://github.com/leehanchung"
  - "https://www.twitter.com/HanchungLee"
  - "raw/articles/2026-04-24_leehanchung_hidden-technical-debt-agent-runtime.md"
---

# Han Lee

## Overview

Han Lee (Hanchung Lee) is a machine learning engineer and **Senior Director of Data + AI at Moody's Analytics**, based in the San Francisco Bay Area. He leads teams building custom LLMs, generative AI applications, and search/discovery engines for financial data. He writes the blog **"Han, Not Solo"** (leehanchung.github.io), covering ML engineering, compound AI systems, LLM agents, and data science.

His 2026 article [Hidden Technical Debt of AI Systems: Agent Runtime](https://leehanchung.github.io/blogs/2026/04/24/hidden-technical-debt-agent-runtime/) has become a foundational reference in the agent infrastructure discourse, drawing a direct parallel between Sculley et al.'s classic "Hidden Technical Debt in ML Systems" and the emerging debt patterns in agent serving infrastructure.

## Key Articles

### Agent Runtime & Infrastructure

- **[Hidden Technical Debt of AI Systems: Agent Runtime](https://leehanchung.github.io/blogs/2026/04/24/hidden-technical-debt-agent-runtime/)** (Apr 2026) — The definitive article establishing **agent runtime** as the critical underinvested layer in agent systems. Covers: isolation primitive stack (containers → Firecracker → gVisor → Kata → V8 isolates), sandbox vendor landscape, experiment-vs-production runtime divergence, **runtime shift** (a new flavor of distributional shift), and **runtime debt**. Directly linked to [[concepts/agent-runtime]].
- **[A Taxonomy of RL Environments for LLM Agents](https://leehanchung.github.io/blogs/2026/03/21/rl-environments-for-llm-agents/)** (Mar 2026) — Formally defines the $H$ (harness) and $S$ (state) components of agent RL environments. Framework used throughout the agent runtime article.

### Broader AI Commentary

- **[The AI Great Leap Forward](https://leehanchung.github.io/blogs/2026/04/05/the-ai-great-leap-forward/)** (Apr 2026) — Commentary on the acceleration of AI development.

## Roles & Affiliations

| Role | Organization |
|---|---|
| Senior Director - Data + AI | Moody's Analytics |
| Technical Reviewer | Chip Huyen's "AI Engineering" (O'Reilly, 2025) |
| Blog Author | "Han, Not Solo" (leehanchung.github.io) |

## Online Presence

- **Blog**: [leehanchung.github.io](https://leehanchung.github.io/)
- **GitHub**: [github.com/leehanchung](https://github.com/leehanchung)
- **LinkedIn**: [linkedin.com/in/hanchunglee](https://www.linkedin.com/in/hanchunglee) (500+ connections, 6,914 followers)
- **X/Twitter**: [@HanchungLee](https://www.twitter.com/HanchungLee)
- **Email**: lee [dot] hanchung [at] gmail [dot] com

## Contributions to AI Engineering Discourse

1. **Agent Runtime Taxonomy** — Defined the six components of an agent runtime (compute substrate, filesystem, tools, network boundary, state model, lifecycle controller), now a reference framework in agent infrastructure discussions.
2. **Runtime Shift** — Identified that agents learn their runtime's quirks (tool latencies, failure modes, shell output formats), and that moving to a different runtime causes silent quality regressions. Proposed three paths: co-location, runtime contract, and training against production noise.
3. **Isolation Primitive Analysis** — Produced the most comprehensive public comparison of the five isolation primitives for agent workloads (containers, Firecracker, gVisor, Kata, V8 isolates) with production evidence from Cognition, Manus, and Ramp.
4. **Technical Debt Framework for Agents** — Extended Sculley et al.'s classic framework to agent systems, introducing the concept of "runtime debt" — the compounding cost of entangling agent behavior with a specific runtime's quirks.

## Related Wiki Pages

- [[concepts/agent-runtime]] — Comprehensive concept page built from Lee's article
- [[concepts/agent-harness]] — The harness runs inside the runtime; Lee's taxonomy formalizes $H$ and $S$
- [[concepts/reduce-offload-isolate]] — Anthropic's context engineering approach complements runtime isolation
- [[entities/cognition]] — Devin's cloud agent infrastructure (cited in Lee's article)
- [[entities/manus]] — Agent runtime snapshotting (cited)
- [[entities/modal]] — Sandbox infrastructure (Ramp Inspect case study cited)
