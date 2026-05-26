---
title: "DSPy.RLM"
type: concept
description: "Recursive Language Model — DSPy module for programmatic exploration of large contexts via a sandboxed Python REPL"
category: concepts
sub_category: AI Agent Architectures
tags:
  - dspy
  - rlm
  - context-management
  - inference
  - sandbox
  - developer-tooling
  - coding-agents
  - company
status: complete
related:
  - dspy
  - gea
  - alex-zhang
  - omar-khattab
  - context-fragments
  - long-context-coding-agents
created: 2026-04-21
updated: 2026-04-30
sources:
  - https://dspy.ai/api/modules/RLM/
  - https://github.com/alexzhang13/rlm
  - https://dspy.ai/tutorials/rl_ai_program/
---

# DSPy.RLM (Recursive Language Model)

## TL;DR

RLM is a DSPy module that allows LLMs to **programmatically explore large contexts through a sandboxed Python REPL**. Instead of stuffing context directly into prompts, it separates "variable space" (data in the REPL) from "token space" (what the LLM processes), allowing the model to dynamically load context only when truly needed.

> *"Most people misunderstand RLMs to be about LLMs invoking themselves. The deeper insight is LLMs interacting with their own prompts as objects."*
> — Omar Khattab

## Core Concepts

### Problem: Context Rot

The phenomenon where LLM performance degrades as context grows larger (**context rot**). Traditional approaches push all context into the prompt, but RLM solves this through **selective reading**.

### Architecture: REPL Loop

RLM operates through the following iterative loop:

```
1. LLM receives context overview metadata (not the full context)
2. LLM writes Python code to explore data (search, filter, aggregate)
3. Code executes in a sandboxed interpreter, output shown to LLM
4. llm_query(prompt) invokes sub-LLM for semantic analysis
5. SUBMIT(output) returns the final answer and terminates
```

### Variable Space vs Token Space

| Space | Content | LLM Processing |
|------|------|-----------|
| **Variable Space** | Data within REPL (full context) | Manipulated via code |
| **Token Space** | What the LLM actually processes | Metadata + output results |

## API Reference

### Constructor Parameters

| Parameter | Type | Default | Description |
|-----------|----|-----------|------|
| `signature` | `str \| Signature` | Required | I/O definition (e.g., `"context, query -> answer"`) |
| `max_iterations` | `int` | 20 | Maximum REPL interaction loops |
| `max_llm_calls` | `int` | 50 | Maximum llm_query calls per execution |
| `max_output_chars` | `int` | 10,000 | Maximum characters in REPL output |
| `verbose` | `bool` | `False` | Detailed log output |
| `tools` | `list[Callable]` | `None` | Additional tool functions callable from interpreter |
| `sub_lm` | `dspy.LM` | `None` | LM for subqueries (default: `dspy.settings.lm`). Cheaper model recommended |
| `interpreter` | `CodeInterpreter` | `None` | Custom interpreter (default: Deno/Pyodide WASM) |

### Built-in Tools

| Tool | Description |
|-------|------|
| `llm_query(prompt)` | Semantic analysis with sub-LLM (~500K chars supported) |
| `llm_query_batched(prompts)` | Parallel execution of multiple prompts (batch processing) |
| `print()` | Output display (essential for checking results) |
| `SUBMIT(...)` | Submit final output to end execution |
| `re, json, collections, math` | Standard Python libraries |

## Usage Examples

### Basic Usage

```python
import dspy

dspy.configure(lm=dspy.LM("openai/gpt-5"))

rlm = dspy.RLM("context, query -> answer")

result = rlm(
    context="...very long document or data...",
    query="What is the total revenue mentioned?"
)
print(result.answer)
```

### Using a Cheaper Sub-LM

```python
main_lm = dspy.LM("openai/gpt-5")
cheap_lm = dspy.LM("openai/gpt-5-nano")  # Delegate extraction to cheap model

dspy.configure(lm=main_lm)
rlm = dspy.RLM("data, query -> summary", sub_lm=cheap_lm)
```

### Multi-Type Output

```python
rlm = dspy.RLM("logs -> error_count: int, critical_errors: list[str]")
result = rlm(logs=server_logs)
print(f"Found {result.error_count} errors")
```

### Custom Tools

```python
def fetch_metadata(doc_id: str) -> str:
    """Fetch metadata for a document ID"""
    return database.get_metadata(doc_id)

rlm = dspy.RLM(
    "documents, query -> answer",
    tools=[fetch_metadata]
)
```

