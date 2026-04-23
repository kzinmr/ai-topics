---
title: Building Effective AI Agents
category: other
status: active
---

# Building Effective AI Agents

**Source:** Anthropic Research  
**Date:** December 19, 2024  
**URL:** https://www.anthropic.com/research/building-effective-agents  
**Crawled:** 2026-04-23  

## 🔑 Core Thesis & Key Insight
> *"Consistently, the most successful implementations use simple, composable patterns rather than complex frameworks."*

- **Primary Goal:** Build the *right* system for your needs, not the most sophisticated one. Start with simple prompts, optimize with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short.
- **Key Tradeoff:** Agentic systems trade **latency and cost** for better task performance. Only increase complexity when demonstrably necessary.

## 📐 Definitions & Decision Framework
| System Type | Definition | Best Use Case |
|---|---|---|
| **Workflows** | LLMs & tools orchestrated through **predefined code paths** | Predictability, consistency, well-defined tasks |
| **Agents** | LLMs **dynamically direct** their own processes & tool usage | Flexibility, model-driven decision-making, open-ended problems |
- **When to skip agentic systems:** Optimizing a single LLM call with retrieval and in-context examples is usually sufficient.
- **When to use frameworks:** Claude Agent SDK, AWS Strands Agents SDK, Rivet, Vellum. *Caution:* They add abstraction layers that obscure prompts/responses, making debugging harder. **Recommendation:** Start with direct LLM APIs.

## 🧱 Building Blocks & Workflow Patterns
### Foundation: The Augmented LLM
- Base block enhanced with **retrieval, tools, and memory**. Modern models actively generate queries, select tools, and decide what to retain.
- **Implementation Tip:** Use the [Model Context Protocol (MCP)](https://www.anthropic.com/news/model-context-protocol) for seamless third-party tool integration.

### Workflow Patterns (Composable & Production-Tested)
1. **Prompt Chaining** — Sequential steps where each LLM call processes previous output. Add programmatic "gates" for checks.
2. **Routing** — Classifies input → directs to specialized follow-up tasks/prompts.
3. **Parallelization** — Simultaneous LLM calls with programmatic aggregation (sectioning or voting).
4. **Orchestrator-Workers** — Central LLM dynamically breaks down tasks, delegates to workers, synthesizes results.
5. **Evaluator-Optimizer** — One LLM generates response; another provides evaluation/feedback in a loop.

## 🤖 Autonomous Agents
- **Architecture:** LLMs plan/operate independently, use tools based on environmental feedback, pause for human checkpoints.
- **Risks:** Higher costs, compounding errors. Requires extensive sandbox testing & guardrails.
- **Production Examples:** Coding agents solving SWE-bench tasks; "Computer use" reference implementation (Claude operates a computer).

## 📊 Real-World Applications
- **Customer Support:** Natural fit for open-ended agents. Usage-based pricing models charging only for successful resolutions.
- **Coding Agents:** Highly effective due to verifiable outputs (automated tests), iterative feedback loops.
- **Research:** Literature review, codebase exploration, hypothesis generation.
- **Data Analysis:** ETL pipelines, report generation, anomaly detection.
