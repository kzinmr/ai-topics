---
title: Grok Build
created: 2026-05-27
updated: 2026-05-29
type: entity
tags:
  - entity
  - product
  - xai
  - coding-agents
  - ai-agents
  - developer-tooling
  - agent-sdk
sources: [raw/newsletters/2026-05-28-gbrain.md]
---

# Grok Build

**Grok Build** is [[entities/xai|xAI]]'s terminal-based AI coding agent, released in beta in May 2026. It joins the rapidly expanding field of AI coding agents alongside [[entities/claude-code|Claude Code]], [[entities/cursor-ai|Cursor]], [[entities/github-copilot|GitHub Copilot]], and [[entities/codex-cli|Codex CLI]].

## Overview

Grok Build is a command-line coding agent powered by xAI's Grok models. It operates directly in the terminal, reading and modifying files in the user's codebase to implement features, fix bugs, and assist with development workflows. With 2 million tokens of context, up to 8 parallel subagents, and a unique Plan Mode that reviews all changes before writing, Grok Build joins Claude Code and Codex as one of the three major terminal-based coding agents.

## Key Features

| Feature | Detail |
|---------|--------|
| **Interface** | Terminal-based CLI |
| **Plan Mode** | Shows all planned changes for approval before touching files — a key differentiator from Claude Code and Codex |
| **Context Window** | 2 million tokens |
| **Parallel Subagents** | Up to 8 subagents running in parallel (each on an independent branch) |
| **AGENTS.md Support** | Reads project-level instructions and conventions |
| **MCP Server Discovery** | Auto-detects and connects to MCP servers |
| **Headless Mode** | Runs without user interaction for CI/CD or automated workflows |
| **Access** | Beta for SuperGrok and X Premium Plus subscribers |

## Availability

- **SuperGrok** subscribers
- **X Premium Plus** subscribers
- Beta access as of May 2026

## Competitive Context

Grok Build enters a crowded coding agent market alongside Claude Code, Codex, and Cursor. As of May 2026: [[entities/cursor-ai|Cursor Composer 2.5]], [[entities/claude-code|Claude London]] (Anthropic's self-hosted sandbox with MCP tunneling), and [[entities/qwen-3-7-max|Qwen 3.7 Max]] API for coding. The coding agent space is increasingly shifting from model quality alone to **infrastructure and harness engineering** as the key differentiator.

## Security Note

Grok Build was one of the coding agents identified as vulnerable to the [[events/trustfall-symlink-rce-2026|TrustFall + Symlink RCE]] attack disclosed by Adversa AI in May 2026, affecting all major coding agents that use MCP auto-start. xAI had not responded to the vulnerability disclosure as of reporting.

## Related Pages

- [[entities/xai]] — xAI company
- [[entities/claude-code]] — Anthropic's coding agent
- [[entities/cursor-ai]] — Cursor IDE and agent
- [[entities/github-copilot]] — GitHub Copilot
- [[concepts/coding-agents]] — AI coding agents concept
- [[events/trustfall-symlink-rce-2026]] — shared MCP vulnerability
