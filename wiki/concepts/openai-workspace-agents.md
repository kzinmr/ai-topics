---
title: "OpenAI Workspace Agents"
type: concept
created: 2026-04-27
updated: 2026-04-29
tags: [product, platform, openai, ai-agents, enterprise, workspace, codex]
aliases: ["Workspace Agents", "OpenAI Business Agents"]
sources:
  - raw/articles/openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md
  - raw/articles/simonwillison.net--2026-apr-25-romain-huet--fea00393.md
---

# OpenAI Workspace Agents

## Overview

**OpenAI Workspace Agents** are Codex-powered shared AI agents designed for OpenAI's Business and Enterprise plans. Launched in April 2026 alongside GPT-5.5 and ChatGPT Images 2.0, they represent OpenAI's strategic entry into the enterprise agent platform space.

## Architecture

### Agent Runtime
- Powered by **OpenAI Codex** — the same underlying execution engine as the Codex CLI agent
- As of GPT-5.4+, Codex and the main model are unified into a single system — there is no separate coding model line anymore
- GPT-5.5 delivers "strong gains in agentic coding, computer use, and any task on a computer"
- Shared agents accessible across an organization

### Integrations
Workspace Agents integrate directly with common enterprise SaaS tools:
- **Slack** — communicate and receive tasks via channels
- **Salesforce** — CRM data access and automation
- **Notion** — documentation and knowledge base operations
- **Google Drive** — file access and document processing

### Key Features

| Feature | Description |
|---------|-------------|
| **Persistent Memory** | Agents retain context and learn across sessions |
| **Role-Based Governance** | Admin-defined permissions control what agents can access and do |
| **Shared Deployment** | Agents are available to all authorized team members |
| **Business/Enterprise Only** | Exclusive to paid organization plans |
| **Terminal-Bench 2.0: 82.7%** | GPT-5.5 capability metric — first fully retrained base model since GPT-4.5 |

## Related Launches (April 2026)

OpenAI launched four products in one week, indicating a coordinated push:
1. **GPT-5.5** — first fully retrained base model since GPT-4.5, designed for multi-step work (planning, tool use, self-checking)
2. **Workspace Agents** — enterprise shared agents (this page)
3. **ChatGPT Images 2.0** — hit #1 on all Image Arena leaderboards; beat Google's Nano Banana models by +242 points
4. **ChatGPT for Clinicians** — free tool for verified US medical professionals with HIPAA options

## Competitive Positioning

OpenAI Workspace Agents directly compete with:
- **[[concepts/anthropic-managed-agents]]** — Anthropic's Claude Managed Agents with similar enterprise focus but different memory architecture (filesystem-based text files vs. OpenAI's approach)
- **Cognition Devin** — autonomous AI software engineer

## Related Pages

- [[entities/openai]] — OpenAI entity page
- [[concepts/gpt-5.5]] — Announced alongside Workspace Agents
- [[concepts/chatgpt-images-2.0]] — Announced alongside Workspace Agents
- [[concepts/anthropic-managed-agents]] — Direct competitor
- [[concepts/agent-team-swarm]] — Multi-agent coordination patterns
