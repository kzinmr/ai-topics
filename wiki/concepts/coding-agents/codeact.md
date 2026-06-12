---
title: CodeAct
created: 2026-05-29
updated: 2026-05-29
type: concept
tags:
  - code-act
  - ai-agents
  - architecture
  - tool
  - plan-then-execute
  - sandbox
  - developer-tooling
  - microsoft
aliases: [Executable Code Actions, code-as-action]
related: [concepts/programmatic-tool-calling, concepts/dspy-rlm, concepts/agentic-loop, concepts/agent-sandboxing, concepts/agent-architecture-decomposition, concepts/code-mode]
sources: [raw/papers/2024-02-01_2402.01030_codeact.md, raw/articles/2026-05-20_microsoft_codeact-agent-framework.md]
---

# CodeAct (Executable Code Actions)

CodeAct is a paradigm for LLM agent action spaces: instead of emitting actions as JSON, text, or discrete tool-call blocks, the agent writes **executable Python code** as its action. The code runs in a sandboxed interpreter, and the execution result (output, errors) becomes the observation for the next turn. This unifies all agent actions — tool calls, data processing, control flow — into a single code action space.

Originated in an ICML 2024 paper by Wang et al., CodeAct demonstrated up to **20% higher success rate** over JSON/text-based actions across 17 LLMs. It has since influenced Microsoft's Agent Framework, AWS's Programmatic Tool Calling (PTC), and DSPy's RLM module.

## Discriminative Summary

CodeAct is the **action-space unification** pattern: agents express what they want to do as code, not as constrained action formats. This is distinct from:

- **PTC** — which is a *specific application* of code-as-action to tool orchestration (optimizing the "how to execute" axis)
- **RLM** — which uses code execution for *context exploration* (optimizing the "what to analyze" axis)
- **Coding agents** (Claude Code, Codex) — which write code as their *output*, not as their *action protocol*

## The Core Insight

> Instead of defining a fixed action schema (JSON function calls, text commands) and constraining the agent to it, let the agent write Python code. Code is the most expressive, compositional, and well-supported action format LLMs know — they've been trained on billions of lines of it.

### Traditional vs. CodeAct Action Spaces

| | Traditional (JSON/Text) | CodeAct |
|---|---|---|
| **Action format** | `{"tool": "search", "query": "X"}` | `result = search("X")` |
| **Multi-tool composition** | Separate turn per tool call | Loop over tools in one code block |
| **Conditional logic** | LLM must reason textually | `if result > threshold: ...` |
| **Data transformation** | LLM processes raw results in context | Python filters/aggregates deterministically |
| **Parallelism** | Not natively possible | `asyncio.gather()` or sequential in one block |
| **Error recovery** | LLM sees error text, retries next turn | Code can `try/except` and retry inline |
| **Unified surface** | Multiple formats (text, JSON, tool blocks) | One format: Python code |

## How It Works

### The CodeAct Multi-Turn Loop

```
┌──────────────────────────────────────────────────┐
│                   CodeAct Agent                    │
│                                                    │
│  User Task ──→ LLM generates Python code          │
│                      │                             │
│                      ▼                             │
│              ┌───────────────┐                     │
│              │  Python REPL  │  (Jupyter kernel)   │
│              │               │                     │
│              │  execute(code)│                     │
│              │  return(output│error)               │
│              └───────┬───────┘                     │
│                      │                             │
│                      ▼                             │
│  LLM observes result ──→ generates next code or NL │
│                                                    │
│  Loop continues until agent emits final answer     │
└──────────────────────────────────────────────────┘
```

1. Agent receives task + system prompt (which defines available tools as Python functions)
2. Agent emits Python code wrapped in `<execute>` tags
3. Python interpreter executes the code, returns stdout/stderr
4. Agent observes the result and decides: emit more code (adjust, retry, explore) or emit natural language answer to user
5. Repeat until task complete

### Example Interaction

