---
title: "RLM (Recursive Language Models)"
tags: [training, concept, ai-agents, llm, prompting, rag, evaluations, inference]
created: 2026-04-13
updated: 2026-04-24
type: concept
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

## Related Concepts

- **[[concepts/dspy]]** — Declarative LM programming framework; ships RLM module
- **[[concepts/dspyrlm]]** — This page covers the DSPy.RLM implementation
- **[[concepts/context-folding]]** — Parallel approach: branch/return with summarization
- **[[concepts/inference-time-scaling]]** — RLM scales computation, not parameters
- **** — RLM as a new ACI paradigm
- **** — RLMs are trainable scaffolds
- **[[shunyu-yao]]** — "The Second Half" framework; RL generalization thesis
- **[[alex-zhang]]** — Primary author, RLM creator
- **[[omar-khattab]]** — Co-author, DSPy creator, ColBERT lineage
- **** — Co-author, MIT DSG, ML systems expert
