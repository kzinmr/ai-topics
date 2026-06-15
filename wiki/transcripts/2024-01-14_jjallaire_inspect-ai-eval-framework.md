---
title: "Hamel Husain's Course — Inspect: An OSS Framework for LLM Evals w/ JJ Allaire (Lecture Transcript)"
author: JJ Allaire
date: 2024-01-14
date_ingested: 2026-06-15
source: https://github.com/UK-AISI/inspect_ai
type: transcript
tags:
  - transcript
  - evaluation
  - evals
  - open-source
  - framework
  - llm-as-judge
  - agent-evaluation
  - developer-tooling
  - python
  - ai-safety
  - harness-engineering
participants:
  - JJ Allaire (presenter)
  - Hamel Husain (host)
  - Dan Becker (host)
---

# Inspect: An OSS Framework for LLM Evals — JJ Allaire

> Conference talk from Hamel Husain's AI Evals course (Jan 14, 2024). JJ Allaire presents Inspect, an open-source LLM evaluation framework developed in collaboration with the UK AI Safety Institute.

## Introduction by Hamel Husain

**[00:00:07]** Hamel introduces JJ Allaire as an "epic programmer" with a long history in developer tools. JJ is most well-known for creating **RStudio**, widely regarded as the most loved development environment among data scientists. His company is now called **Posit** (formerly RStudio), where he continues building polished open-source tools in Python.

**[00:01:31]** Hamel notes that when JJ creates something, he always pays attention — and JJ has been working on an open-source LLM framework called **Inspect**.

## What is Inspect?

**[00:01:51]** JJ introduces **Inspect** — an open-source LLM eval framework he's been developing over the past half year.

> `pip install inspect-ai`

**[00:02:50]** **Not a Posit project.** Inspect is a collaboration with the **UK AI Safety Institute (UK AISI)**, which has hundreds of evaluations of every variety — simple QA, cybersecurity CTF, and more.

**[00:03:08]** When they started writing evaluations, there weren't good tools available. Existing tools were either embedded in benchmark frameworks, incomplete, not well-tooled, or unclear about future development. The most popular eval framework was "roll your own." Inspect was built to be something they could use internally and share broadly.

**Key design philosophy:** Python code first. Conforming to simple conventions gives you access to a big pipeline of tools and an ecosystem of related packages.

**[00:05:24]** **Local-first, but scalable.** Development is interactive and local (notebooks, REPL), but Inspect has tooling to scale up — run over 10 models, run in CI, etc.

## Core Concepts

**[00:06:03]** Three core components:

### 1. Dataset
- Inputs and usually targets
- For Honeycomb: 2,300 user inputs + schemas fetched by RAG
- Targets can be: correct answers for multiple choice, grading rubrics for model-graded evals, or validation functions

### 2. Solvers
- The **pipeline that actually does the eval**
- Can do prompt engineering, call the model, multi-turn dialogue, critique, elicitation
- **The heart of the entire eval** — where you customize how it works

### 3. Scorer
- Evaluates the final output
- Can be: text comparisons, model-graded, custom schemes, or human scoring

## Honeycomb Eval Walkthrough

