---
title: RoboRev
type: entity
aliases: [roborev]
created: 2026-06-05
updated: 2026-08-07
status: L3
tags:
  - coding-agents
  - ai-agents
  - verification
  - developer-tooling
  - go
  - open-source
sources:
  - raw/articles/2026-05-27_hugobowne_the-agentic-software-factory.md
  - transcripts/2026-05-08_vanishing-gradients_show-us-your-agent-skills-ep1.md
  - https://hugobowne.substack.com/p/the-agentic-software-factory
  - https://roborev.io
  - https://github.com/kenn-io/roborev
  - https://kenn.io
---

# RoboRev

**Continuous background code review daemon.** Created by [[entities/wes-mckinney|Wes McKinney]] and maintained by his company **Kenn Software** (kenn.io). Installs as a post-commit hook, fires a code review through an AI model every time a coding agent commits, and surfaces issues in seconds. RoboRev is the backbone of McKinney's "agentic software factory" — the verification layer that makes parallel agent-driven development safe.

## Overview

| | |
|---|---|
| **Website** | [roborev.io](https://roborev.io) |
| **GitHub** | [kenn-io/roborev](https://github.com/kenn-io/roborev) |
| **Maintainer** | Kenn Software (kenn.io), led by [[entities/wes-mckinney\|Wes McKinney]] |
| **Language** | Go |
| **License** | MIT |
| **Created** | 2026-01-05 |
| **Stars** | ~1,600 (Aug 2026) |
| **Forks** | 143 |
| **Latest Release** | v0.64.0 (2026-08-06) |

## How It Works

RoboRev automates code review at two layers:

1. **Post-commit reviews** — `roborev init` installs a Git post-commit hook; every commit triggers a background review via an AI model (typically Codex with GPT 5.5, reasoning xHigh)
2. **Agent hook** — `roborev agent-hook install` watches supported coding-agent sessions and brings open findings back into the active workflow (after configured turn, commit, or failed-review thresholds)

Findings accumulate in a per-repo ledger. By the time a PR merges, code has been read by agents 4-5 times minimum. Before shipping, the `/roborev-refine` skill re-reviews and fixes the whole branch until every review passes.

```bash
roborev init                  # layer 1: per-commit reviews
roborev skills install        # install agent skills for Claude/Codex/Droid/Grok
roborev agent-hook install    # layer 2: auto-detect and wire installed agents
```

## Key Features

| Feature | Description |
|---------|-------------|
| **Multi-agent support** | Codex, Claude Code, Gemini, Copilot, OpenCode, Cursor, Kiro, Kilo, Droid, Pi |
| **Agent hooks** | Claude Code, Codex, Copilot CLI, Cursor, Factory Droid, Gemini CLI, Hermes, Qwen, Grok Build (v0.64.0+) |
| **roborev fix** | Auto-fix identified issues (feeds findings to an agent, applies fixes, commits) |
| **roborev refine** | Iterative auto-fix loop: fix → re-review → repeat in an isolated worktree until passing |
| **roborev analyze** | Targeted code analysis: `test-fixtures`, `duplication`, `refactor`, `complexity`, `api-design`, `dead-code`, `architecture`, `security` |
| **roborev compact** | Verify findings against current code, filter false positives, consolidate related issues |
| **roborev export** | `export reviews` / `export ci-metrics` / `export ci-costs` — JSON exports with cursor-based pagination |
| **Interactive TUI** | Terminal interface with vim-style navigation for reviewing findings |
| **Ledger tracking** | Per-repo issue ledger with fine-grained commit tracking |
| **Extensible hooks** | Shell commands on review events; built-in beads and kata integrations file trackable issues from review failures |

## Recent Release Highlights

| Version | Date | Notable |
|---------|------|---------|
| v0.64.0 | 2026-08-06 | GitLab merge request support in `roborev ci review`; first-class Grok Build agent support; multiple named ACP agents + Goose; workspace-scoped snoozing; custom skill install paths; PostgreSQL password env-var support |
| v0.63.0 | 2026-07-16 | CI quiet-hours throttling; machine-readable launch receipts for `roborev run`; tighter `roborev-fix` skill triggers |
| v0.62.x | 2026-07-11/14 | `roborev cancel` for queued jobs; persisted CI panel metrics + `export ci-metrics`; honor `CLAUDE_CONFIG_DIR`/`CODEX_HOME` |
| v0.61.3 | 2026-07-09 | Auto-repair of roborev-managed git hooks on daemon start |

## Design Principles

### Asymmetric Generation vs. Review

McKinney generates code with a ~3:1 mix of Claude Code and Codex (fast). The reviewer model (Codex/GPT 5.5) is allowed to be **slower and stronger** because it runs once per commit, not in the generation hot path.

### Drain the Ledger Inline

For long agent runs (14+ hours), McKinney invokes `roborev-fix` every 5 tasks. The agent pauses, picks up open findings from the ledger, fixes them, and continues. Without this, a long run buries the ledger so deep that context is gone by the time anyone reads it.

### Your Job Is Structure, Not Lines

> *"I almost don't read code now."* — Wes McKinney

RoboRev handles line-by-line correctness. The human focuses on structural questions: is the scope right, is the complexity warranted, is this the right thing to build.

## Claude Code Proxy Routing

`claude-code` agent accepts a model spec of the form `<model>@<base_url>` for routing to Ollama/LiteLLM etc. roborev pins all tier aliases (Opus/Sonnet/Haiku/subagent) to the given model; proxy URLs must not embed credentials (use `ROBOREV_CLAUDE_PROXY_TOKEN`); `http://` only accepted for loopback hosts.

## Security Model & Telemetry

- **Trusted codebases**: review agents may execute read-only git/shell commands; fix agents run in isolated worktrees with full tool access. For untrusted code (e.g., OSS contributions), run inside a sandboxed container/VM to limit prompt-injection blast radius.
- **Telemetry**: limited anonymous PostHog events on daemon start/active (repo count, review count, sync/CI enabled). No repo names, paths, prompts, review output, or tokens. Disable with `ROBOREV_TELEMETRY_ENABLED=0`.

## Impact

- **3,000+ automated reviews** in a matter of weeks
- **1M+ lines of code** reviewed in 6 months
- Enables parallel management of 4-5 projects simultaneously
- Monthly API cost: ~$21,765.80 at API rates (for all tools combined)

## Related

- [[entities/wes-mckinney]] — Creator; Kenn Software founder
- [[entities/agentsview]] — Companion session viewer (kenn-io/agentsview, ~4.7K stars)
- **kata** (kenn-io/kata) — Companion local-first issue tracker with review-to-issue integration (no entity page yet)
- [[concepts/evaluation/generator-evaluator-pattern]] — RoboRev as the "evaluator" half
- kenn-io ecosystem: msgvault, forge, docbank, vibepulse (see kenn.io)

## References

- [roborev.io](https://roborev.io)
- [GitHub: kenn-io/roborev](https://github.com/kenn-io/roborev)
- [Kenn Software (kenn.io)](https://kenn.io)
- [The Agentic Software Factory](https://hugobowne.substack.com/p/the-agentic-software-factory) (Vanishing Gradients, May 2026)

## Log

- **2026-06-05**: Initial entity page created.
- **2026-08-07**: Enriched to L3: repo moved to kenn-io (Kenn Software), current stats (1.6K stars, v0.64.0), agent hooks for 9 harnesses, code analysis types, exports, security model, kata/beads integrations.
