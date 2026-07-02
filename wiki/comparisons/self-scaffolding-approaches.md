---
title: "Self-Scaffolding Approaches — RLM vs Dynamic Workflows vs Ornith"
type: comparison
created: 2026-07-02
updated: 2026-07-02
tags:
  - comparison
  - coding-agents
  - agentic-rl
  - orchestration
  - context-management
  - harness-engineering
  - inference
  - reasoning-model
sources:
  - concepts/rlm-recursive-language-models.md
  - concepts/dynamic-workflows.md
  - concepts/ornith-self-scaffolding-llm.md
  - raw/articles/simonwillison.net--2026-jun-29-ornith--e3eeed57.md
  - raw/articles/2026-05-28_a1zhang_rlm-clarification-what-rlm-is-not.md
  - raw/articles/2026-06-02_trq212_dynamic-workflows-claude-code.md
related:
  - "[[concepts/rlm-recursive-language-models]]"
  - "[[concepts/dynamic-workflows]]"
  - "[[concepts/ornith-self-scaffolding-llm]]"
  - "[[concepts/harness-engineering]]"
  - "[[concepts/inference-time-scaling]]"
  - "[[comparisons/agent-harnesses]]"
---

# Self-Scaffolding Approaches — RLM vs Dynamic Workflows vs Ornith

## Overview

Three converging approaches emerged in 2025–2026 around the idea that **LLMs should generate their own orchestration code** rather than rely on pre-built external frameworks. Each implements "self-scaffolding" at a different layer of the stack, with different training paradigms and primary use cases.

| | [[concepts/rlm-recursive-language-models\|RLM]] | [[concepts/dynamic-workflows\|Dynamic Workflows]] | [[concepts/ornith-self-scaffolding-llm\|Ornith Self-Scaffolding]] |
|---|---|---|---|
| **Origin** | MIT CSAIL (Zhang, Kraska, Khattab) — Dec 2025 | Anthropic (Shihipar, Bidasia) — June 2026 | DeepReinforce — June 2026 |
| **Implementation layer** | Inference paradigm (REPL) | Scaffold layer (JS scripts) | Model weights (Agentic RL) |
| **What gets generated** | Python code for context decomposition + `llm_query()` calls | JavaScript workflow files spawning subagents | Agent harness code (tool-use loops, error recovery) |
| **Primary axis** | Context decomposition | Task orchestration | Task-specific tool-use |
| **License** | MIT (code) | Proprietary (Claude Code) | MIT (model) |

## Core Mechanism Comparison

### RLM: Context as Variable

The LLM interacts with a Python REPL where context is stored as an external variable. The model writes code to examine, filter, chunk, and selectively expose parts of its input, then calls itself recursively on subsets via `llm_query()`.

```
# Canonical RLM pattern
context = load_all_documents()      # 100K+ tokens stored externally
chunks = split_by_section(context)  # Model writes this code
results = []
for chunk in chunks:
    result = llm_query("Summarize: " + chunk)  # Recursive call
    results.append(result)
final = llm_query("Synthesize: " + join(results))
```

**Key insight** (Khattab): *"Most people misunderstand RLMs to be about LLMs invoking themselves. The deeper insight is LLMs interacting with their own prompts as objects."*

### Dynamic Workflows: Model-Generated Orchestration

Claude writes a JavaScript workflow file that spawns parallel subagents, each with isolated context windows, model selection, and worktree isolation. Six composable patterns: Classify-and-Act, Fan-Out-and-Synthesize, Adversarial Verification, Generate-and-Filter, Tournament, Loop-Until-Done.

```javascript
// Canonical DW pattern (conceptual)
const tasks = classifyAndSplit(userGoal);
const results = await Promise.all(
  tasks.map(t => spawnAgent({ prompt: t, model: "sonnet" }))
);
const verified = await spawnAgent({
  prompt: `Verify: ${JSON.stringify(results)}`, model: "opus"
});
```

**Key insight**: The model generates infrastructure that multiplies effective capability — `Effective Capability ∝ Base Model × Thinking Time × Generated Harness Compute`.

### Ornith Self-Scaffolding: Trained Scaffolding Patterns

The model has internalized scaffolding patterns via a **self-improving training framework** where the scaffold co-evolves with the policy. Each RL step has two stages: (1) given task + previous scaffold → propose refined scaffold, (2) given refined scaffold + task → generate solution rollout. Reward propagates to both stages, so the model learns not just to solve tasks but to author the orchestration that elicits solutions.

A 3-layer reward hacking defense prevents the model from gaming its own verifier: fixed trust boundary (environment immutable), deterministic monitor (zero reward for boundary violations), and frozen LLM judge (vetoes intent-level gaming).

```python
# Ornith's self-improving loop (conceptual)
for step in training:
    refined_scaffold = model.propose_scaffold(task, prev_scaffold)  # Stage 1
    solution = model.generate_rollout(task, refined_scaffold)       # Stage 2
    reward = evaluate(solution)
    update_both_stages(reward)  # Scaffold and policy co-evolve
```

**Key insight**: Scaffolding knowledge is baked into weights via co-evolution — the model doesn't just learn to scaffold, it learns to *improve its own scaffolding* iteratively.

## Multi-Dimensional Comparison

### Training & Adaptation

| Dimension | RLM | Dynamic Workflows | Ornith |
|---|---|---|---|
| **Training for the pattern** | RLM-Qwen3-8B post-trained; v3 paper shows depth scaling benefits | No DW-specific model training announced | **Self-improving RL** (scaffold-policy co-evolution) |
| **Adaptation mechanism** | Model learns recursive decomposition via training | Model leverages general reasoning (Opus 4.8) to generate harnesses | Scaffold and policy jointly optimized via reward propagation |
| **Generality** | Task-agnostic (any long-context problem) | Task-agnostic (any complex multi-agent task) | Coding-focused (tool-use, file editing, API calling) |