### Async Execution

```python
import asyncio

rlm = dspy.RLM("context, query -> answer")

async def process():
    result = await rlm.aforward(context=data, query="Summarize this")
    return result.answer

answer = asyncio.run(process())
```

### Trajectory Inspection

```python
result = rlm(context=data, query="Find the magic number")

for step in result.trajectory:
    print(f"Code:\n{step['code']}")
    print(f"Output:\n{step['output']}\n")
```

## Output Structure

`dspy.RLM` returns a `Prediction`:

- Output fields defined in the signature (e.g., `result.answer`)
- `trajectory`: List of dicts containing reasoning, code, output for each step
- `final_reasoning`: LLM reasoning from the final step

## Setup Requirements

### Deno Required

RLM builds a WASM sandbox using **Deno + Pyodide**:

```bash
curl -fsSL https://deno.land/install.sh | sh
```

> ⚠️ **Known Issue**: Deno cache visibility problem from DSPy has been reported. After restarting your shell, verify with `deno --version`.

External sandbox provider support is planned (documentation in progress).

## Benchmark Results

| Model | Performance |
|-------|------|
| RLM(GPT-5-mini) vs GPT-5 | **114% improvement** on OOLONG (132k context) |
| RLM-Qwen3-8B vs Qwen3-8B | **28.3% improvement** average across 4 benchmarks |
| Cost | Equivalent to or below base model calls (median) |

## Technical Depth

### RLM ≠ Self-Invocation

As Khattab emphasizes, the essence of RLM is not "LLMs calling themselves." The deeper insight:

> *"LLMs interacting with their own prompts as objects"*

In other words, the LLM manipulates its own prompt **as data**. This applies **out-of-core algorithm design** patterns to language models.

### Connection to the Mismanaged Geniuses Hypothesis

RLM is an implementation proof of the **Recursive type** in the [Mismanaged Geniuses Hypothesis](mismanaged-geniuses-hypothesis):

- Decomposition to arbitrary depth via `for` loops
- Near-infinite context handling through programmatic decomposition

### Connection to Context Fragments

RLM's "externalized objects" are the inspiration behind [Context Fragments](context-fragments). REPL variables function as context fragments.

## RLM Implementation Patterns in pydantic-ai

The same "REPL-mediated context decomposition" as DSPy's RLM can be achieved with pydantic-ai + Monty, though the approach differs.

| Dimension | DSPy.RLM | pydantic-ai native |
|---|---|---|
| REPL | Deno + Pyodide (WASM sandbox) | Monty (Rust bytecode VM) |
| Loop Control | DSPy module internals | Agent output function / pydantic-graph |
| State Management | REPL variable space | Monty snapshot + message_history |
| Control Authority | DSPy framework | Pydantic AI (Agent around REPL) |

Implementation pattern is 3 stages (details in [[concepts/code-mode]]):

1. **Minimal form**: `Agent(..., capabilities=[CodeMode()], output_type=submit)` — near-RLM UX with minimal custom implementation
2. **DSPy-compatible loop**: `RunCode | FinalAnswer` structured output + explicit Action→Execute→Observe loop
3. **graph-native version**: Decompose Plan/RunCode/Observe/Finalize into pydantic-graph nodes + Monty snapshot for durable execution

## RLM × Programmatic Tool Calling: Two Complementary Axes (Function Axis vs Data Axis)

### Fundamental Framing

RLM and [[concepts/programmatic-tool-calling|PTC]] can be understood as applying the same solution (code execution) to two fundamentally different LLM problems:

| Axis | Problem PTC Solves | Problem RLM Solves |
|----|------------------|------------------|
| **Center** | **Tools (functions)** — "how to execute" | **Data (context)** — "what to analyze" |
| **What LLM replaces** | Sequential tool calling (N `tool_use` blocks) | RAG / long-context prompting (stuffing all data) |
| **Problem** | Round-trip explosion, intermediate result bloat | Context rot (performance degradation with context growth) |
| **What code writes** | `await tool_a()`, `asyncio.gather()` | `context[start:end]`, `re.findall()`, `llm_query()` |
| **Code purpose** | Freely control tool execution order, branching, parallelization | Freely choose data exploration scope and decomposition methods |
| **Code I/O** | Choose inputs, call tools, receive results in variables | Extract context segments, analyze, aggregate into answers |
| **Determinism dimension** | Execution order determinism (same code → same tools in same order) | Exploration strategy determinism (same code → same scope) |
| **Freedom dimension** | Higher than sequential tool calling (conditional branching, parallel execution via code) | Higher than RAG/long-context (freely control exploration scope and decomposition granularity via code) |

