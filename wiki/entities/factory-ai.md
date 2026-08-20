---
title: "Factory.ai"
type: entity
created: 2026-06-03
updated: 2026-08-20
tags:
  - company
  - coding-agents
  - developer-tooling
aliases:
  - "Factory"
sources:
  - https://factory.ai/
  - https://factory.ai/news/factory-router
  - raw/articles/2026-06-03_factory_factory-router.md
  - raw/articles/2026-06-15_factory-ai_software-factory-2.0.md
  - raw/articles/2026-08-12_factory_nvidia-dgx-spark.md
  - raw/articles/2026-08-20_factory_factory-partner-network.md
---

# Factory.ai

**Factory.ai** is a coding agent platform focused on autonomous software development. The company builds agent-based development tools that aim to automate complex engineering workflows.

## Key Facts

- Factory positions itself as an autonomous coding agent platform
- Focuses on "frontier performance at lower cost" with custom-built agent orchestration

## Factory Router (June 2026)

Factory launched a **Router** product — described as "frontier performance at lower cost, custom done for you." The Router entered private research preview on June 1, 2026.

Details are limited as the announcement page contains only a brief teaser with no technical specifications. The product is in research preview status.

Source: raw/articles/2026-06-03_factory_factory-router.md

## Software Factory 2.0 (June 2026)

On June 15, 2026, Factory.ai announced **Factory 2.0: From coding agents to software factories**, expanding from standalone coding agents to an interconnected, agent-native, end-to-end software factory system.

### Vision

Factory 2.0 reconceptualizes software development as a factory system where multiple autonomous agents coordinate across the full SDLC, rather than operating as isolated coding assistants.

### Key Pillars

- **Model Independence** — A Router selects the best model per task, optimizing for performance and cost without vendor lock-in
- **Sovereign Intelligence** — Self-hosted deployment with full data ownership and continual learning capabilities; customers retain control over proprietary code and processes
- **Continual Learning & Self-Improvement** — Full SDLC instrumentation enables the system to learn from outcomes and improve over time
- **Spectrum of Autonomy** — Four graduated tiers of agent autonomy:
  - *Droids* — task-level autonomous agents
  - *Automations* — workflow-level automation
  - *Droid Computers* — full development environment agents
  - *Missions* — end-to-end project-level autonomy

### Production Customers

Factory 2.0 is live with enterprise customers including: NVIDIA, EY, Adobe, Palo Alto Networks, Adyen, Blackstone, Wipro, and Comarch.

## Incident Response (July 2026)

Factory announced **Incident Response** functionality for its Droid autonomous agents (July 10, 2026). The feature enables Droids to automatically transform Slack alerts into autonomous root cause analysis (RCA) sessions, build incident memory across occurrences, and help on-call engineers reduce the signal-to-fix cycle time.

The incident response capability is described as a 2-minute-read feature announcement, positioning it as a practical operational extension of Factory's autonomous agent platform rather than a major product release.

Source: raw/articles/2026-07-11_factory_incident-response.md

## Local Autonomous Software Engineering on NVIDIA DGX Spark (August 2026)

Factory announced (Aug 11, 2026) that **security-sensitive teams can run the autonomous software factory locally on NVIDIA DGX Spark with NVIDIA Nemotron 3.5 Lightning**, keeping source code, operational context, and execution entirely inside their own environment.

Key points:
- **Local deployment for high-security environments**: the full Factory autonomous software engineering loop (Droids, Automations, Missions) runs on-prem on DGX Spark hardware
- **NVIDIA Nemotron 3.5 Lightning** serves as the local model for the agent stack
- **Data sovereignty**: source code, operational context, and execution never leave the customer environment — a concrete realization of the "Sovereign Intelligence" pillar from Factory 2.0 (self-hosted deployment with full data ownership)
- Complements the existing NVIDIA relationship: NVIDIA is already a Factory 2.0 production customer and Fireworks' LangChain Deep Agents work runs Nemotron on NVIDIA Blackwell

Source: raw/articles/2026-08-12_factory_nvidia-dgx-spark.md

## Factory Partner Network (FPN) (August 2026)

Factory announced the **Factory Partner Network (FPN)** on August 19, 2026 (blog post by Mark Kobe), committing **$100M to partnerships across training, deployment, solutions, and marketing**. The move positions Factory to scale the "Software Factory" model through an ecosystem of integration and delivery partners rather than direct sales alone — an ecosystem play that mirrors the partner-network strategies of larger agentic platforms.

Source: raw/articles/2026-08-20_factory_factory-partner-network.md

## Related

- [[entities/codex]] — OpenAI's coding agent, likely a competitive/related product
- [[concepts/ai-agent-engineering]] — broader category of agent orchestration platforms
