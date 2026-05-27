---
title: "Unrolling the Codex agent loop"
source_url: "https://openai.com/index/unrolling-the-codex-agent-loop/"
source_type: "blog-post"
author: "Michael Bolin"
publication: "OpenAI Engineering Blog"
date: "2026-01-23"
tags: ["codex", "openai", "agent-loop", "coding-agents", "developer-tooling"]
---

# Unrolling the Codex agent loop

*By Michael Bolin, Member of the Technical Staff, OpenAI — January 23, 2026*

This is the first post in an ongoing series exploring how Codex works under the hood. The focus: the **agent loop** — the core logic orchestrating interaction between user, model, and tools.

## The Agent Loop

A repeating cycle:

```
User Input → Model Inference → Tool Call? → Execute Tool → Append Output → Repeat → Final Response
```

- Each cycle is a turn. A thread contains multiple turns.
- The loop is **stateless**: every API call sends the full conversation history (no `previous_response_id`).

## Prompt Construction

Codex builds each Responses API request with three main fields:

| Field | Content |
|-------|---------|
| `instructions` | Model-specific or custom instructions from `config.toml` |
| `tools` | Shell, plan, web search (API-provided), MCP server tools |
| `input` | Ordered list: sandbox permissions → developer instructions → skills context → environment context → user message |

### Message Role Hierarchy (decreasing priority)
```
system > developer > user > assistant
```

Static content (instructions, tools) first → variable content (user message) last — maximizes prefix matching for prompt caching.

## Prompt Caching & Prefix Matching

- Cache hits require **exact prefix matches** between requests
- Codex ensures new turns only **append** items, never modify earlier ones
- Makes sampling cost **linear** rather than quadratic over the conversation

**Cache miss triggers:**
- Tools change order (MCP `tools/list_changed`)
- Model switched mid-conversation
- Sandbox config, approval mode, or working directory modified

## Context Window Management & Compaction

When tokens exceed `auto_compact_limit`, Codex calls the `/responses/compact` endpoint. Returns a smaller list with a `type=compaction` item containing `encrypted_content` — preserves the model's latent understanding while freeing context window space.

Earlier versions required manual `/compact` command.

## Tool Integration

| Tool | Purpose | Safety |
|------|---------|--------|
| Shell tool | Spawn local processes | Sandboxed |
| `update_plan` | Built-in task planning | N/A |
| `web_search` | API-provided web search | Cached by default |
| MCP server tools | User-configured custom tools | MCP server handles safety |

MCP tools must be enumerated in deterministic order to avoid cache misses.

## Key Design Decisions

1. **Stateless by design**: no `previous_response_id` — every call carries full history. Simplifies provider architecture, enables Zero Data Retention.
2. **Append-only prompt construction**: preserves prefix match for caching; quadratic growth mitigated by compaction.
3. **Automatic compaction over manual**: seamless user experience at the cost of opaque encrypted state.

## Bugs & Lessons

- MCP tools were initially enumerated inconsistently (ordering variations broke caching)
- Prompt construction bugs: bad truncation, tool call accumulation causing context exhaustion
