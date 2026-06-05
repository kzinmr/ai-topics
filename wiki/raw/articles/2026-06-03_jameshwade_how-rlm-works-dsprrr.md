---
title: "How the Recursive Language Model (RLM) Works — dsprrr"
url: https://jameshwade.github.io/dsprrr/articles/how-rlm-works.html
author: James H. Wade
date: 2026-06-03
fetched: 2026-06-05
type: article
tags: [rlm, dspy, context-rot, repl, r-language, code-execution, long-context, inference]
---

# How the Recursive Language Model (RLM) Works

**Author:** James H. Wade
**Date:** 2026-06-03
**Package:** dsprrr v0.0.0.9000 (R)
**Source:** https://jameshwade.github.io/dsprrr/articles/how-rlm-works.html
**Paper:** Zhang et al. 2025, https://arxiv.org/abs/2512.24601

## The Problem: Context Rot

Modern LLMs accept enormous context windows. GPT-5 handles a million tokens; Gemini stretches to two million. But bigger windows do not solve the fundamental problem.

As context grows, performance degrades: details get lost and answers go wrong. The MIT researchers who introduced Recursive Language Models call this *context rot*, the empirical observation that output quality deteriorates as prompts grow, even when the relevant information is technically within the window. The model misses what it needs with increasing frequency as input length grows.

And there is no adaptive retrieval. The model cannot decide to re-read section 14 after discovering something relevant in section 42. It processes the entire input in one pass and produces output from whatever signal survived.

## The Insight: Context as Environment

The core idea behind RLMs is simple: *don't put the context in the prompt*. Instead, store it as a variable in a programming environment and let the model write code to explore it.

A traditional call looks like this:
```r
llm$chat(paste("Summarize this document:", huge_document))
```

An RLM inverts the relationship. The document lives outside the model as a variable in an R session, and the model generates code to interact with it. When you call `run()`, dsprrr provides a REPL: the model writes R code, dsprrr executes it in a subprocess, and the printed output feeds back into the next iteration. A typical exploration might look like this:

```r
# The model generates and executes code like this:
intro <- peek(.context$document, 1, 2000)
findings <- search(.context$document, "\\b(conclusion|finding|result)\\b")
section_42 <- peek(.context$document, 85000, 90000)
SUBMIT(answer = "The document concludes that...")
```

The shift is from treating context as *input* to treating it as *environment*. The model reads what it needs, skip what it doesn't, and revisits sections as its picture of the data develops.

In dsprrr's API, the module receives input arguments (e.g., `question`), holds context variables (e.g., `document`) outside the prompt, and exposes `llm_query()` so the model can delegate sub-questions to a secondary model from generated code. In the paper's notation (Zhang et al. 2025), these correspond to a query q, context C, and a recursive tool call RLM_M(q̂, Ĉ) that spawns an isolated sub-instance with a new query and a transformed slice of the context.

## Origin and Ecosystem

RLMs were introduced by Alex Zhang, Tim Kraska, and Omar Khattab at MIT (Zhang et al. 2025). On BrowseComp-Plus (a benchmark with 6–11 million token inputs), standard models scored 0% while an RLM powered by GPT-5 achieved 91.33%. That comparison is less "RLM beats prompting" than "RLM makes previously intractable tasks tractable"; inputs that large exceed every current model's context window. The fairer apples-to-apples result is that their post-trained RLM-Qwen3-8B outperformed the base Qwen3-8B by 28.3% on average across long-context tasks.

The idea has since spread quickly. DSPy integrated RLMs as a first-class module (`dspy.RLM`) in version 3.1.2+, using a Pyodide WASM sandbox for code execution. Google's Agent Development Kit re-implemented the pattern with Gemini models. The official `rlm` Python package, a community implementation, and Prime Intellect's research program round out the ecosystem.

dsprrr's `rlm_module()` brings the same approach to R, using R as the REPL language instead of Python, with subprocess isolation via callr and structured outputs via ellmer.

## How dsprrr Implements RLM

### The User-Facing API

Creating an RLM module requires two things: a signature declaring inputs and outputs, and a code runner for subprocess isolation:

```r
library(dsprrr)

runner <- r_code_runner(timeout = 30)

rlm <- rlm_module(
  signature = "document, question -> answer",
  runner = runner
)
```

For tasks that benefit from recursive sub-queries, you can wire up a secondary model:

```r
rlm <- rlm_module(
  signature = "document, question -> answer",
  runner = runner,
  sub_lm = ellmer::chat_openai(model = "gpt-5-mini"),
  max_llm_calls = 10
)
```

You can also inject custom R functions as tools available in the REPL. The factory validates these against reserved names (SUBMIT, peek, search, llm_query, etc.) to prevent collisions.

### The REPL Loop

When you call `run(rlm, ...)`, dsprrr dispatches to the module's internal `forward()` method. This is where the REPL loop lives. A `PredictModule`'s `forward()` makes a single call; the RLM module loops, up to `max_iterations` times (default 20):

```r
# From R/module-rlm.R (simplified)
for (iter in seq_len(self$max_iterations)) {
  prompt <- private$build_iteration_prompt(system_prompt, history, iter)
  response <- private$get_code_response(llm, prompt)
  exec_result <- private$execute_with_rlm_tools(response$code, inputs, call_counter)

  history[[iter]] <- list(
    iteration = iter,
    reasoning = response$reasoning,
    code = response$code,
    output = exec_result$formatted_output,
    success = exec_result$success,
    is_final = exec_result$is_final
  )

  if (exec_result$is_final) {
    final_answer <- exec_result$final_value
    break
  }
}
```

Each iteration produces a structured response with two fields: `reasoning` (the model's explanation of its plan for that step) and `code` (R code to execute). This uses ellmer's structured output support:

```r
output_type <- ellmer::type_object(
  reasoning = ellmer::type_string("Your thought process for this step"),
  code = ellmer::type_string("R code to execute")
)
result <- llm$chat_structured(prompt, type = output_type)
```

The accumulated history gives the model a growing record of what it has tried. Failed executions are included. The model sees its own errors and can correct course.

### REPL Tools

Before each execution, dsprrr injects a "prelude" that defines the tools available in the subprocess. These are defined in `R/rlm-tools.R`:

**`peek(var, start, end)`** views a slice of a variable. It dispatches on the input type: for a character vector, `start` and `end` are element indices; for a single string, they are character positions.

**`search(var, pattern)`** runs a Perl-compatible regex against a variable and returns all matches.

**`SUBMIT(...)`** terminates the loop and returns the final answer. It validates that the provided values match the signature's output fields, supporting both positional (`SUBMIT("my answer")`) and named (`SUBMIT(answer = "my answer")`) arguments.

The `.rlm_output_fields` variable is not magic. It is injected into the subprocess by the same prelude that defines `peek()`, `search()`, and `SUBMIT()` itself. The prelude reads the signature's output field names and writes them as a character vector at the top of the execution script.

The `rlm_final` class is a sentinel: when the parent process sees it in the subprocess result, it exits the loop and extracts the answer.

### Subprocess Isolation

All model-generated code runs in an isolated R subprocess via `callr::r()`. The `RCodeRunner` class in `R/r-code-runner.R` handles this:

```r
exec_result <- callr::r(
  func = private$execution_wrapper,
  args = list(code = code, context = context, ...),
  timeout = self$timeout,
  stdout = stdout_file,
  stderr = stderr_file,
  user_profile = FALSE
)
```

Inside the subprocess, a fresh environment is created with the context available as `.context`. The wrapper overrides `library()` and `require()` to enforce a package allowlist, and a pattern scanner rejects calls to `system()`, `unlink()`, `quit()`, and `download.file()`. Each iteration spawns a new subprocess, so each pays a cold-start cost (typically 200–400ms depending on platform).

### Recursive Sub-Queries

This is where the "recursive" in RLM comes from. When `sub_lm` is provided, the model can write `llm_query("What does section 3 say?", context_slice)` in its generated code. The function does not execute the sub-call inside the subprocess, which would be a security problem. Instead, it returns a marker object:

```r
llm_query <- function(query, context_slice = NULL) {
  structure(
    list(query = query, context = context_slice, batch = FALSE),
    class = "rlm_query_request"
  )
}
```

The parent process intercepts this marker after execution, performs the actual call, and feeds the result back on the next iteration. A batched variant, `llm_query_batched()`, allows multiple sub-questions at once, running concurrently via `ellmer::parallel_chat()` when available.

A shared call counter tracks total calls across all iterations and enforces the `max_llm_calls` budget, preventing runaway recursion.

### Fallback and Output Normalization

If the model exhausts all iterations without calling SUBMIT(), the module performs fallback extraction: it feeds the entire exploration trajectory back and asks for a synthesized answer from what was discovered. This uses a two-phase approach, trying structured output via `chat_structured()` first, then unstructured `chat()` if that fails.

The final answer passes through output normalization, which coerces whatever was produced into the signature's declared output fields. This handles named lists, positional lists, scalar values, and case-insensitive enum matching.

### Observability

Every RLM execution records its full REPL history: reasoning, code, output, success or failure, and timing for each iteration:

```r
history <- rlm$get_repl_history()
last_run <- history[[length(history)]]
last_run$iterations_used  # e.g. 5
last_run$llm_calls_used   # e.g. 3
```

## Comparison Table: RLM Implementations

| | dsprrr | DSPy | Official rlm | Google ADK |
|---|---|---|---|---|
| **Language** | R | Python | Python | Python |
| **REPL** | R via callr | Python via Pyodide/WASM | Python (isolated or not) | Python via ADK |
| **Sandbox** | Subprocess (callr) | Deno/WASM | Configurable | ADK orchestration |
| **Structured output** | ellmer types | DSPy signatures | Freeform | ADK tools |
| **Recursive calls** | llm_query() | Built-in | Built-in | Child agents |
| **Optimization** | Teleprompters, grid search | DSPy optimizers | Manual | Manual |
| **Batched sub-calls** | llm_query_batched() | – | – | – |

dsprrr is the only implementation that uses R as the REPL language, which matters when your context is R data: data frames, model objects, or package source code. It also inherits dsprrr's full optimization infrastructure (teleprompters, grid search, evaluation metrics), so you can systematically improve RLM performance, not just run it.

## When to Use RLMs (and When Not To)

The hard part of any task here is either finding the right context or reasoning about it once found. RLMs help with the first problem. If the context is already short and well-scoped, simpler approaches are faster and cheaper.

| Approach | Best for | Latency | Context limit |
|---|---|---|---|
| PredictModule | Short, self-contained tasks | Low | Context window |
| chain_of_thought() | Complex reasoning, known context | Medium | Context window |
| rag_module() | Lookup in large corpora | Medium | Chunk size |
| rlm_module() | Exploration of large, interconnected data | High | Unlimited* |

*Bounded by max_iterations and max_llm_calls, not by context window size.

**Skip RLMs when the context is short.** If the document fits comfortably in the context window, a PredictModule or chain_of_thought() will be faster and cheaper.

**Skip RLMs when the task is well-defined.** If you know what you are looking for (extracting a specific field from a known document format), a prompt-optimized module will outperform an RLM.

**Skip RLMs when cost-per-query matters.** An RLM with 15 iterations makes at least 15 calls, plus any recursive sub-queries. For a production pipeline processing thousands of inputs, that multiplier adds up.

**Skip RLMs when the context contains bad information.** RLMs gather more evidence than simpler approaches, which is usually beneficial. But more evidence also means more surface area for misleading content.

## Improvement Opportunities

### Design Constraints

- Process-level isolation is not a security boundary — the package allowlist and pattern scanner are defense-in-depth, not a sandbox
- No persistent REPL state across iterations — each subprocess starts fresh
- Subprocess cold-start overhead — each iteration spawns a fresh callr::r() process, costing 200–400ms per iteration

### API Improvements

- `peek()` dual-dispatch API silently changes meaning depending on input type
- `search()` returns raw matches, not locations — the model gets matched text but not byte offset or surrounding context
