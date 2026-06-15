---
title: "Inspect AI"
created: 2026-06-15
updated: 2026-06-15
type: entity
tags: [product, framework, open-source, evaluation, evals, llm-as-judge, agent-evaluation, python, ai-safety]
sources:
  - transcripts/2024-01-14_jjallaire_inspect-ai-eval-framework.md
  - https://github.com/UK-AISI/inspect_ai
---

# Inspect AI

| | |
|---|---|
| **Type** | Open-source LLM evaluation framework |
| **Author** | [[entities/jj-allaire\|JJ Allaire]] |
| **Organization** | UK AI Safety Institute (UK AISI) collaboration |
| **Language** | Python (`pip install inspect-ai`) |
| **GitHub** | [UK-AISI/inspect_ai](https://github.com/UK-AISI/inspect_ai) |
| **Docs** | [inspect.ai-safety-institute.org.uk](https://inspect.ai-safety-institute.org.uk/) |
| **License** | Open source |

## Overview

**Inspect AI** is an open-source Python framework for LLM evaluation developed by [[entities/jj-allaire|JJ Allaire]] in collaboration with the **UK AI Safety Institute**. It is designed to support both simple benchmark-style evaluations and highly complex evals, with a focus on being Python-code-first, composable, and extensible.

Unlike many eval tools that are embedded in benchmark frameworks or are incomplete, Inspect was built from the ground up to handle the scale and variety of evaluations needed by the UK AISI — which has hundreds of evaluations spanning QA, cybersecurity CTF, and more.

## Core Architecture

Inspect is built around three core components:

### Dataset
- Inputs and optional targets (correct answers, grading rubrics, or validation functions)
- Standard fields (`input`) plus custom fields for specific evals
- Supports CSV, message histories, and replaying past logs

### Solvers
The pipeline that executes the eval — the **heart of the framework**. Solvers transform task state (message history + model output) in useful ways:

| Solver | Description |
|--------|-------------|
| `prompt_template` | Transform prompt through a template with metadata |
| `generate` | Call the model to generate (source code is ~3 lines) |
| `chain_of_thought` | Basic CoT template |
| `multiple_choice` | Shuffle choices → generate → unshuffle |
| `self_critique` | Run critique on completion, append to history, re-generate |
| Custom | Write your own — anything that transforms task state |

Solvers can be composed into pipelines or used as standalone "boss of everything" patterns. External solver packages (e.g., jailbreak solvers from UK AISI's internal `Shepherd` package) can be plugged in.

### Scorers
Evaluate the final output:

| Scorer | Description |
|--------|-------------|
| Pattern matching | Regex, template matching, answer extraction |
| Model-graded | LLM-as-judge with customizable templates |
| Expression equivalence | Few-shot model assessment for math expressions |
| Human | No automated score — human grading |
| Custom | Any Python function |

> **Critical principle:** Rigorously evaluate model-graded scores against human baselines. Don't deploy LLM judges without grounding them.

## Key Design Decisions

### Python Code First
Inspect is not super opinionated. By conforming to simple conventions, your existing code works inside the pipeline with minimal lift. The Honeycomb eval example reused Hamel Husain's existing course code almost verbatim.

### Composition Over Prescription
The framework expects people to write Python packages with scores and solvers that can be mixed and matchable. This enables an ecosystem of:
- Prompt engineering technique packages
- Jailbreaking solver packages
- Critique/debate packages
- Model-graded scoring variations

### Local Development → Production Scale
- **Development**: Interactive notebooks, REPL, exploratory iteration
- **Production**: CLI (`inspect eval`), eval suites, CI integration, S3 log storage
- Parameterized tasks allow external driver programs to vary inputs

### Tool Use and Agent Support
Task state includes **tools** — Python functions made available to the model via docstrings. This bridges into agent evaluation:
- Simple tool use (web search, Wikipedia)
- Bespoke agent loops (cybersecurity CTF)
- External agent framework integration (LangChain agents wrapped as solvers)

### Reproducibility
If run from a git repository, the log file is a **unit of reproducibility** — read the log, get origin/commit, clone, and re-run. Models are non-deterministic so results differ, but all input parameters are preserved.

## Model Support

Uses a `provider/model-name` convention where the provider prefix determines the API:
- `openai/gpt-4-turbo` — OpenAI models
- `hf/meta-llama/Llama-2-70b` — Any HuggingFace model
- `ollama/...` — Local models via Ollama (Metal/Mac GPU support)
- `together/...` — Together AI models
- Custom base URLs for vLLM, LM proxies (LiteLLM)
- Custom model providers can be created and published as packages

Model names are **opaque** — passed through without resolution. New models work immediately.

## Tooling

- **Log viewer**: Rich exploration of everything that happened during an eval — message histories, tool use, scoring explanations, per-sample drill-down
- **VS Code extension**: Tweak evals, run different models
- **Log API**: Rich Python object + JSON with published JSON schema + TypeScript types
- **Quarto slides**: The presentation itself was built with Quarto

## Development Team

- **Core team**: 2-3 people working full-time (JJ Allaire + 1-2 others)
- **Contributors**: Many UK AISI researchers providing PRs and design feedback
- **Not a Posit project** — exists in a parallel universe from JJ's Posit/RStudio work

## Ecosystem

Inspect is designed to be extended through:
- Custom solver packages (prompt engineering, jailbreaking, critique)
- Custom scorer packages (model-graded variations)
- Agent framework bridges (LangChain, etc.)
- Tool execution environments (Docker-based, coming 2024)

### Planned Integrations
- **Weights & Biases**: On short list (iframe log viewer + log projection into W&B affordances)
- **Tool execution environments**: Formal Docker/docker-compose support
- **Expanded metrics**: MRR and other ranking metrics
- **Annotation**: Shared viewing and annotation capabilities

## Relationship to Other Tools

> *Not to be confused with [[entities/inspect|Ramp's Inspect]] — a background coding agent at Ramp.*

Inspect AI occupies the **evaluation/harness engineering** space alongside:
- [[concepts/evaluation/llm-as-judge]] — Inspect supports model-graded scoring
- [[concepts/harness-engineering]] — Inspect embodies the principle that eval tooling is fundamental
- Promptfoo, LangSmith, Braintrust — but Inspect is more framework than platform

## Sources

- JJ Allaire, "Inspect: An OSS Framework for LLM Evals," Hamel Husain's AI Evals course, Jan 14, 2024
- [Inspect AI GitHub](https://github.com/UK-AISI/inspect_ai)
- [Inspect AI Documentation](https://inspect.ai-safety-institute.org.uk/)
