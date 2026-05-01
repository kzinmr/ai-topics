---
title: "Programmatic Tool Calling — LLM Writing Code that Calls Tools"
tags: [concept, tool-calling, code-execution, anthropic, sandbox, mcp, code-mode, harness-engineering]
created: 2026-05-01
updated: 2026-05-01
type: concept
aliases: [ptc, programmatic-tool-use, code-execution-tool]
sources:
  - https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling
  - https://www.anthropic.com/engineering/code-execution-with-mcp
status: draft
---

# Programmatic Tool Calling — LLM Writing Code that Calls Tools

## Definition

Programmatic Tool Calling (PTC) is the paradigm where an LLM writes **code (typically Python) that calls tools as async functions** within a sandboxed execution environment, rather than making sequential direct tool calls. This is the foundational API mechanism enabling CodeMode patterns.

Coined and shipped by **Anthropic** as the `code_execution_20260120` tool, it provides the `allowed_callers` field on tool definitions to control whether tools can be called directly by the model, programmatically from within code, or both.

> **The core shift:** Instead of the model saying "call tool A → get result → call tool B → get result" (N round trips), the model writes Python code that calls `await tool_a()`, processes the result with native Python, and calls `await tool_b()` — all within one round trip.

## Conceptual Hierarchy

```
Programmatic Tool Calling (API mechanism)
    └── Code Execution with MCP (architectural pattern: MCP as code API)
            └── CodeMode (specific implementations: Cloudflare V8, Pydantic Monty, Anthropic sandbox)
```

| Layer | Description | Example |
|-------|-------------|---------|
| **Programmatic Tool Calling** | API-level mechanism: `allowed_callers`, `code_execution_20260120` | Anthropic Claude API |
| **Code Execution with MCP** | Architectural pattern: treat MCP servers as code APIs | Anthropic Filesystem MCP (Nov 2025) |
| **CodeMode** | Concrete implementation: search + execute, in-process sandbox | Cloudflare MCP, Pydantic Monty |

## Key Features

### 1. `allowed_callers` Field

Each tool definition gains an `allowed_callers` field:

| Value | Meaning |
|-------|---------|
| `["direct"]` | Only callable directly by the LLM (default) |
| `["code_execution_20260120"]` | Only callable from code in the execution sandbox |
| `["direct", "code_execution_20260120"]` | Callable either way |

This creates a **security boundary**: tools like `write_file` or `send_email` can be restricted to programmatic use only, requiring the model to pass through the sandbox's safety checks.

### 2. Sandboxed Container

- **Idle timeout**: 4.5 minutes
- **Max lifetime**: 30 days
- **Stateful**: Container ID allows state persistence across requests

### 3. Token Optimization

Tool results from programmatic calls are **NOT** added to Claude's context window — only the final `stdout/stderr` output of the executed code is. This eliminates **Intermediate Result Bloat**:

**Before (direct tool calling):**
```
model: call gdrive.getDocument → full text enters context (50K tokens)
model: call salesforce.updateRecord → full text enters context again (50K tokens)
Total: ~100K tokens consumed
```

**After (programmatic tool calling):**
```
model: writes Python code → sandbox runs: 
  transcript = await gdrive.getDocument(...)
  await salesforce.updateRecord(...)
  print("Done!")
→ model sees only "Done!" (2 tokens)
Total: ~2 tokens consumed
```

### 4. Async Tool Interface

Custom tools are automatically converted to async Python functions. The model writes:

```python
results = await query_database("SELECT * FROM sales")
top_five = sorted(results, key=lambda x: x['revenue'])[:5]
print(top_five)
```

Native Python capabilities (loops, conditionals, generators, comprehensions) replace sequential tool calling patterns.

## Model Compatibility

Requires `code_execution_20260120` tool. Supported on:
- **Claude Opus**: 4.7, 4.6, 4.5
- **Claude Sonnet**: 4.6, 4.5

## Workflow

1. **Initial Request**: User asks complex question; tools provided with `allowed_callers` set
2. **API Response**: Claude returns `server_tool_use` (Python code) + `tool_use` (specific tool call requested by that code)
3. **Provide Result**: Client provides `tool_result` (message must contain ONLY `tool_result` blocks — no text)
4. **Completion**: Code execution finishes; Claude receives stdout and gives final answer

### The `caller` Field in Responses

Every `tool_use` block now includes a `caller` object:

```json
"caller": {
  "type": "code_execution_20260120",
  "tool_id": "srvtoolu_abc123"
}
```

This allows the client to distinguish between direct LLM tool calls and tool calls originating from programmatic code execution.

## Advanced Patterns

| Pattern | Description | Example |
|---------|-------------|---------|
| **Batch Processing** | Loop to query multiple endpoints in one turn | Query all regions for health status |
| **Early Termination** | Stop loop as soon as condition met | Find first "healthy" server |
| **Conditional Logic** | Choose tool based on previous result | Check file size before deciding to read |
| **Data Aggregation** | Filter/sort/transform before returning | 10K rows → 5 filtered rows |
| **Chained Operations** | Sequence of tool calls in one execution | Download → process → upload |

## Constraints

| Constraint | Detail |
|------------|--------|
| **Structured Outputs** | Tools with `strict: true` not supported |
| **Tool Choice** | Cannot force programmatic calling via `tool_choice` |
| **MCP Tools** | MCP connector tools cannot be called programmatically yet |
| **ZDR** | Not eligible for Zero Data Retention |

## Why This Is the Highest-Level Concept

Programmatic Tool Calling is the **API mechanism** that makes all CodeMode patterns possible. Without `code_execution_20260120` and `allowed_callers`, models cannot write code that calls tools — they can only make direct sequential tool calls.

The subsequent patterns build on this foundation:

- **[[concepts/code-execution-with-mcp]]** — Applies PTC to the MCP ecosystem: MCP servers as filesystem of TypeScript wrappers, progressive disclosure, PII tokenization, skills persistence
- **[[concepts/code-mode]]** — Concrete implementations: Cloudflare's server-side V8 Code Mode, Pydantic's Monty-based CodeMode, Anthropic's sandbox
- **[[concepts/rlm-recursive-language-models|RLM]]** — Applies the same code-execution pattern to long-context document processing

All three converge on the same insight: **LLMs are better at writing code than at using tools directly**, and code execution collapses N round trips into 1.

## Relation to Agentic Search Level 3

This mechanism enables the Externalized Processing pattern described in [[concepts/agentic-search]]. Cao et al.'s finding that "coding agents are effective long-context processors" is a direct consequence of programmatic tool calling: the model writes code to grep, search, and filter before the results enter the context window.

## See Also

- [[concepts/code-execution-with-mcp]] — Architectural pattern: MCP as code API
- [[concepts/code-mode]] — Specific CodeMode implementations
- [[concepts/rlm-recursive-language-models]] — RLM: code execution for long-context
- [[concepts/agentic-search]] — Externalized processing level
- [[concepts/harness-engineering/system-architecture/code-execution-with-mcp]] — Anthropic engineering blog coverage (deep dive)
- [[concepts/harness-engineering/system-architecture/advanced-tool-use]] — Related advanced tool patterns
