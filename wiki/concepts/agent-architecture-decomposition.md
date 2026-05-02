---
title: "Agent Architecture Decomposition: Model / Runtime / Harness"
category: concept
tags:
  - ai-agents
  - architecture
  - open-source
  - open-runtime
  - open-harness
  - mcp
created: 2026-04-30
updated: 2026-04-30
---

# Agent Architecture Decomposition: Model / Runtime / Harness

A three-layer framework for understanding production AI agent systems, articulated by Harrison Chase (LangChain CEO) in March 2026.

## The Three Layers

### 1. Open Models

The **intelligence layer** — the LLM that powers agent reasoning, planning, and decision-making.

**Key thesis**: No single model dominates all tasks. Production agents should be model-agnostic, selecting the best model per workload.

**Notable open-weight models**:
- NVIDIA Nemotron 3 Super (120B MoE, 1M context)
- Meta Llama 4 (MoE variants)
- Qwen 3 series

**Proprietary models used in agents**:
- Claude Opus 4.7 / Sonnet 4.5 (Anthropic)
- GPT-5.5 (OpenAI)

See: [[entities/harrison-chase]] on model optionality.

### 2. Open Runtime

The **execution environment** where agents operate. This layer determines the native tool-use interface and security boundary.

**Critical insight**: The runtime choice *constrains the natural function-calling mechanism*.

| Runtime Type | Native Tool Interface | Example Agents | Security Model |
|---|---|---|---|
| **Bash/Shell** | CLI commands (`curl`, `grep`, `python script.py`) | Claude Code, OpenClaw, Codex CLI | User-level permissions |
| **Python REPL** | Python function calls | DSPy, Pydantic AI, RLM | Process-level isolation |
| **Micro-VM Interpreter** | Bytecode VM with capability grants | Pydantic Monty | Deny-by-default, explicit function exposure |
| **Browser DOM** | DOM manipulation, JS execution | Browser Use, Playwright MCP | Browser sandbox |
| **Container/MicroVM** | Full environment API | Daytona, Rivet agentOS | Hardware-level isolation |
| **Dedicated Sandboxes** | Policy-enforced execution | NVIDIA OpenShell | Deny-by-default + YAML policies |

#### Agent on REPL: Python関数ネイティブのRuntime

Python REPLをRuntimeに選択すると、エージェントはCLIコマンドではなく**Python関数**を直接呼び出す形でツールを利用する。

```python
agent → call_tool(search_codebase, pattern="...")
agent → call_tool(run_tests, path="./tests/")
agent → call_tool(fetch_weather, city="London")
```

**代表例: RLM (Recursive Language Model)**

RLMは「コンテキストの分解」をモデルに委ねるアーキテクチャ（[[mlops/agent-vs-rlm-comparison]]）。REPL環境内で`grep`、スライス等のコード操作を通じて関連コンテキストを選択的に抽出する。タスク分解ではなく**コンテキスト分解**が基本単位。

**代表例: Pydantic AI**

型安全なエージェントフレームワーク（[[concepts/pydantic-ai]]）。Python関数をツールとして登録し、Pydanticモデルで入出力を検証。Graph APIによるワークフロー定義も可能。

**Agent on REPLの利点**:
- 型安全: Python型ヒントでツールパラメータを検証可能
- 構造化出力: Pydanticモデル等で戻り値を保証
- 高速: プロセス内実行（IPC不要）
- 状態共有: REPL内のメモリ空間をエージェント間で共有可能

#### Micro-VM Interpreter: 専用バイトコードVMのRuntime

**代表例: Pydantic Monty**

MontyはRust製のミニマルPythonインタープリタ（[[concepts/monty-sandbox]]）。Agent on REPLの延長線上にあるが、**CPythonではなく専用VM**でコードを実行する点が根本的に異なる。

