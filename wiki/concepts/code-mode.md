---
title: "CodeMode — LLM Code Execution Over Sequential Tool Calling"
tags:
  - coding-agents
  - company
  - developer-tooling
  - tool
  - sandbox
  - rlm
  - mcp
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

## Language Choice Dichotomy: JavaScript vs Python

Cloudflare uses JS/TypeScript, Pydantic uses Python, Anthropic uses Python — this language choice difference deeply influences CodeMode's direction, but has not been systematically analyzed until now.

| Dimension | JavaScript (Cloudflare V8) | Python (Pydantic Monty) | Python (Anthropic Container) |
|------|---------------------------|------------------------|-----------------------------|
| **Runtime** | V8 isolate (lightweight, millisecond startup) | Rust-based bytecode VM (0.004ms startup) | Docker container (~seconds startup) |
| **Package Management** | npm (depends on tsc type checking) | PyPI (pip install) | Pre-installed |
| **Async Execution** | native async/await | asyncio (Monty on Rust tokio) | asyncio |
| **Type Handling** | Dynamic dispatch via `any` (type safety vs speed tradeoff) | duck typing + pydantic BaseModel | duck typing |
| **Model Affinity** | Rich TS training data (GitHub TS code volume) | Extremely rich Python training data | Python |
| **Ecosystem Affinity** | MCP SDK (TypeScript-first) | pydantic / FastAPI / LangChain | Claude API (strong Python SDK) |

### Why Cloudflare Chose JS

Cloudflare's official rationale:

> *"We made this choice with the intuition that the models are better at TypeScript than custom tool-call formats."*
> — Cloudflare Code Mode blog

However, this is a **testable hypothesis**, not settled knowledge. The following points remain unresolved:

1. **Training data volume**: The ratio of Python vs TypeScript in GPT-5/Claude 4-series training data is undisclosed. Both are abundant, but Python has more domain-specific code (NumPy/PyTorch/pandas), while tool-calling patterns may be more intuitive in TypeScript (async/await).
2. **Model generation differences**: There are reports that Python code generation capability significantly improved from Opus 4.6 to Sonnet 4.7, meaning language choice advantage fluctuates with model version.
3. **Type safety**: As Cloudflare itself notes, tool wrappers that heavily use TypeScript's `any` type lose type safety. Python's strict type definitions via pydantic BaseModel (Pydantic AI's core design) may be more robust as a CodeMode tool interface.

### Implications: Predicting the Runtime Fork

As CodeMode standardization progresses, the following directions are conceivable:

- **Multi-language runtime**: Cloudflare's MCP Server Portal vision suggests switching between multiple execution environments through a single gateway. Could offer both JS Dynamic Workers and Monty.
- **MCP standardization**: If the MCP protocol itself standardizes code execution, language choice becomes a runtime provider concern, invisible to the client.
- **Language-agnostic PTC**: The essence of PTC is "calling tools via async code," with language being a secondary choice. For RLM integration (PTC in RLM, Plan A), Python is natural, but for CLI tools, JS starts faster.

## MCP-based vs Native API: Transport Layer Design Choices

Cloudflare's CodeMode uses **MCP as the transport** (implemented as two MCP tools: search + execute). In contrast, Anthropic's PTC uses a **native API** (`code_execution_20260120` tool built into the model side). This transport layer difference is a fork point for the future PTC ecosystem.

| Dimension | MCP-based (Cloudflare) | Native API (Anthropic) |
|------|----------------------|----------------------|
| **Protocol** | Standard MCP — usable by any client | Claude API-specific — cannot be used by other models |
| **Tool Definition** | Follows MCP schema (code execution via 2 tools: search/execute) | Model-specific `tool_use` block (1 tool: `code_execution_20260120`) |
| **Code Execution Result** | stdout returned as MCP tool_result | stdout returned as tool_result (same) |
| **Security** | OAuth 2.1 + scoped permissions + Binding | `allowed_callers` + container sandbox |
| **Portability** | High (works with any MCP client) | Low (Claude API-dependent) |
| **State Management** | Depends on MCP session (persistent in Cloudflare DO case) | Managed via session token (container lifetime-dependent) |
| **Extensibility** | MCP Server Portal enables multi-service unified gateway | Depends on API expansion (Anthropic roadmap-dependent) |

### Advantages of MCP-based

- **Protocol standardization**: Any MCP client (Claude Desktop, Cursor, VS Code extension) gets the same CodeMode experience
- **OAuth 2.1 integration**: Fine-grained access control via scoped permissions
- **Server Portal vision**: Single gateway unifies multiple backend MCP servers, with token consumption collapsed to the gateway's fixed tool count (search + execute)

### Advantages of Native API

- **Model-optimized**: `code_execution_20260120` is integrated with the model's internal tool_use mechanism, allowing the model to spontaneously choose code execution
- **`allowed_callers`**: Can control per-tool whether "direct call is allowed" or "only callable from code execution." MCP-based lacks an equivalent mechanism in the protocol standard
- **Caller identification**: The response's `caller` field distinguishes whether a tool call originated from code or was direct

### Predicted Future Convergence

As a compromise between the two, the following standardization is expected:

1. **MCP protocol extension for code execution standardization**: Adding a `code_execution` primitive (with `allowed_callers`-equivalent fields) to the MCP spec → Cloudflare's MCP dependency strength becomes standard
2. **Native API MCP-compatible wrapper**: Anthropic publishing Claude API's code execution feature as an MCP server (already partially in progress)
3. **Runtime-independent PTC**: The core of PTC (the pattern of calling tools via code) becomes standardized independent of the transport layer, with the same experience whether via MCP or Native API

## Related Patterns

- [[concepts/programmatic-tool-calling]] — API mechanism: `allowed_callers`, `code_execution_20260120`
- [[concepts/code-execution-with-mcp]] — Architectural pattern: MCP servers as code APIs
- [[concepts/harness-engineering]] — Monty as a harness environment
- [[concepts/pydantic-ai-harness]] — Official CodeMode capability library
- [[concepts/structured-outputs]] — Type safety constrains LLM output
- [[concepts/harness-engineering/system-architecture/code-execution-with-mcp]] — Alternative to MCP tool execution

## Agent around REPL: 3 Implementation Patterns

When using CodeMode in an RLM (Recursive Language Model) style, there are three levels of approach on pydantic-ai.

### Pattern 1: CodeMode + output function (minimal, recommended)

Build on existing CodeMode and make `output_type` an output function, forcing the model to "always call submit(...) at the end." The REPL is the agent's internal execution mechanism, with final control remaining on the agent side.

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
        'Perform exploration, aggregation, and intermediate computation via run_code, '
        'and call submit(...) to finish once confident.'
    ),
)
```

This achieves a UX close to DSPy's RLM with minimal custom implementation in the Pydantic AI style. CodeMode already bundles all tools into a single `run_code` tool, maintains REPL state within the same agent run, and can be reset with `restart: true`.

### Pattern 2: Action → Execute → Observe explicit external loop (DSPy-compatible)

When you want to port DSPy's RLM more faithfully, make the agent's `output_type` a structured output like `RunCode | FinalAnswer`, having the model output exactly one "next action" per turn. When the host side receives RunCode, it executes it in the Monty REPL and returns the observation result to the next turn.

```python
class RunCode(BaseModel):
    code: str

class FinalAnswer(BaseModel):
    answer: str

