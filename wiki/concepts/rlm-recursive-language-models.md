---
title: "RLM (Recursive Language Models)"
tags:
  - training
  - concept
  - ai-agents
  - model
  - prompting
  - rag
  - evaluation
  - inference
  - context-management
  - coding-agents
created: 2026-04-13
updated: 2026-05-01
type: concept
sources:
  - https://arxiv.org/abs/2512.24601
  - https://alexzhang13.github.io/blog/2025/rlm/
  - https://dspy.ai/api/modules/RLM/
  - https://github.com/alexzhang13/rlm
---

# RLM (Recursive Language Models)

## Overview

Recursive Language Models (RLMs) are a task-agnostic inference paradigm proposed by **Alex Zhang, Tim Kraska, and Omar Khattab** (MIT CSAIL/OASYS Lab) that allows language models to handle **near-infinite length contexts** by programmatically examining, decomposing, and recursively calling themselves over input snippets.

- **Paper:** arXiv:2512.24601 (Dec 2025, revised Jan 2026)
- **Blog:** [alexzhang13.github.io/blog/2025/rlm](https://alexzhang13.github.io/blog/2025/rlm/)
- **Code:** [github.com/alexzhang13/rlm](https://github.com/alexzhang13/rlm) (3,296 stars)
- **Minimal:** [github.com/alexzhang13/rlm-minimal](https://github.com/alexzhang13/rlm-minimal) (749 stars)
- **Docs:** [alexzhang13.github.io/rlm](https://alexzhang13.github.io/rlm/)
- **PyPI:** `rlms` — 6,034 downloads/month

## Core Architecture

### The Fundamental Shift: Context as Environment

RLMs replace the canonical `llm.completion(prompt, model)` call with `rlm.completion(prompt, model)`. The key innovation:

> "RLMs offload the context as a variable in a REPL environment that the LM can interact with and launch sub-LM calls inside of."
> — Alex Zhang, RLM blog post (Oct 2025)

**How it works:**
1. **Persistent REPL:** The full input is loaded into a Python REPL as a string variable. The root model never sees the full context at once.
2. **Programmatic Decomposition:** The LLM writes Python code to peek into, slice, and transform the context variable.
3. **Recursive Sub-calls:** The model spawns sub-LM calls (`llm_query`) on shorter, programmatically constructed prompts.
4. **Final Synthesis:** The main model aggregates results and produces a final answer.

### REPL Environment Design

The RLM uses the REPL as a **control plane** for long context:
- Environment is usually written in Python
- Exposes functions like `llm_query(prompt, model)` for recursive calls
- Main model output is capped (e.g., 8,192 characters per `print` call)
- Heavy tool use (web search, file access) is delegated to sub-LLMs

This design means the **main model's context window stays bounded** regardless of input size.

### RLM + DSPy Breakthrough (April 2026)

Raymond Weitekamp ([@raw_works](https://twitter.com/raw_works)) demonstrated that DSPy.RLM enables small open models to achieve SOTA on LongCoT:

| Model + Setup | LongCoT-Mini | LongCoT-Full |
|---------------|-------------|--------------|
| Qwen3-8B (vanilla) | 0% | — |
| Qwen3-8B + dspy.RLM | 6.5% (#7 on leaderboard) | — |
| Qwen3.5-9B + dspy.RLM | 17.2% | 15.69% (SOTA) |
| Qwen3.5-27B + dspy.RLM | — | **22.18%** (new king) |
| GPT-5.2 | — | 9.83% |

> "Same model. Same weights. No fine-tuning. The scaffold is doing 100% of the lifting." — [@raw_works](https://twitter.com/raw_works/status/2045208764509470742)

**Key insight:** Small open models + RLM scaffold can more than double the performance of closed frontier models. Full benchmark (2500 questions) validates these results.

Sources:
- [RLMs are SOTA on LongCoT](https://raw.works/rlms-are-sota-on-longcot/) (Apr 2026)
- [RLMs are the New Reasoning Models](https://raw.works/rlms-are-the-new-reasoning-models/) (Apr 2026)

### Benchmark Performance

| Benchmark | GPT-5 Baseline | RLM (GPT-5-mini) | Improvement |
|-----------|----------------|-------------------|-------------|
| CodeQA | 24% | 62% | +38pp |
| OOLONG | collapses at 1M+ | maintains accuracy | catastrophic→stable |
| OOLONG Pairs | fails | succeeds | — |
| S-NIAH | — | strong | — |
| BrowseComp-Plus | — | improved | — |

### RLM-Qwen3-8B (First Post-Trained Native RLM)

- Outperforms underlying Qwen3-8B by **28.3%** on average
- Approaches vanilla GPT-5 quality on three long-context tasks
- Demonstrates that RLM-native training yields significant gains

### Scale & Cost

- Handles inputs up to **100x beyond model context windows** (tested at 10M+ token regime)
- **2-3x reduction** in main model token consumption
- Cost comparable to or cheaper than vanilla single-pass inference
- Sequential REPL operations add 40-80% latency vs single-pass

## Comparison with Other Long-Context Approaches

### RLM vs Context Folding (Sun et al., 2025)

| Aspect | RLM (Zhang et al.) | Context Folding (Sun et al.) |
|--------|---------------------|-------------------------------|
| Approach | Context → REPL variable | Context → summarized branches |
| Mechanism | Recursive sub-calls in code | Branch/return with folding |
| Training | Can be RL-trained end-to-end | FoldGRPO (token-level rewards) |
| Context Limit | Near-infinite (REPL-based) | 10x reduction (32K active) |
| Information Loss | None (exact access) | Summarization-based loss |
| BrowseComp-Plus | — | 62.0% (FoldGRPO) |
| SWE-Bench Verified | — | 58.0% (FoldGRPO) |

**Convergence:** Both treat context management as an **active, learnable behavior** rather than a passive data loading problem. Both can be trained with RL.

### RLM vs Traditional Scaffolds

| Scaffold | Context Handling | Info Loss | Trainability |
|----------|------------------|-----------|--------------|
| Direct prompt | All-at-once | None | N/A |
| Summarization | Compressed | High | Hard |
| Retrieval agents | Selected chunks | Medium | Medium |
| Code agents | Programmatic | Low | Medium |
| **RLM** | **REPL + recursion** | **None** | **High (end-to-end RL)** |

## The "Trainable Scaffold" Thesis

Prime Intellect (building on RLM) positions this as **"the paradigm of 2026"**:

> "Teaching models to manage their own context end-to-end through reinforcement learning will be the next major breakthrough, enabling agents to solve long-horizon tasks spanning weeks to months."

This connects directly to **Shunyu Yao's "The Second Half"** framework:
- Yao: "RL finally generalizes... evaluation becomes more important than training"
- Zhang: "RLMs trained explicitly to recursively reason are likely to represent the next milestone"

Both converge on: **the scaffold itself becomes the environment for RL training**.

## Lambda-RLM: Production Case Study (AEC Domain)

Theodoros Galanos ([the-harness-blog|The Harness Blog]) demonstrated a production-grade RLM variant called **Lambda-RLM** in the Architecture, Engineering, and Construction (AEC) domain. Unlike standard RLM which uses an open-ended REPL with dynamic decomposition, Lambda-RLM computes the task structure upfront as a deterministic pipeline:

1. **Plan** — Reads template, measures sources, computes dependency tree (0 LLM calls)
2. **Extract + Review** — Pulls data from bounded chunks in dependency order with contract alignment
3. **Generate** — Composes sections from extractions and dependencies

### Key Metrics (Open REPL vs Lambda-RLM)

| Metric | Open REPL | Lambda-RLM | Improvement |
|--------|-----------|------------|-------------|
| Total Tokens | 740K | 53K | **14x less** |
| Input Tokens | 732K | 33K | **22x less** |
| API Calls | 48 | 27 | **1.8x fewer** |
| Quality (Reward) | 0.67 | 0.73 | **+8.4%** |

Core insight: When task structure is deterministic and bounded, giving the model freedom to decide decomposition strategy wastes tokens on control code rather than engineering reasoning. See [[concepts/lambda-rlm]] for full details.

Source: ["Recursive by Design"](https://theharness.blog/blog/recursive-by-design/) (The Harness Blog, April 2026)

### λ-RLM: Typed Functional Runtime (Huawei)

**λ-RLM** (Amartya Roy et al., Huawei Noah's Ark Lab, arXiv:2603.20105, March 2026) replaces the open-ended REPL control flow with a **typed functional runtime grounded in λ-calculus**. Unlike standard RLM (LLM writes Python control code) and Lambda-RLM (template-driven pipeline), λ-RLM uses a fixed-point combinator over a library of pre-verified operators (SPLIT, MAP, FILTER, REDUCE, CROSS).

| Aspect | λ-RLM | Lambda-RLM |
|--------|-------|------------|
| **Control model** | Y-combinator fixed-point over combinators | Deterministic pipeline (Plan → Extract → Generate) |
| **Formal proofs** | Termination, cost bounds, optimal partition | None |
| **Optimal split** | k*=2 (binary splitting, proven) | Template-driven |
| **Empirical scope** | 9 models, 4 benchmarks | Single domain (AEC), single model |
| **Key metric** | +21.9pp accuracy, 4.1× faster | 14× token reduction, +8.4% quality |

These two variants independently arrived at the same critique (open-ended REPL is wasteful) from opposite directions — λ-RLM from formal theory, Lambda-RLM from production practice. See [[concepts/typed-rlm]] for full analysis and [[concepts/typed-rlm#Comparison with Lambda-RLM (Galanos)|detailed comparison]].

Source: [arXiv:2603.20105](https://arxiv.org/abs/2603.20105) (Huawei Noah's Ark Lab, March 2026, arXiv-only)

## Adoption & Ecosystem

- **Prime Intellect:** Implemented RLMEnv in their verifiers stack; ablation with GPT-5-mini and INTELLECT-3-MoE
- **DSPy:** Omar Khattab (co-author) plans an `RLM` module that could subsume CoT/ReAct
- **Open Source:** Full codebase released, 20+ contributors, v0.1.1a release (Feb 2026)
- **Sandbox Support:** Modal, Daytona, Prime Sandboxes, local Python REPL

## Limitations & Open Problems

1. **Sequential execution:** RLM calls are synchronous; no parallel sub-call execution
2. **Recursion depth:** Currently limited; not truly unbounded in practice
3. **Cost distribution:** Heavy tails due to very long trajectories
4. **Model underutilization:** Current models not trained for RLM scaffolding show "significant performance being left untapped"
5. **Mathematical reasoning:** RLMs struggle on math-heavy tasks without specialized training
6. **Latency:** 40-80% overhead from REPL operations vs single-pass

## Future Directions

- **RL-native training:** Cascade SFT+RL recipe for RLM trajectories
- **Parallel sub-calls:** Fan-out many sub-LLM queries simultaneously
- **Custom data types:** Beyond strings, support structured context (graphs, databases)
- **Long-horizon agents:** Tasks spanning weeks to months with persistent state
- **Hybrid folding + RLM:** Combine context folding's efficiency with RLM's precision

## Quotes

> "RLMs offload the context as a variable in a REPL environment that the LM can interact with and launch sub-LM calls inside of."
> — Alex Zhang, RLM blog post (Oct 2025)

> "We think that RLMs trained explicitly to recursively reason are likely to represent the next milestone in general-purpose LLM inference."
> — Alex Zhang, RLM blog post (Oct 2025)

> "Current models show significant performance being left untapped due to poor usage of the scaffolding. This suggests major gains from RLM-native training."
> — Prime Intellect, "Recursive Language Models: the paradigm of 2026"

> "RLMs reframe long context as an environment variable."
> — MarkTechPost technical summary

## DSPy.RLM API Reference

DSPy v3.1.3+ ships built-in `dspy.RLM` module. The API provides a high-level interface for RLM execution:

### Constructor Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `signature` | `str \| Signature` | required | Input/output definition (e.g., `"context, query -> answer"`) |
| `max_iterations` | `int` | 20 | Maximum REPL interaction loops |
| `max_llm_calls` | `int` | 50 | Maximum `llm_query` calls per execution |
| `max_output_chars` | `int` | 10,000 | Maximum characters from REPL output |
| `verbose` | `bool` | `False` | Enable detailed logging |
| `tools` | `list[Callable]` | `None` | Additional tools callable from interpreter |
| `sub_lm` | `dspy.LM` | `None` | Sub-LM for queries (defaults to `dspy.settings.lm`). Use cheaper model. |
| `interpreter` | `CodeInterpreter` | `None` | Custom interpreter (default: Deno/Pyodide WASM) |

### Built-in Tools

| Tool | Description |
|------|-------------|
| `llm_query(prompt)` | Query sub-LM for semantic analysis (~500K char capacity) |
| `llm_query_batched(prompts)` | Batch multiple prompts concurrently |
| `print()` | Print output (required to see results) |
| `SUBMIT(...)` | Submit final output and end execution |
| Standard library | `re, json, collections, math`, etc. |

### Basic Usage Example

```python
import dspy

dspy.configure(lm=dspy.LM("openai/gpt-5"))
rlm = dspy.RLM("context, query -> answer")

result = rlm(
    context="...very long document...",
    query="What is the total revenue mentioned?"
)
print(result.answer)
```

### Deno Requirement

RLM uses Deno + Pyodide for WASM sandbox. Install:
```bash
curl -fsSL https://deno.land/install.sh | sh
```

### Output Structure

Returns `Prediction` with:
- Output fields from signature (e.g., `result.answer`)
- `trajectory`: List of dicts with `reasoning`, `code`, `output` per step
- `final_reasoning`: LLM reasoning on final step

## Relation to Programmatic Tool Calling (PTC): 2-Axis Complementarity

RLM and [[concepts/programmatic-tool-calling|Programmatic Tool Calling (PTC)]] are **complementary paradigms** that apply the same solution (code execution) to fundamentally different problems:

| Dimension | RLM (Data Axis) | PTC (Function Axis) |
|-----------|-----------------|---------------------|
| **Core concern** | **What to analyze** — context management | **How to execute** — tool orchestration |
| **Direction** | **Split** — decompose 1 huge context → N pieces | **Merge** — bundle N tool calls → 1 code block |
| **Replaces** | RAG / long-context prompting | Sequential `tool_use` blocks |
| **Code writes** | `context[start:end]`, `re.findall()`, `llm_query()` | `await tool_a()`, `asyncio.gather()` |
| **Freedom** | Dynamic decomposition strategy (4-level spectrum) | Dynamic execution flow (conditionals, parallelism) |
| **Metaphor** | Soft MapReduce: MAP → SHUFFLE(llm_query) → REDUCE(SUBMIT) | Orchestration: async function composition |

### Decomposition Strategy: The LLM Decides

A key insight from the RLM paper (§5): *"Unlike prior agentic methods that rigidly define these workflow patterns, RLMs defer these decisions entirely to the language model."*

The LLM dynamically chooses its decomposition strategy from a spectrum:

1. **Manual** — raw Python: `re.findall()`, slicing
2. **Semi-manual** — helper functions defined in code
3. **Tool-delegated** — PTC tools like `chunk_by_topic(context)`
4. **Recursive** — `llm_query()` for semantic decomposition

This flexibility is the core advantage over RAG (fixed chunk size + fixed top-k).

### Architectural Fusibility

A **Tool-Augmented RLM** (案A: PTC in RLM) can naturally host both axes in the same environment:

```python
relevant = [s for s in context if "revenue" in s.lower()]  # RLM: explore
financials = await query_api({"ids": extract_ids(relevant)})  # PTC: execute
analysis = llm_query(f"Compare: {relevant} vs {financials}")  # RLM: analyze
```

Full analysis in [[concepts/dspy-rlm#RLM × Programmatic Tool Calling: 補完する2軸（関数軸 vs データ軸）]].

## Related Concepts

- **[[concepts/dspy]]** — Declarative LM programming framework; ships RLM module
- **[[concepts/dspy-rlm]]** — DSPy.RLM implementation with full analysis of PTC relationship, 2-axis framing (function vs data), merge/split symmetry, and Tool-Augmented RLM design
- **[[concepts/programmatic-tool-calling]]** — Complementary paradigm: LLM writes code that calls tools (function axis). PTC merges N tool calls into 1 code block; RLM splits 1 huge context into N pieces. Mirror symmetry.
- **[[concepts/code-execution-with-mcp]]** — Middle architectural layer between PTC and CodeMode: MCP as code API with progressive disclosure
- **[[concepts/code-mode]]** — Specific implementations (Cloudflare V8, Pydantic Monty) of the code-execution-over-tool-calling pattern
- **[[concepts/context-folding]]** — Parallel approach: branch/return with summarization
- **[[concepts/inference-time-scaling]]** — RLM scales computation, not parameters
- **[[concepts/typed-rlm]]** — Typed functional runtime variant (Huawei); formal proofs for termination, cost bounds, optimal partition
- **[[shunyu-yao]]** — "The Second Half" framework; RL generalization thesis
- **[[alex-zhang]]** — Primary author, RLM creator
- **[[omar-khattab]]** — Co-author, DSPy creator, ColBERT lineage
