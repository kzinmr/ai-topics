---
title: "SaaSの未来とAI Agent開発者のキャリア戦略"
created: 2026-05-27
query_date: 2026-05-27
type: query
tags:
  - saas
  - ai-agents
  - career-strategy
  - harness-engineering
  - service-as-software
  - fde
  - agent-native
  - mcp
aliases:
  - "saas-agent-strategy"
  - "post-saas-career"
related:
  - concepts/service-as-software
  - concepts/harness-engineering
  - concepts/agent-native-product-management
  - comparisons/open-harness-vs-agent-framework
  - comparisons/agent-harnesses
  - concepts/agent-patterns
  - entities/palantir
  - concepts/ai-services-joint-ventures
  - concepts/after-automation
---

# SaaSの未来とAI Agent開発者のキャリア戦略

## クエリ概要

**質問**: SaaS企業でAI Agentを開発しているが、パーソナルAI Agentの爆発的普及と企業向けFDEモデルの拡大により、SaaS業態から距離を置くべきか、FDEのようなロールに寄るべきか。

**回答日**: 2026-05-27

---

## 分析: 3つの同時進行トレンド

### トレンドA: パーソナルAI Agent（Harness）による水平吸収

[[comparisons/agent-harnesses]] が示すように、OpenClaw（145K+ stars）、Hermes Agent、OpenCode（155K stars）、Pi、Codex CLIといったパーソナルAI Agent Harnessが爆発的に普及。これらの本質:

- **「モデルよりハーネスが重要」** — 同じモデルでHarnessの違いが5〜40ptの性能差
- **コーディング不要の設定吸収** — ユーザー側のMCP設定・スキル追加・プロンプト変更で多様なユースケースを吸収
- **Runtime-Centricアーキテクチャ** — 従来のワークフロー中心（LangGraph的）から、モデルが自律的に制御フローを握る実行基盤へ [[comparisons/open-harness-vs-agent-framework]]

**含意**: 「なぜSaaSツールを買うのか？自分のAI AgentがAPIを叩けば済む」。これが水平吸収の力学。

### トレンドB: FDEモデルのグローバル展開（垂直深化）

[[entities/palantir]] と [[concepts/ai-services-joint-ventures]] が記録:

| プレイヤー | 規模 | 戦略 |
|---|---|---|
| Palantir | Q1 2026 $1.63B (+84% YoY 政府) | 20年のFDE先行者利益 |
| OpenAI "The Deployment Company" | $4B JV、3件の買収交渉中 | GPT-5.5 + 数百人のエンジニア埋め込み |
| Anthropic × Blackstone/Goldman | $1.5B JV | Claude + 数百人のエンジニア/コンサルタント |

PalantirのFDEモデルの本質: *"To displace Palantir, it is not enough to show up with equivalent software. A substitute would ALSO have to come up with free support staff, to replicate the whole experience."* — Bert Hubert

### トレンドC: SaaSフリーミアムモデルの崩壊

[[raw/newsletters/2026-05-05-why-saas-freemium-playbooks-don-t-work-in-ai]] でGoogleのAIサブスクリプション責任者Vikas Kansal:

> *"Traditional SaaS freemium assumes near-zero marginal cost. In AI, every free prompt burns expensive compute."*
> *"We stopped selling 'answers' and started selling 'hours'."*

Sequoiaの[[concepts/service-as-software]]論文: SaaSはツールを売る（Copilot）、Service-as-Softwareは成果を売る（Autopilot）。後者のTAMは6倍（ソフトウェア予算→人件費予算）。

---

## 「真ん中」の危険地帯

現在の「SaaS企業でAI Agentを開発するプロダクト開発者」は3つのトレンドの交差点:

| レイヤー | 従来のSaaS | AI Agent時代 |
|---|---|---|
| UI層 | 人間向けGUI | Agent向けAPI + MCPツールに置換 |
| ロジック層 | 汎用機能（マルチテナント） | パーソナライズド文脈蓄積が競争力 |
| データ層 | 共有ストレージ（コスト効率） | 顧客固有オントロジーが参入障壁 |

- **Agentは「汎用」を求めない** — 特定の文脈・データ・ワークフローに深く結合して初めて価値
- **マルチテナンシーの限界** — Agentの文脈蓄積（メモリ・スキル・セッション履歴）はテナント分離が難しい
- **コスト構造の逆転** — 従来SaaSは限界費用ゼロ、AI Agentは使うたびに計算資源が燃える

---

## 戦略的提言: 第三のレイヤー

