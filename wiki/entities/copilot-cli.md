---
title: GitHub Copilot CLI
type: entity
aliases: [copilot-cli, gh-copilot-cli, github-copilot-cli]
created: 2026-05-07
updated: 2026-08-10
status: L3
tags:
  - entity
  - coding-agent
  - developer-tooling
  - microsoft
  - ai-agents
sources:
  - https://github.com/github/copilot-cli
  - https://github.com/features/copilot/cli
  - https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli
  - https://github.blog/changelog/2026-04-07-copilot-cli-now-supports-byok-and-local-models/
  - https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli
  - https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference
  - https://raw.githubusercontent.com/github/copilot-cli/main/README.md
  - https://raw.githubusercontent.com/github/copilot-cli/main/changelog.md
  - raw/articles/simonwillison.net--2026-apr-22-changes-to-github-copilot--21b3a503.md
  - raw/articles/wheresyoured.at--news-microsoft-to-shift-github-copilot-users-to-token-based---d4b13c77.md
related:
  - "[[entities/claude-code]]"
  - "[[entities/codex]]"
  - "[[entities/opencode]]"
  - "[[entities/droid]]"
  - "[[concepts/github-copilot-billing]]"
  - "[[concepts/microsoft-copilot-wave-3]]"
  - "[[concepts/agent-harnesses]]"
---

# GitHub Copilot CLI

> **GitHub Copilot CLI** brings Copilot's agentic AI capabilities directly to your terminal — powered by the same harness as GitHub's Copilot coding agent. Features built-in sub-agents (explore, code-review, research, general-purpose), MCP-powered extensibility, BYOK/local model support, and deep GitHub workflow integration. As of August 2026 it is one of the most actively developed coding agent CLIs (v1.0.79, 11K+ GitHub stars, near-daily releases).

## Basic Information

