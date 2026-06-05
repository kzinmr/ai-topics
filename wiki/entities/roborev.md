---
title: RoboRev
type: entity
aliases: [roborev]
created: 2026-06-05
updated: 2026-06-05
status: L2
tags:
  - code-review
  - ai-agents
  - verification
  - developer-tooling
  - go
  - open-source
  - agent-skills
sources:
  - raw/articles/2026-05-27_hugobowne_the-agentic-software-factory.md
  - https://hugobowne.substack.com/p/the-agentic-software-factory
  - https://roborev.io
  - https://github.com/roborev-dev/roborev
---

# RoboRev

**Continuous background code review daemon.** Created by [[entities/wes-mckinney|Wes McKinney]]. Installs as a post-commit hook, fires a code review through an AI model every time a coding agent commits, and surfaces issues in seconds. RoboRev is the backbone of McKinney's "agentic software factory" — the verification layer that makes parallel agent-driven development safe.

## Overview

| | |
|---|---|
| **Website** | [roborev.io](https://roborev.io) |
| **GitHub** | [roborev-dev/roborev](https://github.com/roborev-dev/roborev) |
| **Language** | Go |
| **Creator** | [[entities/wes-mckinney\|Wes McKinney]] |
| **Releases** | 55+ (v0.26.0+) |

## How It Works

1. **Post-commit hook** — RoboRev installs as a Git post-commit hook
2. **Background review** — Every commit triggers a review via AI (typically Codex with GPT 5.5, reasoning xHigh)
3. **Ledger accumulation** — Findings accumulate in a per-repo ledger
4. **Pre-merge verification** — By the time a PR merges, code has been read by agents 4-5 times minimum
5. **Fix cycle** — `roborev fix` auto-fixes issues; `roborev refine` iterates on branches

## Key Features

| Feature | Description |
|---------|-------------|
| **Multi-agent support** | Codex, Claude Code, Gemini, Copilot |
| **roborev fix** | Auto-fix identified issues |
| **roborev refine** | Iterative branch refinement |
| **roborev analyze refactor** | Per-file refactoring analysis |
| **Interactive TUI** | Terminal interface for reviewing findings |
| **Ledger tracking** | Per-repo issue ledger with fine-grained commit tracking |

## Design Principles

### Asymmetric Generation vs. Review

McKinney generates code with a ~3:1 mix of Claude Code and Codex (fast). The reviewer model (Codex/GPT 5.5) is allowed to be **slower and stronger** because it runs once per commit, not in the generation hot path.

### Drain the Ledger Inline

For long agent runs (14+ hours), McKinney invokes `roborev-fix` every 5 tasks. The agent pauses, picks up open findings from the ledger, fixes them, and continues. Without this, a long run buries the ledger so deep that context is gone by the time anyone reads it.

### Your Job Is Structure, Not Lines

> *"I almost don't read code now."* — Wes McKinney

RoboRev handles line-by-line correctness. The human focuses on structural questions: is the scope right, is the complexity warranted, is this the right thing to build.

## Impact

- **3,000+ automated reviews** in a matter of weeks
- **1M+ lines of code** reviewed in 6 months
- Enables parallel management of 4-5 projects simultaneously
- Monthly API cost: ~$21,765.80 at API rates (for all tools combined)

## Related

- [[entities/wes-mckinney]] — Creator
- [[entities/agents-view]] — Companion session viewer
- [[entities/middleman]] — Companion local GitHub dashboard
- [[concepts/generator-evaluator-pattern]] — RoboRev as the "evaluator" half

## References

- [roborev.io](https://roborev.io)
- [GitHub](https://github.com/roborev-dev/roborev)
- [The Agentic Software Factory](https://hugobowne.substack.com/p/the-agentic-software-factory) (Vanishing Gradients, May 2026)

## Log

- **2026-06-05**: Initial entity page created.
