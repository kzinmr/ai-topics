---
title: RAW.works - RLMs are the New Reasoning Models
category: other
status: active
---

# RAW.works - RLMs are the New Reasoning Models

**Source:** [raw.works](https://raw.works/rlms-are-the-new-reasoning-models/) | April 20, 2026

---

## Core Definition: What is an RLM?

A **Recursive Language Model (RLM)** is an inference paradigm where a language model treats its input prompt as an **environment** rather than a fixed string.

> "The root LM is given a REPL in which the prompt is bound to a variable it can inspect, slice, and partition programmatically. When it decides a region is worth a closer look, it issues a recursive subcall — to itself or another LM — over that slice and incorporates the result."

**Key insight:** Context itself becomes the object of computation. RLMs collapse reasoning and tool use into a single inference abstraction.

**Critical capability:** Input size is no longer a hard ceiling on computation. RLMs can process inputs **up to two orders of magnitude** beyond the underlying model's context window.

---

## The Big Picture

RLMs represent the direct marriage of two important axes of model capability:
- **Reasoning** — how well a model allocates inference-time compute
- **Tool use** — whether a model can call external functions, search, calculate, or interact

This is more radical than it first sounds. The model treats its own prompt as an environment it can inspect, slice, and recursively query.

---

## History: Reasoning & Tool Use Timeline

### 2022: Reasoning First (Mostly Without Tools)

| Paper | Contribution |
|-------|-------------|
| [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903) | Intermediate reasoning steps dramatically improve multi-step reasoning |
| [Self-Consistency](https://arxiv.org/abs/2203.11171) | Sampling multiple reasoning paths, selecting most consistent answer |

**Key lesson:** A large share of "reasoning" gains come from spending more inference-time compute on the same prompt, not just from adding more knowledge.

### Late 2022: First Bridge Between Reasoning and Acting

| Paper | Contribution |
|-------|-------------|
| [ReAct](https://arxiv.org/abs/2210.03629) | Model alternates between reasoning traces and external actions (retrieval, environment interaction) |

ReAct framed tool use not as a one-off API call, but as a **loop** where reasoning selects actions and tool outputs reshape the next reasoning step.

### 2023: Tool Use Becomes an API Discipline

| Paper/Event | Contribution |
|-------------|-------------|
| [Toolformer](https://arxiv.org/abs/2302.04761) | Models learn when to call tools, which tools, and how to incorporate results |
| OpenAI Function Calling (June 2023) | Standardized function-calling interfaces; made structured tool invocation reliable |

This improved tool-use reliability faster than it improved deep reasoning.

### 2023: Deepening the Separation

| Paper | Contribution |
|-------|-------------|
| [Tree of Thoughts](https://arxiv.org/abs/2305.10601) | Models explore multiple candidate thought branches, look ahead, and backtrack — search over reasoning traces without requiring tools |

### 2024: Reasoning Models Become Their Own Product Category

| Event | Significance |
|-------|-------------|
| OpenAI o1 launch | Models designed to "spend more time thinking before they respond" |
| o1 API announcement | Explicitly noted function calling was not yet included |

Strong evidence that reasoning and tool use were still **separable** at the product level.

### 2024: Agentic Tool Use Gets Serious

- **Claude 3.5 Sonnet** — emphasized stronger tool use for coding and agentic tasks
- **Anthropic Computer Use** — model interacting with real computer via screenshots, mouse, and keyboard

### Late 2024–2025: Tool Use as Native (Still Distinct from Thinking)

- **Google Gemini 2.0** — framed around "agentic era" and native tool use, while keeping "thinking" as distinct capability

> "That split mirrors the real architecture: one layer governs deliberation, another governs interaction with external affordances."

**RLMs are the abstraction where that split finally collapses.**

---

## Recent RLM Results: Three Failure Modes

The arc moves through three successive failure modes of the single forward pass:

| Failure Mode | Benchmark | What It Tests |
|--------------|-----------|---------------|
| **Long Context** | [Oolong](https://arxiv.org/abs/2511.02817) | Analyze many local chunks, aggregate into global answer |
| **Memory** | [LongMemEval](https://arxiv.org/abs/2410.10813) | Long-term interactive memory over sustained chat histories |
| **Long Reasoning** | [LongCoT](https://arxiv.org/abs/2604.14140) | Long-horizon chain-of-thought reasoning |

### Key Results Timeline

#### October 2025: Original Public RLM Write-up

[Recursive Language Models](https://alexzhang13.github.io/blog/2025/rlm/) by Alex Zhang:

- GPT-5-mini RLM **beats GPT-5 by more than 2×** on Oolong split while being cheaper per query
- Beats ReAct + test-time indexing/retrieval on long-context research task
- Does not visibly degrade even at 10× the original context length

#### January 2026: o3-mini and Reasoning Budgets

- OpenAI o3-mini showed that giving models more time to think solves harder problems
- Cost scales with inference-time compute in a predictable way

#### April 2026: RLM + DSPy Breakthrough Results

See [RLMs are SOTA on LongCoT](https://raw.works/rlms-are-sota-on-longcot/) for full benchmark details.

Key results:
- **Qwen3-8B + dspy.RLM**: 0% → 6.5% on LongCoT-Mini (from literally zero correct to #7 on leaderboard)
- **Qwen3.5-9B + dspy.RLM**: 17.2% → **15.69% SOTA** on LongCoT-Full (1.6× GPT-5.2)
- **Qwen3.5-27B + dspy.RLM**: **22.18%** — new LongCoT king, more than double GPT-5.2

---

## RLM Architecture: Key Concepts

### The Prompt-as-Environment Model

In standard LLM inference, the prompt is a static string. In RLM inference:

1. The prompt is **bound to a variable** the model can inspect
2. The model can **slice** regions of the prompt programmatically
3. The model can **partition** the prompt into sub-regions
4. The model issues **recursive subcalls** over those slices
5. Results are incorporated back into the main context

### Recursive Subcall Mechanism

```
Root LM
  └─ sees prompt as variable P
  └─ inspects P → identifies region R
  └─ issues subcall(R) → Sub LM
  └─ incorporates result → continues
```

### DSPy.RLM

[DSPy.RLM](https://dspy.ai/api/modules/RLM/) is the reference implementation for RLM scaffolding in the [DSPy](https://dspy.ai/) framework. It provides:

- Prompt introspection and slicing
- Recursive subcall orchestration
- Result incorporation

---

## Related Concepts

- [[recursive-language-model]] — RLM
- [[raw/articles/raw-works-rlms-sota-on-longcot-2026-04-19.md]] — Long Chain-of-Thought benchmark
- [[dspy]] — DSPy framework
- [[reasoning-models]] — Reasoning models product category
- [[chain-of-thought]] — CoT prompting
- [[concepts/harness-engineering/system-architecture/advanced-tool-use.md]] — Tool use in LLMs

---

## Source

- Article: [RLMs are the New Reasoning Models](https://raw.works/rlms-are-the-new-reasoning-models/) (raw.works, April 20, 2026)
- Author: Raymond Weitekamp ([@raw_works](https://twitter.com/raw_works))
- Related: [RLMs are SOTA on LongCoT](https://raw.works/rlms-are-sota-on-longcot/)