### Complementary Relationship Diagram

```
                ↑ RLM (Data Axis: what to analyze)
                │   Code explores, decomposes, recursively analyzes context
                │   context[start:end], llm_query(), SUBMIT()
                │
                │   ★ Tool-Augmented RLM (Option A)
                │   PTC in RLM — adds tools to environment
                │   context exploration + await tool() + llm_query()
                │
    ────────────┼──────────────────────────────────→ PTC (Function Axis: how to execute)
                │   Code async-calls tools, parallelizes
                │   await tool(), asyncio.gather()
                │
                │   RLM as PTC Tool (Option B)
                │   PTC agent calls RLM as one of its tools
```

### Concrete Examples of the Difference

**PTC Code (Function Axis):**
```python
# Focused on "how to execute"
results = await asyncio.gather(
    query_database("SELECT * FROM sales"),
    fetch_weather("Tokyo"),
    search_docs("budget 2025"),
)
aggregated = sorted(results[0], key=lambda x: x['revenue'])[:5]
print(aggregated)
```

**RLM Code (Data Axis):**
```python
# Focused on "what to analyze"
budget_sections = [s for s in context if "budget" in s.lower()]
for i, section in enumerate(budget_sections[:10]):
    analysis = llm_query(f"Extract key numbers from: {section}")
    print(f"Section {i}: {analysis}")
SUBMIT(synthesized_answer)
```

**Integrated Code (Tool-Augmented RLM, Option A):**
```python
# Handles both axes simultaneously
relevant = [s for s in context if "revenue" in s.lower()]  # RLM: context exploration
financials = await query_financial_api({"ids": extract_ids(relevant)})  # PTC: external execution
analysis = llm_query(f"Compare: {relevant} vs {financials}")  # RLM: recursive analysis
print(analysis)
```

### Why This Framing Matters

If you lump PTC and RLM together under "code execution" as a common substrate, you lose sight of **the fundamentally different problems each solves**. Conversely, treating them as "completely unrelated" causes you to **miss the synergistic effects of integration**.

Correct understanding:
- PTC optimizes the **function axis** (improving inefficient standard tool calling via code)
- RLM optimizes the **data axis** (improving inefficient RAG/long-context via code)
- The two are orthogonal, so integration (Tool-Augmented RLM, Option A) can optimize both axes simultaneously

### Directional Symmetry: PTC merges, RLM splits

A deeper symmetry exists:

```
PTC: Merges decomposed tool calls into efficient bundles
     [tool_call_1] + [tool_call_2] + ... + [tool_call_N]
     → 1 code block: await tool_a(); await tool_b()

RLM: Splits unified context via divide and conquer
     [single huge context]
     → Code-based exploration: relevant = [s for s in context if ...]
     → Recursive llm_query: for section in relevant: llm_query(section)
```

| Direction | PTC | RLM |
|--------|-----|-----|
| **Operation** | **Merge** — Bundle scattered tool calls into one code block | **Split** — Use code to slice massive context into individually processed fragments |
| **Problem shape** | N independent calls → 1 code block | 1 massive data blob → N fragments |
| **Bottleneck** | Round-trip count (model round trips) | Context size (what can be read at once) |
| **Improvement method** | Hand parallel execution, conditionals, aggregation to code | Hand selective reading, recursive analysis to code |

In other words, PTC goes in the **bundling direction** while RLM goes in the **splitting direction** — they are precisely symmetric and orthogonal.

### RLM = Soft MapReduce for Context, Performed by LLM

RLM can be understood as "MapReduce for context":

```
MAP Phase (exploration, decomposition):
  context[start:end]             ← context extraction
  re.findall(pattern, context)    ← keyword search
  [s for s in context if cond]  ← filtering

SHUFFLE (intermediate aggregation):
  llm_query("Extract from: {section}")  ← analyze each fragment with sub-LM

REDUCE (final aggregation):
  llm_query("Synthesize: {analyses}")   ← integrate results
  SUBMIT(final_answer)                   ← final answer
```

