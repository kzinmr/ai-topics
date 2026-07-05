---
title: LangGraph
type: concept
created: 2026-05-08
updated: 2026-05-08
tags:
  - orchestration
  - ai-agents
  - langchain
aliases:
  - LangGraph Framework
  - LangGraph Platform
related:
  - "[[entities/langchain]]"
  - "[[entities/harrison-chase]]"
  - "[[concepts/human-in-the-loop]]"
  - "[[comparisons/agent-orchestration-frameworks]]"
  - "[[concepts/harness-engineering]]"
  - "[[concepts/deep-agents]]"
sources:
  - raw/articles/2025-04-20_langchain-how-to-think-about-agent-frameworks.md
  - "https://langchain-ai.github.io/langgraph/"
  - "https://github.com/langchain-ai/langgraph"
---

# LangGraph

**LangGraph** is a low-level, event-driven orchestration framework for building stateful, production-grade agentic systems. Created by **LangChain** (Harrison Chase), it is the successor and evolution of the original LangChain agent/chains architecture, designed to provide explicit control over what context reaches the LLM at every step.

LangGraph's philosophy is best described as **"Keras for Agents"** — high-level abstractions to get started, built on a low-level orchestration layer so developers never outgrow it.

## Architecture

LangGraph models agentic systems as **nodes and edges**:

- **Nodes** represent units of work (normal Python/TypeScript functions)
- **Edges** represent transitions between nodes (fixed or conditional)
- The graph structure is declared declaratively, but node logic is normal imperative code
- Supports **cycles**, **branching**, and **conditional routing**

### Key APIs

| API | Description |
|-----|-------------|
| **Declarative Graph API** | Recommended — define nodes and edges in a declarative graph structure |
| **Functional API** | Alternative imperative-style API for those who prefer it |
| **Event-Driven API** | Low-level access to the underlying event system |
| **Agent Abstractions** | Higher-level abstractions built on top (similar to "Keras on TensorFlow") |

### Built-in Features

1. **Persistence Layer** — Built-in state management enabling:
   - **Short-term Memory:** Multi-turn chat threads
   - **Long-term Memory:** Cross-thread memory (remembering across conversations)
   - **Fault Tolerance:** Durable workflows with configurable retries

2. **Human-in-the-loop (HITL)** — Built-in support for interrupts, approvals, manual edits, and tool call argument modification

3. **Human-on-the-loop** — "Time travel" capabilities: inspect agent trajectories, rewind to earlier steps, modify and rerun

4. **Streaming** — Real-time streaming of tokens, node transitions, and arbitrary events

5. **LangSmith Integration** — First-class debugging, evaluation, and observability via LangSmith's LLM-specific tracing

## Philosophy: Floor vs. Ceiling

Introduced by Harrison Chase in "How to think about agent frameworks" (April 2025), LangGraph is positioned on the **Floor vs. Ceiling** framework:

| Dimension | LangGraph Position |
|-----------|-------------------|
| **Floor** | Low (via agent abstractions built on top) |
| **Ceiling** | High (via low-level orchestration) |

Most other agent frameworks (OpenAI Agents SDK, CrewAI) are described as **Low Floor, Low Ceiling** — they provide easy onboarding but cannot support non-trivial use cases.

## Critique of Agent Abstractions

LangGraph was designed as a direct response to the limitations of "agent abstractions" — classes like OpenAI's Agent that take a model, prompt, and tools as parameters and hide the internal logic:

> "These abstractions end up making it really really hard to understand or control exactly what is going into the LLM at all steps. This is important — having this control is crucial for building reliable agents."

Chase explicitly calls out that the original LangChain chains/agents suffered from this same problem, and LangGraph was built to solve it.

## Workflows vs. Agents Spectrum

Rather than forcing a binary choice, LangGraph supports every point on the spectrum from fully deterministic workflows to fully autonomous agents:

- **Workflows** — LLMs orchestrated through predefined code paths (high predictability)
- **Agents** — LLMs dynamically directing their own processes via feedback loops (high flexibility)
- **Hybrid** — Most production systems combine both patterns, and LangGraph supports this natively

## Framework Comparison

Harrison Chase's [living comparison spreadsheet](https://docs.google.com/spreadsheets/d/1B37VxTBuGLeTSPVWtz7UMsCdtXrqV5hCjWkbHN8tfAo/edit?usp=sharing) evaluates LangGraph against: OpenAI Agents SDK, Google ADK, LangChain (original), CrewAI, LlamaIndex, Agno AI, Mastra, Pydantic AI, AutoGen, Temporal, SmolAgents, DSPy.

## Key Critiques of Competitors

- **OpenAI Agents SDK**: Misleadingly presents itself as "imperative" but is just an abstraction; lacks real orchestration control
- **CrewAI**: High-level abstractions without the escape hatch to low-level control
- **Original LangChain**: Admits the original chains/agents had the same abstraction problem LangGraph was built to solve

## Milestones

| Date | Milestone |
|------|-----------|
| Sep 2024 | Launched as a separate framework from LangChain |
| Oct 2025 | LangGraph 1.0 released at LangChain Series B |
| May 2025 | LangGraph Platform GA for managing long-running stateful agents |
| Apr 2025 | Harrison Chase publishes "How to think about agent frameworks" — articulating LangGraph's philosophy |

## Related Concepts

- [[entities/langchain]] — Parent company and ecosystem
- [[entities/harrison-chase]] — Creator and LangChain CEO
- [[concepts/human-in-the-loop]] — Human-AI interaction patterns LangGraph enables
- [[concepts/harness-engineering]] — Higher-level agent architecture framework
- [[comparisons/agent-orchestration-frameworks]] — Competitive landscape
- [[concepts/deep-agents]] — LangChain's open-source agent harness built on LangGraph
