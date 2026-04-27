---
title: "Agent Harness"
created: 2026-04-27
updated: 2026-04-27
tags: [agent-infrastructure, harness, agent-orchestration]
aliases: [agent-harness, agent-runtime]
related: [[concepts/claude-managed-agents]], [[concepts/harness-engineering]], [[concepts/tool-orchestration]], [[entities/anthropic]]
sources: [
  "https://x.com/RLanceMartin/status/2041927992986009773",
  "https://foundationcapital.com/ideas/context-graphs-ais-trillion-dollar-opportunity"
]
---

# Agent Harness

## Summary

An agent harness is the infrastructure layer that sits between an LLM API and the agent's execution environment. It manages tool routing, context management, session lifecycle, and error recovery. As LLMs grow more capable, harnesses face the challenge of keeping pace with model capabilities — assumptions about what a model "can't do" become stale quickly, bottlenecking performance.

## Key Concepts

### The Stale Assumption Problem
Agent harnesses encode assumptions about model capabilities. As models like Claude get more capable (exceeding 10+ human-hours of continuous work on METR benchmark), these assumptions become stale. A harness that assumes "Claude can't do X" will underperform when Claude actually can do X.

### Decoupling Architecture
The modern approach decouples three components:
- **Brain** — The LLM and its reasoning/harness logic
- **Hands** — Sandboxes and tools that perform actions
- **Session** — The log of session events and state

Each becomes an independent interface. This allows each component to fail, evolve, or be replaced without cascading failures.

### Managed vs. Custom Harnesses
Traditional approach: build your own harness with tool routing, context windows, and error handling. Modern approach: use managed infrastructure (e.g., Claude Managed Agents) that provides the harness and infrastructure, letting developers focus on agent configuration and multi-agent orchestration patterns.

## Key Ideas

- Harnesses encode capability assumptions that grow stale as models improve
- Decoupling brain/hands/session enables independent evolution
- Managed harnesses reduce infrastructure burden, enabling exploration at the agent level
- Long horizon tasks (days/weeks/months) require resilient infrastructure beyond simple tool routing
- The harness is not the agent — it's the runtime that enables the agent to execute safely

## Terminology

- **Agent Harness** — The orchestration layer managing tool calls, context, and session state
- **Managed Infrastructure** — Pre-built harness + infrastructure provided by the model vendor
- **Session** — A stateful run of an agent with specific configuration and environment
- **Tool Orchestration** — Routing model tool calls to handler functions
- **Context Management** — Managing the conversation history and context window

## Examples

### Claude Managed Agents
Anthropic's pre-built, configurable agent harness running in managed infrastructure. Defines agents as templates (tools, skills, files/repos). The harness and infrastructure are provided — developers focus on configuration and multi-agent patterns. Three central concepts: Agent (versioned config), Environment (sandbox template), Session (stateful run).

### Traditional Custom Harnesses
Build-your-own approach using Claude API messages API or OpenAI functions. Requires custom tool routing, context window management, error recovery, and long-running task infrastructure. More flexible but higher operational burden.

## Related Concepts
- [[concepts/claude-managed-agents]] — Anthropic's managed agent infrastructure
- [[concepts/harness-engineering]] — Principles of building agent harnesses
- [[concepts/tool-orchestration]] — How agents route tool calls to handlers
- [[entities/anthropic]] — Provider of Claude Managed Agents
