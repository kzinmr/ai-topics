---
title: "How We Built Our Multi-Agent Research System"
source: Anthropic Engineering Blog
url: https://www.anthropic.com/engineering/multi-agent-research-system
date_published: 2025-06-13
type: raw_article
tags:
  - multi-agent
  - ai-agents
  - anthropic
  - agent-architecture
  - prompt-engineering
  - claude-research
---

# How We Built Our Multi-Agent Research System — Anthropic

*Summary of Anthropic's engineering blog post on Claude's Research feature, a multi-agent system for complex, open-ended web research.*

---

## Key Excerpts

> "Our Research system uses a multi-agent architecture with an orchestrator-worker pattern, where a lead agent coordinates the process while delegating to specialized subagents that operate in parallel."

> "Even generally-intelligent agents face limits when operating as individuals; groups of agents can accomplish far more."

> "Multi-agent research systems excel especially for breadth-first queries that involve pursuing multiple independent directions simultaneously."

> "We found that a multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval."

> "Token usage by itself explains 80% of the variance … upgrading to Claude Sonnet 4 is a larger performance gain than doubling the token budget on Claude Sonnet 3.7."

> "Without effective mitigations, minor system failures can be catastrophic for agents."

> "The compound nature of errors in agentic systems means that minor issues for traditional software can derail agents entirely."

> "The gap between prototype and production is often wider than anticipated."

---

## 1. Benefits of a Multi-Agent System

- **Open-ended problems need dynamic, path-dependent exploration** – research cannot be hardcoded; it evolves based on discoveries.
- **Agents are ideal** because they can autonomously decide next steps over many turns.
- **Parallelism & compression**: Subagents search different facets simultaneously, each within its own context window, then compress the most important tokens for the lead agent.
- **Separation of concerns** – each subagent has distinct tools, prompts, and trajectory, reducing path dependency.
- **Scaling analogy**: Human collective intelligence dramatically amplifies capability; multi-agent systems do the same for AI.
- **Internal evaluation**: Multi-agent (Opus 4 + Sonnet 4 subagents) beat single Opus 4 by **90.2%** on breadth-first research tasks (e.g., identifying all board members of S&P 500 IT companies).
- **Performance drivers**: **Token usage explains 80%** of variance in BrowseComp; the other factors are number of tool calls and model choice.
- **Cost & applicability**:
  - Agents burn ~4× more tokens than chat; multi-agent ~15× more.
  - Best for high-value tasks with heavy parallelisation, information exceeding single context windows, and many complex tools.
  - Less suited for domains with shared context requirements or many inter‑agent dependencies (e.g., most coding tasks today).

---

## 2. Architecture Overview

**Orchestrator-worker pattern**:

- **User query** → **Lead Agent** (LeadResearcher) analyses the query, plans an approach, saves the plan to **Memory** to persist it across context truncation (200k token limit).
- Lead agent spawns **specialized Subagents** in parallel.
- Each subagent:
  - Performs web searches (or uses other tools),
  - Evaluates results with **interleaved thinking**,
  - Returns findings to the lead agent.
- Lead agent synthesises results, decides if more research is needed (may spawn more subagents or refine strategy).
- When done, a **CitationAgent** processes documents and the report to locate exact citation positions before final output to the user.

**vs. RAG**:

> "Traditional approaches using Retrieval Augmented Generation (RAG) use static retrieval … In contrast, our architecture uses a multi‑step search that dynamically finds relevant information, adapts to new findings, and analyzes results to formulate high‑quality answers."

---

## 3. Prompt Engineering & Evaluations for Research Agents

Coordination complexity grows rapidly. Prompt engineering was the primary lever. Eight principles emerged:

1. **Think like your agents**
   – Build simulations with exact tools and prompts, watch agent behavior step‑by‑step to spot failure modes (e.g., continuing after enough results, overly verbose queries, wrong tool choice).

2. **Teach the orchestrator how to delegate**
   – Subagent tasks need clear objectives, output format, tool/source guidance, and boundaries to avoid duplication or gaps.
   – Vague instructions like "research the semiconductor shortage" caused overlap; one agent explored 2021 crisis while two others duplicated 2025 supply chains.

3. **Scale effort to query complexity**
   – Embed explicit scaling rules in prompts:
     - Simple fact-finding → 1 agent, 3–10 tool calls
     - Direct comparisons → 2–4 subagents, 10–15 calls each
     - Complex research → 10+ subagents with divided responsibilities
   – Prevents overinvestment in simple queries.

4. **Tool design and selection are critical**
   – Agent-tool interface is as critical as human-computer interfaces.
   – Provide explicit heuristics: examine all tools first, match tool usage to intent, prefer specialized tools.
   – "Bad tool descriptions can send agents down completely wrong paths."

5. **Let agents improve themselves**
   – Claude 4 models can diagnose failure modes and suggest prompt fixes.
   – Created a **tool-testing agent** (meta-agent) that uses a flawed MCP tool repeatedly, finds bugs and nuances, then rewrites the tool description.
   – **Result: 40% decrease in task completion time** for future agents using the improved description.

6. **Start wide, then narrow down**
   – Mirror human research: begin with short, broad queries, then progressively narrow focus based on findings.

7. **Guide the thinking process**
   – Extended thinking serves as a controllable scratchpad for planning, tool selection, role definition.
   – Subagents interleave thinking after tool results to evaluate quality and decide next steps.

8. **Test early, test often**
   – Start with small-scale evals immediately rather than waiting for large test suites.
   – LLM-as-a-judge worked well but human evaluation was essential.
   – Human testers caught a critical bias: agents preferred SEO-optimized content farms over authoritative sources (academic PDFs, personal blogs). Fixed with source quality heuristics in prompts.

---

## 4. Parallelism for Speed

Two kinds of parallelization:

1. **Lead agent spawns 3–5 subagents in parallel** (instead of serially)
2. **Subagents use 3+ tools in parallel** (simultaneous tool calls)

> "These changes cut research time by up to 90% for complex queries, allowing Research to do more work in minutes instead of hours while covering more information than other systems."

### Example Prompt for Parallel Tool Calls

```
For maximum efficiency, whenever you need to perform multiple independent operations,
invoke all relevant tools simultaneously rather than sequentially. Call tools in parallel
to run subagents at the same time. You MUST use parallel tool calls for creating multiple
subagents (typically running 3 subagents at the same time) at the start of the research,
unless it is a straightforward query. For all other queries, do any necessary quick initial
planning or investigation yourself, then run multiple subagents in parallel. Leave any
extensive tool calls to the subagents; instead, focus on running subagents in parallel
efficiently.
```

---

## 5. From Prototype to Production

> "The gap between prototype and production is often wider than anticipated."

Key lessons:

- **Compound errors**: Minor failures that are non-critical in traditional software can derail agents entirely. The compound nature of errors in agentic systems amplifies small mistakes.
- **Prompt engineering was the primary lever** — not model upgrades, not tool improvements.
- **Human evaluation was irreplaceable** — LLM-as-judge missed biases like SEO content farm preference.
- **Self-improving agents** — the tool-testing meta-agent pattern was an unexpected success.
