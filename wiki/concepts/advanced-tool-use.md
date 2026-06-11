---
title: "Advanced Tool Use (Claude Developer Platform)"
type: concept
created: 2026-04-25
updated: 2026-05-08
tags:
  - tool
  - mcp
  - context-engineering
  - developer-tooling
aliases:
  - programmatic tool calling
  - Tool Search Tool
  - deferred tool loading
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_advanced-tool-use.md
  - raw/articles/2025-11-24_anthropic_advanced-tool-use.md
  - https://www.anthropic.com/engineering/advanced-tool-use
related:
  - concepts/tool-search-tool
  - concepts/tool-use-examples
  - concepts/programmatic-tool-calling
  - concepts/code-execution-with-mcp
  - concepts/mcp
  - concepts/context-engineering
---

# Advanced Tool Use (Claude Developer Platform)

Three advanced tool-use features released by Anthropic in March 2026. Foundation for agents handling hundreds to thousands of tools.

## Three New Features

| Feature | Problem | Solution |
|------|------|--------|
| **Tool Search Tool** | All tool definitions loaded into context (58 tools = 55K tokens) | On-demand discovery (~500 tokens, only search tool upfront) |
| **Programmatic Tool Calling** | Natural language tool calls = per-reasoning pass + intermediate results accumulating in context | Tool calls from code execution environment |
| **Tool Use Examples** | JSON schemas only show structural validity, not usage patterns | Universal standard for showing effective tool usage examples |

## Tool Search Tool

See [[concepts/tool-search-tool]] for full treatment.

### Token Savings

| | Before | Tool Search Tool |
|---|---|---|
| Upfront Tokens | ~72K (50+ MCP tools) | ~500 (search tool only) |
| Runtime Tokens | — | ~3K (3-5 relevant tools) |
| Total Consumption | ~77K (before conversation starts) | **~8.7K (95% reduction)** |

### Accuracy Improvement

| Model | Before | Tool Search Tool |
|--------|------|-----------------|
| Opus 4 | 49% | **74%** (+25pp) |
| Opus 4.5 | 79.5% | **88.1%** (+8.6pp) |

### How It Works

```json
{
  "tools": [
    {"type": "tool_search_tool_regex_20251119", "name": "tool_search_tool_regex"},
    {"name": "github.createPullRequest", "defer_loading": true, ...}
  ]
}
```

- `defer_loading: true` → Not initially loaded into context
- Claude searches only when needed → expands only relevant tools
- Prompt Caching remains intact (deferred tools excluded from initial prompt)

### When to Use
- ✅ Tool definitions >10K tokens / Tool selection accuracy issues / Multiple MCP servers / 10+ tools
- ❌ Small tool libraries / All tools always used / Compact definitions

## Programmatic Tool Calling

### Two Problems It Solves

1. **Context Pollution**: 10MB log analysis → entire file enters context (only the summary is needed)
2. **Inference Overhead**: Loop iterations, conditionals, and data transformations each require an inference pass

### How It Works
- Tool calls from within a sandboxed Python REPL
- Process results with code (filtering, aggregation, transformation) → only final results injected into context
- Example: Claude for Excel — Manipulate thousands of spreadsheet rows without context overload

## Tool Use Examples

```json
{
  "name": "search_customers",
  "examples": [
    {
      "description": "Search by email domain",
      "input": {"query": "@example.com", "field": "email"},
      "output": {"customers": [{"id": 123, "name": "ACME Corp"}]}
    }
  ]
}
```

- Conveys usage patterns, optional parameter best practices, and API conventions that JSON schemas alone cannot express

## See Also

- [[concepts/code-execution-with-mcp]] — Code execution with MCP
- [[concepts/mcp]] — Model Context Protocol
- [[concepts/context-engineering|Context Engineering]] — Context engineering for AI agents
- [[tool-use-tax]] — Tool calling performance overhead
