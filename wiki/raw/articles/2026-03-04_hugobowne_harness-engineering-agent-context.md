---
title: "Harness Engineering: Why Agent Context Isn't Enough"
source: "Vanishing Gradients (Hugo Bowne-Anderson)"
source_url: "https://hugobowne.substack.com/p/harness-engineering-why-agent-context"
date_published: 2026-03-04
date_scraped: 2026-05-13
authors:
  - Hugo Bowne-Anderson
featured_guest: Jeff Huber
guest_affiliation: Chroma (CEO & Co-founder)
type: article
tags:
  - agent-harness
  - context-engineering
  - ai-agents
  - llm
  - search
  - rag
  - chroma
---

# Harness Engineering: Why Agent Context Isn't Enough

**Published**: Mar 04, 2026 | **Author**: Hugo Bowne-Anderson | **Guest**: Jeff Huber (CEO & Co-founder, Chroma)

## Summary

Hugo Bowne-Anderson distills key insights from a Vanishing Gradients podcast conversation with Jeff Huber, CEO and co-founder of Chroma, covering the paradigm shift to agentic search, context engineering as the central discipline, the agent harness as tool suite + sub-agents + workflows, and the inner vs outer loop of context engineering.

## Key Themes

### From Human Queries to Agentic Search

- Paradigm shift: humans manually search → AI agents perform complex multi-hop searches, synthesizing from hundreds/thousands of sources
- Agentic search: agent executes many queries in sequence, composes results
- Challenge: transferring human search intuition (when to start, stop, change strategies) into automated systems

### Context Engineering: The Real Job

> *"Context engineering does a few things. Number one, it is the job today. If you're looking to build a production system, that is the job: engineer your context window. Prompt engineering's like script kitty versus context engineering's more like software engineering."* — Jeff Huber

Why simply filling a large context window is not viable:
1. **Context Rot**: LLM performance degrades as context size increases, especially for high-attention tasks
2. **Cost and Latency**: Processing millions of tokens is slow and expensive for user-facing apps
3. **Distraction**: Irrelevant information causes agents to make mistakes or repeat errors

### Building the Agent Harness

The agent harness = tools + sub-agents + workflows:
- Ability to write and execute code
- Access to filesystem for planning/scratchpad
- Suite of search tools with clear descriptions
- Power to spawn specialized sub-agents for specific tasks

**Coding agents are general-purpose agents**: Code acts as a scaffold that enables creative composition of tools, unlocking emergent multi-hop reasoning. (Cloudflare argued this is because models are well-trained on code; Jeff argued code itself is the enabler.)

> *"If you want the agent to do something that it doesn't do yet, you don't go and download an extension... You ask the agent to extend itself. It celebrates the idea of code writing and running code."* — Armin Ronacher on Pi

### Practical Advice for Agentic Retrieval

1. **Start with Hybrid Search**: Lexical (BM25) + semantic vector search as robust default
2. **Create a Golden Dataset**: Queries + expected outcomes for benchmarking
3. **Cluster and Analyze Your Data**: Embeddings to cluster agent traces, find systemic patterns
4. **Engineer Your Tools Thoughtfully**: Clear descriptions, specialized tools (broad search + specific get_document)

### Inner Loop vs Outer Loop of Context Engineering

- **Inner Loop**: Figuring out what information to put into context for a single task, right now.
- **Outer Loop**: Building systems that get better at filling context over time. The "machine that builds the machines."

The long-term challenge: building systems that learn from feedback and continuously improve — moving from 90% reliability (internal tools) to 99.9%+ (user-facing products). Agent evaluation remains largely unsolved.

### Key Takeaways

1. Agentic search is the new paradigm — AI performs complex multi-step research
2. Context engineering is the central job — discipline of curating information fed to the model
3. Large context windows are not a silver bullet — context rot, cost, latency, distraction
4. The agent harness is critical — capabilities defined by tools, sub-agents, environment
5. Focus on the outer loop — durable advantage from systems that learn and improve over time
