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

| Category | Recommended Models | Notes |
|----------|-------------------|-------|
| **Primary Agent** | GPT 4.1, DeepSeek V3, Claude Sonnet, Gemini 2.5 Pro | Prioritize tool-use reliability over raw intelligence |
| **Helper (cheap)** | GPT 4.1 Mini/Nano, Gemini Flash, Haiku, Mistral Small 3.1, Qwen | For bulk processing, LLM-as-judge, synthetic data |
| **Reasoner (surgical)** | Claude Opus, DeepSeek R1 | Use sparingly for hard problems; high latency in multi-tool pipelines |
| **Open (fine-tunable)** | Qwen (0.6B–200B+), Gemma 3 (2B–27B), Mistral Small 3.1 | Permissive licensing for training on outputs |

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
