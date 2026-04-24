---
title: Claude Code Routines
type: concept
created: 2026-04-24
updated: 2026-04-24
tags: [concept, claude-code, automation, agentic-engineering]
aliases: [claude-code-scheduling, claude-code-automation]
sources: []
---

# Claude Code Routines

**Claude Code Routines** are scheduled and event-driven automation configurations introduced by Anthropic in April 2026. They allow users to configure Claude Code once — including a prompt, repository, and connectors — and then run it on a schedule, from an API call, or in response to an event.

## Overview

Routines run on Claude Code's web interface and provide a persistent, repeatable agent execution model. Unlike ad-hoc Claude Code sessions, routines are designed for recurring tasks.

## Key Features

- **Prompt configuration**: Define the prompt/behavior once for consistent results
- **Repository binding**: Tied to specific code repositories for context-aware execution
- **Connector integrations**: Can connect to external systems (GitHub, Slack, etc.)
- **Multiple triggers**: Schedule-based, API-based, or event-based execution
- **Research preview**: Available in research preview as of April 19, 2026

## Use Cases

- Automated code reviews on a schedule
- CI/CD pipeline integration with agent-assisted decisions
- Periodic dependency vulnerability scanning
- Regular documentation updates
- Scheduled refactoring tasks

## Platform Context

Claude Code Routines represent Anthropic's move toward persistent, scheduled agent execution — paralleling OpenAI's Symphony managed agents and the broader agentic automation trend. This positions Claude Code as not just a development tool but as an operational platform for recurring agent tasks.

## Comparison with Alternatives

| Feature | Claude Code Routines | OpenAI Symphony | OpenClaw |
|---------|---------------------|-----------------|----------|
| Trigger types | Schedule, API, Event | Managed agent calls | Cron + event |
| Interface | Claude Code web | API + dashboard | CLI + web |
| Persistence | Full session state | Session management | Config-driven |
| Connector model | Built-in | API integrations | MCP-based |

## Related

- [[concepts/claude-code-best-practices]] — Claude Code best practices and patterns
- [[concepts/openai-codex-superapp]] — OpenAI's competing platform
- [[concepts/harness-engineering]] — Agent execution environment design
- [[entities/anthropic]] — Anthropic company context

## Sources

- [Anthropic: Introducing routines in Claude Code](https://substack.com/redirect/36a5d462-fad9-43b3-afff-c1d7c95077fe) (2026-04-19)

## See Also

- [[concepts/_index.md]]
