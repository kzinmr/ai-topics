---
title: "Container Context"
type: concept
aliases:
  - hosted-container
  - agent-container
  - container-workspace
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - architecture
  - harness-engineering
  - infrastructure
status: draft
sources:
  - "https://openai.com/index/equip-responses-api-computer-environment/"
---

# Container Context

A hosted container providing agents with a **persistent execution environment**. A "model workspace" integrating filesystem, database, and network access.

## Three Pillars

### 1. Filesystem
- Persisted in `/workspace` directory
- Stage input resources into the container
- **Anti-pattern**: Pasting large files/tables directly into the prompt
- **Best Practice**: Place resources in the container, let the model selectively open what it needs

> "Much like humans, models work better with organized information."

### 2. Database (SQLite)
- Store and query structured data
- Instead of copying entire spreadsheets into the prompt, describe the table structure
- The model can query only the rows it needs

**Example**:
```
Prompt: "Which products had declining sales this quarter?"
→ Model queries only relevant rows (no full scan)
→ Faster, cheaper, scalable to large datasets
```

### 3. Network Access
- Live data retrieval, external API calls, package installation
- Controlled via **sidecar egress proxy**
- Domain-scoped secret injection

## Container Spec (As of March 2026)

| Resource | Value |
|----------|-----|
| vCPU | 4 |
| RAM | 8GB |
| Workspace | Up to 10GB |
| Pre-installed | Python 3.12, Node.js 22, Go 1.24, Java 21 |
| Storage Cost | $0.03/GB-hour |

## Session Management

```bash
# Create persistent container session
session = client.responses.sessions.create(
    model="gpt-5.4",
    tools=[{"type": "shell"}],
    container_config={
        "persist_workspace": True
    }
)
```

## Design Philosophy

OpenAI chose the approach of "providing managed containers rather than having developers build their own execution environments." This contrasts with **Anthropic's approach of "developers designing the harness."**

| | OpenAI | Anthropic |
|--|--------|-----------|
| Runtime | Managed container | Developer implementation |
| Flexibility | Limited (within sandbox) | Maximum control |
| Developer Burden | Minimal | Medium to high |
| Portability | OpenAI-dependent | Model-agnostic |

## Related Concepts

- [[concepts/agent-loop-orchestration]] — Loop execution within containers
- [[concepts/harness-engineering/system-architecture/agent-security-patterns]] — Network control and secret management
- [[concepts/harness-engineering]] — Higher-level execution environment design

## References

- [OpenAI: Equipping the Responses API with a computer environment](https://openai.com/index/equip-responses-api-computer-environment/)
- [[entities/openai]] — OpenAI