Differences from traditional MapReduce:
- **Split units are not fixed**: Model dynamically decides decomposition method per task (regex, semantic boundaries, size thresholds, etc.)
- **LLM-based aggregation**: Not just summing or concatenating — `llm_query` enables semantic aggregation
- **Recursive**: Map phase can further MapReduce (llm_query within llm_query)
- **Strategy itself is dynamic**: Model selects "what to Map" and "how to Reduce" per task

### Context Splitting Strategy is Chosen by the LLM Itself — And Is Free-Form

> **In RLM, the context splitting strategy itself is handled by the LLM**

**Yes, this is the essence of RLM.** The paper's core insight:

> *"Unlike prior agentic methods that rigidly define these workflow patterns, RLMs defer these decisions entirely to the language model."*
> — RLM paper, §5

Where prior methods hardcode splitting strategies (RAG uses fixed chunk size + retriever; agentic workflows use fixed DAGs), RLM **lets the model itself decide**. This is the source of its "softness."

#### Spectrum: From Manual Splitting to Tool Delegation

In RLM's environment, the model can dynamically choose from this spectrum:

| Level | Method | Model's Code | Characteristics |
|--------|------|--------------|------|
| **1. Fully Manual** | Split with raw Python | `context[1000:2000]`, `re.findall()` | Maximum control, fully transparent |
| **2. Semi-Manual (helper functions)** | Define helper functions in code | `def chunk_by_section(text): ...` | Flexible but longer code |
| **3. Tool Delegation** | Call environment PTC tools | `await chunk_document(context, strategy="topic")` | Efficient but depends on tool design |
| **4. Recursive Delegation** | Delegate to sub-LM via llm_query | `llm_query(f"Split and analyze: {section}")` | Most flexible, highest cost |

**Key freedom**: The model can choose the appropriate level per task. Simple date search → Level 1 (`re.findall`); complex semantic splitting → Level 4 (delegate to `llm_query`).

#### Extension in Tool-Augmented RLM

Option A (PTC in RLM) enriches tool delegation for splitting strategies:

```python
# Splitting strategy options in Tool-Augmented RLM (model dynamically selects):

# Option 1: Manual split (raw Python)
relevant = [s for s in context if "festival" in s.lower()]

# Option 2: Delegate to tool (provided as PTC tool)
sections = await chunk_by_topic(context, max_tokens=2000)
relevant = [s for s in sections if topic_relevance(s, query) > 0.8]

# Option 3: Recursive delegation (delegate semantic decomposition to llm_query)
analysis = llm_query(f"Find all sections about festivals in: {context[:50000]}")

# Option 4: Combination
# First roughly split with tool, recursively analyze each part
sections = await chunk_by_semantic_boundary(context)
for s in sections:
    if llm_query(f"Is this relevant to {query}? Answer yes/no: {s[:500]}") == "yes":
        details = llm_query(f"Extract details: {s}")
        print(details)
```

#### Summary: RLM Splitting Strategy Freedom

RLM's context splitting freedom is realized across three axes:

1. **Freedom of means**: Raw Python, helper functions, environment tools, llm_query — the model decides which means
2. **Freedom of granularity**: Character-level, semantic-level, keyword-level — dynamically chosen per task
3. **Freedom of depth**: One split to completion, recursive deep dive, or abort as needed — the model decides how far to decompose

Calling this "soft MapReduce" is extremely accurate, and this is where RLM's essential advantage over traditional RAG (fixed chunk + fixed top-k) and Agentic Workflow (fixed DAG) lies.

### Current State in DSPy Implementation and First-Principles Possibilities

### RLM Does Not Explicitly Incorporate PTC

After scrutinizing the RLM paper (arXiv:2512.24601, Dec 2025) and DSPy.RLM API:

1. **RLM's only built-in tool is `llm_query(prompt)`** — This is not an external tool call but the model's own recursive subquery. The PTC `allowed_callers` concept does not exist.
2. **RLM's `tools` parameter accepts generic `Callable`s** — Arbitrary Python functions are accepted, but PTC-style "async tool wrapping + allowed_callers" is not provided.
3. **RLM solves "context management"** — Giant documents are given as REPL variables, and the model explores/decomposes/recursively queries via code. "Tool orchestration" (what PTC solves) is out of scope.

### Problem Difference

