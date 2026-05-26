---
title: "Anthropic Multi-Agent Research System (Claude Research)"
created: 2026-05-20
updated: 2026-05-20
type: concept
tags:
  - multi-agent
  - ai-agents
  - anthropic
  - agent-architecture
  - agent-orchestration
  - subagents
  - prompting
  - deep-research
aliases:
  - claude-research
  - anthropic-research-agent
  - orchestrator-worker-pattern
sources:
  - raw/articles/2025-06-13_anthropic_multi-agent-research-system.md
  - raw/articles/2025-06-14_simonwillison_multi-agent-research-system.md
  - https://www.anthropic.com/engineering/multi-agent-research-system
  - https://simonwillison.net/2025/Jun/14/multi-agent-research-system/
---

# Anthropic Multi-Agent Research System (Claude Research)

A detailed engineering report published by Anthropic in June 2025 on the design and operation of the **multi-agent system** powering Claude's Research functionality. Adopts the Orchestrator-Worker pattern, with a lead agent spawning multiple sub-agents in parallel to conduct research.

> "A multi-agent system consists of multiple agents (LLMs autonomously using tools in a loop) working together."

## Architecture

### Orchestrator-Worker Pattern

```
User Query
    │
    ▼
┌─────────────────────────────────┐
│  LeadResearcher (Claude Opus 4) │  ← Strategy development, Memory persistence
│  - Query analysis                │
│  - Plan creation & Memory save  │
│  - Sub-agent generation & merge │
└──────────┬──────────────────────┘
           │ spawn parallel subagents
    ┌──────┼──────┬──────┐
    ▼      ▼      ▼      ▼
┌──────┐┌──────┐┌──────┐┌──────┐
│Sub-  ││Sub-  ││Sub-  ││Sub-  │  ← Claude Sonnet 4
│agent ││agent ││agent ││agent │
│ 1    ││ 2    ││ 3    ││ N    │     Independent context windows
│      ││      ││      ││      │     Tool loop
│ search││search││search││search│    Interleaved thinking
└──┬───┘└──┬───┘└──┬───┘└──┬───┘
   │       │       │       │
   └───────┴───┬───┴───────┘
               ▼  Integration
    ┌─────────────────────┐
    │  CitationAgent       │  ← Pinpoints exact citation locations
    │  (Final processing)  │
    └─────────────────────┘
               │
               ▼
         Final Answer (User)
```

### Key Components

| Component | Role | Model |
|-----------|------|-------|
| **LeadResearcher** | Query analysis, strategy planning, sub-agent generation and integration | Claude Opus 4 |
| **Subagents** | Parallel search, result evaluation, reporting to lead | Claude Sonnet 4 |
| **CitationAgent** | Document processing, citation location identification | — |
| **Memory** | Context retention when exceeding 200K token limit | — |

### Differences from RAG

> "Traditional approaches using Retrieval Augmented Generation (RAG) use static retrieval … In contrast, our architecture uses a **multi-step search** that dynamically finds relevant information, adapts to new findings, and analyzes results to formulate high-quality answers."

Compared to RAG's static retrieval, multi-agent systems achieve **dynamic, iterative, adaptive** exploration.

## Performance

### Evaluation Results

- **Outperforms single Opus 4 by 90.2%** (internal research eval)
- Example: "Identify all board members of S&P 500 IT companies" → single agent fails, multi-agent succeeds
- **Token usage explains 80% of performance variance** (BrowseComp evaluation)
- Tool call count and model selection account for the remaining 20%

### Token Economics

| Mode | Token consumption (vs chat) | Suitable tasks |
|------|----------------------------|----------------|
| Chat | 1× | Daily conversation |
| Single Agent | ~4× | Simple tool operations |
| Multi-Agent | ~15× | High-value, parallel research |

**Economic conditions**: Heavy parallelism possible, information exceeding single context window, high-value tasks requiring coordination with many complex tools.

