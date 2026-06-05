---
title: "Microsoft Scout"
type: concept
created: 2026-06-05
updated: 2026-06-05
tags:
  - product
  - microsoft
  - ai-agents
  - managed-agents
  - enterprise-ai
aliases: [Scout, Microsoft Scout Agent, Autopilot Agent, M365 Scout]
sources:
  - raw/articles/2026-06-02_microsoft_scout-autopilot-agent.md
  - raw/newsletters/2026-06-04-build-tools-to-build-more.md
---

# Microsoft Scout

**Microsoft Scout** is Microsoft's first "Autopilot" — an always-on AI agent that operates autonomously within [[entities/microsoft|Microsoft 365]], with its own governed identity (Entra ID). Announced June 2, 2026 at Microsoft Build, Scout represents a new category of agents called **Autopilots**: persistent, background-running agents that act on the user's behalf without needing to be prompted each time.

## Architecture

### Autopilot Category

Microsoft defined a new agent category called Autopilots with three defining characteristics:

1. **Always-on**: Active in the background continuously, not triggered by user prompts
2. **Own Identity**: Each agent operates under its own governed Entra ID identity
3. **Autonomous Action**: Takes action without requiring per-task prompting

### OpenClaw Foundation

Scout is built on **OpenClaw**, an open-source agent framework. Microsoft is contributing policy conformance checks directly upstream to OpenClaw, allowing organizations running OpenClaw to validate whether their environment is configured within security and compliance requirements.

### Work IQ

A learning system that builds contextual knowledge about the user's work patterns over time:
- Learns how the user works, what they prioritize
- Tracks what needs to happen next across tasks and meetings
- Carries work forward — becoming more useful and aligned over time

## Capabilities

### Proactive Coordination
- Automatically schedules and coordinates meeting times across time zones
- Flags important meetings and generates pre-meeting preparation materials
- Identifies coordination gaps and surfaces them before they become blockers

### M365 Integration
Operates across cloud, desktop, and web, connecting to:
- **Teams** — Chats, meetings, channels
- **Outlook** — Email, calendar
- **OneDrive** — Files and documents
- **SharePoint** — Team sites and content

### Enterprise Security
| Feature | Description |
|---------|-------------|
| **Identity per agent** | Governed Entra ID, not shared service account |
| **Scoped credentials** | Access restricted to task scope, redacted from logs |
| **Human sign-off** | Sensitive actions require user approval |
| **Purview integration** | Microsoft Purview data protection policies apply |
| **Intune policy** | Configuration managed via Intune |

## Availability

- **Private preview**: Beginning June 2026, select customers
- **Frontier** program: Experimental release for Frontier organizations
- **Requirements**: GitHub Copilot license, Intune policy configuration, Frontier enrollment, opt-in attestation
- Internal Microsoft deployment: Early desktop experience already used by Microsoft employees

## Strategic Positioning

Microsoft Scout contrasts with [[concepts/google-ai-gemini-spark|Gemini Spark]] (Google's always-on agent) — Scout emphasizes enterprise identity governance (Entra ID) and deep M365 integration, while adopting the open-source OpenClaw framework rather than building a proprietary runtime.

## Related

- [[entities/microsoft]] — Parent company
- [[concepts/openclaw-agent]] — Open-source agent runtime foundation
- [[concepts/microsoft-agent-365]] — M365 Copilot agent ecosystem
- [[concepts/google-ai-gemini-spark|Gemini Spark]] — Competitive always-on agent from Google
- [[concepts/microsoft-mai-models]] — Microsoft's AI model family
- [[concepts/agentic-engineering]] — Developer-agent workflow patterns
