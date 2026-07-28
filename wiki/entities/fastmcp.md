---
title: FastMCP
type: entity
aliases: [fast-mcp, gofastmcp]
created: 2026-06-05
updated: 2026-07-28
status: enriched
tags:
  - mcp
  - framework
  - developer-tooling
  - open-source
  - tool
  - python
  - ai-agents
sources:
  - raw/articles/2026-05-27_hugobowne_the-agentic-software-factory.md
  - transcripts/2026-05-08_vanishing-gradients_show-us-your-agent-skills-ep1.md
  - https://hugobowne.substack.com/p/the-agentic-software-factory
  - https://github.com/PrefectHQ/fastmcp
  - https://gofastmcp.com
---

# FastMCP

**FastMCP** is the dominant Python framework for building MCP (Model Context Protocol) servers and clients. Maintained by [[entities/jeremiah-lowin|Jeremiah Lowin]] under the **PrefectHQ** organization. It has spun off **Prefab** (a Python front-end framework for MCP apps) and **Prefect Horizon** (enterprise MCP gateway).

> FastMCP 1.0 was incorporated into the official MCP Python SDK. The actively maintained standalone project is downloaded a million times a day and powers ~70% of MCP servers across all languages.

## Quick Start

```python
from fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()
```

## GitHub Stats

| Metric | Value |
|--------|-------|
| **Stars** | 26,910 |
| **Forks** | 2,195 |
| **Language** | Python |
| **License** | Apache-2.0 |
| **Created** | 2024-11-30 |
| **Organization** | PrefectHQ |
| **Open Issues** | 252 |

## The Three Pillars

FastMCP provides three core capabilities:

### Servers
Expose tools, resources, and prompts to LLMs. Python functions are automatically wrapped into MCP-compliant tools with generated schema, validation, and documentation.

### Apps
Give tools interactive UIs rendered directly in the conversation. Enables building dashboards and MCP apps without requiring a separate backend.

### Clients
Connect to any MCP server — local or remote, programmatic or CLI. Full protocol support including transport negotiation and authentication.

## Key Features

- **Python-first**: Native Python decorators for defining tools and resources
- **FastMCP Server**: High-performance server implementation
- **Type-safe**: Pydantic-based type validation
- **Transport**: stdio and HTTP transports supported
- **Ecosystem**: Growing collection of community servers
- **Automatic schema generation**: Declare a tool with a Python function, and the schema, validation, and documentation are generated automatically

## Prefab (Spin-off)

**Prefab** is a Python front-end framework for MCP apps spun out of FastMCP by Jeremiah Lowin. It enables building dashboards and UIs that connect to MCP servers without requiring a backend.

> *"I desperately wanted to create MCP apps in Python, and that meant I needed a Python front-end framework that didn't require a backend, which almost every one of them assumes a very specific backend, which we don't get here. We have an MCP server."* — Jeremiah Lowin, Show Us Your Agent Skills Ep. 1

## Prefect Horizon (Enterprise Gateway)

**Prefect Horizon** is the enterprise MCP gateway for running FastMCP servers safely in production:

- Deploy FastMCP servers from GitHub with branch previews and instant rollback
- Create a private registry of every MCP your company uses
- Secure access with SSO and tool-level RBAC
- Get audit logs, observability, and governance
- Remix approved tools into purpose-built endpoints for teams and agents

## MCP in Enterprise

From Jeremiah Lowin's perspective on MCP adoption:

> *"The MCP versus CLI style debate, which I think is stupid if you're an individual, use whichever one you prefer, and non-starter if you're an enterprise. We're not installing a bunch of CLIs on people's machines. We never have. We never will. It's a nightmare. We're going to distribute the business logic centrally."*

> *"Overwhelmingly, the use case for MCP is distributing internal business logic to internal teams in enterprises."*

## Documentation

Full documentation available at [gofastmcp.com](https://gofastmcp.com), including detailed guides, API references, and advanced patterns. Also available in LLM-friendly `llms.txt` and `llms-full.txt` formats.

## Installation

```bash
uv pip install fastmcp
```

## Related

- [[entities/jeremiah-lowin]] — Core maintainer
- [[entities/openclaw]] — Uses MCP for integrations
- [[concepts/personal-software]] — Prefab enables personal MCP apps
- [[entities/prefect]] — Parent organization
- [[concepts/mcp]] — The Model Context Protocol that FastMCP implements

## References

- [The Agentic Software Factory](https://hugobowne.substack.com/p/the-agentic-software-factory) (Vanishing Gradients, May 2026)
- [GitHub: PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp)
- [Documentation](https://gofastmcp.com)

## Log

- **2026-07-28**: Enriched with GitHub stats (26.9K stars), three pillars architecture, Prefect Horizon enterprise gateway, adoption metrics
- **2026-06-05**: Initial entity page created.
