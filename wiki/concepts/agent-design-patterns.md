---
title: Agent Design Patterns
type: concept
created: 2026-06-11
updated: 2026-06-11
tags:
  - ai-agents
  - agent-design-patterns
  - tool-calling
  - ai-agent-engineering
  - structured-outputs
  - context-engineering
sources:
  - raw/articles/2025-06-17_willbrown_agents-mcp-rl-lesson1
  - transcripts/2025-06-17_willbrown_agents-mcp-rl-agent-patterns-lecture
  - raw/articles/2025-06-10_willbrown_build-your-own-research-agent-lightning
---

# Agent Design Patterns

Practical patterns and principles for building effective AI agents, drawn from the [[concepts/agents-mcp-rl-course]] curriculum. These patterns address model selection, tool calling, state management, delegation, and concurrency — the core engineering concerns that determine whether an agent works reliably in production.

## Model Selection Framework

A 3-tier model strategy avoids overpaying for tasks that don't require top-tier models.

### Tier 1 — Primary Models
These handle the main reasoning and orchestration loop:
- **DeepSeek V3** — strong cost-to-capability ratio for everyday agent work
- **GPT-4.1** — reliable tool caller with broad capability
- **Claude Sonnet** — strong instruction following and tool use
- **Gemini 2.5 Pro** — large context window, good multimodal support

**Key insight:** Prioritize tool-use reliability over raw intelligence. A model that scores slightly lower on benchmarks but calls tools correctly every time will outperform a "smarter" model that occasionally hallucinates tool parameters.

### Tier 2 — Helper / Sub-Models
Lightweight models used for bulk reading, extraction, and summarization:
- **GPT-4.1 Mini** — fast, cheap, sufficient for structured extraction tasks
- Use these when you need to process many documents or fields without paying primary-model prices

### Tier 3 — Reasoner Models
Reserved for complex, multi-step planning or tasks requiring extended chain-of-thought. Used sparingly due to latency and cost.

## Tool Calling Patterns

### Pydantic Structured Outputs
Use Pydantic models to define expected output schemas. This gives you type safety at the boundary between the LLM and your code — invalid outputs fail fast with clear errors rather than silently propagating bad data.

### Thinking-First Ordering
Autoregressive models generate tokens left-to-right. Place "thinking" tokens (scratchpad reasoning, planning) **before** tool call tokens in the output. This lets the model reason about what tool to call and with what arguments before committing to the call, improving reliability.

### Chat Completions API over Responses API
The Chat Completions API (messages array) is recommended over the newer Responses API for portability. It works identically across OpenAI, Anthropic, Google, and open-weight model serving, making it easier to swap models without rewriting agent logic.

### Tool Schema Design
In tool/function schemas, **descriptions matter more than parameter names**. Models read descriptions to understand intent — invest in clear, example-rich descriptions rather than clever parameter naming.

## Multi-Turn State Management

### Message Array Accumulation
The core agent loop maintains a growing messages array:

1. Append user message
2. Call model → get assistant response (may include tool calls)
3. If tool call: execute tool, append tool result to messages
4. Loop back to step 2
5. If no tool call: return final text response

This pattern is the backbone of every tool-using agent. The full conversation history (including tool calls and results) is sent on each turn, giving the model complete context.

### Max Turns as Safety Limit
Set a hard cap on loop iterations (typically 10–20 turns). Without this, a confused agent can loop indefinitely burning tokens. When the limit is hit, return whatever partial result exists or an error.

### Token Context Window Management
As the message array grows, it will eventually hit the model's context window. Strategies include:
- Truncating or summarizing older messages
- Dropping intermediate tool results that are no longer relevant
- Using models with larger context windows (e.g., Gemini's 1M+ tokens) for long-running agents

## Sub-Models as Tools

A powerful pattern: register a helper model as a callable tool that the main agent can invoke.

### How It Works
1. Define a tool (e.g., `extract_fields`) that internally calls a cheaper/faster model
2. The main agent delegates heavy reading/extraction to this tool
3. The sub-model returns structured results that the main agent incorporates

### V2 Agent Pattern
From the Lightning Lesson research agent, the V2 pattern evolves from a single-model agent to a multi-model architecture:
- **V1**: One model does everything (reads, reasons, writes)
- **V2**: Main agent orchestrates; sub-models handle bulk extraction tasks in parallel

This separation lets you use expensive models for planning and cheap models for reading — a significant cost reduction with no loss in quality.

## Async Processing

### asyncio.gather + Semaphores
Default concurrency pattern for production agents:

```python
semaphore = asyncio.Semaphore(10)  # limit concurrent calls

async def bounded_call(coro):
    async with semaphore:
        return await coro

results = await asyncio.gather(*[bounded_call(call_model(msg)) for msg in messages])
```

This yields approximately **7–8x speedup** over sequential processing when handling multiple independent tasks (document reading, parallel tool calls, multi-source retrieval).

### Why Async Is Essential
- Agent loops involve many I/O-bound operations (API calls, tool execution)
- Sequential processing wastes time waiting on network round trips
- Semaphores prevent rate-limit violations while still maximizing throughput
- Production agents that aren't async are simply too slow for real-world use

## Related Concepts

- [[concepts/context-engineering]] — managing what information the model sees
- [[concepts/mcp]] — the Model Context Protocol for tool interoperability
- [[concepts/grpo-rl-training]] — reinforcement learning approaches to improving agent tool use