> "Multi-agent systems work mainly because they help spend enough tokens to solve the problem."

## Two Axes of Parallelization

1. **Lead agent spawns 3-5 sub-agents in parallel** (not sequentially)
2. **Sub-agents call 3+ tools simultaneously in parallel**

> "These changes cut research time by up to **90%** for complex queries, allowing Research to do more work in minutes instead of hours."

### Parallel Tool Calling Prompt Example

```
For maximum efficiency, whenever you need to perform multiple independent operations,
invoke all relevant tools simultaneously rather than sequentially. Call tools in parallel
to run subagents at the same time. You MUST use parallel tool calls for creating multiple
subagents (typically running 3 subagents at the same time) at the start of the research,
unless it is a straightforward query.
```

## 8 Prompt Engineering Principles

> "Prompt engineering was the primary lever" — not model upgrades nor tool improvements.

### 1. Think Like Your Agents

Build simulations using accurate tools and prompts, observe agent behavior step by step. Discover failure modes like continuing when sufficient information exists, redundant queries, and incorrect tool selection.

### 2. Teach the Orchestrator How to Delegate

Explicitly specify each sub-agent's **purpose, output format, tool/source guidance, and task boundaries**.
Vague instructions ("investigate semiconductor shortages") → duplication and gaps. One agent researches the 2021 crisis, two duplicate research on the 2025 supply chain.

### 3. Scale Effort to Query Complexity

| Query Type | Agents | Tool calls |
|------------|--------|------------|
| Simple fact check | 1 agent | 3-10 calls |
| Direct comparison | 2-4 subagents | 10-15 calls each |
| Complex research | 10+ subagents | Divided responsibility scopes |

### 4. Tool Design and Selection Are Critical

The Agent-Tool interface is as important as HCI (Human-Computer Interaction).
Explicit heuristics: Pre-verify all tools → select tools matching intent → prioritize specialized tools.
> "Bad tool descriptions can send agents down completely wrong paths."

### 5. Let Agents Improve Themselves

Introduce a **Tool-Testing Agent (meta-agent)**:
- Repeatedly uses defective MCP tools
- Identifies bugs and nuances
- Rewrites tool descriptions

→ **Task completion time reduced by 40%**.

### 6. Start Wide, Then Narrow Down

Mimic human research: start with short, broad queries and gradually focus based on findings.

### 7. Guide the Thinking Process

Use extended thinking as a controllable scratchpad for planning, tool selection, and role definition.
Sub-agents use **interleaved thinking** after tool results for quality assessment and next-step decisions.

### 8. Test Early, Test Often

- Start small-scale eval with a few examples immediately, don't wait for large test suites
- **LLM-as-a-judge** is effective, but **human evaluation is essential**
- Bias discovered by human testers: agents prioritized SEO-optimized content farms over academic PDFs and personal blogs
- → Fixed by adding source quality heuristics to prompts

## Lessons from Prototype to Production

> "The gap between prototype and production is often wider than anticipated."

### The Danger of Compound Errors

> "The compound nature of errors in agentic systems means that minor issues for traditional software can derail agents entirely."

What would be minor issues in traditional software can be fatal for agents. The compounding effect of errors amplifies small mistakes.

### Early Failure Examples

- Spawning 50 sub-agents for a simple query
- Endlessly searching across the web for nonexistent sources
- Interfering with each other through excessive update notifications

### Keys to Success

1. **Prompt engineering is the most important lever** (more than model upgrades)
2. **Human evaluation complements LLM-as-judge** (essential for bias detection)
3. **Self-improving agents** (Tool-Testing Agent was an unexpected success)
4. **Memory mechanism** (persisting plans as context loss protection)

## Optimal Use Cases

Areas where multi-agent is suitable:
- Tasks allowing **heavy parallelization**
- **Information volume exceeding** a single context window
- Coordination with **many complex tools**
- **High-value, open-ended** research

