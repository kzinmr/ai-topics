---
title: "BFCL V3 (Berkeley Function Calling Leaderboard V3)"
type: concept
created: 2026-05-08
tags:
  - ai-benchmarks
  - function-calling
  - tool-use
  - agentic-evaluation
  - multi-turn
  - llm-evaluation
related_concepts:
  - concepts/ai-benchmarks-evals-overview
  - concepts/bfcl-v1
  - concepts/bfcl-v2
  - concepts/bfcl-v4
  - concepts/agentic-ai
related_entities:
  - entities/berkeley
  - entities/gorilla
  - entities/florian-brand
---

# BFCL V3 (Berkeley Function Calling Leaderboard V3)

## Overview

BFCL V3 is the third major iteration of the Berkeley Function Calling Leaderboard, released in September 2024 by the Gorilla project at UC Berkeley. While BFCL V1 established the foundational single-turn function calling evaluation and BFCL V2 added enterprise-contributed live data, **V3 introduced multi-turn and multi-step function calling** — representing a major leap toward evaluating models in realistic, stateful, agentic scenarios.

The benchmark was accepted as an ICML 2025 paper and has become the de facto standard for evaluating LLM tool-use capabilities. As of 2026, BFCL has evolved to V4 (adding holistic agentic evaluation including web search, memory management, and format sensitivity), but V3's multi-turn evaluation remains a critical component.

## What It Measures

| Aspect | Detail |
|--------|--------|
| **Domain** | Function/tool calling in LLMs |
| **Task type** | Multi-turn and multi-step function call generation with state verification |
| **Format** | Conversation with function definitions → model must generate correct function calls across multiple turns/steps |
| **Evaluation** | State-based verification (checking API system state after execution) rather than AST parameter matching |
| **Languages** | Python, Java, JavaScript, REST API, SQL |

BFCL V3 distinguishes between three interaction patterns:

**Single-Turn (from V1/V2):** The assistant fulfills a user request with one function call. Requests are self-contained and state-agnostic.

**Multi-Step:** The assistant executes multiple internal function calls to address a single user request. The user interacts only once at the beginning; the model then interacts with the system back-and-forth (e.g., listing a directory, trying to write to a file, listing again to verify).

**Multi-Turn:** An extended exchange between user and assistant across multiple conversational turns. Each turn may involve several steps, and the assistant must retain context from previous exchanges. Users provide clarification, follow-up requests, or corrections across turns.

### Why Multi-Turn Matters

- Models must handle **dynamic, realistic interactions** where users provide partial information and follow up with clarifications.
- Models must perform **complex workflows** where one function's output becomes the next function's input.
- Models must **identify and rectify errors** across multiple exchanges — self-correction is tested naturally.
- Models may encounter scenarios like demanding credentials when already logged in, or looping endlessly on file operations — failure modes only exposed in multi-turn interactions.

## Data Sourcing

| Detail | Value |
|--------|-------|
| **Total multi-turn samples** | ~1,000 (200 base + 800 augmented) |
| **Base Multi-Turn** | 200 samples covering foundational diverse multi-turn interactions |
| **Augmented Multi-Turn** | 800 samples with additional complexity (ambiguous prompts, multi-hop reasoning, disambiguation, conditional logic) |
| **Single-turn data** | Inherited from V1 (~1,700 expert-curated) and V2 (live user-contributed) |
| **Curation method** | Expert-curated + user-contributed (V2 Live dataset) |
| **Validation** | Human-validated |
| **Release date** | September 19, 2024 |
| **Paper** | "The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models" (ICML 2025) |
| **Code** | Open-source: `github.com/ShishirPatil/gorilla` |

### State-Based Evaluation

A critical innovation in BFCL V3 is the evaluation methodology: instead of using Abstract Syntax Tree (AST) matching on function parameters (as in V1/V2), V3 **verifies the actual state of the API system** after the model executes its functions. For example, if a model is asked to create a file, modify it, then delete it, the evaluator checks the filesystem state at each step — not just whether the function calls looked syntactically correct.

This makes evaluation more realistic: a model that produces syntactically valid function calls but achieves the wrong system state will be penalized.

## Key Numbers

### Human Baseline
No formal human baseline is published. The tasks are designed to be straightforward for humans (who can easily plan multi-step tool workflows), making the human ceiling effectively 100%. The difficulty for models comes from maintaining state awareness and planning across multiple steps.

### Top Model Scores (as of May 2026)

