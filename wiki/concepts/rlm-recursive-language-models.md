---
title: "RLM (Recursive Language Models)"
created: 2026-04-13
updated: 2026-06-04
type: concept
tags: [rlm, long-context, inference, test-time-scaling, context-rot, context-degradation, ai-agents, coding-agents, orchestration, subagents, workflow, claude-code, research, neurosymbolic]
related: [dspy, dspy-rlm, context-engineering, gepa, lambda-rlm, programmatic-tool-calling, code-execution-with-mcp, code-mode, context-folding, anthropic-multi-agent-research, inference-time-scaling, typed-rlm, dynamic-workflows]
sources:
  - https://arxiv.org/abs/2512.24601
  - https://alexzhang13.github.io/blog/2025/rlm/
  - https://dspy.ai/api/modules/RLM/
  - https://github.com/alexzhang13/rlm
  - raw/articles/2026-05-28_a1zhang_rlm-clarification-what-rlm-is-not.md
  - raw/articles/2026-06-04_softwaredoug_search-with-agents-lesson6-rlms.md
---

# RLM (Recursive Language Models)

## Overview

Recursive Language Models (RLMs) are a task-agnostic inference paradigm proposed by **Alex Zhang, Tim Kraska, and Omar Khattab** (MIT CSAIL/OASYS Lab) that allows language models to handle **near-infinite length contexts** by programmatically examining, decomposing, and recursively calling themselves over input snippets.

