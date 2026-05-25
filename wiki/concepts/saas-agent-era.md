---
title: "SaaS in the AI Agent Era"
type: concept
created: 2026-05-25
updated: 2026-05-25
tags:
  - saas
  - ai-agents
  - enterprise-ai
  - business-model
  - pricing
  - multi-tenancy
  - agent-infrastructure
  - career-strategy
  - fde
sources:
  - raw/articles/2026-05-25_saas-fde-ai-agent-era_career-strategy.md
related:
  - concepts/forward-deployed-engineering
  - concepts/agent-control-plane
  - concepts/tenant-agent-pack
  - concepts/ai-operating-model
  - concepts/enterprise-ai
  - concepts/service-as-software
---

# AI Agent時代のSaaS

## 概要

SaaSは終わらない。しかし、その**構造は根本から変わる**。

旧来のSaaSモデルは「全顧客に共通の画面・機能・ワークフローを提供する」ことが中心だった。Agent時代のSaaSは「顧客ごとの業務・データ・権限・評価基準に接続し、AI Agentが実際に仕事を完了する状態を作る」ことが中心になる。つまり、**機能配布プラットフォームから、Agent運用OSへ**の転換である。

## レイヤー別の構造変化

SaaSを構成する各レイヤーは、以下のように質的に変化する：

| レイヤー | 旧来SaaS | Agent時代のSaaS |
|---|---|---|
| **UI** | 全顧客共通の画面 | 薄いUI。Slack/Teams/メール/Agent UIがエントリポイント |
| **機能** | 共通機能の追加 | Agentがツールを呼び出して業務を遂行 |
| **カスタマイズ** | 管理画面・設定・ワークフロー定義 | メモリ、スキル、ポリシー、MCP、評価セット、承認フロー |
| **マルチテナンシー** | DB/計算資源の共有分離 | Agent実行・権限・監査・コスト・評価・メモリのテナント分離 |
| **価値単位** | 席数、ログイン、画面操作 | 完了タスク、削減時間、解決件数、品質、リスク低減 |
| **競争優位（moat）** | 機能数、UX、データ蓄積 | 業務データ、権限モデル、評価、監査、統合、導入知見 |

## 危険なSaaSと強いSaaS

### 淘汰リスクが高いSaaS

- **画面＋DBだけのSaaS**：入力フォーム、承認フロー、ダッシュボードに留まっているもの
- **薄いAIラッパーSaaS**：LLM APIに軽いUIを被せただけのもの
- **水平SaaSで業務状態を持たないもの**：データ・権限・業務文脈を顧客側に依存しているもの

### Agent時代に勝つSaaS

- **業務状態を握るSaaS**：CRM、CS、会計、法務、HR、ITSM、物流、医療、金融、製造、建設——System of Recordを持つもの
- **Agentを安全に動かす仕組みを持つSaaS**：権限・監査・評価・承認のレイヤーを備えているもの
- **深い業界知識を埋め込めるVertical SaaS**
- **FDEで得た知見を標準機能へ還流できるSaaS**

## 個別対応はコード分岐ではなくアーティファクト分離

旧来のSaaS原則「顧客ごとの機能は作らない」は維持される。変わらないのは**コードを分岐させない**という鉄則。変わるのは「個別性をどこに置くか」である。

コード分岐の代わりに分離するもの：

- **業務メモリ**、**スキル**、**ツール接続**
- **権限ポリシー**、**承認条件**
- **評価データセット**、**成功基準**
- **例外処理ルール**、**エスカレーションルール**
- **プロンプト／システム指示**、**Agent役割定義**
- **コスト上限**、**実行ログ保持ポリシー**

つまり、コードを顧客別に作るのではなく、**Agentの「運用アーティファクト」を顧客別に持つ**設計への転換である。これは[[forward-deployed-engineering]]の現場で発見されたパターンが、プロダクト設計にフィードバックされる領域でもある。

## エンタープライズSaaSは統治レイヤーになる

Agentの爆発的普及は、むしろSaaSに新たな需要を生む。それは**Agentの登録・統治・監査・評価**を行うレイヤーだ。

- **ServiceNow**：自社プラットフォームをAI Agentの「control tower」と位置づけ、Agent Orchestratorで複数Agentを部門横断で協調させる
- **Workday**：Agent System of Recordを提供し、AI Agentを人間の従業員と同様にライフサイクル管理する
- **Deloitte**：2026年にSaaS経由のAI Agent利用が急増し、複数ベンダー・社内開発Agentの活動・コスト・セキュリティ・コンプライアンスを追跡する「control centers」が重要になると予測
- **Google Cloud**：Gemini Enterprise Agent PlatformでAgent Identity、Registry、Gateway、Simulation、Evaluation、Observabilityを中核機能として提供

## 価格モデルの転換

席課金（seat-based）は成果課金（outcome-based）へシフトする：

| 旧モデル | 新モデル |
|---|---|
| ユーザー席数 | アクション単位、解決件数単位 |
| ログインベース | 完了ワークフロー単位、自動化判断単位 |
| 固定ライセンス | 削減時間単位、base platform fee + usage |
| — | base SaaS fee + Agent outcome fee |

具体例として、**Zendesk**は「自律解決件数」に紐づくOutcome-Based Pricingを発表。**Salesforce Agentforce**はFlex Credits、会話課金、ユーザーライセンスの複合モデルを採用している。

## 主要リスク

Gartnerは2025年、**Agentic AIプロジェクトの40%以上が2027年末までに中止される**と予測した。理由はコスト超過、価値の不明確さ、リスク管理不足である。

この予測が示唆するのは、Agent導入の「現場実装力」と「統治の仕組み」を持つSaaSこそが、淘汰の波を生き残るという構図だ。単にAgentを載せただけのSaaSは、PoC止まりで終わるリスクが極めて高い。

## 関連ページ

- [[forward-deployed-engineering]] — FDEの役割と方法論
- [[enterprise-agents]] — エンタープライズにおけるAI Agentの導入パターン
- [[agent-executor]] — Agent実行のアーキテクチャ
- [[agent-skills]] — Agentスキルの設計と管理