| Dimension | RLM | Programmatic Tool Calling |
|------|-----|--------------------------|
| **Problem** | Context rot (performance degradation from context growth) | Tool definition bloat, intermediate result bloat |
| **Search space** | 1M+ token documents | 2,500+ API endpoints |
| **Model behavior** | Code explores context → `llm_query` recursive analysis | Code async-calls tools → filters results |
| **Recursion** | **Essential** — `llm_query` launches sub-LM | **None** — tool calls are flat |
| **Tool origin** | `tools` parameter (arbitrary Python functions) | MCP/API tool definitions with `allowed_callers` |
| **`allowed_callers`** | Concept absent | **Core mechanism** |

### Common Substrate

Both share only the **sandboxed code execution** substrate:

```
LLM writes code → executes in sandbox → only results returned to model
```

This substrate is the same, but the code **content** is fundamentally different:

- RLM code: `data[start:end]`, `re.findall(pattern, text)`, `llm_query("summarize this")`, `SUBMIT(answer)`
- PTC code: `await tool_a(input)`, `await tool_b(result)`, `asyncio.gather(...)`, `print(filtered)`

### Architectural Freedom: Composable but Not Designed

Passing PTC-like tool functions to RLM's `tools` parameter is **technically possible**:

```python
# Pass PTC-like functions to RLM's tools (possible, but lacks PTC async wrapping)
rlm = dspy.RLM(
    "context, query -> answer",
    tools=[search_api, fetch_document]  # arbitrary Python functions
)
```

But this is **accidental extensibility, not designed integration**. The following constraints apply:

1. No PTC `allowed_callers` security boundary — all code within RLM can access all tools
2. No auto async-wrapping of tools — PTC automatically converts tools to async
3. No `caller` identifier — PTC responses include a `caller` field to trace code→tool invocation
4. No guaranteed context exclusion of tool results — PTC automatically excludes programmatic call results from context

### Conclusion: Two Independent Paradigms

```
RLM:                                   PTC:
Code explores context                  Code calls tools
    ↓                                       ↓
Recursive analysis via llm_query        External execution via await tool()
    ↓                                       ↓
Final answer via SUBMIT                 Termination via print(stdout)
```

The two have a **complementary relationship**:
- RLM selects "what to analyze" (context decomposition)
- PTC controls "how to execute" (tool orchestration)

True integration (calling PTC tools within RLM → recursively analyzing results) currently requires **manual configuration** and is not framework-supported. However, [[concepts/pydantic-ai-harness]] (Monty + CodeMode) is the closest platform to encompassing both.

### First-Principles Re-examination: Environment Extension Design for PTC Integration

The above analysis is accurate for "current state of DSPy.RLM implementation," but from the **pure architecture** of the RLM paper, PTC integration is rather a natural extension.

#### RLM Paper's Environment Abstraction

The RLM paper defines the environment as consisting of 3 elements:

```
Environment = {
  REPL: Python execution environment (persistent state, sandboxed builtins)
  context variable: massive input data
  llm_query(): recursive sub-LM invocation
  SUBMIT(): final answer
}
```

This environment is designed as **"the set of objects the model can symbolically manipulate."** The paper emphasizes:

> *"The key insight is that long prompts should not be fed into the neural network directly but should instead be treated as **part of the environment** that the LLM can **symbolically interact with**."*

The paper only envisions the `context` variable as an "environment part," but **this abstraction is extensible to any "symbolically manipulable object."**

#### Tool-Augmented Environment Design

Design for integrating PTC tools as first-class citizens of the RLM environment:

```
Tool-Augmented Environment = {
  REPL: Python execution environment (sandboxed, async-capable)
  context variable: input data (from RLM)
  tools: PTC tool collection (exposed as async functions) ← NEW
  llm_query(): recursive sub-LM invocation (from RLM)
  SUBMIT(): final answer (from RLM)
}
```

The RLM loop structure is unchanged, but the code can target more objects.

#### Why RLM's Environment Abstraction Is PTC-Compatible

| RLM Environment Property | PTC Integration Compatibility |
|--------------|------------------|
| **REPL executes arbitrary Python code** | PTC tools can be called via `await tool()` — a natural code extension |
| **Results remain in REPL variable space** | PTC tool results don't enter model context; kept in variable space |
| **sandboxed builtins** | PTC's `allowed_callers` is a form of sandbox |
| **Recursive analysis via llm_query** | PTC tool results can serve as llm_query input |
| **Final answer via SUBMIT** | Submit final answer including PTC tool results |

