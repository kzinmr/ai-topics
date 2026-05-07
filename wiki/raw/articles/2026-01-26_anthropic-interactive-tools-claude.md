---
title: "Interactive Connectors and MCP Apps in Claude"
source: Anthropic Claude Blog (claude.com)
author: Anthropic
url: https://claude.com/blog/interactive-tools-in-claude
published: 2026-01-26
type: article
tags: [anthropic, claude, mcp, mcp-apps, interactive-connectors, product-announcement]
---

# Interactive Connectors and MCP Apps in Claude

**Published:** January 26, 2026
**Category:** Product Announcements
**Availability:** Free, Pro, Max, Team, and Enterprise plans (Web, Mobile, Desktop, and Claude Cowork).

## Overview

Anthropic introduced **interactive connectors** powered by **MCP Apps**. This update allows Claude to not only access data from third-party tools but to display them as interactive interfaces within the chat. Users can now view, edit, and manage workflows across various platforms without leaving the Claude interface.

> "Claude already connects to your tools and takes actions on your behalf. Now, with MCP Apps, those tools show up as interactive connectors right in the conversation, so you can see what's happening and collaborate in real time."

## Supported Interactive Connectors

The following apps now feature rich, interactive UI within Claude:

- **Amplitude:** Build analytics charts; interactively adjust parameters and explore trends.
- **Asana:** Convert chats into projects, tasks, and timelines.
- **Box:** Search files and preview documents inline; extract insights directly.
- **Canva:** Create presentation outlines and customize branding/design in real-time.
- **Clay:** Research companies/contacts and draft personalized outreach within the conversation.
- **Figma:** Use prompts to generate flow charts, Gantt charts, or diagrams in FigJam.
- **Hex:** Ask data questions to receive interactive charts, tables, and citations.
- **monday.com:** Manage boards, assign tasks, and visualize project progress.
- **Slack (Salesforce):** Search conversations for context, generate drafts, and review/format messages before posting.
- **Salesforce (Coming Soon):** Integration via Agentforce 360 for enterprise-wide reasoning and action.

## Technical Foundation: MCP Apps

The technology driving these connectors is the **Model Context Protocol (MCP)**, extended with the **MCP Apps** specification:

- **MCP Apps** is a new extension to MCP that allows any MCP server to deliver a rich user interface inside supporting AI products.
- MCP remains an open standard — MCP Apps is intended for the entire ecosystem, not just Claude.
- Developers can build their own interactive UIs on top of MCP Apps.
- Detailed documentation is available at [modelcontextprotocol.io](https://modelcontextprotocol.io/docs/getting-started/intro).

## How to Get Started

1. Navigate to [claude.ai/directory](https://claude.ai/directory).
2. Locate the **"Featured"** section.
3. Connect the desired apps to enable interactive capabilities within your chats.

## Related Updates

- **Claude Managed Agents (May 2026):** Introduced "dreaming," outcomes, and multi-agent orchestration.
- **Claude Security (April 2026):** Now in public beta.
- **Memory (Sept 2025):** Added persistent memory capabilities to Claude.
