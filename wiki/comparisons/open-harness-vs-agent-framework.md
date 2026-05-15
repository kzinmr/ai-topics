---
title: "Open Harness 対 Agent Framework/SDK — 投資対象としての本質的差異"
created: 2026-05-14
updated: 2026-05-15
type: comparison
tags:
  - comparison
  - agent-harness
  - agent-framework
  - harness-engineering
  - ai-agents
aliases: ["harness-vs-framework", "harness-vs-sdk"]
sources:
  - "raw/articles/2026-05-14_kzinmr_open-harness-vs-agent-framework.md"
  - "raw/articles/2026-05-15_kzinmr_agent-stack-architecture-comparative-analysis.md"
  - "raw/articles/2026-05-15_kzinmr_why-runtime-centric-now-control-flow-ownership.md"
related:
  - concepts/agent-harness
  - concepts/harness-engineering
  - comparisons/agent-harnesses
  - entities/atal-upadhyay
---

# Open Harness 対 Agent Framework/SDK — 投資対象としての本質的差異

## 要約

**Open Harness 系と Agent Framework / Runtime 系は、同じ「AI Agent基盤」に見えても、投資対象としてはかなり異なる。**

- **Open Harness** = 人間がAI Agentを**使う**ための操作環境・実行環境・作業面への投資
- **Agent Framework / Runtime** = AI Agentを**システムに組み込む**ための制御基盤への投資

最も堅い戦略は、両者を対立的に選ぶのではなく、**役割を分離して併用すること**。

---

## 1. 両者の本質的差異

### 1.1 定義

| 軸 | Open Harness | Agent Framework / Runtime |
|---|---|---|
| **目的** | 人間がAI Agentを操作・実行する作業面 | AI Agentをアプリケーション/業務システムに組み込む制御面 |
| **主な利用者** | 開発者、運用者、個人、少人数チーム | プロダクト開発チーム、業務システムチーム |
| **メンタルモデル** | 「タスクを与えて走らせる」 | 「状態遷移を持つシステムとして設計する」 |
| **制御フロー** | 固定された `while` ループ + escape hatches | ユーザー定義の graph / state machine |
| **抽象度** | 完成品（すぐ使える） | 部品（組み立てが必要） |

### 1.2 柔軟性の種類が違う

| | Open Harness（広い柔軟性） | Framework / Runtime（深い柔軟性） |
|---|---|---|
| **何が柔軟か** | モデル切替、CLI/チャット/IDEの選択、ファイル・シェル操作、MCP追加、プロンプト変更 | 型付き状態管理、graph遷移、checkpoint保存、副作用制御、承認フローコード化、tenant境界 |
| **向いている場面** | 探索、開発、運用補助、個人作業、少人数チーム | プロダクト化、業務システム化、本番運用 |
| **初期コスト** | 低（すぐ使える） | 高（設計・実装が必要） |
| **表現** | **使う**柔軟性 | **作る・運用する**柔軟性 |

### 1.3 Security / Control / Ops の質が違う

| | Open Harness | Framework / Runtime |
|---|---|---|
| **Securityの種類** | **Operator Safety**（信頼された人間の操作安全性） | **Product / Tenant Safety**（信頼できないユーザー・複数tenantの安全性） |
| **守るもの** | ファイル・シェル・MCPの誤操作防止 | PII管理、権限分離、監査、SLA |
| **評価軸** | Operator Workbench Readiness | Untrusted Product Runtime Readiness |
| **代表的ツールの強み** | OpenClaw: gateway/control plane、Hermes: persistent personal agent、OpenCode: coding workbench | LangGraph: stateful durable execution、Pydantic AI: typed application framework |

---

## 2. Open Harness 系 詳細

### 2.1 共通する特性

Open Harness 系が扱う要素:
- チャット、CLI、IDE、Web UI などのインターフェース
- セッション管理、ファイル読み書き、シェル実行
- MCP やカスタムツール、サンドボックス、承認フロー
- ローカル/リモート実行環境、長期メモリやスキル
- AGENTS.md、SYSTEM.md、カスタムプロンプト

**強み**: 人間の生産性向上に非常に効く。
**リスク**: 業務ロジックや状態が harness 内部に散らばりやすい。open source であっても **harnessロックイン**を起こし得る。