output_type = RunCode | FinalAnswer
```

Pydantic AI can pass `message_history` as-is between multiple runs. Internally, the agent runs on a `pydantic-graph` basis, and since node-level control via `agent.iter()` is available, the "Action → Execute → Observe → Next Action" explicit loop can be built straightforwardly.

### Pattern 3: graph-native version (production-ready)

Split Plan / RunCode / Observe / Finalize into explicit nodes. The Monty side can save snapshots, making suspension/resumption and restoration across process boundaries easy. Pydantic AI officially supports durable execution with Temporal / DBOS / Prefect / Restate, so the two-layer approach of "RLM state transitions via pydantic-graph, code execution state via Monty snapshot" has good synergy.

## Agent around REPL vs Agent on REPL

Monty is designed as a **REPL sandbox solution**. When implementing RLM natively on pydantic-ai, it is healthier to design it as **"Agent around REPL"** (REPL as the agent's internal executor) rather than "Agent on REPL" (trapping the model inside the REPL).

Monty's README explicitly marks it as experimental, with only a reasonable subset supported, host environment access via external functions, and third-party libraries out of scope. In other words, **conversation control, output verification, approval, history management, and durability belong on the Pydantic AI outside, with REPL confined to the internal executor** — this is the correct separation.

## Current State of Deferred Tool Calls

| CodeMode documentation states "approval/deferred tools are excluded from the sandbox," but in the v0.2.0 release notes, `HandleDeferredToolCalls` can now resolve them inline. The implementation branches as "resolve if handler exists, error if not." The current state is more accurately read as **"handler-required, work in progress"** rather than "completely prohibited." The documentation may be lagging behind the implementation.

## CodeMode × RLM: Two Parallel Approaches to Context Collapse

CodeMode and [[concepts/rlm-recursive-language-models|RLM]] evolved independently yet have surprisingly similar problem awareness and solutions.

### Identity of the Core Problem

Both share the same fundamental problem:

> **"How to handle enormous search spaces within an LLM's limited context window"**

| Aspect | CodeMode (Cloudflare) | RLM (DSPy) |
|------|----------------------|------------|
| **Search Space** | 2,500+ API endpoints | 1M+ token documents |
| **Solution** | Search and execute against OpenAPI spec via code | Explore and decompose context via code |
| **Tool Surface Area** | search() + execute() (2 tools) | llm_query() + SUBMIT() (implicit REPL) |
| **Sandbox** | V8 isolate (JS) | Deno + Pyodide (Python) |
| **Contract** | Model writes JS code | Model writes Python code |
| **Context Collapse Rate** | 99.9% (1.17M→1K tokens) | Virtually unlimited (10M+ tokens possible) |

### Common Architectural Pattern

A 3-layer structure common to both:

1. **Discovery layer**: Filter the search space via code (OpenAPI spec exploration / document exploration)
2. **Execution layer**: Execute operations against found targets (API calls / llm_query)
3. **Synthesis layer**: Aggregate results into final output (JSON response / SUBMIT)

This pattern also connects to [[concepts/agentic-search]] Level 3 (Externalized Processing) — the same insight that Cao et al. demonstrated as "coding agents as effective long-context processors" appears independently in the different domains of API access and document processing.

### Tradeoffs

| Dimension | CodeMode Advantage | RLM Advantage |
|------|----------------------|------------|
| **Latency** | Fixed 2 round trips | Proportional to REPL loop count |
| **Security** | V8 isolate + server-side | Deno WASM sandbox |
| **Expressiveness** | Code freedom (write anything) | Semantic exploration via llm_query |
| **Customizability** | Depends on server-provided OpenAPI schema | Can handle arbitrary data structures |
| **Learnability** | Prompt engineering | DSPy optimization + RL trainable |

### Predicted Convergence

The MCP Server Portals (Cloudflare) vision generalizes "fixed tool surface area + server-side code execution" for API access. Combining this with RLM's "context exploration + recursive subqueries" enables a general-purpose CodeMode agent that integrates API calls and document processing:

```
Agent → search(OpenAPI + docs) → execute(API calls + llm_query) → submit(result)
```

pydantic-ai-harness already provides a Python REPL via [[concepts/monty-sandbox|Monty]], and implementing llm_query-like subcalls within CodeMode's `run_code` makes CodeMode+RLM integration feasible.
