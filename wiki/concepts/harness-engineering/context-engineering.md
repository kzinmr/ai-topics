---
title: "Context Engineering — コンテキスト最適化の統合フレームワーク"
type: concept
aliases:
  - context-engineering
  - コンテキストエンジニアリング
created: 2026-04-13
updated: 2026-05-13
tags:
  - concept
  - harness-engineering
  - context-management
  - prompting
  - optimization
status: active
sources:
  - "OpenAI Cookbook — Context engineering patterns"
  - "Andrej Karpathy, X/Twitter, June 25, 2025"
  - "Anthropic — Effective context engineering for AI agents"
  - "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines (Khattab et al., 2023)"
  - "Khairallah AL-Awady — How to Master Context Engineering & Build AI Systems That Actually Understand You (Full Course), May 2026"
  - "[[raw/articles/2025-06-23_rlancemartin_context-engineering-for-agents]] — Lance Martin, Context Engineering for Agents (Write/Select/Compress/Isolate), June 2025"
  - "[[raw/articles/2026-01-09_rlancemartin_agent-design-patterns]] — Lance Martin, Agent design patterns (7 patterns extending context engineering), Jan 2026"
  - "[[raw/articles/2026-05-13_anthropic_claude-code-agent-sdk-sessions]] — Anthropic, Work with sessions (Claude Code Agent SDK), 2026"
---

# Context Engineering

コンテキストウィンドウを効果的に活用し、LLMの性能を最大化する体系的アプローチ。**Harness Engineeringの横断技術コンポーネント**として位置づけられる。

> "Context engineering is the delicate art and science of filling the context window with just the right information for the next step." — Andrej Karpathy

> "Building with language models is becoming less about finding the right words and phrases for your prompts, and more about answering the broader question of 'what configuration of context is most likely to generate our model's desired behavior?'" — Anthropic

## Harness Engineeringとの関係

| レイヤー | 概念 | 焦点 |
|---------|------|------|
| **最上位** | Harness Engineering | Agent = Model + Harness（環境設計哲学） |
| **横断技術** | Context Engineering | コンテキストの選択・圧縮・配置（有限リソース管理） |
| **応用（人間側）** | Agentic Engineering | 開発者がエージェントを「活用する」パターン |
| **応用（システム側）** | AI Agent Engineering | エージェントを「構築する」パターン |

Context EngineeringはHarness Engineeringの**サブコンポーネント** — 「エージェントに何を見せ、何を隠すか」の設計の中で、特にコンテキストウィンドウの最適化を扱う。

## Karpathyによる定義とSoftware 3.0

Karpathyは「Software 2.0」（2017年）において、ニューラルネットワークを「最適可能なパラメータ」として扱うパラダイムシフトを提唱。この考え方はLLM時代の「コンテキストエンジニアリング」に直接接続している：

| パラダイム | プログラミング対象 | 最適化手法 |
|------------|-------------------|-----------|
| Software 1.0 | 明示的なコード（Python, C++等） | 手書きロジック |
| Software 2.0 | ニューラルネットワーク重み | 勾配降下法 |
| Software 3.0 | LLMへのプロンプト/コンテキスト | コンテキストエンジニアリング |

### Autoresearchとの関係
Karpathyのautoresearch（2026年3月）：
1. 不変の評価器（prepare.py）を固定
2. エージェントが1つの編集可能なファイル（train.py）を変更
3. 一晩中実行し、改善を保持、後退を破棄

このパターンはDSPyの「プロンプトをハイパーパラメータとして最適化」と構造的に同一。

## DSPyとの関係性

DSPy（Declarative Self-improving Python）は、プロンプトを学習パラメータとして扱い、最適化によって自動的に改善するフレームワーク：

| 観点 | KarpathyのContext Engineering | DSPy |
|------|------------------------------|------|
| 焦点 | コンテキスト全体の設計 | プロンプトの最適化 |
| 手法 | 情報の選択・整理・圧縮 | 宣言的プログラミング・コンパイル |
| 目的 | LLMの性能最大化 | 自己改善パイプライン |
| パラダイム | Software 3.0 | Software 2.0の延長 |