Harnessロックインを構成する資産:
- セッション履歴、メモリ、スキル、custom command
- approval運用、sandbox設定、MCP設定
- workspace layout、agent routing、chat identity mapping
- チャットチャネルとユーザーIDの対応、gateway routing/approvalルール

### 2.2 OpenClaw — Agent Control Gateway / Operator Workbench

| 評価軸 | 判定 |
|---|---|
| **本質** | Agent gateway / control plane。agentそのものを作るのではなく、**人間、チャットチャネル、agent harness、workspace、approval、sandbox、tool policyを接続する** |
| **強み** | Slack/Telegram/Discord/Google Chat/iMessage/Matrix/Teams/Signal/WhatsApp 対応。session routing、transcript mirror、approval、tool policy、sandbox設定、model fallback/live switching、agent runtime差し替え余地 |
| **Operator Workbench Readiness** | ★★★★☆ 高い（trusted operator / trusted teamでは強い） |
| **Untrusted Product Runtime** | ★★☆☆☆ 低い（tenant isolation、credential isolation、監査、RBAC、policy enforcementの追加設計が必要） |
| **総評** | agent product runtime というより、**agent control gateway / operator workbench** として評価すべき |

### 2.3 Hermes Agent — Persistent Personal Agent / Self-Improving Workbench

| 評価軸 | 判定 |
|---|---|
| **本質** | 常駐し、記憶を持ち、スキルを蓄積し、複数チャネルから操作できる **persistent ops agent**。単発のcoding agentではない |
| **強み** | Telegram/Discord/Slack/WhatsApp/Signal/Email/CLI対応。persistent memory、auto-generated skills、cron、isolated subagents、container isolation、checkpoint/rollback、MCP credential filtering |
| **Operator Workbench Readiness** | ★★★★★ 非常に高い（個人または信頼チームのAI operating layerとして有望） |
| **リスク** | 長期メモリ・自己改善・自動スキル生成・cron・subagentにより**状態が肥大化し挙動の説明可能性が低下**。どのmemoryが挙動に影響したか・どのskillがいつ生成/変更されたかの管理が必要 |
| **総評** | 顧客向けproduct runtimeより、**自分専用または信頼チーム向けのAI operating layer**として評価すべき |

### 2.4 OpenCode — Practical Coding Harness

| 評価軸 | 判定 |
|---|---|
| **本質** | 最も実用的なcoding harness。terminal/desktop app/IDE extension |
| **強み** | 75+ LLM provider対応（モデルロックイン低）、MCP/custom tools、permission（bash/edit/read/external_directory）、plan mode、undo/redo、AGENTS.md |
| **Operator Workbench Readiness** | ★★★★☆ 高い（開発者のcoding workbenchとして強力） |
| **注意点** | default設定では比較的permissive。hardened config前提で評価すべき。AGENTS.md、MCP設定、custom command、permission policy、provider設定が蓄積されると**OpenCode固有の運用資産**になる |
| **総評** | 開発者のcoding workbenchとしては強く、本番agent backendとしては別途runtimeを持つべき |

### 2.5 Pi — Minimal Core + Extension Harness Platform

| 評価軸 | 判定 |
|---|---|
| **本質** | 最小コアを保ちつつ、extensionによって独自agent harnessを構築する**harness基盤** |
| **強み** | minimal terminal coding harness、多数provider対応、AGENTS.md/SYSTEM.md、customizable compaction、skills、extensions、MCP integration、sandboxing、TypeScript extensionsでtool call/session lifecycle介入 |
| **Operator Workbench Readiness** | ★★★☆☆ 中程度（完成済みcontrol planeではなく、自分で作る基盤） |
| **リスク** | extensionがfull system permissionsで動く場合、信頼できないextensionは危険。チーム利用にはextension governance、review、署名、配布、権限分離が必要 |
| **総評** | **標準で安全な完成済みcontrol plane**というより、**control planeを自分で作れるharness基盤** |

---

## 3. Agent Framework / Runtime 系 詳細

### 3.1 共通する特性

Agent Framework / Runtime 系が担う領域:
- agent loop、tool calling、function calling、handoff
- graph / workflow、typed state、session
- durable execution、retry、checkpoint
- human-in-the-loop、guardrail
- tracing、evaluation、observability
- deployment、tenant / user / role separation、audit log

