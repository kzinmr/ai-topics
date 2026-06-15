---
title: "Inspect AI"
created: 2026-06-15
updated: 2026-06-15
type: entity
tags: [product, framework, open-source, evaluation, evals, llm-as-judge, agent-evaluation, agent-framework, sandbox, python, ai-safety, mcp]
sources:
  - transcripts/2024-01-14_jjallaire_inspect-ai-eval-framework.md
  - https://github.com/UKGovernmentBEIS/inspect_ai
  - https://inspect.aisi.org.uk/
  - https://hamel.dev/notes/llm/evals/inspect.html
---

# Inspect AI

| | |
|---|---|
| **Type** | Open-source LLM evaluation framework |
| **Author** | [[entities/jj-allaire\|JJ Allaire]] |
| **Organization** | UK AI Safety Institute (UK AISI) + Meridian Labs |
| **Language** | Python (`pip install inspect-ai`) |
| **Version** | v0.3.239 (June 9, 2026) — 239 releases since May 2024 |
| **GitHub** | [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai) |
| **Docs** | [inspect.aisi.org.uk](https://inspect.aisi.org.uk/) |
| **Evals** | 200+ pre-built evaluations |
| **Contributors** | 100+ external contributors |
| **Adopters** | UK AISI, Anthropic, DeepMind, Grok |

## Overview

**Inspect AI** is an open-source Python framework for LLM evaluation developed by [[entities/jj-allaire|JJ Allaire]] in collaboration with the **UK AI Safety Institute** and **Meridian Labs**. It is the framework of choice for many of the largest AI labs including Anthropic, DeepMind, and Grok, and is used for nearly all of UK AISI's automated evaluations.

Inspect supports a broad range of evaluations measuring coding, agentic tasks, reasoning, knowledge, behavior, and multi-modal understanding. It is designed to be Python-code-first, composable, and extensible — conforming to simple conventions gives you access to a big pipeline of tools and an ecosystem of related packages.

> *Not to be confused with [[entities/inspect|Ramp's Inspect]] — a background coding agent at Ramp.*

## Core Architecture

Inspect is built around three core components (Dataset → Solver → Scorer):

### Dataset
- Inputs and optional targets (correct answers, grading rubrics, or validation functions)
- Standard fields (`input`, `target`) plus custom fields via `FieldSpec` or `record_to_sample()`
- Sources: HuggingFace (`hf_dataset()`), CSV, JSON, in-memory lists, message histories
- Declarative field mapping: `FieldSpec(input="problem", target="answer")`

### Solvers
The pipeline that executes the eval — the **heart of the framework**. Solvers transform `TaskState` (message history + model output) in useful ways:

| Solver | Description |
|--------|-------------|
| `generate()` | Call the model to generate — handles tool-call loops automatically |
| `prompt_template()` | Transform prompt through a template with metadata |
| `system_message()` | Set the system prompt |
| `chain_of_thought()` | Basic CoT template |
| `multiple_choice()` | Format choices → generate (single-token) → unshuffle |
| `self_critique()` | Generate → critique → append critique → re-generate |
| `use_tools()` | Make tools available to the model |
| Custom | Write your own — anything that transforms task state |

Solvers are Python functions (sync or async) that take `TaskState` and return `TaskState`. They can be composed into pipelines (`plan=[system_message(), generate()]`) or used as standalone agents.

### Scorers
Evaluate the final output:

| Scorer | Description |
|--------|-------------|
| `match()` | Exact string matching |
| `includes()` | Target appears in output |
| `choice()` | Multiple choice correctness |
| `model_graded_fact()` | LLM judges if response matches target |
| `model_graded_qa()` | LLM judges QA quality |
| `expression_equivalence()` | Model judges math equivalence (few-shot) |
| `@scorer` decorator | Custom scorer with `accuracy()`, `stderr()` metrics |
| Human | No automated score — human grading |

> **Critical principle:** Rigorously evaluate model-graded scores against human baselines. Don't deploy LLM judges without grounding them.

## Agent System (Post-2024 Evolution)

Inspect has evolved from basic tool use into a comprehensive agent evaluation framework:

### Built-in Agents
- **`react()`**: General-purpose ReAct agent — reason-act-observe loop with tool calling, retry support, `submit()` for final answer. The baseline architecture for agent evals.
- **Deep Agent**: For long-horizon tasks with subagent delegation, memory, and planning.
- **Human Agent**: Enables human baselining of computing tasks.

### Agent Primitives
Agents use a narrower interface than solvers, making them more versatile. A single agent can be:
1. Used as a top-level Solver for a task
2. Run standalone via `run()`
3. Delegated to via `as_tool()` or `handoff()` in multi-agent architectures
4. Provided as a standard Tool to a model

**Multi-agent support**: `handoff()` forwards entire conversation history between agents; `as_tool()` provides string-in/string-out interface.

### Agent Bridge
Bridges external agent frameworks into Inspect by monkey-patching OpenAI API calls:

| Framework | Bridge Type |
|-----------|------------|
| OpenAI Agents SDK | `agent_bridge()` — Python, same process |
| Pydantic AI | `agent_bridge()` — Python, same process |
| LangChain | `agent_bridge()` — Python, same process |
| Claude Code | `sandbox_agent_bridge()` — runs in Docker sandbox |
| Codex CLI | `sandbox_agent_bridge()` — runs in Docker sandbox |
| Gemini CLI | `sandbox_agent_bridge()` — runs in Docker sandbox |

The bridge intercepts API calls with `model="inspect"`, routes them to the current Inspect model provider, and logs the entire interaction. Works with OpenAI Completions, OpenAI Responses, Anthropic, and Google APIs.

**Bridged Tools**: Host-side Inspect tools can be exposed as MCP tools to sandboxed agents via `BridgedToolsSpec`.

### Inspect SWE Package
The separate `inspect-swe` package (`pip install inspect-swe`) provides drop-in coding agents:
```python
from inspect_swe import claude_code, codex_cli, gemini_cli
# Use as solver:
solver=claude_code()
```

## Built-in Tools

Inspect provides 6 pre-built agent tools for evaluations:

| Tool | Description |
|------|-------------|
| `bash()` | Execute shell commands in sandbox |
| `python()` | Execute Python code in sandbox |
| `text_editor()` | Edit files (view, create, modify) |
| `web_search()` | Search the web |
| `web_browser()` | Headless Chromium browser interaction |
| `computer()` | Desktop interaction via screenshots |
| `think()` | Explicit reasoning output |
| `todo_write()` | Task tracking for agents |
| `submit()` | Agent signals task completion |

Custom tools use the `@tool` decorator with type annotations and docstrings (required for model instruction).

## Sandboxing

A critical feature for safety evaluations. `SandboxEnvironment` abstraction isolates tool code execution:

| Backend | Description |
|---------|-------------|
| Docker | Per-task Dockerfile or compose.yaml |
| Kubernetes | K8s pod isolation |
| Modal | Modal cloud sandboxes |
| Proxmox | VM-level isolation |
| Local | Same filesystem (only if outer sandbox exists) |
| Extension API | Custom sandbox implementations |

Set per-task: `sandbox="docker"` in the `Task` definition.

## Scanning (inspect-scout)

Post-run **scanners** review completed transcripts to surface issues:

```python
from inspect_scout import Scanner, Transcript, llm_scanner, scanner

@scanner(messages="all")
def refusal() -> Scanner[Transcript]:
    return llm_scanner(
        question="Did the assistant refuse to answer?",
        answer="boolean",
    )
```

Run with: `inspect eval task.py --scanner refusals.py`

Supports boolean, numeric, string, classification, and structured answers.

## Model Support

20+ built-in model providers via `provider/model-name` convention:

| Provider | Example |
|----------|---------|
| OpenAI | `openai/gpt-5`, `openai/gpt-4o` |
| Anthropic | `anthropic/claude-sonnet-4-0` |
| Google | `google/gemini-2.5-pro` |
| HuggingFace | `hf/meta-llama/Llama-2-7b-chat-hf` |
| Ollama | `ollama/...` (local, Metal/Mac GPU) |
| Together AI | `together/...` |
| vLLM | via OpenAI-compatible API |
| SGLang | via OpenAI-compatible API |
| LiteLLM | proxy |
| Custom | `model-base-url` or custom provider package |

**Advanced features:**
- **Concurrency**: `max_connections` for API parallelism, `max_subprocesses` for Docker
- **Caching**: Reuse model calls across runs
- **Compaction**: Automatic context window management
- **Fallbacks**: Model fallback chains on refusal/error
- **Batch mode**: Provider-native batch APIs
- **Multimodal**: Image, audio, video inputs
- **Reasoning**: `reasoning_effort`, `reasoning_tokens` controls
- **Structured output**: JSON schema response format

## Production Features

### Eval Sets
```python
from inspect_ai import eval_set
success, logs = eval_set(
    tasks=[task1(), task2()],
    model=["openai/gpt-5", "anthropic/claude-sonnet-4-6"],
    log_dir="logs/run-1",
)
```
Automatic retries, resumption from last checkpoint, failure thresholds.

### Logging & Analysis
- **EvalLog**: Structured Python object + JSON with published JSON schema + TypeScript types
- **Log viewer** (`inspect view`): Web-based UI for exploring results, message histories, tool use, scoring explanations
- **`inspect view bundle`**: Creates standalone static website for sharing results (e.g., GitHub Pages)
- **DataFrames**: `samples_df()`, `evals_df()` for Pandas-based analysis
- **VS Code Extension**: Embedded log viewer, run/debug evals from IDE

### Limits
- Message limits, token limits, time limits, cost limits per eval
- `message_limit=30` in Task definition

### Control Channel
`inspect eval` / `inspect eval-set` bind a per-process control server (AF_UNIX) exposing live run observation. `inspect ctl` commands let other processes observe running evals.

## Design Philosophy

### Two API Levels
1. **High-level (declarative)**: `@task` decorator, `Task(dataset=..., solver=..., scorer=...)`
2. **Low-level (async Python)**: Full control over message management, tool calling loops, state

### Composition Over Prescription
Custom solvers and scorers packaged as standard Python packages, easily shared and reused. Examples: UK AISI's `Shepherd` jailbreak solver package, custom critique packages.

### Reproducibility
If run from a git repository, the log file is a **unit of reproducibility** — read the log, get origin/commit, clone, and re-run.

### LLM-Friendly Docs
Inspect provides `llms.txt` (~2k tokens index), `llms-guide.txt` (~185k tokens full), and per-page Copy Page buttons for LLM assistance.

## Development Team

- **Organization**: UK AI Safety Institute + Meridian Labs (JJ Allaire's new lab)
- **Core team**: 2-3 people full-time
- **Contributors**: 100+ external contributors
- **Release cadence**: Near-daily releases (239 versions in ~2 years)
- **Not a Posit project** — separate from JJ's Posit/RStudio work

## Ecosystem & Extensions

| Package | Description |
|---------|-------------|
| `inspect-ai` | Core framework |
| `inspect-swe` | Coding agents (Claude Code, Codex CLI, Gemini CLI) |
| `inspect-scout` | Transcript scanning (refusals, eval awareness) |
| `inspect_evals` | 200+ pre-built benchmark implementations |
| VS Code Extension | Authoring, debugging, log viewing |
| Extensions Gallery | Community packages for sandboxes, models, etc. |

## Relationship to Evaluation Ecosystem

Inspect AI occupies the **evaluation/harness engineering** space:
- [[concepts/evaluation/llm-as-judge]] — Inspect supports model-graded scoring natively
- [[concepts/harness-engineering]] — Inspect embodies the principle that eval tooling is fundamental
- vs. Promptfoo, LangSmith, Braintrust — Inspect is a framework (code-first, OSS) rather than a platform (UI-first, SaaS)
- vs. [[concepts/evaluation/eval-frameworks]] — Inspect is the research/safety-oriented choice, adopted by major AI labs

## Sources

- JJ Allaire, "Inspect: An OSS Framework for LLM Evals," Hamel Husain's AI Evals course, Jan 14, 2024
- Hamel Husain, ["Inspect AI, An OSS Python Library For LLM Evals"](https://hamel.dev/notes/llm/evals/inspect.html), June 23, 2025 — annotated presentation with video
- [Inspect AI Documentation](https://inspect.aisi.org.uk/) — current as of v0.3.239
- [Inspect AI Changelog](https://inspect.aisi.org.uk/CHANGELOG.html) — 239 releases
- [Inspect AI GitHub](https://github.com/UKGovernmentBEIS/inspect_ai)
- [Inspect SWE](https://meridianlabs-ai.github.io/inspect_swe/) — coding agent bridges
