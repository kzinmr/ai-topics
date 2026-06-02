# Introducing Advanced Tool Use on the Claude Developer Platform

**Source:** Anthropic Engineering Blog
**URL:** https://www.anthropic.com/engineering/advanced-tool-use
**Date:** November 24, 2025
**Authors:** Bin Wu, Adam Jones, Artur Renault, Henry Tay, Jake Noble, Noah Picard, Sam Jiang (Claude Developer Platform team)

## Summary

Three new beta features for Claude Developer Platform enabling dynamic tool discovery, code-orchestrated tool invocation, and example-driven tool usage:

1. **Tool Search Tool** — on-demand tool discovery instead of loading all definitions upfront
2. **Programmatic Tool Calling (PTC)** — tools invoked via Python code in sandboxed execution environment
3. **Tool Use Examples** — concrete usage examples in tool definitions (input_examples field)

## Tool Search Tool

### Problem
MCP tool definitions consume massive tokens:
- GitHub: 35 tools (~26K tokens)
- Slack: 11 tools (~21K tokens)
- Sentry: 5 tools (~3K tokens)
- Grafana: 5 tools (~3K tokens)
- Splunk: 2 tools (~2K tokens)
- Total: 58 tools, ~55K tokens before conversation starts
- At Anthropic: saw 134K tokens consumed by tool definitions alone

Common failures: wrong tool selection, incorrect parameters (similar names like notification-send-user vs notification-send-channel).

### Solution
- Mark tools with `defer_loading: true` → not loaded into context initially
- Only Tool Search Tool (~500 tokens) loaded upfront
- Claude searches for relevant tools on-demand (regex, BM25, or custom)
- Returns references → expanded into full definitions in context
- **85% token reduction** (77K → 8.7K tokens for 50+ MCP tools)
- **Accuracy improvement**: Opus 4: 49% → 74%, Opus 4.5: 79.5% → 88.1%
- Preserves prompt caching (deferred tools excluded from initial prompt)

### MCP Server-Level Deferral
Entire MCP servers can be deferred with per-tool overrides:
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

### When to Use
- Tool definitions >10K tokens
- Tool selection accuracy issues
- MCP-powered systems with multiple servers
- 10+ tools available

## Programmatic Tool Calling (PTC)

### Problem
1. **Context pollution**: 10MB log file enters context even if only summary needed
2. **Inference overhead**: Each tool call = full model inference pass; 5 tools = 5 passes + manual synthesis

### Solution
Claude writes Python code to orchestrate tools. Code runs in Code Execution sandbox. Intermediate results never enter context.

- `code_execution_20250825` tool type
- `allowed_callers` field on tools to opt-in to programmatic execution
- Only `print()` output returns to Claude as `code_execution_tool_result`

### Results
- Token savings: 43,588 → 27,297 tokens (37% reduction on complex research)
- Knowledge retrieval: 25.6% → 28.5%
- GIA benchmarks: 46.5% → 51.2%

### Production Example
Claude for Excel uses PTC to read/modify spreadsheets with thousands of rows without overloading context.

## Tool Use Examples

### Problem
JSON Schema defines structure but NOT usage patterns:
- Format ambiguity: `due_date` as "2024-11-06" vs "Nov 6, 2024" vs ISO 8601?
- ID conventions: UUID vs "USR-12345" vs "12345"?
- Nested structure: When to populate `reporter.contact`?
- Parameter correlations: How do `escalation.level` and `sla_hours` relate to `priority`?

### Solution
`input_examples` field in tool definitions — concrete usage patterns showing:
- Format conventions (dates, IDs, labels)
- Nested structure patterns
- Optional parameter correlations (critical bugs = full escalation; features = reporter only)

```json
{
  "name": "create_ticket",
  "input_schema": {...},
  "input_examples": [
    {"title": "Login page returns 500 error", "priority": "critical", ...},
    {"title": "Add dark mode support", "labels": ["feature-request", "ui"], ...},
    {"title": "Update API documentation"}
  ]
}
```

### Results
- Complex parameter handling: 72% → 90% accuracy

### Best Practices
- Use realistic data (real city names, plausible prices, not "string")
- Show variety: minimal, partial, full specification patterns
- 1-5 examples per tool
- Focus on ambiguity (only where correct usage isn't obvious from schema)

## Layering Strategy

Start with biggest bottleneck:
1. Context bloat from tool definitions → Tool Search Tool
2. Large intermediate results → Programmatic Tool Calling
3. Parameter errors → Tool Use Examples

Complementary: Search finds tools, PTC executes efficiently, Examples ensure correct invocation.

## References
- Joel Pobar's LLMVM
- Cloudflare's Code Mode
- Code Execution as MCP
