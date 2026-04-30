---
title: "Agent Communication Standards — ACP, A2A, BeeAI"
type: concept
created: 2026-04-30
updated: 2026-04-30
tags: [agent-communication, protocol, standards, linux-foundation, beeai, a2a, acp]
sources:
  - raw/articles/2025-08-25_i-am-bee_acp-joins-a2a.md
  - raw/articles/2026-02-01_philschmid_acp-overview.md
  - https://github.com/orgs/i-am-bee/discussions/5
  - https://www.philschmid.de/acp-overview
related:
  - concepts/model-context-protocol-mcp
  - concepts/harness-engineering
  - concepts/agentic-engineering
---

# Agent Communication Standards — ACP, A2A, BeeAI

The AI agent ecosystem has converged around two primary communication paradigms: **Agent-to-Agent protocols** (A2A, ACP) and **Agent-Client protocols** (ACP - Agent Client Protocol). As of August 2025, these are merging under the Linux Foundation.

## Timeline of Convergence

| Date | Event |
|---|---|
| March 2025 | IBM Research launches ACP (Agent Communication Protocol) for BeeAI Platform |
| Late March 2025 | BeeAI and ACP donated to Linux Foundation |
| April 2025 | Agent2Agent (A2A) Protocol launched by Google |
| February 2026 | Philipp Schmid publishes comprehensive ACP overview covering agent-client patterns |
| August 2025 | Official merger of ACP into A2A announced (note: chronology shows A2A launched after ACP but merger happened later) |

**Key Organizational Change**: Kate Blair (IBM Research, Director of Incubation) joins the **A2A Technical Steering Committee (TSC)**. The TSC now includes representatives from Google, Microsoft, AWS, Cisco, Salesforce, ServiceNow, SAP, and IBM.

## ACP (Agent Communication Protocol)

Originally developed by IBM Research for the BeeAI Platform, ACP enables agents to communicate with clients (IDEs, web interfaces, CLI tools).

### ACP Overview (Philipp Schmid, Feb 2026)

With the explosion of AI coding agents — Claude Code, Gemini CLI, OpenCode, Goose, Codex CLI — every major AI lab ships their own client-based coding agent. ACP provides a **standardized interface** for agent-client communication:

- **Agent Discovery**: Clients can discover available agents and their capabilities
- **Task Submission**: Standardized task format with context, constraints, and expected outputs
- **Streaming Responses**: Real-time agent output delivery to clients
- **Session Management**: Persistent agent sessions with state tracking

> ACP is to agents what MCP is to tools — a standardized communication layer that enables interoperability across different agent implementations.

### BeeAI Platform Integration

The BeeAI platform, previously ACP-dependent, is transitioning to A2A:
- **A2AServer Adapter**: Makes BeeAI framework agents A2A-compliant
- **A2AAgent Integration**: Allows external A2A agents to integrate into BeeAI applications
- **Native A2A Support**: Platform now uses A2A for cross-framework agent interaction

## A2A (Agent2Agent Protocol)

Launched by Google in April 2025, A2A is designed for **direct agent-to-agent communication** — enabling agents from different frameworks to collaborate without human intermediaries.

### Key Features
- **Agent Cards**: Standardized metadata describing agent capabilities
- **Task Protocol**: Structured request/response for inter-agent work
- **Cross-Framework Compatibility**: Agents from any framework can communicate

## Why the Merger Matters

The ACP→A2A merger consolidates two complementary protocols:

1. **ACP**: Agent-to-client communication (IDE ↔ Agent, Web UI ↔ Agent)
2. **A2A**: Agent-to-agent communication (Agent ↔ Agent)

Together, they form a complete stack for multi-agent systems:
- **Human-facing**: ACP handles how users interact with agents through various clients
- **Agent-facing**: A2A handles how agents discover and collaborate with each other

## Relationship to MCP

| Protocol | Purpose | Scope |
|---|---|---|
| **MCP** (Model Context Protocol) | Tool discovery and execution | Agent ↔ Tools |
| **ACP** (Agent Client Protocol) | Task submission and streaming | Client ↔ Agent |
| **A2A** (Agent2Agent Protocol) | Agent collaboration and coordination | Agent ↔ Agent |

Together, these three protocols form the **agent interoperability stack**:
```
User/Client ──ACP──→ Agent ──MCP──→ Tools
                        │
                       A2A
                        │
                    Other Agents
```

## Migration Resources
- [Migration Guide](https://github.com/i-am-bee/beeai-platform/blob/main/docs/community-and-support/acp-a2a-migration-guide.mdx)
- [A2A GitHub Issues](https://github.com/a2aproject/A2A/issues) (tracking ACP feature porting)
- [BeeAI A2A Integrations Documentation](https://framework.beeai.dev/integrations/a2a)
- [ACP Overview](https://www.philschmid.de/acp-overview) — Philipp Schmid, February 2026

## See Also
- [[concepts/model-context-protocol-mcp]]
- [[concepts/harness-engineering]]
- [[concepts/agentic-engineering]]
- [[concepts/agent-interoperability]]