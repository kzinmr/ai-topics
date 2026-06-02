---
title: Programmatic Tool Calling (PTC)
created: 2026-05-29
updated: 2026-05-29
type: concept
tags: [tool-use, ai-agents, agent-architecture, agent-infrastructure, sandbox, token-economics, cost-optimization, agent-design-patterns, aws, bedrock]
aliases: [PTC, code-orchestrated-tool-calling]
related: [concepts/agent-hosting-aws, concepts/agentic-loop, concepts/codeact, concepts/rlm-recursive-language-models, concepts/code-execution-with-mcp, concepts/code-mode]
sources: [raw/articles/2026-05-19_aws_ptc-bedrock-agentcore.md, raw/articles/2025-11-24_anthropic_advanced-tool-use.md, raw/articles/2026-06-02_anthropic_cookbook_ptc.md]
---

# Programmatic Tool Calling (PTC)

A paradigm shift in AI agent tool interaction: instead of calling tools **one-at-a-time** through sequential LLM round-trips, the model generates **Python code** that orchestrates multiple tool calls programmatically (with loops, conditionals, parallelism, and filtering) inside a sandboxed execution environment. Only the final processed result — not the intermediate data — enters the model's context window.

## Key Insight

> Instead of orchestrating tool calls one at a time, the model writes code — typically Python — that invokes multiple tools programmatically within a sandboxed execution environment. The model is only sampled once to produce the code and once to interpret the final output. — AWS ML Blog, May 2026

## Traditional vs. PTC

| Dimension | Traditional Sequential Tool Calling | Programmatic Tool Calling (PTC) |
|---|---|---|
| **Tool invocation** | One at a time, LLM decides each | Python code orchestrates all |
| **Model sampling** | N+1 times (N tool calls + final) | **2 times** (code gen + answer) |
| **Data processing** | Natural language reasoning | **Python** (deterministic) |
| **Parallelism** | Not possible (sequential) | **Yes** (`asyncio.gather()`) |
| **Intermediate data** | All enters context window | **Never enters context** |
| **Token consumption** | High (all intermediate results) | **87-92% lower** |
| **Accuracy on tabular data** | Model-dependent, error-prone | **Deterministic** (Python logic) |

## How It Works

### The PTC Loop

```
User Query → LLM generates Python code → Sandbox executes code
                                              │
                                    ┌─────────┴─────────┐
                                    │ Tool A  Tool B ... │  (parallel, via asyncio)
                                    │ Filter, aggregate  │  (Python logic)
                                    └─────────┬─────────┘
                                              │
                                    Only final print() → LLM formats answer → User
```

1. **Tool definitions are embedded in the system prompt**, not in `tool_config`
2. The LLM writes a single Python script that calls all necessary tools
3. The script runs in a **sandbox** (Docker container, AgentCore, or equivalent)
4. Tool calls are **intercepted** by the orchestrator (via IPC) and executed externally
5. Results are returned to the sandbox for further processing
6. Only the final `print()` output is sent back as a `tool_result` to the LLM
7. The LLM formats the answer — all intermediate data never touched its context

### Example: Expense Audit

Traditional: 20 `get_expenses` calls → 2,000+ records → all enter context → LLM reasons over raw data

PTC: Single Python script with `asyncio.gather()` runs all 20 calls in parallel → filters/aggregates in Python → only 3 names with budget violation summary reaches LLM

## Token Reduction Benchmarks (AWS, May 2026)

Expense audit task across 8 models on Amazon Bedrock. All 8 models produced **correct** answers in PTC mode; only Claude models were correct in sequential mode.

| Model | PTC tokens | Non-PTC | Reduction |
|---|---|---|---|
| Kimi 2.5 (thinking) | 10,875 | 148,085 | **92.7%** |
| DeepSeek V3.2 (thinking) | 19,543 | 245,967 | **92.1%** |
| Claude Sonnet 4.6 (adaptive) | 12,739 | 128,043 | **90.1%** |
| GLM 4.7 (thinking) | 11,550 | 115,829 | **90.0%** |
| Claude Opus 4.6 (adaptive) | 13,043 | 126,152 | **89.7%** |
| Qwen3-Coder-480B | 34,159 | 305,114 | **88.8%** |
| MiniMax M2.1 (thinking) | 11,787 | 101,990 | **88.4%** |
| Qwen3-Next-80B | 28,878 | 233,332 | **87.6%** |

