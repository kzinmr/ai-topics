---
title: "OpenClaw"
type: concept
tags:
  - openclaw
  - ai-agents
  - always-on
status: L3
created: 2026-04-27
updated: 2026-04-28
aliases: [Clawdbot, OpenClaw Agent Framework]
related: [[entities/openclaw]], [[entities/peter-steinberger]], [[entities/hermes-agent]], [[concepts/agent-harness-primitives]], [[concepts/agent-sandboxing]]
sources: [https://github.com/OpenClaw/OpenClaw, https://blog.owulveryck.info/2025/10/11/openclaw-demystify-the-ai-agent-that-runs-on-your-machine.html]
---

# OpenClaw

## Summary

OpenClaw (originally "Clawdbot") is an open-source, always-on AI assistant framework created by Peter Steinberger (former PSPDFKit CEO). It deploys autonomous agents that run continuously on a user's machine, self-evolve through interaction, and integrate deeply with the local environment via shell access, file system operations, and MCP server integration. OpenClaw represents the "always-on agent" paradigm — an AI that persists across sessions rather than being invoked statelessly per query.

## Key Ideas

- **Always-On Architecture**: Unlike stateless chat interfaces, OpenClaw agents run as persistent daemon processes that maintain session state, memory, and context across interactions
- **Self-Evolving Capabilities**: Agents can modify their own configuration, install new tools, and extend their capabilities based on user needs and observed patterns
- **Local-First Design**: All agent execution happens on the user's machine, providing low latency, privacy, and the ability to interact with local files, terminals, and applications
- **Tool-Augmented**: OpenClaw agents can execute shell commands, edit files, browse the web, use MCP servers, and interact with local applications — far beyond simple text generation
- **NVIDIA NemoClaw Integration**: NVIDIA's enterprise-hardened distribution of OpenClaw adds secure sandboxing, GPU acceleration, and enterprise governance features
- **Gateway + Orchestrator Architecture**: OpenClaw employs a two-component architecture — a Gateway (self-hosted bridge connecting to LLM APIs) and an Orchestrator (the agent runtime that manages tool execution, memory, and session lifecycle)

## Terminology

- **Gateway**: The self-hosted bridge component that manages LLM API connections, routing requests through configurable providers (OpenAI, Anthropic, local models, etc.)
- **Orchestrator**: The agent runtime that manages tool execution, memory persistence, session lifecycle, and the agent's core loop
- **NemoClaw**: NVIDIA's enterprise distribution of OpenClaw, adding sandboxed execution via Firecracker microVMs, GPU-accelerated inference, and audit logging
- **MCP Server Integration**: OpenClaw agents can connect to Model Context Protocol (MCP) servers, giving them access to standardized external tool ecosystems
- **Always-On Persistence**: The agent maintains a rolling window of conversation history, file system state, and learned behaviors across machine restarts

## Examples/Applications

- **Personal Assistant**: An OpenClaw agent running 24/7 on a developer's machine, managing email triage, calendar scheduling, and file organization
- **Development Copilot**: Agent integrated with local dev environment, managing git operations, running tests, and assisting with code reviews
- **Research Assistant**: Always-on agent monitoring RSS feeds, summarizing articles, and maintaining a personal knowledge base
- **Home Automation Hub**: OpenClaw connected to local IoT devices and MCP servers, managing home automation through natural language

## Related Concepts

- [[agent-harness-primitives]]
- [[agent-sandboxing]]
- [[hermes-agent]]
- [[entities/peter-steinberger]]
- [[entities/nvidia-nemoclaw]]

## Sources

- [OpenClaw GitHub Repository](https://github.com/OpenClaw/OpenClaw)
- [OpenClaw Demystified: The AI Agent That Runs on Your Machine | O. Wulveryck](https://blog.owulveryck.info/2025/10/11/openclaw-demystify-the-ai-agent-that-runs-on-your-machine.html)
- [NVIDIA NemoClaw: Enterprise AI Agent Development Framework](https://developer.nvidia.com/nemoclaw)
