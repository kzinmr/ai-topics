---
title: "Programmatic Tool Calling — LLM Writing Code that Calls Tools"
tags:
  - concept
  - tool
  - coding-agents
  - anthropic
  - sandbox
  - mcp
  - harness-engineering
created: 2026-05-01
updated: 2026-06-03
type: concept
aliases: [ptc, programmatic-tool-use, code-execution-tool]
sources:
  - https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling
  - https://www.anthropic.com/engineering/code-execution-with-mcp
  - https://blog.cloudflare.com/project-think/
  - https://blog.cloudflare.com/code-mode/
  - raw/articles/2026-04-15_cloudflare-project-think.md
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

## Cloudflare Project Think: Dimensional Expansion of PTC

Cloudflare's **Project Think** (released April 2026) extends the PTC paradigm in the following four new dimensions. These dimensions were not covered by existing PTC analysis (Anthropic's API mechanism, Pydantic's Monty runtime).

| New Dimension | Traditional PTC Assumption | Project Think Expansion |
|---------------|---------------------------|------------------------|
| Execution Ladder | Single code execution environment | 5-tier capability escalation |
| Durable Execution | Short-lived stateless sessions (4.5 min idle timeout) | Checkpoint + resumable persistent Fiber |
| Self-Authored Extensions | LLM calls existing tools with code | LLM **generates new tools themselves** with code |
| Hibernation Economics | Always-on containers (cost proportional to agent count) | Zero idle cost with hibernation (effectively 1/100th) |

### Execution Ladder (Tiered Capability Expansion)

Traditional PTC assumes a single execution environment for "running Python/JS code in a sandbox." Project Think layers this as **5 capability tiers**, dynamically selecting execution environments based on task complexity:

```
Tier 0: Workspace (virtual filesystem)
   Virtual FS on SQLite + R2. Read/write/grep/diff only.
   Simple file operations without network.

Tier 1: Dynamic Worker (V8 Isolate)
   Sandboxed JS execution. No network access.
   Safely execute LLM-generated code.

Tier 2: npm (Runtime Package Resolution)
   Dynamic resolution and bundling of npm packages.
   import { z } from "zod" available immediately.

Tier 3: Browser (Headless Browser)
   Browser automation via Cloudflare Browser Rendering.
   E2E tests, UI verification.

Tier 4: Sandbox (Full OS Access)
   Full access to git, compilers, test runners.
   Build and test suite execution.
```

**Relationship to PTC**: Each Tier represents the trade-off between capability and isolation for PTC's code execution environment. Lower tiers are safer but limited; higher tiers are more capable but riskier. Which tier the model uses is controllable by host-side policy — understandable as a natural extension of PTC's `allowed_callers` concept.

| Dimension | Tier 0-2 (Low Risk) | Tier 3-4 (High Risk) |
|-----------|--------------------|---------------------|
| Network | Disabled | Permitted with restrictions |
| Filesystem | Virtual FS only | Real OS access |
| Packages | Allowlist-controlled | Any npm/PyPI |
| Startup time | Milliseconds | Seconds to minutes |
| Typical use | API calls, data transformation | Builds, tests, git operations |

### Durable Execution (PTC Persistence)

Anthropic's PTC container timeouts at 30 days max, 4.5 min idle. Project Think's **Fibers** are fundamentally different in design:

```typescript
// Project Think Fiber: checkpoint + resumable
void this.runFiber("research", async (ctx) => {
  const findings = [];
  for (let i = 0; i < 10; i++) {
    const result = await this.callLLM(`Step ${i}`);
    findings.push(result);
    ctx.stash({ findings, step: i });  // ← resumable from here
  }
  return { findings };
});
```

**`stash()` checkpointing**: Saves mid-execution state to Durable Objects' SQLite. Seamlessly resumes from checkpoint after eviction or platform restart.

| Dimension | Anthropic Container | Cloudflare Durable Objects |
|-----------|-------------------|---------------------------|
| Session lifetime | Max 30 days (container limit) | Unlimited (hibernation = infinite life) |
| Idle handling | Container stops at 4.5 min | Immediate hibernation (zero cost) |
| State persistence | Manual (session ID to external DB) | Automatic (SQLite + stash()) |
| Failure recovery | State lost on container restart | Automatic recovery from checkpoint |
| PTC code continuity | Complete within 1 request | Cross multiple LLM calls within a Fiber |

**Relationship to RLM**: The RLM paper's environment abstraction (REPL variable space retains state) is implicitly stateful but lacks explicit checkpoint mechanisms. Project Think's `stash()` provides a design pattern for adding explicit persistence to the RLM environment. Applicable to long-running RLM state persistence in PTC-in-RLM (Plan A) implementations.

### Self-Authored Extensions (PTC Self-Expansion — Meta-PTC)

