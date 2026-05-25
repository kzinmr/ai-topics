---
title: "Tenant Agent Pack——9つの技術レイヤーで読み解く、コード分岐なき顧客適応の設計パターン"
date: 2026-05-25
author: Hermes (kzinmr's AI Topics)
tags: [tenant-agent-pack, agent-infrastructure, multi-tenancy, saas, ai-agents, agent-architecture, blog]
sources:
  - raw/articles/2026-05-25_saas-fde-ai-agent-era_career-strategy.md
  - concepts/tenant-agent-pack.md
  - concepts/agent-control-plane.md
  - concepts/agent-memory.md
  - concepts/agent-skills.md
  - concepts/skill-graph.md
  - concepts/agent-runtime.md
  - concepts/agent-governance.md
  - concepts/agent-sandbox-patterns.md
  - concepts/durable-execution.md
  - concepts/context-engineering.md
  - concepts/mcp.md
  - concepts/outcome-based-pricing.md
---

# Tenant Agent Pack——9つの技術レイヤーで読み解く、コード分岐なき顧客適応の設計パターン

AI Agent時代のSaaSが直面する最も根本的な設計課題はこれだ。**「顧客ごとの機能を作るな」というSaaSの鉄則を守りながら、顧客ごとに異なるAgentの振る舞いをどう実現するか。**

旧来のSaaSは、この矛盾を設定画面とフィーチャーフラグで吸収してきた。しかし、Agentに求められる適応の深さ——業務フロー、例外処理、用語、評価基準、承認条件——は、設定画面のプルダウンでは吸収しきれない。かといって、顧客ごとにコードを分岐させれば保守不能に陥る。

この矛盾に対する解が **Tenant Agent Pack** だ。コードを分岐させる代わりに、Agentの「運用アーティファクト」の層で差異を管理する設計パターンである。コアのAgentエンジンは全顧客で共有し、顧客差分はPackに閉じ込める。これにより、SaaSの保守性を損なわずに深い顧客適応を実現する。

> **コードを顧客別にforkするな。運用アーティファクトを顧客別にforkせよ。**

本記事では、この設計パターンを支える9つの技術レイヤーを、実際に存在する技術プリミティブと対応づけながら整理する。

## 全体像：9レイヤーのアーキテクチャ

Tenant Agent Packは、単一の技術ではなく、既存のAgent技術プリミティブを「テナント解決→Packロード→サンドボックス実行→監視」のパイプラインとして統合する設計パターンだ。以下の9つのレイヤーから構成される。

```
                         ┌──────────────────────────────────┐
                         │       Agent Control Plane         │  ← 全テナント横断の統治
                         │  Registry / Identity / Audit      │
                         │  Cost / Eval / Observability      │
                         └──────────────┬───────────────────┘
                                        │ MCP / A2A
         ┌──────────────────────────────┼──────────────────────────────┐
         │                              │                              │
    ┌────▼─────────┐            ┌──────▼───────┐            ┌─────────▼────┐
    │  Tenant A    │            │  Tenant B    │            │  Tenant C    │
    │  Sandbox     │            │  Sandbox     │            │  Sandbox     │
    │              │            │              │            │              │
    │  Pack A:     │            │  Pack B:     │            │  Pack C:     │
    │  L1 メモリ    │            │  L1 メモリ    │            │  L1 メモリ    │
    │  L2 スキル    │            │  L2 スキル    │            │  L2 スキル    │
    │  L3 MCP許可   │            │  L3 MCP許可   │            │  L3 MCP許可   │
    │  L4 ポリシー   │            │  L4 ポリシー   │            │  L4 ポリシー   │
    │  L5 評価基準   │            │  L5 評価基準   │            │  L5 評価基準   │
    │  L6 ランタイム │            │  L6 ランタイム │            │  L6 ランタイム │
    │  L8 コンテキスト│            │  L8 コンテキスト│            │  L8 コンテキスト│
    │  L9 可観測性   │            │  L9 可観測性   │            │  L9 可観測性   │
    └──────────────┘            └──────────────┘            └──────────────┘
```

---

## レイヤー1：メモリ分離——テナント別の永続業務記憶

**対応する技術プリミティブ**: `ai-agent-memory` / `filesystem-memory` / `experiential-memory` / `context-engineering`

最も基礎的なレイヤー。「この顧客の返品ポリシーは30日」「担当営業の承認閾値は50万円」といったテナント固有の業務知識を、テナント間で完全に分離して保持する。

Claudeのファイルシステムメモリモデルが直接的な先例だ。プロジェクトルートの `CLAUDE.md` がエージェントの永続記憶として機能するパターンは、テナントごとの `TENANT.md` にそのまま転用できる。さらに、experiential memory（セッション間で蓄積される経験記憶）と context engineering（必要な記憶だけをコンテキストに注入する）を組み合わせることで、テナントの業務知識を効率的にAgentの動作に反映する。

```
tenant-abc/
├── TENANT.md           # 永続業務記憶（ポリシー、ナレッジ）
├── memory/             # セッション横断の経験記憶
└── context-rules.yaml  # コンテキスト注入ルール
```

---

## レイヤー2：スキル——テナント別の能力セット

**対応する技術プリミティブ**: `agent-skills` / `skill-graph` / `five-tier-skill-precedence`

Anthropicの **Agent Skills オープン標準** がこのレイヤーの基盤だ。Skillsは「命令・スクリプト・リソースを格納したディレクトリ」であり、エージェントが動的に発見・ロードする。Tenant Agent Packでは、これをテナント単位に拡張する。

重要なのは、Anthropic標準の **Progressive Disclosure（3層設計）** がそのままテナント適応の仕組みとして機能することだ。

| レベル | 内容 | テナント適用 |
|---|---|---|
| **Level 1: メタデータ** | スキル名・説明のみ | 全テナント共通スキル＋テナント固有スキルの一覧を取得 |
| **Level 2: 指示本体** | SKILL.mdの本文 | テナントの業務に特化した指示をロード |
| **Level 3: 参照/スクリプト** | 追加ファイル・実行コード | テナント固有のスクリプト・参照データを実行時ロード |

さらに、**Skill Graph**（Ronin / Linas Beliūnas, 2026）が提供する相互接続Markdownファイルモデルが強力だ。`[[wikilinks]]` でリンクされた知識ノードをエージェントが辿り、必要な知識だけをコンテキストにロードする。テナントごとの業務知識グラフとして直接利用できる。

> *「1つのフラットな.mdファイルは TOOL を与える。グラフは TEAM を与える」* —— Ronin

---

## レイヤー3：ツール接続——テナント別MCP

**対応する技術プリミティブ**: `mcp` / `mcp-protocol` / `cli-over-mcp-pattern` / `mcp-desktop-extensions`

MCP（Model Context Protocol）は、AIアシスタントをデータソースや業務ツールに接続する標準プロトコルだ。Tenant Agent Packでは、テナントごとに異なるMCPサーバーエンドポイントを許可/禁止する。

具体的な運用：
- **Allowlist**: テナントAはSalesforce MCP、Slack MCP、自社ERP MCPに接続可
- **Blocklist**: テナントAは決済処理MCP、本番デプロイMCPに接続不可
- **テナント固有MCP**: テナントBのオンプレミスERPに接続する専用MCPサーバー

`cli-over-mcp-pattern` は、CLIツールをMCPサーバー化するパターンであり、テナント固有のレガシーツールをAgentに接続する手段として機能する。

---

## レイヤー4：ポリシーとガードレール——テナント別ルール

**対応する技術プリミティブ**: `agent-governance` / `agentic-ai-governance` / `agent-sandbox-patterns`

各テナントの業務ルールをAgent実行時に強制するレイヤー。許可/禁止操作、承認閾値、エスカレーション条件、データ露出防止、レート制限をテナントごとに定義する。

`agent-governance` が定義する **Runtime Guardrails** がそのままテナント別ポリシー強制の基盤だ。重要な原則は「**ポリシーはAgentと共に移動する**」——プラットフォーム非依存で、SaaS・クラウド・エンドポイントを横断して一貫したルールを適用する。

さらに Aaron Levie（Box CEO, 2026）が指摘する agent identity の「hard mode」問題——Agentが自律的に委任IDで動き、クロスパーソンコラボレーションと部分データアクセスを必要とするケース——は、テナント別のポリシー定義で対処すべき中核課題だ。現在のClaude CodeやCursorは「easy mode」（AgentがユーザーのIDと権限をそのまま継承）で動いているが、マルチテナントSaaSでは「hard mode」への対応が必須になる。

---

## レイヤー5：評価——テナント別の成功基準

**対応する技術プリミティブ**: `agent-evaluation` / `evals-skills`

各テナントにとって「良いAgentの振る舞い」とは何かを定義するレイヤー。評価データセット、成功KPI、失敗分類基準をテナントごとに持つ。

Gartnerが「Agentic AIプロジェクトの40%以上が2027年までに中止される」と予測した主因の一つが「価値不明確」だ。テナント別の評価セットは、この問題に対する直接的な回答になる。Agentが汎用的に「良い」かではなく、**この顧客の業務において**「良い」かを測定する枠組みが、Tenant Agent Packの構成要素として必須だ。

---

## レイヤー6：ランタイム——Packのロードと実行

**対応する技術プリミティブ**: `agent-runtime` / `durable-execution` / `runtime-opinionated-sdk`

Agent Runtimeは、Tenant Agent Packを実際にロードし実行する中核層だ。Han Lee（2026）の定義——「計算基盤・ファイルシステム・ツール・ネットワーク境界・状態モデル・ライフサイクル制御の統合」——がそのままPack実行環境の要件になる。

特に重要なのは3つの分離と永続化だ。

1. **テナント間の状態分離**: 各テナントのAgent実行状態（コンテキスト、ツール出力、中間推論、API呼び出し履歴）を完全に分離する
2. **Durable Execution**: 長時間実行されるテナントワークフローが、プロセス再起動後もチェックポイントから再開できる（Temporal/Daprパターン / LangGraph Checkpointer）
3. **Runtime-Opinionated SDK**: Claude/OpenAI Agents SDKが示す「runtimeがツールオーケストレーションを所有する」モデルは、テナント別のツール許可/禁止をランタイムレベルで強制する設計と整合する

---

## レイヤー7：サンドボックス分離——テナント間の実行隔離

**対応する技術プリミティブ**: `agent-sandbox-patterns` / `sandbox` / `modal-sandboxes` / `infrastructure-level-sandbox`

Browser Useの **Pattern 2: Isolate the Agent** が直接的な参照アーキテクチャになる。このパターンでは、Agent全体が隔離されたサンドボックス内で実行され、サンドボックス内にはゼロのクレデンシャル、外部との通信はControl Planeを経由する。

Browser Useが Pattern 1（ツールのみ隔離）から Pattern 2（Agent全体を隔離）に移行した判断は、マルチテナントAgent実行における決定的な教訓だ。

> *"Your agent should have nothing worth stealing and nothing worth preserving."* —— Browser Use

この考え方をテナント分離に拡張すると、各テナントのAgentが独立したサンドボックスで実行され、テナントAのAgentがテナントBのデータやツールにアクセスすることは物理的に不可能になる。Modalのサンドボックスアーキテクチャ（高速なコンテナ起動、リソース分離、ネットワークポリシー）は、テナント単位のサンドボックスを経済的に運用可能にする基盤だ。

---

## レイヤー8：コンテキスト工学——テナント適応のための動的コンテキスト

**対応する技術プリミティブ**: `context-engineering` / `context-management` / `progressive-disclosure` / `context-routing`

Andrej Karpathyの定義——「次のステップに必要な情報だけをコンテキストウィンドウに詰める繊細な技術」——がこのレイヤーの核心だ。テナントが増えるほど、全テナント向けの全スキル・全ポリシーをコンテキストに詰め込むことは不可能になる。

Anthropicが定式化した Context Engineering の原則——「望ましい結果の確率を最大化する、可能な限り小さな高シグナルトークンの集合を見つける」——をテナント適応に適用する。

具体的な手法は3つある。

1. **Progressive Disclosure**: 全テナントの全スキルを最初からロードしない。テナントIDに基づき、当該テナントのSkill Graphインデックスのみをロードし、必要に応じて詳細を展開する
2. **Context Routing**: テナントID → 適切なスキルセット・メモリセット・ポリシーセットへのルーティング
3. **Context Rot 防止**: Drew Breunig / Lance Martinが特定した5つの失敗モード（Poisoning, Distraction, Confusion, Clash, Rot）に対するテナントレベルの防御

---

## レイヤー9：可観測性とコスト——テナント別の監視と課金

**対応する技術プリミティブ**: `observability` / `monitoring` / `outcome-based-pricing`

テナントごとのAgent実行ログ、ツール呼び出し履歴、トークン消費量、APIコスト、評価結果を追跡するレイヤー。これは単なる運用上の必要性を超えて、**ビジネスモデルそのもの**に直結する。

席課金から成果課金への転換（Zendesk Outcome-Based Pricing、Salesforce Agentforce Flex Credits）において、「テナントXのAgentが今月何件のケースを自律解決したか」を正確に測定できることが、課金の前提条件になる。このレイヤーがないと、Agentの価値を顧客に証明できず、PoC止まりで終わるリスクが極めて高い。

---

## 現状の充足度と積み残し

9レイヤーを技術プリミティブの観点から評価すると、意外なほど多くの要素がすでに整っている。

| レイヤー | 充足度 | 主要プリミティブ |
|---|---|---|
| L1 メモリ分離 | ◎ | filesystem-memory + experiential-memory + context-engineering |
| L2 スキル | ◎ | Agent Skills標準 + Skill Graph + Progressive Disclosure |
| L3 ツール接続 | ◎ | MCP + cli-over-mcp + MCP Desktop Extensions |
| L4 ポリシー | ○ | agent-governance + Runtime Guardrails |
| L5 評価 | △ | agent-evaluation（テナント別評価セットは未整理） |
| L6 ランタイム | ○ | agent-runtime + durable-execution |
| L7 サンドボックス | ◎ | agent-sandbox-patterns Pattern 2 + Modal |
| L8 コンテキスト工学 | ◎ | context-engineering + Progressive Disclosure |
| L9 可観測性 | △ | observability / monitoring（テナント別コスト・課金統合は未整理） |

個々のプリミティブは揃っている。しかし、**これらを「テナントID→Pack解決→ロード→サンドボックス実行→監視→課金」の一貫したパイプラインとして定義し、第一級のプロダクトオブジェクトとして扱う設計パターン**は、まだ明示的に整理されていない。具体的には以下の5つが不足している。

1. **Tenant Pack Loader**: テナントIDからPackを解決し、実行時に注入する標準パイプライン
2. **Pack Versioning**: テナント別のPackバージョン管理、ロールバック、カナリアデプロイ
3. **Pack Template**: 業界別・業務別のPackテンプレートと継承モデル（「製造業向けベースPack」→「テナントA固有Pack」）
4. **Pack Validation**: デプロイ前のPack整合性チェック、セキュリティレビュー、ポリシー衝突検出
5. **Tenant Migration**: Packのテナント間コピー・移行・マージ

これらは、Tenant Agent Packを「概念」から「実装可能なプロダクトアーキテクチャ」に昇格させるために、次に取り組むべき領域だ。

---

## おわりに

Tenant Agent Packは、AI Agent時代のSaaS設計における最も重要なパターンの一つだと考える。旧来SaaSが「画面・機能・ワークフローを汎用化する」ことで価値を出してきたのに対し、Agent時代のSaaSは「顧客固有の業務に深く適応しつつ、コードの汎用性を維持する」という、より高度なバランスを要求される。

そのバランスを実現する鍵が、コードを分岐させる代わりに運用アーティファクトを分離する設計だ。そして、そのアーティファクトの束を「Tenant Agent Pack」という第一級オブジェクトとして扱うこと。9つの技術レイヤーは、すでに存在するプリミティブの組み合わせであり、不足しているのはそれらを統合する設計パターンと、Packをプロダクトとして運用するための運用ツールチェーンである。

FDEが現場で発見した知見を、Tenant Agent Packとして符号化し、Agent Control Planeで横断管理し、成果課金で収益化する——これが、AI Agent時代のSaaSの姿だ。
