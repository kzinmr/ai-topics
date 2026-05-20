---
title: Agent Operator Patterns
created: 2026-05-20
updated: 2026-05-20
type: concept
tags:
  - ai-agents
  - agent-architecture
  - agent-ergonomics
  - orchestration
  - hermes-agent
  - governance
  - methodology
  - durable-execution
  - multi-agent
  - design-patterns
sources:
  - raw/articles/2026-05-15_shann_hermes-agent-operator.md
related:
  - "[[entities/shannhk]]"
  - "[[entities/hermes-agent]]"
  - "[[comparisons/hermes-vs-openclaw]]"
---

# Agent Operator Patterns

**Agent Operator Patterns** は、自律型AIエージェントの**運用・管理・拡張**に関する設計パターンとベストプラクティスの集合である。Shann Holmberg (@shannhk) の "How to Become a Hermes Agent Operator" で体系化されたパターン群は、単一エージェントから本格的なエージェント艦隊へとスケールするための実践的フレームワークを提供する。

## Core Mental Model（4要素モデル）

Shannの運用モデルは4つの要素で構成される：

```
┌───────┐
│  YOU  │   the operator
└───┬───┘
    │
    ├── control path ────► Agent Control Room（管理・設定・ドキュメント）
    ├── direct path  ────► Specialist Agent（直接対話・最速）
    └── orchestrated ────► Orchestrator → Task Bus → Specialists（合成・分配）
```

| 要素 | 役割 | アクセス手段 |
|---|---|---|
| **You（オペレーター）** | 最終判断者、全要素への直接アクセス権を持つ | すべてのパス |
| **Agent Control Room** | 艦隊全体のドキュメント・設定・ガバナンス。チャットする場所ではない | ファイルシステム（`/root/vps-agents/`） |
| **Hermes Agents（ワーカー）** | 実作業を担うスペシャリスト。独自の brain/personality/skillset | Chat + cron |
| **Agent Task Bus（任意）** | Orchestrator ⇔ Specialists 間のタスク中継（Level 3+） | Orchestratorが読み書き |

## Pattern 1: Control Room（サイドコントロールプレーン）

### 原則
> "The control room is the brain that defines the system. The live runtime is the body that runs it. You can rebuild the body from the brain. You cannot rebuild the brain from the body."

Control Room はエージェントの**ランタイム（body）と分離された管理レイヤー（brain）**である。

```
/root/vps-agents/          → Control Room: docs, rules, runbooks, architecture
   README.md
   CLAUDE.md
   agents/<agent-name>/
     inventory.md           ← エージェント一覧：何が・どこで・どう動くか
     docker.md              ← Docker構成
     env-map.md             ← 参照しているcredential/環境変数（生のsecretは置かない）
     runbook.md             ← 再起動・ログ確認・障害対応の手順
     backup.md              ← バックアップ手順
   shared/
     security.md            ← 共通セキュリティルール
     commands.md            ← 共通コマンド集
   api-keys-sop.md          ← API key管理SOP
   orchestrator-and-fleet-skills.md

/srv/<agent-name>/data/     → Live Runtime: secrets, memory, skills, sessions, crons
```

**Storage Split の価値**:
- Brain（Control Room）をGit管理すれば、body全体を再構築可能
- Brainには生のsecretを一切置かない
- 新しい運用者が来てもControl Roomを読めば全体像が把握できる

### Wiki管理システムへの応用

現在のwiki管理システムは27個のcronジョブと28個のスクリプトで構成されているが、パイプラインの全体像はAGENTS.mdとスキル内に散在している。Control Room パターンを適用することで：

```
~/wiki/control-room/
  README.md                    ← システム全体像、アーキテクチャ図
  inventory.md                 ← 全cronジョブ・パイプライン・スクリプト一覧
  agents/
    hermes-wiki/
      runbook.md               ← 再起動・ログ確認・トラブルシューティング
      env-map.md               ← 参照credential一覧（実値なし）
  pipelines/
    newsletter-ingest.md
    blog-ingest.md
    x-bookmarks.md
    x-accounts-scan.md
    raw-backlog.md
    daily-report.md
    dreaming.md
    wiki-health.md
  shared/
    naming-conventions.md      ← ファイル名規則、frontmatter規約
    quality-standards.md       ← entityページ品質基準
    troubleshooting.md         ← よくある問題と対処法
```

## Pattern 2: Brain Layers（文脈レイヤー化）

### 原則
> "The layers are not decoration. They are the reason the agent does not lose context as the work gets specialized. The company brain stays stable while the worker iterates. The brain layers make the worker disposable."

ShannのSEO agentの5層構造：

```
Company Brain（安定）    ← vision, brand, audience, products
    ↓
Orchestrator            ← ルーティングのみ
    ↓
SEO Brain（半安定）      ← ranking playbook, voice rules, content formats, style guide
    ↓
3 Sub-agents（可変）:
  Research + Ideate      ← keyword seed, SERP, competitor extraction, gap analysis
  Production             ← angle brief, outline, draft, image gen, QA
  Distribution           ← publish prep, schema, internal linking, syndication, monitoring
```

**ポイント**: Company Brain と SEO Brain は安定しており、Sub-agents（ワーカー）は使い捨て可能。文脈が失われない理由は、上層のBrainが下層の反復を吸収するからである。

### Wiki管理システムへの応用

現在のHermesのmemoryは全コンテキストがフラットに詰まっている。Brain Layersを導入すると：