**User:** "What's the weather in Tokyo, London, and New York? Tell me which is warmest."

**CodeAct agent (turn 1):**
```python
cities = ["Tokyo", "London", "New York"]
results = {}
for city in cities:
    results[city] = get_weather(city)  # tool exposed as Python function
print(results)
```

**REPL output:** `{"Tokyo": 22, "London": 15, "New York": 24}`

**CodeAct agent (turn 2):**
```python
warmest = max(results, key=results.get)
print(f"The warmest city is {warmest} at {results[warmest]}°C")
```

Notice: 2 turns total. Traditional JSON tool-calling would require 4+ turns (3 `get_weather` calls + final answer).

## CodeAct as Plan-then-Execute

CodeAct is one of the earliest and purest instantiations of the **Plan-then-Execute** design pattern in AI agents. The model:

1. **Plans** by writing Python code that expresses the full sequence of operations
2. **Executes** the code in one shot (or in multi-turn iterations), receiving structured results
3. **Observes** the output and either refines the plan (more code) or delivers the answer

This contrasts with the traditional **Plan-then-Call** pattern (`model → tool → model → tool → …`) where each atomic action requires its own model turn. The Plan-then-Execute pattern collapses N round-trips into ~2, shifting the bottleneck from LLM inference latency to code execution speed.

### Where CodeAct Sits in the Plan-then-Execute Landscape

| System | Plan Format | Execute Target | Year |
|---|---|---|---|
| **CodeAct** (academic) | Python code | Jupyter kernel | 2024 |
| **CodeAct** (MS Agent Framework) | Python code (single `execute_code`) | Hyperlight sandbox | 2026 |
| **PTC** (AWS Bedrock) | Python code with async tool calls | Docker sandbox / AgentCore | 2026 |
| **RLM** (DSPy) | Python code with `llm_query()` | Deno+Pyodide WASM sandbox | 2025 |
| **CodeMode** (Pydantic AI) | Python bytecode | Monty VM (Rust) | 2026 |

All share the same architectural pattern: **LLM writes code → sandbox executes → result returned** — but differ in what the code *targets* (tools vs. context vs. general computation).

## Relationship to PTC (Programmatic Tool Calling)

CodeAct and PTC share the "code as action" substrate but address different scopes:

| Dimension | CodeAct | PTC |
|---|---|---|
| **Scope** | Universal action space (any agent action is code) | Tool orchestration specifically (replacing sequential tool calls) |
| **Origin** | Academic (ICML 2024) | Industry (AWS, May 2026) |
| **Core claim** | Code outperforms JSON/text as action format | Code orchestration reduces token usage by 87-92% |
| **Iteration** | Multi-turn REPL loop (code → observe → code) | Single code block per task (code → result → final answer) |
| **Relationship** | **Ancestor paradigm** — defined the "code as action" pattern | **Application** of the pattern to tool orchestration |

CodeAct is the *general principle*; PTC is a *specific application* of that principle to the tool-calling bottleneck. PTC can be understood as "CodeAct for tool orchestration."

## Relationship to RLM (Recursive Language Models)

CodeAct and RLM share the sandboxed code execution substrate but optimize perpendicular axes:

| Dimension | CodeAct | RLM |
|---|---|---|
| **Axis** | **Action** — how the agent interacts with tools/environment | **Data** — how the agent explores/decomposes context |
| **Problem** | Action space fragmentation (JSON/text/tool blocks) | Context rot (performance degradation with context growth) |
| **What code does** | Calls tools, orchestrates actions | Explores context (`context[start:end]`), calls `llm_query()` |
| **Recursion** | Iterative code refinement across turns | Recursive sub-LLM calls (`llm_query` within `llm_query`) |
| **Relationship** | **Orthogonal** — solves a different problem | **Complementary** — RLM can call tools (PTC-in-RLM); PTC can invoke RLM |

