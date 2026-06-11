---
title: "Advanced Tool Use"
type: concept
aliases:
  - advanced-tool-use
  - tool-search-tool
  - programmatic-tool-calling
created: 2026-04-12
updated: 2026-05-26
tags:
  - concept
  - architecture
  - harness-engineering
  - anthropic
  - mcp
status: draft
sources:
  - "https://www.anthropic.com/engineering/advanced-tool-use/"
---

# Advanced Tool Use

Three new features released by Anthropic on the Claude Developer Platform that enable large-scale tool use.

## Problem Statement

> "The future of AI agents is one where models work seamlessly across hundreds or thousands of tools."

Traditional tool calling faces the following problems at scale:
- **Context starvation**: Pre-loading all MCP definitions consumes 50K-134K+ tokens before the first request
- **Reasoning overhead**: Each tool call requires a full model pass. Intermediate results pollute the context
- **Schema limits**: JSON defines structure but cannot define usage conventions, parameter correlations, or format expectations

## Three New Features

### 1. Tool Search Tool

**Problem**: Context inflation and incorrect tool selection in large libraries

**How it works**:
- Exclude tools from initial context with `"defer_loading": true`
- Claude discovers relevant tools on-demand using search tools (regex, BM25, custom embeddings)
- Only matched tools are expanded into context. Prompt cache is maintained.

**Implementation example**:
```json
{
  "tools": [
    {"type": "tool_search_tool_regex_20251119", "name": "tool_search_tool_regex"},
    {
      "name": "github.createPullRequest",
      "description": "Create a pull request",
      "input_schema": {...},
      "defer_loading": true
    }
  ]
}
```

**MCP server configuration**:
```json
{
  "type": "mcp_toolset",
  "mcp_server_name": "google-drive",
  "default_config": {"defer_loading": true},
  "configs": {
    "search_files": {"defer_loading": false}
  }
}
```

**Effectiveness**:
- 85% reduction in context consumption (191,300 tokens vs 122,800 tokens for traditional approach)
- Significant accuracy improvement in MCP evaluations with large tool libraries (notable with Opus 4)

**When to use**:
| ✅ Best for | ❌ Not needed |
|---|---|
| Tool definitions exceeding 10K tokens | Fewer than 10 tools or compact definitions |
| Accuracy issues with similar tool names | All tools are used every session |
| Multi-server MCP architecture | |

### 2. Programmatic Tool Calling (PTC)

**Problem**: Context pollution from intermediate results and reasoning latency

**How it works**:
- Claude writes Python orchestration code and executes it instead of sequential API calls
- Code executes in a sandboxed `code_execution` environment
- Tool results are processed programmatically; **only the final output** enters Claude's context

**Orchestration example**:
```python
team = await get_team_members("engineering")
levels = list(set(m["level"] for m in team))
budget_results = await asyncio.gather(*[
    get_budget_by_level(level) for level in levels
])
budgets = {level: budget for level, budget in zip(levels, budget_results)}
expenses = await asyncio.gather(*[
    get_expenses(m["id"], "Q3") for m in team
])
exceeded = []
for member, exp in zip(team, expenses):
    budget = budgets[member["level"]]
    total = sum(e["amount"] for e in exp)
    if total > budget["travel_limit"]:
        exceeded.append({"name": member["name"], "spent": total, "limit": budget["travel_limit"]})
print(json.dumps(exceeded))
```

**API flow**:
1. Opt-in: `"allowed_callers": ["code_execution_20250825"]`
2. Claude returns `server_tool_use` and code blocks
3. API executes the code, pauses at tool calls, returns results to sandbox
4. Only the final `code_execution_tool_result` (stdout) enters Claude's context

**Effectiveness**:
- 200KB raw data → 1KB result reduction
- Token consumption: 43,588 → 27,297 tokens (37% reduction)
- Latency: Eliminates each API round-trip (hundreds of ms to seconds)

**When to use**:
| ✅ Best for | ❌ Not needed |
|---|---|
| Large datasets needing aggregation/summary | Simple single-tool calls |
| 3+ dependent tool calls | Tasks needing intermediate reasoning |
| Filtering, sorting, parallel operations | Simple searches with small responses |

### 3. Tool Use Examples

**Problem**: JSON schema ambiguity and incorrect parameter usage

**How it works**:
- Add `"input_examples"` array to tool definitions showing actual usage patterns
- Teaches format conventions, nested structure patterns, and parameter correlations

**Implementation example**:
```json
{
  "name": "create_ticket",
  "input_schema": {...},
  "input_examples": [
    {
      "title": "Login page returns 500 error",
      "priority": "critical",
      "labels": ["bug", "authentication", "production"],
      "reporter": {"id": "USR-12345", "name": "Jane Smith", "contact": {"email": "jane@acme.com", "phone": "+1-555-0123"}},
      "due_date": "2024-11-06",
      "escalation": {"level": 2, "notify_manager": true, "sla_hours": 4}
    },
    {"title": "Add dark mode support", "labels": ["feature-request", "ui"], "reporter": {"id": "USR-67890", "name": "Alex Chen"}},
    {"title": "Update API documentation"}
  ]
}
```

**Effectiveness**:
- Internal testing enables constructions previously impossible with traditional tool-use patterns
- Claude for Excel uses PTC to read/modify thousands of spreadsheet rows without overloading the context window

**When to use**:
| ✅ Best for | ❌ Not needed |
|---|---|
| Complex nested structures | Simple tools with single parameters |
| Many optional parameters with usage patterns | Standard formats (URLs, emails) |
| Domain-specific conventions or similar tools | Validation better handled by schema constraints |

## Strategic Best Practices

1. **Layer by bottleneck**: Start with features solving primary constraints, then combine
   - Context inflation → Tool Search Tool
   - Intermediate result pollution → Programmatic Tool Calling
   - Schema ambiguity → Tool Use Examples
2. **Gradual adoption**: Don't introduce everything at once; add as problems arise
3. **Evaluation-based improvement**: Measure each feature's effectiveness and adjust as needed

## Related Concepts

- [[concepts/harness-engineering]] — Parent index
- [[concepts/writing-tools-for-agents]] — Five principles of agent tool design
- [[concepts/context-engineering|Context Engineering]] — Context engineering
