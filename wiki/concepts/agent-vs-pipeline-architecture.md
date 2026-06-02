---
title: "Agent vs Pipeline Architecture"
created: 2026-05-31
updated: 2026-06-02
type: concept
tags: [agent-architecture, workflow, design-patterns, agentic-engineering]
sources:
  - raw/articles/seangoedecke.com--build-agents-not-pipelines--43a57b4a.md
---

# Agent vs Pipeline Architecture

Two fundamental approaches to building systems with LLMs: **pipelines** (control flow in code) and **agents** (control flow delegated to the LLM). This distinction is one of the most important architectural decisions in AI application design in 2026.

## Core Distinction

| | **Pipeline** | **Agent** |
|---|---|---|
| **Control flow** | Defined in code by the developer | Managed by the LLM at runtime |
| **Context assembly** | Pre-gathered before LLM invocation | Gathered dynamically by the agent |
| **Execution model** | Linear sequence: input → transform → output | Loop: observe → think → act → repeat |
| **Library vs Framework** | Library — you call the LLM as a helper | Framework — the LLM calls your tools |

### Pipeline Example
```python
context = gather_context(data_sources)
llm_response = llm_summarize(context)
summary = parse(llm_response)
email_me(summary, my_email)
```

### Agent Example
```python
read_data_tool = build_read_data_tool(data_sources)
email_tool = build_email_tool(my_email)
run_agent(tools=[read_data_tool, email_tool])
```

## Tradeoffs

### When to Use Pipelines

1. **Strict context size requirements** — Pipelines work with smaller, bounded contexts
2. **Predictable cost/latency** — Each LLM call has known token counts and costs
3. **Local model deployment** — Limited VRAM (under 32K tokens) forces pipeline design
4. **Multi-model architectures** — Use different models for different pipeline stages
5. **Production at scale** — When running millions of invocations, cost predictability matters

### When to Use Agents

1. **Unknown context requirements** — When you can't pre-assemble all relevant data
2. **Hard problems** — When the task difficulty exceeds what a single prompt can handle
3. **Coding tasks** — "The most successful AI products (Claude Code, Codex, Cursor, Copilot) are agents because coding is too hard for pipelines"
4. **Reactive workflows** — When the system needs to take action and react to results
5. **Future-proofing** — Agent systems benefit more from model improvements over time

## Context-Gathering: The Key Differentiator

The most significant practical difference between pipelines and agents is **context assembly**:

- **Pipeline**: All required data must be present before the LLM runs. This is often the hardest part of building a pipeline — you must solve retrieval, ranking, and relevance yourself.
- **Agent**: The agent can decide what data to fetch and when. You provide tools (`grep`, `read_file`, `web_search`) and let the agent figure out what's relevant.

> "Find what information is relevant to this problem" is often as hard as actually solving the problem. Semantic embeddings and cosine similarity are not powerful enough tools for the job. Agents solve this by doing plain-text search like a human would.

### Why RAG Didn't Replace Agents

In 2023-2024, many believed RAG would solve context-gathering permanently. It didn't happen because:
1. Semantic embeddings miss subtle but critical context
2. "Finding relevant information" is often harder than solving the actual task
3. Agents with simple tools (grep, read) outperform complex embedding pipelines in practice

## Multi-Model Pipelines vs Agent Tool Design

Pipelines can use different LLMs for different stages (cheap model for summarization, expensive model for reasoning). However:

- The signal is often in the raw data itself
- Summarizing before reasoning can lose important information
- This can also be done in agents via tool design (e.g., a `web_search` tool that internally uses a cheaper model)

## Safety and Legibility

### Sandboxing
Both pipelines and agents face the same prompt injection and action-safety problems. Whether you're feeding data directly into a prompt (pipeline) or through tool calls (agent), the LLM sees human-generated content either way. **Sanitization and action verification are required in both architectures.**

### Legibility
- **Pipelines** are slightly more traceable — you control the flow
- **Agents** are harder to debug — the LLM decides what actions to take
- However, neither architecture gives you full transparency into *why* the LLM made its decisions

## Real-World Example: LLM-Driven Analysis at Scale

Consider building a system to analyze millions of documents:

1. **Pipeline layer**: Cheap, fast classification of every document — flags interesting items
2. **Agent layer**: Fleet of agents that investigate flagged items, make queries, react to findings — like human analysts

This hybrid approach uses pipelines for scale and agents for depth. The pipeline scales predictably with volume; the agents scale independently but are bottlenecked on GPU availability and human review.

## Migration Patterns

As of 2026, the industry trend is strongly **one-directional**: multiple projects have migrated from pipelines to agents, but none have gone the other way. The recommendation when unsure: **build agents first**, then migrate to pipelines if cost/latency constraints demand it.

> "When in doubt, use agents. If you want to change to a cheaper, pipeline-based system later, at least you'll be able to compare it to a working agentic design and make an informed decision."

## Related Concepts

- [[concepts/agentic-engineering]] — Engineering practices for agent-based systems
- [[concepts/agent-sandboxing]] — Security isolation for agent execution
- [[concepts/direct-corpus-interaction]] — Agents searching raw text with terminal tools
- [[concepts/defense-in-depth]] — Layered security for AI agents
