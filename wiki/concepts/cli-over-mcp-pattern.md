---
title: "CLI Over MCP Pattern"
created: 2026-04-13
updated: 2026-04-13
tags: [cli, mcp, tool-design, context-efficiency, agentic-engineering]
aliases: ["cli-first-development", "mcp-skepticism", "tool-agnostic-agents", "minimal-tooling-pattern"]
related: [[direct-prompting-philosophy]], [[claude-code-best-practices]], [[context-window-management]], [[agentic-engineering]]
sources:
  - url: "https://steipete.me/posts/2025/optimal-ai-development-workflow/"
    author: "Peter Steinberger (@steipete)"
    date: "2025-08-25"
    title: "My Current AI Dev Workflow"
  - url: "https://steipete.me/posts/2025/just-talk-to-it"
    author: "Peter Steinberger (@steipete)"
    date: "2025-10"
    title: "Just Talk To It - the no-bs Way of Agentic Engineering"
---

# CLI Over MCP Pattern

**CLI Over MCP** is a design principle for AI-assisted development workflows that prioritizes standard Command Line Interface (CLI) tools over Model Context Protocol (MCP) servers. The pattern argues that CLIs are more efficient, more reliable, and more context-friendly for agent-driven development.

> "Pick services that have CLIs: vercel, psql, gh, axiom. Agents can use them, one line in CLAUDE.md is enough." — Peter Steinberger

---

## Why CLIs Beat MCP Servers

### 1. Context Window Efficiency

| Aspect | MCP Server | CLI Tool |
|--------|-----------|----------|
| **Token cost per call** | High (protocol overhead + tool schema) | Low (just the command + output) |
| **Schema complexity** | Requires JSON schema definition | Pre-existing, well-documented |
| **Context pollution** | Tool definitions persist in every message | Only present when invoked |
| **Error verbosity** | Often verbose and structured | Standardized, concise |

### 2. Model Familiarity

> "I bet that you'd get better result if you ask your agent to 'google AI agent building best practices' and let it load some websites than this crap." — Steipete on custom MCP configurations

Standard CLIs like `gh`, `vercel`, `psql` have:
- **Extensive training data** — models know these tools intimately
- **Predictable behavior** — consistent output formats
- **Rich documentation** — models can reference official docs when needed
- **No setup overhead** — works immediately, no MCP server configuration

### 3. Reliability and Debugging

When an MCP server fails:
- Debug the server process
- Check the protocol layer
- Verify tool schemas
- Handle connection issues

When a CLI fails:
- Read the error message
- Fix the command
- Done

> "CLIs beat MCPs. A 2-hour CLI wrapper (logs, API pulls) pays for itself and keeps context small." — Steipete

---

## The Pattern in Practice

### Before (MCP-heavy):
```
1. Configure MCP server in settings.json
2. Define tool schemas for each operation
3. Handle authentication, rate limiting, error recovery
4. Agent calls MCP tools → protocol overhead → verbose responses
5. Context window fills with tool definitions
```

### After (CLI-first):
```
1. Install CLI tool (e.g., `brew install gh`)
2. Add one line to CLAUDE.md: "Use `gh` for all GitHub operations"
3. Agent uses CLI directly → minimal overhead → clean context
4. Errors are standard CLI output → easy to debug
5. Context stays focused on the task
```

### Example: GitHub Operations

**MCP Approach:** Configure GitHub MCP server, define schemas for PR creation, issue management, etc.

**CLI Approach:** One line in CLAUDE.md:
```
GitHub: use `gh` CLI. Examples: `gh pr create --title "fix: auth" --body "Fixed login"`, `gh issue list`
```

The agent immediately knows how to use `gh` because it was trained on millions of GitHub CLI examples.

---

## When MCPs Make Sense

MCPs are not universally bad — they excel in specific scenarios:

| Use Case | Recommended | Why |
|----------|-------------|-----|
| **Web scraping** | MCP | Browsers need specialized protocols |
| **Database exploration** | MCP | Schema discovery benefits from structured queries |
| **Design-to-code** | MCP | Figma/Sketch integration requires protocol |
| **Standard operations** | CLI | Git, deployments, logs, package management |
| **File operations** | CLI | `ls`, `grep`, `cat`, `sed` are sufficient |
| **API calls** | CLI | `curl` + one-liner config beats MCP setup |

---

## Connection to Direct Prompting Philosophy

The CLI-first pattern complements [[direct-prompting-philosophy]]:

- **Less setup** → more time for direct interaction
- **Fewer abstraction layers** → cleaner mental model
- **Standard tools** → model already knows how to use them
- **Minimal configuration** → one line in CLAUDE.md vs. entire MCP setup

Both patterns share the core principle: **reduce overhead, increase direct engagement**.

---

## Anti-Patterns to Avoid

### 1. The MCP Graveyard
**Problem**: Installing dozens of MCP servers "just in case."
**Result**: Context pollution, confusion about which tool to use, debugging nightmares.
**Fix**: Start with zero MCPs. Add only when a CLI genuinely can't do the job.

### 2. The Custom Tool Trap
**Problem**: Building bespoke MCP tools for operations that existing CLIs handle.
**Result**: Wasted development time, maintenance burden, model unfamiliarity.
**Fix**: Check if `gh`, `vercel`, `aws`, `kubectl` etc. already do it.

### 3. The Protocol Purist
**Problem**: Insisting on MCP for everything because "it's the future."
**Result**: Ignoring the practical reality that CLIs work better today.
**Fix**: Be pragmatic. Use what works, not what's trendy.

---

## Related Concepts

- [[direct-prompting-philosophy]] — The anti-overengineering mindset this serves
- [[claude-code-best-practices]] — Practical implementation patterns
- [[context-window-management]] — How CLIs preserve precious context
- [[agentic-engineering]] — The broader methodology

## Sources

- [Peter Steinberger: My Current AI Dev Workflow](https://steipete.me/posts/2025/optimal-ai-development-workflow/) — CLI-first practices
- [Peter Steinberger: Just Talk To It](https://steipete.me/posts/2025/just-talk-to-it) — MCP skepticism, CLI preference
- [Manuel Odendahl: MCPs are Boring](https://steipete.me/posts/2025/essential-reading-july-2025) — Recursive code generation vs. rigid tool schemas
