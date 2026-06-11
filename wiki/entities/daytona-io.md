---
title: "Daytona"
type: entity
created: 2026-04-30
updated: 2026-05-22
tags:
  - entity
  - company
  - infrastructure
  - sandbox
related: [ivan-burazin, headless-saas, agent-sandboxing, agent-serverless]
sources:
  - https://www.daytona.io/
  - https://github.com/daytonaio/daytona
  - raw/newsletters/2026-05-22-ainews-daytona-podcast.md
---

# Daytona

**Founded:** 2023
**CEO:** [[entities/ivan-burazin]]
**Website:** https://www.daytona.io/
**GitHub:** https://github.com/daytonaio/daytona

## Overview

Daytona builds **composable computers (sandboxes) for AI agents** — fast, stateful computing environments that let AI agents run code, commands, and computer-use workflows with full control over CPU, RAM, disk, and OS, provisioned in under 60 milliseconds.

## Key Products

- **Daytona Sandbox** — Sub-60ms provisioning of isolated computing environments
- **macOS Sandboxes** — Early access (Oct 2025)
- **Computer Use Support** — Full GUI interaction capabilities for agents

## Funding

| Date | Round | Amount | Lead |
|------|-------|--------|------|
| Nov 2023 | Pre-Seed | $2M | — |
| Jun 2024 | Seed | $5M | Upfront Ventures |

## Milestones

- **Mar 2024:** Open-sourced Daytona
- **Oct 2025:** 1M+ sandboxes per day
- **Jun 2025:** Launched macOS sandboxes (early access)

## Related Concepts

- [[concepts/security-and-governance/agent-sandboxing]] — Daytona's core technology category
- [[concepts/headless-saas]] — Ivan Burazin's framing of the broader trend
- [[concepts/harness-engineering/agent-serverless]] — Serverless computing for AI agents

## Sources

- [Daytona.io](https://www.daytona.io/)
- [GitHub: daytonaio/daytona](https://github.com/daytonaio/daytona)

## Developments (May 2026)

### Daytona Podcast

Ivan Burazin presented new technical details in a podcast (May 2026):

**Performance:**
- **60ms** sandbox provisioning
- **50,000 sandboxes** in **75 seconds**
- **850,000 sandboxes/day** for largest customer

**Architecture:**
- **Custom scheduler** — no Kubernetes; bare metal + NVMe
- **Dynamic resize** without restart
- **3 isolation layers**: Docker + Sysbox + custom networking
- **Usage shift**: RL/evals are now 50% of total sandbox usage

**Philosophy:**
- **CLI > MCP** — CLI is more composable for agent-computer interaction
- Vision: AI cloud is closer to Stripe than AWS
