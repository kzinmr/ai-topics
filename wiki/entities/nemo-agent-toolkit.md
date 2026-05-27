---
title: NVIDIA NeMo Agent Toolkit
created: 2026-05-27
updated: 2026-05-27
type: entity
tags: [entity, platform, nvidia, ai-agents, agent-framework, multi-agent, orchestration, observability, open-source, mcp]
sources:
  - raw/articles/2026-05-27_nemo-agent-toolkit-v1-7-0.md
  - https://github.com/NVIDIA/NeMo-Agent-Toolkit/releases/tag/v1.7.0
---

# NVIDIA NeMo Agent Toolkit

**NVIDIA NeMo Agent Toolkit (NAT)** is an open-source library for efficiently connecting and optimizing teams of AI agents. At 2K+ GitHub stars, it provides a Python framework for building, orchestrating, and deploying multi-agent systems with observability, security hardening, and enterprise-grade tooling.

## Overview

NAT provides a CLI (`nat`) and Python SDK for agent orchestration, supporting ReAct agents, multi-agent workflows, and integration with NVIDIA's ecosystem including Nemotron models and OCI (Oracle Cloud Infrastructure) deployments.

## v1.7.0 Highlights (May 21, 2026)

### New Capabilities
- **AI coding agent skills** — first-class support for coding agent workflows
- **ATOF v0.1** — Agentic Trajectory Observability Format, an open spec for agent execution traces
- **Exa Search API** integration as internet search tool
- **OCI LangChain support** for hosted Nemotron workflows
- **Arize AX OTLP exporter** — OpenTelemetry-based observability

### Observability Stack
- **ATIF trajectory exporter** for Phoenix visualization and debugging
- **Consent-gated telemetry** for CLI commands (privacy-preserving)
- Multiple exporters: Phoenix, Arize AX

### Agent Runtime Improvements
- **Token streaming** support for ReAct Agent
- **OAuth2** MCP support (client-id-only)
- Security hardening: no exception details leaked in `chat_completion` errors
- Dependency slimming: removed `flask`, `optuna`, `chain`, `openinference` from core

### Breaking Changes
- OpenAI dependency migrated from 1.x to 2.x
- Removed `nvidia-nat-vanna` integration

## Architecture

NAT is built around a modular agent framework supporting:
- **ReAct agents** with streaming
- **Multi-agent orchestration** with MCP-based tool sharing
- **Trajectory observability** via ATOF/ATIF/OTLP
- **Enterprise authentication** with OAuth2
- **Model integration** with Nemotron, OpenAI, and open-weight models

## Related

- [[entities/nvidia]] — NVIDIA ecosystem
- [[concepts/agent-observability]] — agent observability
- [[concepts/mcp]] — Model Context Protocol
- [[entities/microsoft-agent-framework]] — Microsoft's agent framework
- [[entities/google-adk]] — Google's Agent Development Kit

## References

- GitHub: [NVIDIA/NeMo-Agent-Toolkit](https://github.com/NVIDIA/NeMo-Agent-Toolkit)
- Release: [v1.7.0](https://github.com/NVIDIA/NeMo-Agent-Toolkit/releases/tag/v1.7.0)
