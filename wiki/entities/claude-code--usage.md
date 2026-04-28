---
title: "Claude Code — Usage & Workflows"
type: entity
parent: claude-code
created: 2026-04-28
updated: 2026-04-28
tags:
  - product
  - usage
  - workflow
  - pricing
sources:
  - https://claude.com/blog/introducing-routines-in-claude-code
---

# Claude Code: Usage & Workflows

Back to main profile: [[claude-code]]

## Core Workflow Patterns

### Parallel Agent Execution
Boris Chernyの最も影響力のある洞察:
> "Run 3–5 Claude sessions simultaneously using git worktrees or separate checkouts."

- 1つのエージェントがログを読みクエリを実行（分析用ワークツリー）
- 複数のエージェントが並行して機能を実装（機能用ワークツリー）
- 人間はコーディネーター兼承認者として機能

### Plan Mode → Auto-Accept
1. **Plan Modeで開始** (`Shift+Tab` 2回) — Claudeがアプローチを概説
2. **レビューと改善** — 計画が堅固になるまでClaudeと対話
3. **Auto-acceptに切り替え** — Claudeが計画を実行、通常は一発で成功
4. **検証** — Claudeがテストを実行またはブラウザ拡張機能で確認

### CLAUDE.md as Team Memory
- チームで共有するファイルをgitで管理
- 間違いのたびにCLAUDE.mdを更新
- PRで`@claude`を使用してガイドラインを更新

## Terminal Environment

### Recommended Setup
- **Ghostty**: チームが推奨（同期レンダリング、24-bitカラー、Unicodeサポート）
- **tmux**: ワークツリーごとにタブをカラーコード/命名
- シェルエイリアス（za, zb, zc）で瞬時のワークツリー切り替え
- ターミナルタブを1-5に番号付け、システム通知を有効化

### Mobile-to-Desktop Workflow (2026)
iOSからタスクを開始し、デスクトップにルーティングして実行、PRとして仕上げる「Phone to PR」ワークフローに対応。

## Claude Design Integration

Claude Design (April 2026) creates a direct handoff pipeline to Claude Code. When a design is complete, Claude Design packages everything into a handoff bundle that Claude Code can receive with a single instruction.

## Pricing (April 2026)

| Plan | Price | Details |
|------|-------|---------|
| **Pro** | $17/mo annual or $20/mo monthly | Claude Code included; Sonnet 4.6 + Opus 4.7 |
| **Max 5x** | $100/mo | Larger codebases, more usage |
| **Max 20x** | $200/mo | Maximum access, power users |
| **Team** | $20/seat/mo (5–150 seats) | Self-serve seat management |
| **Enterprise** | Contact sales | Advanced security, data management |
| **API** | Pay-as-you-go | No per-seat fee, unlimited developers |