DSPyの最適化パターン：
- **MIPROv2**: ベイズ最適化によるプロンプト改善
- **BootstrapFewShot**: 自己生成によるデモ例の最適化
- **GEPA**: 反映的進化によるプロンプト最適化

## Anthropic: Context Engineering vs Prompt Engineering

| 次元 | Prompt Engineering | Context Engineering |
|------|-------------------|---------------------|
| 焦点 | 最適なシステムプロンプトの作成（1ショット） | 推論中に渡される**すべてのトークン**の反復的・包括的管理 |
| スコープ | システム指示 | システム指示、ツール、MCP、外部データ、メッセージ履歴 |
| 性質 | 離散的タスク指向 | 継続的・循環的キュレーション |

### Attention Budgetの制約
Transformerアーキテクチャは `n²` のペアワイズ関係を必要とする：
- **Context Rot**: コンテキスト長が増すにつれ、LLMのリコール精度が勾配上に劣化
- **Position Encoding Interpolation**: より長いシーケンスを可能にするが、トークン位置理解が劣化

### コンポーネント別ベストプラクティス

| コンポーネント | ベストプラクティス |
|--------------|-------------------|
| **システムプロンプト** | 「ゴールディロックスゾーン」をターゲット — 具体的すぎず、曖昧すぎず |
| **ツール** | 自己完結型、トークン効率、明確なコントラクト |
| **Few-Shot例** | 多様で標準的な例をキュレーション。エッジケースのダンプを避ける |
| **外部データ** | JIT読み込み — 必要なときに段階的に発見 |
| **メッセージ履歴** | コンパクション — 反復的ツール呼び出しを削除、決定を保持 |

## Core Techniques

### 1. Context Compression
- 冗長な情報の削除
- 重要な事実の抽出と要約
- キーワード/エンティティの優先順位付け

### 2. Context Ordering
- 重要な情報を最初と最後に配置（recency/primacy effect）
- 関連する情報をグループ化
- 時系列または論理構造で整理

### 3. Dynamic Context Management
- タスクの複雑さに応じたコンテキスト量の調整
- 不要な情報の動的排除
- コンテキスト使用量の監視と最適化

### 4. Context Chunking
- large documentsを意味のあるチャンクに分割
- 各チャンクにメタデータを付加
- 必要に応じてチャンクを組み合わせ

## 3つの戦略的アプローチ（Anthropic）

### 1. Compaction（圧縮）
コンテキストウィンドウの限界に近づいたとき、会話を要約して再開。
- **保持すべき**: アーキテクチャ上の決定、未解決のバグ、実装の詳細
- **破棄すべき**: 冗長なツール呼び出し/結果、中間思考

### 2. Structured Note-Taking（構造化メモ）
コンテキストウィンドウ外に永続メモを保持し、必要に応じて再度読み込む。
- 数千ステップにわたる追跡を可能にする
- Claude Sonnet 4.5にはファイルベースのメモリツールが含まれる

### 3. Sub-Agent Architectures（サブエージェント）
メインエージェントが高レベル計画を調整。専門化されたサブエージェントがクリーンなコンテキストで焦点を絞ったタスクを処理。
- サブエージェントは凝縮された要約（〜1,000–2,000トークン）を返す

## Lance Martin: Write / Select / Compress / Isolate の4バケット分類

