---
title: "Axe — Lightweight AI Agent CLI Framework"
created: 2026-06-16
updated: 2026-06-16
type: concept
tags:
  - ai-agents
  - developer-tooling
  - framework
  - go
  - architecture
  - agent-tooling
  - coding-agents
  - security
  - open-source
  - philosophy
sources:
  - https://github.com/jrswab/axe
  - https://docs.getaxe.dev
---

# Axe — Lightweight AI Agent CLI Framework

**Axe** is a lightweight CLI tool for managing and running LLM-powered agents, written in Go (99.9% of the codebase). It treats AI agents the way Unix treats programs — each agent does one thing well, defined in a TOML file, and triggered from the command line, pipes, git hooks, cron, or CI pipelines.

Created by **jrswab** and licensed under Apache-2.0. As of June 2026: **820 GitHub stars**, 25 forks, 15 releases (latest v1.10.0).

## What It Is

Axe inverts the dominant coding-agent paradigm. Instead of monolithic chatbot interfaces with massive context windows (Claude Code, Codex, Cursor), Axe provides a minimal CLI shell around focused, single-purpose agents. Each agent is a declarative TOML configuration — system prompt, model selection, skill files, context files, working directory, and persistent memory — that can be invoked with a single command.

This maps directly to the [[concepts/unix-philosophy|Unix philosophy]] applied to AI: *"Write programs that do one thing and do it well. Write programs to work together."* Axe agents are designed to be piped, chained, and composed — the AI equivalent of `grep | sort | uniq`.

## Key Technical Features

### Multi-Provider Support
Axe connects to Anthropic, OpenAI, Ollama (local models), OpenCode, and AWS Bedrock. The provider is a configuration choice, not a framework lock-in.

### TOML-Based Agent Configuration
Declarative, version-controllable agent definitions. Each agent specifies:
- System prompt and model selection
- Skill files (following the [[concepts/agent-skills|SKILL.md]] open standard)
- Context files for domain-specific knowledge
- Working directory and persistent memory path

### Sub-Agent Delegation
Agents can call other agents via LLM tool use with:
- **Depth limiting** — hard maximum of 5 levels to prevent infinite recursion
- **Parallel execution** — fan-out patterns for independent subtasks
- **Depth-aware context management** — each delegation level gets its own context window

