---
title: MCP (Model Context Protocol)
created: 2026-04-26
updated: 2026-04-26
type: concept
tags: [protocol, agentic-engineering, tool]
sources: [raw/articles/troyhunt.com--heres-what-agentic-ai-can-do-with-have-i-been-pwneds-apis--7eefad3f.md, raw/articles/2026-04-25-langchain-anatomy-agent-harness.md, raw/articles/gemini-deep-research-agent.md]
---

# MCP (Model Context Protocol)

## Overview

**Model Context Protocol (MCP)** is an open standard that defines how AI agents discover, authenticate with, and call tools over a network. Created by Anthropic, MCP serves as a universal "USB-C for AI" — one protocol that connects any agent to any tool, eliminating the fragmented ecosystem where tools built for one framework did not work with another.

Think of it as a standardization layer between AI applications (Claude, ChatGPT, Gemini, custom agents) and external systems (databases, APIs, file systems, search engines, calculators, workflows).

## Core Architecture

MCP defines three primary abstractions:

1. **Resources** — Read-only data sources that agents can access (files, database queries, API endpoints)
2. **Tools** — Callable functions that agents can invoke (search, compute, execute code, send emails)
3. **Prompts** — Pre-defined conversation templates that guide agent interactions

An MCP server exposes these abstractions over a transport layer (stdio or HTTP). An MCP client (AI application or agent harness) discovers available tools and resources, then invokes them in a standardized way.

### Key Design Principles

- **Discovery-first**: Agents can enumerate available tools at runtime rather than requiring hardcoded integrations
- **Authentication at protocol level**: Each MCP server handles its own auth (API keys, OAuth, etc.)
- **Transport agnostic**: Works over stdio (local subprocess) or HTTP (remote servers)
- **Schema-driven tool definitions**: Tools declare their parameters with JSON schemas for validation

## Ecosystem Adoption

### Anthropic (Originator)
MCP was created by Anthropic. The Anthropic SDK has accumulated **150M+ downloads** across package registries, outpacing React's first 3 years in just 16 months. MCP is the default tool integration mechanism in Claude Code.

### OpenAI (Adopter)
In March 2025, OpenAI announced adoption of MCP across its products — the first time OpenAI embraced a rival's standard. Sam Altman stated: "People love MCP and we are excited to add support across our products." MCP is available in the OpenAI Agents SDK, ChatGPT desktop app, and Responses API.

### Google
Gemini Deep Research Agent adds MCP integration, enabling custom tool and data source extensibility.

### Enterprise Platforms
- **Red Hat OpenShift AI 3**: Adds MCP support directly to the platform with guided server creation, containerization, and deployment
- **VS Code, Cursor, Windsurf**: MCP servers can be configured as tool integrations
- **Gemini-CLI**: MCP tool integration support

### Security Concerns
OX Security identified serious vulnerabilities in MCP implementations — specifically **Remote Code Execution (RCE) across the AI agent ecosystem**. MCP's universal tool access model means a compromised MCP server can execute arbitrary code in the agent's context. Thousands of community-published MCP servers increase the attack surface.

## MCP in Agent Harnesses

MCP is one of the core primitives in the agent harness architecture:

> **Agent = Model + Harness**

The harness layer (not the model itself) provides:
- Filesystems for durable storage
- Code execution (Bash)
- **Tools & Skills (MCPs, custom tools, encoded engineering taste)**
- Orchestration logic (subagent spawning, handoffs)
- Feedback loops and recovery mechanisms

Without external tools via MCP, an agent "in isolation is rather dumb" — it can only operate within its training data. MCP dramatically increases agent autonomy by enabling on-the-fly tool selection.

## Use Cases

### Enterprise Data Access
MCP enables agents to connect to internal databases, CRMs, and knowledge bases without custom integration code:

```json
{
  "url": "https://haveibeenpwned.com/mcp",
  "headers": {
    "hibp-api-key": "YOUR_STANDARD_HIBP_API_KEY"
  },
  "type": "http"
}
```

### Security & Compliance
Security teams use MCP to build agents that can:
- Monitor breach notifications across organizations
- Identify compromised employee accounts
- Automate security incident response

### Developer Tooling
MCP servers for GitHub, databases, and file systems enable AI coding agents (Claude Code, Codex, Gemini CLI) to interact with external infrastructure naturally.

## 2026 Roadmap

MCP creator David Soria Parra outlined the 2026 roadmap at a keynote:

- **Triggers**: Event-driven MCP server activation (webhooks, file changes)
- **Streaming**: Real-time data streaming from MCP servers
- **Skills**: Pre-configured tool bundles for common workflows
- **Enterprise integration**: Deeper support for production AI agent pipelines

## Open Questions & Debates

1. **Context bloat**: Critics argue MCP adds unnecessary abstraction layers. Some argue custom integrations are simpler for single-agent setups.
2. **Security surface**: Thousands of community MCP servers create supply-chain risks. Who audits MCP server code before deployment?
3. **Protocol maturity**: MCP is still young. How does it compare to alternatives like OpenAI's function calling or custom agent tool protocols?
4. **Vendor lock-in vs. openness**: Anthropic created MCP but OpenAI, Google, and Microsoft have all adopted it. Is MCP truly vendor-neutral?

## Related Concepts

- [[concepts/harness-engineering]] — Agent harness architecture where MCP serves as the tool integration layer
- [[claude-code]] — Anthropic's agentic coding system with native MCP support
- [[ai-agent-platforms]] — Platform comparison including MCP as a tool integration standard
- [[concepts/multi-agent-orchestration-architecture]] — MCP as part of the tooling layer in multi-agent systems
- [[concepts/agent-governance]] — Runtime guardrails that apply to MCP tool invocations
