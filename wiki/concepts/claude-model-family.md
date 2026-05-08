---
title: "Build with Claude — Developer Guide"
type: concept
aliases:
  - claude
  - Claude AI
  - anthropic-claude
  - claude-models
  - build-with-claude
  - claude-developer-guide
created: 2026-05-08
updated: 2026-05-08
tags:
  - concept
  - anthropic
  - model-family
  - model
  - large-language-model
  - ai-agents
  - developer-guide
  - developer-tooling
status: complete
sources:
  - url: "https://www.anthropic.com/learn/build-with-claude"
    title: "Build with Claude — Anthropic Developer Guide"
  - url: "https://www.anthropic.com/news/claude-3-family"
    title: "Claude 3 Family Announcement"
  - url: "https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking"
    title: "Extended Thinking Guide"
  - url: "https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching"
    title: "Prompt Caching Guide"
  - url: "https://github.com/anthropics/anthropic-cookbook"
    title: "Anthropic Cookbook"
  - url: "https://www.anthropic.com/research/building-effective-agents"
    title: "Building Effective Agents — Anthropic"
  - url: "https://www.anthropic.com/engineering/harness-design-long-running-apps"
    title: "Harness Design for Long-Running Application Development"
related:
  - "[[entities/anthropic]]"
  - "[[entities/claude-code]]"
  - "[[entities/claude-design]]"
  - "[[claude-managed-agents]]"
  - "[[concepts/mcp]]"
  - "[[claude-opus-4-7]]"
  - "[[concepts/anthropic-computer-use]]"
  - "[[concepts/claude-memory-tool]]"
  - "[[concepts/extended-thinking]]"
  - "[[concepts/prompt-caching]]"
  - "[[concepts/claude-agent-sdk-orchestration-hooks-subagents-plan-mode-output-styles]]"
  - "[[concepts/ai-safety-military-governance-claude]]"
  - "[[concepts/coding-agents]]"
---

# Build with Claude — Developer Guide

