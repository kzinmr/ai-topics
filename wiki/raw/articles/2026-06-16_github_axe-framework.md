---
title: "Axe — Lightweight CLI for Running Single-Purpose AI Agents"
date: 2026-06-16
source_url: "https://github.com/jrswab/axe"
tags:
  - ai-agents
  - cli
  - developer-tools
  - framework
  - golang
---

# Axe Framework

## What It Is
Axe is a lightweight CLI tool for managing and running LLM-powered agents. Written in Go (99.9% of the codebase), it treats AI agents the way Unix treats programs — each agent does one thing well, defined in a TOML file, and triggered from the command line, pipes, git hooks, cron, or CI pipelines.

## Who Made It
Created by **jrswab** (GitHub). Licensed under Apache-2.0.

## Key Technical Details
- **Multi-provider support**: Anthropic, OpenAI, Ollama (local models), OpenCode, and AWS Bedrock
- **TOML-based agent configuration**: Declarative, version-controllable agent definitions with system prompts, model selection, skill files, context files, working directories, and persistent memory
- **Sub-agent delegation**: Agents can call other agents via LLM tool use with depth limiting (hard max: 5) and parallel execution
- **Persistent memory**: Timestamped markdown logs that carry context across runs, with LLM-assisted garbage collection and pattern analysis
- **Skill system**: Reusable instruction sets following the community SKILL.md format
- **Stdin piping**: Pipe any output directly into an agent (`git diff | axe run reviewer`)
- **Local agent directories**: Auto-discovers agents from `<cwd>/axe/agents/` before the global config
- **Built-in tools**: File operations (read, write, edit, list) sandboxed to working directory, shell command execution, URL fetching, web search
- **Output allowlist**: Restricts `url_fetch` and `web_search` to specific hostnames; private/reserved IPs always blocked (SSRF protection)
- **Token budgets**: Cap cumulative token usage per agent run
- **MCP tool support**: Connect to external MCP servers for additional tools via SSE or streamable-HTTP transport
- **Configurable retry**: Exponential, linear, or fixed backoff for transient provider errors (429, 5xx, timeouts)
- **Docker support**: Containerized execution with non-root user, read-only root filesystem, all capabilities dropped
- **Go 1.25+ required**: Pre-built binaries available for Linux, macOS, and Windows

## Stats (as of June 2026)
- 820 GitHub stars
- 25 forks
- 15 releases (latest: v1.10.0, May 5, 2026)
- 4 direct dependencies (cobra, toml, mcp-go-sdk, x/net)

## CLI Commands
| Command | Description |
|---|---|
| `axe run <agent>` | Run an agent |
| `axe agents list` | List all configured agents |
| `axe agents show <agent>` | Display agent configuration |
| `axe agents init <agent>` | Scaffold a new agent |
| `axe agents edit <agent>` | Edit an agent TOML |
| `axe config path` | Print config directory path |
| `axe config init` | Initialize config with defaults |
| `axe gc <agent>` | Run memory garbage collection |
| `axe gc --all` | Run GC on all agents |
| `axe version` | Print version |

## Exit Codes
- 0: Success
- 1: Runtime error
- 2: Configuration error
- 3: Provider/network error
- 4: Token budget exceeded

## Why It Matters
Axe represents a philosophical shift in AI tooling. Instead of monolithic chatbot interfaces with massive context windows, Axe embraces the Unix philosophy: small, focused, composable agents. This approach is better aligned with how good software actually works. The tool's emphasis on security (SSRF protection, path sandboxing, Docker hardening), cost control (token budgets, context caching), and integration with existing developer workflows (cron, git hooks, pipes) makes it a practical choice for production AI agent deployment. The sub-agent delegation with depth limiting and parallel execution enables complex multi-step workflows while maintaining control and observability.

## Source Information
- Repository: https://github.com/jrswab/axe
- Documentation: https://docs.getaxe.dev
- License: Apache-2.0