Lance Martin（[[entities/lance-martin]]）はAnthropicの3戦略を拡張し、Context Engineeringの技術を**Write, Select, Compress, Isolate**の4バケットに分類した（[Context Engineering for Agents](https://rlancemartin.github.io/2025/06/23/context_engineering/), June 2025）。この分類は、AnthropicのCompaction/Structured Note-Taking/Sub-Agentと構造的に対応しつつ、より細分化されたフレームワークを提供する。

### 4バケットの全体像

| バケット | 定義 | Anthropic対応 | 主なテクニック |
|---------|------|--------------|--------------|
| **Write** | コンテキストウィンドウの外に情報を保存する | Structured Note-Taking | スクラッチパッド、長期記憶（Reflexion, Generative Agents）、CLAUDE.md / Cursor Rules |
| **Select** | 必要な情報をコンテキストウィンドウに取り込む | —（新規） | メモリ検索（埋め込み+知識グラフ）、ツール選択RAG、意味検索 |
| **Compress** | 必要なトークンだけを保持する | Compaction | 要約（再帰的/階層的）、トリミング、fine-tuned pruning（Provence） |
| **Isolate** | コンテキストを分割して管理する | Sub-Agent Architectures | マルチエージェント、コードエージェント+サンドボックス、Stateオブジェクト分離 |

### Write（コンテキストの外部保存）

**スクラッチパッド**: AnthropicのThink Toolのように、エージェントがタスク実行中に情報をファイルやStateオブジェクトに書き出す。Claude Codeのauto-compact前に計画をMemoryに保存するパターンが典型。

**記憶（Memories）**: セッションを超えて持続する知識。
- **Reflexion**（Shinn et al., 2023）: 各ターンの反射を生成し、自己生成記憶として再利用
- **Generative Agents**（Park et al., 2023）: 過去のフィードバックから定期的に記憶を合成
- **製品実装**: ChatGPT Memory, Cursor Memories, Windsurf Memories — ユーザーとの対話から長期記憶を自動生成

### Select（コンテキストの選択的取り込み）

**ツール選択のRAG化**: ツール数が増えるとツール説明の重複によりモデルが混乱。ツール説明にRAGを適用し、タスクに関連するツールのみを意味検索で取得。3倍の精度向上が報告されている（arXiv:2505.03275, 2025）。

**コードエージェントにおける知識選択**: WindsurfのVarunによる実践的洞察：
> "Indexing code ≠ context retrieval … embedding searchはコードベースが大きくなるにつれ検索ヒューリスティックとして信頼性を失う。grep/file search、知識グラフベース検索、リランキングの組み合わせが必要"

**メモリ選択の課題**: Simon WillisonがAIEngineer World's Fairで報告 — ChatGPTが位置情報をMemoryから意図せず取得し画像生成に注入。不要な記憶検索はユーザーに「コンテキストウィンドウがもはや自分のものではない」感覚を与える。

### Compress（コンテキストの圧縮）

**要約（Summarization）**:
- Claude Codeのauto-compact: コンテキストウィンドウの95%を超えると、ユーザー-エージェント対話全体を要約
- **再帰的要約**（arXiv:2308.15022）: 長大な対話を段階的に圧縮
- **階層的要約**（Anthropic Alignment, 2025）: Computer Use能力のモニタリングに適用
- Cognition: エージェント間の知識ハンドオフ時に要約。fine-tunedモデルを使用 — この工程の重要性を示す

**トリミング（Trimming）**: ハードコードされたヒューリスティック（例: 古いメッセージの削除）によるフィルタリング。**Provence**（arXiv:2501.16214）はQA用に訓練されたコンテキストプルーナー。

### Isolate（コンテキストの分離）

**マルチエージェント**: OpenAI Swarmの「関心の分離」、Anthropicのマルチエージェントリサーチャー — サブエージェントが独立したコンテキストウィンドウで並列動作。単一エージェントより高性能だが、最大15倍のトークン消費。

**コードエージェント + サンドボックス**: HuggingFaceのDeep Researcher — CodeAgentがツール呼び出しを含むコードを出力し、E2Bサンドボックスで実行。トークン重いオブジェクト（画像、音声等）を変数として保持し、必要時のみLLMに戻す。

**Stateオブジェクト**: LangGraphのStateスキーマ — `messages`フィールドだけをLLMに公開し、他のフィールドは選択的に使用。スキーマ設計によるコンテキスト分離。

### Anhropicとの対応関係

| Anthropic戦略 | Martin分類 | 拡張点 |
|--------------|-----------|--------|
| Compaction | **Compress** | 要約に加えトリミング（Provence）を含む |
| Structured Note-Taking | **Write** + **Select** | 保存（Write）と検索（Select）を分離。記憶のRAG検索・知識グラフを追加 |
| Sub-Agent | **Isolate** | サブエージェントに加え、コードエージェント+サンドボックス、State分離を含む |

Martinのフレームワークの革新性は、**WriteとSelectの分離** — 保存と検索を独立した関心事として扱い、それぞれに固有の技術スタックが存在することを明確化した点にある。

### Reduce/Offload/Isolate への進化

Martinは本記事（June 2025）の半年後、High Signalポッドキャスト（Dec 2025）でフレームワークを **Reduce / Offload / Isolate** の3原則に凝縮・再編成した。4バケット→3原則へのマッピングと詳細は [[concepts/reduce-offload-isolate]] を参照。

| 4バケット (Jun 2025) | 3原則 (Dec 2025) | 変化 |
|---------------------|-----------------|------|
| Write + Select | → **Offload** | 保存と検索を統合。ファイルシステムを外部記憶として、選択的読み出しを行うパターンに一本化 |
| Compress | → **Reduce** | 軌跡要約・コンパクションを「縮小」として再定義。cache hit rateを最重要指標に |
| Isolate | → **Isolate** | 不変だが、Ralph Wiggumループ・fresh contextの重要性が強化された |

この進化は、実運用経験から得た **「コンテキストは最も稀少なリソース」** という深まった理解を反映している。

### Claude Code Agent SDK: Context Engineering の SDK 実装

Lance Martinの4バケット分類とReduce/Offload/Isolateは、Anthropic自身の**Claude Code Agent SDK**（[[entities/claude-code]]）においてSDKプリミティブとして具現化されている。特に**セッション管理**（[Work with sessions](https://code.claude.com/docs/en/agent-sdk/sessions)）は、Context Engineeringの各パターンを開発者が直接呼び出せるAPIに落とし込んだ設計である。

**セッション**は「プロンプト + 全ツール呼び出し + 全ツール結果 + 全応答」を含む会話履歴であり、`~/.claude/projects/<encoded-cwd>/*.jsonl` に自動的に永続化される。これはMartinの **Write** パターンそのものであり、Claude Codeの `auto-compact` が **Compress** として働く前に、生の会話状態を外部保存する仕組みを提供する。

#### Continue / Resume / Fork — 3つのセッション操作

| 操作 | 動作 | Martin分類での対応 | 用途 |
|------|------|-----------------|------|
| **Continue** | カレントディレクトリの最新セッションを自動検出し追記 | **Write + Select** | シングルプロセス内のマルチターン会話。`ClaudeSDKClient`（Python）または `continue: true`（TypeScript）で透過的に管理 |
| **Resume** | 指定されたセッションIDの会話を再開 | **Select**（精密検索） | プロセス再起動後の復旧、特定セッションへの復帰、マルチユーザーアプリでのセッション分離 |
| **Fork** | 元セッションをコピーした新規セッションを作成。元は不変 | **Isolate**（分岐） | 別アプローチの試行。JWT実装を維持したままOAuth2を試す、など |

#### Context Engineering フレームワークとの対応

```
Martin 4バケット              Claude Code Session API
─────────────────────────────────────────────────
Write（外部保存）          →  自動セッション永続化（JSONL）
Select（選択的取り込み）    →  Resume: セッションIDによる精密なコンテキスト復元
Compress（圧縮）           →  auto-compact: 95%しきい値での自動要約
Isolate（分離）            →  Fork: 会話履歴の分岐 + Sub-agents: 独立セッション

Martin 3原則 (Dec 2025)
──────────────────────
Reduce                    →  Compaction + セッションサイズ管理
Offload                   →  セッション永続化 + File Checkpointing（ファイル変更の分離管理）
Isolate                   →  Fork + Sub-agents（Ralph Wiggum loop）
```

**重要な設計判断**: セッションは**会話**を永続化し、**ファイルシステム**は永続化しない。ファイル変更の追跡とロールバックは **File Checkpointing** が別途担当する。この「会話状態」と「ファイル状態」の**関心の分離**は、Martinの **Offload**（ファイルシステムを外部記憶として使うが、会話コンテキストとは分離する）パターンのSDKレベルでの実装である。

**クロスホストセッション**: `~/.claude/projects/` 下のJSONLファイルを移動するか、`SessionStore` アダプターで共有ストレージにミラーリングすることで、CIワーカーやサーバーレス環境間でのセッション復元が可能。これは Martin の「Give Agents A Computer」パターン（[Agent design patterns](https://rlancemartin.github.io/2026/01/09/agent_design/), Jan 2026）のインフラ的裏付けである。

**含意**: Context Engineeringはもはやアドホックなプロンプト設計ではなく、SDKの型付きAPIとして **プログラマティックに管理可能** になりつつある。Martinが予見した Bitter Lesson — 「モデルが賢くなるにつれハーネスは削ぎ落とされる」 — の対極として、セッション管理のような**基盤プリミティブ**は逆にSDKに吸収され、標準化されていく。

## Just-in-Time (JIT) コンテキスト

事前計算された埋め込み検索から、実行時のJIT読み込みへのパラダイムシフト。

**プログレッシブディスクロージャー**: エージェントが必要なコンテキストを段階的に発見し、ワーキングメモリに必要最小限の情報だけを維持。

**ハイブリッド戦略**:
- `CLAUDE.md` などの静的・高価値コンテキストを事前にロード
- `glob`, `grep`, `head`, `tail` などのシェルプリミティブでJIT探索

## 戦略選択マトリックス

| タスクプロファイル | 推奨テクニック |
|-------------------|--------------|
| 双方向/会話的フロー | **Compaction** |
| 明確なマイルストーンを持つ反復的開発 | **構造化メモ** |
| 複雑な探索/並列調査 | **サブエージェント** |
| 静的ドメイン（法務、金融） | **ハイブリッド（CLAUDE.md + JIT）** |

## Anti-Patterns
- **Context Overflow**: 最大トークン数を超える情報投入
- **Context Dilution**: 無関係な情報で重要な事実が埋もれる
- **Static Context**: 会話の進行に伴うコンテキスト更新を怠る
- **Prompt-only Focus**: プロンプトのみを最適化し、コンテキスト全体を軽視する

## 実践者フレームワーク: Khairallahの4ファイルアーキテクチャ (2026)

Khairallah AL-Awady（[[entities/khairallah-al-awady]]）はContext Engineeringの実践者向けフレームワークとして、**4ファイルアーキテクチャ**と**動的コンテキストローディング**を提唱。Anthropic/Karpathyの技術的視点を補完する、個人およびチームが今日から導入できる具体的手法を提供している。

### コア命題

> "Prompt engineering is the syntax. Context engineering is the infrastructure. And infrastructure beats syntax every single time."

> "A perfectly worded prompt inside a poorly designed context will produce average results every time. A basic prompt inside a perfectly designed context will produce exceptional results every time."

### 3層コンテキストモデル

| レイヤー | 説明 | 普及率 |
|---------|------|--------|
| **Layer 1: Immediate Context** | プロンプトそのもの | 99%の人がここで止まる |
| **Layer 2: Session Context** | アップロードファイル、会話履歴、システム指示 | 部分的に使用、意図的設計なし |
| **Layer 3: Persistent Context** | メモリシステム、コンテキストファイル、KB、保存された設定 | ほぼ未活用、最大のレバレッジ |

### 4ファイルアーキテクチャ

すべてのプロフェッショナルが用意すべき4つのコンテキストファイル。セッション開始時にロードすることで、AIを「汎用アシスタント」から「コンテキスト認識型コラボレーター」に変える：

| ファイル | 内容 | 役割 |
|---------|------|------|
| **Identity File** | 専門性、バックグラウンド、コミュニケーションスタイル | AIの「オンボーディング文書」 |
| **Audience File** | 対象読者のデモグラ、知識レベル、課題、目標、言語 | 出力のターゲット精度を保証 |
| **Standards File** | 品質基準、フォーマット設定、トーンガイドライン、アンチパターン、成功例と失敗例 | 品質管理システム |
| **Project File** | 現在の目標、アクティブプロジェクト、最近の決定、未解決課題、期限 | 週次/月次で更新する動的レイヤー |

**制約**: 各ファイル2,000語以下（コンテキストウィンドウに容易に収まるサイズ）

### 動的コンテキストローディング

「すべてをロードする」ことはトークン浪費と注意散漫（attention dilution）を招く。タスクタイプに応じて必要なファイルだけをロードする：

| タスクタイプ | ロードするコンテキスト |
|-------------|----------------------|
| **Writing** | Identity + Audience + Standards + 成果物の成功例 |
| **Analysis** | Identity + Project + 生データ + 過去の分析 |
| **Research** | Project + 研究方法論文書 + 構築対象の既存研究 |
| **Strategy** | 全4ファイル + 競合分析 + 業界データ |

### メモリ進化ラダー

| 段階 | 手法 | 適用タイミング |
|------|------|--------------|
| **Manual** | 意思決定・学びを追跡するランニングドキュメント | ドキュメント数 < 20 |
| **Structured KB** | Obsidian等の構造化マークダウンフォルダ | ドキュメント数 20+ |
| **Vector DB + RAG** | 埋め込みによる自動検索、数千ドキュメント対応 | 手動管理の限界を超えた時 |

### Context-MCP統合パターン

> "Context without tools is knowledge without hands."

**Context-first, tools-second** パターン：
1. システムプロンプトがコンテキストを確立（「誰で、何を知っているか」）
2. MCPサーバーがケイパビリティを提供（「何ができるか」）
3. タスクプロンプトが両者を結合（「今、何をすべきか」）

**ContextはWHYとWHAT。ToolsはHOW。TaskはWHENとWHERE。**

### プロダクション展開

個人の生産性向上からビジネスインフラへの進化：
- AIワークフロー監査 → コンテキストアーキテクチャ設計 → メモリシステム実装 → MCP接続 → 本番システム納品
- 市場価値: **$5,000〜$25,000/プロジェクト**（2026年時点）
- 需要は供給を上回り続ける — Context Engineeringはトレンドではなく、すべてのAIアプリケーションを改善する**基盤インフラ層**

### 技術的視点との統合

Khairallahの実践者フレームワークは、既存の技術的知見（AnthropicのCompaction/Structured Note-Taking/Sub-Agent、KarpathyのSoftware 3.0、DSPyの最適化）を**人間側の導入プロセス**に変換する：

| 技術概念 | Khairallahの実践的対応 |
|---------|----------------------|
| Compaction（Anthropic） | 動的コンテキストローディング — 必要なものだけロード |
| Structured Note-Taking（Anthropic） | メモリ進化ラダー — Manual → KB → RAG |
| Sub-Agent（Anthropic） | Context-MCP統合 — ツール接続による機能拡張 |
| Software 3.0（Karpathy） | 4ファイルアーキテクチャ — コンテキストを「プログラミング」する |
| Attention Budget制約 | 2,000語制限 + タスク別ローディングで注意散漫防止 |

## 関連概念

- [[concepts/context-engineering]] — 上位概念: Harness Engineering
- [[concepts/reduce-offload-isolate]] — Lance Martinの4バケット→3原則への進化形
- [[concepts/harness-engineering/agentic-workflows/context-window-management]] — Willisonのコンテキスト管理パターン
- [[concepts/harness-engineering/system-architecture/context-compaction]] — OpenAI Responses APIの圧縮メカニズム
- [[concepts/harness-engineering/system-architecture/context-anxiety]] — Claude Sonnet 4.5のコンテキスト不安現象
- [[concepts/harness-engineering/system-architecture/harness-design-long-running-apps]] — 長期実行エージェントのGANループ
- [[concepts/token-economics]] — トークンコスト分析
- [[concepts/attention-mechanism-variants]] — KV cacheとattention効率
- [[concepts/dspy]] — DSPy: Declarative Self-improving Python
- [[entities/khairallah-al-awady]] — Khairallah AL-Awady: 実践者向け4ファイルアーキテクチャの提唱者
