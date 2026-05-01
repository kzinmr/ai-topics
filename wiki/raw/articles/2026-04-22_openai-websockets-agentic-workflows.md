---
title: "Speeding up agentic workflows with WebSockets in the Responses API"
source: "https://openai.com/index/speeding-up-agentic-workflows-with-websockets/"
date: 2026-04-22
author: OpenAI
tags: [openai, agentic-workflows, websockets, api, performance, codex]
---

# Speeding up agentic workflows with WebSockets in the Responses API

**Source:** OpenAI
**Date:** April 22, 2026
**Key Achievement:** 40% reduction in end-to-end agentic cycle latency, enabling speeds up to 1,000+ tokens per second (TPS).

## 1. The Problem: API Overhead as a Bottleneck
As model inference speeds increased (moving from GPT-5 to GPT-5.3-Codex-Spark), the traditional synchronous HTTP API structure became a bottleneck. Agentic workflows—which require multiple "round trips" to execute tools and process results—spent more time on API service overhead than on actual GPU inference.

### Key Performance Stats:
- **Previous Baseline:** GPT-5 and GPT-5.2 operated at ~65 TPS.
- **New Target:** 1,000+ TPS for GPT-5.3-Codex-Spark (using Cerebras hardware).
- **The Issue:** Structural overhead from treating every request as independent, forcing the API to re-process the entire conversation history and state for every follow-up call.

## 2. Technical Solution: Persistent WebSocket Connections
OpenAI transitioned from a series of synchronous HTTP calls to a persistent WebSocket transport. This allows the server to maintain an in-memory cache of the conversation state for the duration of the connection.

### Why WebSockets?
- **Simplicity:** It is a message-based protocol that didn't require changing API input/output formats.
- **Efficiency:** Eliminates redundant work by sending only new information that requires validation.
- **State Retention:** The server caches the previous `response` object, input/output elements, tool definitions, and pre-rendered tokens.

### The "Tool Call" Analogy:
> "In our design... instead of calling a remote service, we sent the model's tool call back to the client over the WebSocket. When the client responded, we appended the client's tool response to the context and continued sampling."

## 3. Implementation Details
To maintain developer familiarity, OpenAI avoided a complete rewrite of the API interaction mode.

- **`previous_response_id`:** Developers use this parameter in a `response.create` call to resume context from a previous state.
- **Incremental Processing:** Safety classifiers and request validators now only process *new* inputs rather than the full history.
- **Task Overlapping:** Non-blocking post-inference tasks (like billing) are now performed in parallel with subsequent requests.

## 4. Real-World Impact & Benchmarks
The transition to WebSockets resulted in immediate, measurable speed gains across the developer ecosystem:

| Platform | Latency Improvement |
| :--- | :--- |
| **General Agentic Workflows** | ~40% faster |
| **Vercel AI SDK** | Up to 40% faster |
| **Cline (Multi-file workflows)** | 39% faster |
| **Cursor** | Up to 30% faster |

### Peak Performance:
> "For GPT‑5.3‑Codex‑Spark, we hit our goal of 1000 TPS and saw bursts as high as 4000 TPS, proving that the Chat API could keep up with much faster inference under real-world production traffic."

## 5. Summary of Key Optimizations
1. **Token Caching:** Rendered tokens and model configurations are cached to avoid repeated tokenization.
2. **Network Hop Reduction:** Eliminated intermediate service calls (e.g., image processing resolution) to call the inference service directly.
3. **Security Stack Upgrades:** Faster execution of classifiers to flag conversations without delaying the first token.
4. **Asyncio Integration:** The API blocks asynchronously during tool execution and resumes immediately upon receiving a `response.append` event from the client.