- **Paper:** arXiv:2512.24601 (Dec 2025, revised Jan 2026, **v3 May 2026**)
- **Blog:** [alexzhang13.github.io/blog/2025/rlm](https://alexzhang13.github.io/blog/2025/rlm/)
- **Code:** [github.com/alexzhang13/rlm](https://github.com/alexzhang13/rlm) (3,296 stars)
- **Minimal:** [github.com/alexzhang13/rlm-minimal](https://github.com/alexzhang13/rlm-minimal) (749 stars)
- **Docs:** [alexzhang13.github.io/rlm](https://alexzhang13.github.io/rlm/)
- **PyPI:** `rlms` — 6,034 downloads/month

## What RLM Is and Is Not (Author Clarifications)

In response to community criticism, Alex Zhang published a detailed clarification on May 28, 2026 that explicitly defines RLM's scope by what it does **not** claim, and what makes it genuinely novel.

### Five Things RLM Does NOT Claim

1. It does **not** claim to be the first to explore an LM talking to an LM
2. It does **not** claim to be the first to explore sub-agents
3. It does **not** claim to be the first to argue for CodeAct-style execution
4. It does **not** claim to be the first to propose recursion with respect to an LM
5. It does **not** claim to be the first to propose any of the independent features that make an RLM (context offloading, PTC, etc.)

Each of these ideas has precedent in prior work. RLM's contribution is not in inventing any single building block.

### The Real Novelty: Composition + Sufficiency

> "All of the ideas that make up an RLM are somewhat intuitive and implemented in various ways, many with little success. **The composition of them, and the lack of a need for any more, is what makes it unique.**" — Alex Zhang

The insight has two sides:
- **Composition**: Which specific building blocks are assembled together (REPL-as-context-variable + recursive sub-calls + CodeAct-style execution + programmatic sub-agent invocation)
- **Sufficiency**: The argument that this specific set of components is *enough* — no additional mechanisms are needed for robust long-context reasoning

This is why RLM resists being reduced to "just X + Y" — every individual component has been tried before, but the *particular* composition and the *completeness* argument are novel.

### RLM as a Normative Argument for Abstractions

Beyond the technical contribution, Zhang reframes RLM as a **prescriptive argument**:

> "The paper is an argument for exactly the type of abstractions one should define to better enable a sub-agent calling system (i.e. context offloading, CodeAct-style execution, programmatically sub-agent calling)."

RLM is not merely describing a technique — it is arguing for **what abstractions matter** in agent design. The paper proposes that the line between a sub-agent calling system and a "language model" is blurry, and that a **well-designed, general enough abstraction yields a meaningful "language model."** When the scaffold abstraction is sufficiently principled, the distinction between "model capability" and "system capability" dissolves.

### Why This Matters for Claude Code

Zhang notes that Claude Code's recent releases have moved away from standard ReAct-style loops with JSON tool-calling toward RLM-like abstractions. The Dynamic Workflows launch (May 2026) is significant not because Anthropic "adopted RLM," but because **frontier engineering converged on the same abstractions that RLM formalized** — an independent validation of the thesis that these specific components, composed together, form a sufficient foundation for agent reasoning at scale.

Source: [[raw/articles/2026-05-28_a1zhang_rlm-clarification-what-rlm-is-not|a1zhang RLM Clarification Tweet (May 28, 2026)]]

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

### MGH Validation: Zhang's Direct LongCoT RLM Experiment (April 2026)

**Alex Zhang** directly tested the Mismanaged Geniuses Hypothesis on LongCoT by using **Claude Code** to analyze RLM failure trajectories and generate corrective "tips." Unlike Weitekamp's approach (open models + dspy.RLM), Zhang used **GPT-5.2 + RLM + targeted prompting fixes**:

| Method | Total Score | MATH | CHEM | CS | LOGIC | CHESS |
|--------|-------------|------|------|----|-------|-------|
| GPT-5.2 (Base) | 38.7% | 26.0% | 37.0% | 40.4% | 53.6% | 36.6% |
| RLM (GPT-5.2) - Initial | 50.6% | 5.6% | 50.0% | 11.0% | 86.7% | 93.0% |
| **RLM (GPT-5.2) + Tips** | **65.6%** | Significant Incr. | — | — | — | — |
| Partial Rewards | >70% | — | — | — | — | — |

**Identified failure modes via trajectory analysis:**
1. **Brute-force timeouts** — Models tried to solve MATH/CS nodes via brute force, crashing the REPL
2. **Lack of verification** — Sub-agents launched but outputs never validated
3. **Prompting gaps** — Models not instructed on how to handle graph-structured dependencies

**Key insight:** The same tips given to a non-RLM (standard) LM resulted in *worse* performance — proving the RLM's recursive decomposition mechanism is essential for tracking graph-structured reasoning.

Source: [[raw/articles/2026-04-26_alex-zhang-longcot-rlm-mgh.md]] | [alexzhang13.github.io/blog/2026/longcot-rlm/](https://alexzhang13.github.io/blog/2026/longcot-rlm/)

### Benchmark Performance (v3, Table 1)

#### GPT-5 Results

| Method | CodeQA | BrowseComp+ (1K) | OOLONG | OOLONG-Pairs |
|--------|--------|-------------------|--------|--------------|
| Base Model | 24.0* | 0.0* | 44.0 | 0.1 |
| CodeAct (+ BM25) | 22.0* | 51.0 | 38.0 | 24.7 |
| CodeAct (+ sub-calls) | 24.0* | 0.0* | 40.0 | 28.4 |
| Compaction agent | 58.0 | 70.5 | 46.0 | 0.1 |
| OpenCode | 18.0* | 0.0* | 32.0 | 3.1 |
| OpenCode (+ context offloading) | 64.0 | 94.0 | 52.0 | 4.8 |
| Claude Code (Opus 4.1) | 12.0* | 0.0* | 40.2 | 0.1 |
| Claude Code (+ context offloading) | 62.0 | 84.0 | 48.0 | 6.5 |
| RLM (depth=0) | 58.0 | 88.0 | 36.0 | 43.9 |
| RLM (depth=1) | 62.0 | 91.3 | 56.0 | 58.0 |
| **RLM (depth=2)** | **66.0** | **92.0** | **56.5** | **65.5** |
| **RLM (depth=3)** | 58.0 | **92.0** | **58.0** | **76.0** |

**Key insight:** On OOLONG-Pairs (the hardest, quadratic-complexity task), RLM(depth=3) achieves **76.0%** vs depth=1's 58.0% — demonstrating that deeper recursion dramatically improves performance on information-dense tasks. Higher-depth RLMs outperform all methods including Claude Code and OpenCode by a large margin.

#### Qwen3-Coder-480B-A35B Results

| Method | CodeQA | BrowseComp+ | OOLONG | OOLONG-Pairs |
|--------|--------|-------------|--------|--------------|
| Base Model | 20.0* | 0.0* | 36.0 | 0.1 |
| OpenCode (+ offloading) | 40.0 | 58.0 | 24.0 | 2.1 |
| RLM (depth=0) | 66.0 | 46.0 | 43.5 | 17.3 |
| RLM (depth=1) | 56.0 | 44.7 | 48.0 | 23.1 |
| RLM (depth=2) | 54.0 | 68.0 | 26.0 | 19.0 |
| RLM (depth=3) | 44.0 | 68.7 | 32.0 | 21.1 |

*Note: On CodeQA, RLM(depth=0) — REPL-only without sub-calls — outperforms ALL sub-calling variants for Qwen3-Coder, showing that offloading context as a variable alone provides strong benefits. On information-dense tasks, depth helps (BrowseComp+: 46.0→68.7 from depth 0→3).*

### RLM-Qwen3-8B (First Post-Trained Native RLM)

- Outperforms underlying Qwen3-8B by **28%** on average
- Approaches vanilla GPT-5 quality on three long-context tasks
- **Training method:** Rejection fine-tuning on 1,000 filtered RLM(Qwen3-Coder-480B-A35B) trajectories from LongBenchPro
- **Efficiency:** 3× faster and cheaper than base model as RLM — better decision making, fewer syntax errors
- Demonstrates that RLM-native training yields significant cross-domain gains

### Scale & Cost

- Handles inputs up to **100x beyond model context windows** (tested at 10M+ token regime)
- **2-3x reduction** in main model token consumption
- Cost comparable to or cheaper than vanilla single-pass inference
- Sequential REPL operations add 40-80% latency vs single-pass

## V3 New Findings (May 2026)

### Recursion Depth Scaling

v3 introduces **depth>1 experiments** where RLMs have access to recursive RLM calls (not just LLM sub-calls):

| Depth | Behavior | Best For |
|-------|----------|----------|
| 0 | REPL-only, no sub-calls | Code-heavy tasks where context offloading suffices |
| 1 | Sub-calling LLMs (original RLM) | Balanced tasks with moderate information density |
| 2 | Sub-calling RLMs (recursive RLM calls) | Information-dense tasks requiring multi-level decomposition |
| 3 | Deeper recursion | Quadratic-complexity tasks (OOLONG-Pairs) |

**Key findings:**
- **OOLONG-Pairs (quadratic complexity):** GPT-5 depth=3 hits **76.0%** vs depth=1's 58.0% — a 31% relative improvement
- **BrowseComp+:** depth=3 achieves 92.0% for GPT-5, 68.7% for Qwen3-Coder
- On CodeQA with Qwen3-Coder, depth=0 (no sub-calls) outperforms all sub-calling variants — context offloading alone provides strong benefits
- Open source `rlm` repo supports `max_depth` parameter

### OpenCode & Claude Code Comparisons

v3 adds coding agent baselines per popular request:

| Agent | Model | Context Strategy | OOLONG-Pairs (GPT-5) |
|-------|-------|------------------|----------------------|
| OpenCode | GPT-5 | Standard | 3.1% |
| OpenCode | GPT-5 | Context offloading to file | 4.8% |
| Claude Code | Claude Opus 4.1 | Standard | 0.1% |
| Claude Code | Claude Opus 4.1 | Context offloading to file | 6.5% |
| **RLM (depth=3)** | GPT-5 | REPL + recursive sub-calls | **76.0%** |

**Key finding:** Context offloading (writing to file) dramatically improves coding agents (OpenCode: 3.1%→4.8%, Claude Code: 0.1%→6.5%) but still lags far behind RLMs on information-dense tasks. RLMs outperform all coding agents by a large margin on OOLONG-Pairs.

### MRCRv2 Length Generalization

A new training experiment demonstrating **length generalization**:

- **Setup:** Qwen3-4B-Instruct-0527 trained as RLM(depth=1) on MRCRv2 via RLVR (reinforcement learning with verifiable rewards)
- **Training split:** 32K-64K tokens, 2-needle configuration (150 steps, batch 128, 4 rollouts/example)
- **Test split:** 1M tokens, 8-needle configuration
- **Result:** RLM generalizes to the longer, more difficult split — approaches Gemini 3.1 Pro (native 1M context frontier model)
- **Implication:** RLM-native RL training produces **context-length generalization** — models learn the scaffolding, not just the context

### Error Analysis (§5, expanded)

v3 significantly expands trajectory analysis:

**First Decomposition & Errors:**
- RLMs defer unbounded-length reasoning chains to sub-LM calls
- First decomposition attempt is critical — while RLMs frequently recover from incorrect initial decomposition, it significantly impacts overall performance
- In-context RLM trajectory examples in system prompt improve **both** overall performance and initial decomposition quality

**Syntax Errors (Figure 4b):**
- Percentage of trajectories with ≥1 syntax error, bucketed by correct/incorrect rollouts
- RLM-native training (post-training) significantly reduces syntax errors — RLM-Qwen3-8B has 3× fewer mistakes

**Prompting Case Study (Figure 4a):**
- On OOLONG, ablation of in-context decomposition examples in system prompt
- In-context examples improve performance even if unrelated to actual task
- First decomposition attempt categorized per rollout

**General Observations:**
- Models probe context → decompose into sub-tasks → recursive sub-calls
- On BrowseComp-Plus: LM uses model priors to programmatically narrow search space
- On OOLONG-Pairs: output beyond context window by stitching sub-LM calls in REPL

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
2. **Recursion depth:** Explored up to depth=3 in v3; diminishing returns observed for some model/task combinations (e.g., Qwen3-Coder on CodeQA)
3. **Cost distribution:** Heavy tails due to very long trajectories; median RLM run cheaper than base model but mean higher
4. **Model underutilization:** Current models not trained for RLM scaffolding shows "significant performance being left untapped" — v3 shows training partly addresses this
5. **Mathematical reasoning:** RLMs struggle on math-heavy tasks without specialized training (LongCoT-mini MATH subscore dropped from 26.0 to 5.6 without decomposition hints)
6. **Latency:** 40-80% overhead from REPL operations vs single-pass; v3 shows 3× speed improvement after training
7. **Syntax errors:** v3 quantifies this — percentage of trajectories with ≥1 syntax error; training significantly reduces this
8. **State integrity:** Agents can mutate or delete REPL variables (including tool functions themselves). Practitioners must decide: reset state per tool call (Turnbull's compromise), use immutable tool wrappers, or accept the risk. See [[concepts/agent-driven-ranker-optimization]] for the guardrail-based approach.

## Practitioner Design Decisions (Search Domain)

Doug Turnbull's "Search with Agents" Lesson 6 (June 2026) demonstrates RLM applied to patent expert finding, surfacing several design decisions that the formal paper does not address:

### Stateful Variables as Agent Memory

The REPL is initialized with domain-specific state:

```python
repl_box.start(
    historical_results=[],          # Mutable list — agent's search log
    patent_search=patent_search,    # Immutable tool — external API wrapper
    llm_query=llm_query             # Recursive LLM call — the key addition
)
```

`historical_results` acts as **persistent, inspectable agent memory** — the agent reads it to avoid duplicate queries, appends findings, and can even ask `llm_query()` to summarize what's been found so far. Unlike context window memory, REPL variables survive across tool calls without context rot.

### Generic vs Task-Specific LLM Tools

A key design tension: expose a generic `llm_query(prompt)` or wrap it in domain-specific tools?

| Approach | Example | Pro | Con |
|----------|---------|-----|-----|
| Generic `llm_query` | `llm_query("Is expert X relevant?")` | Maximum flexibility | Unpredictable usage, prompt injection risk |
| Task-specific `judge` | `judge(expert_info, topic)` | Constrained, testable | Less exploratory, harder to iterate |

Turnbull's demo uses generic `llm_query` with **usage examples in the system prompt** to guide behavior — a middle ground between freedom and control.

### State Integrity Problem

When `patent_search` enforces deduplication (raises error on duplicate queries), the agent could theoretically **redefine the function in the REPL** to bypass the check. Turnbull proposes forcing `repl.set(agent_state)` before each tool call — resetting protected state — as a pragmatic compromise. This is a form of **REPL-level security** that the formal RLM paper does not discuss.

### Validation for REPL Outputs

REPL state can become corrupted: the agent might delete entries from `historical_results` or hallucinate expert names. Turnbull's harness adds `validators=[eval_results, check_results, ...]` — a post-hoc check that can force the agent to restore state or discard the run entirely. This connects directly to the [[concepts/agent-steering|agent steering]] pattern of carrot-and-stick validation.

### `harness()` as the Orchestration Primitive

Turnbull's implementation uses a `harness()` function (likely from a custom framework) rather than the RLM paper's `rlm.completion()`. The harness provides:
- `tools=[repl_tool]` — tool registration
- `stoppers=[stop_after_N_calls]` — recursion depth control
- `validators=[...]` — post-execution checks
- `summary=True` — automatic context summarization
- `text_format=str` — output formatting

This suggests that practical RLM implementations often sit **inside a broader agent harness** rather than being the top-level abstraction — the RLM is the reasoning engine, the harness is the execution environment.

Source: [[raw/articles/2026-06-04_softwaredoug_search-with-agents-lesson6-rlms|Search with Agents Lesson 6 slides]]

## Future Directions

- **RL-native training:** Cascade SFT+RL recipe for RLM trajectories
- **Parallel sub-calls:** Fan-out many sub-LLM queries simultaneously
- **Custom data types:** Beyond strings, support structured context (graphs, databases)
- **Long-horizon agents:** Tasks spanning weeks to months with persistent state
- **Hybrid folding + RLM:** Combine context folding's efficiency with RLM's precision
- **Indexing & Content Understanding:** Applying RLM to the ingestion side — adaptive chunking, context-aware enrichment with index-relative judgment, cross-document reasoning, progressive schema discovery. See [[concepts/rlm-for-indexing]] for the full design space analysis.

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

A **Tool-Augmented RLM** (Option A: PTC in RLM) can naturally host both axes in the same environment:

```python
relevant = [s for s in context if "revenue" in s.lower()]  # RLM: explore
financials = await query_api({"ids": extract_ids(relevant)})  # PTC: execute
analysis = llm_query(f"Compare: {relevant} vs {financials}")  # RLM: analyze
```

Full analysis in [[concepts/dspy-rlm#RLM × Programmatic Tool Calling: Complementary 2 Axes (Function Axis vs Data Axis)]].

### From 2-Axis to 3-Axis: Programmatic Sub-Agent Calling (PSAC)

Dynamic Workflows introduce a **third axis** that completes the structural triad:

| Axis | Paradigm | Core Operation | Direction | Concrete Form |
|---|---|---|---|---|
| **Data Axis** | RLM | Split 1 huge context → N pieces | **Disaggregate** (read) | `context[start:end]`, `llm_query(subset)` |
| **Function Axis** | PTC | Merge N tool calls → 1 code block | **Aggregate** (write) | `await tool_a()`, `asyncio.gather()` |
| **Agent Axis** | PSAC (DW) | Spawn 1 script → N sub-agents | **Delegate** (orchestrate) | `spawn_subagent(task)`, workflow script |

**Why this matters**: RLM solved "how does the model process huge context?" (data decomposition). PTC solved "how does the model use tools efficiently?" (function composition). PSAC solves "how does the model build its own execution infrastructure?" (agent orchestration). Together they form a complete framework for model-driven computation:

```
                  PTC (Aggregate)
                  N tools → 1 call
                       ↑
                       │  function axis
                       │
    RLM ←──────────────┼──────────────→ PSAC
    (Disaggregate)     │               (Delegate)
    1 context → N pieces│              1 script → N sub-agents
                       │
                  data axis          agent axis
```

**The key distinction from traditional multi-agent systems**: In LangGraph, CrewAI, or pre-DW Claude Code sub-agents, the human designs the topology — which agent does what, how they communicate, what the handoff protocol is. PSAC shifts this entirely to the model: the orchestration script IS the generated topology. The model "vibecodes" a custom sub-agent fleet harness for each specific task (as @nickadobos put it: "Claude vibecoding an entire brand new subagent fleet harness on demand").

**Structural comparison — Task Decomposition vs Context Decomposition vs Programmatic Sub-Agent Calling:**

| Dimension | Task Decomposition (Multi-Agent) | Context Decomposition (RLM) | Prog. Sub-Agent Calling (DW) |
|---|---|---|---|
| **What is decomposed** | Task → subtasks (explicit, human-designed) | Context → chunks (explicit) + Task → sub-queries (implicit/emergent) | Task → sub-agent assignments (explicit, model-designed) |
| **Who decides** | Human (workflow designer) | Model (in REPL code) | Model (in orchestration script) |
| **Topology** | Fixed / pre-defined graph | Dynamic, model-chosen | Dynamic, script-generated |
| **Invocation** | Pre-built pipeline | `llm_query()` from code | `spawn_subagent()` from script |
| **State location** | Orchestrator's context window | REPL environment variables | Script variables (outside model context) |
| **Output coupling** | Accumulates in orchestrator context | Returned to REPL, then model reads | Results in script, final summary only to model |
| **Context isolation** | Partial (context rot risk) | Full (sub-calls isolated) | Full (sub-agents isolated) |
| **Verification** | External / human review | Implicit in recursive loop | Explicit adversarial agents |
| **Scaling axis** | Agent count (horizontal) | Recursion depth (vertical) | Agent count × recursion depth (matrix) |
| **Failure mode** | Context bloat, coordination overhead | Counting errors at high depth | Independent error surfaces per agent |

**RLM's dual decomposition**: The RLM authors frame their contribution as context-centric ("the choice of decomposition should purely be the choice of an LM"), but in practice, context decomposition **is** task decomposition by another name. When the model writes `llm_query(subset_a)` vs `llm_query(subset_b)`, it's implicitly deciding that subset A needs different analysis than subset B — i.e., assigning different sub-tasks to different recursive calls. The decomposition of context and the decomposition of task are two sides of the same coin; RLM makes task decomposition an emergent property of context manipulation rather than an explicit design step. This contrasts with both traditional multi-agent systems (task decomposition is explicit but human-designed) and Dynamic Workflows (task decomposition is explicit and model-designed).

**Nickadobos framing as "new scaling law dimension"**: The 3-axis model implies a multiplicative scaling relationship:

```
Effective Capability ∝ Base Model × Thinking Time × Generated Harness Compute
```

This explains why the Bun migration (750K LOC, 11 days, 99.8% tests pass) was possible — not because one agent thought harder, but because the model **generated infrastructure** (the harness) that multiplied its effective capability by coordinating hundreds of agents. Traditional single-agent scaling (model size × thinking time) could never reach this result; the generated harness compute is a genuinely new multiplicative factor.

## Dynamic Workflows: RLM in Production

On May 28, 2026, Anthropic launched **[[concepts/dynamic-workflows]]** in Claude Code — a feature that lets Claude write JavaScript orchestration scripts to spawn tens to hundreds of parallel subagents with verification and convergence loops. Alex Zhang (@a1zhang) immediately identified this as "perhaps the first instance of a frontier model seriously trained to be an RLM."

### The a1zhang Claim: Opus 4.8 + Dynamic Workflows ≈ Trained RLM

Zhang's argument: Dynamic Workflows implement the core RLM properties — **programmatic sub-agent invocation with outputs outside the main model's context**. He clarified that the Python REPL is "a particular instantiation" but not essential; the defining RLM trait is a **symbolic environment where LLM calls are invoked in code, passing around outputs not in the context of the main model**. By this definition, Claude Code's workflow scripts (JavaScript orchestration with isolated subagent contexts) qualify as an RLM instantiation.

### Assessment: Scaffold-Level RLM, Not Trained RLM

The claim has **substantial validity** but requires nuance:

| Aspect | Alignment | Divergence |
|---|---|---|
| **Programmatic sub-agent invocation** | ✅ Workflow scripts invoke sub-agents from code, not prompt chains | — |
| **Context isolation** | ✅ Intermediate results stay in script variables, outside Claude's context | RLM uses REPL-as-context-variable; DW uses JavaScript variables + subagent contexts |
| **Model-determined decomposition** | ✅ Model decides task breakdown dynamically | DW decomposition is **task-centric**; canonical RLM is **context-centric** (programmatic context partitioning) |
| **Recursive refinement** | ✅ Convergence loop provides iterative improvement | RLM uses `llm_query()` recursion over context subsets; DW uses verification + adversarial agents |
| **Training** | ❌ Anthropic announcement mentions no model-level training changes | RLM paper includes post-trained RLM-Qwen3-8B; canonical RLM envisions "models explicitly trained to reason as RLMs" |

**Synthesis**: Dynamic Workflows are **scaffold-level RLM** rather than **trained RLM**. They implement the architectural pattern (model-driven decomposition, programmatic sub-agent invocation, context-isolated execution) at the orchestration layer, without evidence of model training specifically for recursive context decomposition. Zhang's own RLM vision calls for models "explicitly trained to reason as RLMs" — Dynamic Workflows achieve the scaffold, not the training.

The significance is real: this is the first production-grade coding agent system where the model dynamically decides its own decomposition strategy and invokes sub-agents programmatically. Whether this is "RLM" or "RLM-adjacent" depends on whether one defines RLM by architecture (scaffold pattern) or genesis (training).

### Community Debate

The a1zhang thread generated significant discussion:

- **Counterarguments**: "Parallelizing work and RLMs are different" — RLM's defining feature is context-centric decomposition, not just parallelism. "They don't dynamically query the prompt — it's prompt → script → call subagents on each prompt."
- **Support**: "The unlock is the model deciding when verification is actually done. That's what makes this RLM and not just parallel CoT."
- **Key insight from a1zhang**: "Invoking sub-agents programmatically... has been the key missing feature in coding agents for a while, and is what RLMs have been arguing we need for a long time. Essentially now, CC can function as an RLM."

### Claude Code's Architectural Evolution Toward RLM

Zhang contextualizes Dynamic Workflows within a broader trend:

> "The last few releases in Claude Code have moved away from standard ReAct-style loops with JSON tool-calling to more of this abstraction."

This matters because it frames DW not as a one-off feature but as the **culmination of a directional shift** in Claude Code's architecture: from turn-by-turn ReAct (human-in-the-loop JSON tool calls) → model-determined orchestration (CodeAct-style execution with programmatic sub-agent invocation). Each release has incrementally moved Claude Code closer to the RLM abstraction — DW is the point where the convergence became undeniable.

This is also why Zhang calls DW "RLM-like" rather than "RLM": the abstraction is converging, but the full RLM vision includes **training-level changes** (models explicitly taught to reason recursively) that scaffolding alone doesn't achieve. The convergence at the architectural level is significant validation; convergence at the training level remains to be seen.

### Author Clarifications on Scope

See [[#what-rlm-is-and-is-not-author-clarifications|What RLM Is and Is Not]] for Zhang's explicit May 2026 clarification of what RLM does and does not claim — including the argument that RLM's novelty lies in **composition + sufficiency**, not in any individual component.

See also: [[concepts/dynamic-workflows#Relationship to Recursive Language Models (RLM)]]

## Related Concepts

- **[[concepts/dspy]]** — Declarative LM programming framework; ships RLM module
- **[[concepts/harness-engineering]]** — Evaluation and constraint systems around LLMs; RLM's recursive decomposition pattern aligns with harness engineering's "build-verify loop" philosophy
- **[[concepts/dspy-rlm]]** — DSPy.RLM implementation with full analysis of PTC relationship, 2-axis framing (function vs data), merge/split symmetry, and Tool-Augmented RLM design
- **[[concepts/tool-use-examples]]** — Semantic Conventions Beyond Schema. RLM's first iteration data sampling is the runtime analogue: observe examples before acting, build internal "semantic layer" from data itself.
- **[[concepts/programmatic-tool-calling]]** — Complementary paradigm: LLM writes code that calls tools (function axis). PTC merges N tool calls into 1 code block; RLM splits 1 huge context into N pieces. Mirror symmetry.
- **[[concepts/code-execution-with-mcp]]** — Middle architectural layer between PTC and CodeMode: MCP as code API with progressive disclosure
- **[[concepts/code-mode]]** — Specific implementations (Cloudflare V8, Pydantic Monty) of the code-execution-over-tool-calling pattern
- **[[concepts/context-folding]]** — Parallel approach: branch/return with summarization
- **[[concepts/anthropic-multi-agent-research]]** — Structural similarity: breaking context constraints through horizontal task space decomposition (MapReduce pattern). While RLM uses depth-based input splitting, multi-agent uses parallel task splitting. Both share the same divide-and-conquer approach.
- **[[concepts/inference-time-scaling]]** — RLM scales computation, not parameters
- **[[concepts/agent-vs-pipeline-architecture]]** — RLM dissolves the pipeline/agent binary: recursive context management lets small models match frontier performance, challenging the assumption that agents require large context windows
- **[[concepts/typed-rlm]]** — Typed functional runtime variant (Huawei); formal proofs for termination, cost bounds, optimal partition
- **[[entities/shunyu-yao]]** — "The Second Half" framework; RL generalization thesis
- **[[entities/alex-zhang]]** — Primary author, RLM creator
- **[[entities/omar-khattab]]** — Co-author, DSPy creator, ColBERT lineage
