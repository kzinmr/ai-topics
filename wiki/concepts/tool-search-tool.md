---
title: "Tool Search Tool — On-Demand Tool Discovery via Progressive Disclosure"
type: concept
created: 2026-06-02
updated: 2026-06-02
tags: [tool-use, mcp, context-engineering, token-economics, agent-harness, progressive-disclosure]
aliases: [deferred-tool-loading, on-demand-tool-discovery]
related: [concepts/advanced-tool-use, concepts/code-execution-with-mcp, concepts/code-mode, concepts/programmatic-tool-calling, concepts/context-engineering, concepts/agentic-search]
sources:
  - raw/articles/2025-11-24_anthropic_advanced-tool-use.md
  - https://www.anthropic.com/engineering/advanced-tool-use
  - raw/articles/2026-04-30_cloudflare-code-mode-mcp.md
---

# Tool Search Tool — On-Demand Tool Discovery via Progressive Disclosure

## Definition

The **Tool Search Tool** is an architectural pattern where agents discover and load tool definitions **on-demand** rather than loading all definitions upfront. Only the search tool itself (~500 tokens) is loaded initially; tools marked `defer_loading: true` are discovered via search (regex, BM25, embeddings) and expanded into the model's context only when needed.

**Coined by:** Anthropic (Nov 2025)
**Also known as:** Deferred Tool Loading, On-Demand Tool Discovery

## The Problem: Tool Definition Overload

As agents scale to hundreds of MCP servers, tool definitions consume massive context before any work begins:

| Source | Tools | Tokens |
|--------|-------|--------|
| GitHub | 35 | ~26K |
| Slack | 11 | ~21K |
| Sentry | 5 | ~3K |
| Grafana | 5 | ~3K |
| Splunk | 2 | ~2K |
| **Total** | **58** | **~55K** |

At Anthropic internal testing: **134K tokens** consumed by tool definitions alone.

Beyond cost, accuracy suffers: wrong tool selection and incorrect parameters are the most common failures, especially with similar names (`notification-send-user` vs `notification-send-channel`).

## Solution: Progressive Disclosure of Tools

```
Traditional:   [58 tool schemas (55K)] → [conversation] → model
Tool Search:   [search tool (500)] → [conversation] → model searches → [3-5 tools (3K)] → model acts
```

### Token Savings

| | Traditional | Tool Search Tool |
|---|---|---|
| Upfront | ~72K (50+ MCP tools) | ~500 (search tool only) |
| Runtime | — | ~3K (3-5 relevant tools) |
| **Total** | **~77K** | **~8.7K (88% reduction)** |

### Accuracy Improvement

| Model | Without | With Tool Search | Δ |
|-------|---------|-------------------|---|
| Opus 4 | 49% | **74%** | +25pp |
| Opus 4.5 | 79.5% | **88.1%** | +8.6pp |

### Implementation

Tools are marked with `defer_loading: true`. The search tool (regex, BM25, or custom) finds matching tools and expands their full definitions into context.

```json
{
  "tools": [
    {"type": "tool_search_tool_regex_20251119", "name": "tool_search_tool_regex"},
    {"name": "github.createPullRequest", "defer_loading": true, ...},
    {"name": "github.listIssues", "defer_loading": true, ...}
  ]
}
```

MCP servers can be deferred at server level with per-tool overrides:

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

**Prompt caching note:** Deferred tools are excluded from the initial prompt, so system prompt and core tool definitions remain cacheable.

### Search Strategies

| Strategy | Mechanism | Best For |
|----------|-----------|----------|
| Regex | Pattern matching on tool names/descriptions | Simple keyword matching |
| BM25 | Term-frequency ranking | Natural language queries |
| Custom (embeddings) | Semantic similarity | Complex intent matching |

## Position in the Progressive Disclosure Hierarchy

Tool Search Tool is one layer in a broader pattern of **progressive disclosure** for agent tool interaction:

```
Level 0: All schemas upfront (traditional)
  ↓ 55K+ tokens wasted
Level 1: Tool Search Tool (defer_loading + search)
  ↓ 85% token reduction, accuracy up
Level 2: Code Execution with MCP (filesystem navigation)
  ↓ Agent loads .ts/.py wrappers as needed
Level 3: Skills persistence (save & reuse tool patterns)
  ↓ Agent accumulates reusable workflows
Level 4: Tool Use Examples (semantic conventions in schema)
    Schema defines structure; examples define usage patterns
```

## When to Use

| ✅ Use | ❌ Skip |
|--------|---------|
| Tool definitions >10K tokens | Small tool library (<10 tools) |
| Tool selection accuracy issues | All tools used every session |
| Multiple MCP servers | Compact tool definitions |
| 10+ tools available | |

## Design Principles

1. **Keep 3-5 most-used tools always loaded** — balance immediate access for common ops with on-demand discovery
2. **Clear, descriptive tool names/descriptions** — search matches against these
3. **System prompt guidance** — tell the model what tool categories are available ("You have access to Slack, GitHub, Jira, and Google Drive tools. Use tool search to find specific capabilities.")
4. **Layer with PTC** — Tool Search finds the right tools; PTC executes them efficiently

## Related Concepts

- [[concepts/advanced-tool-use]] — Anthropic's three-feature framework (Search + PTC + Examples)
- [[concepts/code-execution-with-mcp]] — Filesystem-based progressive disclosure (deeper level)
- [[concepts/programmatic-tool-calling]] — Efficient tool execution via code
- [[concepts/context-engineering]] — Broader context management strategy
- [[concepts/agentic-search]] — Search-as-code applies same progressive principle to retrieval
