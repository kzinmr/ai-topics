---
title: "Deep Agents Runtime"
type: concept
aliases:
  - deep-agents
  - agent-runtime
  - durable-execution
tags:
  - concept
  - agent-runtime
  - durable-execution
  - langchain
  - langsmith
  - orchestration
status: complete
description: "Production runtime primitives for deep AI agents — durable execution, memory, multi-tenancy, HITL, guardrails, observability, sandbox, and cron."
created: 2026-04-27
updated: 2026-04-27
sources:
  - "https://x.com/i/article/2046277232537256002"
related:
  - "[[concepts/harness-engineering]]"
  - "[[concepts/agent-loop-orchestration]]"
  - "[[concepts/durable-execution]]"
  - "[[concepts/human-in-the-loop]]"
---

# Deep Agents Runtime

> **Definition:** Deep AgentsはLangChain/Anthropicが構築したプロダクション対応エージェントランタイム。durable execution、memory、multi-tenancy、guardrails、HITL、observability、sandboxed code execution、scheduled cronをパッケージ化。

## 生産環境で必要とされるランタイム要件

### 1. Durable Execution (永続実行)
エージェントのループ（prompt → reasoning → tool call → observe → repeat）は数分〜数時間に及ぶ。単一の実行が数十回のモデル呼び出しやサブエージェントの生成を行うことがある。

**2つの核心要件:**
- **Long runs survive infrastructure failures** — ワーカープロセスが死んでも、トークン代とtool callを無駄にしない。最後の完了ステップからresumeする
- **Agents can stop and wait** — ヒトの承認を待機する際、ワーカープロセス/クライアント接続を占有しない。リソースを解放し、後で再開する

**実装:**
- 管理されたtask queue + automatic checkpointing
- 各super-stepがPostgreSQL（デフォルト）にcheckpointをwrite（thread_idでkey）
- ワーカー障害時はleaseがreleaseされ、別のワーカーがlatest checkpointから再開
- 可変retry policies（backoff、max attempts、per-node exception）

### 2. Memory — 2層メモリ構造
- **Short-term memory** — シングル会話内で蓄積される。checkpointに保存、thread_idでスコープ。会話終了後消失
- **Long-term memory** — 会話間を横断する。ユーザー設定、プロジェクト規約、知識ベース。namespace tuplesでorganized（例: `(user_id, "memories")`）

**Long-term Memoryの保存場所:**
- Agent Serverのbuilt-in store（key-value interface）
- PostgreSQL backed、semantic search via embeddings
- namespaceでuser/assistant/orgごとにスコープ可能
- APIで直接query可能

### 3. Multi-tenancy — 3層分離
1. **Data isolation** — Custom auth middleware（`@auth.authenticate`）。リソースにownership metadataをタグ付け
2. **Agent acting on behalf of user** — Agent AuthがOAuth danceとtoken storageを処理。ユーザーは1回認証、エージェントがその後で代わりに行動
3. **Operator-level access control** — RBACでチームメンバーのデプロイ/設定/トレース権限を管理

### 4. Human-in-the-Loop (HITL)
2つのシチュエーション:
- **Tool call review** — 重要なアクション（メール送信、金融取引、ファイル削除）前にヒトが承認
- **Clarifying question** — ヒトの判断/好みに依存する判断ポイント

**実装:**
- `interrupt()` — 実行をpauseしpayloadをcallerにsurface
- `Command(resume=...)` — ヒトのresponseでresume
- checkpointがdurable storageに保存。resumeは任意のJSON-serializable value（approve/rejectだけでなく、edited draft、missing context、computed results）

### 5. Real-time Interaction
- **Streaming** — partial outputをリアルタイムでclientにflow。4モード: full state snapshots、state updates only、token-by-token LLM output、custom events
- **Thread streaming** — 長寿接続、follow-up/background/HITL-resumptionをすべて同じthreadでdelivery。`Last-Event-ID`でresume
- **Double-texting** — 新しいmessageが古いrun中に送られてきた場合:
  - `enqueue`（デフォルト）: 待機してsequential処理
  - `reject`: 新しいinputを拒否
  - `interrupt`: 現在のrunをhaltし、new inputをそのstateから処理
  - `rollback`: 現在のrunをhaltし、すべてのprogressをrevertしてfresh runとして処理

### 6. Guardrails (Middleware)
2つの主要ケース:
- **PII Redaction** — モデルが見る前にsensitive dataをredact。every model callでdeterministically実行
- **Cap expensive operations** — 有料external APIの呼出数をper runでキャップ

**LangChain built-in middleware:**
PIIRedactionMiddleware, ModelRetryMiddleware, ModelFallbackMiddleware, ToolCallLimitMiddleware, SummarizationMiddleware, HumanInTheLoopMiddleware, OpenAIModerationMiddleware

**Hooks:** `before_model`, `wrap_model_call`, `wrap_tool_call`, `after_model`

### 7. Observability & Time Travel
- 実行ツリーをout of the boxで取得（model calls、tool calls、subagent runs、middleware hooks）
- 費用/エラー/ユーザー/カスタムタグでfilter
- **Polly** — LangSmith AI assistantがtracesを分析しcommon failure modes/slow tool calls/repeated patternsをsurface
- **Online Evals** — LLM-as-judge or custom scorers for production traces
- **Time Travel** — checkpointからrewindしstateをmodifyしてbranch。fork元のthreadは保持。LLM/tool call/interruptがすべてre-triggerされる

### 8. Sandboxed Code Execution
- **Sandbox backends:** Daytona, Modal, Runloop, LangSmith Sandboxes（private preview）
- LangSmith Sandboxes: templates for container images/resource limits/volumes, warm pools for cold start elimination, auth proxy sidecarでcredentials never enter sandbox

### 9. Integrations
- **MCP** — Model Context Protocol（標準化されたagent-tool/data接続）
- **A2A** — Agent-to-Agent standard（multi-agent architectures across deployments）
- **Webhooks** — run completionでdownstreamをkick off
- **Cron** — scheduled runs（stateful: threadにtie, stateless: fresh thread per execution）

### 10. Open Harness (Lock-in avoidance)
- MIT licensed harness + fully open source
- AGENTS.md（open standard）for agent instructions
- Open protocols: MCP, A2A, Agent Protocol
- inspection/customization/extension of every layer（rate limits, retry logic, model fallback, PII detection, file permissions）

## 関連リソース
- [Going to Production Guide](https://docs.deepagents.ai) — credential management, async patterns, frontend integration
- [LangSmith Deployment & Agent Server docs](https://docs.langchain.com)
- [Deep Agents deploy docs](https://docs.deepagents.ai/deploy)

## Sources
- [The runtime behind production deep agents](https://x.com/i/article/2046277232537256002) (2026-04-26, X article) — durable execution, HITL, double-texting, guardrails, observability, time travel, sandbox, cron
