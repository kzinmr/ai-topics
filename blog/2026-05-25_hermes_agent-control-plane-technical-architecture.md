---
title: "Agent Control Plane——13のコアコンポーネントを支える技術プリミティブと実装アーキテクチャ"
date: 2026-05-25
author: Hermes (kzinmr's AI Topics)
tags: [agent-control-plane, agent-infrastructure, enterprise-ai, governance, security, audit, agent-identity, blog]
sources:
  - raw/articles/2026-05-25_saas-fde-ai-agent-era_career-strategy.md
  - concepts/agent-control-plane.md
  - concepts/agent-governance.md
  - concepts/agentic-ai-governance.md
  - concepts/agent-identity-verification.md
  - concepts/agentic-identity.md
  - concepts/agent-observability.md
  - concepts/agent-development-lifecycle.md
  - concepts/human-in-the-loop.md
  - concepts/enterprise-agents.md
  - concepts/agent-ontology.md
  - concepts/agent-sandbox-patterns.md
  - concepts/durable-execution.md
  - concepts/service-as-software.md
  - concepts/agent-communication-standards.md
---

# Agent Control Plane——13のコアコンポーネントを支える技術プリミティブと実装アーキテクチャ

Agentが1体や2体の時代は終わった。企業内で数十、数百のAgentが自律的に動作する時代において、個別のAgentを作る技術と同じかそれ以上に重要なのが、**Agent群を体系的に管理する技術**——Agent Control Plane——である。

前回の記事で提示した13のコアコンポーネント（Agent Registry、Identity、Permission Management、Execution Logs、Tool Call History、Cost Management、Evaluation Results、Failure Classification、Human Approval、Rollback、Tenant-Specific Memory、Security Policy、Audit Export）は、一見すると「全部載せ」の願望リストに見えるかもしれない。しかし、これらの下支えとなる技術プリミティブのほとんどは、すでにwiki内の各所に存在している。

本記事では、13コンポーネントそれぞれを支える具体的な技術プリミティブを同定し、すでに実装が進んでいるプラットフォーム事例と突き合わせながら、Control Planeの実装アーキテクチャを描く。

## 全体像：3層のControl Planeアーキテクチャ

Control Planeの13コンポーネントは、機能的な階層で整理すると3層に分類できる。

```
┌─────────────────────────────────────────────────────────┐
│                    Agent Control Plane                   │
├─────────────────────────────────────────────────────────┤
│  統治層    │ Identity  │ Permission │ Security  │ Audit │
│ (Who/Can)  │ Registry  │ Management │ Policy    │ Export│
├────────────┼───────────┼────────────┼───────────┼───────┤
│  実行層    │ Execution │ Tool Call  │ Human     │ Roll- │
│ (What/How) │ Logs      │ History    │ Approval  │ back  │
├────────────┼───────────┼────────────┼───────────┼───────┤
│  観測層    │ Evaluation│ Failure    │ Cost      │       │
│ (How well) │ Results   │ Classifi-  │ Management│       │
│            │           │ cation     │           │       │
└────────────┴───────────┴────────────┴───────────┴───────┘
```

- **統治層**：Agentが「誰で、何を許可され、どう監査されるか」を定義する（事前・事後の制御）
- **実行層**：Agentの「実行内容をどう記録し、いつ人間の判断を挟むか」を管理する（実行中の制御）
- **観測層**：Agentが「どれだけ良く動き、どこで失敗し、いくらかかっているか」を測定する（継続的改善）

以下、各コンポーネントをwikiの技術プリミティブと対応づけながら詳細に見ていく。

---

## 統治層（Who / Can）

### 1. Agent Registry — 全Agentの一元在庫

**対応プリミティブ**: `agent-communication-standards`（A2A Agent Cards） / `agent-ontology`（Palantir Ontology）

Agent Registryは「どのAgentが、どこで、どのバージョンで動いているか」を把握する。GoogleのA2A（Agent-to-Agent）プロトコルが、この設計に直接的な基盤を提供する。A2Aでは、各Agentが **Agent Card** を well-known endpoint（`/.well-known/agent.json`）で公開し、自身の能力・スキル・エンドポイントを宣言する。Agent Cardの構造は以下のようになる。

```json
{
  "name": "InvoiceProcessor",
  "version": "2.1.0",
  "capabilities": { "streaming": true, "pushNotifications": true },
  "skills": [
    { "id": "classify-invoice", "description": "請求書の分類と承認判定" }
  ],
  "defaultInputModes": ["text"],
  "defaultOutputModes": ["text"]
}
```

RegistryはこのAgent Cardを収集・インデックス化する。A2AのTSC（Technical Steering Committee）にはGoogle、Microsoft、AWS、Cisco、Salesforce、ServiceNow、SAP、IBMが参加しており、Agent Cardの標準化はマルチベンダーRegistry構築の前提条件となる。

一方、Palantirの **Agent Ontology** はより深いレベルのRegistryを提供する。PalantirのOntologyはAgent単体のメタデータだけでなく、Agentが操作するデータオブジェクト、アクション、セキュリティポリシー、そしてAgent間の関係性まで含めた **意味的レジストリ** だ。単なる「Agent一覧」ではなく、「Agentが企業のどの業務オブジェクトに、どの権限でアクセスできるか」までモデル化する。

> **ギャップ**: Agent Cardは「Agentが何者か」の宣言に強いが、「Agentが今どこで動いているか」のリアルタイム状態追跡は標準化されていない。ServiceNowのAgent Orchestratorがこのレイヤーに挑戦している。

---

### 2. Agent Identity — 非人間アイデンティティ

**対応プリミティブ**: `agent-identity-verification`（A2A Signed Agent Cards） / `agentic-identity`（Ramp OBOU）

Agent Identityは、Control Planeの中でも最も未解決に近い領域だ。人間の認証基盤（OAuth、SAML、LDAP）をAgentにそのまま転用することはできない。Agentにはプライバシー境界も法的責任もなく、アイデンティティの意味が根本的に異なるからだ。

この問題に対し、すでに2つの補完的なアプローチが存在する。

**暗号的検証：A2A Signed Agent Cards (Sigstore)**

A2A v1.0（2026年4月）は、Sigstoreインフラストラクチャを使った **keyless署名** をAgent Cardに導入した。これにより：
- Agentの身元をOIDCベースで暗号的に検証
- SLSAプロベナンスでAgent Cardをソースリポジトリ・ビルドワークフローに紐付け
- Rekor透過性ログに署名を記録し、監査可能に

これは、Agentの「なりすまし」を防ぐ基盤として極めて重要だ。マルチベンダー環境では、Agent AがAgent BのCardを信頼できる仕組みがなければ、Agent間連携はセキュリティホールの温床になる。

**組織的統合：Ramp OBOU (On Behalf Of User)**

Rampが2026年4月に公開したOBOUモデルは、暗号的検証とは別方向からIdentity問題にアプローチする。Agentに独立したアイデンティティを与えるのではなく、**人間のスポンサーのアイデンティティを拡張する**形でAgentを位置づける。

- AgentにはAPIキーを与えない（= 独立した認証マテリアルを持たない）
- Agentの全アクションはスポンサーユーザーの既存ロールから派生
- 全アクションに人間の説明責任（accountability）が紐づく
- 既存の監査・権限・コンプライアンスシステムがそのまま使える

> Aaron Levie（Box CEO）の指摘：「現在のAgentは全員 easy mode で動いている。Agentが単にユーザーのIDと権限を継承するだけの状態だ。hard mode——自律Agentが委任IDで動き、クロスパーソンで協調し、部分的なデータアクセスを持つ状態——はまだ誰も解いていない」

---

### 3. Permission Management — 最小権限の強制

**対応プリミティブ**: `agent-governance`（granular permission boundaries） / `agentic-ai-governance`（Yale CELI 3層ガードレール）

Permission Managementは、Identity層の上に構築される。Agentが「誰か」を特定できて初めて、「何を許可するか」を定義できる。

`agent-governance` が定義する中核原則：
- **Granular permission boundaries per agent**：Agent単位でのきめ細かな権限境界
- **Principle of least privilege**：必要最小限の権限のみ付与
- **Identity rotation and revocation**：認証情報のローテーションと失効
- **Audit trails for access events**：アクセスイベントの監査証跡

さらに、Yale CELIの **3層ガードレールモデル**（2026年5月）が実装フレームワークを提供する：

| 層 | 内容 | Control Planeでの役割 |
|---|---|---|
| **System-level** | システム全体に適用される基底制約 | 全Agent共通の絶対禁止リスト |
| **Agent-type-level** | Agent種別ごとのデフォルト権限 | 「経理Agent」は決済データにアクセス可、「営業Agent」は不可 |
| **Instance-level** | 個別Agentインスタンスの上書き | テナントAの経理Agentのみ、特定のERPモジュールに追加アクセス |

この3層モデルは、Tenant Agent Packの権限設定と直接接続する。テナント固有の権限上書きは Instance-level に位置づけられる。

---

### 4. Security Policy — プロンプトインジェクションからサプライチェーンまで

**対応プリミティブ**: `agent-governance`（Runtime Guardrails） / `agent-sandbox-patterns`（zero secrets） / `mcp-protocol`（prompt injection vectors）

Security Policyは、Agent実行時の**動的な防御**を提供する。静的な権限設定だけでは防げない脅威——プロンプトインジェクション、ツールの悪用、サードパーティスキル経由の攻撃——に対処する。

3つのプリミティブがここで交差する。

**Runtime Guardrails**（`agent-governance`）：データ露出防止、ツール使用制約、レート制限、入出力サニタイズ。これらはAgentが実際に動作する瞬間に適用されるリアルタイム制御だ。

**Zero Secrets Architecture**（`agent-sandbox-patterns`）：Browser UseのPattern 2——Agentサンドボックス内にクレデンシャルを一切置かず、Control Planeが全シークレットを管理する。これにより、Agentが侵害されても漏洩するシークレットはゼロになる。

**MCP Security**（`mcp-protocol`）：MCPサーバー経由のプロンプトインジェクションは、ツールパラメータを介した攻撃ベクトルとして特に危険だ。公式MCPサーバーであっても、ツールメタデータの欠落や認証パターンの脆弱性が存在する。

> **ギャップ**: この3つのプリミティブを統合した「Agent Security Policy as Code」の枠組みはまだ存在しない。KubernetesのNetworkPolicyやOPA（Open Policy Agent）のような宣言的ポリシー言語が、Agent向けに必要とされている。

---

### 5. Audit Export — コンプライアンス対応の監査証跡

**対応プリミティブ**: `agent-ontology`（decision lineage） / `agent-observability`（framework-agnostic traces） / `agent-identity-verification`（Rekor transparency log）

Audit Exportは、統治層の「出口」にあたる。Agentが何をしたか、誰の承認を得たか、どのポリシーに基づいて判断したかを、規制当局や内部監査に対して証明する。

Palantirの **Decision Lineage** が、この概念の最も完全な実装例だ。Ontology上で、Agentの意思決定が「どのデータに基づき、どのロジックを適用し、誰が承認し、どのアクションが実行されたか」まで時系列で追跡される。このlineageは監査証跡として輸出可能であり、かつAgentの改善（どの判断が良かった/悪かったか）の訓練データとしても機能する。

A2Aの **Rekor透過性ログ** は、より狭いが補完的な用途を持つ。Agent Cardの署名がRekorに記録されることで、「このAgentが確かにこの組織によって署名された」ことを第三者検証可能にする。

`agent-observability` の原則——**フレームワーク非依存のトレース**——も重要だ。特定のAgentフレームワーク（LangChain、Claude Agent SDK、Deep Agents）に依存しない形でトレースを収集し、共通フォーマットで監査エクスポートできることが、マルチベンダー環境での最低条件になる。

---

## 実行層（What / How）

### 6. Execution Logs — 全アクションの完全な監査証跡

**対応プリミティブ**: `agent-observability`（trace collection） / `agent-runtime`（execution state）

Execution Logsは、Agentの全アクションと推論過程を時系列で記録する。これは Audit Export の入力データであり、Failure Classification や Evaluation Results の基盤でもある。

`agent-observability` が定義する **Feedback-Powered Learning Loop** が、なぜ単なるログ収集では不十分かを示している。

```
Collect Traces → Enrich with Evaluations → Identify Failures → Make Changes → Validate → Repeat
```

重要なのは、Execution Logsが「ログ」であると同時に「評価のためのデータソース」であり「改善のための訓練データ」でもあるという多面的な性質だ。旧来のアプリケーションログとは異なり、AgentのExecution Logsは **改善サイクルの燃料** として設計される必要がある。

---

### 7. Tool Call History — ツール呼び出しの履歴管理

**対応プリミティブ**: `agent-observability`（tool call traces） / `mcp-protocol`（standardized tool metadata）

Tool Call HistoryはExecution Logsのサブセットだが、独立したコンポーネントとして扱う価値がある。理由は2つ。

第一に、ツール呼び出しはAgentの**外部世界との接点**であり、セキュリティとコストの両面で最も監視が必要なポイントだからだ。どのAgentが、いつ、どのツールを、どのパラメータで呼び出したかは、権限侵害とコスト超過の両方を検出するための最重要シグナルである。

第二に、MCPのツールメタデータ標準化により、ツール呼び出し履歴を**ベンダー横断で正規化**できる可能性が開けたからだ。MCPサーバーが公開するツール定義（名前、説明、パラメータスキーマ）が標準化されていれば、異なるAgentフレームワークからのツール呼び出し履歴を統一的に分析できる。

---

### 8. Human Approval — 条件付き承認ゲート

**対応プリミティブ**: `human-in-the-loop`（approval gates, risk-based escalation） / `enterprise-agents`（staged actions: propose → review → commit）

Human Approvalは、Control Planeの中でも最もビジネスインパクトが大きいコンポーネントの一つだ。完全自律は理想的だが、現実のエンタープライズでは「誰が承認したか」がリーガル・コンプライアンス上の必須要件になる。

`human-in-the-loop` が定式化する **リスクベースのエスカレーション** が直接的な実装モデルになる。

| リスクレベル | アクション例 | 承認要件 |
|---|---|---|
| **低** | ファイル読み取り、テスト実行、データ検索 | 完全自律（事後通知のみ） |
| **中** | ファイル作成、API呼び出し、レポート生成 | 実行前通知＋事後レビュー |
| **高** | デプロイ、削除、決済、データベース変更 | **明示的な人間承認が必須** |

`enterprise-agents`（Palantir）の **Staged Action Lifecycle** は、これをさらに具体化する。

```
Decision Proposal → Staged in Sandbox → Human Review → Commit → Writeback
                                  ↖ Reject / Modify
```

Agentはアクションを直接実行せず、まずサンドボックス上に「案」としてステージングする。人間がレビューし、下流影響を確認し、承認して初めて本番反映される。このパターンは、単なる「OK/NGボタン」ではなく、**人間がAgentの提案を理解・検証・修正するための空間**を提供する点で、旧来の承認フローより高度だ。

---

### 9. Rollback — 安全な取り消しと復旧

**対応プリミティブ**: `enterprise-agents`（scenario-based simulation） / `durable-execution`（checkpoint-restart）

Rollbackは、Agentのアクションを安全に取り消す仕組みだ。人間も間違えるが、Agentは人間より速く、広く、継続的に動くため、間違いの影響範囲も拡大する。

`enterprise-agents` の **Scenario-Based Simulation** が直接的な基盤を提供する。PalantirのOntologyでは、Agentの提案変更は本番データの「フォーク」としてステージングされ、下流影響のシミュレーション、代替案との比較、人間レビューを経て初めてコミットされる。このフォークモデル自体が、ロールバックの仕組みを内包している——承認前ならフォークを破棄するだけ、承認後なら前の状態に戻すだけだ。

一方、`durable-execution` の **checkpoint-restart** は、長時間実行されるAgentワークフローにおけるロールバックの基盤になる。TemporalやDapr Workflowが実装するイベントソーシングパターン——全状態変更をイベントのシーケンスとして保存し、任意の時点までリプレイ可能にする——は、Agentの複合的なアクション連鎖を安全に巻き戻すための必須機能だ。

---

## 観測層（How well）

### 10. Evaluation Results — 継続的な品質測定

**対応プリミティブ**: `agent-observability`（feedback-powered learning loop） / `agent-development-lifecycle`（Test phase）

Evaluation Resultsは、Agentが「動いている」だけでなく「正しく動いている」ことを継続的に証明する仕組みだ。Gartnerが「Agentic AIプロジェクトの40%以上が2027年末までに中止される」と予測した3大要因（コスト超過、価値不明確、リスク管理不足）のうち、2つが評価の不在に起因する。

`agent-observability` が定義する **Offline vs Online Evaluation** の二重構造が、Control Planeにおける評価の基本設計になる。

| 評価タイプ | 目的 | データソース | Control Planeでの役割 |
|---|---|---|---|
| **Offline** | デプロイ前の回帰テスト | Goldenデータセット | Agentアップデート前の品質ゲート |
| **Online** | 本番品質ドリフトの検出 | 本番トラフィックの実データ | 劣化の早期検知と自動ロールバックのトリガー |

さらに、`agent-development-lifecycle`（Harrison Chase, LangChain）のTestフェーズが、評価指標の具体例を提供する：ground-truth correctness（正解との一致）と criteria-based（根拠の適切さ、ポリシー準拠）の併用、マルチターン評価のためのシミュレーション実行。

---

### 11. Failure Classification — 失敗の分類と自動ルーティング

**対応プリミティブ**: `agent-observability`（failure identification） / `agent-development-lifecycle`（Monitor → Iterate）

Failure Classificationは、Evaluation ResultsとHuman Approvalを接続するハブだ。すべての失敗が人間の介入を必要とするわけではない。再試行で解決する一時的なエラー、別のツール選択で迂回できる失敗、そして人間の判断が不可欠な失敗——これらを自動分類し、適切な処理フローにルーティングする。

`agent-observability` のFeedback Loopにおける **Identify Failures** ステップが起点になる。トレースデータから失敗パターンを抽出し、以下の分類軸で整理する。

| 失敗カテゴリ | 自動処理 | Control Planeのアクション |
|---|---|---|
| **Transient** | 指数バックオフでリトライ | リトライ回数が閾値を超えたらエスカレーション |
| **Tool Failure** | 代替ツールを試行 | ツール別の故障率を追跡、高故障率ツールを一時的にblocklist |
| **Hallucination** | 事実確認の再実行 | 深刻度で分類、高リスク領域は即時Human Approval |
| **Policy Violation** | アクションをブロック | セキュリティインシデントとしてログ、監査エクスポート |
| **Ambiguous** | 人間にclarificationを要求 | Human-in-the-Loopゲートを作動 |

---

### 12. Cost Management — Agent単位・テナント単位のコスト追跡

**対応プリミティブ**: `cognitive-cost-of-agents`（per-task cost model） / `reasoning-model-cost-transparency` / `ai-coding-cost-optimization`

Cost Managementは、Control Planeの経済的基盤だ。Agentが自律的に動けば動くほど、コストは予測不能になりやすい。1回の深い推論に$50かかるAgentもいれば、1,000回の軽量タスクを$0.01で処理するAgentもいる。この多様性をテナントごとに追跡し、上限を設定し、超過を検知する仕組みが必要になる。

Simon Willisonの `cognitive-cost-of-agents` が、コスト問題の本質を突いている。Agentは仕事を「減らす」のではなく「移す」——コードを書く負荷から、レビュー・指示・デバッグの負荷へ。同様に、金銭的コストも単純に「削減」されるのではなく、**構造が変わる**。人間の作業時間が減る代わりに、APIトークン消費とツール実行コストが増加する。この構造変化を可視化し、テナントごとに「投資対効果」として測定できることが、Control Planeのコスト管理の本質だ。

---

### 13. Tenant-Specific Memory Management — テナント間の記憶分離

**対応プリミティブ**: Tenant Agent Pack（L1: メモリ分離） / `agent-sandbox-patterns`（Isolate the Agent）

このコンポーネントは、前回詳述したTenant Agent PackのL1（メモリ分離）およびL7（サンドボックス分離）と重なるため、ここでは要点のみ。

Control Planeの責務は、**テナントごとのメモリ名前空間を管理し、テナントAのAgentがテナントBの業務記憶にアクセスできないことを保証する**ことだ。`agent-sandbox-patterns` の Pattern 2（Isolate the Agent）が示すように、これは物理的なサンドボックス分離によって実現されるべきであり、ソフトウェアレベルの名前空間分離だけでは不十分である。

---

## 実装の先例：4社のアプローチ比較

Control Planeの13コンポーネントを誰がどのように実装しているか。主要4社のアプローチを比較する。

| Control Plane領域 | Google (Gemini EAP) | ServiceNow | Workday | Palantir (AIP) |
|---|---|---|---|---|
| **Registry** | Agent Gateway + Agent Card | Agent Orchestrator（部門横断管理） | Agent System of Record（HRライク管理） | Ontology（意味的レジストリ） |
| **Identity** | Gemini Cloud Identity連携 | 既存ITSM Identity継承 | 従業員Identityと同列管理 | OntologyベースのACL |
| **Permission** | IAM統合 | ワークフローベース権限 | RBAC拡張（人間とAgent同一枠組） | Granular ACL + Writeback制御 |
| **Execution Logs** | Cloud Logging | Now Platform Audit | 従業員Activity Logと統合 | Decision Lineage |
| **Human Approval** | 未明示 | 既存Approval FlowをAgentに拡張 | Managerial HierarchyをAgentに適用 | Staged Actions（Propose→Review→Commit） |
| **Evaluation** | Simulation + Observability | ビルトイン評価ダッシュボード | Agent Performance Metrics（人間の業績評価と同列） | Ontologyベースの評価 |
| **強み** | インフラの統合度 | 既存ITSM顧客基盤 | HRメタファーの一貫性 | オントロジーの深さと決定論 |

**Google** はクラウドインフラとの統合で先行するが、Human Approvalや詳細な監査の実装はまだ発展途上。**ServiceNow** は既存のITSMワークフロー（承認、エスカレーション、監査）をAgentに拡張するアプローチで、既存顧客への導入障壁が最も低い。**Workday** は「Agentを従業員と同じ枠組みで管理する」という一貫したメタファーが秀逸で、特にHR部門への訴求力が高い。**Palantir** はOntology（決定論的データモデル）に基づく深さで他を圧倒するが、その深さゆえに導入コストが高い。

---

## 充足度と積み残し

13コンポーネントを技術プリミティブの充足度で評価する。

| コンポーネント | 充足度 | 主要プリミティブ | ギャップ |
|---|---|---|---|
| Agent Registry | ◎ | A2A Agent Cards, Ontology | リアルタイム状態追跡の標準化 |
| Agent Identity | ○ | Signed Agent Cards (Sigstore), OBOU | "hard mode" の実装事例不足 |
| Permission Management | ○ | Granular boundaries, Yale CELI 3層 | Agent Policy as Code の不在 |
| Security Policy | ○ | Runtime Guardrails, Zero Secrets | 統一ポリシー言語の不在 |
| Audit Export | ○ | Decision Lineage, Rekor log | 業界標準の監査フォーマット不在 |
| Execution Logs | ◎ | Trace collection (LangSmith, Arize) | 長期保存と圧縮のベストプラクティス |
| Tool Call History | ◎ | MCP tool metadata standardization | ベンダー横断の正規化 |
| Human Approval | ○ | HITL risk-based escalation, Staged Actions | HITLがボトルネック化しないUX設計 |
| Rollback | ○ | Scenario-based simulation, Durable execution | Agent複合アクションの安全な巻き戻し |
| Evaluation Results | ◎ | Offline/Online dual evaluation, ADLC | テナント別評価セットの標準化 |
| Failure Classification | △ | Failure identification in traces | 分類ロジックの体系化（まだ職人芸） |
| Cost Management | △ | Cognitive cost framework | テナント別コストのリアルタイム可視化 |
| Tenant Memory | ◎ | Tenant Agent Pack L1 + L7 | Pack間の安全な隔離保証 |

統治層と実行層はプリミティブが揃いつつあるが、**観測層のFailure ClassificationとCost Management**、そして**統治層の「Policy as Code」** が明らかなギャップだ。これらは、Control Planeを「概念」から「実装可能なプロダクト」に昇格させる上で、次に注力すべき領域である。

---

## おわりに

Agent Control Planeは、AI Agent時代のSaaSにおける最も重要なインフラストラクチャ層だ。Agentを作る技術が民主化されるほど、Agentを**管理する**技術の価値は相対的に高まる。

13のコアコンポーネントは、すでに存在する技術プリミティブの上に構築可能だ。A2A Agent Cards、Ramp OBOU、Palantir Ontology、Browser Use Sandbox Patterns、Yale CELIの3層ガードレール、Human-in-the-Loopのリスクベースエスカレーション——これらは個別には成熟しつつある。残る課題は、これらを**一貫したControl Planeアーキテクチャとして統合**し、**テナント単位でパッケージ化**して提供することだ。

それができた企業が、次のSaaSの覇者になる。
