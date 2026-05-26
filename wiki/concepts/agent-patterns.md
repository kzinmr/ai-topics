---
title: "Agent Patterns"
type: concept
created: 2026-04-30
updated: 2026-05-20
tags:
  - concept
  - ai-agents
  - agentic-engineering
  - multi-agent
  - agent-architecture
  - anthropic
status: complete
description: "Patterns and practices for building and deploying AI agents — harnesses, workflows, and multi-agent orchestration."
---
# Agent Patterns

Architecture patterns, harness design, and workflows for AI Agents.

## Overview

AI Agent patterns span a wide spectrum: from single-agent patterns to sub-agents, meta-agents, long-running agents, and multi-agent coordination.

## Subagent Patterns (Philipp Schmid, May 2026)

Philipp Schmid's four subagent patterns are classified by the level at which the main agent controls sub-agents:

### 1. Inline Tool — Sub-agent as Function Call
The simplest pattern. The main agent calls a `call_agent` tool, spawns a sub-agent, and returns the result as a tool response. Two variants: synchronous (blocking) or asynchronous (returns agent_id).
- **Use cases**: Research references, code review, test generation
- **Limitation**: No intermediate follow-ups

### 2. Fan-Out — Spawn and Wait
The main agent dispatches multiple tasks and controls collection timing. Two tools: `spawn_agent` (immediate ID return) and `wait_agent` (blocking).
- **Strength**: Main agent can work while sub-agents execute in parallel
- **Limitation**: Timing design is critical (immediate `wait_agent` nullifies parallelism)

### 3. Agent Pool — Persistent Messaging
Sub-agents are long-lived, stateful, interactive. The main agent acts as coordinator with a rich toolset: `spawn_agent`, `send_message`, `wait_agent`, `list_agents`, `kill_agent`.
- **Strength**: Sub-agents maintain conversation history, can receive feedback and iterate
- **Use cases**: Multi-step workflows like Researcher finding data → Writer using data to compose articles

### 4. Teams — Direct Agent-to-Agent Communication
The main agent is a high-level supervisor. After setting up the team, sub-agents communicate directly via `send_message`.
- **Strength**: Keeps main agent context clean
- **Limitation**: Risk of agent loops (A waiting for B, B waiting for A). All roles require frontier models

| Pattern | Tools | Main Role | Lifespan |
|---------|--------|----------|----------|
| Inline Tool | `call_agent` | Caller | Single task |
| Fan-Out | `spawn`, `wait` | Dispatcher | Single task |
| Agent Pool | `spawn`, `send`, `wait`, `list`, `kill` | Coordinator | Multi-turn |
| Teams | All + cross-agent `send` | Supervisor | Persistent |

### 5. Orchestrator-Worker — Research via Parallel Sub-agents (Anthropic, 2025)

A production pattern adopted by Anthropic's Claude Research (see [[concepts/anthropic-multi-agent-research]]).

- **LeadResearcher (Opus 4)**: Query analysis → strategy formulation → save to Memory → spawn sub-agents in parallel
- **Subagents (Sonnet 4)**: Independent context windows, parallel search, interleaved thinking for result evaluation, compressed results returned to lead
- **CitationAgent**: Locates citation positions in the final report

**Key findings**:
- **90.2% performance improvement** over single agent (internal evaluation)
- Token usage explains **80%** of performance variance
- **Memory mechanism** prevents plan loss when exceeding 200k token limit
- Tool-Testing Agent (meta-agent) improvements to tool descriptions yielded **40% time reduction**
- Agent consumes 4x vs chat's 15x token consumption (justified only for high-value tasks)

**Limitation**: Unsuitable for tasks with high inter-agent dependency (e.g., coding).

| Pattern | Tools | Main Role | Lifespan |
|---------|--------|----------|----------|
| Orchestrator-Worker | `spawn_subagent`, `Memory`, parallel tools | Orchestrator | Multi-turn |

### Implementation Guidelines
1. **Start with Inline Tool** — Most multi-agent needs are served by single-task calls
2. **Model selection**: Patterns 1-2 work with smaller models. Pattern 3 requires models capable of multi-agent state tracking. Pattern 4 requires frontier models for all roles (GPT-4o, Claude 3.5 Sonnet)
3. **Result collection**: The framework provides tools, but the model controls orchestration. Developers must ensure the model calls `wait_agent`/`kill_agent` appropriately
4. **Future-proofing**: Today's 4-agent coordinated task may be solvable by a single high-performance model tomorrow. Design flexibly