The two are **complementary and orthogonal**: CodeAct handles the *function axis* (how to act), RLM handles the *data axis* (what to analyze). They can be combined — see [[concepts/dspy-rlm#rlm--programmatic-tool-calling-two-complementary-axes-function-axis-vs-data-axis|RLM × PTC analysis]] for the full two-axis framework.

## CodeActAgent: Fine-Tuned Models

The original paper produced two fine-tuned models trained on CodeActInstruct (7k multi-turn interactions):

| Model | Base | Context | Availability |
|---|---|---|---|
| CodeActAgent-Mistral-7b-v0.1 | Mistral-7B-v0.1 | 32k | HuggingFace, Ollama, llama.cpp |
| CodeActAgent-Llama-7b | Llama-2-7B | 4k | HuggingFace |

These models **excel at out-of-domain agent tasks** while maintaining general knowledge and dialogue capability — suggesting that code-action fine-tuning transfers broadly across agent tasks.

## Microsoft Agent Framework Implementation

Microsoft adopted CodeAct in Agent Framework (May 2026) via the **Hyperlight CodeAct** connector. This implementation differs from the academic version:

- **Single-shot execution**: The model writes one program per turn (not multi-turn REPL iteration within a turn)
- **Sandbox**: Hyperlight micro-VM instead of Jupyter kernel
- **Provider-owned tools**: Exposed via `call_tool(...)` inside the sandbox
- **Approval model**: Single approval for the entire `execute_code` call

The MS implementation emphasizes the **orchestration-overhead reduction**: "Modern AI agents often are not bottlenecked by model quality, but by orchestration overhead."

## CodeAct in the Agent Architecture Stack

In the Model/Runtime/Harness decomposition ([[concepts/harness-engineering/agent-architecture-decomposition]]):

```
Harness: Agent Framework (MS), custom orchestrator (academic)
   │
   │  Decides: "Use CodeAct for this task"
   │
   ▼
Runtime: Hyperlight sandbox (MS), Jupyter kernel (academic)
   │
   │  Executes: Python code in isolated environment
   │
   ▼
Model: Claude/GPT/CodeActAgent (any LLM capable of code generation)
```

CodeAct is a **Harness-level decision** ("generate code instead of JSON tool calls") implemented at the **Runtime level** ("execute code in sandbox"). This separation is why CodeAct works model-agnostically — any model that can write Python benefits.

## Current Landscape and Influence

CodeAct's "code as action" paradigm has become a convergent design pattern across the agent ecosystem:

| System | Code-as-Action Implementation | Year |
|---|---|---|
| CodeAct (Wang et al.) | Multi-turn Python REPL | Feb 2024 |
| RLM (DSPy) | WASM sandbox + `llm_query` recursion | Dec 2025 |
| Monty/CodeMode (Pydantic) | Rust bytecode VM, deny-by-default | Feb 2026 |
| PTC (AWS Bedrock) | Docker sandbox + async tool orchestration | May 2026 |
| CodeAct (MS Agent Framework) | Hyperlight micro-VM + provider tools | May 2026 |
| Claude Code, Codex CLI, OpenClaw | Bash runtime (code execution as primary mode) | 2025-2026 |
| MemEx (Databricks) | Persistent Python kernel + typed returns + sub-agents | May 2026 |

The pattern's convergence across academic and industrial systems suggests that **code as the universal action format** is not just one approach among many — it may be the natural endpoint for capable LLMs whose training data is dominated by code.

## Open Questions

- **Security boundary**: When the agent writes arbitrary code, sandbox isolation becomes critical. Is Hyperlight's micro-VM approach sufficient? What about supply-chain risks from imported Python packages?
- **Observability**: When N tool calls collapse into one code block, individual operations become invisible to monitoring — the opposite of distributed tracing.
- **Model capability floor**: CodeAct requires models capable of generating correct, multi-step Python programs. At what capability threshold does CodeAct become viable?
- **Approval granularity**: Per-code-block approval (MS approach) vs. per-tool-call approval (traditional) — is the trade-off acceptable for production?
