---
title: "John Berryman"
type: entity
aliases: [JnBrymn, john-berryman]
status: complete
created: 2026-05-13
updated: 2026-05-13
tags:
  - person
  - agent-harness
  - ai-agents
  - search
  - information-retrieval
  - blogger
  - ai-product
sources:
  - raw/articles/2026-04-24_arcturus-labs_unharnessed-agents.md
  - https://blog.jnbrymn.com/about/
  - https://arcturus-labs.com/blog/
social:
  x: "@JnBrymn"
  github: "JnBrymn"
  blog: "https://blog.jnbrymn.com"
---

# John Berryman

**Founder of Arcturus Labs, search engineer, AI product thinker, author.** Former early engineer on **GitHub Copilot** (completions and chat). Co-author of *Relevant Search* and *Prompt Engineering for LLMs*. Known for the "unharnessed agents" thesis — arguing that "agent harness" is the wrong frame and agents should leave the IDE.

| Field | Value |
|---|---|
| Handle | [@JnBrymn](https://twitter.com/JnBrymn) |
| Blog | https://blog.jnbrymn.com (Thought Box) |
| Company | https://arcturus-labs.com |
| GitHub | [@JnBrymn](https://github.com/JnBrymn) |
| Books | *Relevant Search* (2016, Manning), *Prompt Engineering for LLMs* (2025, O'Reilly) |

---

## Career

| Period | Role | Organization | Key Work |
|---|---|---|---|
| Pre-2020 | Search Engineer | US Patent Office, Eventbrite, GitHub | Built next-gen patent search, Eventbrite search/recommendations, GitHub code search |
| ~2020–2023 | Early Engineer, Copilot | **GitHub / Microsoft** | Built completions and chat features for GitHub Copilot |
| 2024–present | Founder | **Arcturus Labs** | Helps startups/enterprises build production AI apps (RAG, agents, LLM applications) |

## Key Ideas

### Unharnessed Agents (April 2026)

Berryman's most influential thesis, articulated in ["Unharnessed Agents Power the Future of AI Products"](https://arcturus-labs.com/blog/2026/04/24/unharnessed-agents-power-the-future-of-ai-products/):

- **"Agent harness" is the wrong frame** — The agent IS the whole composition (while loop, LLM calls, tool calls, context management, skills, MCP). The agent is the "agent harness."
- **Agents should leave the IDE** — Agents should be personal assistants, interface builders, workflow operators across every part of digital life
- **Skills are the new programs** — English is the new programming language, agents are the new runtime. Skills can create, improve, and compose other skills dynamically
- **Standardize agent primitives** — We need Lego-block composable agent modules (compaction, pruning, memory, auth) so agents can be assembled rather than built from scratch
- **Form a standards committee** — Catalog real agent behaviors across tasks/environments/users to define how agents should be built and behave

See: [[concepts/unharnessed-agents]]

This thesis forms a complementary tension with [[concepts/harness-commoditization|Amp's "The Coding Agent Is Dead"]]:
- **Amp/Thorsten Ball**: Harness differentiation is dead because models absorb harness functionality → the harness doesn't matter
- **Berryman**: The term "harness" itself is misleading → call them agents and let them leave the IDE

Both agree the current "harness" framing is limiting, but draw opposite conclusions about what comes next.

### The AI Product Eras Framework (March 2026)

In ["The AI Product Era You're Building For Might Already Be Over"](https://arcturus-labs.com/blog/2026/03/22/the-ai-product-era-youre-building-for-might-already-be-over/), Berryman traces five eras of AI product development — from prompt engineering to agentic runtimes — arguing each era absorbs and buries the last. The trajectory informs what to build next.

### Agentic Search (March 2026)

With Tobasum Mandal, demonstrated that wrapping existing search in an agentic loop improves results without expensive infrastructure changes. See: [[entities/doug-turnbull]]

### The Dark Factory (May 2026)

Documented Twin Sun's automated dev pipeline: 70% of PRs approved autonomously with no human review. A production case study in AI-driven software development.

### Context Engineering & AI Empathy (October 2025)

Argued that effective context engineering requires "AI empathy" — thinking like an AI intern on their first day. Understanding the model's attention patterns (ADHD-like), providing proper tools and clear instructions.

## Books

| Title | Year | Co-Authors | Notes |
|---|---|---|---|
| ***Relevant Search*** | 2016 | [[entities/doug-turnbull|Doug Turnbull]] | Standard practical reference for search relevance with Elasticsearch and Solr. 360 pages. |
| ***Prompt Engineering for LLMs*** | 2025 | Sathvik Nair, Ben Auffarth, Max Humber | O'Reilly guide to prompt engineering patterns and practices |

## Arcturus Labs Blog — Notable Articles

| Date | Title | Theme |
|---|---|---|
| 2026-05-03 | [The Dark Factory: How Twin Sun Automated Their Entire Dev Pipeline](https://arcturus-labs.com/blog/2026/05/03/the-dark-factory-how-twin-sun-automated-their-entire-dev-pipeline/) | AI dev pipeline, 70% autonomous PR approval |
| 2026-04-24 | [Unharnessed Agents Power the Future of AI Products](https://arcturus-labs.com/blog/2026/04/24/unharnessed-agents-power-the-future-of-ai-products/) | Anti-harness thesis, agents leave IDE |
| 2026-03-22 | [The AI Product Era You're Building For Might Already Be Over](https://arcturus-labs.com/blog/2026/03/22/the-ai-product-era-youre-building-for-might-already-be-over/) | Five eras of AI product development |
| 2026-03-10 | [Make AI Your Search Team](https://arcturus-labs.com/blog/2026/03/10/make-ai-your-search-team/) | Agent-wrapped product search |
| 2026-02-05 | [Anthropic SKILLs – Prime Example of Red Riding Hood Principle](https://arcturus-labs.com/blog/2026/02/05/anthropic-skills--prime-example-of-red-riding-hood-principle/) | Filesystem metaphors for agent reliability |
| 2026-01-18 | [Incremental AI Adoption for E-commerce](https://arcturus-labs.com/blog/2026/01/18/incremental-ai-adoption-for-e-commerce/) | 5-level agentic search maturity model (Level 0-4). Presented on Vanishing Gradients Ep. 68. [[raw/articles/2026-01-18_arcturus-labs_incremental-ai-adoption-ecommerce-5level]] |
| 2025-12-07 | [Programming in English](https://arcturus-labs.com/blog/2025/12/07/programming-in-english/) | English as programming language, agents as runtime |
| 2025-10-25 | [Context Engineering Requires AI Empathy](https://arcturus-labs.com/blog/2025/10/25/context-engineering-requires-ai-empathy/) | AI empathy for better context engineering |
| 2025-06-17 | [Recipes – A Pattern for Common Code Transformations](https://arcturus-labs.com/blog/2025/06/17/recipes--a-pattern-for-common-code-transformations/) | Recipe pattern for vibe coding |

## Podcast Appearances

- **Vanishing Gradients Ep. 68** — "A Builder's Guide to Agentic Search & Retrieval" with Hugo Bowne-Anderson and Doug Turnbull. Presented 5-level agentic search maturity model. See: [[entities/hugo-bowne-anderson]]

## Related

- [[entities/doug-turnbull]] — Co-author of *Relevant Search*, search relevance collaborator
- [[entities/hugo-bowne-anderson]] — Podcast collaborator, Vanishing Gradients Ep. 68
- [[concepts/unharnessed-agents]] — Concept page for the anti-harness thesis
- [[concepts/harness-commoditization]] — Complementary thesis from Amp/Thorsten Ball
- [[concepts/agent-harness-comparison]] — Broader harness comparison landscape

## References

- [Arcturus Labs Blog](https://arcturus-labs.com/blog/)
- [Thought Box (Personal Blog)](https://blog.jnbrymn.com/)
- [X/Twitter @JnBrymn](https://twitter.com/JnBrymn)
- [GitHub @JnBrymn](https://github.com/JnBrymn)
- [LinkedIn](https://www.linkedin.com/in/jnberryman/)

## Log

- **2026-05-13**: Entity page created from multi-source research (Arcturus Labs blog, Thought Box about page, podcast appearances). Key ideas: unharnessed agents thesis, AI product eras, agentic search, dark factory, context engineering. Moved from concepts/john-berryman.md stub.
