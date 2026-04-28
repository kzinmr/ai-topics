---
title: "Research Agent Fundamentals"
tags: [claude-agent-sdk-research-stateless-stateful-web-search]
created: 2026-04-24
updated: 2026-04-24
type: concept
---

# Research Agent Fundamentals

Anthropic cookbook: [The One-Liner Research Agent](https://platform.claude.com/cookbook/claude-agent-sdk-00-the-one-liner-research-agent)

## Core Concept

Research tasks traditionally consume hours of expert time because **the optimal search path emerges during exploration**, not upfront. The Claude Agent SDK enables autonomous agents that adapt strategies based on discoveries, follow promising leads, synthesize conflicting sources, and know when they have enough information.

> *"The core challenge isn't finding information but knowing what to search for next based on what you just discovered."*

**Ideal Use Cases:** Competitive analysis, technical troubleshooting, investment research, literature reviews, investigative journalism.

## Two Agent Modes

### Mode 1: Stateless (`query()`)

Single-turn, independent interactions with no conversation memory.

```python
from claude_agent_sdk import ClaudeAgentOptions, query

async for msg in query(
    prompt="Research the latest trends in AI agents...",
    options=ClaudeAgentOptions(
        model="claude-opus-4-6",
        allowed_tools=["WebSearch"],
    ),
):
    print_activity(msg)
```

**When to Use:**
✅ One-off questions, parallel independent tasks, fresh context needed
❌ Multi-turn investigations, iterative refinement, sustained analysis

### Mode 2: Stateful (`ClaudeSDKClient`)

Maintains conversation memory across multiple queries.

```python
from claude_agent_sdk import ClaudeSDKClient

RESEARCH_SYSTEM_PROMPT = """You are a research agent specialized in AI.
When providing research findings:
- Always include source URLs as citations
- Format citations as markdown links
- Group sources in a 'Sources:' section at the end"""

async with ClaudeSDKClient(
    options=ClaudeAgentOptions(
        model="claude-opus-4-6",
        cwd="research_agent",
        system_prompt=RESEARCH_SYSTEM_PROMPT,
        allowed_tools=["WebSearch", "Read"],
        max_buffer_size=10 * 1024 * 1024,  # 10MB for image handling
    )
) as agent:
    # Query 1: Analyze image/chart
    await agent.query("Analyze the chart in research_agent/projects_claude.png")
    async for msg in agent.receive_response():
        messages.append(msg)

    # Query 2: Validate findings (inherits context)
    await agent.query("Based on the chart analysis, search for recent news...")
    async for msg in agent.receive_response():
        messages.append(msg)
```

**When to Use:**
✅ Multi-turn investigations, iterative refinement, multimodal analysis
❌ Simple one-off queries, parallel independent tasks

## Tool Permissions

| Permission Type | Behavior |
|---|---|
| `allowed_tools` | Claude uses freely without approval (e.g., `WebSearch`) |
| Other tools | Available but require explicit approval |
| Read-only tools | Always allowed by default (e.g., `Read`) |
| `disallowed_tools` | Completely removed from Claude's context |

## Critical: Buffer Overflow Handling

**Error:** `Fatal error in message reader: Failed to decode JSON: JSON message exceeded maximum buffer size of 1048576 bytes`

- **Cause:** Default `max_buffer_size` is 1MB. Base64-encoded images + overhead easily exceed this.
- **Fix:** Set `max_buffer_size=10*1024*1024` (10MB) in `ClaudeAgentOptions`.
- **Best Practice:** Monitor for buffer errors, use thumbnails/descriptions when possible.

## Production Module Pattern

Packaged as reusable `research_agent/agent.py`:

```python
from research_agent.agent import send_query

# Single query (stateless)
result = await send_query("What is the Claude Code SDK? Only do one web search")

# Multi-turn conversation
result1 = await send_query("What is Anthropic? Only do one web search")
result2 = await send_query("What are some of their products?", continue_conversation=True)
```

| Function | Purpose |
|----------|---------|
| `print_activity()` | Real-time console logging of agent actions |
| `get_activity_text()` | Extract activity for custom logging/monitoring |
| `send_query()` | Main entry point with built-in display control |

## Research Workflow Example

```python
# Multi-step investigation with memory
async with ClaudeSDKClient(options=...) as agent:
    # Step 1: Initial discovery
    await agent.query("Search for recent advances in AI agent orchestration...")
    
    # Step 2: Follow promising leads
    await agent.query("Based on the search results, find papers on multi-agent coordination...")
    
    # Step 3: Cross-reference
    await agent.query("Compare the approaches in papers A and B...")
    
    # Step 4: Synthesize
    await agent.query("Summarize findings with confidence levels and sources...")
```

## Key Insights

1. **Emergent Search Paths**: The optimal research strategy emerges during exploration. Agents should adapt based on discoveries, not follow rigid plans.
2. **Stateless vs Stateful**: Use `query()` for parallel, independent tasks. Use `ClaudeSDKClient` for iterative investigations where context matters.
3. **System Prompts Enforce Rigor**: Citation requirements, output formatting, and source verification should be baked into the system prompt.
4. **Buffer Management is Critical**: Default 1MB buffer overflows with images/PDFs. Set `max_buffer_size=10MB+` for multimodal research.
5. **Modular Design**: Package agents as reusable modules with `send_query()` interface for production deployment.

## Related

- [[concepts/claude-agent-sdk-sre-patterns]] — MCP integration and safety guardrails
- [[concepts/chief-of-staff-agent-patterns]] — Subagent orchestration and plan mode
- [[concepts/managed-agents-sre-incident-response]] — Human-in-the-loop approval patterns
