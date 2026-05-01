---
title: "CodeMode — LLM Code Execution Over Sequential Tool Calling"
tags: [code-execution, monty, pydantic-ai, tool-calling, sandbox, RLM, mcp, cloudflare]
created: 2026-04-16
updated: 2026-04-30
type: concept
sources:
  - raw/articles/2026-04-30_cloudflare-code-mode-mcp.md
  - https://blog.cloudflare.com/code-mode-mcp/
  - https://blog.cloudflare.com/project-think/
  - raw/articles/2026-04-15_cloudflare-project-think.md
---

# CodeMode — LLM Code Execution Over Sequential Tool Calling

## Positioning in the Hierarchy

CodeMode is a **concrete implementation layer** below two higher-level concepts:

```
Programmatic Tool Calling (API mechanism — allowed_callers, code_execution_20260120)
    └── Code Execution with MCP (Architectural pattern — MCP as code API)
            └── CodeMode (Specific implementations — Cloudflare MCP, Pydantic Monty) ★ このページ
```

- [[concepts/programmatic-tool-calling]] — The API-level mechanism enabling models to write code that calls tools
- [[concepts/code-execution-with-mcp]] — The architectural pattern: MCP servers as code APIs with progressive disclosure
- **CodeMode** — Concrete implementations (Cloudflare server-side V8, Pydantic Monty in-process)

## Definition

CodeMode is the paradigm where LLMs write code (typically Python) for batch execution rather than making sequential tool calls. Coined by Cloudflare and independently developed by Anthropic, Pydantic, and others.

> *"LLMs work faster, cheaper and more reliably when they write code instead of making sequential tool calls."* — Samuel Colvin

## The Execution Continuum

| Approach | Control | Capability | Start Latency | Cost Model |
|----------|---------|------------|---------------|------------|
| **Tool Calling** | High | Low | Sequential (4-7 round trips, ~12s) | Per-token |
| **CodeMode (Monty)** | High-Medium | Medium | 0.004ms | In-process, zero infra |
| **Sandbox Services** (Modal, E2B, Daytona) | Medium | High | ~1000ms+ | Per-execution billing |
| **Coding Agents** (Claude Code, Cursor) | Low | Very High | Minutes | High |
| **Full Computer Use** | None | Maximum | Minutes | Very high |

## Why It Works

1. **Parallel Execution**: LLM writes a single Python script using `asyncio.gather()` instead of 4-7 sequential tool calls
2. **Native Control Flow**: Loops, conditionals, transforms, comprehensions — all expressed naturally in code
3. **Lower Token Usage**: Weather comparison example: 4.1k input tokens (tool calling) vs 3.3k (CodeMode), $0.019 vs $0.017
4. **Composable**: Code can chain operations, handle errors, and transform data in ways tool calling cannot

## Cloudflare Server-Side Code Mode (MCP)

Cloudflare introduced a radical implementation of CodeMode for their MCP server, collapsing **2,500+ API endpoints** into just **2 MCP tools**: `search()` and `execute()`. This achieves a **99.9% token reduction** — from 1.17M tokens (naive tool-by-tool MCP) to ~1,000 tokens.

### The Two-Tool Interface

```json
[
  {
    "name": "search",
    "description": "Search the Cloudflare OpenAPI spec.",
    "inputSchema": {
      "type": "object",
      "properties": {
        "code": { "type": "string", "description": "JavaScript async arrow function to search the OpenAPI spec" }
      },
      "required": ["code"]
    }
  },
  {
    "name": "execute",
    "description": "Execute JavaScript code against the Cloudflare API.",
    "inputSchema": { ... }
  }
]
```

### Two-Step Workflow

1. **Discovery via `search()`**: Agent writes JS to filter the OpenAPI spec (pre-resolved all `$ref`s). The full spec never enters the model's context.
2. **Action via `execute()`**: Agent writes async JS using `cloudflare.request()` client. Multiple API calls, pagination, error handling — all in one tool call.

> Example: search for WAF endpoints, then fetch + update rules — in one or two tool calls instead of dozens.

### Execution Environment