**強み**: 本番運用、監査、再現性、テスト、障害復旧、品質保証に向く。
**弱み**: Open Harnessより初期設計が重い。

Framework / Runtime が必要になる場面:
- 顧客ごとに状態を分ける必要がある
- agentの判断や操作を監査したい
- 人間の承認を業務ルールとして組み込みたい
- 長時間実行する処理を途中再開したい
- tool callの副作用を管理したい
- 評価データセットで品質を継続的に測定したい
- モデルやプロンプト変更の影響を回帰テストしたい
- 本番SLAを持つagent機能を提供したい

### 3.2 Claude Agent SDK — Claude Code Harness 埋め込みSDK

| 評価軸 | 判定 |
|---|---|
| **本質** | Claude Codeのagent loop、tool、session、permission、subagent、hook、MCP、filesystem操作を**自社アプリに埋め込むSDK**。model-agnostic frameworkではない |
| **強み** | Claude Code相当のcoding agent能力を利用可能。agent loop自前実装不要。software engineering agentを速く作れる |
| **ロックイン** | **高い**。Claude Code runtimeやtool behaviorに深く依存。他モデル/他SDKへの移植困難 |
| **総評** | **Claudeに賭けるなら強いが、vendor lock-inを避けたい中核基盤としては慎重に**。state、tool API、eval dataset、approval recordはSDK外に保持すべき |

### 3.3 OpenAI Agents SDK — 軽量 Agent Primitive Framework

| 評価軸 | 判定 |
|---|---|
| **本質** | Agents、handoffs、guardrails、function tools、MCP、sessions、HITL、tracing、realtime/voiceを扱う軽量Framework |
| **強み** | 抽象が比較的薄い、OpenAI APIとの統合強力、tracing/guardrails組み込み容易、product agentを短期間で作れる |
| **ロックイン** | **中程度**。高度な機能（hosted tools、Responses API、tracing、guardrails、realtime）はOpenAI依存 |
| **総評** | **OpenAIを中核に据えたproduct agent開発には有力**。ロックイン抑制にはtool schema、business state、approval policy、audit log、eval datasetをSDK外に出すべき |

### 3.4 Google ADK — Google Ecosystem Agent Framework

| 評価軸 | 判定 |
|---|---|
| **本質** | Google Cloud / Gemini / enterprise deploymentを意識したagent development framework |
| **強み** | Python/TypeScript/Go/Java対応、multi-agent、workflow agents、Cloud Run/GKE/Agent Runtimeへのdeployment path |
| **ロックイン** | **高い**（Google Cloud）。model-agnosticを掲げるが、最も快適なのはGoogle ecosystem内 |
| **総評** | **Google Cloudを戦略基盤にする企業には自然な選択肢**。クラウド中立性優先時はADK固有機能の採用範囲を制限すべき |

### 3.5 Strands Agents — 軽量 Model-Driven Agent SDK

| 評価軸 | 判定 |
|---|---|
| **本質** | AWS / Bedrock親和、model-drivenで軽量なagent SDK。workflow-heavyよりモデルのplanning/reasoning能力を活かす思想 |
| **強み** | 軽量、model-driven、Bedrock/AWSとの相性良、Anthropic/Ollama/LiteLLM対応、MCP/A2A/multi-agent構成対応、orchestration codeを薄くできる |
| **リスク** | model-drivenな設計は業務上の決定性・監査性をモデルに委ねすぎる危険。複雑な業務フローにはLangGraphのような明示的state machineが向く |
| **総評** | **軽量でAWS-friendlyなagent SDKとして有力**。厳密なworkflow runtimeとして使う場合は慎重な設計が必要 |

### 3.6 LangGraph — Production-Grade Stateful Agent Runtime

| 評価軸 | 判定 |
|---|---|
| **本質** | 状態を持つ長時間実行agent/workflowを**graphとして明示的に設計**できるproduction runtime |
| **強み** | stateful graph、durable execution、checkpoint、thread/session管理、HITL、streaming、memory、retry/resume、persistence、debugging。モデル非依存性が比較的高い |
| **ロックイン** | **中程度**。LangSmith/LangGraph Platformへのobservability/deployment依存は発生し得るが、graph stateやcheckpointの概念は長く残る |
| **総評** | **本番agent workflow、長時間実行、監査、HITL、状態管理が必要な場合の中核候補**。学習コストは高いが長期的技術投資として堅い |