### ❌ 選択肢A: 従来型SaaSに留まる → 非推奨

MCPが標準化されつつある今、Agentが直接叩けるAPIとツールを持つことが新しいSaaSの定義。「UIもDBも全部入り」の従来型SaaSは、水平吸収と垂直深化の板挟み。

### ❌ 選択肢B: 純粋なFDEロールに転身 → 部分的に妥当だが本質ではない

FDEは「既存プラットフォームを顧客環境に適合させる」仕事。「新しいものをゼロから設計する」こととは異なる。

### ✅ 選択肢C: Agent-Nativeプロダクト開発者

#### ① Harness Engineeringを中核能力にする

[[concepts/harness-engineering]]: *"60-80% of development time should be spent on the harness, not on model selection or prompt engineering."* — Hamel Husain

差別化要因:
- コンテキスト管理（何をモデルに見せるか）
- ツールオーケストレーション（MCPツールの設計と品質）
- 評価パイプライン（Evals as a Moat — Viv Trivedy提唱）
- サンドボックス・セキュリティ・状態管理

#### ② Agent-Nativeアプリケーションを設計する

[[concepts/agent-native-product-management]] が示すように、これからのアプリケーションはAgentが使うことを第一に設計。

[[comparisons/open-harness-vs-agent-framework]] の設計原則:
> *"Harnessを捨てても業務ロジックが残るようにする"*

- 作るもの: Agentが叩くAPI + MCPツール群 + 状態管理層
- 人間向けUI: OpenClaw/Hermes/OpenCodeなどの汎用Harnessで十分
- 中核資産: データモデル・オントロジー・統合ロジック・評価データセット

#### ③ Service-as-Softwareの製品設計にシフトする

[[concepts/service-as-software]]: *"For every $1 spent on software, $6 is spent on services."*

ツール（Copilot）→ 成果（Autopilot）:
- ❌ 「AIが提案するCRM」→ ✅ 「AIがパイプラインを管理する」
- 課金: シート課金 → 解決済み会話あたり / 処理完了タスクあたり

---

## キャリア戦略の具体像

| 期間 | アクション | 狙い |
|---|---|---|
| 短期（3〜6ヶ月） | 現職でAgent-Nativeアーキテクチャにピボット。MCP対応・Harness Engineering導入・Evals構築 | SaaS→Agent Platformへの転換を主導 |
| 中期（6〜18ヶ月） | Service-as-Softwareの課金モデル実験。成果報酬型のパイロット顧客を獲得 | 従来SaaSの単価構造から脱却 |
| 長期（18〜36ヶ月） | 業界内での「Agent Runtime専門家」としてのポジショニング | Harness Engineeringの第一人者に |

### 最も差別化される能力セット

1. **Harness Engineering** — モデルではなく実行基盤を設計できる
2. **Ontology Design** — Palantir的な意思決定中心のデータモデルを構築できる
3. **MCPエコシステム設計** — Agentが使うツールの品質と発見可能性を設計できる
4. **Evals駆動開発** — 評価データセットを競争優位の源泉として蓄積できる

---

## 結論

SaaSを「去る」のではなく「再定義」する側に立つ:

- **作るものを変える**: 人間向けUI → Agent向けAPI・MCPツール・状態管理
- **売り方を変える**: シート課金 → 成果報酬（Service-as-Software）
- **競争優位の源泉を変える**: 機能数 → Harness品質・Evals・文脈蓄積
- **キャリアの軸を変える**: SaaSプロダクトマネージャー → Agent Runtime Architect / Harness Engineer

---

## ソース

- [[concepts/service-as-software]] — Sequoia Cap Julien Bek (Mar 2026)
- [[concepts/harness-engineering]] — Hamel Husain, Viv Trivedy, Addy Osmani, LangChain
- [[comparisons/open-harness-vs-agent-framework]] — kzinmr (May 2026)
- [[comparisons/agent-harnesses]] — Agent Harness比較
- [[concepts/agent-native-product-management]] — Marcus Moretti / Every Inc
- [[entities/palantir]] — FDEモデル
- [[concepts/ai-services-joint-ventures]] — OpenAI/Anthropic/AWSのJV戦略
- [[raw/newsletters/2026-05-05-why-saas-freemium-playbooks-don-t-work-in-ai]] — Lenny's Podcast (Vikas Kansal / Google)
- [[concepts/after-automation]] — Dan Shipper (Every)
- https://x.com/vtrivedy10/status/2052100726608781363
- https://sequoiacap.com/article/services-the-new-software/
- https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering
