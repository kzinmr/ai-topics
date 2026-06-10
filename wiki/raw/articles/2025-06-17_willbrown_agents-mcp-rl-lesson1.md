---
title: "Production-Ready Agent Engineering — Lesson 1: Agent Patterns and Principles"
author: Will Brown
date: 2025-06-17
date_ingested: 2026-06-10
source: https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
type: lecture-summary
tags:
  - ai-agents
  - reinforcement-learning
  - tool-calling
  - context-engineering
  - education
---

# Production-Ready Agent Engineering — Lesson 1: Agent Patterns and Principles

**Instructor:** Will Brown (Research Lead, [[entities/prime-intellect]])
**Date:** June 17, 2025
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
**Lecture transcript:** [[transcripts/2025-06-17_willbrown_agents-mcp-rl-agent-patterns-lecture|Agent Patterns and Principles (Lecture Transcript)]]
**Notebook:** [agent_patterns.ipynb](https://github.com/willccbb/agent-engineering/blob/main/lectures-1-through-4/lec1-agent-patterns/agent_patterns.ipynb)

## Summary

The inaugural lecture establishes the course's central thesis: **RL and agents are two sides of the same coin**, yet practitioners in each field rarely engage with the other. The lecture covers foundational concepts needed for building production agents: model selection, tool calling patterns, structured outputs, and multi-turn state management.

## Key Topics

### 1. Model Ecosystem Recommendations

#### Primary Agent Models

| Model | Strengths | Notes |
|-------|-----------|-------|
| **DeepSeek V3-0324** | Cheap, reliable, solid all-around (comparable to Sonnet 3.5 / GPT-4o) | Not a "reasoner" by default but works with `<think>` prompting (trained on R1 data). Free + automatic prefix caching via deepseek.ai. Available from many providers (Bedrock, Azure Foundry, Together, Fireworks, OpenRouter). **No restrictions on distillation/training.** |
| **GPT 4.1** | More "agentic" / less "chatty" than GPT-4o | Good default for capable non-reasoner, especially in OpenAI-centric workflows |
| **Claude 4 Sonnet** | Very strong all-around agentic model | Popular in code editors (Cursor, Windsurf, Claude Code). Configurable thinking budgets. |
| **Gemini 2.5 Pro** | Very strong all-around agentic model | Configurable thinking budgets. Popular alongside Sonnet. |

**Selection principle:** Prioritize tool-use reliability over raw intelligence. *"Most of what you care about is having a model that is very good at being an LLM. More so than a model that has all the answers to every question in the universe."*

#### Helper Models (cheap, bulk processing)

| Model | Notes |
|-------|-------|
| **GPT 4.1 Mini / Nano** | Good default helpers for OpenAI users |
| **Gemini 2.5 Flash** | Google's fast/cheap option |
| **Claude 3.5 Haiku** | Anthropic's fast/cheap option |
| **Mistral Small 3.1 (24B)** | Very permissive license; popular as a finetuning base. *"If you were going to pick only one open model to do everything with, that's a pretty good one."* |
| **Qwen 2.5/3** | Many variants + sizes (0.6B–200B+). Popular for finetuning + self-hosting. Qwen3 models are "thinking optional." |
| **Gemma 3** | Mini/open versions of Gemini (2B–27B). Good model suite for scaling experiments. |
| **Llama 3.1 8B** | Still perfectly fine as a small helper; widely hosted by inference providers |
| **Phi-4** | Non-reasoning small model; decent for simple helper methods |

#### Reasoner Models (use surgically)

| Model | Notes |
|-------|-------|
| **o3, o4-mini** | Generally slow, expensive, prone to overthinking. Often overkill if you require low latency + many tool calls. *o4-mini supports the RFT API for reinforcement learning.* |
| **DeepSeek R1** | Good for hard reasoning tasks; not for primary agent use |
| **Claude 4 Opus** | One of the strongest models ever made, but very expensive |
| **Llama 4 (Scout / Maverick)** | Fast inference + multimodal + openly available + fairly strong. Lots of RAM needed for self-hosting; similar license to Llama models. |

> *"In the context of an agent pipeline, you want to be very surgical with using reasoner models, because they will add a lot of latency. And if you're doing things that involve many tool calls, some of these models are not very good at managing context or not thinking too much."*

### 2. Tool Calling & Structured Outputs

- **Chat Completions > Responses API** — portable across providers (OpenAI, DeepSeek, Gemini, Claude all support it); Responses API is OpenAI-only
  - ⚠️ *As of GPT-5+, OpenAI has shifted to Responses API as primary; Completions support may be incomplete for newer models. Portability argument still holds for non-OpenAI providers.*
- **Pydantic for structured outputs** — typed schemas ensure reliable parsing
- **Thinking-first ordering** — chain of thought fields must precede action fields in schema (transformers are autoregressive; planning must happen before execution)
- **Outlines & XGrammar** — token-level constrained decoding backends for self-hosted models (vLLM, SGLang)
- **Literal types** — use `Literal["celsius", "fahrenheit"]` for guaranteed field validation

### 3. Multi-Turn State Management

- Agents vs chatbots: multi-turn interaction is what makes something an agent
- State management: maintain a message list, append user/assistant/tool messages as conversation progresses
- Without state, the model is just a language model in a vacuum with no pointer to the conversation

### 4. Evals Philosophy

- "The best eval is your own eval" — build task-specific evaluation, don't rely solely on public benchmarks
- LLMs are ML models; they work best in-distribution
- Making benchmarks is not hard; the course will practice creating custom evals frequently
- BFCL v3 multi-turn: the standard multi-turn tool calling benchmark
- Claude's Pokemon: a surprisingly good agent capability test

### 5. Agent Patterns (from notebook)

- **ReAct** (Reasoning + Acting) — seminal pattern for interleaving thinking and tool use; multiple flavors covered
- **Doc Search Agent** — ChromaDB-backed retrieval agent with tool calling
- **Instructor library** — structured outputs via Pydantic for non-OpenAI providers (DeepInfra etc.)
- **XML-based tool parsing** — using verifiers library for XML-formatted tool calls
- **Self-hosted structured outputs** — vLLM + SGLang with Outlines / XGrammar backends

### 6. Course Logistics

- UV package manager recommended (faster than pip, better dependency resolution)
- Python 3.11–3.13 recommended
- DeepSeek V3: cheap, permissive for training on outputs
- Week 1: APIs, evaluations, concepts (no GPUs needed)
- Week 2+: training experiments with RL
- Compute credits coming for all students

## Related

- [[concepts/agents-mcp-rl-course]] — Course portal page
- [[entities/will-brown]] — Instructor profile
- [[concepts/agentic-rl]] — RL for agents paradigm
- [[concepts/context-engineering]] — Agent context design
- [[concepts/grpo-rl-training]] — Key RL algorithm (covered in later lessons)