Existing PTC analysis covers up to "LLM writes code to **efficiently call existing tools** asynchronously." Project Think abstracts this one level further, introducing a Meta-PTC layer where "LLM writes code to **generate new tools themselves**."

```
1. User: "Manage GitHub PRs"
2. Agent: Generates TypeScript program for GitHub Extension
3. Dynamic bundle with @cloudflare/worker-bundler
4. Load into Dynamic Worker → github_create_pr tool immediately available
5. Persistently usable in subsequent conversations (saved to Durable Objects)
```

```typescript
// Agent self-generated tool extension (example)
// ExtensionManager receives TypeScript, bundles npm deps,
// loads into Dynamic Worker. New tools persistently available.
self.extensionManager.add("github", {
  tools: {
    github_create_pr: async (input) => { /* ... */ },
    github_list_prs: async (input) => { /* ... */ },
  }
});
```

**Relationship to PTC**: This is an increase in abstraction from "calling tools with code (PTC Level 1)" to "creating tools with code (PTC Level 2)." Understandable in layers:

| Layer | Name | Existing Analysis | Project Think |
|-------|------|-----------------|---------------|
| L1 | **PTC as Efficiency** | Bundle N tool calls into 1 code block | ✅ Covered by existing PTC analysis |
| L2 | **PTC as Autogenesis** | Code dynamically generates new tool definitions | ❌ Not covered by existing analysis |

**Relationship to RLM**: This opens entirely new design possibilities for PTC-in-RLM (Plan A). A **3-layer recursive loop** becomes possible where the model self-generates PTC tools within the RLM environment, then uses those tools to further explore context:

```
RLM environment (context exploration)
  └── Self-generate PTC Tool
        └── Call external API with generated tool
              └── Recursive analysis of results with llm_query
```

### Hibernation Economics (Zero Idle Cost)

Project Think's **Durable Objects** model provides extreme economic asymmetry: "10000 agents but only 1% active → effectively 100 instances running." This fundamentally changes PTC's operational cost structure.

| Dimension | Anthropic (Container) | Cloudflare (Durable Objects) |
|-----------|----------------------|-----------------------------|
| Idle cost | Always pays container fee | Zero (free during hibernation) |
| State management | External DB via session ID | Built-in SQLite, state bundled with execution environment |
| Scaling | N agents = N containers | N agents = ~N × activity rate active instances |
| Code execution lifetime | 30 days (container limit) | Unlimited (hibernation = infinite life) |

**Implications for PTC design**:
- Whether the "code execution sandbox" supports hibernation qualitatively changes how PTC is used
- When implementing RLM-style "long-duration context exploration" with PTC, Anthropic's 30-day limit is a bottleneck, but Cloudflare's DO model is theoretically unlimited
- Cost differences also affect "PTC granularity design": if costs are linear, fine-grained tool calls are disadvantageous; if sub-linear, fine-grained approaches are acceptable

## Reference Runtime: Monty (Pydantic)

Monty — Pydantic's Rust-based Python interpreter — is explicitly positioned as a **runtime designed for Programmatic Tool Calling**.

