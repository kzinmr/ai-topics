---
title: Microsoft Copilot Wave 3
created: 2026-05-02
updated: 2026-05-02
type: concept
tags: [product, platform, ai-agents, enterprise, microsoft, anthropic, multi-model, governance]
sources:
  - raw/articles/2026-03-09_microsoft-copilot-wave-3-frontier-transformation.md
---

# Microsoft Copilot Wave 3

**Wave 3 of Microsoft 365 Copilot** (announced March 9, 2026) represents a fundamental architectural shift from AI assistance to embedded agentic capabilities. Built in close collaboration with Anthropic, Wave 3 introduces **Copilot Cowork**, the **Agent 365** governance control plane, and the **Microsoft 365 E7 Frontier Suite**.

## Key Products

### Copilot Cowork
The flagship Wave 3 innovation — an autonomous agent that moves beyond single prompts to long-running, multi-step execution:

- **Built with Anthropic**: Uses technology powering Claude Cowork, integrated into Microsoft 365
- **Multi-model intelligence**: Automatically selects best model (OpenAI or Anthropic) per task
- **Work IQ**: Full contextual awareness of user's work graph (email, calendar, files, chats, contacts)
- **Autonomous execution**: Can work for minutes or hours on complex tasks while remaining observable and steerable
- **Cross-app context**: Sees entire Microsoft 365 tenant simultaneously — no manual linking or uploading
- **Pricing**: Included in existing $30/user/month M365 Copilot license

### Agent 365 — The Control Plane
Centralized governance layer for enterprise agent management:

- **Observe, secure, govern** every agent across the organization
- Integrates with Microsoft Admin Center, Defender, Entra, Purview
- **$15 per user per month**
- **GA: May 1, 2026**

### Microsoft 365 E7 — Frontier Suite
New premium enterprise tier unifying productivity, AI, and security:

| Component | Description |
|-----------|-------------|
| Microsoft 365 Copilot | AI assistant with Cowork capabilities |
| Agent 365 | Agent governance and security |
| Microsoft Entra Suite | Identity and access management |
| Microsoft 365 E5 | Advanced Defender, Intune, Purview |

- **Pricing**: $99 per user per month (retail)
- **Available**: May 1, 2026

### Agents in Core Apps
- **Word Agent**: Drafts and refines documents iteratively
- **Excel Agent**: Creates spreadsheets with real formulas
- **PowerPoint Agent**: Understands layouts, object styles, brand kits
- **Outlook Agent**: Drafts and refines emails in-app
- **Copilot Chat**: Supports MCP Apps ecosystem (Adobe, Monday.com, Figma)

## Strategic Significance

### Microsoft + Anthropic Partnership
- Microsoft spending ~$500M annually on Anthropic models
- Claude available directly in Copilot Chat alongside OpenAI models
- Marks end of Microsoft-OpenAI "exclusive" era
- Anthropic demonstrated agentic capability; Microsoft commercialized it at scale

> "What Anthropic has done is demonstrate the value of these agentic capabilities. Microsoft is all about commercialization." — Jared Spataro

### EU Restrictions
Anthropic models disabled by default in EU/UK/EFTA tenants due to regulatory compliance (data residency, EU AI Act). Administrators must explicitly enable them — limiting Wave 3 capabilities for European organizations initially.

## Market Context
- IDC projects **1.3 billion AI agents** by 2028
- Wave 3 positions Microsoft 365 as agentic operating system, not just productivity suite
- Competes with Google Workspace (Gemini 3.1) and standalone agents (Claude Cowork, ChatGPT)

## Related Pages
- [[entities/anthropic]] — Technology partner for Copilot Cowork
- [[entities/claude-code]] — Anthropic's standalone coding agent
- [[concepts/claude-managed-agents]] — Anthropic's enterprise agent deployment
- [[entities/xai]] / [[entities/grok-4-3]] — Competing enterprise AI
- [[concepts/grok-computer]] — xAI's desktop automation agent
- [[concepts/ai-agents]] — Broader AI agents landscape
