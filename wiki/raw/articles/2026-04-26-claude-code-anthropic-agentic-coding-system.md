# Claude Code: Anthropic's Agentic Coding System

> Source: Multiple sources compiled from Claude Code documentation and analysis
> - Anthropic: https://www.anthropic.com/product/claude-code
> - Claude Code Docs: https://code.claude.com/docs/en/overview
> - AI Wiki: https://aiwiki.ai/wiki/claude_code
> - Newsletter: "Dive into Claude Code" (True Positive Weekly, Apr 26, 2026, paywalled)

## Overview

Claude Code is Anthropic's agentic coding system — an AI coding agent that reads codebases, edits files, runs commands, and integrates with development tools. It is available in the terminal, IDE, desktop app, and browser.

As of 2026, the majority of code at Anthropic is now written by Claude Code. Engineers focus on architecture, product thinking, and continuous orchestration.

## Core Capabilities

### Terminal-Based Agent
- Reads your codebase, edits files, runs shell commands
- Works in any terminal environment
- Follows Unix philosophy: composable, pipe-able, chainable with other tools

### IDE Integration
- Native VS Code extension (beta since September 2025)
- Direct IDE integration with auto-detection of workspace environment
- Line-of-code operations and continuous session persistence
- Eliminates need to switch between terminal and editor

### Agent Teams
- Spawn multiple Claude Code agents working on different parts of a task simultaneously
- Lead agent coordinates work, assigns subtasks, merges results
- For fully custom workflows, the [Agent SDK](/en/agent-sdk/overview) lets you build custom agents

### Computer Use (March 2026)
- Claude can use the developer's computer directly
- Point, click, type, navigate applications autonomously
- Remote Mac desktop control and mobile terminal access
- Available alongside Claude Cowork

### Scheduled Tasks (/loop)
- Turn Claude Code into a background worker with Cron-like scheduling
- Practical uses: PR reviews, deployment monitoring
- Most practical new feature as of March 2026

### Skills, Subagents, Hooks, MCP, Plugins
- Form a complete Agent development platform
- Skills: reusable capability bundles
- Hooks: lifecycle event handlers
- MCP: Model Context Protocol for tool integration
- Plugins: extensible architecture

## Architecture Comparison: Claude Code vs OpenAI Codex

| Dimension | Claude Code (Anthropic) | OpenAI Codex |
|-----------|------------------------|--------------|
| Execution environment | Developer's own harness | Managed containers provided by OpenAI |
| Skills | SKILL.md bundles (via API) | Tool definitions (JSON schema) |
| Context | Developer-implemented compaction | Native compaction |
| Security | Developer responsibility | Sidecar egress proxy |
| Platform model | Developer builds harness | OpenAI provides full platform |

## Platform Philosophy

- **Anthropic**: Developer-centric. Provides the LLM and agent framework; developers build their own execution environment (harness).
- **OpenAI**: Platform-centric. Provides managed containers, built-in skills, security layers.

This creates fundamentally different developer experiences and ecosystems.

## Evolution Trajectory

Claude Code is evolving from "better code completion" into a full **autonomous coding agent platform**. The 2026 trajectory shows:
1. Terminal agent → IDE integration
2. Single agent → Agent teams (sub-agents)
3. Code editing → Computer Use (full desktop control)
4. Task-specific → Scheduled/background operation (/loop)
5. Tool → Platform (Skills, Hooks, MCP, Plugins)

## Key Dates

- **September 2025**: VS Code extension launched (beta)
- **March 2026**: Computer Use capability announced (March 23)
- **2026**: Majority of Anthropic code written by Claude Code
