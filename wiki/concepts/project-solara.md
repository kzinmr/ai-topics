---
title: "Project Solara"
type: concept
created: 2026-06-08
updated: 2026-06-08
tags:
  - microsoft
  - agent-first
  - hardware
  - ai-agents
  - build-2026
sources:
  - https://commandline.microsoft.com/project-solara-build-2026/
---

# Project Solara

**Project Solara** is a chip-to-cloud software platform from Microsoft, designed from the ground up for **agent-first devices** — a new category of computing hardware where the primary interaction model is AI agents rather than traditional applications. Announced at Build 2026 by Steven Bathiche (CVP & Technical Fellow, Applied Sciences Group).

## Core Thesis

> "The next platform shift is from apps to agents — from software you open to intelligence you invoke; from graphical interfaces of buttons to expressing intent directly."

Solara's premise is that **agents as a new unit of programming** reduce the traditional cost and complexity of creating specialized computing hardware. Historically, each new form factor required rebuilding almost the entire stack (silicon, firmware, OS, UI patterns, app model, dev tools). With AI-generated just-in-time UI and multi-agent orchestration, the marginal cost of specialization drops dramatically.

## Reference Designs

Two concept-device categories were announced as reference designs for the ecosystem:

### 1. Qualcomm Wearable Badge (Portable)

- Lightweight, always-connected companion in an **access badge** form factor
- Hello for Business with fingerprint recognition — "always a touch away from your agents"
- Integrated camera for environment-aware agent interactions (user-permission-gated)
- Glanceable Priority Cards, one-tap agent invocation
- Target users: information workers, nurses, front-line workers
- Qualcomm lead: Dino Bekis (SVP, Personal & Computing) — emphasized breadth across wearable form factors

### 2. MediaTek Desk Hub (Stationary)

- Desk companion designed for stationary environments
- Hello for Business for frictionless authentication
- Can work stand-alone, as a Windows PC companion, or as a Windows 365 Cloud PC when connected to an external display
- Curated Priority Cards for glanceable calendar and task access
- MediaTek lead: Vince Hu (SVP & GM, Data Center & Computing) — emphasized intelligence at the edge
- Target users: information workers, desk workers

Together, the two form factors span portable→stationary, showing how agent-first experiences move across devices.

## Platform Architecture

### Just-in-Time UI

Solara introduces a spectrum of UI adaptability:

| Level | Structure | Description |
|-------|-----------|-------------|
| **Responsive UI** | High structure | Interfaces that reflow predictably across screen sizes (traditional) |
| **Adaptive UI (Solara target)** | Moderate structure | Agents have enough flexibility to tailor interfaces while maintaining reliability |
| **Unconstrained Generation** | Low structure | Models generate full layouts from scratch |

Solara is intentionally building for the **middle of the spectrum** — beyond responsive design but not dependent on unconstrained generation.

### Multi-Agent Ecosystem

> "There will not be a single dominant agent. We are entering a world of many specialized agents."

Solara is designed for an **open, multiple-agent world** where:
- Organizations use Microsoft agents where they add value
- They also use third-party and custom agents
- Platform brings agents together coherently while respecting boundaries between data, domains, identities, and organizations
- Enterprise manageability, identity, security, and privacy are first-class concerns

### Enterprise Foundation

- **Hardware and software manageability** at enterprise scale
- **Privacy protections** with transparency and control mechanisms
- **Work IQ integration** for secure access to work context
- **Microsoft 365 Agents SDK** compatibility — agents built for Microsoft 365 already take the right path

## Pilot Partners

Industry leaders participating in early piloting:

| Partner | Domain |
|---------|--------|
| **AccuWeather** | Weather intelligence |
| **Best Buy** | Consumer electronics retail |
| **CVS Health** | Healthcare & pharmacy |
| **Levi's** | Retail & apparel |
| **Target** | Retail & general merchandise |

## Silicon Partners

| Partner | Role | Focus |
|---------|------|-------|
| **Qualcomm** | First silicon partner | Wearables, portable form factors |
| **MediaTek** | First silicon partner | Stationary devices, IoT ecosystem |

## Strategic Context

Solara represents the culmination of a framework Steven Bathiche first articulated at Build 2023, identifying three AI application structures:

1. **AI beside your app** — Minimal disruption, AI as helper
2. **AI inside your app** — AI as main input loop, redefining interaction (agents emerge here: Researcher, Agent Mode in Office)
3. **AI outside your app** — AI orchestrates across apps and services globally (OpenClaw, Lobster, coworker-like agents)

Solara is Microsoft's bet that the ecosystem is ready for the **third structure** as a primary device interaction model.

## Integration Points

- **OpenClaw** and **Work IQ** — agent orchestration and work management
- **Microsoft 365 Agents SDK** — developer path for Solara-compatible agents
- **Windows 365** — Cloud PC integration for desk hub
- **Copilot Studio** — agent building tools
- **Azure** — cloud-scale backend

## Related

- [[concepts/microsoft-scout-agent]] — Microsoft's always-on Autopilot agent
- [[concepts/microsoft-mai-models]] — Microsoft's first-party model family
- [[concepts/agent-first-devices]] (stub) — Emerging device category
- [[entities/microsoft]] — Parent organization
- [[concepts/agent-team-swarm/agent-team-swarm]] — Multi-agent orchestration patterns
