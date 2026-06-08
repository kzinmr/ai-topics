---
title: Microsoft Agent Framework
created: 2026-05-21
updated: 2026-05-21
type: entity
tags:
  - microsoft
  - ai-agents
  - multi-agent
  - framework
  - mcp
  - orchestration
  - open-source
  - company
  - developer-tooling
  - dotnet
sources: [raw/articles/2026-04-08_microsoft-agent-framework-v1.md]
---

# Microsoft Agent Framework

Microsoft Agent Framework is a production-ready, open-source SDK for **.NET and Python** that unifies Semantic Kernel foundations with AutoGen orchestrations into a single framework for building enterprise-grade multi-agent AI systems. Version 1.0 was released on April 8, 2026.

## Stable Features (v1.0)

### Single Agent & Service Connectors
Production-ready agent abstraction with first-party connectors for: **Microsoft Foundry, Azure OpenAI, OpenAI, Anthropic Claude, Amazon Bedrock, Google Gemini, Ollama**.

### Middleware Hooks
Intercept, transform, and extend agent behavior. Use cases: content safety filters, logging, compliance policies, custom logic.

### Agent Memory & Context Providers
Pluggable memory architecture supporting conversational history, key-value state, and vector retrieval. Backends: Foundry Agent Service memory, Mem0, Redis, Neo4j, or custom stores.

### Agent Workflows
Graph-based workflow engine for composing agents and functions. Supports branching, parallel fan-out, checkpointing, and hydration for long-running processes.

### Multi-Agent Orchestration
Patterns evolved from Microsoft Research and AutoGen: **sequential, concurrent, handoff, group chat, Magentic-One**. All support streaming, checkpointing, human-in-the-loop approvals, pause/resume.

### Declarative Agents & Workflows (YAML)
Define instructions, tools, memory, and topology in version-controlled YAML. Load and run with a single API call.

### A2A and MCP Protocols
- **MCP** (Model Context Protocol): Dynamic tool discovery and invocation from MCP servers
- **A2A** (Agent-to-Agent, coming): Cross-runtime agent collaboration via structured messaging

### Migration Assistants
Tools for teams migrating from Semantic Kernel or AutoGen — analyze existing code and generate migration plans.

## Preview Features

- **DevUI**: Browser-based local debugger for real-time visualization of agent execution, message flows, and tool calls
- **Foundry Hosted Agent Integration**: Run agents as managed services on Microsoft Foundry or Azure Durable Functions
- **Foundry Tools, Memory, Observability, Evaluations**: Deep integration with Microsoft's AI platform

## Quick Start

```python
# pip install agent-framework
from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient

agent = Agent(
    client=FoundryChatClient(model="gpt-5.3"),
    name="HelloAgent",
    instructions="You are a friendly assistant."
)
print(await agent.run("Write a haiku about shipping 1.0."))
```

## Multi-Agent Example

Sequential orchestration with a copywriter and reviewer pipeline — `SequentialBuilder` composes agents into workflows with streaming, checkpointing, and human-in-the-loop support.

## Significance

Microsoft Agent Framework v1.0 represents the convergence of two major Microsoft AI SDK efforts (Semantic Kernel + AutoGen) into a unified framework. Its enterprise focus — with Foundry integration, A2A/MCP protocol support, and migration tooling — positions it as a key infrastructure layer for production AI agent deployments.

## Related Pages

- [[entities/microsoft]] — Microsoft's AI strategy and ecosystem
- [[concepts/multi-agent]] — Multi-agent AI systems
- [[concepts/mcp]] — Model Context Protocol
- [[entities/autogen]] — Microsoft AutoGen framework
- [[entities/semantic-kernel]] — Microsoft Semantic Kernel
- [[concepts/agent-framework]] — AI agent frameworks landscape
