---
title: Jeff Huber
type: entity
aliases:
  - "@jeffchuber"
  - "Jeff Huber (Chroma)"
created: 2026-05-13
updated: 2026-05-13
status: l2
tags:
  - person
  - entrepreneur
  - chroma
  - vector-database
  - search
  - context-engineering
  - agent-harness
  - ai-agents
  - open-source
sources:
  - https://hugobowne.substack.com/p/harness-engineering-why-agent-context
  - https://www.ia40.com/blog-podcast/chroma
  - https://www.praxis.co/people/jeff-huber
related:
  - entities/chroma
  - entities/hugo-bowne-anderson
  - entities/lance-martin
  - concepts/reduce-offload-isolate
  - concepts/context-rot
  - concepts/agent-harness-comparison
---

# Jeff Huber (@jeffchuber)

| | |
|---|---|
| **Role** | Co-founder & CEO, Chroma |
| **LinkedIn** | [jeffchuber](https://www.linkedin.com/in/jeffchuber/) |
| **GitHub** | [jeffchuber](https://github.com/jeffchuber) |
| **Location** | San Francisco, CA |
| **Background** | Economics & Industrial Engineering, N.C. State (dropped out) |
| **Known for** | Vector database pioneer (Chroma), context engineering thought leadership, agent harness engineering discourse |
| **Previous ventures** | Standard Cyborg (YC W15) — computer vision systems, acquired by Össur |

## Overview

Jeff Huber is a serial founder and engineer who co-founded **Chroma**, the leading open-source AI-native embeddings database (vector database). Chroma emerged as one of the dominant vector database offerings in the AI ecosystem, with $18M in seed funding led by Quiet Capital (2023). Huber bridges the gap between **database infrastructure** and **AI agent engineering**, articulating how vector databases and context engineering are two sides of the same coin in building reliable AI systems.

Huber's background spans 11+ years of startup experience, from computer vision at Standard Cyborg to building the database infrastructure layer for the AI era. He is a hands-on CEO who contributes code to `chroma-core`, including Python client libraries, Flask apps, and notebook integrations.

## Core Ideas

### Context Engineering > Prompt Engineering

Huber's most influential framing: prompt engineering is insufficient for production AI systems. The real job is **context engineering** — the systematic process of curating what information an LLM receives at each step.

> *"Context engineering does a few things. Number one, it is the job today. If you're looking to build a production system, that is the job: engineer your context window. Prompt engineering's like script kitty versus context engineering's more like software engineering."*

This reframing elevates context management from an ad-hoc activity to a disciplined engineering practice, emphasizing precision over volume.

### Large Context Windows Are Not a Silver Bullet

Huber identifies three reasons why simply filling large context windows fails in production:

1. **Context Rot**: LLM instruction-following degrades as context grows, especially for high-attention tasks — even in million-token models
2. **Cost and Latency**: Processing millions of tokens per turn is prohibitively slow and expensive for user-facing applications
3. **Distraction**: Irrelevant information causes agents to repeat errors they previously identified as incorrect

### The Inner Loop / Outer Loop of Context Engineering

Huber's key architectural distinction:

- **Inner Loop**: What to put into context for a single task, right now. The tactical, per-request curation problem.
- **Outer Loop**: Building systems that get better at filling context *over time*. The strategic, learning-oriented problem. The "machine that builds the machines."

This framework complements Lance Martin's **[[concepts/reduce-offload-isolate|Reduce, Offload, Isolate]]** by adding a temporal dimension: the inner loop is Reduce/Offload/Isolate applied per-task; the outer loop is the continuous improvement system that optimizes how those decisions are made.

> *"The long-term challenge is building the machine that builds the machines: systems that can learn from feedback and continuously improve their performance."*

### Code-Writing Unlocks Emergent Reasoning

Huber argues that coding agents are **general-purpose agents in disguise**. When an LLM can write and execute code:

- Code acts as a **scaffold** enabling creative composition of tools
- Multi-hop reasoning emerges naturally (e.g., importing `datetime` to determine which days were Mondays, then searching by date)
- The agent can **extend itself** — following Armin Ronacher's [[entities/pi|Pi]] philosophy: "You ask the agent to extend itself"

This is NOT primarily because models are well-trained on code (contra Cloudflare's argument). Rather, code as a medium enables emergent composition that raw tool calling cannot match.

### Practical Build Advice

From the Vanishing Gradients conversation, Huber's pragmatic recommendations for builders:

1. **Start with Hybrid Search**: Lexical (BM25) + semantic vector search as the robust default
2. **Create a Golden Dataset**: Queries + expected outcomes for system benchmarking
3. **Cluster and Analyze Data**: Use embeddings to cluster agent traces and find systemic failure patterns
4. **Engineer Tools Thoughtfully**: Provide clear descriptions and specialized tools (broad search + specific `get_document`)

## Chroma

Chroma is the AI-native open-source embeddings database co-founded by Huber. Key facts:

| | |
|---|---|
| **Founded** | 2022 |
| **Funding** | $18M seed (Quiet Capital, 2023) |
| **License** | Apache 2.0 |
| **GitHub** | [chroma-core/chroma](https://github.com/chroma-core/chroma) |
| **Type** | Vector database / Embeddings database |
| **Key feature** | Open-source, AI-native, developer-first |

Chroma positions itself as the database layer for AI applications, handling the storage and retrieval of embeddings that power RAG systems, semantic search, and agent memory. See [[entities/chroma]].

## Podcast / Media Appearances

- **Vanishing Gradients with Hugo Bowne-Anderson** (Mar 2026) — "Harness Engineering: Why Agent Context Isn't Enough" — Inner/outer loop framework, context engineering discipline, agent harness as tools+sub-agents+workflows
- **IA40 Podcast with Vivek Ramaswami** (2023) — Chroma founding story, vector database market, community-led growth, competitive landscape
- Multiple AI/ML conference talks on vector databases, RAG, and production AI systems

## Related People

- [[entities/hugo-bowne-anderson]] — Host of the Vanishing Gradients conversation; central hub for harness engineering discourse
- [[entities/lance-martin]] — Complementary framework: Reduce/Offload/Isolate; both articulate context engineering discipline
- [[entities/ivan-leo]] — Self-extending agents via code-writing; practical implementation of Huber's thesis
- [[entities/doug-turnbull]] — Agentic search collaborator; practical application of context engineering to retrieval

## See Also

- [[concepts/reduce-offload-isolate]] — Lance Martin's complementary 3-principle framework
- [[concepts/agent-harness-comparison]] — Comparative analysis of major agent harnesses
- [[entities/chroma]] — Chroma vector database