| 特性 | 値 |
|---|---|
| 起動遅延 | 0.004ms（Docker 195msの~1/50,000） |
| バイナリサイズ | ~4.5MB |
| メモリオーバーヘッド | ~5MB（CPython埋め込み時） |
| セキュリティ | Deny-by-default。外部関数として明示的に公開したもののみアクセス可能 |

Montyは「**エージェントのために作られたエージェントのRuntime**」という設計思想。標準ライブラリもサードパーティパッケージも使わず、ホストから明示的にgrantされた関数のみを実行できる。これはcapabilities-based securityの原則に従っている。

**実行連続体**（Samuel Colvinの整理）:

| アプローチ | 制御度 | 表現力 | 遅延 | コスト |
|---|---|---|---|---|
| **Tool Calling** | 高 | 低 | シーケンシャル往復 | トークンごと |
| **Monty / CodeMode** | 高-中 | 中 | 0.004ms起動 | プロセス内 |
| **Sandbox Services** | 中 | 高 | ~1000ms+起動 | 実行ごと |
| **Coding Agents** | 低 | 非常に高い | 分単位 | 高 |
| **Full Computer Use** | なし | 最大 | 分単位 | 非常に高 |

Montyは「シーケンシャルなTool Callingの低表現力」と「Sandbox/Full Computer Useの高コスト・高遅延」の間に位置する。エージェントがループ・条件分岐・並列呼び出しを1回のコード生成で表現でき、かつインフラコストゼロ。

#### Runtime → Tool-Use Relationship

When an agent runs **on bash**, CLI tools become the natural function-calling interface:
```
agent → execute("curl -s https://api.example.com")
agent → execute("grep -r 'pattern' /project")
```

When an agent runs **on Python REPL**, Python functions are the natural interface:
```python
agent → call_tool(search_codebase, pattern="...")
agent → call_tool(run_tests, path="./tests/")
```

This is why coding agents (Claude Code, OpenClaw) feel like "terminal users" — bash is their runtime, so shell commands are their native function-calling protocol.

#### Heterogeneous Agent Composition

For systems with multiple agents on different runtimes, **(Remote) MCP** serves as the universal adapter:

```
┌──────────┐    MCP     ┌──────────────┐
│ CLI Agent│◄──────────►│              │
│ (bash)   │            │   MCP Router │
├──────────┤            │  (Gateway)   │
│ Python   │◄──────────►│              │
│ Agent    │    MCP     └──────────────┘
├──────────┐                     ▲
│ Browser  │    MCP              │
│ Agent    │◄────────────────────┘
└──────────┘
```

This architecture is analogous to **microservices with an API gateway**:
- Each agent is an independent service with its own runtime
- MCP standardizes the interface (like gRPC/REST)
- The MCP Router handles routing, auth, and load balancing

See: [[entities/nvidia-openshell]] for the Open Runtime reference implementation.

### 3. Open Harness

The **orchestration layer** that connects the model to the runtime and manages the agent lifecycle.

**Components**:
- **Task Planning** — Breaking high-level goals into executable steps
- **Sub-agent Spawning** — Creating worker agents for parallel tasks
- **Memory Management** — Short-term context + long-term memory persistence
- **Tool Routing** — Selecting which tool/capability to invoke
- **Context Management** — Maintaining conversation history, file state, etc.