Unsuitable areas:
- Tasks with many inter-agent dependencies
- Tasks requiring real-time delegation
- Most coding tasks (currently)

## Related Pages

- [[concepts/agent-patterns]] — General agent patterns (Inline Tool, Fan-Out, Agent Pool, Teams)
- [[concepts/agentic-search]] — Comprehensive guide to agentic search
- [[concepts/rlm-recursive-language-models]] — RLM: Overcoming context length constraints through recursive decomposition (structurally similar pattern)
- [[comparisons/agent-orchestration-frameworks]] — Comparison of orchestration frameworks (LangGraph, CrewAI, etc.)
- [[concepts/ai-operating-model]] — Multi-agent as an AI operating model
- [[concepts/coding-agents]] — Coding agent design patterns

## Structural Similarity Pattern: Multi-Agent × RLM — Divide and Conquer of Context Constraints

The multi-agent research system and [[concepts/rlm-recursive-language-models|RLM (Recursive Language Models)]] **solve the same fundamental problem on different axes**.

| Dimension | Multi-Agent Research (Anthropic) | RLM (Zhang, Kraska, Khattab) |
|-----------|--------------------------------|------------------------------|
| **Division target** | Research **tasks** | Input **context** |
| **Division direction** | **Horizontal** (parallel Fan-Out) | **Depth** (recursive tree) |
| **Pattern** | MapReduce: parallel sub-agents → aggregation | Recursive: model calls itself on chunks |
| **Constraint breakthrough** | Scale information via multiple context windows | Surpass context length by 2 orders via recursive processing |
| **Scaling** | 15× token consumption for 90.2% performance gain | 10M+ token processing without accuracy degradation |
| **Aggregation method** | Lead agent compresses and integrates sub-results | Synthesize recursive call results |
| **Essence** | **Horizontal scaling** via agent parallelization | **Depth scaling** via model self-invocation |

> Both overcome the constraint of "what cannot be processed in a single context window" through **divide and conquer**. Multi-Agent parallelizes task space, RLM recursivizes input space. Different axes, but the same architectural insight.

### Agent-Context Duality — Homology with IR Query-Document Duality

Abstracting one step further reveals a structure homologous to **Information Retrieval (IR) query-document duality** in the agent-context relationship:

| IR Duality | Agent-Context Duality |
|------------|----------------------|
| Query = short information request | Sub-agent task = short research instruction |
| Document = complete answer to query | Sub-agent result = complete answer to task |
| Both projected into the **same semantic space** | Both expressed in the **same token space** |
| Query ≒ short document, Document ≒ long query | Objective ≒ condensed result, Result ≒ expanded objective |
| Pseudo-relevance feedback dissolves boundaries | Interleaved thinking enables evaluation and re-search (relevance feedback) |
| Ranking function determines query-document match | Lead agent determines and integrates task-result match |

The core of this duality: "Task instructions" and "exploration results" are essentially **different granularities of the same semantic object**, both projected into the LLM's token space. Sub-agents expand tasks (queries) into contexts (documents), while the lead agent compresses documents to update queries — the same feedback loop as IR's pseudo-relevance feedback.

> Anthropic themselves stated "search is compression" — which is precisely a restatement of this duality. Search results in document space are compressed into new judgments in query space — the same structure IR uses (query → document → relevance feedback → query expansion) appears in agent systems as objective → exploration → interleaved thinking → objective update.

## Simon Willison's Assessment

Simon Willison was initially skeptical of multi-agent LLM systems but became convinced after reading Anthropic's detailed report:

- **"Multi-agent systems work mainly because they help spend enough tokens to solve the problem"** — token usage explains 80% of performance
- **Compression through parallelization** is the core insight
- **Prompt engineering is paramount** (not model size nor tool quality)
- **Tool-Testing Agent** (40% improvement) is a novel meta-learning pattern worth researching
- **Human evaluation detects biases missed by automated eval**
- **Cost is a trade-off**: 15× token consumption vs chat is only justified for high-value tasks