| Field | Details |
|---|---|
| Developer | GitHub (Microsoft) |
| Repository | [github/copilot-cli](https://github.com/github/copilot-cli) |
| Official Site | [github.com/features/copilot/cli](https://github.com/features/copilot/cli) |
| Initial Release | 2025 (replaced retired gh copilot extension) |
| Supported Environments | Terminal (CLI) — Linux, macOS, Windows |
| Pricing | Included in Copilot Free/Pro/Pro+/Business/Enterprise |
| Installation | `curl -fsSL https://gh.io/copilot-install \| bash`, `brew install copilot-cli`, `winget install GitHub.Copilot`, `npm install -g @github/copilot` |
| GitHub Stats (Aug 2026) | 11,076 stars, 1,886 forks, active daily releases |

## Key Features

### Built-in Sub-Agents
Copilot CLI ships with specialized sub-agents, each with default model assignments:

| Agent | Default Model | Description |
|-------|---------------|-------------|
| **explore** | Claude Haiku 4.5 | Fast codebase exploration, searches files, reads code, answers questions (safe to parallelize) |
| **code-review** | Claude Sonnet 4.5 | High signal-to-noise code review, analyzes diffs for bugs and security issues |
| **general-purpose** | Claude Sonnet 4.5 | Full-capability agent for complex multi-step tasks in separate context |
| **research** | Claude Sonnet 4.6 | Deep research agent generating reports from codebase + web |
| **rubber-duck** | Complementary model | Constructive critique of proposals, designs, implementations |
| **configure-copilot** | Varies | NL-based configuration management (MCP, agents, skills) |

### Advanced Agent Features
- **`/fleet`** — Parallelized sub-agents for multi-file operations
- **`/plan`** → merged code — Full workflow from planning to PR
- **Autopilot mode** — Autonomous multi-step task completion without step-by-step approval
- **Steering** — Guide agent behavior mid-execution
- **Remote steering** — Monitor/respond from GitHub.com or GitHub Mobile
- **`/pr` command** — PR management from terminal
- **Custom agents** — Invoke specialized agents via NL

### BYOK & Local Models (April 2026+)
Copilot CLI now supports **bring-your-own-key** and **local models**:
- Connect any model provider (OpenAI-compatible)
- Offline mode for air-gapped environments
- GitHub authentication optional
- **Requirements**: Model must support tool calling + streaming, 128K+ context window
- Built-in sub-agents inherit your provider config automatically

### MCP-Powered Extensibility
- Ships with GitHub's MCP server by default
- Supports custom MCP servers
- Skills system for reusable workflows
- Custom agents via NL configuration

### GitHub Workflow Integration
- Direct access to repositories, issues, pull requests via NL
- Authenticated with existing GitHub account
- Cloud agent handoff — delegate tasks from CLI to cloud agent
- Code review in terminal → GitHub.com loop

## Model Support

| Tier | Models | How |
|------|--------|-----|
| 🥇 Default | Claude Sonnet 4.5/4.6, Claude Haiku 4.5 | GitHub-hosted model routing |
| 🥇 BYOK | Any OpenAI-compatible API | Custom provider config |
| 🥇 Local | Ollama, LM Studio, etc. | Local endpoint (air-gap capable) |

## Pricing

| Plan | Price | Copilot CLI Access |
|------|-------|--------------------|
| Copilot Free | $0 | ✅ Basic access |
| Copilot Pro | $10/mo | ✅ Full access |
| Copilot Pro+ | $39/mo | ✅ Priority access |
| Copilot Business | $19/user/mo | ✅ Enterprise features |
| Copilot Enterprise | $39/user/mo | ✅ Full + customization |

## Development History

Copilot CLI is one of the fastest-moving coding agent CLIs, shipping near-daily releases with a mature v1.0.x line (v1.0.79 as of 2026-08-10).

### Key milestones
- **2025** — Launched as a standalone CLI, replacing the retired `gh copilot` extension
- **2026-04-07** — BYOK (bring-your-own-key) and local model support added
- **2026-04-22** — Microsoft announces token-based billing shift and tighter rate limits for individual plans (see Billing below)
- **2026-06/07** — Sandbox enforcement matures: macOS/Windows native MDM policy support, managed settings fallback, restrictive enterprise sandbox floors
- **2026-08** — v1.0.79: worktree management (`/worktree new`), prompt pinning, sessions sidebar, tgrep (trigram-indexed grep) for large monorepos, kimi-k3 model support, model picker grouping

### Recent feature highlights (v1.0.77–1.0.79, Jul–Aug 2026)
- **Sessions sidebar** — manage multiple concurrent sessions; resume restores autopilot/plan mode
- **`/worktree new`** — start a new session in a new git worktree; `worktreeBaseRef` setting controls HEAD vs remote default branch
- **Prompt pinning** — pin the current prompt as a single line; off by default, enable via `pinnedPrompts`
- **Queue manager** — queue prompts, shell commands, and slash commands to run in order
- **`/plan` + autopilot combo** — plan first, then implement without waiting for approval
- **tgrep for monorepos** — large codebases now use [tgrep](https://github.com/microsoft/tgrep) (trigram-indexed grep) instead of ripgrep
- **Enterprise sandbox policy** — admins enforce a restrictive sandbox floor via managed settings; `allow-auto-only` policy; proxy URL enforcement
- **Extension plugins** — first-party plugins auto-update; `extraKnownMarketplaces` auto-update support

## Sandbox & Safety

Copilot CLI runs commands in a **sandbox** with per-path read/write enforcement:
- **`/sandbox`** — shows effective sandbox paths, denials, network access, and policy; tags inactive settings as disabled
- **Auth isolation** — git/gh/keychain credentials managed under a dedicated Auth tab (`sandbox.auth.git` / `sandbox.auth.gh`)
- **Managed policy** — macOS and Windows native MDM enforcement; restrictive floors that tighten (never loosen) user policy
- **Enterprise controls** — `allow-auto-only` policy allows `/allow-all auto` while full allow-all stays blocked; proxy URL enforcement with user-controlled credentials
- **Windows Dev Drive** — sandboxed commands work when cwd lives on a Dev Drive
- **Bypass semantics** — disabling sandbox from a bypass prompt applies only to that session; new sessions start sandboxed again

## LSP Server Support

Copilot CLI supports Language Server Protocol (LSP) for code intelligence (go-to-definition, hover, diagnostics). LSP servers are not bundled — install separately (e.g. `npm install -g typescript-language-server`), then configure:
- **User-level**: `~/.copilot/lsp-config.json`
- **Repository-level**: `.github/lsp.json`

## Billing & Pricing Context

Copilot CLI is included in all Copilot plans, but the pricing model shifted significantly in April 2026:

| Plan | Price | Notes |
|------|-------|-------|
| Copilot Free | $0 | Basic access |
| Copilot Pro | $10/mo | 300 premium requests/mo (legacy request model) |
| Copilot Pro+ | $39/mo | Claude Opus 4.7 restricted to this tier |
| Copilot Business | $19/user/mo | Enterprise features |
| Copilot Enterprise | $39/user/mo | Full + customization |

**Token-based billing transition (Apr 2026)**: Microsoft announced moving Copilot from per-request to token-based billing after agentic workloads "fundamentally changed Copilot's compute demands." Leaked internal documents (Where's Your Ed At) showed weekly Copilot costs doubled since the start of 2026, individual signups were temporarily paused, and rate limits tightened. Each prompt submitted to Copilot CLI reduces the monthly premium-request quota by one. Usage caps now matter more than plan tier for heavy agentic use — see [[concepts/github-copilot-billing]].

## Positioning

Copilot CLI is GitHub's answer to Claude Code — but deeply integrated with the GitHub ecosystem. Its key differentiator is **seamless GitHub workflow integration**: issues → planning → code → PR → review, all from the terminal without switching tools.

**Key differentiator vs competitors**: GitHub integration depth (repos, issues, PRs, code review all native), sub-agent specialization, and the `/fleet` parallel execution model.

**History note**: The "GitHub CLI Copilot extension" was retired and replaced by the new standalone Copilot CLI. Do not confuse with the old `gh copilot` extension.

## Related

- [[entities/claude-code]] — primary competitor (terminal-first agentic coding)
- [[entities/codex]] — OpenAI's terminal coding agent
- [[entities/opencode]] — open-source terminal agent with BYOK
- [[entities/droid]] — enterprise multi-surface agent platform
- [[concepts/agent-harnesses]] — harness engineering context
- [[concepts/github-copilot-billing]] — billing model transition
- [[concepts/microsoft-copilot-wave-3]] — Copilot ecosystem wave 3
