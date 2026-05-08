---
title: "Effective Harnesses for Long-Running Agents"
type: concept
created: 2026-04-25
updated: 2026-05-08
tags:
  - harness-engineering
  - agent-architecture
  - claude-agent-sdk
  - long-running
aliases:
  - long-running agent harness
  - multi-context-window agent
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_effective-harnesses-for-long-running-agents.md
  - https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
related:
  - building-effective-agents
  - harness-design-long-running-apps
  - agent-skills
  - claude-code-best-practices
---

# Effective Harnesses for Long-Running Agents

Anthropicによる、複数コンテキストウィンドウを跨ぐ長時間稼働エージェントのハーネス設計。Claude Agent SDKをベースにした2部構成のソリューション。

## 核心的課題

> 各セッションはゼロから始まる。前のシフトで何が起きたか記憶していない新しいエンジニアが毎回やってくるソフトウェアプロジェクトを想像せよ。

### 2つの典型的失敗パターン

1. **一気にやりすぎ**: アプリ全体をone-shotしようとしてコンテキスト途中切れ → 次のセッションは中途半端な実装を推測から再開
2. **早期完了宣言**: ある程度進捗した後、後のエージェントが「完了」と判断してしまう

## 2部構成ソリューション

### 1. Initializer Agent（初回セッション専用）

**役割**: 後続のコーディングエージェントが効果的に作業できる環境を整備

生成する成果物:
- `init.sh` — 開発サーバー起動・基本E2Eテスト実行スクリプト
- `claude-progress.txt` — エージェントの作業ログ
- `feature_list.json` — 200以上の機能要件リスト（全項目初期状態: `"passes": false`）
- 初期git commit

```json
{
    "category": "functional",
    "description": "New chat button creates a fresh conversation",
    "steps": ["Navigate to main interface", "Click 'New Chat'", ...],
    "passes": false
}
```

**重要な設計判断**: JSONフォーマットを使用（Markdownよりモデルが不適切に変更・上書きしにくい）

### 2. Coding Agent（後続全セッション）

**原則**:
- 1セッションで**1機能のみ**に集中
- セッション終了時は**クリーンな状態**で残す（mainブランチにマージ可能な品質）
- 記述的なgitコミットメッセージ + 進捗ファイルにサマリを記録

### セッション開始ルーチン

```
1. pwd → 作業ディレクトリ確認
2. git log + progress file → 最近の作業内容を把握
3. feature_list.json → 最高優先度の未完了機能を選択
4. init.sh → 開発サーバー起動 + 基本E2Eテスト
5. 基本機能が壊れていないことを確認してから新機能に着手
```

## テスト戦略

- **ブラウザ自動化ツール必須**（Puppeteer MCP等）: 「人間のユーザーがするように」E2Eテスト
- 明示的に指示しないと、ユニットテストだけしてE2Eを確認しない傾向
- **制限**: ブラウザネイティブのアラートモーダルはPuppeteer MCPで見えない等

## 知見

> 効果的なソフトウェアエンジニアが日常的に行っていることから着想を得た。

- gitによる悪い変更のrevertと動作状態への復帰
- 次のセッションが「推測」に時間を浪費しないための明確なアーティファクト
- トークン節約: 毎回テスト方法を考えさせるより、init.shで標準化

## See Also

- [[concepts/building-effective-agents]] — Building effective agents
- [[harness-design-long-running-apps]] — Harness design for long-running apps
- [[concepts/agent-skills]] — Equipping agents with skills
- [[concepts/claude-code-best-practices]] — Claude Code best practices
- [[concepts/carlini-c-compiler-agents]] — Carlini's parallel agent experiment