### Architecture & Execution

| Dimension | RLM | Dynamic Workflows | Ornith |
|---|---|---|---|
| **Parallelism** | Recursive over context subsets | Fan-out of subagents (tens to hundreds) | Sequential multi-turn with error recovery |
| **Context isolation** | REPL variables (external to model) | Script variables + subagent contexts | Model-internal state management |
| **External framework** | DSPy / Python REPL required | Claude Code required | None (self-contained) |
| **Resumability** | Manual (REPL state) | Built-in (workflow resumes on interruption) | N/A (single session) |
| **Model routing** | Single model | Multi-model (Sonnet/Opus per subagent) | Single model (variant selected at deploy) |

### Performance & Scope

| Dimension | RLM | Dynamic Workflows | Ornith |
|---|---|---|---|
| **Benchmark results** | RLM(GPT-5-mini) > GPT-5 by 34pts on OOLONG; depth=3 achieves 76.0% on OOLONG-Pairs | Bun migration: 750K LOC, 11 days, 99.8% tests pass | SWE-bench Verified: top in size class |
| **Token efficiency** | Comparable to or cheaper than base model calls | Higher (model generates harness code) | N/A (no published comparisons) |
| **Primary domain** | Long-context information processing | Complex multi-agent orchestration | Agentic coding (tool-use + code gen) |
| **Local deployment** | Yes (Qwen3-8B, any Python env) | No (requires Claude Code + Anthropic API) | Yes (9B on consumer hardware, ~103 tok/s) |

## Convergence Analysis

### What All Three Share

1. **Model-generated code as orchestration** — The LLM writes executable code (Python or JS) that controls its own execution flow
2. **Context outside the main window** — Intermediate results live in variables/subagents, not in the primary context
3. **Programmatic tool invocation** — Tools are called from generated code, not from prompt-template chains
4. **Decomposition by the model** — The model decides how to break down tasks, not a human-designed pipeline

### The Training vs Scaffold Axis

The most important distinction is **where the scaffolding intelligence lives**:

```
Scaffold-only ◄────────────────────────────────────► Trained-in
     │                                                      │
     │  Dynamic Workflows          Ornith                   │
     │  (scaffold-level RLM)       (trained self-           │
     │                              scaffolding)            │
     │              RLM                                     │
     │         (both: scaffold +                            │
     │          post-training)                              │
```

- **RLM** spans both: the paradigm defines a scaffold pattern AND includes post-trained models (RLM-Qwen3-8B)
- **Dynamic Workflows** are scaffold-only: Opus 4.8 generates harnesses via general reasoning, with no DW-specific training
- **Ornith** is training-only: Agentic RL bakes scaffolding into weights, without the parallel orchestration layer

### Alex Zhang's Convergence Claim

On May 28, 2026, Zhang identified Dynamic Workflows as *"perhaps the first instance of a frontier model seriously trained to be an RLM"*. The wiki's assessment: DW implements the **architectural pattern** of RLM (programmatic sub-agent invocation, context isolation) at the scaffold layer, without evidence of model-level training for recursive context decomposition. The convergence is at the **architecture level**, not the **training level**.

Ornith adds a third vertex: convergence at the **training level** without the parallel orchestration architecture. The three approaches together suggest the field is converging on a future where both the scaffold pattern AND the training are unified — models explicitly trained to generate their own parallel orchestration code.

## Decision Framework

| If your need is... | Best fit | Why |
|---|---|---|
| Processing very long documents (>100K tokens) | RLM | Context-centric decomposition is its core strength |
| Complex multi-agent orchestration (parallelism, verification) | Dynamic Workflows | Fan-out + adversarial patterns at production scale |
| Autonomous coding with local deployment | Ornith | Self-contained, no external framework, MIT license |
| Research / understanding the paradigm | RLM | Academic foundation with formal benchmarks |
| Enterprise / production agent systems | Dynamic Workflows | Integrated with Claude Code ecosystem |
| Open-source agentic coding models | Ornith | MIT license, 9B–397B variants |

## Open Questions

1. **Will Anthropic train a model specifically for Dynamic Workflows?** Zhang's full RLM vision calls for models "explicitly trained to reason as RLMs" — DW currently relies on general reasoning
2. **Can Ornith's training approach scale to parallel orchestration?** Current Ornith is sequential; combining Agentic RL with fan-out patterns is unexplored
3. **Will RLM + DW converge?** DSPy's RLM module and Claude Code's DW could theoretically merge — a model trained to generate RLM-style REPL code with DW-style parallelism
4. **Is self-scaffolding a permanent capability or a training artifact?** Whether these patterns generalize beyond training distribution remains untested

## References

- [RLM paper (arXiv:2512.24601)](https://arxiv.org/abs/2512.24601) — Zhang, Kraska, Khattab (Dec 2025, v3 May 2026)
- [a1zhang RLM clarification](https://x.com/a1zhang/status/...) — What RLM is and is not (May 2026)
- [Dynamic Workflows announcement](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) — Anthropic (June 2026)
- [Simon Willison on Ornith-1.0](https://simonwillison.net/2026/Jun/29/ornith/) — Hands-on evaluation (June 2026)
- [Ornith-1.0 model card](https://huggingface.co/DeepReinforce) — DeepReinforce on Hugging Face