Source: [Philipp Schmid — How Agents Manage Other Agents: Four Subagent Patterns in 2026](https://www.philschmid.de/subagent-patterns-2026)

## Raw Articles

- [2025286163641118915_The-File-System-Is-the-New-Database-Personal-OS-for-AI-Agents](2025286163641118915_The-File-System-Is-the-New-Database-Personal-OS-for-AI-Agents.md)
- [2026-04-25-agent-product-design-chinese](2026-04-25-agent-product-design-chinese.md)
- [2026-04-25-agentcraft-rts-agent-orchestration](2026-04-25-agentcraft-rts-agent-orchestration.md)
- [2026-04-27_2045080054917476451_Hermes-Agent-Polymarket-Self-Learning-Weather-Trading-Bot](2026-04-27_2045080054917476451_Hermes-Agent-Polymarket-Self-Learning-Weather-Trading-Bot.md)
- [2026-04-27_2045935785661349956_Hermes-Agent-What-People-Are-Actually-Using-It-For](2026-04-27_2045935785661349956_Hermes-Agent-What-People-Are-Actually-Using-It-For.md)
- [2026-04-27_2046277232537256002_The-Runtime-Behind-Production-Deep-Agents](2026-04-27_2046277232537256002_The-Runtime-Behind-Production-Deep-Agents.md)
- [2026-04-28_x-article-15-hermes-agent-features](2026-04-28_x-article-15-hermes-agent-features.md)
- [2026-04-28_x-article-connecting-agents-to-decisions-palantir](2026-04-28_x-article-connecting-agents-to-decisions-palantir.md)
- [2026-2013-effective-harnesses-for-long-running-agents](2026-2013-effective-harnesses-for-long-running-agents.md)
- [2026-2026-devin-use-cases---agent-workflows-cookbook](2026-2026-devin-use-cases---agent-workflows-cookbook.md)
- [2026-2035-agent-skills-overview---agentskills.io](2026-2035-agent-skills-overview---agentskills.io.md)
- [2026-designing-for-agents](2026-designing-for-agents.md)
- [2041927992986009773_Launching-Claude-Managed-Agents](2041927992986009773_Launching-Claude-Managed-Agents.md)
- [2042539396638085339_What-Hermes-Agent-Can-Do-for-You](2042539396638085339_What-Hermes-Agent-Can-Do-for-You.md)
- [2047720067107033525_Memory-in-Claude-Managed-Agents](2047720067107033525_Memory-in-Claude-Managed-Agents.md)
- [agent-sandbox-architecture-2026-02-25](agent-sandbox-architecture-2026-02-25.md)
- [crawl-2026-04-23-building-effective-ai-agents](crawl-2026-04-23-building-effective-ai-agents.md)
- [hyperbo.la--w-agents-agents-agents--79613a0d](hyperbo.la--w-agents-agents-agents--79613a0d.md)
- [jason-liu-sandboxes-agents-sdk-2026-04](jason-liu-sandboxes-agents-sdk-2026-04.md)
- [lucumr.pocoo.org--2026-2-9-a-language-for-agents--77a0e78a](lucumr.pocoo.org--2026-2-9-a-language-for-agents--77a0e78a.md)
- [martinalderson.com--posts-ai-agents-are-starting-to-eat-saas--37d8652e](martinalderson.com--posts-ai-agents-are-starting-to-eat-saas--37d8652e.md)
- [martinalderson.com--posts-excel-agents-could-unlock-1t-in-economic-value--2fb910d0](martinalderson.com--posts-excel-agents-could-unlock-1t-in-economic-value--2fb910d0.md)
- [martinalderson.com--posts-travel-agents-developers--03e9ba7f](martinalderson.com--posts-travel-agents-developers--03e9ba7f.md)
- [martinalderson.com--posts-using-agents-and-wine-to-move-off-windows--85a78b28](martinalderson.com--posts-using-agents-and-wine-to-move-off-windows--85a78b28.md)
- [martinalderson.com--posts-why-im-building-my-own-clis-for-agents--08080178](martinalderson.com--posts-why-im-building-my-own-clis-for-agents--08080178.md)
- [milksandmatcha-0xsero-single-agent-ceiling-2026](milksandmatcha-0xsero-single-agent-ceiling-2026.md)
- [nesbitt.io--2026-04-08-package-security-problems-for-ai-agents-html--cec0229c](nesbitt.io--2026-04-08-package-security-problems-for-ai-agents-html--cec0229c.md)
- [nesbitt.io--2026-04-09-package-security-defenses-for-ai-agents-html--aa01c0e5](nesbitt.io--2026-04-09-package-security-defenses-for-ai-agents-html--aa01c0e5.md)
- [open.substack.com--pub-importai-p-import-ai-453-breaking-ai-agents--80eac51f](open.substack.com--pub-importai-p-import-ai-453-breaking-ai-agents--80eac51f.md)
- [open.substack.com--pub-nlpnews-p-ai-agents-weekly-claude-managed-agents--883aac03](open.substack.com--pub-nlpnews-p-ai-agents-weekly-claude-managed-agents--883aac03.md)
- [seangoedecke.com--programming-with-ai-agents-as-theory-building--b672de74](seangoedecke.com--programming-with-ai-agents-as-theory-building--b672de74.md)
- [two-ways-to-sandbox-agents-2026-02-25](two-ways-to-sandbox-agents-2026-02-25.md)
- [workos-fga-authorization-ai-agents-2026-04-13](workos-fga-authorization-ai-agents-2026-04-13.md)