- **Runtime**: Dynamic Worker isolate (**V8 sandbox**) — lightweight, process-based, no filesystem access
- **Language**: JavaScript (TypeScript-compatible), not Python
- **Security**: External fetches disabled by default; scoped via OAuth 2.1 permissions
- **Startup**: Server-side — no sandbox startup cost on the agent client

This contrasts with Pydantic's Monty: Monty is an in-process Rust bytecode VM (0.004ms startup, Python language), while Cloudflare uses a server-side V8 isolate (JavaScript language, remote execution via MCP).

### Context Reduction Approaches — Comparison

| Approach | Mechanism | Token Cost | Pros | Cons |
|---|---|---|---|---|
| **Traditional MCP (tool-per-endpoint)** | Each API operation = 1 tool definition | ~1.17M tokens | Simple, standard | Exceeds context windows |
| **Client-side CodeMode** | Model writes TS against local SDKs | Low (code only) | High flexibility | Requires client-side sandbox access |
| **CLI Tools** | MCP implemented as self-documenting CLI | Medium | Progressive disclosure | Shell access required; larger attack surface |
| **Dynamic Tool Search** | Surface only "relevant" tools per task | Varies (still per-tool) | Shrinks context per task | Search maintenance overhead |
| **Server-side CodeMode** | **Two fixed tools: search + execute** | **~1,000 tokens (fixed)** | **Zero agent-side changes; secure V8 sandbox; fixed token cost** | Requires server-side execution environment |

### MCP Server & Open Source