### 3.7 Pydantic AI — 型安全 Python Agent Application Framework

| 評価軸 | 判定 |
|---|---|
| **本質** | LLM agentを**型のある通常のPythonアプリケーション開発に近づける**フレームワーク |
| **強み** | Python中心、model-agnostic、typed deps、structured output、Pydantic型安全性、FastAPIとの相性、MCP対応、HITL approval、durable execution、Pydantic Evals、Logfire/OpenTelemetry、graph support |
| **ロックイン** | **低〜中**（モデルロックインは低いが、Pydantic ecosystem/Logfireへの依存あり） |
| **総評** | **Python product agentを型安全に作りたい場合の非常に有力な選択肢**。LangGraphが「stateful workflow runtime」として強いのに対し、Pydantic AIは「型安全なPython agent application framework」として強い |

---

## 4. ツール横断比較マトリクス

### 4.1 Operator Workbench Readiness（Open Harness 系）

| ツール | 本質 | Workbench Readiness | 主要リスク |
|---|---|---|---|
| **OpenClaw** | Agent control gateway | ★★★★☆ | multi-tenant化には追加設計必要 |
| **Hermes Agent** | Persistent ops agent | ★★★★★ | 状態肥大化・説明可能性低下 |
| **OpenCode** | Coding harness | ★★★★☆ | default permissive、harnessロックイン |
| **Pi** | Harness platform | ★★★☆☆ | extension権限管理が必要 |

### 4.2 Untrusted Product Runtime Readiness（Framework / Runtime 系）

| ツール | 本質 | Runtime Readiness | ロックイン度 |
|---|---|---|---|
| **LangGraph** | Stateful agent runtime | ★★★★★ | 中（概念は普遍的、platform依存あり） |
| **Pydantic AI** | Typed Python framework | ★★★★☆ | 低〜中（ecosystem依存） |
| **OpenAI Agents SDK** | 軽量agent primitive | ★★★★☆ | 中（OpenAI ecosystem依存） |
| **Claude Agent SDK** | Claude Code埋め込み | ★★★☆☆ | 高（Claude専用） |
| **Google ADK** | GCP agent framework | ★★★★☆ | 高（Google Cloud依存） |
| **Strands Agents** | 軽量model-driven | ★★★☆☆ | 中（AWS/Bedrock依存） |

---

## 5. ベンダーロックインの4象限

| ロックイン種別 | 該当ツール | 対策 |
|---|---|---|
| **モデルロックイン** | Claude Agent SDK（Claude依存）、OpenAI Agents SDK（Responses API依存）、Google ADK（Gemini依存） | model routing layerの分離、tool schemaの標準化 |
| **SDKロックイン** | 全Framework（handoff, guardrail, graph state等の抽象） | 良い抽象へのロックインは許容。state, eval datasetはSDK外 |
| **Harnessロックイン** | OpenCode（AGENTS.md, permission）、Pi（extension）、Hermes（memory, skills）、OpenClaw（gateway routing） | 中核業務ロジック・状態はharness外（DB, API, object storage）に保持 |
| **クラウドロックイン** | Google ADK（GCP）、Strands（AWS/Bedrock） | agent state, tool API, eval dataset, audit logをクラウド固有機能に閉じ込めない |

---

## 6. 推奨アーキテクチャ

最もバランスの良い構成は、HarnessとFrameworkを**役割分離して併用**する構成:

```
Human Interface / Harness Layer
  OpenClaw / Hermes Agent / OpenCode / Pi
        ↓
Tool Boundary
  MCP / HTTP APIs / typed function tools / internal service APIs
        ↓
Agent Control Layer
  LangGraph / Pydantic AI / OpenAI Agents SDK / Google ADK / Strands / Claude Agent SDK
        ↓
State & Governance Layer
  DB / object storage / audit logs / eval datasets / traces / approval records
        ↓
Execution Layer
  containers / sandbox / serverless / Kubernetes / CI runners / isolated workspaces
```

