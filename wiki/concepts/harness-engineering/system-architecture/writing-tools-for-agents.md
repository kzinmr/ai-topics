---
title: "Writing Effective Tools for AI Agents"
type: concept
aliases:
  - writing-tools-for-agents
  - tool-design-principles
  - mcp-tool-design
  - agent-tool-ergonomics
created: 2026-04-12
updated: 2026-05-26
tags:
  - concept
  - architecture
  - harness-engineering
  - anthropic
  - mcp
  - tool
status: draft
related:
  - "[[concepts/writing-tools-for-agents]]"
  - "[[concepts/harness-engineering]]"
  - "[[concepts/building-effective-agents]]"
  - "[[concepts/harness-engineering/system-architecture/advanced-tool-use]]"
  - "[[concepts/harness-engineering/system-architecture/code-execution-with-mcp]]"
  - "[[concepts/evals-skills]]"
sources:
  - "https://www.anthropic.com/engineering/writing-tools-for-agents"
  - "raw/articles/2026-05-08_anthropic-engineering_writing-tools-for-agents.md"
---
# Writing Effective Tools for AI Agents

> **Canonical page promoted.** This subdirectory page was promoted to [[concepts/writing-tools-for-agents]] for broader discoverability. Key content retained below; see the canonical page for the comprehensive "Design for Agent" paradigm framing.

Tool design methodology for AI agents, as practiced by Anthropic. The approach is to "write tools for agents, and use agents to optimize tools."

## Core Philosophy

> "Instead of writing tools and MCP servers the way we'd write functions and APIs for other developers or systems, we need to design them for agents."

> "Tools optimized for agent context limits and reasoning patterns are often more intuitive for human developers as well."

**A different design philosophy is needed compared to traditional software development: agents are non-deterministic, prone to hallucinations, and can misinterpret specifications. Design must accommodate agent context constraints and reasoning patterns.**

## Iterative Development Workflow

### 1. Build Prototypes Quickly
- Provide LLM-friendly documentation via `llms.txt` files
- Wrap tools with local MCP server or Desktop Extension (DXT)
- Claude Code: `claude mcp add [args...]`
- Claude Desktop: `Settings > Developer/Extensions`
- Identify rough edges through manual testing. Refine use cases through actual user feedback

### 2. Build and Run Evaluations
- **Task design**: Based on real-world complexity. Avoid superficial sandboxes. Robust tasks require dozens of tool calls
- **Validation**: Flexible matching (allow format/punctuation variations). Avoid overfitting to a single strategy
- **Execution**: Simple agent loop (alternating between LLM API calls and tool invocations in a while loop)
- **CoT triggers**: Output reasoning/feedback before tool calls. Inter-task

### 3. Automated Optimization with Agents
- Paste evaluation transcripts into Claude Code for automatic tool refactoring, inconsistency fixes, and description improvements
- Validate improvements on holdout test sets (prevent overfitting to training evaluations)

> "Most of the advice in this post came from repeatedly optimizing our internal tool implementations with Claude Code."

## Five Principles of Tool Design

### 1. Choose the Right Tools

> More tools ≠ better performance.

| ❌ Bad Example | ✅ Good Example |
|---|---|
| `list_contacts`, `list_users`, `create_event` | `search_contacts`, `schedule_event`, `get_customer_context` |

- Integrate multi-step workflows
- Avoid raw data dumps that waste context
- Focus on high-impact tools

### 2. Design Namespaces Strategically

- Group by service/resource (e.g., `asana_search`, `jira_search`)
- Reduce context load and prevent tool confusion
- **Prefix vs suffix naming affects LLMs differently** — test empirically

### 3. Return Meaningful Context

> Resolving cryptic IDs to human-readable formats significantly reduces hallucinations.

| ❌ Low Signal | ✅ High Signal |
|---|---|
| `uuid`, `mime_type` | `name`, `image_url` |

- Prioritize semantic fields over technical IDs
- Resolving cryptic IDs to human-readable formats significantly reduces hallucinations

### 4. Optimize Token Efficiency

> Claude Code defaults to a 25,000-token response cap.

- Implement pagination, filtering, and truncation with sensible defaults
- **Concise mode**: Maintain essential information at ~1/3 the tokens
- **Detailed mode**: Only retrieve technical IDs needed for downstream calls

```python
enum ResponseFormat {
   DETAILED = "detailed",
   CONCISE = "concise"
}
```

### 5. Engineer Descriptions as Prompts

> The most effective optimization lever.

- Write as if onboarding a new hire: make implicit context explicit
- Use strict data models
- Name parameters clearly (`user_id` > `user`)
- **Small adjustments yield dramatic results** (e.g., SOTA results on SWE-bench Verified)

## Real-World Fix Examples

### Web Search Bias Fix
- **Problem**: Claude always added `2025` to web search queries, biasing results
- **Fix**: Resolved by improving only the tool description

### Error Response Design
- Instead of opaque tracebacks, provide clear, actionable guidance that steers agents toward token-efficient strategies
- Example: Suggest using filters instead of broad searches

## Evaluation Tactics

### Robust Tasks vs Weak Tasks

| ✅ Robust (complex, multi-step) | ❌ Weak (overly simple) |
|---|---|
| `"Schedule a meeting with Jane for next week... attach notes... book the room"` | `"Schedule a meeting with jane@acme.corp for next week"` |
| `"Customer ID 9182 reports triple billing... find the logs... check if others are affected"` | `"Check customer 9182's billing"` |

### Evaluation Metrics
- Top-level accuracy
- Execution time
- Number of tool calls
- Token consumption
- Error rate

### Pattern Diagnosis
| Pattern | Diagnosis | Fix |
|---|---|---|
| Redundant calls | Adjust pagination/token limits |
| Parameter errors | Improve descriptions/examples |
| Missing agent feedback | May be more useful than explicit output |

## Related Concepts

- [[concepts/harness-engineering]] — Parent index
- [[concepts/harness-engineering/system-architecture/advanced-tool-use]] — Advanced tool use
- [[concepts/building-effective-agents]] — Fundamentals of agent building
- [[concepts/harness-engineering/system-architecture/code-execution-with-mcp]] — Code execution with MCP
- [[concepts/evals-skills]] — Evaluation skills
