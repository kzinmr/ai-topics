---
title: "Agentic Workflow Patterns — 3 Levels, 4 Components, Architecture Taxonomy"
type: concept
created: 2026-04-22
updated: 2026-05-26
tags: [concept, ai-agents, orchestration, framework]
status: active
sources:
  - "Vellum AI — Agentic Workflows in 2026 (Dec 2025)"
  - "https://www.vellum.ai/blog/agentic-workflows-emerging-architectures-and-design-patterns"
aliases:
  - agentic-workflow-patterns
  - agent-workflow-levels
  - workflow-autonomy-scale
---

# Agentic Workflow Patterns

> "The most successful AI systems in 2026 are built around agentic workflow patterns that manage uncertainty, memory, tools, and feedback deliberately. These patterns aren't flashy. They are structured, observable, and resilient."

**Overview:** A formal taxonomy of agentic workflows. Three levels of autonomy, four core components, design patterns, and the 2026 AI agent stack.

## 3 Levels of Agentic Architectures

| Workflow Type | L1: Output Decisions | L2: Task Decisions | L3: Process Decisions |
|:---|:---:|:---:|:---:|
| **AI Workflow** | ✅ | ❌ | ❌ |
| **Router Workflow** | ✅ | ✅ Task/tool selection within predefined environment | ❌ |
| **Autonomous Agent** | ✅ | ✅ | ✅ New task/tool creation, code writing, feedback exploration |

> L2 is currently the most active innovation area. L3 (Devin, BabyAGI, MetaGPT) is promising but not yet production-ready.

## 4 Core Components

### 1. Planning
- CoT, ReAct, Self-Refine, RAISE, Reflexion, LATS, PlaG
- Document Agents + Meta-Agent Pattern

### 2. Execution
- Tools/Subagents: Web search, vector DB, scrapers, DB, ML models
- **Self-Tool Creation:** Autonomous agents write custom code (LATM - LLMs as Tool Makers)
- Guardrails and error handling

### 3. Refinement
- LLM evaluation: Use of detailed scoring rules
- **Memory Systems:**
  - Short-term: Context window + prompting
  - Long-term: Vector DB / Key-Value / Knowledge graph
- **Human-in-the-Loop:** Tracing required for each intermediate step

### 4. Interface
- Human-Agent Interface: Interactive UI, collaborative style
- Agent-Computer Interface (ACI): Optimize tool call syntax per model

## Design Patterns

### Single-Agent (For Focused Tasks)
- ReAct, Self-Refine, RAISE, Reflexion, LATS, PlaG

### Multi-Agent (For Parallel Workflows)
- Lead Agents, DyLAN (dynamic re-evaluation), Agentverse (structured phases), MetaGPT, BabyAGI

**Research Insight:** A single agent with strong prompting can achieve results comparable to multi-agent systems. Architecture should be chosen based on the use case.

## 2026 AI Agent Stack

| Function | Purpose |
|------|------|
| Tracing & Replay | Replay tasks with new instructions to improve |
| LLM Calls with Fallbacks | Ensure reliability during model failures |
| Human Approval in Production | Checkpoints for moderation and error handling |
| Tool Library & Execution | Use, create, and save tools |
| Executable Code | Arbitrary code execution for customization/flexibility |
| Metrics & Evaluation | Scalable performance tracking via built-in/custom metrics |
| User Feedback Integration | Real input as training data feedback |
| Version Control for Prompts/Models | Track changes safely without core code updates |

## Expert Insights

| Expert | Company | Key Insight |
|--------|---------|-------------|
| Eduardo Ordax | AWS | **Understand actions through tracing first**. RAG orchestrator, ML agents, RPA replacement |
| Armand Ruiz | IBM | Shift from Native RAG → **Agentic RAG**. Document Agents + Meta-Agent |
| Erik Wikander | Zupyak | **Embedded agents** are the biggest unlock. Copilot → AI co-worker |
| Yohei Nakajima | BabyAGI | **Graph-based agents** enable self-improvement |
| Vasilije Markovic | Cognee | Blend of graph + LLM + vector search for better long-term memory |

## Related Concepts

- [[concepts/agentic-engineering]] — Simon Willison's Agentic Engineering philosophy
- [[concepts/harness-engineering]] — Agent = Model + Harness
- [[concepts/harness-engineering/system-architecture/container-context]] — System construction patterns
- [[concepts/agent-loop-orchestration]] — Agent Loop Orchestration
- [[concepts/harness-engineering/system-architecture/building-effective-agents]] — Building Effective Agents (Anthropic)
- [[concepts/context-engineering|Context Engineering]] — Integrated framework for context optimization
