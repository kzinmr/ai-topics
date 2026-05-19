---
title: Mastra
created: 2026-05-19
updated: 2026-05-19
type: entity
tags: [product, framework, ai-agents, agent-framework, typescript, open-source, developer-tooling, workflow, voice-ai, enterprise-ai]
sources: [raw/articles/2026-05-14_mastra-acp-agents.md, https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.34.0]
---

# Mastra

**Mastra** is an open-source TypeScript framework for building AI-powered applications and agents, created by the team behind Gatsby. 24K+ GitHub stars. Provides a modern stack for agent orchestration, workflows, and real-time voice AI.

## Key Capabilities

- **Agent Framework**: Code-first agent definition with supervisor delegation, multi-agent workflows
- **Workflows**: Durable, stateful workflows with Inngest adapter for production deployment
- **ACP Integration** (v1.34.0, May 2026): [[concepts/mastra-acp-agents]] — ACP-compatible coding agents as tools or subagents
- **Voice AI**: Providers for xAI Grok Voice Agent API (`@mastra/voice-xai-realtime`)
- **Observability**: Trace listing API, retry step tracking
- **Enterprise**: RBAC provider extensions, model allowlist/admin policies (EE)

## Architecture

Agents support tools, subagents (including ACP), metadata (static/dynamic), and can be composed into supervisors and workflows. Workspace abstraction handles filesystem, sandbox, and media operations.

## Related

- [[concepts/mastra-acp-agents]] — ACP-compatible agents in Mastra
- [[entities/langchain]] — Alternative agent framework
- [[concepts/agent-development-kit]] — Google's ADK
- [[concepts/acp-agent-communication-protocol]] — ACP protocol
