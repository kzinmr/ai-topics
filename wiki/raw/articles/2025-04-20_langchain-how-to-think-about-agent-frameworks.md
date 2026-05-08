---
title: "How to think about agent frameworks"
source: LangChain Blog
url: https://www.langchain.com/blog/how-to-think-about-agent-frameworks
author: Harrison Chase
date_published: 2025-04-20
date_scraped: 2026-05-08
tags:
  - agent-frameworks
  - langgraph
  - harrison-chase
  - orchestration
  - agent-abstractions
  - workflows-vs-agents
---

# How to Think About Agent Frameworks

**Author:** Harrison Chase (LangChain CEO)
**Published:** April 20, 2025
**Read time:** 20 min

## TL;DR (from the article)

- The hard part of building reliable agentic systems is making sure the LLM has the appropriate context at each step. This includes both controlling the exact content that goes into the LLM, as well as running the appropriate steps to generate relevant content.
- Agentic systems consist of both workflows and agents (and everything in between).
- Most agentic frameworks are neither declarative or imperative orchestration frameworks, but rather just a set of agent abstractions.
- Agent abstractions can make it easy to get started, but they can often obfuscate and make it hard to make sure the LLM has the appropriate context at each step.
- Agentic systems of all shapes and sizes (agents or workflows) all benefit from the same set of helpful features, which can be provided by a framework, or built from scratch.
- LangGraph is best thought of as a orchestration framework (with both declarative and imperative APIs), with a series of agent abstractions built on top.

## Key Contributions

### 1. The "Context" Problem
The primary challenge in building reliable agentic systems is **context management** — making sure the LLM has the appropriate context at each step. Common causes of context failure:
- Incomplete/short system messages or vague user input
- Poor tool descriptions or lack of access to the right tools
- Poorly formatted tool responses
- **Framework Obfuscation:** Abstractions that make it impossible to see or control what is being passed to the LLM

### 2. Workflows vs Agents (Spectrum, Not Binary)
Rather than a binary choice, systems exist on a spectrum of **"agenticness."**
- **Workflows:** LLMs and tools orchestrated through predefined code paths. High predictability, lower flexibility.
- **Agents:** LLMs dynamically direct their own processes and tool usage via feedback loops. High flexibility, lower predictability.
- **Agentic Systems:** Most effective production systems are a combination of both.

### 3. The "Floor vs. Ceiling" Framework
A framework for evaluating agent frameworks:
- **Low Floor:** Easy to start (beginner-friendly)
- **High Floor:** Steep learning curve (requires expertise)
- **Low Ceiling:** Limited capabilities; easy to outgrow
- **High Ceiling:** Extensive flexibility for advanced use cases

Insight: Most "Agent Abstractions" (OpenAI SDK, CrewAI, early LangChain) are **Low Floor, Low Ceiling** — they get you started fast but fail when you need granular control.

### 4. Critique of Agent Abstractions
Chase argues that frameworks like OpenAI Agents SDK and similar "black-box" abstractions make it hard to understand or control what goes into the LLM at each step. Comparison:

| Feature | Agent Abstractions (OpenAI SDK, CrewAI) | Orchestration Frameworks (LangGraph) |
|---------|----------------------------------------|--------------------------------------|
| Logic | Hidden inside class methods | Explicitly defined in nodes and edges |
| Control | Hard to modify context flow | Full control over every step |
| Flexibility | Limited to what the abstraction allows | Supports workflows, agents, and hybrids |
| Nature | Set of parameters (Prompt, Model, Tools) | Low-level orchestration layer |

### 5. What a Framework Should Provide
Beyond abstractions, a framework should provide:
1. **Short-term Memory:** Managing multi-turn chat threads
2. **Long-term Memory:** Remembering information across conversations
3. **Human-in-the-loop:** Interrupts, approvals, manual edits
4. **Human-on-the-loop:** Time travel — inspect, rewind, rerun trajectories
5. **Streaming:** Real-time tokens and node transitions
6. **Fault Tolerance:** Durable execution and configurable retries
7. **Debugging/Observability:** LLM-specific (not traditional) observability
8. **Optimization:** (Future) automatic prompt optimization via evaluation datasets

### 6. Will Agents Replace Workflows?
Chase argues **no**, for two reasons:
- **Unique Tasks:** Most enterprise tasks are unique — a generic agent won't have specific procedural knowledge
- **Efficiency:** Workflows remain cheaper, faster, and more deterministic for well-defined tasks

### 7. Framework Comparison Spreadsheet
Chase published a [living comparison spreadsheet](https://docs.google.com/spreadsheets/d/1B37VxTBuGLeTSPVWtz7UMsCdtXrqV5hCjWkbHN8tfAo/edit?usp=sharing) comparing: Agents SDK, Google ADK, LangChain, CrewAI, LlamaIndex, Agno AI, Mastra, Pydantic AI, AutoGen, Temporal, SmolAgents, DSPy.

## Notable Arguments

### Open vs Imperative Debate
Chase argues the "declarative vs non-declarative" framing by OpenAI is a false dichotomy — frameworks like Agents SDK are neither declarative nor imperative orchestration frameworks; they are **just abstractions** with internal logic hidden behind a class.

### The "Keras for Agents" Philosophy
LangGraph aims to be like Keras: high-level abstractions to start, built on a low-level orchestration framework so you never outgrow it.

### Code as a Breakout Use Case
Coding agents (Claude Code, Codex CLI) are identified as the strongest example of the simple tool-calling loop working well because coding is a relatively generic task with abundant training data. Ben Hylak's observation about models being "optimized for terminal" is cited as evidence of task-specific training shaping behavior.
