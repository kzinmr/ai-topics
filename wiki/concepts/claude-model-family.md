---
title: "Claude Model Family"
type: concept
aliases:
  - claude
  - Claude AI
  - anthropic-claude
  - claude-models
created: 2026-05-08
updated: 2026-05-08
tags:
  - concept
  - anthropic
  - model-family
  - llm
  - large-language-model
  - ai-agent
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
  - url: "https://arxiv.org/html/2604.14228v1"
    title: "Dive into Claude Code — Design Space of AI Agent Systems"
  - url: "https://www.anthropic.com/research/building-effective-agents"
    title: "Building Effective Agents — Anthropic"
  - url: "https://www.anthropic.com/engineering/harness-design-long-running-apps"
    title: "Harness Design for Long-Running Application Development"
related:
  - "[[anthropic]]"
  - "[[claude-code]]"
  - "[[claude-design]]"
  - "[[claude-managed-agents]]"
  - "[[mcp]]"
  - "[[claude-opus-4-7]]"
  - "[[concepts/anthropic-computer-use]]"
  - "[[concepts/claude-memory-tool]]"
  - "[[concepts/extended-thinking]]"
  - "[[concepts/prompt-caching]]"
  - "[[concepts/claude-agent-sdk-orchestration-hooks-subagents-plan-mode-output-styles]]"
  - "[[concepts/ai-safety-military-governance-claude]]"
  - "[[coding-agents]]"
---

# Claude Model Family

**Claude** は、[[anthropic]] が開発・運用する大規模言語モデル（LLM）ファミリー。Constitutional AI（合憲的AI）を中核的な安全設計思想とし、**Haiku / Sonnet / Opus** の3段階の性能・価格帯で提供される。2023年3月のClaude 1公開から2026年4月のOpus 4.7までに13以上のメジャーバージョンを経て、コーディングエージェント、長時間稼働エージェント、マルチモーダル推論において業界トップクラスの性能を達成している。

本ページは、Claudeモデルファミリー全体の進化、アーキテクチャ哲学、コア機能、APIエコシステム、開発者向けツールチェーンを網羅する。個別製品については各サブページを参照。

---

## モデルファミリーの哲学

Claudeは3階層のモデル設計を採用する。これは、同一世代内で**性能・速度・コストのトレードオフをユーザーが選択できる**設計思想に基づく：

| 階層 | ターゲット | 特徴 |
|------|-----------|------|
| **Haiku** 🏎️ | 超低レイテンシ・軽量タスク | 即時応答、低コスト、分類/抽出/ルーティングに最適 |
| **Sonnet** ⚖️ | 実用的なバランス | コーディング、エージェント、知識業務の主力。多くの本番ワークロードの推奨モデル |
| **Opus** 🧠 | 最高性能・複雑推論 | 最高水準のコーディング・エージェント性能、高難易度推論、長時間計画。フロンティア研究と最重要タスク向け |

**設計原則（Building Effective Agentsより）**：
1. **Simple is best** — 複雑なフレームワークよりも、小さな構成可能なパターンを推奨
2. **Context is all you need** — 豊富なコンテキスト環境が、明示的な決定スキャフォールディング（planner, state graph）より効果的
3. **Deterministic infrastructure over decision scaffolding** — エージェントの98.4%のインフラは決定論的（コンテキスト管理、ツールルーティング、リカバリ）
4. **Unix philosophy** — 「Unixユーティリティのようなもの」：最小構成要素が「有用で理解可能で拡張可能」であることを重視

---

## 全モデルリリースタイムライン

