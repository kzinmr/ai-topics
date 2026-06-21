---
title: "CLI-First Development"
type: concept
aliases:
  - cli-first-development
  - agent-friendly-cli
  - cli-design-for-agents
created: 2026-04-25
updated: 2026-05-24
tags:
  - concept
  - agentic-engineering
  - developer-tooling
  - agent-ergonomics
sources:
  - raw/articles/2026-05-23_yan5xu_agent-friendly-cli-design.md
  - https://x.com/yan5xu/status/2058151727333880265
related:
  - concepts/agent-ergonomics
  - concepts/agent-first-design
  - concepts/cli-over-mcp-pattern
  - concepts/writing-effective-tools-for-ai-agents
---

# CLI-First Development

**CLI-First Development** is the practice of designing command-line interfaces with **AI coding agents as first-class users**. While "machine-readable CLI" solves programmatic chaining (pipes, structured output), **agent-friendly CLI** additionally addresses semantic comprehension — ensuring the CLI output and command structure are optimized for LLM context windows, where both token budget and semantic clarity are scarce.

The canonical case study is **GitHub CLI (`gh`)**, which [[entities/yan5xu|yan5xu]] analyzed in May 2026 as an exemplar of agent-friendly CLI design.

## Core Thesis

> Agent-friendly CLI ≠ machine-readable CLI. Machine-readable solves program chaining; agent-friendly must also solve **semantic comprehension** in a constrained context window.

Two structural requirements for agent-friendly CLI:
1. **Stable, composable structure** — resource paths, unified verbs, `--json`, `--jq`
2. **LLM-optimized semantics** — natural language defaults, clear error messages, minimal token noise

## Two Key Problems (and gh's Solutions)

### Problem 1: Command Explosion

When a platform's capability surface is large (e.g., GitHub: issues, PRs, repos, projects, deployments, actions, packages...), mapping each capability to a CLI command leads to an unmaintainable `--help` and forces agents to guess whether an operation has a dedicated command.

**gh's solution: Resource layer via `gh api`**

```
gh api repos/cli/cli/pulls/13492 --jq '{number: .number, title: .title, state: .state}'
```

The RESTful API's resource model is **directly mapped to the CLI**: paths locate resources, HTTP methods express actions, auth and output formatting are handled uniformly. This means API documentation itself becomes CLI documentation — agents don't need to learn a DSL.

### Problem 2: Output Pollution

In agent workflows, extraneous fields entering the LLM context waste tokens AND pollute the semantic space, degrading subsequent reasoning.

**gh's solution: `--json` / `--jq` for pre-context trimming**

```bash
# Instead of verbose human-readable output:
gh pr list -R cli/cli --limit 1 --json title --jq '.[0].title'
# → "Replace SITE_DEPLOY_PAT with gh-cli-site-deployer App"
```

The critical insight: **trimming happens before entering the LLM context**. It's not just about saving a pipe — it's about preventing irrelevant fields from interfering with reasoning.

## Architecture: Resource Layer + Command Layer

| Layer | Syntax | Purpose | Examples |
|-------|--------|---------|----------|
| **Command** | No `/` prefix | Actions that cannot be naturally resource-ified | `login`, `clone`, `checkout`, `merge`, `status` |
| **Resource** | `/` prefix | CRUD operations on resources | `/issues/42 get`, `/issues/42 update state=closed`, `/projects/4/items list` |

### Why the `/` prefix matters
- `/issues` is unambiguously a resource path (vs. ambiguous `issues` — command or resource?)
- Doesn't consume a reserved word (`api`, `resource`)
- Verbs converge to a minimal set: `list`, `get`, `create`, `update`, `delete`
- Agent learns one resource → learns all resources

### Why command layer still exists
REST has always struggled with intentions that don't map cleanly to CRUD on a single resource:
- `merge` — involves multiple underlying actions; user intent is "integrate this change," not "modify field X, then delete branch Y"
- `clone` — spans remote repo + local filesystem + git state
- `checkout` — switches local workspace state, not an API operation

The command layer handles **high-level intent**; the resource layer handles **long-tail coverage**. They are complementary, not alternatives.

## Output Design: Semantic Default, Structured on Demand

### Principle

| Mode | Format | When to Use |
|------|--------|-------------|
| **Default** | Semantic (natural language) | Agent reads and comprehends |
| **Structured** | JSON + `--jq` | Agent chains commands, needs precise extraction |

### Example

```bash
# Default — semantic, LLM-friendly:
cli /issues/42 get
# Issue #42: Fix login bug
# State:   open
# Author:  epiral
# Labels:  bug, auth
# Updated: 2h ago
# Login fails when session expires.

# Structured — for chaining:
cli /issues list state=open --json --jq '.[].title'
# Fix login bug
# Add rate limiting
```

JSON is for **chaining and precise extraction**, not the default cognitive interface. Natural language is the representation LLMs process best.

## Execution-Level Design

### Consistent Flags
`--repo`, `--assignee`, `--label`, `--json`, `--jq`, `--web` are reused across commands. For humans: lower learning curve. For agents: **better generalization** — learned flag behavior transfers across commands.

### `--web` as Natural Fallback
```bash
gh pr view --web
```
The CLI doesn't pretend to cover all interactions. Some things are better in a browser. Honest fallbacks prevent agents from getting stuck.

### Non-Interactive Mode (Agent Infrastructure)
```bash
GH_PROMPT_DISABLED=1 gh pr create --title "fix bug" --body "..."
```
- `--yes` skips confirmation prompts
- `--dry-run` enables preview without side effects
- Environment variables for auth tokens
- These are the **infrastructure that makes agents stable CLI users**

## Design Checklist for Agent-Friendly CLI

| Requirement | Why |
|-------------|-----|
| Resource path syntax (`/resource/id verb`) | Avoids command explosion; API docs become CLI docs |
| Unified verb set (`list/get/create/update/delete`) | Generalization — learn one, learn all |
| `--json` + `--jq` output filtering | Trim before LLM context; prevent semantic pollution |
| Semantic default output | Natural language is LLMs' best representation |
| Consistent cross-command flags | Flag behavior transfers; agents generalize |
| `--yes` / `--dry-run` / env var auth | Non-interactive agent stability |
| `--web` fallback | Honest about CLI limitations; prevents agent dead-ends |

## See Also

- [[concepts/harness-engineering/agent-ergonomics]] — Language and toolchain design for AI agents (Wes McKinney)
- [[concepts/agent-first-design]] — Programming language design for agents (Armin Ronacher)
- [[concepts/cli-over-mcp-pattern]] — CLI as an alternative to MCP for agent-tool interfaces
- [[concepts/writing-effective-tools-for-ai-agents]] — General tool design principles for agents
- [[entities/yan5xu]] — Author of the gh CLI analysis (ex-Manus AI, ex-Monica)

## References

- yan5xu, "How to design agent-friendly CLI from GitHub CLI" (May 23, 2026) — [X Article](https://x.com/yan5xu/status/2058151727333880265)
