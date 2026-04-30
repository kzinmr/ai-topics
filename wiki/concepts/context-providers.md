---
title: "Context Providers — The Missing Layer Between Agents and Tools"
type: concept
created: 2026-04-30
updated: 2026-04-30
tags: [agent-architecture, context-management, tool-use, multi-agent, subagents]
sources:
  - raw/articles/2026-context-providers-the-missing-layer-between-agents-and-tools.md
related:
  - concepts/mcp
  - concepts/subagents
  - concepts/agent-sandboxing
  - concepts/agent-skills
  - concepts/context-engineering
---

# Context Providers — The Missing Layer Between Agents and Tools

The **Context Provider** pattern introduces a thin abstraction layer between agents and tools, solving three critical walls that emerge when agents use multiple tool sources:

1. **Context pollution** from too many tools
2. **Degrading performance** from overlapping scopes
3. **Main agent forgets its job** because context is all tool instructions

## The Three Walls

### Wall 1: Context Pollution
Every tool takes up precious context — schemas, descriptions, example usage. A Slack toolkit is 8-12 tools, Gmail is 6-10, Calendar another 6. You're at 50 tools before adding anything custom. Past 20, models start hallucinating tools or calling them with wrong shapes.

### Wall 2: Blurry Scopes Don't Compose
Two tools both take a `workspace` argument: one is Slack's, one is Google's. Search in one MCP collides with search in another. `send_message` could be Slack, email, or CRM. The agent picks wrong half the time.

### Wall 3: Tool-Use Logic Lives with Main Agent
The system prompt becomes the union of every API's quirks. Every turn carries every rule, even when the user just asked about Slack. Adding a source means editing the prompt and praying nothing else regresses.

## The Context Provider Pattern

```
# Traditional: Agent ← Tools (or Agent ← MCP Server ← Tools)
# Context Provider: Agent ↔ ContextProvider

# Each ContextProvider wraps one source (Slack, FileSystem, Drive)
# To the agent, it exposes exactly TWO tools:
#   query_<source>(question) — natural-language reads
#   update_<source>(instruction) — natural-language writes
```

Behind each provider is a **sub-agent** scoped to that one source. The sub-agent owns:
- The source's tools
- The source's quirks (pagination, ID resolution, etc.)
- The lookup-before-write patterns
- Returns clean results to the main agent

### Adding 10 Sources = Linear Growth
The main agent's tool surface stays at max 2N (query_X + update_X per source). Add ten sources, still only 20 tools — not 200.

## Relationship to Skills

| Aspect | Skills | Context Providers |
|---|---|---|
| **Purpose** | Compress task knowledge | Hide tool complexity |
| **Loading** | Conditional (when relevant) | Always available as query/update |
| **Scope** | Task-specific instructions | Source-specific abstraction |
| **Composition** | Can conflict when loading multiple | Compose cleanly (each isolated) |

**Better together**: A Slack Context Provider's sub-agent can load a Slack skill — skills do their best work in the context of the thing actually executing against the source, not the main agent.

## Key Findings

1. **Sub-agents are cheaper than expected**: Main agent's smaller context means faster, better calls. Sub-agents only fire on turns that touch their source. Total tokens are roughly flat at low source counts and improve as source count grows.

2. **Wall-clock latency drops** at every source count measured.

3. **GPT-5.4 works out of the box** with zero guidance on how to use a source — the uniform interface "just works."

4. **Composition works**: Two providers can read each other in the same turn (query_slack + query_drive), main agent writes synthesis.

5. **Adding a source is one line**, removing is one line. Swapping backend (Exa → Parallel) stays inside the provider.

## Open Questions
- **Caching across calls**: Same query shouldn't redo work two turns later
- **Per-user auth that survives the hop**: Partially solved (user_id, session_id, metadata passed through)
- **When to expose underlying tools**: Small sources may benefit from direct tool driving

## Implementation Examples
- **Filesystem** (00), **Database** (04), **Slack** (05), **Google Drive** (07), **GitHub** (12), **Web via Exa/Parallel** (01, 02, 03, 11)
- **MCP wrapper** (06): Collapses a 50-tool MCP server to 1 tool from main agent's view
- **Read/write split** (04): Separate sub-agents with separate engines for DB read vs write

## See Also
- [[concepts/mcp]]
- [[concepts/subagents]]
- [[concepts/agent-skills]]
- [[concepts/context-engineering]]
- [[concepts/multi-agent-orchestration]]