> **Claude** は [[entities/anthropic]] が開発する LLM ファミリー。Constitutional AI を安全設計思想とし、**Haiku / Sonnet / Opus** の3階層で提供される。
> 本ページは [Anthropic の Build with Claude ガイド](https://www.anthropic.com/learn/build-with-claude) の構成に従い、開発者がアプリケーションに Claude を組み込むための実践的な指針をまとめる。
> 個別製品・モデルの詳細は各サブページを参照。

---

## 🚀 1. Quick Start — 開発の第一歩

[Anthropic Console](https://console.anthropic.com) でAPIキー発行。[Quickstart Guide](https://docs.anthropic.com/en/docs/get-started) で初回APIリクエスト。CLIで `npm install -g @anthropic-ai/claude-code`。詳細は [Developer Docs](https://docs.anthropic.com/en/home) と [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) を参照。

---

## 🧠 2. Advanced Model Capabilities — 高度なモデル機能

### 2.1 Extended Thinking（拡張思考）

Claude が応答前に内部推論ステップを実行する機能。2025年2月の Claude 3.7 Sonnet で初導入。

- **向いているタスク**: 複雑な論理・数学・コーディング、マルチステップ推論
- **API での利用**: `thinking` パラメータを指定
- **料金**: 推論トークンは出力トークン価格で課金
- **Claude Code での活用**: Ultraplan 機能や Subagent 委任で内部的に利用
- 詳細: [Extended Thinking Guide](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)

### 2.2 Vision & マルチモーダル

Claude 3 以降、画像入力に対応。Opus 4.7 で最高水準の視覚認識を達成。

- **入力可能なメディア**: 画像（JPEG/PNG/GIF/WebP）、PDF（テキスト+画像）
- **ユースケース**: スクリーンショット解析、チャート読み取り、PowerPoint スライド解析、技術図面の理解
- **テクニック**: 複数画像の比較、テキスト埋め込み画像の文字起こし
- 詳細: [[concepts/multimodal]]

### 2.3 Computer Use（ベータ）

Claude がスクリーンショットを見てデスクトップ GUI を直接操作する機能。

- **操作方法**: クリック、キー入力、スクロール（人間と同等の操作）
- **導入経緯**: 2024年10月 研究プレビュー → 2026年2月 Vercept 買収で機能強化
- **ユースケース**: ブラウザ操作、デスクトップアプリの操作、データ入力の自動化
- **制約**: ベータ版、レイテンシと精度に改善余地あり
- 詳細: [[entities/anthropic-computer-use]]

---

## 🛠️ 3. Architectural Patterns — アーキテクチャパターンとツール

> **設計原則（[Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) より）**:
> 1. **Simple is best** — 複雑なフレームワークより、小さな構成可能なパターンを
> 2. **Context is all you need** — 豊富なコンテキスト環境が明示的 planner より効果的
> 3. **Deterministic infrastructure over decision scaffolding** — エージェント実行基盤の98.4%は決定論的でよい
> 4. **Unix philosophy** — 最小構成要素は「有用で理解可能で拡張可能」であること

### 3.1 Tool Use（関数呼び出し）

Claude が外部 API やローカルツールと対話するための標準機能。2023年11月ベータ導入、2024年3月GA。

- **標準ツール**: Bash実行、ファイル編集、テキストエディタ、コード実行、Web検索
- **カスタムツール**: JSONスキーマで任意の外部APIを定義
- **MCP統合**: [[concepts/mcp]] 対応ツールサーバーと接続
- **並列呼び出し**: 複数ツールの同時実行が可能
- 学習リソース: [Tool Use Course](https://github.com/anthropics/courses/blob/master/tool_use/README.md)

### 3.2 Agents & Skills — 自律エージェントの構築

Claude で自律エージェントを構築するための3層アプローチ：

| 階層 | 説明 | 具体例 |
|------|------|--------|
| **Skills** | タスク特化の指示ブロック | コードレビュースキル、テスト生成スキル |
| **MCP** | ツール接続のオープン標準 | ファイルシステムMCP、DB MCP、Slack MCP |
| **Agent SDK** | エージェントライフサイクルの管理 | Hooks, Subagents, Plan Mode |

Claude Agent SDK (`@anthropic-ai/claude-agent-sdk`) の主要機能：
- **Hooks**: `before_tool`, `after_tool`, `on_error` などのライフサイクルフック
- **Subagents**: 子エージェントの生成と結果収集
- **Plan Mode**: 実行前に計画を生成・承認するワークフロー
- **Output Styles**: 構造化出力のスタイル指定
- **MCP統合**: ビルトインMCPサーバー対応

### 3.3 RAG — 外部データとの統合

Claude に外部データを組み合わせて回答精度を向上させる：

- **Contextual Retrieval**: Anthropic が開発した高精度RAG手法
- **対応埋め込み**: Voyage AI と統合
- **対応フレームワーク**: LlamaIndex, MongoDB
- **テクニック**: プロンプトキャッシングで参照文書のコストを削減

### 3.4 Structured Output（構造化出力）

モデルの出力を確実にJSONスキーマに従わせる機能。

- JSONモードでスキーマ準拠をバリデーション保証
- エージェント制御の信頼性向上、後続処理のパース不要に
- 参照: [[concepts/claude-code-prompt-engineering-context-management-caching-agent-architecture]]

---

## 📈 4. Optimization & Performance — 最適化と性能

### 4.1 Prompt Engineering

Claude の性能を最大限引き出すプロンプト設計：

- **[Prompt Generator](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-generator)** — 自動プロンプト生成ツール
- **[Interactive Tutorial](https://github.com/anthropics/courses/blob/master/prompt_engineering_interactive_tutorial/README.md)** — 対話型学習コース
- **ポイント**: 明確な指示、例示（Few-shot）、役割設定、出力フォーマット指定
- **システムプロンプト**: 永続的な指示をシステムメッセージとして設定

### 4.2 Prompt Caching

頻繁に送信される大きなコンテキストを再利用してコスト・レイテンシを削減：

- **キャッシュ書き込みコスト**: 標準入力の1.25倍
- **キャッシュ読み取りコスト**: 標準入力の**10%**（5分間有効）
- **効果**: 長いシステムプロンプトや参照文書を何度も送るワークロードで大幅なコスト削減
- **例**: Sonnet 4.6でシステムプロンプト50Kトークンの場合、通常 $0.15 → キャッシュ $0.015

| モデル | キャッシュ書込 ($/MTok) | キャッシュ読込 ($/MTok) |
|--------|----------------------|----------------------|
| Opus 4.7 | $6.25 | $0.50 |
| Sonnet 4.6 | $3.75 | $0.30 |
| Haiku 4.5 | $1.25 | $0.10 |

- 詳細: [Prompt Caching Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)

### 4.3 Evaluations（Evals）

システム的な性能測定でプロンプトとアーキテクチャを改善：

- **Anthropic Console**: ブラウザ上でEvalを作成・実行・比較
- **自動化パイプライン**: [Cookbook Notebook](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building_evals.ipynb) でCI/CD統合
- **バッチ処理**: 全トークンコスト50%オフで大規模Eval実行
- **測定項目**: 精度、レイテンシ、コスト、一貫性

---

## Appendix A: モデルリファレンス

### A.1 2分でわかる3階層

| 階層 | 価格 (input) | 最適ワークロード | 推奨ユーザー |
|------|-------------|-----------------|------------|
| **Haiku 4.5** 🏎️ | $1/MTok | 分類、抽出、ルーティング、チャット | コスト重視・高スループット |
| **Sonnet 4.6** ⚖️ | $3/MTok | コーディング、エージェント、知識業務、RAG | 本番ワークロードの第一候補 |
| **Opus 4.7** 🧠 | $5/MTok | 高難易度推論、長時間計画、複雑コーディング | 品質最優先のフロンティアタスク |

### A.2 簡易タイムライン

| 期間 | マイルストーン |
|------|--------------|
| 2023 | Claude 1 → 2.1。Tool Useベータ、200Kコンテキスト。Constitutional AI確立 |
| 2024 | Claude 3 (Haiku/Sonnet/Opus)。3階層 + マルチモーダル導入。3.5 SonnetでOpus級性能をSonnet価格に |
| 2025前 | 3.7 Sonnetで Extended Thinking。Claude Codeリリース。GPT-4oと競合 |
| 2025後 | Claude 4 → 4.5 世代。SWE-bench 77.2%達成。Computer Use改善。Bun買収 |
| 2026上 | Opus 4.6 (2月)→ Sonnet 4.6 (2月)→ Opus 4.7 (4月)。Managed Agents GA。Claude Design発表 |

詳細なモデル別情報は各サブページを参照：[[claude-opus-4-7]], [[claude-sonnet-4.6]], [[claude-opus-4-6]]

---

## Appendix B: エコシステム概要

| 製品 | 説明 | 詳細 |
|------|------|------|
| **Claude.ai** | 公式Web/モバイルチャット。サブスクリプション方式 | Projects, ファイル添付, 200Kコンテキスト |
| **[[entities/claude-code]]** | 自律型コーディングエージェント (CLI/IDE/Web/Mobile/Slack) | SWE-bench 72.7%, 7.6xデプロイ向上 |
| **[[entities/claude-design]]** | ビジュアルデザインコラボレーションツール (2026年4月研究プレビュー) | Opus 4.7視覚モデル搭載 |
| **[[claude-managed-agents]]** | エンタープライズ向けマネージドエージェントプラットフォーム | メモリストア、マルチエージェント、Outcomes Loop |
| **[[concepts/mcp]]** | Model Context Protocol — ツール接続のオープン標準 | OpenAI/Google/Microsoft/Red Hat採用 |
| **Claude Agent SDK** | Node.js SDK (`@anthropic-ai/claude-agent-sdk`) | Hooks, Subagents, Plan Mode |

---

## Appendix C: サブスクリプション価格

| プラン | 価格 | 対象ユーザー |
|--------|------|------------|
| Free | 無料 | お試し |
| Pro | $20/月 | 個人開発者 |
| Max (5x) | $100/月 | ヘビーユーザー（API比最大36倍お得） |
| Max (20x) | $200/月 | 高頻度利用（ただし週制限は5xの約2倍） |
| Team | $25/席/月 | チーム |
| Enterprise | カスタム | 大企業（SSO, 監査ログ、利用量は別途API課金） |

> API価格は [Anthropic Console](https://console.anthropic.com) または [[concepts/claude-opus-4-7]] を参照。

---

## 関連ページ

- **[[entities/anthropic]]** — Claudeを開発する企業
- **[[entities/claude-code]]** — AIコーディングエージェント
- **[[claude-code--capabilities]]** — Claude Codeの機能詳細
- **[[entities/claude-design]]** — ビジュアルデザインツール
- **[[claude-managed-agents]]** — エンタープライズエージェントプラットフォーム
- **[[claude-opus-4-7]]** — 最新Opusモデル詳細
- **[[concepts/anthropic-computer-use]]** — GUI操作機能
- **[[concepts/mcp]]** — Model Context Protocol
- **[[concepts/ai-safety-military-governance-claude]]** — 安全性・ガバナンス
- **[[concepts/coding-agents]]** — AIコーディングエージェントエコシステム
- **[[concepts/claude-agent-sdk-orchestration-hooks-subagents-plan-mode-output-styles]]** — Agent SDK
- **[[concepts/claude-memory-tool]]** — メモリツール
