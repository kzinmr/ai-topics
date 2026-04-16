---
title: "OpenAI Agents SDK"
created: 2026-04-16
updated: 2026-04-16
tags: [framework, ai-agents, openai, sandbox, harness, compute, tooling]
aliases: ["OpenAI Agent SDK", "openai-agents"]
---

# OpenAI Agents SDK (v0.14.0)

| | |
|---|---|
| **Package** | `openai-agents>=0.14.0` |
| **Release Date** | April 15, 2026 (GA) |
| **Language** | Python (TypeScript planned) |
| **Developer** | [[entities/openai]] |
| **API** | [platform.openai.com](https://platform.openai.com) |
| **Docs** | [Sandbox Agents Guide](https://developers.openai.com/api/docs/guides/agents/sandboxes) |

## Overview

The OpenAI Agents SDK is a standardized, model-native framework for building production-ready AI agents. Version 0.14.0 introduced **native sandbox execution**, enabling agents to safely inspect files, run commands, edit code, and execute long-horizon tasks within controlled, isolated environments.

## Core Architecture

### Harness vs Compute Separation

The SDK introduces a fundamental architectural split:

| Plane | Responsibility | Examples |
|---|---|---|
| **Harness (Control)** | Agent loop, model calls, tool routing, handoffs, approvals, tracing, recovery, auth, billing | OpenAI infrastructure |
| **Compute (Execution)** | File I/O, commands, dependency installs, port exposure, provider-specific state | Sandbox environments |

> *"The key split is the boundary between the harness and compute."*

This separation mitigates prompt-injection/exfiltration risks and isolates credentials from model-generated code.

### Standardized Integrations

- **MCP** — Tool use via Model Context Protocol
- **Skills** — Progressive disclosure via [[agent-skills]]
- **AGENTS.md** — Custom instructions
- **Shell** — Code execution
- **Apply Patch** — File edits

### Sandbox Execution

- **Providers:** Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, Vercel (BYO-sandbox supported)
- **Manifest Abstraction:** Workspace contract defining files, dirs, repos, mounts, env vars, users/groups
- **Cloud Storage Integration:** AWS S3, Google Cloud Storage, Azure Blob Storage, Cloudflare R2
- **Security:** Workspace-relative paths only; absolute paths and `..` traversal blocked
- **Durability:** Externalized agent state enables snapshotting & rehydration

## Key Components

### SandboxAgent
```python
from agents.sandbox import SandboxAgent, Manifest
from agents.sandbox.entries import LocalDir

agent = SandboxAgent(
    name="Dataroom Analyst",
    model="gpt-5.4",
    instructions="Answer using only files in data/. Cite source filenames.",
    default_manifest=Manifest(entries={"data": LocalDir(src=dataroom)}),
)
```

### Capabilities
| Capability | Purpose |
|---|---|
| `Shell()` | Command execution, interactive input |
| `Filesystem()` | Edit files, inspect images |
| `Skills()` | Repeatable instructions/scripts/assets |
| `Memory()` | Persist lessons across runs |
| `Compaction()` | Long-running context trimming |

### Session Resolution Order
1. `run_config.sandbox.session` → Live session reuse
2. `RunState` → Resume from saved state
3. `run_config.sandbox.session_state` → Serialized state
4. Fallback → New session

## Security Model

- **Default-Deny:** Sandboxes start with zero permissions
- **Path Isolation:** Workspace-relative paths only
- **Credential Handling:** Runtime configuration, never prompt content
- **Provider-Native Secrets:** Use hosted sandbox secret systems
- **Artifact Review:** Export only after reviewing generated content

## Provider Ecosystem

| Provider | Type | Notes |
|---|---|---|
| **Blaxel** | Cloud sandbox | Multi-tenant |
| **Cloudflare** | Edge compute | Workers integration |
| **Daytona** | Dev environments | Secure sandboxes |
| **E2B** | Cloud sandbox | Specialized for AI agents |
| **Modal** | Serverless | GPU support |
| **Runloop** | Cloud sandbox | Fast boot times |
| **Vercel** | Edge/Serverless | Web deployment |

## Pricing & Availability

- **Status:** Generally Available (GA)
- **Access:** OpenAI API
- **Pricing:** Standard API pricing (tokens + tool use)

## Customer Validation

> *"The updated Agents SDK made it production-viable for us to automate a critical clinical records workflow that previous approaches couldn't handle reliably enough."*
> — **Rachael Burns**, Staff Engineer & AI Tech Lead, Oscar Health

## Roadmap

- **TypeScript SDK** (planned)
- **Code mode & subagents** (rolling out to Python & TS)
- **Additional sandbox providers**
- **Deeper third-party integrations**

## Related Concepts

- [[harness-engineering]] — Ryan Lopopolo / OpenAI Symphony orchestration philosophy
- [[sandbox/_index]] — AI agent sandbox isolation technologies
- [[sandbox/infrastructure]] — Container, microVM, gVisor-level isolation
- [[agent-skills]] — SKILL.md bundles
- [[agentic-engineering/how-agents-work]] — Coding agent architecture

## Entity Connections

- [[entities/openai]] — Developer
- [[entities/samuel-colvin]] — Monty (in-process sandbox) developer
- [[entities/anthropic]] — Competitor (Managed Agents, Computer Use)
- [[entities/cognition]] — Competitor (Devin)

## Sources

- [[raw/articles/openai-agents-sdk-next-evolution-2026-04]]
- [[raw/articles/openai-sandbox-agents-api-guide-2026-04]]
- [OpenAI Agents SDK Blog (2026-04-15)](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)
- [OpenAI API Sandbox Docs](https://developers.openai.com/api/docs/guides/agents/sandboxes)
