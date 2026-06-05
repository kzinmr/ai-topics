---
title: "dsprrr"
created: 2026-06-05
updated: 2026-06-05
type: entity
tags: [dspy, rlm, framework, structured-outputs]
sources:
  - https://jameshwade.github.io/dsprrr/
  - https://github.com/JamesHWade/dsprrr
  - https://jameshwade.github.io/dsprrr/articles/how-rlm-works.html
---

# dsprrr

**dsprrr** is an R-native implementation of the [DSPy](/concepts/dspy) programming model for language models, created by **James H. Wade**. It brings DSPy-style declarative LM programming to the R ecosystem with tight integration into the tidyverse toolchain.

## Core Features

- **Signatures**: Declarative input/output specifications (e.g., `"document, question -> answer"`)
- **Modules**: `PredictModule` (single-shot), `rlm_module()` (recursive REPL-based), `chain_of_thought()`, `rag_module()`
- **Structured outputs**: Via [ellmer](https://ellmer.tidyverse.org/) types (`type_object`, `type_string`, `type_enum`, etc.)
- **Optimization**: Teleprompters and grid search for systematic prompt/example optimization
- **Evaluation**: Built-in metrics and evaluation infrastructure

## RLM Module

dsprrr's flagship feature is `rlm_module()`, an R-native implementation of [[concepts/rlm-recursive-language-models|Recursive Language Models (RLM)]]. Key implementation details:

- **Subprocess isolation** via [callr](https://callr.r-lib.org/): each REPL iteration runs in a fresh R subprocess with package allowlist and dangerous-call pattern scanner
- **REPL tools**: `peek()` (variable slicing with dual-dispatch), `search()` (Perl-compatible regex), `SUBMIT()` (sentinel class `rlm_final`), `llm_query()` / `llm_query_batched()` (marker-based recursive sub-queries)
- **Sub-LM support**: Configurable secondary model for recursive queries (e.g., `ellmer::chat_openai(model = "gpt-5-mini")`)
- **Fallback extraction**: Two-phase structured/unstructured output synthesis when `SUBMIT()` never called
- **Observability**: Full REPL history recording (reasoning, code, output, success/failure, timing per iteration)

## R-Language Differentiation

dsprrr is the **only R-language RLM implementation**. This matters when context is R data:
- Data frames, model objects, package source code can be directly accessed as REPL variables
- Inherits tidyverse evaluation and metaprogramming patterns
- Compatible with R's statistical modeling ecosystem

## Ecosystem Position

| | dsprrr | DSPy | Official rlm | Google ADK |
|---|---|---|---|---|
| **Language** | R | Python | Python | Python |
| **REPL** | R via callr | Python via Pyodide/WASM | Python | Python via ADK |
| **Sandbox** | Subprocess (callr) | Deno/WASM | Configurable | ADK orchestration |
| **Structured output** | ellmer types | DSPy signatures | Freeform | ADK tools |
| **Optimization** | Teleprompters, grid search | DSPy optimizers | Manual | Manual |
| **Batched sub-calls** | `llm_query_batched()` | — | — | — |

## Status

- **Version:** 0.0.0.9000 (development)
- **Source:** [github.com/JamesHWade/dsprrr](https://github.com/JamesHWade/dsprrr)

## Related

- [[concepts/rlm-recursive-language-models]] — The RLM paradigm that dsprrr implements in R
- [[concepts/dspy]] — The original Python framework that dsprrr ports to R
- [[concepts/dspy-rlm]] — DSPy's RLM module (Python counterpart)
- [[entities/omar-khattab]] — DSPy creator and RLM co-author
- [[entities/alex-zhang]] — RLM primary author
