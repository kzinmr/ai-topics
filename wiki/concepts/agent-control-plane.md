---
title: "Agent Control Plane"
type: concept
created: 2026-05-25
updated: 2026-05-25
tags:
  - agent-infrastructure
  - control-plane
  - ai-agents
  - enterprise-ai
  - governance
  - audit
  - security
  - monitoring
  - multi-tenancy
  - agent-identity
  - agent-governance
  - cost-optimization
  - observability
sources:
  - raw/articles/2026-05-25_saas-fde-ai-agent-era_career-strategy.md
related:
  - concepts/saas-agent-era
  - concepts/enterprise-agents
  - concepts/agent-ontology
  - concepts/decision-centric-architecture
---

# Agent Control Plane（エージェント制御基盤）

**Agent Control Plane**（エージェント制御基盤）とは、AI Agent をエンタープライズ規模で管理・運用するためのガバナンス・統治インフラストラクチャ層である。Agent の数が指数関数的に増加するにつれ、個別の Agent を作るだけではなく、**Agent 群（フリート）全体を体系的に管理する仕組み**が不可欠になる。Agent Control Plane は、そのための「Agent OS」とも呼べる存在である。

## 登場の背景

[[concepts/saas-agent-era|SaaSからAgent時代]]への構造転換において、企業では人間の従業員と同様に AI Agent を管理する必要性が高まっている。[[entities/palantir|Palantir]]、[[entities/workday|Workday]]、[[entities/servicenow|ServiceNow]]、Google など主要プラットフォームがこぞって Agent 制御基盤の構築に乗り出している背景には、**Agent の数が増えるほど、管理不在によるリスクが指数関数的に拡大する**という構造的要因がある。Deloitte は 2026 年までに「コントロールセンター」と Agent マーケットプレイスが重要になると予測する。

## コアコンポーネント

Agent Control Plane は以下の 13 のコアコンポーネントで構成される：

| コンポーネント | 説明 |
|---|---|
| **Agent Registry** | デプロイされた全 Agent の一元在庫管理。どの Agent が、どこで、どのバージョンで動いているかを把握する |
| **Agent Identity** | 非人間アイデンティティ（Non-Human Identity）管理。Agent ごとに一意の識別子と認証情報を付与 |
| **Permission Management** | 最小権限（least privilege）、委任権限（delegated authority）、ツールレベルでのアクセス制御 |
| **Execution Logs** | Agent の全アクションと意思決定の完全な監査証跡（audit trail） |
| **Tool Call History** | いつ、どのツールが、誰によって呼び出されたかの履歴 |
| **Cost Management** | Agent 単位・テナント単位のコスト追跡と上限（cap）設定 |
| **Evaluation Results** | 継続的な品質測定。タスク成功率、訂正率、エスカレーション率など |
| **Failure Classification** | 失敗の分類と自動ルーティング。どの失敗が人間の介入を要するかを判断 |
| **Human Approval** | 高リスク操作に対する条件付き承認ゲート。金額閾値や業務クリティカル度に基づく |
| **Rollback** | Agent のアクションに対する安全な取り消し・巻き戻し機能 |
| **Tenant-Specific Memory Management** | 顧客（テナント）ごとに隔離された業務メモリ管理 |
| **Security Policy** | プロンプトインジェクション防御、ツール権限制御、サードパーティスキルレビュー |
| **Audit Export** | コンプライアンス対応可能な監査証跡のエクスポート機能 |

## 業界の方向性

### Google Gemini Enterprise Agent Platform
Google は Agent Identity、Agent Registry、Agent Gateway、Simulation、Evaluation、Observability を中核に据えたプラットフォームを展開している。[[concepts/agent-ontology|Agent オントロジー]]に基づく構造化された管理を志向。

### ServiceNow
自社プラットフォームを Agent の「コントロールタワー」と位置づけ、**Agent Orchestrator** によって複数 Agent を部門横断で協調させる。

### Workday Agent System of Record
AI Agent を人間の従業員と同様に登録・管理・計測し、**ライフサイクル管理**を行う。Agent の採用から退役までを人事システムと同一の枠組みで扱う。

### Deloitte の予測
2026 年までに「コントロールセンター」と Agent マーケットプレイスがエンタープライズ AI の重要インフラになると予測。複数ベンダーや社内開発 Agent の活動・使用量・コスト・アクセス・性能・セキュリティ・コンプライアンスを一元的に追跡する必要性が高まる。

## SaaS との関係

Agent Control Plane は、SaaS の次なる進化形である。旧来的な SaaS が「全顧客共通の画面と機能」を提供していたのに対し、Agent Control Plane は **Agent が安全に動作するための統治レイヤー** を提供する。つまり、機能を売るのではなく、**Agent が安全かつ監査可能に業務を完了できる環境**を売るビジネスモデルへの転換である。

これは [[concepts/decision-centric-architecture|意思決定中心アーキテクチャ]] とも深く関係し、Agent の意思決定をどのようにガバナンスするかが中核課題となる。

## 開発者に求められるスキル

Agent Control Plane の構築・運用には、従来の SaaS 開発とは異なる能力が必要になる：

1. **権限・監査設計** — 最小権限、委任権限、非人間アイデンティティ、監査証跡設計
2. **セキュリティ** — プロンプトインジェクション対策、ツール権限制御、サンドボックス設計
3. **評価フレームワーク** — Agent の品質を継続的に測定する評価基盤の設計
4. **コスト管理** — Agent 単位・テナント単位のコスト可視化と上限設定
5. **コンプライアンス・規制理解** — 業界規制（金融・医療・法務など）に対応した監査エクスポート設計

## 関連する概念

- [[concepts/enterprise-agents|Enterprise Agents]] — Agent Control Plane が管理対象とするエンタープライズ Agent の実践
- [[concepts/agent-ontology|Agent Ontology]] — Agent の構造的分類と管理のためのオントロジー
- [[concepts/saas-agent-era|SaaSからAgent時代へ]] — この構造転換の全体像