> *"Monty avoids the 'faff' of containers. It is designed for Programmatic Tool Calling, where LLMs write Python code to interact with tools more reliably than traditional JSON-based tool calling."*
> — [Monty README](https://github.com/pydantic/monty)

### Why Monty Is Optimal for PTC

| Monty Feature | PTC Requirement |
|--------------|-----------------|
| 0.06ms startup (no container) | Runtime startup needed per tool call |
| Strict isolation (fs/network/env fully blocked) | Safety guarantee for LLM-generated code |
| Explicit access control via external functions | Runtime-side implementation of `allowed_callers` |
| Snapshot-capable (state serialization/restore) | State persistence for long-running PTC |
| Callable from Rust/Python/JS | Cross-platform PTC |

Monty provides the **Open Runtime** layer of the PTC pattern, combining with [[concepts/pydantic-ai-harness]]'s CodeMode functionality (Harness layer) to form the complete PTC stack.

See [[concepts/monty-sandbox]] for details.

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

## Relation to RLM: Function Axis vs Data Axis Complementarity

### Fundamental Framing

PTC and [[concepts/dspy-rlm|RLM]] apply **the same solution (code execution)** to two different fundamental problems of LLMs, but their **center of gravity differs**:

| Dimension | PTC | RLM |
|-----------|-----|-----|
| **Center** | **Tools (Function)** — "how to execute" | **Data (Context)** — "what to analyze" |
| **LLM replacement target** | Sequential tool calling (N `tool_use` blocks) | RAG / long-context prompting (stuffing all data) |
| **Problem** | Round-trip explosion, intermediate result bloat | Context rot (performance degradation from context growth) |
| **Determinism dimension** | Execution order determinism (code fixes tool call order) | Exploration strategy determinism (code fixes search scope) |
| **Freedom dimension** | Higher than sequential tool calling (branching, parallel execution possible) | Higher than RAG/long-context (freedom to control search scope and decomposition granularity) |

Your intuition is precise:

> PTC = means to achieve **deterministic execution** with higher dynamic freedom than direct LLM tool calling
> RLM = means to achieve **context length scaling and context selection** with higher dynamic freedom than RAG/long-context LLM prompting

### Complementarity Diagram

```
                ↑ RLM (Data Axis)
                │    Explore/decompose context with code
                │    context[start:end], llm_query()
                │
                │    ★ Tool-Augmented RLM
                │    context exploration + await tool() + llm_query()
                │
    ────────────┼─────────────────────────→ PTC (Function Axis)
                │    Async call tools with code
                │    await tool(), asyncio.gather()
```

### Example: Difference Between the Two Axes

**PTC (Function Axis):** Focus on how to execute tools
```python
results = await asyncio.gather(
    query_db("SELECT * FROM sales"),
    fetch_weather("Tokyo"),
)
aggregated = sorted(results[0], ...)[:5]
```

**RLM (Data Axis):** Focus on how to analyze data
```python
relevant = [s for s in context if "budget" in s.lower()]
analysis = llm_query(f"Extract from: {relevant}")
SUBMIT(analysis)
```

**Integration (Both Axes):** Handle both simultaneously
```python
relevant = [s for s in context if "revenue" in s.lower()]  # RLM
financials = await query_api({"ids": extract_ids(relevant)})  # PTC
analysis = llm_query(f"Compare: {relevant} vs {financials}")  # RLM
```

See the full analysis at [[concepts/dspy-rlm#RLM × Programmatic Tool Calling: Complementary 2 Axes (Function Axis vs Data Axis)]].

### Current Status in DSPy Implementation

| Dimension | PTC | RLM (DSPy implementation) |
|-----------|-----|---------------------------|
| **Problem** | Tool definition bloat, intermediate result bloat | Context rot (degradation from context growth) |
| **Model behavior** | Async call tools with code → filter results | Explore context with code → recursive analysis with `llm_query` |
| **Recursiveness** | None (tool calls are flat) | Essential (`llm_query` launches sub-LMs) |
| **`allowed_callers`** | Core mechanism | No concept |
| **`tools` parameter** | None | Arbitrary Python functions (no PTC-style control) |

### Integration Possibility from First Principles

Respecting the RLM paper's environment abstraction, PTC integration is actually a natural extension:

```
RLM paper environment:                        Tool-Augmented RLM:
Environment = {                        Environment = {
  REPL,                                   REPL,
  context variable, ← symbolic manipulation target  context variable,
  llm_query(),                            tools(PTC), ← same symbolic target
  SUBMIT()                                llm_query(),
}                                         SUBMIT()
                                        }
```

| RLM Environment Characteristic | Compatibility with PTC Integration |
|-------------------------------|-----------------------------------|
| Execute arbitrary Python code in REPL | PTC tools also callable with `await tool()` — extension of code |
| Results stay in REPL variable space | PTC tool results also stay in variable space, not in model context |
| Sandboxed builtins | PTC's `allowed_callers` is also a form of sandbox |
| Recursive analysis with llm_query | PTC tool results can be input to llm_query |

### Recommended Architecture: PTC in RLM (Plan A)

```
RLM Root (environment with context + tools + llm_query)
  └── Model writes Python code
        ├── context exploration          ← RLM
        ├── await tool_a()                ← PTC
        └── llm_query(...)                ← RLM recursive analysis
  └── SUBMIT(answer)
```

See [[concepts/dspy-rlm#RLM × Programmatic Tool Calling: Two Independent Paradigms]] (First Principles section) for detailed comparison and design decisions.

**Conclusion**: The DSPy implementation does not currently incorporate PTC, but this is not an architectural necessity. RLM's environment abstraction has high affinity with PTC and can be integrated with appropriate design (Plan A).

## See Also

- [[concepts/code-execution-with-mcp]] — Architectural pattern: MCP as code API
- [[concepts/code-mode]] — Specific CodeMode implementations
- [[concepts/dspy-rlm]] — RLM: same substrate (code execution), different problem (context management)
- [[concepts/rlm-recursive-language-models]] — RLM general concept
- [[concepts/agentic-search]] — Externalized processing level
- [[concepts/monty-sandbox]] — Reference runtime: Rust-based Python interpreter for PTC
- [[concepts/pydantic-ai-harness]] — Harness layer: CodeMode capability wrapping Monty
- [[concepts/harness-engineering/system-architecture/code-execution-with-mcp]] — Anthropic engineering blog coverage (deep dive)
- [[concepts/harness-engineering/system-architecture/advanced-tool-use]] — Related advanced tool patterns