**[00:07:14]** JJ demonstrates an eval built for the Honeycomb dataset (from Hamel's course):

- **Dataset**: Read from CSV, save `columns` field for prompt template
- **Plan**: Same system message from the course notebooks
- **Solver (`prompt_with_schema`)**: Takes a prompt template, substitutes prompt and columns — that's all it does
- **Solver (`generate`)**: Literally just calls the model to generate
- **Score**: Uses the `check_query` function from the course, strips JSON code blocks, calls `is_valid`

**[00:09:05]** After running the eval, you get a **log viewer** that lets you explore everything — overall results and per-sample drill-down. You can see the full message history, injected schemas, and the assistant's answer.

> *In so many evals, the score really doesn't tell you anything close to enough, especially when you first start developing them.*

## Critique-Based Scoring

**[00:10:15]** A second eval uses the same code but with a **critique model for scoring** instead of a validation function:

- **Parameterized grader model** — don't use the same model for scoring as the one being evaluated; often use a more powerful model
- Defaults to GPT-4 Turbo but users can specify any model
- Critique prompt is the exact same prompt from the course notebooks
- Runs critique, parses output, checks if good, returns score

**[00:12:03]** You can drill into incorrect answers to see the critique model's explanation — this helps identify whether the prompt template for the critique needs improvement or whether a fine-tuned grader model is needed.

## Solvers in Depth

**[00:14:12]** A solver transforms **task state** (current message history + current model output). It can:
- Call the model, generate, append assistant message
- Do prompt engineering
- Do critique
- Anything that transforms state usefully

### Simple Solvers
- **Prompt template**: Transform prompt through a template with metadata
- **Generate**: Literally just calls `model.generate()` — the source code is that simple
- **Chain of thought**: Basic CoT template (but often needs domain customization)

### Advanced Solvers
- **Multiple choice**: Shuffles choices, calls generate, unshuffles
- **Self critique**: Takes existing completion, runs critique, appends to message history, calls generate again to re-answer with critique available

## Composition — The Big Idea

**[00:17:55]** One of Inspect's key ideas: people will write Python packages with scores and solvers that you can **mix and match**.

**Example — Shepherd (internal UK AISI package):**
- Contains jailbreak solvers that do prompt engineering to get models to answer questions they'd otherwise refuse
- Used in a cybersecurity eval where the model flags security questions — the jailbreak solver helps elicit actual knowledge
- You bring in a jailbreak solver from Shepherd and use it in your pipeline alongside your normal system message

> You can imagine a whole Python package full of prompt engineering techniques. And a whole Python package full of critique, debate, all kinds of things.

## Tool Use and Agents

**[00:20:09]** Task state also includes **tools** — Python functions made available to the model via docstrings.

**Simple tool use example:** Biology QA task where the model can use web search for obscure questions.

**Bespoke agent example:** Cybersecurity CTF task — a hand-rolled agent loop where the model keeps using tools until it finds the flag or terminates.

### Integrating External Agent Frameworks

**[00:22:04]** High-order functions let you take an existing agent framework and turn it into a solver:

**LangChain example:** Pure LangChain code (Wikipedia tool, agent setup) wrapped in a solver function. No Inspect code in the middle — just bridge the interface.

The log viewer shows tool use diagnostics: what tools the model chose, explanations, results.

## Scoring Deep Dive

**[00:25:28]** Scoring approaches:
- **Pattern matching**: Regex, template matching, answer extraction
- **Model-graded scores**: Built-in but usually need template customization for your domain
- **Pluggable**: Get from other packages
- **Human scoring**: Just say "no score" and have humans grade
- **Rigorously evaluate model-graded scores against human baselines** — many people deploy LLM judges without grounding them

### Math Benchmark Scoring Example

**[00:26:51]** For the math benchmark:
- Model does math, there's a target, but the answer can be correct even if not literally matching the target
- **Expression equivalence solver**: A few-shot model assessment (20 examples) that checks if expressions are logically equivalent — can handle algebra and factoring
- Extract answer via regex of "answer:" pattern, then send to equivalence solver

## Logging

**[00:29:08]** Logging is "massively important" for good evals:
- Rich Python object + JSON with published JSON schema
- Log viewer on top of logs
- API for interrogation — get multiple logs, plot differences
- Compute on logs for grid search results, comparisons

## Models

**[00:30:18]** Supports many models via provider prefix:
- `openai/gpt-4-turbo`, `hf/meta-llama/Llama-2-70b`, `together/...`, `ollama/...`
- **Model names are opaque** — just passed through, no resolution. When a new model comes out, you just start using it.
- Custom base URLs supported (Ollama, vLLM use OpenAI API)
- Custom model providers can be created and published as packages
- LM proxies like LiteLLM work fine

## Development to Production Workflow

**[00:31:56]** Interactive notebook development → formalized tasks → external driver programs:

- **Notebooks**: Exploratory work, grid search over models/graders/system prompts
- **Parameterized tasks**: Vary system prompt and grading prompt externally via `inspect eval` CLI
- **Eval suites**: Dozens of evals in directories, found and run automatically
- **Production**: Run evals, put logs in S3 bucket, retry failures

## Reproducibility

**[00:34:29]** If you run an eval from a git repository, the log file is a **unit of reproducibility**:
- Read log → get origin and commit → clone → run eval
- Won't give same results (models are non-deterministic) but reproduces all input parameters

## Resources

- **Documentation**: https://inspect.ai-safety-institute.org.uk/
- **Annotated examples**: Walk through code explaining all components
- **Benchmarks**: Implemented benchmarks showing how they're done
- **Workshop repo**: Slides + code (Honeycomb evals, LangChain example, benchmarks)
  - Honeycomb directory: full code, prompts, utils from the course, two eval tasks + notebook version

## Q&A

**[00:37:54] Integration with Posit products?**
Inspect is not a Posit project — it's a UK AISI project. VS Code extension exists, but no planned Posit integration.

**[00:38:29] Evaluating with past inputs/outputs?**
Yes — input can be a prompt or a message history. You can replay an entire message history from past logs to construct a new dataset.

**[00:39:15] Expanding metrics (MRR, etc.)?**
Yes — built-in metrics are sparse because many people write their own, but definitively important metrics will be added. Team is 2-3 people full-time, plus many UK AISI contributors.

**[00:40:23] Long-term future?**
Definitely long-term development. Viewed as a foundational piece for sophisticated evaluations. Interested in community discussion and consensus. Goal: level up evaluation quality broadly.

**[00:41:40] Log sources (API, database)?**
Uses fsspec — logs can come from any file system addressable by fsspec. Internal log recorder abstraction doesn't presume JSON files. Published JSON schema, TypeScript types, Python API.

**[00:43:06] Docker-based cybersecurity CTF evals?**
Shareable suites of security tests are planned. Others in the ecosystem planning to open-source similar suites. A more formal **tool execution environments** construct for Docker/docker-compose support is coming in 1-2 months.

**[00:44:24] Weights & Biases integration?**
On the short list (2-4 months). Could potentially embed log viewer via iframe, project log results into W&B affordances.

**[00:45:13] Design philosophy?**
> *"It's all Hadley all the time."*

Inspired by **Hadley Wickham** (tidyverse creator). Hadley is the "virtual sitting on my shoulder" keeping things clean, simple, straightforward, and composable.

**[00:45:55] LM proxies (LiteLLM)?**
Absolutely works.

**[00:46:12] Mac GPU support?**
Via Ollama (Metal acceleration) or HuggingFace MPS backend. Ollama has done a better job reducing memory requirements.

## Companion Resources

- **Inspect AI docs**: https://inspect.ai-safety-institute.org.uk/
- **Inspect AI GitHub**: https://github.com/UK-AISI/inspect_ai
- **JJ Allaire GitHub**: https://github.com/jjallaire
- **Workshop repo**: Referenced in talk (slides + Honeycomb evals + LangChain example + benchmarks)
