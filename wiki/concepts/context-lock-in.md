---
title: "Context Lock-In — AIの第三フェーズ競争"
type: concept
created: 2026-05-19
updated: 2026-05-19
tags:
  - enterprise-ai
  - context-management
  - vendor-lock-in
  - platform-economics
  - ai-agents
aliases:
  - "context-lock-in"
  - "文脈ロックイン"
  - "context lock-in"
  - "context lockin"
sources:
  - raw/articles/2026-05-17_rent-intelligence-own-context.md
  - https://x.com/i/article/2056142316713472000
related:
  - "[[concepts/contextmaxxing]]"
  - "[[concepts/tokenmaxxing]]"
  - "[[concepts/enterprise-ai-operating-model]]"
  - "[[concepts/enterprise-ai-deployment-jv]]"
  - "[[concepts/context-graph]]"
  - "[[entities/ashwingop]]"
  - "[[entities/sentra-app]]"
---

# Context Lock-In — AIの第三フェーズ競争

> *"Rent the Intelligence. Own the Context."* — Ashwin Gopinath, "Rent the Intelligence. Own the Context." (May 2026)

**Context Lock-In**（文脈ロックイン）は、[[entities/ashwingop|Ashwin Gopinath]]が提唱する概念で、企業向けAI導入における最も危険な依存形態を指す。モデルロックイン（単一モデルプロバイダーへの依存）が「面倒だが乗り換え可能」なのに対し、Context Lock-Inは「企業の作業記憶を他者のOSから引き剥がす」レベルの構造的依存である。

## 三つのフェーズ：AI競争の進化

GopinathはAI競争を3つのフェーズに分類する：

| フェーズ | 競争軸 | 収束性 | 例 |
|---------|--------|--------|-----|
| **Phase 1: モデル品質** | ベンチマーク性能、推論能力 | 収束しつつある | GPT-5, Claude, Gemini, Qwen |
| **Phase 2: エージェント層** | 計画、ツール使用、Eval、権限、UI | 収束する（模倣可能） | Claudeの agentic system, Codex, Gemini Agent |
| **Phase 3: コンテキスト** | 企業固有の作業記憶、意思決定履歴、約束、例外 | **収束しない（企業固有）** | MCP, Sentra, 企業内知識グラフ |

> Phase 1と2は「良いパターンは全ベンダーが模倣する」ため収束する。Phase 3のみが収束しない。なぜなら「顧客への約束、ロードマップ上の対立、サポートエスカレーション、Slackでの議論、価格例外、失敗したマイグレーション、会議の根拠、オーナー履歴、決定の傷跡」はモデルの重みには存在せず、その企業にしかないものだからだ。

## モデルロックイン vs コンテキストロックイン

| 次元 | モデルロックイン | コンテキストロックイン |
|------|----------------|---------------------|
| **依存対象** | API呼び出し先 | エージェント層＋ワークフロー＋記憶 |
| **乗り換えコスト** | API切り替え（概念的には単純） | 企業の作業記憶の移行（OS移行レベル） |
| **可視性** | 高い（データベース、ファイル形式） | 低い（ワークフロー痕跡、プロンプト慣習、埋め込み） |
| **時間軸** | 即時的 | 6ヶ月〜2年で不可逆的に深化 |
| **危険な錯覚** | N/A | 「システムが賢くなっている」＝ロックインの深化 |

## なぜモデルロックインより危険か

### 1. 不可視の依存

古いソフトウェアのロックインは可視的だった：データベース、ファイル形式、ライセンス契約。AIの文脈ロックインは「クラウド状」— ワークフロー痕跡、記憶された好み、ツール履歴、Evalセット、プロンプト規約、埋め込み、権限、エージェント行動の集積。最初は「システムが改善している」ように感じられる。

### 2. MCPの両義性

Anthropicの Model Context Protocol (MCP) は「AIアシスタントをデータが存在するシステムに接続する標準」として多くの企業が今経験している「MCPモーメント」を生んでいる。しかし Gopinath はこれを「クエリ時再構成は記憶ではない」と警告する：

> ユーザーが質問した時に5つのツールから情報を引っ張ることは有用だが、企業が長期にわたって所有・維持する**永続的コンテキストグラフ**と同じではない。なぜ決定が変更されたか、どの約束が失効したか、どの試みが失敗したか、どのオーナーが静かに変わったかを保存しない。**記憶の感覚を作り出すが、実際の記憶を構築する前の段階**である。

### 3. フォワードデプロイメントの二面性

OpenAI Deployment Company（$4B投資、Tomoro買収）と Anthropic AI Services（Blackstone、Hellman & Friedman、Goldman Sachsとの合弁）は「フォワードデプロイメント」モデルを採用している。Palantirが証明したように、このモデルは実際の顧客運用環境を学習することで真の価値を生む。しかし同じメカニズムが依存も生む：

- フォワードデプロイされたチームは「奇妙なワークフロー、非公式プロセス、壊れやすいスプレッドシート、隠れたオーナー、例外パス、システム記録が間違っている理由、実際の決定が行われる会議」を学ぶ
- その知識がベンダーのエージェントと記憶層にエンコードされると、ベンダーは単にサービスを提供しているのではなく、**企業の運用記憶そのもの**になる

## アーキテクチャの正解：「知能はレンタル、コンテキストは所有」

