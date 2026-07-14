---
title: Merge.dev (Merge Agent Handler)
type: entity
created: 2026-05-24
updated: 2026-07-14
tags:
  - entity
  - company
  - mcp
  - developer-tooling
  - ai-agents
sources:
  - https://www.merge.dev/blog/github-mcp-cursor
  - https://www.merge.dev/blog/trello-mcp-cursor
  - raw/articles/merge.dev--blog-github-mcp-cursor--805854f6.md
  - raw/articles/merge.dev--blog-trello-mcp-cursor--46131e27.md
  - raw/articles/merge.dev--blog-mcp-governance-platform--5437a765.md
  - raw/articles/merge.dev--blog-ai-agent-governance--4bf04b32.md
  - raw/articles/merge.dev--blog-gpt-5-6-terra-vs-claude-sonnet-5--9c5002f0.md
---

# Merge.dev (Merge Agent Handler)

> **Merge Agent Handler** is Merge.dev's MCP (Model Context Protocol) server product that connects AI coding agents (Cursor, Claude Code) to third-party SaaS APIs through a centralized OAuth management layer. Provides enterprise-grade access control, audit logging, and token lifecycle management for agent-to-API interactions.

| | |
|---|---|
| **Website** | [merge.dev](https://www.merge.dev) |
| **Product** | Merge Agent Handler |
| **CLI** | `merge-api` (pipx install) |
| **Focus** | MCP servers for SaaS APIs + enterprise governance |

## Overview

Merge Agent Handler bridges AI coding agents and third-party APIs by providing managed MCP servers with centralized authentication. Instead of developers managing personal access tokens and configuring auth state per-project, Merge handles OAuth credentials, token rotation, and access control centrally.

## Core Products

### GitHub MCP Server

Connects Cursor (and other MCP clients) to the GitHub API. Enables agents to:

- **PR inspection**: Fetch real PR diff structures, file changes, hunk data, review threads
- **Issue data**: Retrieve issue schemas including labels, milestones, assignees, timeline events
- **Repository permissions**: Query collaborator lists with role/permission fields
- **Commit metadata**: Pull commit records with author identity, message body, associated PRs
- **Workflow runs**: Fetch CI pipeline results with job-level step outcomes and log URLs
- **Labels & milestones**: Query full label sets and open milestones with IDs

**Setup (4 steps)**: `pipx install merge-api` → `merge login` → `merge connect-cursor` from project root → first tool invocation triggers Magic Link OAuth.

**Why Merge vs self-hosted**: Self-hosted GitHub MCP servers use personal access tokens that carry full account access with no per-agent controls. Merge provides scoped access (e.g., read-only PR monitoring without write/delete), audit logging with timestamps/tool names/inputs, and centralized token rotation.

### Trello MCP Server

Connects Cursor to Trello boards. Enables agents to:

- **Card schemas**: Fetch real card objects with field names, nested member objects, due date formats
- **List IDs**: Query board list structures for card creation targeting
- **Label definitions**: Retrieve full label sets with IDs and color values
- **Member permissions**: Query board member records with role/permission fields
- **Checklist items**: Fetch cards with nested checklist item structures and completion states
- **Webhook events**: Pull real board activity to understand event field structures

## Architecture

Merge Agent Handler uses a CLI-based MCP pattern:

1. `merge-api` CLI installed via pipx
2. `merge login` authenticates against Merge account (central OAuth)
3. `merge connect-cursor` writes a `## Merge CLI` section to `.cursorrules`
4. Cursor's agent calls `merge search-tools` and `merge execute-tool` to reach third-party APIs
5. Merge handles OAuth token storage/refresh — no personal access tokens stored locally

## Enterprise Features

- **Scoped access control**: Per-agent tool permissions (e.g., PR read but never merge/delete)
- **Audit logging**: Every call logged with timestamp, tool name, inputs
- **Multi-user OAuth**: Handles Trello multi-workspace OAuth across users
- **Centralized token rotation**: No per-project auth state management

## Refs (July 2026)

- **MCP Governance Platform Comparison** — Merge's analysis of the MCP governance platform category (AHFE vs Runlayer vs MintMCP). Covers evaluation criteria: SCIM-based provisioning, auditability, comprehensive connector coverage. While Merge's entity page documents its specific MCP products (GitHub MCP, Trello MCP), this post contextualizes them within the broader governance platform landscape.
- **AI Agent Governance Framework** — Overview of AI agent governance concepts: authentication enforcement, tool testing, audit trails, RBAC, rule violation alerts, data leak prevention. Provides the conceptual framework for Merge's specific governance features, complementing the product-focused sections above.
- **Claude Sonnet 5 vs GPT-5.6 Terra Benchmark** — Merge's build-test comparison between Claude Sonnet 5 and GPT-5.6 Terra on coding tasks: Sonnet 5 (136.6s, 17,870 tokens, $0.179) vs GPT-5.6 Terra (60.2s, 10,677 tokens, $0.120 — ~33% cheaper). Quality comparable. Recommendation: Sonnet 5 for agentic/quality-focused work, Terra for speed/cost-sensitive tasks. Comparison primarily serves Merge's product positioning but provides useful real-world benchmark data.

## Related

- [[concepts/model-context-protocol-mcp]] — MCP protocol standard
- [[entities/codex]] — Codex MCP dual support
- [[entities/claude-code]] — Claude Code MCP integration
- [[entities/cursor]] — Cursor IDE

## References

- merge.dev--blog-github-mcp-cursor--805854f6
- merge.dev--blog-trello-mcp-cursor--46131e27
- merge.dev--blog-mcp-governance-platform--5437a765
- merge.dev--blog-ai-agent-governance--4bf04b32
- merge.dev--blog-gpt-5-6-terra-vs-claude-sonnet-5--9c5002f0
