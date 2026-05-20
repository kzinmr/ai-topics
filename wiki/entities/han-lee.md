---
title: "Han Lee (Hanchung Lee)"
created: 2026-05-15
updated: 2026-05-20
type: person
tags:
  - person
  - infrastructure
  - agent-runtime
  - agent-harness
  - technical-debt
  - evaluation
  - ai-adoption
aliases: [Hanchung Lee, Han-chung Lee, leehanchung]
sources:
  - "https://leehanchung.github.io/about/"
  - "https://www.linkedin.com/in/hanchunglee"
  - "https://github.com/leehanchung"
  - "https://www.twitter.com/HanchungLee"
  - "https://leehanchung.github.io/feed.xml"
  - "raw/articles/2026-04-24_leehanchung_hidden-technical-debt-agent-runtime.md"
  - "raw/articles/2026-05-08_leehanchung_hidden-technical-debt-agent-harness.md"
  - "raw/articles/2026-05-10_leehanchung_data-aggregation-is-not-a-moat.md"
  - "raw/articles/2026-05-01_leehanchung_dont-outsource-your-understanding.md"
  - "raw/articles/2026-04-07_leehanchung_determinism-biggest-cope-in-ai-adoption.md"
  - "raw/articles/2026-03-21_leehanchung_rl-environments-for-llm-agents.md"
---

# Han Lee

## Overview

Han Lee (Hanchung Lee) is a machine learning engineer and **Senior Director of Data + AI at Moody's Analytics**, based in the San Francisco Bay Area. He leads teams building custom LLMs, generative AI applications, and search/discovery engines for financial data. He writes the blog **"Han, Not Solo"** (leehanchung.github.io), covering ML engineering, compound AI systems, LLM agents, data science, and AI adoption.

