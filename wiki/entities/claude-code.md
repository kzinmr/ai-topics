---
title: Claude Code
type: entity
created: 2026-04-24
updated: 2026-04-27
tags:
  - product
  - coding-agent
  - anthropic
aliases:
  - Claude Code CLI
  - Anthropic Coding Agent
  - Claude Code Desktop
sources:
  - raw/articles/openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md
  - https://code.claude.com/en/whats-new/2026-w15
  - https://code.claude.com/en/whats-new/2026-w14
  - https://code.claude.com/en/changelog
  - https://www.getaiperks.com/en/articles/claude-code-updates
  - https://arxiv.org/html/2604.14228v1
  - https://claude.com/blog/introducing-routines-in-claude-code
  - https://claude.com/blog/auto-mode
---

# Claude Code

AnthropicのAIコーディングエージェント。CLI、デスクトップアプリ、VS Code/JetBrains拡張、Web、iOS、Slackマルチサーフェスで動作。[[boris-cherny]]によって開発され、2025年7月に[[anthropic]]から[[openai]]へ移管された。

SWE-bench Verifiedで72.7%を達成。2026年4月現在、7.6倍のデプロイ頻度向上、89%のAI採用率を記録する業界トップのコーディングエージェント。

## 基本情報

| 項目 | 内容 |
|------|------|
| 開発元 | Anthropic（オリジナル）→ OpenAI（2025年7月移管） |
| 開発者 | Boris Cherny |
| 初回リリース | 2025年5月（GA） |
| 最新メジャー | v2.1.119（2026年4月23日） |
| 標準モデル | Opus 4.7, Sonnet 4.6, Haiku 4.5 |
| 対応環境 | CLI, Desktop, VS Code, JetBrains, Web, iOS, Slack |

## Sub-Pages

- **[[claude-code--capabilities]]** — Key metrics, latest features (Ultraplan, Monitor, Auto Mode, Routines, CLI Computer Use, Fast Mode), and key capabilities (Subagents, MCP Integration, Slash Commands, Checkpointing, Skills System)
- **[[claude-code--architecture]]** — 5-layer decomposition, 7-component flow, core loop, infrastructure dominance (98.4% deterministic infra)
- **[[claude-code--usage]]** — Workflow patterns (parallel agent execution, Plan Mode → Auto-Accept), terminal setup, Claude Design integration, pricing
- **[[claude-code--history]]** — Origins, internal dogfooding, GA, OpenAI transfer, Agent Teams GA, and the source code leak incident

## Key Metrics (2026)

| Metric | Value |
|--------|-------|
| SWE-bench Verified | 72.7% (vs Codex 69.1%) |
| Deployment frequency increase | **7.6x** |
| AI adoption across employees | **89%** |
| Feature delivery speed | **2x faster** |
| Incident investigation speed | **80% faster** |

## Comparisons

- **Cursor** — Competitor
- **OpenAI Codex** — Competitor (SWE-bench: 69.1% vs Claude Code 72.7%)

## Related

- [[boris-cherny]] — Creator
- [[anthropic]] — Original developer
- [[openai]] — Current owner (since Jul 2025)
- [[claude-mythos]] — Withheld high-security model
- [[concepts/project-glasswing]] — Safety initiative
- [[concepts/harness-engineering]]

## Sources

- [Claude Code What's New — Week 15 (Ultraplan, Monitor)](https://code.claude.com/en/whats-new/2026-w15) (Apr 2026)
- [Claude Code What's New — Week 14 (CLI Computer Use)](https://code.claude.com/en/whats-new/2026-w14) (Apr 2026)
- [Claude Code Changelog](https://code.claude.com/en/changelog)
- [Introducing Routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code) (Apr 14, 2026)
- [Auto Mode Blog](https://claude.com/blog/auto-mode) (Mar 24, 2026)
- [GetAI Perks — Claude Code Updates 2026](https://www.getaiperks.com/en/articles/claude-code-updates) (Mar 26, 2026)
- [arXiv:2604.14228v1 — Dive into Claude Code Architecture](https://arxiv.org/html/2604.14228v1) (Apr 2026)
- [Claude Code Camp — How the team really works](https://www.claudecodecamp.com/p/how-the-claude-code-team-really-works) (Feb 5, 2026)
- [The Register — Claude Code source code leak](https://www.theregister.com/2026/03/31/anthropic_claude_code_source_code/) (Mar 31, 2026)
