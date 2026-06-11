---
title: "System Architecture — System Design Under Harness Engineering"
type: concept
aliases:
  - system-architecture
  - agent-system-design
  - agent-architecture-patterns
created: 2026-04-12
updated: 2026-05-26
tags:
  - concept
  - methodology
  - harness-engineering
  - architecture
status: active
parent: harness-engineering
sources: []
---

# System Architecture — System Design Under Harness Engineering

System design and architecture patterns for **building** AI agents. Positioned as a **sub-section of Harness Engineering**.

The Anthropic Engineering blog and OpenAI Cookbook are the primary sources. Covers technical aspects such as agent internal structure, tool design, evaluation, and context management.

## Positioning within Harness Engineering

| Layer | Concept | Focus |
|---------|------|------|
| **Top Layer** | [[concepts/_index|Harness Engineering]] | Agent = Model + Harness (environment design philosophy) |
| **Cross-cutting** | [[concepts/context-engineering|Context Engineering]] | Context selection, compression, placement (finite resource management) |
| **Application (Human Side)** | [[concepts/agentic-engineering]] | Patterns for developers "using" agents |
| **Application (System Side)** | **System Architecture** (this page) | Patterns for "building" agents |

## Concept List

### 🏗️ Agent Design Patterns

| Page | Summary | Source |
|-------|------|------|
| [[concepts/building-effective-agents]] | Workflows vs agents, start with simplicity | Anthropic |
| [[concepts/multi-agent-research-system]] | Orchestrator-Worker, parallel sub-agents | Anthropic |
| [[concepts/harness-engineering/system-architecture/advanced-tool-use]] | Tool Search Tool / PTC / Tool Use Examples | Anthropic |
| [[concepts/writing-tools-for-agents]] | 5 principles of tool design, evaluation-driven optimization. Comprehensive "Design for Agent" paradigm. | Anthropic |
| [[concepts/harness-engineering/system-architecture/code-execution-with-mcp]] | Expose MCP as a code API (98.7% token reduction) | Anthropic |

### 🔄 Agent Execution Infrastructure (OpenAI Responses API)

| Page | Summary | Source |
|-------|------|------|
| [[concepts/agent-loop-orchestration]] | Autonomous loop: model proposes → shell executes → feedback | OpenAI |
| [[concepts/harness-engineering/system-architecture/context-compaction]] | Context compaction mechanism for long-running agents | OpenAI |
| [[concepts/harness-engineering/system-architecture/container-context]] | Persistent agent workspace via host containers | OpenAI |
| [[concepts/agent-skills]] | Reusable workflow patterns via SKILL.md bundles | OpenAI |

### 🛡️ Security & Control

| Page | Summary | Source |
|-------|------|------|
| [[concepts/harness-engineering/system-architecture/agent-security-patterns]] | Egress proxy, domain-scoped secret injection | OpenAI |
| [[concepts/evals-for-ai-agents]] | Fundamental principles of agent evaluation | Anthropic |
| [[concepts/infrastructure-noise]] | Impact of infrastructure settings on benchmark scores | Anthropic |

### 🧠 Context & Internal Structure

| Page | Summary | Source |
|-------|------|------|
| [[concepts/harness-design-long-running-apps]] | GAN-inspired Generator-Evaluator loop, context reset | Anthropic |
| [[concepts/harness-engineering/system-architecture/effective-harnesses-for-long-running-agents]] | Harness design for long-running agents | Anthropic |
| [[concepts/claude-code-best-practices]] | Claude Code practical best practices | Sankalp + Anthropic |

## Differences from Agentic Workflows

| Dimension | Agentic Workflows | System Architecture |
|------|-------------------|---------------------|
| Focus | Developer workflow | System architecture |
| Subject | "How humans use agents" | "How to build agents" |
| Representative | Willison's Red/Green TDD, Cognitive Debt | Anthropic's Building Effective Agents |
| Layer | Application/Use | Foundation/Design |

## Update History

| Date | Changes |
|------|---------|
| 2026-04-12 | Initial creation — reclassified Anthropic Engineering articles |
| 2026-04-19 | Harness umbrella reorganization: updated titles, removed duplicate entries, added positioning table |