Gopinathの提案する正しいアーキテクチャ：

```
┌──────────────────────────────────────────────┐
│              任意のモデルプロバイダー            │
│   OpenAI  ·  Anthropic  ·  Gemini  ·  OSS     │
│         「知能はレンタル」                        │
└──────────────────┬───────────────────────────┘
                   │
┌──────────────────▼───────────────────────────┐
│         ニュートラルなコンテキスト層              │
│    「企業の作業記憶」— 検査可能・権限付き・移植可能  │
│    上：ソースシステム（Slack, Jira, Salesforce...）│
│    下：エージェント層                             │
│    知っているべきこと：何が起きたか、証拠はどこか、  │
│    誰が閲覧可能か、何が変わったか、何が約束されたか、│
│    誰がオーナーか、どのオントロジーが適用されるか     │
└──────────────────────────────────────────────┘
```

> 「企業の記憶層は、モデルとエージェントハーネスを所有するのと同じベンダーが管理するブラックボックスであってはならない。企業が管理しなければならない。検査可能、権限付き、移植可能、転送可能でなければならない。」

## 構造的教訓：Microsoft アナロジー

GopinathはMicrosoft独禁法訴訟（DOJがOSの力をブラウザ市場に拡張する排他的行為を主張）を引用するが、教訓は法的ではなく**構造的**だ：

- プラットフォーム企業は支配点から隣接層へと水平展開するインセンティブを持つ（資本主義の論理として当然）
- 全員が依存する層を支配すれば、それをバンドルし、誘導し、デフォルトにし、周辺層を吸収するあらゆる理由がある
- AIではこれが古いソフトウェアより危険：ロックインが「クラウド状」で不可視

## Chamath Palihapitiyaのトークンコントロール論への応答

Chamathは「トークン制御（8090のSoftware Factoryがトークン生成を制御し任意のモデルにルーティングできる）」が重要だと主張した。Gopinathは「正しい危険を指しているが、本質はトークンより深い」と応答する：

- トークンルーティングは価格・レイテンシ・能力・可用性の交渉力を与える
- しかしコンテキスト層が単一ベンダーに閉じ込められているなら、トークンルーティングだけでは不十分
- 「任意のモデルにプロンプトを送れる」ことと「任意のモデルがあなたの会社を理解できる」ことは別
- 真の価値は「コンテキストパック」：どの顧客約束が重要か、どのSlackスレッドが決定を変えたか、どのJiraチケットが陳腐化しているか

## 24〜36ヶ月の予測

> 「まともなモデル＋まともなエージェント＋優れた企業コンテキスト」が「フロンティアモデル＋より良いエージェント＋浅いコンテキスト」に勝つ。

| 領域 | コンテキストがモデル品質より重要な理由 |
|------|--------------------------------------|
| **営業** | 最後の約束を知っていること ＞ 賢く聞こえること |
| **サポート** | アカウント履歴を知っていること ＞ 文の品質 |
| **エンジニアリング** | 過去の失敗したマイグレーションを知っていること ＞ ベンチマーク1ポイント |
| **ファイナンス** | 現在の例外とオーナーを知っていること ＞ 一般的な会計知識 |

## Graph Structure Query

```
[context-lock-in] ──author──→ [entity: ashwingop]
[context-lock-in] ──extends──→ [concept: contextmaxxing]
[context-lock-in] ──contrasts──→ [concept: tokenmaxxing]
[context-lock-in] ──relates-to──→ [concept: enterprise-ai-deployment-jv]
[context-lock-in] ──relates-to──→ [concept: context-graph]
[context-lock-in] ──embodies──→ [concept: platform-economics]
[context-lock-in] ──references──→ [entity: sentra-app]
```

> This section informs graph queries: authored by [[entities/ashwingop]], extends [[concepts/contextmaxxing]] with the competitive-dynamics dimension, contrasts with the token-level framing of [[concepts/tokenmaxxing]], relates to [[concepts/enterprise-ai-deployment-jv]] (OpenAI/Anthropic forward-deployment), and is embodied by [[entities/sentra-app]] as the neutral context layer implementation.

## Implementation: Sentra.app

Gopinathの Sentra.app（a16z Speedrun + Together Fund、$5M Seed）は、この「所有されたコンテキスト層」の参照実装である。「Company Brain」として全てのコミュニケーションチャネル、知識ベース、アクション・エージェント痕跡の上に座り、組織全体の「生きた世界モデル」をほぼリアルタイムで構築する。

## Related Concepts

- [[concepts/contextmaxxing]] — アーキテクチャ的基盤：より良い記憶 ＞ トークン消費。Context Lock-Inはこれが失敗した時の帰結
- [[concepts/tokenmaxxing]] — 対比：トークン消費の最適化は第一の制御面だが、第二（コンテキスト）には届かない
- [[concepts/enterprise-ai-deployment-jv]] — OpenAI Deployment Company と Anthropic AI Services の詳細
- [[concepts/context-graph]] — コンテキストロックインを防ぐ技術的基盤
- [[concepts/enterprise-ai-operating-model]] — 企業AI運用モデル全体の中での位置づけ

## Sources

- [Rent the Intelligence. Own the Context.](https://x.com/i/article/2056142316713472000) — Ashwin Gopinath, X Article (May 17, 2026)
- [[raw/articles/2026-05-17_rent-intelligence-own-context.md]] — Full raw article