**The "Harness = Backend" thesis** (from [[concepts/harness-engineering]]#iii-platform): the harness shouldn't be separate from the backend infrastructure — it *is* the backend. When agents are treated as workers in a unified system, the distinction between "agent orchestration" and "backend services" collapses.

**Open vs Closed Harness**:
| Property | Open Harness | Closed Harness |
|---|---|---|
| Memory ownership | User-controlled (Mongo, Postgres, Redis) | Platform-controlled |
| Model selection | Pluggable / swappable | Vendor-locked |
| Tool ecosystem | Standardized (MCP, AGENTS.md) | Proprietary |
| Portability | High | Low |

LangChain Deep Agents is Chase's reference implementation of an Open Harness.
[[concepts/pydantic-ai-harness]] is the Pydantic team's reference implementation — a modular capability library that provides CodeMode, memory, orchestration, guardrails, and more.

### Pydantic: The Full Stack (Runtime + Harness)

Pydantic is unique in providing **both** the Open Runtime and Open Harness layers as an integrated stack:

| Layer | Component | Role |
|---|---|---|
| **Open Runtime** | [Monty](https://github.com/pydantic/monty) | Secure Python bytecode VM (0.004ms startup, deny-by-default) |
| **Open Harness** | [pydantic-ai-harness](https://github.com/pydantic/pydantic-ai-harness) | Capability library (CodeMode, memory, orchestration, guards) |
| **Open Models** | Pydantic AI core | Model-agnostic — works with Claude, GPT, Gemini, Ollama |

**The coupling insight**: CodeMode in the Harness *requires* Monty as its Runtime. The Harness decides *when* to write code vs. use sequential tool calls; the Runtime executes that code safely. This is analogous to how Kubernetes (orchestration) requires container runtime (containerd) — they're separate layers but tightly coupled by design.

This contrasts with frameworks that mix Runtime and Harness concerns:
- **Claude Code / OpenClaw**: Runtime = bash, Harness = proprietary (not separable)
- **LangChain**: Runtime = container/VM (external), Harness = LangGraph (separate vendors)
- **RLM**: Runtime = Python REPL, Harness = recursive context decomposition (same repo, different abstraction levels)

Samuel Colvin's design philosophy — *"Start from nothing, then selectively grant capabilities"* — applies to both Monty (zero filesystem/network by default) and the Harness (zero tools by default — you compose what you need).

## Relationship to Traditional Architecture

The Model/Runtime/Harness decomposition maps to traditional software architecture:

| AI Agent Layer | Traditional Equivalent |
|---|---|
| Open Model | AI/ML inference service |
| Open Runtime | Container / VM / execution environment |
| Open Harness | Orchestration layer + message queue + state management |
| MCP (inter-runtime) | API Gateway / Service Mesh |
| Agent Workers | Microservices |

This mapping explains why **microservice architecture patterns** (service discovery, routing, circuit breakers, observability) directly apply to multi-agent systems.

## Sources

- [Harrison Chase's post](https://x.com/hwchase17/status/2034297125417460044) (March 2026)
- [NVIDIA OpenShell announcement](https://developer.nvidia.com/blog/) — Open Runtime reference implementation
- [LangChain Deep Agents](https://blog.langchain.dev/deep-agents/) — Open Harness reference
- [Continual learning for AI agents](https://x.com/i/article/2040467997022884194) (@hwchase17, April 2026)
- [The Definitive Guide to Harness Engineering](../raw/articles/2026-04-27_2047145274200768969_The-Definitive-Guide-to-Harness-Engineering.md)
- [Pydantic Monty: A Minimal Python Sandbox for AI Agents](https://pydantic.dev/articles/pydantic-monty) (Samuel Colvin, Feb 2026)
- [RLM Blog Post](https://alexzhang13.github.io/blog/2025/rlm/) (Alex L. Zhang, Oct 2025)
- [Language Models will be Scaffolds](https://alexzhang13.github.io/blog/2026/scaffold/) (Alex L. Zhang, Feb 2026)
- [Monty, from tool calling to computer use - PyAI Conf 2026](https://www.youtube.com/watch?v=wXjZdrS3LqA) (Samuel Colvin, 2026)

## Related

- [[entities/harrison-chase]]
- [[entities/samuel-colvin]]
- [[entities/nvidia-openshell]]
- [[concepts/harness-engineering]]
- [[concepts/deep-agents]]
- [[concepts/monty-sandbox]]
- [[concepts/pydantic-ai]]
- [[mlops/agent-vs-rlm-comparison]]
- [[entities/alex-zhang]]
