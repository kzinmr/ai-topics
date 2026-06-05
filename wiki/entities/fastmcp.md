---
title: FastMCP
type: entity
aliases: [fast-mcp]
created: 2026-06-05
updated: 2026-06-05
status: L2
tags:
  - mcp
  - framework
  - python
  - open-source
  - developer-tooling
  - tool-use
sources:
  - raw/articles/2026-05-27_hugobowne_the-agentic-software-factory.md
  - transcripts/2026-05-08_vanishing-gradients_show-us-your-agent-skills-ep1.md
  - https://hugobowne.substack.com/p/the-agentic-software-factory
---

# FastMCP

**Python framework for building MCP (Model Context Protocol) servers.** Core maintained by [[entities/jeremiah-lowin|Jeremiah Lowin]]. FastMCP is the dominant Python library for creating MCP servers, and has spun off **Prefab** (a Python front-end framework for MCP apps).

## Overview

FastMCP provides a Pythonic interface for building MCP servers that expose tools, resources, and prompts to AI agents. It handles the protocol boilerplate so developers can focus on business logic.

## Key Features

| Feature | Description |
|---------|-------------|
| **Python-first** | Native Python decorators for defining tools and resources |
| **FastMCP Server** | High-performance server implementation |
| **Type-safe** | Pydantic-based type validation |
| **Transport** | stdio and HTTP transports supported |
| **Ecosystem** | Growing collection of community servers |

## Prefab (Spin-off)

**Prefab** is a Python front-end framework for MCP apps spun out of FastMCP by Jeremiah Lowin. It enables building dashboards and UIs that connect to MCP servers without requiring a backend.

> *"I desperately wanted to create MCP apps in Python, and that meant I needed a Python front-end framework that didn't require a backend, which almost every one of them assumes a very specific backend, which we don't get here. We have an MCP server."* — Jeremiah Lowin, Show Us Your Agent Skills Ep. 1

## MCP in Enterprise

From Jeremiah Lowin's perspective on MCP adoption:

> *"The MCP versus CLI style debate, which I think is stupid if you're an individual, use whichever one you prefer, and non-starter if you're an enterprise. We're not installing a bunch of CLIs on people's machines. We never have. We never will. It's a nightmare. We're going to distribute the business logic centrally."*

> *"Overwhelmingly, the use case for MCP is distributing internal business logic to internal teams in enterprises."*

## Related

- [[entities/jeremiah-lowin]] — Core maintainer
- [[entities/openclaw]] — Uses MCP for integrations
- [[concepts/personal-software]] — Prefab enables personal MCP apps

## References

- [The Agentic Software Factory](https://hugobowne.substack.com/p/the-agentic-software-factory) (Vanishing Gradients, May 2026)

## Log

- **2026-06-05**: Initial entity page created.
