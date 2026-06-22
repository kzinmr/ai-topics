---
title: W&B Weave
type: entity
tags:
  - model
  - evaluation
  - infrastructure
  - trace-analysis
  - tool
created: 2026-06-15
updated: 2026-06-15
sources:
  - "https://wandb.ai/weave"
  - "https://weave-docs.wandb.ai"
  - "https://github.com/wandb/weave"
---

# W&B Weave

**Type:** LLM tracing and evaluation framework
**Parent:** [[entities/weights-and-biases|Weights & Biases]]
**Status:** Public preview (announced 2024), integrated into CoreWeave/W&B platform (2025+)
**Python:** `pip install weave`
**GitHub:** https://github.com/wandb/weave

## Overview

W&B Weave is a lightweight Python library for tracing, evaluating, and debugging LLM applications. It extends W&B's experiment tracking heritage into the LLM application layer — where the "experiment" is not a training run but an LLM-powered function call chain.

Weave targets the **LLM application developer** persona: someone who builds on top of LLM APIs (OpenAI, Anthropic, etc.) and needs to trace inputs/outputs, evaluate quality, and iterate on prompts and chains.

## Core Concepts

### Tracing with `@weave.op()`
The primary interface is a decorator that wraps Python functions:

```python
import weave

weave.init("my-project")

@weave.op()
def call_openai(prompt):
    response = openai.chat.completions.create(
        model="gpt-4", messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
```

When decorated functions are called, Weave automatically logs:
- Function signature (inputs/outputs via Pydantic)
- Nested call hierarchy (which functions call which)
- Underlying API calls (with provider integrations for OpenAI, etc.)
- Latency, token counts, and cost metadata

### Evaluation Framework
Weave provides a structured evaluation pipeline:

1. **Define a model** (lightweight wrapper around a Pydantic base model with a `predict` function)
2. **Create a dataset** (list of examples with expected outputs)
3. **Define a scoring function** (compare predictions against expected outputs)
4. **Run evaluation**: `weave.Evaluation(dataset=dataset, scorers=[score_fn]).evaluate(model)`

Results flow to a W&B dashboard with:
- Per-sample inspection (input, prediction, score, expected)
- Version tracking across model and prompt iterations
- Leaderboard comparison across evaluation runs

### Integrations
- **OpenAI**: Automatic tracing of `chat.completions.create` calls
- **Anthropic**: Tracing for Claude API calls
- **Pydantic**: Built on top of Pydantic for type-safe inputs/outputs
- **W&B Models**: Evaluation results can flow to W&B experiment tracking dashboards

## Architecture

Weave is designed as a lightweight, standalone library (not a full platform dependency):
- `pip install weave` — single package install
- Connects to W&B backend for storage and visualization
- Can log to W&B projects (shared dashboards) or local mode
- Pydantic-based model wrappers for structured data handling

## Use Cases

### LLM Application Debugging
Trace nested function calls in multi-step LLM pipelines (RAG, tool use, chains). When a function fails, inspect inputs/outputs at each level — "like a debugger for LLM applications."

### Prompt Iteration
Version-track prompts, models, and evaluation results together. Compare "one-shot prompt" vs "chain-of-thought" vs "tool-augmented" approaches on the same evaluation dataset.

### Evaluation-as-Dashboard
Create shared evaluation dashboards where teams can submit and compare model/prompt versions. The NYT Connections puzzle demo (Thomas Capelle, Jan 2024) showed this pattern: multiple participants could submit solutions and compare on a leaderboard.

## Relationship to W&B Models

| Aspect | W&B Models | W&B Weave |
|--------|-----------|-----------|
| Target | Training/fine-tuning | LLM application layer |
| What's tracked | Training metrics, loss, gradients | Function calls, API inputs/outputs |
| User | ML engineer training models | Developer building on LLM APIs |
| Artifact | Checkpoints, datasets | Traces, evaluations, prompts |
| Decorator | N/A (framework integration) | `@weave.op()` |

Both products share the W&B backend for storage and visualization. Weave traces and Model experiments can coexist in the same project.

## Compared to Alternatives

- **LangSmith** (LangChain): Tighter LangChain ecosystem integration; Weave is framework-agnostic
- **Arize Phoenix**: Open-source LLM observability; Weave has tighter W&B integration
- **Helicone**: API proxy-based logging; Weave uses in-code decorators
- **Braintrust**: Evaluation-focused; Weave combines tracing + evaluation

## Notable Wiki Connections

- [[entities/weights-and-biases|Weights & Biases]] — Parent platform
- [[entities/thomas-capelle]] — W&B engineer who demonstrated Weave (NYT Connections demo)
- [[transcripts/2024-01-26_tcapelle_getting-the-most-out-of-llm-experiments-lecture]] — Weave demo walkthrough
- [[concepts/ai-evals-people|AI Evals]] — Weave is used for LLM evaluation workflows

## Related

- [[entities/weights-and-biases|Weights & Biases]] — Parent company
- [[concepts/experiment-tracking]] — W&B's heritage; Weave extends this to LLM apps