**設計原則**: **Harnessを捨てても業務ロジックが残る**ようにする。これにより将来以下が変わっても対応しやすくなる:
- 使うモデル、agent harness、framework、cloud provider
- observability platform、chat interface、IDE
- MCP server、pricing model、vendor terms

---

## 7. 実務上の選定指針

### Open Harness 優先ケース（AI Agentを人間の作業環境に入れたい）
- 開発者のcoding productivity向上
- CLI/IDE/Slack/Telegramからのagent操作
- 個人/チームのAI workbench構築
- ローカルファイル、シェル、MCP、ブラウザの柔軟な利用
- モデル/providerの頻繁な試行錯誤
- production SLAより探索速度を重視

→ OpenCode/Piを開発者環境に、OpenClaw/Hermesをoperator/personal agentとして使う

### Framework / Runtime 優先ケース（AI Agentをプロダクト/業務システムに組み込みたい）
- 顧客向けagent機能、業務ワークフロー組込み
- tenantごとの状態分離、監査ログ、承認フロー、PII/機密情報
- 長時間実行/途中再開、eval/traceによる品質管理
- モデル変更時の回帰テスト、本番SLA

→ LangGraph、Pydantic AI、OpenAI Agents SDK、Google ADK、Strands Agentsを中核に

### ツール別最適シナリオ

| シナリオ | 推奨ツール | 理由 |
|---|---|---|
| Software engineering agentを自社アプリに埋め込み | Claude Agent SDK | Claude Code能力を再利用可能 |
| Python/FastAPI中心の型安全agent | Pydantic AI | typed deps + structured output + FastAPI親和性 |
| 長時間実行・状態管理・HITLが必要な本番workflow | LangGraph | stateful graph + durable execution |
| OpenAI ecosystem中心の軽量product agent | OpenAI Agents SDK | 薄い抽象 + tracing/guardrails統合 |
| Google Cloud戦略基盤の企業 | Google ADK | GCP/Geminiとの統合 |
| AWS中心・軽量model-driven | Strands Agents | Bedrock親和 + 薄いorchestration |

---

## 8. 最終総評

- **Open Harnessは、AI Agentを人間が使うための操作面として投資すべき**
- **Framework / Runtimeは、AI Agentをシステムに組み込むための制御面として投資すべき**
- **中核資産は、どちらにも閉じ込めず、自社所有のtool API、state、audit log、eval dataset、prompt registry、approval recordとして保持すべき**
- この分離ができれば、Open Harnessのスピードと柔軟性、Framework / Runtimeの信頼性と再現性を両方取れる

Harness系のControl/Security/Opsを低く見すぎるのも、Framework系と同じ意味で高く見るのも誤り。正しくは、**何を守るSecurityなのか**を分けて評価すべきである。

---

## 9. Runtime-Centric vs Workflow-Centric: The Fundamental Axis

Beyond the Operator Workbench vs Product Runtime axis (§4), there is an even more fundamental architectural distinction (kzinmr, 2026-05-15): **runtime-centric systems** vs **workflow-centric systems**.

| Axis | Runtime-Centric (Harness) | Workflow-Centric (Framework) |
|---|---|---|
| **Core abstraction** | Runtime — manages *execution* | Workflow — describes *orchestration* |
| **Primary concern** | How execution proceeds continuously and safely | What execution topology should be |
| **Control center** | Runtime (autonomous) | Developer (explicit) |
| **State model** | Runtime-managed (implicit, across turns) | Graph-managed (explicit, designed) |
| **Environment coupling** | Strong (direct mediation of browser/shell/GUI) | Weak (abstracted through tool layer) |
| **Opinionatedness** | High (runtime makes decisions) | Medium (developer makes decisions) |
| **Extensibility** | Runtime extension (hooks, plugins, custom tools) | Workflow composition (nodes, edges, state transitions) |
| **Mental model** | Agent OS | Orchestration library |
| **Determinism** | Low (model-driven autonomy) | High (explicit state machine) |
| **Best for** | Autonomous execution, exploration, operator workbench | Production workflows, audit, deterministic business logic |

### The Runtime-Centric Family

A key insight: ClaudeCode, Codex CLI, PI, OpenClaw, and Hermes Agent are **all in the same architectural family** — they are runtime-centric systems despite their differences in openness and environment type.

