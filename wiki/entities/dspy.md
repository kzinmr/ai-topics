---
title: DSPy
created: 2026-04-25
updated: 2026-04-30
type: entity
tags:
  - open-source
  - framework
  - tool
  - nlp
sources:
  - raw/articles/crawl-2026-04-29-dspy-adoption-gap-khattabs-law.md
---

# DSPy

DSPy (Declarative Self-improving Python) is an open-source framework developed by Stanford NLP Group (led by Omar Khattab, Arnav Singhvi, Paridhi Maheshwari, et al.) for building systems that use large language models. Instead of writing hand-crafted prompts, developers declare what the LLM should do, and DSPy optimizes the prompt automatically.

## Key Facts

- **Created by:** Stanford NLP Group (Omar Khattab, Arnav Singhvi, Paridhi Maheshwari, et al.)
- **Type:** Open-source Python framework
- **Core idea:** Replace prompt engineering with declarative program specification
- **Approach:** Uses bootstrap-and-finetune cycles to optimize prompt templates
- **GitHub:** [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)

## Philosophy

> *"It's actually better to think of language models as modules in programs, not end products."* — Omar Khattab, Cohere talk (2024)

DSPy treats LMs as **learnable modules** in a computational graph:
1. **Define** a program with LM modules (Chain of Thought, ReAct, program-level reasoning)
2. **Specify** a metric for evaluation
3. **Optimize** the prompts (or fine-tune weights) automatically using built-in optimizers

DSPy unifies prompting, fine-tuning, and retrieval-augmented generation under a single programming model. Small models (T5, <1B parameters) expressed in DSPy routinely outperform large standalone LMs with hand-crafted prompts.

## Core Components

| Component | Description |
|-----------|-------------|
| **Signatures** | Declarative input/output contracts (model-independent) |
| **Modules** | Composable inference patterns (`dspy.Predict`, `dspy.ChainOfThought`, `dspy.ReAct`, `dspy.ProgramOfThought`) |
| **Optimizers** | Automatically tune prompt templates via Teleprompter (`BootstrapFewShot`, `MIPRO`, `MIPROv2`) |

## Architecture

See [[concepts/dspy-architecture]] for the full architectural deep-dive including the three core abstractions (Signatures, Modules, Teleprompters).

## Modules and Patterns

DSPy provides a rich set of composable modules supporting patterns like RAG, multi-hop search, and multi-agent debate — all **model-independent**.

See [[concepts/dspy-modules]] for the complete module reference.

## Optimization

DSPy offers three complementary optimization approaches:
1. **Teleprompters** — Data-driven prompt optimization (BootstrapFewShot, MIPROv2, COPRO, Ensemble)
2. **Assertions** — Runtime validation with automatic self-correction loops
3. **Fine-Tuning + Prompt Optimization synergy** — Combined approach yields +23% improvement

See [[concepts/dspy-optimization]] for detailed coverage.

## Adoption: Khattab's Law

Skylar Payne (March 2026) introduced **"Khattab's Law"** — named after DSPy creator Omar Khattab — which holds that *any sufficiently complex AI system eventually reinvents DSPy's core abstractions on its own*: typed I/O signatures, composable modules, prompt versioning, retry logic, and model-swapping shims. Teams do this ad hoc, buggily, and after significant pain.

**Production users** include JetBlue, Databricks, Replit, VMware, and Sephora. **Download gap:** DSPy ~4.7M monthly downloads vs LangChain ~222M, indicating significant adoption friction despite technical merit.

## Application Guidelines

**Use DSPy when:**
- Same task is **repeated** in a pipeline
- **Evaluation metrics** are clearly defined
- 10-50+ training examples are available
- Pipeline runs across multiple LLMs
- Prompt maintenance cost is high

**Avoid DSPy when:**
- One-off exploratory queries (no evaluation data)
- Highly **dynamic tasks** (frequent Signature changes)
- **Real-time adaptation** needed (consider RLMs)
- Broad **ecosystem integrations** critical (consider LangChain)

## Relationship to Other Wiki Topics

- [[concepts/dspy]] — Core concept page (deep-dive)
- [[concepts/dspy-architecture]] — Architecture deep-dive
- [[concepts/dspy-optimization]] — Teleprompters, Assertions, Fine-Tuning
- [[concepts/dspy-comparisons]] — DSPy vs LangChain, RLMs, GEPA
- [[concepts/gepa]] — Genetic prompt optimization built on DSPy
- [[concepts/recursive-language-models]] — RLM approach can complement DSPy
- [[concepts/rlms]] — Recursive Language Models
- [[omar-khattab]] — Creator of DSPy

## Key Papers

| Date | Title | Insight |
|------|-------|---------|
| Oct 2023 | DSPy: Compiling Declarative LM Calls (ICLR 2024) | Teleprompter paradigm |
| Dec 2023 | DSPy Assertions | Self-correcting pipelines |
| Jul 2024 | Fine-Tuning and Prompt Optimization | Synergistic combination (+23%) |
| 2025 | GEPA | Genetic prompt evolution |
| 2025 | RLMs | Recursive context processing |