| モデル | リリース日 | 主な新機能・特徴 | ステータス |
|--------|-----------|----------------|-----------|
| **Claude 1** | 2023年3月 | 初の公開モデル。Constitutional AI、約9Kコンテキスト | ❌ 退役 |
| **Claude 1.3** | 2023年7月 | 推論とコード生成改善 | ❌ 退役 |
| **Claude 2** | 2023年7月 | 100Kコンテキスト、推論/コーディング大幅改善、GPT-4と競合 | ❌ 退役 |
| **Claude 2.1** | 2023年11月 | 200Kコンテキスト、幻覚低減、Tool Use（ベータ） | ❌ 退役 |
| **Claude 3 Haiku / Sonnet / Opus** | 2024年3月 | 3階層ファミリー導入。マルチモーダル（画像入力）対応。正しくない拒否率 10%（Claude 2.1の25%から改善） | ❌ 退役 |
| **Claude 3.5 Sonnet** | 2024年6月 | Opus級の性能をSonnet価格で。最高のコーディングモデルと評価 | ❌ 退役 |
| **Claude 3.5 Haiku** | 2024年10月 | スピード/コスト最適化版3.5世代 | ❌ 退役予定 |
| **Claude 3.7 Sonnet** | 2025年2月 | **Extended Thinking** 導入（初の明示的CoT推論モデル）。Claude Code開始 | ❌ 退役予定 |
| **Claude 4 Sonnet / Opus** | 2025年5月 | エージェント時代向け設計。SWE-benchリーダーシップ、Computer Use改善 | ⚠️ 2026年6月15日退役予定 |
| **Claude Sonnet 4.5** | 2025年9月 | SWE-bench Verified 77.2%（当時最高）。30+時間フォーカスウィンドウ | ✅ 現行 |
| **Claude Haiku 4.5** | 2025年10月 | 軽量モデル最新版 | ✅ 現行 |
| **Claude Opus 4.5** | 2025年11月 | コーディング、エージェント、Computer Useで世界最高性能 | ✅ 現行 |
| **Claude Opus 4.6** | 2026年2月5日 | 計画能力向上、長時間エージェントタスク継続、大規模コードベース信頼性 | ✅ 現行 |
| **Claude Sonnet 4.6** | 2026年2月17日 | コーディング、Computer Use、長文脈推論、エージェント計画、知識業務、デザインの全スキルアップグレード | ✅ 現行 |
| **Claude Opus 4.7** | 2026年4月16日 | 高度SE、視覚認識、長期マルチステップタスクで大幅改善。[[claude-design]]対応 | ✅ 現行最新 |

---

## コア技術

### Constitutional AI（合憲的AI）
Anthropicの基盤技術。モデルに明示的な「憲法（Constitution）」を与え、RLHFに代わる原則ベースの調整を行う。
- 人間のフィードバックに依存せず、自己改善ループで安全性を学習
- Claude Opus 4.7ではさらに**Model Spec Midtraining**（pre-trainingとAFTの中間段階で合成Model Spec文書を学習）を導入し、エージェント的誤整列を68%→5%に低減
- 参照: [[concepts/model-spec-midtraining]]

### Extended Thinking（拡張思考）
Claudeが応答前に内部推論ステップを実行する機能。2025年2月のClaude 3.7 Sonnetで初導入。
- 複雑な論理・数学・コーディングタスクの性能を向上
- 推論トークンは別途課金（出力トークン価格に含まれる）
- APIで `thinking` パラメータで制御可能
- [[claude-code]] の「Ultraplan」やSubagent委任で内部的に活用

### Vision & マルチモーダル
Claude 3（2024年3月）で初めて画像入力に対応。現在のOpus 4.7では最高水準の視覚認識を達成。
- 画像・チャート・グラフ・PowerPointスライド・技術図面の解析
- テキスト埋め込み画像の文字起こし
- 複数画像の比較・合成分析
- [[concepts/multimodal]] 参照

### Computer Use（ベータ）
Claudeがスクリーンショットを通じてデスクトップGUIを直接操作する機能。
- クリック、キー入力、スクロールなど人間と同等の操作方法
- 2024年10月研究プレビュー → 2026年2月Vercept買収で機能強化
- 詳細: [[anthropic-computer-use]]

---

## APIエコシステム

### Messages API（標準API）
Anthropicの主要APIエンドポイント。全Claudeモデルに統一インターフェースを提供。
- **コンテキストウィンドウ**: 最大200Kトークン（全現行モデル共通）
- **最大出力**: 最大64Kトークン（Opus 4.7, Sonnet 4.6）
- **ストリーミング**: サーバー送信イベント（SSE）によるリアルタイム出力
- **マルチターン会話**: メッセージリストによる会話履歴管理