- **MCP Server**: `https://mcp.cloudflare.com/mcp` — OAuth 2.1 compliant, scoped permissions
- **SDK**: [Code Mode SDK](https://github.com/cloudflare/agents/tree/main/packages/codemode) within the [Cloudflare Agents SDK](https://github.com/cloudflare/agents)
- **Future — MCP Server Portals**: Single gateway for multiple MCP servers (GitHub, databases, docs) with unified auth and fixed token footprint regardless of number of connected services.

## Monty Implementation (Pydantic)

- Minimal, secure Python interpreter written in Rust
- From-scratch bytecode VM using Ruff's parser
- **Capabilities-based security**: Zero default access, explicit grants
- **State snapshotting**: Serialize execution mid-flight to bytes, resume elsewhere
- **Binary size**: ~4.5MB, memory overhead ~5MB

## Key Advocates

- **Samuel Colvin** (Pydantic): Built Monty, advocates "start from nothing" security
- **Cloudflare**: Coined the term "CodeMode", most radical implementation (server-side V8, 99.9% token reduction)
- **Andrej Karpathy**: Popularized code-over-sequential-tool-calls paradigm
- **Anthropic**: Documented in multiple blog posts on agent patterns

## Official Implementations

### Pydantic AI Harness — CodeMode

The [pydantic-ai-harness](https://github.com/pydantic/pydantic-ai-harness) library provides the canonical CodeMode implementation:

- `CodeMode` capability wraps all agent tools into a single `run_code` tool
- Powered by [Monty](https://github.com/pydantic/monty) sandbox (Rust-based Python VM)
- Supports `asyncio.gather()` for parallel tool execution within one model round-trip
- Observability via [Logfire](https://pydantic.dev/logfire) — nested tool calls as child spans

### Other Implementations

- **Anthropic** — Code execution in Claude agent mode
- **Cloudflare** — Server-side V8 sandbox MCP (search + execute); [[concepts/model-context-protocol-mcp]]
- **OpenAI Codex CLI** — Code-first agent approach with sandboxed Python execution

## 言語選択の二分性: JavaScript vs Python

CloudflareはJS/TypeScript、PydanticはPython、AnthropicはPython — この言語選択の違いはCodeModeの方向性に深い影響を与えるが、これまで系統的に分析されていない。

| 次元 | JavaScript (Cloudflare V8) | Python (Pydantic Monty) | Python (Anthropic Container) |
|------|---------------------------|------------------------|-----------------------------|
| **ランタイム** | V8 isolate（軽量、起動ミリ秒） | Rust製bytecode VM（起動0.004ms） | Dockerコンテナ（起動~秒） |
| **パッケージ管理** | npm（tscの型検査に依存） | PyPI（pip install） | プリインストール済み |
| **非同期実行** | native async/await | asyncio（MontyはRust tokio上） | asyncio |
| **型の扱い** | `any` による動的dispatch（型安全と速度のトレードオフ） | duck typing + pydantic BaseModel | duck typing |
| **モデル親和性** | TSの豊富な学習データ（GitHub TSコード量） | Pythonの極めて豊富な学習データ | Python |
| **エコシステム親和性** | MCP SDK（TypeScriptファースト） | pydantic / FastAPI / LangChain | Claude API（Python SDK充実） |

### なぜCloudflareはJSを選んだのか

Cloudflare公式の論点：

> *"We made this choice with the intuition that the models are better at TypeScript than custom tool-call formats."*
> — Cloudflare Code Mode blog

しかしこれは**検証可能な仮説**であり、確定した知見ではない。以下の論点が未解決：

1. **訓練データ量**: GPT-5/Claude 4系の訓練データにおけるPython vs TypeScriptの割合は非公開。両者とも豊富だが、PythonはNumPy/PyTorch/pandas等の特定ドメインコードが多く、ツール呼び出しパターンはTypeScript（async/await）の方が直感的か。
2. **モデル世代差**: Opus 4.6→Sonnet 4.7でPythonコード生成能力が有意に向上したという報告があり、言語選択の優位性はモデルバージョンによって変動する。
3. **型安全性**: Cloudflare自身も指摘する通り、TypeScriptの`any`型を多用するツールラッパーでは型安全が損なわれる。Pythonのpydantic BaseModelによるstrictな型定義（Pydantic AIのコア設計）の方が、CodeModeのツールインターフェースとして堅牢である可能性がある。

### 示唆: ランタイム分岐の予測

今後、CodeModeの標準化が進むにつれて、以下の方向性が考えられる：

- **マルチランゲージランタイム**: CloudflareのMCP Server Portal構想は、1つのゲートウェイで複数の実行環境を切り替える方向を示唆している。JSのDynamic Worker + Montyの両方を提供する可能性。
- **MCP標準化**: MCPプロトコル自体がコード実行を標準化すれば、言語選択はランタイムプロバイダの問題に分離され、クライアントは意識しなくなる。
- **言語非依存PTC**: PTCの本質は「コードでツールをasync呼び出す」こと自体にあり、言語は二次的な選択。RLMとの統合（PTC in RLM, 案A）ではPythonが自然だが、CLIツールとしてはJSの方が起動が速い。

## MCP-based vs Native API: トランスポート層の設計選択

CloudflareのCodeModeは **MCPをトランスポートとして使う**（search + executeの2つのMCP toolとして実装）。一方、AnthropicのPTCは **ネイティブAPI**（`code_execution_20260120`ツールとしてモデル側に組み込み）。このトランスポート層の違いは、今後のPTCエコシステムの分岐点となる。

| 次元 | MCP-based (Cloudflare) | Native API (Anthropic) |
|------|----------------------|----------------------|
| **プロトコル** | 標準MCP — どんなクライアントでも使える | Claude API固有 — 他のモデルでは使えない |
| **ツール定義** | MCPスキーマに従う（コード実行はsearch/execute 2ツール） | モデル固有の`tool_use`ブロック（1ツール: `code_execution_20260120`） |
| **コード実行結果** | MCP tool_resultとしてstdoutが返る | tool_resultとしてstdoutが返る（同様） |
| **セキュリティ** | OAuth 2.1 + scoped permissions + Binding | `allowed_callers` + container sandbox |
| **移植性** | 高い（任意のMCPクライアントで動作） | 低い（Claude API依存） |
| **状態管理** | MCPセッションに依存（Cloudflare DOの場合は永続的） | session tokenで管理（container lifetime依存） |
| **拡張性** | MCP Server Portalで複数サービスの統合ゲートウェイ化可能 | API拡張に依存（Anthropicのロードマップ次第） |

### MCP-basedの優位性

- **プロトコル標準化**: どんなMCPクライアント（Claude Desktop, Cursor, VS Code extension）でも同じCodeMode体験を得られる
- **OAuth 2.1統合**: スコープ付きパーミッションで細かいアクセス制御が可能
- **Server Portal構想**: 単一ゲートウェイで複数のバックエンドMCPサーバを統合し、トークン消費はゲートウェイの固定ツール数（search + execute）に縮退される

### Native APIの優位性

- **モデル最適化**: `code_execution_20260120`はモデル内部のtool_useメカニズムと統合されており、モデルが自発的にコード実行を選択できる
- **`allowed_callers`**: ツールごとに「直接呼び出し可能」「コード実行からのみ呼び出し可能」を制御できる。MCP-basedでは`allowed_callers`相当の機構がプロトコル標準にない
- **caller識別**: レスポンスの`caller`フィールドで、ツール呼び出しがコードから発信されたか直接か区別できる

### 将来の収束予測

両者の折衷として、以下の標準化が予想される：

1. **MCPプロトコル拡張によるコード実行標準化**: MCP仕様に`code_execution`プリミティブ（`allowed_callers`相当のフィールド）を追加 → CloudflareのMCP依存強みが標準に
2. **Native APIのMCP互換ラッパー**: AnthropicがClaude APIのコード実行機能をMCPサーバとしても公開（既に部分的に進行中）
3. **ランタイム非依存PTC**: PTCのコア（コードでツールを呼ぶパターン）はトランスポート層から独立して標準化され、MCP経由でもNative API経由でも同じ体験を目指す

## Related Patterns

- [[concepts/programmatic-tool-calling]] — API mechanism: `allowed_callers`, `code_execution_20260120`
- [[concepts/code-execution-with-mcp]] — Architectural pattern: MCP servers as code APIs
- [[concepts/harness-engineering]] — Monty as a harness environment
- [[concepts/pydantic-ai-harness]] — Official CodeMode capability library
- [[concepts/structured-outputs]] — Type safety constrains LLM output
- [[concepts/harness-engineering/system-architecture/code-execution-with-mcp]] — Alternative to MCP tool execution

## Agent around REPL: 3つの実装パターン

CodeModeをRLM（Recursive Language Model）的に使う場合、pydantic-ai上では3段階のアプローチが存在する。

### パターン1: CodeMode + output function（最小形、推奨）

既存のCodeModeを土台にし、`output_type`をoutput functionにすることでモデルに「最後は必ずsubmit(...)を呼ばせる」形にする。REPLはagentの内部実行機構、最終制御はagent側に残す。

```python
from pydantic_ai import Agent
from pydantic_ai_harness import CodeMode

def submit(answer: str) -> str:
    """Final answer — ends the run."""
    raise EndRun(answer)

agent = Agent(
    'anthropic:claude-sonnet-4-6',
    capabilities=[CodeMode()],
    output_type=submit,
    instructions=(
        '探索・集計・中間計算は run_code で行い、'
        '確信が持てたら submit(...) で終了すること。'
    ),
)
```

DSPyのRLMに近いUXを、Pydantic AIの流儀で最も少ない独自実装で実現できる。CodeModeはすでに全ツールを1個の`run_code`ツールへ束ね、同一agent run内でREPL状態を保持し、`restart: true`でリセットできる。

### パターン2: Action → Execute → Observe の明示的外部ループ（DSPy互換）

DSPyのRLMをより忠実に移植したい場合、agentの`output_type`を`RunCode | FinalAnswer`のような構造化出力にし、各ターンでモデルに「次のaction」を1つだけ出させる。ホスト側がRunCodeを受け取ったらMonty REPLで実行し、観測結果を次ターンへ戻す。

```python
class RunCode(BaseModel):
    code: str

class FinalAnswer(BaseModel):
    answer: str

output_type = RunCode | FinalAnswer
```

Pydantic AIは複数run間で`message_history`をそのまま受け渡し可能。内部的にagentは`pydantic-graph`ベースで動いており、`agent.iter()`によるnode-level制御もあるため、"Action → Execute → Observe → Next Action"の明示ループは素直に組める。

### パターン3: graph-native版（本番向け）

Plan / RunCode / Observe / Finalizeを明示ノードに分け、Monty側はsnapshotを保存できるので中断・再開やprocess境界越しの復元が容易。Pydantic AIはdurable executionを公式に持ち、Temporal / DBOS / Prefect / Restateをサポートしているため、「RLMの状態遷移はpydantic-graph、コード実行状態はMonty snapshot」という二層化は相性が良い。

## Agent around REPL vs Agent on REPL

Montyは**REPL sandboxソリューション**として設計されている。RLMをpydantic-aiネイティブに実現する場合、「Agent on REPL」（モデルをREPLの中に閉じ込める）より**「Agent around REPL」**（REPLをagentの内部executorとして使う）として設計するのが健全。

MontyのREADMEはexperimentalと明記されており、合理的なsubsetのみ、ホスト環境アクセスはexternal function経由、サードパーティライブラリは対象外。つまり**会話制御・出力検証・承認・履歴管理・durabilityはPydantic AI外側、REPLは内側のexecutorに留める**のが正しい分離。

## Deferred Tool Calls の現状

| CodeModeのドキュメントには「approval/deferredなツールはsandboxから除外」と記載があるが、v0.2.0リリースノートでは`HandleDeferredToolCalls`でinline解決できるようになっている。実装は「handlerがいれば解決、いなければエラー」という分岐。現状は「完全禁止」ではなく**「handler必須で対応中」**と読むのが正確。ドキュメントが実装に追いついていない可能性がある。

## CodeMode × RLM: 並行する文脈爆縮の2つのアプローチ

CodeModeと[[concepts/rlm-recursive-language-models|RLM]]は、独立に発展しながらも驚くほど類似した問題意識と解決策を持つ。

### コア問題の同一性

両者の根底には同じ問題がある：

> **「LLMの限られたコンテキストウィンドウで、膨大な検索空間をどう扱うか」**

| 側面 | CodeMode (Cloudflare) | RLM (DSPy) |
|------|----------------------|------------|
| **検索空間** | 2,500+ APIエンドポイント | 100万トークン以上のドキュメント |
| **解決策** | コードでOpenAPIスペックを検索・実行 | コードでコンテキストを探索・分解 |
| **ツール表面積** | search() + execute() (2 tools) | llm_query() + SUBMIT() (暗黙のREPL) |
| **サンドボックス** | V8 isolate (JS) | Deno + Pyodide (Python) |
| **契約** | モデルがJSコードを書く | モデルがPythonコードを書く |
| **文脈爆縮率** | 99.9% (1.17M→1K tokens) | ほぼ無限 (10M+ tokensでも可能) |

### アーキテクチャの共通パターン

両者に共通する3層構造：

1. **Discovery層**: 検索空間をコードでフィルタ（OpenAPI spec探索 / ドキュメント探索）
2. **Execution層**: 見つけた対象に対して操作を実行（API呼び出し / llm_query）
3. **Synthesis層**: 結果を集約して最終出力（JSON response / SUBMIT）

このパターンは[[concepts/agentic-search]]のLevel 3（Externalized Processing）にも接続する — Cao et al.が示した「coding agents as effective long-context processors」と同一の知見が、APIアクセスと文書処理という異なるドメインで独立に現れている。

### トレードオフ

| 次元 | CodeMode優位 | RLM優位 |
|------|-------------|---------|
| **レイテンシ** | 固定2ラウンドトリップ | REPLループ数に比例 |
| **セキュリティ** | V8 isolate + サーバーサイド | Deno WASMサンドボックス |
| **表現力** | コードの自由度（何でも書ける） | llm_queryによる意味的探索 |
| **カスタマイズ性** | サーバー提供のOpenAPIスキーマに依存 | 任意のデータ構造に対応可 |
| **学習可能性** | プロンプトエンジニアリング | DSPy最適化 + RL訓練可能 |

### 収束の予測

MCP Server Portals（Cloudflare）の構想は、APIアクセスにおける「固定ツール表面積 + サーバーサイドコード実行」を汎用化するもの。これをRLMの「コンテキスト探索 + 再帰的サブクエリ」と組み合わせると、API呼び出しと文書処理を統合した汎用CodeModeエージェントが可能になる：

```
Agent → search(OpenAPI + docs) → execute(API calls + llm_query) → submit(result)
```

pydantic-ai-harnessはすでに[[concepts/monty-sandbox|Monty]]でPython REPLを提供しており、CodeModeの`run_code`内で`llm_query`的なサブコールを実装すれば、CodeModeとRLMの統合は可能な状態にある。