| レイヤー | 内容 | 変更頻度 |
|---|---|---|
| **Wiki Brain（安定）** | wikiの目的、カバレッジ範囲、品質基準、SCHEMA定義 | 極めて低い |
| **Pipeline Brain（半安定）** | 各パイプラインの固有知識（処理ルール、判定基準） | パイプライン追加時のみ |
| **Session Context（一時的）** | 処理対象の記事・論文の具体的内容 | セッションごと |

## Pattern 3: Agent Creation Heuristics（新エージェント作成基準）

### 原則
> "Needs its own credentials → new agent. Needs its own long-term memory → new agent. Ongoing repeated work that is a separate role → new agent. Otherwise stay with what you have."

**アンチパターン**: 全てのcredentialとmemoryを1つの「メガエージェント」に詰め込む。隔離性が失われ、アクセス権限の取り消しが困難になり、どのvoiceを使うべきかエージェントが混乱する。

## Pattern 4: 4-Level Fleet Operation Model

| Level | 構成 | 適した状況 | 必要なスキル |
|---|---|---|---|
| **1: One Agent** | 単一Hermes + Control Room（任意） | 初期セットアップ、個人アシスタント | SOUL.md, MEMORY.md, USER.md |
| **2: Direct Specialists** | 複数スペシャリスト、直接対話、no Orchestrator | 役割分離の検証、credentialスコープ分離 | Docker, SSH, Control Room folder |
| **3: Orchestrator + Specialists** | Orchestratorがフロントドア、+ Task Bus | クロス機能ワークフロー、委任・合成 | 上記 + orchestrator skills |
| **4: Automated Agent Team** | Level 3 + cron + 自動化ワークフロー | 週次レポート、ヘルスチェック、定期業務 | 上記 + cron設計、監視 |

**Level 2→3 への移行判断**: Specialistsが有用であることを直接使って証明するまでは Orchestrator を導入しない。「まだ使えるかわからないエージェントのために Orchestrator を作ってはいけない」。

## Pattern 5: Prototype → Production Methodology

Shannがあらゆるマーケティングワークフローに適用する4ステップ：

```
Prototype in Hermes
  → 2-3回の実データ補正
    → Fine-tune in dedicated workspace
      → Deploy on VPS with cron
```

| ステップ | 内容 | 期間 |
|---|---|---|
| 1. Prototype | メインHermesでワークフローを記述・試行。初回はほぼ間違える | 1日 |
| 2. Iterate | 実ワークで2-3回走らせ、毎回ズレを修正。Harnessが修正を学習しスキル化 | 2-3日 |
| 3. Fine-tune | 専用workspace（Claude Code等）でプロンプト精錬・ルーティング確定・エラーハンドリング追加 | 1週間 |
| 4. Deploy | Docker化 → VPS → cron設定 → 放置 | 1日 |

**核心**: "You cannot write a production agent from scratch. You have to grow one."

### Wiki管理システムへの応用

この方法論は新しいwikiパイプライン追加時にそのまま適用可能：

1. **Prototype**: Hermesで手動処理を数回試す（例：新しいRSSフィードの処理）
2. **Iterate**: 実際の記事で2-3回動かし、タグ付け・分類のズレを修正
3. **Fine-tune**: スクリプト化し、エラーハンドリングとcronスケジュールを確定
4. **Deploy**: `raw-backlog-ingest` のようなcronジョブとして本番化

## Pattern 6: Agent Ergonomics（運用快適性）

### Fleetチェックイン
```
$ ssh hermes
$ docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Image}}"

NAMES                       STATUS         IMAGE
hermes-orchestrator         up 14 hours    hermes-runtime
hermes-seo-espressio        up 8 hours     hermes-runtime
hermes-cmo                  up 8 hours     hermes-runtime
hermes-life                 up 12 hours    hermes-runtime
```

### Runbook例
```
# runbook: hermes-seo-espressio
restart:   docker compose restart hermes-seo-espressio
logs:      docker logs -f hermes-seo-espressio
shell:     docker exec -it hermes-seo-espressio bash
```

## 我々のWiki管理システムへの具体的適用案

Shannのパターン群を現在のwiki管理システム（Hermes単一エージェント + 27 cron jobs）に適用する優先度順：

### 優先度 高: Control Room構築
`~/wiki/control-room/` を作成し、AGENTS.mdとスキルに散在する運用知識を集約する。新パイプライン追加時の参照点となり、障害時の切り分けが速くなる。

### 優先度 中: Agent Creation Heuristicsの適用
現在の単一エージェントを分割すべきかの判断基準を得る：
- **独自credentialが必要か？** → 現状は不要
- **独自の長期memoryが必要か？** → arxiv論文専門の研究エージェントは価値あり
- **継続的反復作業で別ロールか？** → daily-report生成、wiki-healthチェックは分離候補

### 優先度 低〜中: Brain Layersの導入
memory/skillsをレイヤー化し、パイプライン追加時に全体コンテキストが汚染されないようにする。

### 既に実現していること
- **Level 4相当の自動化**: 27 cron jobsによる自律パイプラインはShannのLevel 4（Automated Agent Team）に相当
- **Prototype → Production**: `raw-backlog-ingest` の段階的導入はこの方法論に合致

## Cross-References

- [[entities/shannhk]] — これらのパターンの提唱者。Espressio AIでの実践経験に基づく
- [[entities/hermes-agent]] — パターンが前提とするエージェントフレームワーク
- [[comparisons/hermes-vs-openclaw]] — "Rails vs Linux" の哲学的フレーミング

## References

- [How to Become a Hermes Agent Operator](https://x.com/i/article/2055317817658900480) (2026-05-15, Shann/@shannhk, X article)
- [hermes-agent-control-room template](https://github.com/shannhk/hermes-agent-control-room)