### Tool Use（関数呼び出し）
Claudeが外部APIやローカルツールと対話するための標準機能（2023年11月Claude 2.1でベータ導入、2024年3月GA）。
- **標準ツール**: Bash実行、ファイル編集、テキストエディタ、コード実行、Web検索
- **カスタムツール**: JSONスキーマで定義した任意の外部API呼び出し
- **MCP統合**: [[mcp]] 対応ツールサーバーとの接続
- **並列ツール呼び出し**: 複数ツールの同時実行

### Structured Output（構造化出力）
モデルの出力を確実にJSONスキーマに従わせる機能。
- JSONモード：バリデーション保証付きでスキーマ準拠を担保
- エージェント制御の信頼性向上、後続処理のパース不要に
- 参照: [[concepts/claude-code-prompt-engineering-context-management-caching-agent-architecture]]

### Prompt Caching（プロンプトキャッシング）
頻繁に送信される大きなコンテキスト（システムプロンプト、長文書、コードベース概要）を再利用してコストとレイテンシを削減。
- キャッシュ書き込みコスト：標準入力の1.25倍
- キャッシュ読み取りコスト：標準入力の10%（5分間有効）
- Sonnet 4.6の場合：$3/MTok（標準）→ $0.30/MTok（キャッシュヒット）

### Batch Processing
非同期バッチAPIによる大量リクエスト処理。全トークンコストが50%削減。
- 24時間以内の処理完了
- 同一モデル・同一パラメータのリクエストをバッチ化
- 大規模Evalやオフライン分析に最適

---

## 価格体系

### サブスクリプション（Claude.ai）

| プラン | 価格 | 主な特徴 |
|--------|------|---------|
| **Free** | 無料 | 制限付きアクセス、標準モデル、ピーク時優先度低 |
| **Pro** | $20/月 | 拡張アクセス、新機能優先利用 |
| **Max (5x)** | $100/月 | プロユーザー向け。APIより最大36倍お得（キャッシュ読み取り無料効果） |
| **Max (20x)** | $200/月 | 高頻度利用者向け。ただし週間制限は5xの約2倍 |
| **Team** | $25/席/月 | チーム管理、共有ワークスペース |
| **Enterprise** | カスタム | SSO、監査ログ、APIレート高、ただし利用量は別途API課金 |

### API価格（2026年5月現在）

| モデル | 入力 ($/1M トークン) | 出力 ($/1M トークン) |
|--------|---------------------|---------------------|
| Opus 4.7 | $5.00 | $25.00 |
| Sonnet 4.6 | $3.00 | $15.00 |
| Haiku 4.5 | $1.00 | $5.00 |

- **バッチ処理**: 全価格50%オフ
- **プロンプトキャッシング**: キャッシュ書き込み +25%、キャッシュ読み取り -90%
- **Extended Thinking**: 推論トークンは出力トークン価格で課金

---

## エコシステムと主要製品

### Claude.ai（Web/モバイル）
公式チャットインターフェース。サブスクリプションで利用可能。
- プロジェクト機能（カスタム指示 + 知識ベース）
- ファイルアップロード（画像、PDF、コード）
- 長文書分析（最大200Kトークン）
- 1クリック音声入力・出力

### [[claude-code]]
AnthropicのAIコーディングエージェント。CLI、Desktop、VS Code/JetBrains拡張、Web、iOS、Slackのマルチサーフェス。
- SWE-bench Verified: 72.7%
- 導入企業のデプロイ頻度: 7.6倍向上
- 詳細は専用エンティティページ参照

### [[claude-design]]
Anthropic Labsのビジュアルデザインコラボレーションツール（2026年4月研究プレビュー）。
- Claude Opus 4.7の視覚モデル搭載
- デザイン生成・編集・反復を会話ベースで

### [[claude-managed-agents]]
エンタープライズ向けマネージドエージェントプラットフォーム（2026年4月パブリックベータ）。
- メモリストア（ファイルベース永続化）
- マルチエージェントオーケストレーション（コーディネータ + 20 Subagent）
- Outcomes Loop（ルーブリック駆動のGrader評価）
- Dreams（メモリキュレーション）, Webhook通知

### [[mcp]] — Model Context Protocol
Anthropicが開発したAIエージェント↔ツール間のオープン規格（"USB-C for AI"）。
- OpenAI/Google/Microsoft/Red Hatが採用
- MCP Apps（インタラクティブUI拡張）対応
- 詳細は専用コンセプトページ参照