His 2026 article series **"Hidden Technical Debt of AI Systems"** — grounded in the formal $E = \{T, H, V, S, C\}$ framework from [A Taxonomy of RL Environments for LLM Agents](https://leehanchung.github.io/blogs/2026/03/21/rl-environments-for-llm-agents/), then applied to [Agent Runtime](https://leehanchung.github.io/blogs/2026/04/24/hidden-technical-debt-agent-runtime/) and extended to [Agent Harness](https://leehanchung.github.io/blogs/2026/05/08/hidden-technical-debt-agent-harness/) — has become foundational in the agent infrastructure discourse, drawing direct parallels to Sculley et al.'s classic "Hidden Technical Debt in ML Systems."

## Monitoring

| Source | Method | Status |
|--------|--------|--------|
| RSS Feed | [feed.xml](https://leehanchung.github.io/feed.xml) | ✅ Active (added 2026-05-20; RSS → blogwatcher → daily `blog-ingest` pipeline) |
| X/Twitter | [@HanchungLee](https://x.com/HanchungLee) | ❌ Not yet tracked in `x-accounts.yaml` |

## Key Articles

### Hidden Technical Debt Series

- **[Hidden Technical Debt of AI Systems: Agent Runtime](https://leehanchung.github.io/blogs/2026/04/24/hidden-technical-debt-agent-runtime/)** (Apr 2026) — The definitive article establishing **agent runtime** as the critical underinvested layer in agent systems. Covers: isolation primitive stack (containers → Firecracker → gVisor → Kata → V8 isolates), sandbox vendor landscape, experiment-vs-production runtime divergence, **runtime shift** (a new flavor of distributional shift), and **runtime debt**. Raw: [[raw/articles/2026-04-24_leehanchung_hidden-technical-debt-agent-runtime]]. Directly linked to [[concepts/agent-runtime]].
- **[Hidden Technical Debt of AI Systems: Agent Harness](https://leehanchung.github.io/blogs/2026/05/08/hidden-technical-debt-agent-harness/)** (May 2026) — Third in the series. Deconstructs the **agent harness**: the orchestration layer (system prompts, tool surfaces, rollout protocols, context managers, memory, sub-agent topologies, guardrails, verifiers, observability). Key contributions: (1) **training vs production harness asymmetry** — they are different artifacts and should be engineered separately; (2) **first-party vs third-party harness** dynamics — models run out-of-distribution in third-party harnesses, but third parties can win on neglected axes (e.g., Letta Code's memory investment); (3) **five harness design principles** including "treat the harness as temporary scaffolding." Raw: [[raw/articles/2026-05-08_leehanchung_hidden-technical-debt-agent-harness]].

### AI Agent Infrastructure & Theory

- **[A Taxonomy of RL Environments for LLM Agents](https://leehanchung.github.io/blogs/2026/03/21/rl-environments-for-llm-agents/)** (Mar 2026) — **Foundational first article** in the "Hidden Technical Debt" series. Formally defines the RL environment as $E = \{T, H, V, S, C\}$ — tasks, agent harness, verifier, state management, configuration. Establishes the $H$ (harness) and $S$ (state) framework used throughout the Agent Runtime and Agent Harness articles. Includes task taxonomy (10 types), rollout protocol classification, tools landscape, verifier types (exact match → LLM-as-Judge → execution-based → hybrid), and context management strategies for 600+ turn episodes. Raw: [[raw/articles/2026-03-21_leehanchung_rl-environments-for-llm-agents]].

### AI Adoption & Evaluation

- **[Data Aggregation Is Not a Moat](https://leehanchung.github.io/blogs/2026/05/10/data-aggregation-is-not-a-moat/)** (May 2026) — Argues that AI agents collapse the cost structure of data aggregation businesses. Most "data moats" are operational competence, not data ownership. Value shifts from "who collected the data" → "who can produce decision-quality answers that are current, verified, auditable, and integrated." Case study of OpenAI/Anthropic's full value chain (crawlers → model weights → intelligence-as-a-service). Raw: [[raw/articles/2026-05-10_leehanchung_data-aggregation-is-not-a-moat]].
- **[Don't Outsource Your Understanding](https://leehanchung.github.io/blogs/2026/05/01/dont-outsource-your-understanding/)** (May 2026) — Distinguishes **cognitive offloading** (human verifies) from **cognitive surrender** (human delegates verification too). Catalogs the pattern across law (1,300+ hallucinated filings, $145K+ sanctions in Q1 2026), software (vibe-coding "slop-field"), corporate comms, academia (ICLR fabricated references), and engineering ops. Antidote: "Read the agent's output. Walk one path through the code. This reconstruction is the work." Raw: [[raw/articles/2026-05-01_leehanchung_dont-outsource-your-understanding]].
- **["Determinism" is the Biggest Cope in AI Adoption](https://leehanchung.github.io/blogs/2026/04/07/determinism-biggest-cope-in-ai-adoption/)** (Apr 2026) — Argues determinism was never guaranteed in software (Halting Problem, Rice's Theorem). The real shift with AI is from pre-deployment code verification → continuous evaluation. Six Sigma parallel: "define, measure, analyze, improve, control" — evaluation, not determinism. Raw: [[raw/articles/2026-04-07_leehanchung_determinism-biggest-cope-in-ai-adoption]].

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
- **RSS**: [feed.xml](https://leehanchung.github.io/feed.xml)
- **GitHub**: [github.com/leehanchung](https://github.com/leehanchung)
- **LinkedIn**: [linkedin.com/in/hanchunglee](https://www.linkedin.com/in/hanchunglee) (500+ connections, 6,914 followers)
- **X/Twitter**: [@HanchungLee](https://x.com/HanchungLee)
- **Email**: lee [dot] hanchung [at] gmail [dot] com

## Contributions to AI Engineering Discourse

1. **Agent Runtime Taxonomy** — Defined the six components of an agent runtime (compute substrate, filesystem, tools, network boundary, state model, lifecycle controller), now a reference framework in agent infrastructure discussions.
2. **Runtime Shift** — Identified that agents learn their runtime's quirks (tool latencies, failure modes, shell output formats), and that moving to a different runtime causes silent quality regressions. Proposed three paths: co-location, runtime contract, and training against production noise.
3. **Isolation Primitive Analysis** — Produced the most comprehensive public comparison of the five isolation primitives for agent workloads (containers, Firecracker, gVisor, Kata, V8 isolates) with production evidence from Cognition, Manus, and Ramp.
4. **Technical Debt Framework for Agents** — Extended Sculley et al.'s classic framework to agent systems, introducing "runtime debt" (Agent Runtime article) and "harness debt" (Agent Harness article). Key insight: most harness code is temporary scaffolding that the next generation of models will absorb.
5. **Training vs Production Harness Asymmetry** — Articulated why the training harness and production harness must be different artifacts with different owners, and that the evaluation harness bridging them is where the real moat lies.
6. **Cognitive Offloading vs Cognitive Surrender** — Popularized the distinction (from Shaw & Nave, 2026) with vivid cross-domain examples, establishing the practical rule: "outsource everything else, don't outsource your understanding."
7. **Data Moat Deconstruction** — Argued that AI agents collapse the cost structure of data aggregation, shifting defensibility from "who collected it" to "who can produce verified, auditable, decision-quality answers."

## Related Wiki Pages

- [[concepts/agent-runtime]] — Comprehensive concept page built from Lee's Agent Runtime article
- [[concepts/agent-harness]] — The harness runs inside the runtime; Lee's taxonomy formalizes $H$ and $S$
- [[concepts/reduce-offload-isolate]] — Anthropic's context engineering approach complements runtime isolation
- [[entities/cognition]] — Devin's cloud agent infrastructure (cited in Lee's article)
- [[entities/manus]] — Agent runtime snapshotting (cited)
- [[entities/modal]] — Sandbox infrastructure (Ramp Inspect case study cited)
- [[entities/letta]] — Letta Code's memory investment as third-party harness advantage (Agent Harness article)