This implements the [[concepts/subagent-patterns|Inline Tool pattern]] (Philipp Schmid's Pattern 1) with the safety rails of depth limiting. The parallel execution capability also supports the [[concepts/subagent-patterns|Fan-Out pattern]].

### Persistent Memory
- Timestamped markdown logs that carry context across runs
- LLM-assisted garbage collection to manage memory growth
- Pattern analysis across runs for continuous improvement

### Built-In Tools
| Tool | Description |
|------|-------------|
| File operations | Read, write, edit, list — sandboxed to working directory |
| Shell commands | Execute arbitrary commands within sandbox |
| URL fetching | Retrieve web content with SSRF protection |
| Web search | Search the internet with output allowlisting |
| MCP integration | Connect to external MCP servers via SSE or streamable-HTTP |

### Security
- **SSRF protection**: `url_fetch` and `web_search` restricted to specific hostnames; private/reserved IPs always blocked
- **Path sandboxing**: File operations confined to working directory
- **Docker hardening**: Containerized execution with non-root user, read-only root filesystem, all capabilities dropped
- **Output allowlist**: Restricts network-facing tools to whitelisted hosts

### Cost Control
- **Token budgets**: Cap cumulative token usage per agent run
- **Context caching**: Reuse cached context across runs where possible
- **Exponential exit codes**: 0 (success), 1 (runtime error), 2 (config error), 3 (provider/network error), 4 (token budget exceeded) — enabling automated handling in CI pipelines

### Retry Logic
Configurable retry with exponential, linear, or fixed backoff for transient provider errors (429, 5xx, timeouts).

## CLI Interface

| Command | Description |
|---------|-------------|
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

Stdin piping is first-class: `git diff | axe run reviewer` pipes any output directly into an agent.

## Comparison to Other Coding Agents

Axe occupies the opposite end of the spectrum from tools like [[entities/claude-code|Claude Code]] and [[entities/codex|Codex]]:

| Dimension | Claude Code / Codex | Axe |
|-----------|---------------------|-----|
| **Interface** | Interactive IDE/terminal chat | CLI commands, pipes, hooks |
| **Scope** | General-purpose coding assistant | Single-purpose, focused agents |
| **Architecture** | Monolithic, all-in-one | Composable, Unix-style |
| **Configuration** | Prompts + system instructions in UI | Declarative TOML files |
| **Execution** | Long-running interactive session | Short-lived, pipeable invocations |
| **Cost model** | Open-ended token consumption | Hard token budgets per run |
| **Philosophy** | "One agent to rule them all" | "Do one thing well" |

This contrast exemplifies the [[concepts/harness-engineering|harness engineering]] debate: Claude Code and Codex invest heavily in the harness (context management, feedback loops, error recovery) while Axe invests in agent composition and isolation. Axe's approach aligns more closely with minimal coding agent philosophy — small, auditable, purpose-built units.

## Why It Matters: Unix Philosophy Applied to AI Agents

Axe represents a philosophical counter-movement in the AI tooling landscape. While the industry trend is toward **larger context windows, more capable models, and richer interactive interfaces**, Axe argues that the right architecture is smaller, composable agents glued together by the developer's existing toolchain.

Key philosophical positions:

1. **Composition over integration** — Agents are connected through stdin/stdout and file operations, not through proprietary APIs or cloud infrastructure
2. **Declarative over imperative** — TOML configs are version-controllable, reviewable, and diffable. Agent behavior is encoded in files, not hidden behind UI layers
3. **Local-first over cloud** — Agents run on the developer's machine with local model support (Ollama), no cloud dependency required
4. **Budget-enforced over open-ended** — Token budgets, depth limits, and explicit exit codes prevent runaway costs and infinite loops
5. **Security-by-default over trust-by-default** — SSRF protection, path sandboxing, and Docker hardening are built in, not bolted on

This philosophy resonates with the broader [[concepts/harness-engineering|harness engineering]] principle that *the harness is where the real engineering happens* — Axe makes the harness explicit, auditable, and composable rather than embedded in a monolithic product.

## Architecture and Ecosystem Fit

Axe's design places it at the intersection of several wiki concepts:

- It implements [[concepts/agent-harness-primitives|agent harness primitives]] — filesystem abstraction, code execution, tool/skill system, orchestration logic — but as a minimal, CLI-first framework rather than a full platform
- Its skill system follows the [[concepts/agent-skills|SKILL.md]] open standard, making skills portable across Axe, Claude Code, and Codex
- Its sub-agent delegation with depth limiting is a concrete implementation of the patterns described in [[concepts/subagent-patterns|Subagent Patterns]]
- Its local-first, pipeable design makes it suitable for integration into [[concepts/coding-agents|coding agent]] workflows via git hooks and CI pipelines

## Stats

| Metric | Value |
|--------|-------|
| GitHub Stars | 820 |
| Forks | 25 |
| Releases | 15 (latest: v1.10.0, May 5, 2026) |
| License | Apache-2.0 |
| Language | Go (99.9% of codebase) |
| Dependencies | 4 (cobra, toml, mcp-go-sdk, x/net) |
| Go Version Required | 1.25+ |
| Platforms | Linux, macOS, Windows (pre-built binaries) |

## Related Concepts

- [[concepts/unix-philosophy]] — The philosophy Axe embodies: small, focused, composable tools
- [[concepts/agent-harness-primitives]] — The building blocks Axe implements as a CLI framework
- [[concepts/subagent-patterns]] — Axe's delegation model implements the Inline Tool and Fan-Out patterns
- [[concepts/agent-skills]] — Axe's skill system uses the SKILL.md open standard
- [[concepts/harness-engineering]] — Axe is a harness-first approach to agent deployment
- [[concepts/coding-agents|Coding Agents]] — The broader category Axe fits within, as a minimal alternative