**BFCL V3 Overall Accuracy:**
| Model | Score |
|-------|-------|
| GLM 4.5 (Thinking) | 76.7% |
| Qwen3 32B (Thinking) | 75.7% |
| Qwen3 Max | 74.9% |
| GLM-4.7-Flash (Thinking) | 74.6% |
| Nova Pro 1.0 | 67.9% |
| Kimi K2.5 (Thinking) | 64.5% |
| Llama 4 Scout | 55.7% |
| Gemini 3 Flash Preview (Thinking) | 53.5% |

**Key statistics:**
- Average score across all 23 evaluated models: **55.9%**
- Best score: **76.7%** (GLM 4.5)
- Standard deviation: **18.3**
- The wide spread (76.7% to well below 50%) indicates BFCL V3 effectively differentiates models.

### Key Findings from ICML 2025 Paper
- State-of-the-art LLMs **excel at single-turn function calls** but **struggle with memory, dynamic decision-making, and long-horizon reasoning**.
- Multi-turn scenarios expose failure modes invisible in single-turn evaluations: context loss, credential re-requests, infinite loops, and incorrect state tracking.
- Human-validated data is essential — purely synthetic multi-turn data would miss edge cases that real users encounter.

## @xeophon's Key Insight

> BFCL V3 is very important this year. It tests multi-turn and multi-step function calling — the kind of back-and-forth tool use that real agentic systems need. It's a well-done eval with human validation. The third version focuses on complex multi-step interactions where models must plan, gather information, and chain actions together, with state-based verification rather than just checking parameter matching.

## Strengths

1. **Realistic agentic scenarios**: Multi-turn/multi-step interactions mirror how AI assistants are actually used in production — not just one-shot function calls.
2. **State-based evaluation**: Checking actual system state rather than AST matching provides a more truthful measure of task completion.
3. **Human-validated data**: Expert curation + user contributions ensure real-world relevance.
4. **Comprehensive difficulty spectrum**: From simple single-turn to complex multi-turn with ambiguity and self-correction requirements.
5. **De facto standard**: BFCL has become the go-to benchmark for function calling, with wide industry adoption.
6. **Transparent and reproducible**: Open-source code, public leaderboard, detailed methodology.
7. **Cost and latency tracking**: The leaderboard includes cost and latency metrics alongside accuracy, enabling practical model selection.
8. **Language diversity**: Covers Python, Java, JavaScript, REST API, and SQL — not just Python.

## Weaknesses

1. **Moderate dataset size**: ~1,000 multi-turn samples may not capture the full diversity of real-world tool-use scenarios.
2. **Average scores still low**: The 55.9% average (and 76.7% best) shows that even top models struggle significantly — which is good for differentiation but indicates the benchmark may be too hard for practical guidance.
3. **Rapid version churn**: V1 → V2 → V3 → V4 in rapid succession makes longitudinal tracking difficult.
4. **Single-turn dominance**: Overall accuracy is an unweighted average across all sub-categories; a model doing well on single-turn but poorly on multi-turn can still appear competitive.
5. **No open-ended tool discovery**: Tests function calling given predefined functions, not the ability to discover or compose novel tools.

## Related Wiki Pages

- `concepts/ai-benchmarks-evals-overview` — Overview of the AI benchmarks and evals landscape
- `concepts/bfcl-v1` — BFCL V1, the original single-turn function calling leaderboard
- `concepts/bfcl-v2` — BFCL V2, introducing enterprise-contributed live data
- `concepts/bfcl-v4` — BFCL V4, extending to holistic agentic evaluation
- `concepts/agentic-ai` — Agentic AI systems and their evaluation
- `entities/florian-brand` — @xeophon, author of the AI Benchmarks & Evals analysis series
- `entities/berkeley` — UC Berkeley, home of the Gorilla project

## Sources

1. Patil, S.G., Mao, H., Yan, F., Ji, C.C., Suresh, V., Stoica, I., Gonzalez, J.E. (2025). "The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models." ICML 2025. https://openreview.net/forum?id=2GmDdhBdDk
2. Gorilla Project. "BFCL V3 • Multi-Turn & Multi-Step Function Calling Evaluation" blog post. https://gorilla.cs.berkeley.edu/blogs/13_bfcl_v3_multi_turn.html
3. Berkeley Function Calling Leaderboard (Live). https://gorilla.cs.berkeley.edu/leaderboard.html
4. Gorilla Project. `BFCL` dataset on Hugging Face. https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard
5. Price Per Token — BFCL v3 Leaderboard 2026. https://pricepertoken.com/leaderboards/benchmark/bfcl-v3
6. LLM Stats — BFCL-v3 Leaderboard. https://llm-stats.com/benchmarks/bfcl-v3