## Cost Impact

At 1,000 executions/day with Claude Sonnet pricing ($3/$15 per 1M input/output):

| | Non-PTC | PTC |
|---|---|---|
| Daily | ~$520 | ~$52 |
| Monthly | ~$15,600 | ~$1,560 |
| **Monthly savings** | — | **~$14,040 (90%)** |

## Implementation Approaches

### 1. Self-Hosted (ECS + Docker Sandbox)

Best for: teams needing full control, custom packages, private deployment.

- **Orchestrator**: ECS task or Lambda calling Bedrock `InvokeModel` via Boto3
- **Sandbox**: Docker container, IPC over stdin/stderr
- **Protocol**: Orchestrator intercepts tool calls from sandbox stdout, executes externally, returns results to sandbox stdin
- Model-agnostic — same sandbox, same protocol, only `model_id` changes

### 2. Managed (AgentCore Code Interpreter)

Best for: teams wanting zero operational overhead.

- Fully managed sandbox in Amazon Bedrock AgentCore
- Automatic sandbox lifecycle, security isolation, scaling
- No Docker management, no IPC protocol implementation
- Integrated with CloudWatch monitoring

### 3. Anthropic SDK Compatible (Proxy)

Best for: teams already using the Anthropic SDK.

- Proxy translates between Anthropic SDK interface and Bedrock API
- Drop-in replacement — no application code changes
- Proxy handles model translation, sandbox management, full PTC protocol

## Why PTC Matters for Agent Architecture

PTC fundamentally changes the **tool-calling layer** of agent architectures:

1. **Historically**: Agent loop = LLM → tool call → result → LLM → next tool call — the "Ralph Wiggum loop"
2. **With PTC**: Agent loop = LLM → code → sandbox (execute all tools) → LLM — two round-trips total

This shifts the bottleneck from **LLM inference latency** to **code execution speed**, and from **token cost** to **sandbox compute cost** (which is orders of magnitude cheaper).

### Implications for Agent Design

- **Planning agents** can generate complete execution plans as code rather than step-by-step tool calls
- **Research agents** can query dozens of sources in parallel, filter and deduplicate in Python
- **Coding agents** already work this way — PTC extends the pattern to general tool use
- **Security boundary shifts** from "trust the LLM's tool selection" to "trust the sandbox to contain the LLM's code" — sandbox isolation becomes critical

## Related Concepts

- [[concepts/rlm-recursive-language-models]] — RLM's 2-Axis Complementarity framework: PTC is the **Function Axis** (merge N tool calls → 1 code block), RLM is the **Data Axis** (split 1 huge context → N pieces). Together they form a complete framework for model-driven computation. Tool-Augmented RLM combines both.
- [[concepts/dspy-rlm]] — DSPy.RLM implementation: full PTC relationship analysis, merge/split symmetry, Tool-Augmented RLM design
- [[concepts/code-execution-with-mcp]] — Middle architectural layer between PTC and CodeMode: MCP as code API with progressive disclosure
- [[concepts/code-mode]] — Specific implementations (Cloudflare V8, Pydantic Monty) of the code-execution-over-tool-calling pattern
- [[concepts/agent-hosting-aws]] — AWS infrastructure for running agents, including PTC sandboxes
- [[concepts/agentic-loop]] — The canonical agent execution loop that PTC optimizes
- [[concepts/agent-sandboxing]] — Sandbox isolation is critical for PTC safety
- [[concepts/search-as-code]] — Perplexity's SaC applies PTC pattern to search domain with domain-specific SDK
- [[raw/articles/2026-05-19_aws_ptc-bedrock-agentcore.md]] — Full AWS blog post with implementation details
- [[raw/articles/2026-06-02_anthropic_cookbook_ptc.md]] — Anthropic Cookbook: PTC with Claude API (Pedram Navid, 2025). Team expense analysis example, 85.6% token reduction, `allowed_callers` + `code_execution` tool setup