#### Three Integration Architectures

Respecting the paper's environment abstraction, three architectures are conceivable:

##### Option A: PTC in RLM (RLM outer, PTC inner) ★ Recommended

```
RLM Root (environment has context + tools + llm_query)
  └── Model writes Python code
        ├── context[start:end]  ← RLM: context exploration
        ├── await tool_a()       ← PTC: tool invocation
        └── llm_query(...)       ← RLM: recursive analysis
  └── SUBMIT(answer)
```

**Advantage**: Maintains RLM's loop structure (explore→analyze→aggregate) while adding PTC tools. High environmental consistency.

##### Option B: RLM as PTC Tool (PTC outer, RLM as one tool)

```
PTC Agent
  ├── await search_db(query)
  ├── await rlm_analyze(context, sub_query)  ← Call RLM as a "tool"
  ├── await fetch_details(ids)
  └── submit(answer)
```

**Advantage**: Directly compatible with Anthropic's PTC API. However, RLM's recursive exploration gets buried in "external tool calls," losing the naturalness of context exploration.

##### Option C: Dual Environment (two-layer environment)

```
Layer 1: PTC Environment (tool orchestration)
  └── await tool_a(), await tool_b()
      └── Layer 2: RLM Environment (context decomposition)
            └── context exploration, llm_query(), SUBMIT()
```

**Advantage**: Separation of concerns. However, environment switching has overhead.

#### Design Challenges

True integration requires the following design decisions:

1. **Tool Discovery**: How to inject PTC tool definitions (input_schema) into the RLM environment?
   - Cloudflare CodeMode insight: compress into two tools: `search()` + `execute()`
   - → Add `discover_tools(query)` + `call_tool(name, args)` to the environment

2. **Security Boundary**: How to impose `allowed_callers`-equivalent control on the REPL?
   - RLM paper's sandboxed builtins only "remove dangerous functions"
   - PTC uses a positive model: "can only call permitted tools"
   - → Add `allowed_callers`-equivalent allowlist to RLM's sandbox

3. **Result Routing**: PTC tool results don't enter model context; kept in REPL variable space
   - RLM already only shows `print()` output to the model
   - → Only `print()`ed PTC tool results enter model context (natural extension)

4. **Interaction with Recursion**: Synthesizing PTC tool results + recursive llm_query
   - → `llm_query(tool_result + context_snippet)` can synthesize both (natural in REPL variable space)

#### Summary

That DSPy.RLM currently doesn't "explicitly incorporate" PTC is an implementation constraint, not an **architectural necessity**. The RLM paper's environment abstraction is designed to host PTC tools as first-class citizens.

Design-wise, **Option A (PTC in RLM)** is superior:
- Maintains RLM's loop structure
- Naturally integrates PTC tools as environment parts
- Cloudflare CodeMode's `search()+ execute()` pattern can be ported to the environment layer
- pydantic-ai-harness (Monty + CodeMode) is closest to this architecture in implementation

The shortest implementation path: upgrade RLM environment's `tools` parameter from "a list of plain Python functions" to "a PTC tool collection with async support, allowed_callers, and automatic result filtering." This is achievable either as a DSPy.RLM change or as an independent implementation on pydantic-ai-harness.

## Status & Known Issues

| Item | Status |
|------|----------|
| API Stability | **Experimental** — Subject to change in future versions |
| Thread Safety | Not thread-safe when using custom interpreter. Create separate instances for parallel use |
| Deno Dependency | Required — pay attention to installation and cache configuration |

## Related Projects

- [DSPy](dspy) — Declarative LM programming framework that provides RLM
- [GEPA](gepa) — Genetic Pareto Prompt Evolution by same authors
- [Alex Zhang](alex-zhang) — RLM first author
- [Omar Khattab](omar-khattab) — RLM co-author, DSPy founder
- [Context Fragments](context-fragments) — Concept inspired by RLM's externalized objects
- [Long Context Coding Agents](long-context-coding-agents) — RLM-related technology
- [[concepts/pydantic-ai-harness]] — Monty-based CodeMode
- [[concepts/code-mode]] — Agent around REPL pattern details
- [[concepts/monty-sandbox]] — Rust REPL sandbox

## See Also

- [[concepts/_index]]
- [[concepts/rlm-recursive-language-models]]
- [[concepts/dspy]]
