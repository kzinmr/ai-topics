---
title: "Agent vs Pipeline Architecture"
created: 2026-05-31
updated: 2026-06-02
type: concept
tags: [agent-architecture, workflow, design-patterns, agentic-engineering]
related: [concepts/programmatic-tool-calling, concepts/search-as-code, concepts/rlm-recursive-language-models, concepts/codeact, concepts/agentic-search, concepts/agentic-engineering]
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

## Beyond the Binary: Hybrid Architectures (PTC, SaC, RLM)

Goedecke's pipeline vs. agent dichotomy captures the fundamental tension, but 2026 has seen the emergence of **hybrid patterns that collapse the tradeoff** — architectures that are structurally agents (LLM controls flow) but recover pipeline-like properties (predictable cost, bounded context, deterministic execution) through code orchestration and recursive decomposition.

### Programmatic Tool Calling (PTC)

[[concepts/programmatic-tool-calling]] represents the most direct bridge between the two paradigms. Instead of an agent calling tools one-at-a-time in sequential LLM round-trips (the standard agentic loop), the model generates **a single Python script** that orchestrates all tool calls programmatically — with loops, conditionals, `asyncio.gather()` parallelism, and deterministic filtering — inside a sandbox. Only the final `print()` output returns to the model.

| Goedecke's Concern | Pipeline Answer | Agent Answer | PTC Answer |
|---------------------|----------------|-------------|------------|
| **Cost predictability** | Fixed pipeline stages | Unbounded agent loops | **2 model calls** (code gen + answer) |
| **Context bloat** | Pre-assembled, bounded | Grows with each turn | **87-92% reduction** — intermediate data never enters context |
| **Multi-model flexibility** | Different models per stage | Single model throughout | Tool design can route to cheaper models internally |
| **Context-gathering** | Must solve retrieval yourself | Agent figures it out | **Agent generates code that gathers context programmatically** |

PTC resolves Goedecke's key tension: the agent decides *what* to do (flexibility), but Python code determines *how* (determinism). This is neither pipeline nor agent — it's an agent that writes its own pipeline for each task.

### Search as Code (SaC)

[[concepts/search-as-code]] (Perplexity, June 2026) is **PTC applied to the search layer**. Instead of monolithic search APIs, agents get composable SDK primitives (retrieval, ranking, filtering, fanouts) and generate Python to orchestrate them in sandboxes.

This directly addresses Goedecke's point about RAG's failure: *"Find what information is relevant to this problem is often as hard as actually solving the problem."* SaC's answer is neither RAG (embedding similarity) nor pure agent search (sequential `grep` + `read_file`) — it's **code-level control over the entire search pipeline**, where the model can compose, parallelize, and filter retrieval operations programmatically.

Results: 85.1% token reduction on CVE advisory task, SOTA on 4/5 benchmarks (DSQA, BrowseComp, WideSearch, WANDR).

### Recursive Language Models (RLM)

[[concepts/rlm-recursive-language-models]] address Goedecke's concern about **context growing in agent loops** from a different angle. RLMs treat context as a variable — the model programmatically decomposes input, recursively calls itself on sub-problems, and merges results. Each recursive call operates on a bounded context window.

| Property | Pipeline | Agent | RLM |
|----------|----------|-------|-----|
| **Context management** | Pre-bounded | Grows unboundedly | **Recursive decomposition** — each call bounded |
| **Scaling** | Linear with stages | Linear with turns | **Depth-scaled** — more recursion = more capability |
| **Model requirement** | Any | Frontier preferred | **Small model + deep recursion ≈ large model direct** |

RLMs challenge Goedecke's assumption that agents require frontier models with large context windows. A Qwen3-8B with depth-3 RLM matching a 70B model on information-dense tasks suggests the pipeline→agent binary may dissolve into **how you compose recursive context management**.

### Synthesis: The Architectural Spectrum

These patterns suggest the real landscape is a spectrum, not a binary:

```
Pipeline ←————————————————————————————→ Agent
    │         │           │           │
    │    PTC/SaC      RLM+Code    Pure Agent
    │  (agent writes  (recursive   (LLM decides
    │   its own       context      everything
    │   pipeline)     management)  each turn)
    │
  Fixed          Hybrid           Fully
  control        (LLM decides     autonomous
  flow           intent, code     control flow
                 executes)
```

**Key insight**: PTC/SaC and RLM don't replace Goedecke's framework — they validate it while showing that the "agent" side of the spectrum can recover pipeline-like efficiency. The recommendation "when in doubt, use agents" becomes even stronger when agents can write their own deterministic pipelines per-task.

## Migration Patterns

As of 2026, the industry trend is strongly **one-directional**: multiple projects have migrated from pipelines to agents, but none have gone the other way. The recommendation when unsure: **build agents first**, then migrate to pipelines if cost/latency constraints demand it.

> "When in doubt, use agents. If you want to change to a cheaper, pipeline-based system later, at least you'll be able to compare it to a working agentic design and make an informed decision."

## Related Concepts

- [[concepts/agentic-engineering]] — Engineering practices for agent-based systems
- [[concepts/agent-sandboxing]] — Security isolation for agent execution
- [[concepts/direct-corpus-interaction]] — Agents searching raw text with terminal tools
- [[concepts/defense-in-depth]] — Layered security for AI agents
- [[concepts/programmatic-tool-calling]] — PTC: agent-generated code orchestrating tool calls in sandboxes
- [[concepts/search-as-code]] — Perplexity's SaC: PTC applied to search, composable SDK primitives
- [[concepts/rlm-recursive-language-models]] — RLM: recursive context decomposition for near-infinite context
- [[concepts/codeact]] — Code-as-action paradigm that underlies PTC and SaC
- [[concepts/agentic-search]] — Evolution of search from keyword to SaC (Level 5)
