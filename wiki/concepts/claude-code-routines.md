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


## Opus 4.7 Integration (April 2026)

Claude Opus 4.7's improvements directly enhance routines effectiveness:
- **Long-running task handling**: Opus 4.7's ability to work coherently for hours enables multi-hour scheduled routines without degradation
- **Self-verification**: Routines can now verify their own outputs before reporting results, improving reliability of automated tasks
- **xhigh effort level**: The new `xhigh` setting (between `high` and `max`) provides better reasoning/latency tradeoffs for routine execution
- **API Task Budgets**: Guide token spend across longer routine runs, enabling cost management for scheduled automation

## Claude Design Handoff

Claude Design (April 2026) creates a pipeline integration: designs can be handed off to Claude Code with a single instruction. This enables workflows where:
1. A designer creates a prototype in Claude Design
2. The handoff bundle is automatically processed by Claude Code
3. Implementation begins without manual intervention

This represents a new class of "design-to-code" routines where the design review loop is replaced by AI-mediated handoff.

## Related

- [[concepts/claude-code-best-practices]] — Claude Code best practices and patterns
- [[concepts/openai-codex-superapp]] — OpenAI's competing platform
- [[concepts/harness-engineering]] — Agent execution environment design
- [[anthropic]] — Anthropic company context

## Sources

- [Anthropic: Introducing routines in Claude Code](https://substack.com/redirect/36a5d462-fad9-43b3-afff-c1d7c95077fe) (2026-04-19)

## See Also

- [[concepts/_index]]
