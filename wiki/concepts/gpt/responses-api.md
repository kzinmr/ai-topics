---
title: "OpenAI Responses API"
type: concept
created: 2026-06-02
updated: 2026-06-02
tags:
  - openai
  - developer-tooling
  - ai-agents
  - architecture
  - tool
  - state-management
  - reasoning
  - streaming
  - structured-outputs
  - multimodal
aliases: ["/v1/responses", "Responses API"]
sources:
  - raw/articles/2025-09-22_openai-developers-blog_responses-api.md
  - raw/articles/2026-03-19_openai-developers-blog_one-year-of-responses.md
related:
  - concepts/openai-agents-sdk
  - entities/openai
  - entities/codex
  - concepts/harness-engineering/system-architecture/agent-loop-orchestration
status: active
---

# OpenAI Responses API

## Overview

The Responses API (`/v1/responses`) is OpenAI's current-generation API for interacting with its models, designed as the successor to both `/v1/chat/completions` and the Assistants API. Launched in early 2025, it provides a stateful, multimodal, agentic interface purpose-built for reasoning models and multi-step agent workflows.

The API was born from a recognition that Chat Completions — while widely adopted — was fundamentally a turn-based interface that dropped reasoning state between calls. The Assistants API attempted to solve this with hosted tools but suffered from adoption-limiting design issues. Responses unifies the simplicity of Chat Completions with the power of Assistants, adding native state management, built-in hosted tools, and reasoning preservation.

Within one year of launch, the Responses API became the foundation for thousands of production agent deployments across customer support, legal, life sciences, travel, and developer tooling.

## Key Features

### Stateful Conversations

Unlike Chat Completions, the Responses API is **stateful by default**. Conversation state and tool state are tracked automatically server-side. Multi-turn workflows use `previous_response_id` to chain responses without re-sending full conversation history.

This statefulness delivers concrete benefits:
- **+5% on TAUBench** for GPT-5 compared to Chat Completions, purely from preserved reasoning
- **40–80% better cache utilization**, reducing latency and cost
- Dramatically simpler multi-turn and agentic code

### Reasoning Preservation

The API preserves the model's internal reasoning state across turns — the model's "notebook" stays open between steps. Unlike Chat Completions where reasoning is dropped between calls, Responses maintains encrypted reasoning items that allow safe continuation without exposing raw chain-of-thought.

Reasoning is preserved internally (encrypted, hidden from clients) and can be continued via `previous_response_id` or reasoning items. Summaries of reasoning are exposed for debugging without revealing the full CoT — addressing safety concerns around unaligned thoughts and competitive risks.

### Built-in Hosted Tools

The Responses API includes server-side hosted tools that execute without bouncing calls through the developer's backend:

| Tool | Description |
|------|-------------|
| **Web Search** | Real-time web information retrieval |
| **File Search** | RAG over uploaded documents |
| **Code Interpreter** | Server-side code execution |
| **Computer Use** | Screen interaction and UI automation |
| **Image Generation** | In-context image creation |
| **MCP** | Model Context Protocol tool integration |
| **Shell** | Command execution in hosted containers |

Hosted tool execution reduces latency and round-trip costs compared to client-side function calling patterns.

### Structured Outputs and Multiple Output Items

Responses can emit **multiple output items** per call — not just the model's text reply, but also tool calls, reasoning summaries, and intermediate steps. This provides "receipts" for debugging, auditing, and richer UI construction.

Output item types include `reasoning`, `message`, and `function_call`, each with typed fields and status tracking.

### Multimodal by Design

Text, images, audio, and function calls are all first-class citizens. The API was designed with multimodal inputs/outputs from the start rather than bolting modalities onto a text-only interface.

## Architecture

### Agentic Loop

The Responses API implements an agentic loop pattern: the model receives evidence, investigates, consults tools, and reports back. The loop handles:

1. **Input processing** — User messages, system instructions, prior context
2. **Reasoning** — Internal chain-of-thought (preserved, encrypted)
3. **Tool invocation** — Hosted or custom function calls
4. **State continuation** — Via `previous_response_id` for multi-turn workflows

### SDK Improvements

The API and accompanying SDK introduced several quality-of-life improvements over Chat Completions:
- **Semantic streaming events** — structured, typed stream chunks
- **Internally-tagged polymorphism** — discriminated output types
- **`output_text` helpers** — no more `choices[0].message.content` gymnastics
- **Better multimodal/reasoning parameter organization**

## Comparison with Alternatives

| Dimension | Chat Completions | Responses API | Anthropic Messages |
|-----------|-----------------|---------------|-------------------|
| **State** | Stateless (client-managed) | Stateful (server-managed) | Stateless (client-managed) |
| **Reasoning preservation** | Dropped between calls | Preserved across turns | N/A (extended thinking is client-visible) |
| **Built-in tools** | None (function calling only) | Web search, file search, code interpreter, computer use, MCP, shell | None (tool use via Messages API) |
| **Output items** | Single message | Multiple typed items | Single message |
| **Cache utilization** | Baseline | 40–80% improvement | Prompt caching available |
| **Target use case** | Simple chat | Agents, reasoning, multimodal | General-purpose chat |

Chat Completions remains supported and suitable for simple use cases. Anthropic's Messages API is stateless with no built-in hosted tools — the Responses API's server-side tool execution and state management are key differentiators.

## Production Adoption Patterns (Year One)

After one year, the Responses API enabled several production patterns:

- **Multi-agent orchestration** — Coordinating specialized agents with tool access (Hexagon's 4-agent content pipeline)
- **Monitoring and observability** — Long-running background analysis for agent failure detection (Raindrop AI)
- **Context engineering + deep reasoning** — Separating context gathering from analysis, using background jobs for long-running reasoning (Repo Prompt)
- **Conversational tool interfaces** — Chat UIs with real-time API tool calls (Collxn's Discogs integration)
- **Computer use for automation** — Screen recording analysis and demo generation (Arcade)
- **Simulation pipelines** — Daily batch generation of thousands of AI responses for brand visibility tracking (Hexagon)

Key capabilities powering production use: web search for real-time data, `user_location` for geographic simulation, `reasoning_effort` for depth control, `max_output_tokens` for length limits, and context persistence across multi-step pipelines.

## Code Example

A typical Responses API call with tool use:

```json
{
  "id": "rs_6888f6d0...",
  "output": [
    {
      "type": "reasoning",
      "summary": [{"type": "summary_text", "text": "Determining weather response..."}]
    },
    {
      "type": "message",
      "role": "assistant",
      "content": [{"type": "output_text", "text": "Let me check the weather for you."}]
    },
    {
      "type": "function_call",
      "name": "get_weather",
      "arguments": "{\"location\":\"San Francisco, CA\",\"unit\":\"f\"}",
      "call_id": "call_XOnF4B9..."
    }
  ]
}
```

## Evolution Path

```
/v1/completions (2020) → /v1/chat/completions (2022) → /v1/responses (2025)
     prompt finishing         conversational turns         agentic loops
     no tools                 function calling             hosted tools
     no state                 client-managed state         server-managed state
```

OpenAI expects Responses to become the default way developers build with its models, just as Chat Completions replaced Completions.

## Related Pages

- [[concepts/gpt/agents-sdk]] — SDK framework that uses the Responses API for agent orchestration
- [[entities/openai]] — Developer and maintainer
- [[entities/codex]] — Coding agent built on Responses API infrastructure
- [[concepts/harness-engineering/system-architecture/agent-loop-orchestration]] — General agent loop patterns that Responses implements
