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
- [Anthropic — Measuring Agent Autonomy](https://www.anthropic.com/news/measuring-agent-autonomy) (Feb 2026)
- [Kuber Studio — Claude Code Source Code Leak Analysis](https://kuber.studio/blog/AI/Claude-Code's-Entire-Source-Code-Got-Leaked-via-a-Sourcemap-in-npm,-Let's-Talk-About-it) (Apr 2026)

## References

- 2026-04-16-vivek-trivedy-harness-memory-context-fragments
- 2026-04-28_x-article-the-harness-is-the-backend
- 2026-04-30_willccbb-analysis-rl-harness-lifecycle
- 2026-04-30_willccbb-rl-harness-lifecycle
- 2026-04-viv-harness-memory-context-fragments-bitter-lesson
- 2039441705586602134_The-Trillion-Dollar-Loop-B2B-Never-Had
- 2042660310851449223_Latent-Briefing-Efficient-Memory-Sharing
- crawl-2026-04-23-build-harness-not-code
- crawl-2026-04-23-harness-engineering-discipline

- 2026-01-02_boris-cherny---my-claude-code-setup-(jan-2026)
- 2026-01-31_boris-cherny---10-tips-from-the-claude-code-team-(feb-2026)
- 2026-02-11_chernycode---boris-cherny's-claude-code-config-files
- 2026-03-19-claude-agents-disagree-experiment
- 2026-04-09-claude-managed-agents-guide
- 2026-04-26-claude-code-openclaw-harness-practice
- 2026-keep-your-claude-code-context-clean-with-subagents
- 2041927992986009773_Launching-Claude-Managed-Agents
- 2047720067107033525_Memory-in-Claude-Managed-Agents
- boris-cherny-im-boris-i-created-claude-code
- crawl-2026-04-23-claude-code-design-space
- how-claude-code-team-really-works

## Prompt Caching Architecture (April 2026)

Claude Code is built around prompt caching from day one. The team runs alerts on cache hit rate and declares SEVs if it's too low. Key architectural decisions:

- **Static-first layout**: System prompt → Claude.MD → Session context → Messages. Any change anywhere in the prefix invalidates everything after it.
- **Messages over prompt edits**: When information becomes stale, `<system-reminder>` tags in messages preserve the cache.
- **No mid-session model switching**: Cache is per-model. Switching mid-conversation is more expensive than continuing.
- **Tool state via tools, not tool set changes**: Plan Mode uses `EnterPlanMode`/`ExitPlanMode` as tools rather than swapping tool definitions.
- **Deferred tool loading**: Lightweight stubs (`defer_loading: true`) with `ToolSearch` for discovery keep the prefix stable.
- **Cache-safe compaction**: Context compaction reuses the parent's exact system prompt, tools, and history to get cache hits.

**April 2026 Regression**: Shipped a 47% performance regression caught by user community before internal monitoring — a widely-cited lesson on immature production agent eval practices even at the leaders.

Sources: "Lessons from Building Claude Code: Prompt Caching Is Everything" (April 2026), "Prompt auto-caching with Claude" (@RLanceMartin)

See also: [[concepts/prompt-caching]], [[concepts/context-engineering]]