### Claude Agent SDK
Node.js SDK (`@anthropic-ai/claude-agent-sdk`) でClaudeのエージェント機能をプログラム的に構築。
- Hooks: エージェントライフサイクルフック（before_tool, after_tool, on_error）
- Subagents: 子エージェントの生成と結果収集
- Plan Mode: 実行前に計画を生成・承認
- Output Styles: 構造化出力のスタイル指定
- MCP統合：ビルトインMCPサーバー対応

---

## 開発者向けリソース

| リソース | 説明 | リンク |
|---------|------|--------|
| **Anthropic Console** | APIキー管理、利用状況モニタリング、Evalツール | [console.anthropic.com](https://console.anthropic.com) |
| **APIリファレンス** | 全エンドポイント・パラメータ詳細 | [docs.anthropic.com](https://docs.anthropic.com/en/api/skills-guide) |
| **Developer Docs** | 完全な技術ドキュメント | [docs.anthropic.com/en/home](https://docs.anthropic.com/en/home) |
| **Anthropic Cookbook** | 一般的なワークフローのコードスニペット集 | [GitHub](https://github.com/anthropics/anthropic-cookbook) |
| **Anthropic Quickstarts** | プリビルドのアプリケーションテンプレート | [GitHub](https://github.com/anthropics/anthropic-quickstarts) |
| **Prompt Generator** | 自動プロンプト生成ツール | [docs.anthropic.com](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-generator) |
| **Prompt Engineering Tutorial** | 対話型プロンプトエンジニアリング学習 | [GitHub](https://github.com/anthropics/courses/blob/master/prompt_engineering_interactive_tutorial/README.md) |
| **Tool Use Course** | 関数呼び出しのハンズオンコース | [GitHub](https://github.com/anthropics/courses/blob/master/tool_use/README.md) |
| **Building Effective Agents** | エージェント設計の原則 | [anthropic.com](https://www.anthropic.com/research/building-effective-agents) |

---

## 競合比較

| 特徴 | Claude | GPT-4o / o-series | Gemini | DeepSeek |
|------|--------|-------------------|--------|----------|
| 設計思想 | Constitutional AI + 安全優先 | 汎用性能最優先 | Googleエコシステム統合 | オープンウェイト + 極限効率 |
| モデル階層 | Haiku/Sonnet/Opus (3層) | GPT-4o/o1/o3 (特殊化) | Flash/Pro/Ultra (3層) | V4 Pro/Flash (2層) |
| コンテキスト | 200K tokens | 128K-200K | 1M-2M | 128K-1M (V4 Flash 1M) |
| エージェント機能 | MCP, Tool Use, Extended Thinking, Computer Use | Function Calling, o-series reasoning | Tool Use, Search Grounding | Basic function calling |
| 特筆すべき強み | コーディング品質、安全性、長時間エージェント | マルチモーダル、バランス性能 | 超長文脈、Google連携 | コスト効率（オープンウェイト） |

---

## 関連ページ

- **[[anthropic]]** — Claudeを開発する企業
- **[[claude-code]]** — AIコーディングエージェント（エンティティ）
- **[[claude-code--capabilities]]** — Claude Codeの機能詳細
- **[[claude-design]]** — ビジュアルデザインツール
- **[[claude-managed-agents]]** — エンタープライズエージェントプラットフォーム
- **[[claude-opus-4-7]]** — 最新Opusモデル詳細
- **[[concepts/anthropic-computer-use]]** — GUI操作機能
- **[[mcp]]** — Model Context Protocol
- **[[concepts/ai-safety-military-governance-claude]]** — 安全性・ガバナンス
- **[[coding-agents]]** — AIコーディングエージェントエコシステム全体
- **[[concepts/claude-agent-sdk-orchestration-hooks-subagents-plan-mode-output-styles]]** — Agent SDK
- **[[concepts/claude-memory-tool]]** — メモリツール
- **[[concepts/claude-code-prompt-engineering-context-management-caching-agent-architecture]]** — Claude Codeの技術プラクティス
- **[[concepts/claude-sonnet-4.6]]** — Sonnet 4.6詳細
- **[[concepts/claude-opus-4-6]]** — Opus 4.6詳細
