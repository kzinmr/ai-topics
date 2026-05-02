---
title: "Claude Code Best Practices"
type: concept
aliases:
  - claude-code-best-practices
  - claude-code-tips
created: 2026-04-25
updated: 2026-04-29
tags:
  - concept
  - anthropic
  - best-practices
status: complete
sources:
  - url: "https://code.claude.com/docs/en/best-practices"
    title: "Official Claude Code Best Practices (Anthropic)"
  - url: "https://aiorg.dev/blog/claude-code-best-practices"
    title: "Claude Code Best Practices: 15 Tips from 6 Projects (aiorg.dev, 2026)"
  - url: "https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026"
    title: "Claude Code Advanced Best Practices 2026 (SmartScope)"
  - url: "https://ranthebuilder.cloud/blog/claude-code-best-practices-lessons-from-real-projects"
    title: "Claude Code Best Practices: Lessons from Real Projects (Ran Isenberg, 2026)"
---

# Claude Code Best Practices

**Claude Code Best Practices** は、Anthropic の AI コーディングエージェント「Claude Code」を最大限に活用するための設計パターンと運用ノウハウの集大成。**CLAUDE.md の設定**、**プロンプティングパターン**、**ワークフロー習慣**の3つに大別される。

## 3つの基本カテゴリ

### 1. プロジェクトセットアップ

#### CLAUDE.md（最重要）
プロジェクトの「メモリーカード」。1回の作成で毎セッション20〜30%のトークンを節約：
```
# プロジェクト概要と対象読者
# 技術スタックとフレームワークバージョン
# 主要なビルド・テスト・デプロイコマンド
# プロジェクト構造
# コーディング規約
# 重要なルール（秘密情報非コミット、アクセシビリティ要件など）
```
**重要**: 200行以内に抑える。肥大化は逆効果。

#### .claudeignore
`.gitignore` と同様に、Claude Code がスキップするファイルを指定：
```
node_modules/
.next/
dist/
*.lock
*.log
coverage/
.env*
```
トークン消費を50〜70%削減可能。

#### ルール（`.claude/rules/*.md`）
トピック別のモジュラー設定：
- テストガイドライン
- データ可視化規約
- API 設計ルール

### 2. プロンプティングパターン

| パターン | 説明 | 使用タイミング |
|---------|------|--------------|
| **Plan Mode** | 実行前に計画を確認 | 3ファイル以上に影響する変更 |
| **Feedback Loops** | 品質を2〜3倍向上 | コードレビュー・リファクタリング |
| **Pattern Reference** | 既存パターンを参照 | 新しいAPIルート作成など |
| **One Task Per Session** | 1セッション=1タスク | 複雑なマルチステップ作業 |

### 3. ワークフロー習慣

- **/compact**: コンテキスト圧縮（200Kウィンドウ管理）
- **Hooks**: 確定的な品質ゲート（毎回必ず実行）
- **Slash Commands**: カスタムコマンド（git, test, PR）
- **Git Worktrees**: 5つの Claude エージェントを並列実行
- **Subagents**: セキュリティレビューなどの専門タスクを委譲

## 上級テクニック

| テクニック | 説明 |
|-----------|------|
| **Hooks は必須、CLAUDE.md は助言** | Hooks は確定的に実行、CLAUDE.md は参考情報 |
| **Subagents は別コンテキスト** | サブエージェントは独立したコンテキストウィンドウで動作 |
| **Skills は自動発火** | `.claude/skills/` の SKILL.md が文脈に応じて自動適用 |
| **承認疲れ対策** | Allowlist + Sandbox で頻繁な承認を効率化 |
| **2回失敗 = /clear** | 2回連続失敗したらセッションリセット |
| **1回のセッション=1タスク** | 集中したコンテキストで最高のパフォーマンス |

## よくある落とし穴

| 落とし穴 | 対策 |
|---------|------|
| CLAUDE.md が長すぎる | 200行以内、リンクで外部化 |
| 複数タスクを1セッションで | タスクごとに /compact または新規セッション |
| 承認を毎回要求 | Allowlist + Sandbox 設定 |
| Hooks を使わない | 確定的な品質ゲートを設定 |
| 計画なしで実行 | Plan Mode で事前確認 |

## 関連概念

- [[concepts/claude-perfect-memory]] — Claude Code の永続メモリ設計
- [[concepts/agent-loop-orchestration]] — エージェントループパターン
- [[concepts/monty-sandbox]] — コード実行サンドボックス

## ソース

- [Official Claude Code Best Practices (Anthropic)](https://code.claude.com/docs/en/best-practices)
- [Claude Code Best Practices: 15 Tips from 6 Projects](https://aiorg.dev/blog/claude-code-best-practices)
- [Claude Code Advanced Best Practices 2026](https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026)
- [Lessons from Real Projects (Ran Isenberg, 2026)](https://ranthebuilder.cloud/blog/claude-code-best-practices-lessons-from-real-projects)
