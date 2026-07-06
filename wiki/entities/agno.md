---
title: "Agno"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [agent-platform, agent-framework, open-source, agent-sdk, agent-runtime, agent-observability, multi-agent, control-plane, multi-tenancy, self-hosted]
sources: [raw/articles/2026-06-29_agno_welcome-docs.md]
---

# Agno

**Agno** is an open-source SDK and runtime for building, running, and managing agent platforms. It is model, framework, and cloud agnostic — designed to let any company operate their own agent infrastructure.

## Architecture

Agno has two main components:

| Component | Purpose |
|-----------|---------|
| **Agno SDK** | Build agents, multi-agent teams, and step-based agentic workflows |
| **AgentOS Runtime** | Productionize agents as APIs with multi-user sessions, tracing, scheduling, RBAC, and audit logs |

A unified **control plane** provides full visibility and management. Everything runs in your cloud, with your data staying in your database.

## Use Cases

- **Product teams**: In-product agents and chat copilots
- **ML teams**: Text, image, audio, video data labeling (natively typesafe and multi-modal)
- **AI teams**: Synthetic data generation, document processing, eval generation
- **Data science**: Data enrichment, segmentation, training data curation
- **Data engineering**: Data quality audits, failure log analysis, weekly reports

## Key Features

- **Model-agnostic**: Works with any model provider
- **Framework-agnostic**: Not tied to any agent framework
- **Cloud-agnostic**: Deploy in your own cloud infrastructure
- **Multi-user sessions**: Isolated agent sessions with tracing
- **RBAC**: Role-based access control for agent platforms
- **Scheduling**: Cron-based agent execution
- **Self-improving**: Use session data to auto-improve agents

## Links
- Documentation: https://docs.agno.com
- Demo AgentOS: https://os.agno.com/try-demo
- GitHub: https://github.com/agno-agi/agno

## Related
- [[concepts/agent-platform]] — AI agent platforms
- [[concepts/agent-framework]] — Agent development frameworks
- [[concepts/agent-runtime]] — Agent runtime environments
- [[concepts/agent-observability]] — Agent monitoring and tracing

## Related Pages
- [[entities/_index]]