| System | Nature |
|---|---|
| **ClaudeCode** | Closed runtime (vendor-optimized, co-trained with model) |
| **Codex CLI** | Closed runtime (vendor-optimized, multi-model) |
| **PI** | Programmable runtime substrate (minimal core, extension-based) |
| **OpenClaw** | Open runtime (multi-channel gateway + control plane) |
| **Hermes Agent** | Open runtime (persistent, self-improving, multi-backend) |

LangGraph and PydanticAI are **workflow-centric systems** — their primary abstraction is the orchestration topology, not the execution substrate.

### The PI Distinction: Runtime Substrate, Not an Agent SDK

PI occupies a unique position in this taxonomy. Unlike LangGraph/PydanticAI — which are developer-centric orchestration libraries (graph construction, node orchestration, deterministic workflow composition) — PI is doing **runtime system work**:

- Execution loop management
- State management across turns
- Task runtime with tool orchestration
- Environment mediation (filesystem, shell, browser via extensions)
- Event handling and streaming
- Interruption and recovery

This is closer to an **"Agent OS"** than an orchestration library. PI is not in the Harness↔Framework middle ground — it is firmly on the harness/runtime side. PI is trying to build an **application runtime**; LangGraph/PydanticAI are closer to **agent topology DSLs**.

| Axis | PI | LangGraph / PydanticAI |
|---|---|---|
| **Core abstraction** | Runtime | Workflow |
| **Primary concern** | Execution | Orchestration |
| **State model** | Runtime-managed | Graph-managed |
| **Environment coupling** | Strong | Weak |
| **Extension model** | Runtime extensions (TypeScript SDK) | Workflow composition (nodes, edges) |
| **Mental model** | Agent OS / application runtime | Orchestration library / topology DSL |

This distinction matters because it changes the evaluation criteria. PI should not be compared to LangGraph on "workflow modeling capability" — that's not what it's trying to do. PI should be evaluated as a **runtime substrate**: how well does it manage execution, mediate the environment, and provide a programmable foundation for agent behavior?

### Why the Shift Now: Control Flow Ownership

The runtime-centric shift is not simply "models got smarter." The deeper structural change (kzinmr, 2026-05-15) is **who can safely own control flow**:

- **Workflow-centric era (2023)**: Models were unreliable primitives — tool misuse, context drift, loop collapse. Developers had to hold control flow authority via explicit graphs. LangGraph's worldview was correct for its time.
- **Runtime-centric era (2025+)**: Models can now *maintain execution semantics* — tool continuation, long-horizon tasks, retry adaptation, context tracking, subtask decomposition, failure recovery. When the model can safely own control flow, the bottleneck shifts from "how do we constrain flow?" to "how do we execute safely?"

The ReAct loop always existed — even LangChain could do `while True: thought=llm(...); result=tool(action)`. The presence of a loop is not the structural difference. The difference is that the loop is no longer an unreliable primitive that needs a developer-authored graph to contain it; it's a reliable execution substrate that the runtime can mediate.

#### The Framework Irrelevance Thesis: Half Right, Half Wrong

> "As models improve, frameworks become irrelevant."

- **Half right**: Workflow-centric abstraction (graph topology, explicit routing, structured transitions) declines as models internalize decomposition, planning, and recovery.
- **Half wrong**: Runtime abstraction (observability, state management, permissions, scheduling, isolation, memory, policies) becomes **more** important — the bottleneck shifts from orchestration logic to execution runtime design.

The future is not a "workflow compiler" but an **agent operating runtime**. ClaudeCode and Codex's advantage is not just model quality — it's **model × runtime co-design**.

See [[concepts/agent-runtime#why-now-control-flow-ownership-and-the-real-shift]] and [[concepts/agent-runtime#what-dies-and-what-survives-the-future-of-agent-infrastructure]] for the full analysis. See also [[concepts/runtime-opinionated-sdk]] for the analysis of Claude/OpenAI Agents SDKs as **mini runtimes** that embed a specific execution model (reactive tool loop, runtime-owned tool orchestration, composable actors, native observability).

**Source**: kzinmr, "Agent Stack Architecture & Comparative Analysis" (2026-05-15), [[raw/articles/2026-05-15_kzinmr_agent-stack-architecture-comparative-analysis]].
