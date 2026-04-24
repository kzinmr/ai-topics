---
title: "AI Memory Systems — ChatGPT vs Claude vs Cognition"
type: concept
aliases:
  - ai-memory-systems
  - chatgpt-memory
  - claude-memory
  - agent-memory-architecture
created: 2026-04-13
updated: 2026-04-13
tags:
  - concept
  - memory
  - context-engineering
  - agent-architecture
status: draft
sources: []
---

# AI Memory Systems — ChatGPT vs Claude vs Cognition

AIアシスタント・エージェントにおける「メモリ（記憶）」システムの設計哲学の比較。OpenAI、Anthropic、Cognition（Devin）がそれぞれ異なるアプローチを採用しており、これは製品ターゲット（コンシューマー vs 技術者）とアーキテクチャ思想（自動 vs 明示的）の違いを反映している。

出典: [Shlok Khemani - ChatGPT Memory and the Bitter Lesson](https://www.shloked.com/writing/chatgpt-memory-bitter-lesson), [Claude Memory: A Different Philosophy](https://www.shloked.com/writing/claude-memory), [Anthropic's Opinionated Memory Bet](https://www.shloked.com/writing/claude-memory-tool)

---

## ChatGPT Memory: 4つのメモリバケット + Bitter Lesson戦略

### アーキテクチャ

ChatGPTは毎ターン、システムプロンプトに**4つのデータバケット**を注入する:

| コンポーネント | 説明 | 更新頻度 | ユーザー可視 |
|---|---|---|---|
| **1. Interaction Metadata** | デバイス仕様、使用パターン（トピック比率、平均メッセージ長、会話深度、モデル使用比率、セッションアクティビティ、アカウント年齢、サブスクリプション層、推定地理位置） | リアルタイム | ❌ |
| **2. Recent Conversation Context** | 最新の約40会話のトピックタグ付きタイムスタンプログ（ユーザーメッセージのみ、アシスタント応答はトークン節約のため省略） | リアルタイム | ❌ |
| **3. Model Set Context** | ユーザーが明示的に提供したメモリ（例: 「甲殻類アレルギー」）。上書きレイヤーとして機能 | 随時（ユーザー編集可） | ✅ |
| **4. User Knowledge Memories** | AIが会話履歴から生成した要約（約10段落）。最初の3つは職業/技術的生活、最後の2つはChatGPT使用習慣 | 2〜3日周期 | ❌ |

### LLMトレーニングとのアナロジー

| メモリコンポーネント | LLM相当 | 機能 |
|---|---|---|
| User Knowledge Memories | Pretrained Base Model | 密で重みのある知識。経年劣化するがコアパターンを保持 |
| Model Set Context | RLHF / Fine-tuning | 古いベース知識を上書きする明示的な修正 |
| Recent Conversation Context | In-Context Learning | 即時の行動を形成するセッション固有の例 |
| Interaction Metadata | System Defaults / Environment | ルーティングとフォーマットを暗黙的に誘導 |

### "Bitter Lesson"戦略

OpenAIは複雑な検索アーキテクチャを意図的に回避している。**RAGなし、ベクターDBなし、ナレッジグラフなし。** 代わりに、すべてのメモリコンポーネントを毎ターンコンテキストウィンドウに注入する。

**2つの前提:**
1. **モデルの知能 > 検索エンジニアリング:** LLMは数千トークンを解析し、無関係なコンテキストを無視できるほど賢い
2. **コンテキスト規模 + コストデフレーション:** 総当たりの注入は今は無駄に見えるが、コンテキストウィンドウの拡大と計算コストの低下により自明になる

---

## Claude Memory: 明示的・オンデマンドツール

### アーキテクチャ

ClaudeはChatGPTと**根本的に反対**のメモリ哲学を採用:

- **ブランクスレート初期化:** 会話ごとにゼロから開始。事前読み込みされたプロファイルや履歴なし
- **明示的起動のみ:** 「何について話したっけ」「続きから」といったプロンプトでのみ活性化
- **生履歴検索:** AI生成の要約や圧縮プロファイルは使用しない。実際の過去の会話をリアルタイムで検索
- **可視ツール実行:** ユーザーは検索ツールの起動と意図的な遅延を確認できる

### 検索ツール仕様

| ツール | 機能 | パラメータ |
|---|---|---|
| `conversation_search` | キーワード/トピックベースの全履歴検索。マルチトピッククエリは順次実行 | `query` (必須), `max_results` (1-10, デフォルト5) |
| `recent_chats` | 時間ベースのアクセス、カーソルページネーション | `n` (1-20, デフォルト3), `sort_order` (asc/desc), `before`, `after` |

---

## Claude Memory Tool: ファイルベースのネイティブメモリ

Anthropicは**ファイルベースのメモリツール**をネイティブ提供し、モデルプロバイダーとしてメモリに対する最初のオピニオンを表明した。

### 6つの操作インターフェース

`view` | `create` | `str_replace` | `insert` | `delete` | `rename`

### 責任の分離

1. **ストレージ（開発者）:** ファイル形式（JSON/XML/テキスト）、場所（ローカル/S3/暗号化）、セキュリティ/アクセス制御
2. **ストラテジー（システムプロンプト）:** メモリ構造、保持ポリシー、使用ルールをガイド。カスタムパーサーや抽出ロジックは不要

### Anthropicの4つの戦略的ベット

| ベット | 根拠 | トレードオフ |
|---|---|---|
| **1. メモリ統一** | 検索、保存、会話を単一の推論フローに統合 | 高い遅延・コスト（〜3 LLM呼び出し/インタラクション） |
| **2. ファイル > データベース** | 非構造化ファイルでダイナミックスキーマ進化を可能に | 構造強制にはプロンプトエンジニアリングが必要 |
| **3. 検索関数なし** | `view`はディレクトリ一覧、Claudeはファイル全体を読む。「もうコンテキストが多すぎることはない」 | トークンコスト増。洞察vs費用の权衡 |
| **4. メモリ超え** | ファイルはエージェントの汎用コンテキスト管理（エージェント間通信、タスクワークスペース、自己改善） | ファイルを「作業メモリの拡張」として位置づけるシフト |

---

## Cognition (Devin): ファイルシステムをメモリとして使う

CognitionチームはClaude Sonnet 4.5をDevinに統合する過程で、モデルが**ファイルシステムをメモリとして扱う**ことを発見した。

### 主な発見

- Sonnet 4.5はプロンプトなしで自発的にファイル（CHANGELOG.md, SUMMARY.md）を書き、状態を外部化する
- この行動はコンテキストウィンドウの終端に近づくほど顕著になる
- Cognitionは当初、独自メモリ管理を削除してモデルの自己外部化に任せる可能性を探った
- しかし、モデル生成の要約は不完全で、本番利用にはパフォーマンス低下を招いた
- **結論:** 明示的なメモリシステムとモデルの外部化行動のハイブリッドが必要

### Context Window Anxiety

Sonnet 4.5は自分のコンテキストウィンドウを「認識」しており、制限に近づくと:
- 進捗を自発的に要約し始める
- タスクを完了させるために決断的になる
- ショートカットを取ったり、タスクを不完全に放置したりする
- 常に残りのトークンを過小評価する（しかも驚くほど正確に）

Cognitionのハック: 1Mトークンコンテキストを有効にしつつ、実際の使用を200Kにキャップする。モデルに「余裕がある」と思わせ、不安駆動のショートカットを防ぐ。

---

## 比較マトリクス

| 次元 | ChatGPT | Claude (Web) | Claude (Memory Tool) | Cognition Devin |
|---|---|---|---|---|
| ターゲット | 一般コンシューマー | 技術者/プロフェッショナル | 開発者/エージェントビルダー | エンタープライズSWE |
| 起動 | 常時自動 | 明示的トリガー | 明示的トリガー（ファイル操作） | 自律的 |
| データ形式 | AI生成プロファイル | 生会話履歴 | ファイル（JSON/XML/テキスト） | ファイルシステム |
| 検索 | なし（総注入） | キーワード検索 | ディレクトリ走査+全文 | ハイブリッド |
| ストレージ責任 | OpenAI | Anthropic | 開発者 | Cognition |
| メモリ更新 | 2〜3日周期 | リアルタイム検索 | 会話中随時 | 自律的要約 |
| トークン戦略 | 総当たり注入 | オンデマンド読み取り | ファイル全体読み取り | 外部化+ハイブリッド |

## 関連概念

- [[context-engineering]] — コンテキストエンジニアリング
- [[context-window-management]] — コンテキストウィンドウの戦略的管理
- [[context-compaction]] — コンテキスト圧縮メカニズム
- [[context-anxiety]] — コンテキスト不安現象
- [[harness-engineering]] — エージェント制御・構造化
- [[concepts/harness-engineering/agentic-engineering.md]] — エージェント活用開発

## 更新履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-13 | 初期作成 — Shlok Khemaniの記事3本 + Cognition Sonnet 4.5記事を統合 |
