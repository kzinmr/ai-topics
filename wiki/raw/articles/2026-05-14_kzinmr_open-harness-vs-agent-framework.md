---
title: "Open Harness 系と AI Agent Framework / Runtime 系の比較まとめ"
source: "kzinmr"
date: 2026-05-14
type: analysis
tags: [agent-harness, harness-engineering, agent-framework, comparison, agent-architecture]
url: "discord://hermes-topic-manager/1504369311249334283"
---

# Open Harness 系と AI Agent Framework / Runtime 系の比較まとめ

## 1. 全体結論

今回の検討で最も重要だった結論は、**Open Harness 系と Agent Framework / Runtime 系は、同じ「AI Agent基盤」に見えても、投資対象としてはかなり異なる**という点です。

Open Harness 系は、主に **人間がAI Agentを使うための操作環境・実行環境・作業面** への投資です。
OpenClaw、Hermes Agent、OpenCode、Pi などは、CLI、チャット、IDE、ローカル環境、MCP、ファイル操作、シェル実行、セッション、承認、サンドボックスなどを統合し、開発者や運用者がAI Agentを実際に使いやすくする方向に強みがあります。

一方、Claude Agent SDK、OpenAI Agents SDK、Google ADK、Strands Agents、LangGraph、Pydantic AI のような Agent Framework / Runtime 系は、主に **AI Agentをプロダクトや業務システムの中に組み込むための制御基盤** への投資です。状態管理、ツール呼び出し、評価、トレース、ガードレール、human-in-the-loop、durable execution、型安全性、デプロイ、監査などを設計しやすくする方向に強みがあります。

したがって、最終的な判断は次のようになります。

**Open Harness は「AIを人間が使う面」として非常に有望です。**
ただし、**中核業務ロジックや本番ワークフローの唯一の保管場所にするのは危険**です。

**Agent Framework / Runtime は「AIをシステムに組み込む面」として重要です。**
ただし、**特定ベンダーのSDKやクラウド機能に深く寄せすぎると、別種のロックインが発生します。**

最も堅い戦略は、Open Harness と Framework / Runtime を対立的に選ぶのではなく、**役割を分離して併用すること**です。

---

## 2. Open Harness 系の位置づけ

Open Harness 系は、AI Agentを動かすための **作業環境・操作面・実行面** に近い存在です。

典型的には、以下のような要素をまとめて扱います。

* チャット、CLI、IDE、Web UI などのインターフェース
* セッション管理
* ファイル読み書き
* シェル実行
* MCP やカスタムツール
* サンドボックス
* 承認フロー
* ローカル/リモート実行環境
* 長期メモリやスキル
* AGENTS.md、SYSTEM.md、カスタムプロンプト
* チームや個人の開発ワークフロー

このため Open Harness は、**人間の生産性向上には非常に効く**一方で、業務ロジックや状態が harness 内部に散らばりやすいというリスクも持ちます。

特に、便利に使えば使うほど、以下のようなものが蓄積されます。

* セッション履歴
* 独自プロンプト
* 独自スキル
* MCP設定
* permission設定
* local workspace構造
* custom command
* rollbackやcheckpointの運用
* チャットチャネルとユーザーIDの対応
* gateway側のroutingやapprovalルール

これらは、表面的には「設定」や「運用ノウハウ」に見えますが、実際には重要な技術資産になります。
したがって、Open Harness は open source であっても、**harnessロックイン**を起こし得ます。

---

## 3. Agent Framework / Runtime 系の位置づけ

Agent Framework / Runtime 系は、AI Agentを **アプリケーションや業務フローの一部として制御するための基盤** です。

主に以下のような領域を担います。

* agent loop
* tool calling
* function calling
* handoff
* graph / workflow
* typed state
* session
* durable execution
* retry
* checkpoint
* human-in-the-loop
* guardrail
* tracing
* evaluation
* observability
* deployment
* tenant / user / role separation
* audit log

こちらは Open Harness よりも初期設計が重くなりがちですが、**本番運用、監査、再現性、テスト、障害復旧、品質保証**には向いています。

---

## 4. Harness と Framework の本質的な違い

両者の違いは、単に「UI寄りかコード寄りか」ではありません。
より本質的には、**柔軟性の種類が違う**という点です。

Open Harness の柔軟性は、**広い柔軟性**です。
モデルを切り替える、CLIから使う、SlackやTelegramから使う、ローカルファイルに触る、シェルを叩く、MCPを足す、プロンプトを変える、agentの作業環境を変更する、といった柔軟性です。
これは探索、開発、運用補助、個人作業、少人数チームでは非常に強力です。

Framework / Runtime の柔軟性は、**深い柔軟性**です。
状態を型で管理する、graphで遷移を明示する、checkpointを保存する、tool callの副作用を制御する、承認フローをコード化する、評価とトレースを組み込む、tenantごとの実行境界を切る、といった柔軟性です。
これは初期実装が重くなりますが、プロダクト化や業務システム化に向いています。

したがって、Open Harness は **使う柔軟性** に強く、Framework / Runtime は **作る柔軟性・運用する柔軟性** に強い、と整理できます。

---

## 5. Security / Control / Ops の再評価

Harness 系の Control / Security / Ops を一律に低く採点するのは不適切。Harness系は **trusted operator workbench** として見るべき。

Framework / Runtime 側のSecurityは **product safety / tenant safety / workflow governance**。
Harness系のSecurityは **operator safety**（信頼された人間がagentを使うときの安全性）。

**Operator Workbench Readiness** では OpenClaw、Hermes、OpenCode、Pi は高評価。
**Untrusted Product Runtime Readiness** では LangGraph、Pydantic AI、OpenAI Agents SDK、Google ADK が有利。

---

## 6-11. 各ツールの個別評価

（OpenClaw、Hermes Agent、OpenCode、Pi、Claude Agent SDK、OpenAI Agents SDK、Google ADK、Strands Agents、LangGraph、Pydantic AI の詳細評価は comparison ページを参照）

---

## 12. ベンダーロックインの再整理

ロックインには複数種類がある：

1. **モデルロックイン**: Claude Agent SDKはClaude依存強、OpenAI Agents SDKはResponses API依存強
2. **SDKロックイン**: Frameworkの抽象への依存（handoff, guardrail, graph state等）
3. **Harnessロックイン**: Open Harnessの設定資産（AGENTS.md, permission, extension, memory, skills, gateway routing等）の蓄積
4. **クラウドロックイン**: Google ADK→GCP, Strands→AWS/Bedrock

---

## 13. 推奨アーキテクチャ

```text
Human Interface / Harness Layer
  OpenClaw / Hermes Agent / OpenCode / Pi

Tool Boundary
  MCP / HTTP APIs / typed function tools

Agent Control Layer
  LangGraph / Pydantic AI / OpenAI Agents SDK / Google ADK / Strands / Claude Agent SDK

State & Governance Layer
  DB / object storage / audit logs / eval datasets / traces / approval records

Execution Layer
  containers / sandbox / serverless / Kubernetes / CI runners
```

**Harnessを捨てても業務ロジックが残る**構成が理想。

---

## 14. 最終的な批判的総評

- **Open Harnessは、AI Agentを人間が使うための操作面として投資すべき**
- **Framework / Runtimeは、AI Agentをシステムに組み込むための制御面として投資すべき**
- **中核資産は、どちらにも閉じ込めず、自社所有のtool API、state、audit log、eval dataset、prompt registry、approval recordとして保持すべき**
- この分離ができれば、Open Harnessのスピードと柔軟性、Framework / Runtimeの信頼性と再現性を両方取れる
