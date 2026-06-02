---
title: "Writing Effective Tools for Agents"
type: concept
created: 2026-06-02
updated: 2026-06-02
tags:
  - tool-use
  - ai-agent-engineering
  - context-engineering
  - agent-evaluation
  - mcp
  - agent-ergonomics
  - prompting
sources:
  - raw/articles/2026-05-08_anthropic-engineering_writing-tools-for-agents.md
  - https://www.anthropic.com/engineering/writing-tools-for-agents
related:
  - concepts/advanced-tool-use
  - concepts/context-engineering
  - concepts/evals-for-ai-agents
  - concepts/agent-skills
status: active
---

# Writing Effective Tools for Agents

Tools are a new kind of software: a **contract between deterministic systems and non-deterministic agents**. Traditional API design targets predictable callers — `getWeather("NYC")` always behaves the same way. Agents, by contrast, may call a tool, answer from general knowledge, ask a clarifying question, or even hallucinate a call entirely. This demands rethinking tool design from first principles.

> "Tools that are most 'ergonomic' for agents also end up being surprisingly intuitive to grasp as humans."
> — Anthropic Engineering

This page distills the principles and process Anthropic described for maximizing agent tool effectiveness, based on internal evaluations across Slack, Asana, and other production tool suites.

## Core Principles

### 1. Choose the Right Tools (and Not to Implement)

More tools do not equal better outcomes. A common mistake is wrapping every API endpoint as a tool, regardless of whether agents can use it effectively.

**The address book analogy**: A traditional program can iterate through all contacts efficiently. An LLM agent receiving a full list must read every token — wasting limited context on irrelevant information. The better approach is a `search_contacts` tool that returns only matches, not a `list_contacts` dump.

**Consolidation over fragmentation**: Tools can absorb multiple discrete operations:

| Instead of | Consider |
|---|---|
| `list_users` + `list_events` + `create_event` | `schedule_event` (finds availability and schedules) |
| `read_logs` | `search_logs` (returns only relevant lines + context) |
| `get_customer_by_id` + `list_transactions` + `list_notes` | `get_customer_context` (compiles all relevant info) |

Each tool should have a **clear, distinct purpose** that mirrors how a human would subdivide the task. This simultaneously reduces the number of tool descriptions loaded into context and offloads computation from the agent's reasoning into the tool calls themselves.

### 2. Namespace Your Tools

Agents may have access to dozens of MCP servers and hundreds of tools. When tools overlap in function or have vague names, agents get confused about which to use.

**Namespacing** groups related tools under common prefixes, delineating boundaries:

- By service: `asana_search`, `jira_search`
- By resource: `asana_projects_search`, `asana_users_search`

The choice between prefix- and suffix-based namespacing has **non-trivial effects** on tool-use evaluations and varies by LLM. Anthropic encourages selecting a naming scheme based on your own evaluation results.

### 3. Return Meaningful Context

Tool implementations should return only **high-signal information**. Prioritize contextual relevance over flexibility.

- **Use natural language identifiers**: Resolving arbitrary UUIDs to human-readable names (or even 0-indexed IDs) significantly improves retrieval precision and reduces hallucinations.
- **Prefer semantic fields**: `name`, `image_url`, `file_type` over `uuid`, `256px_image_url`, `mime_type`.

#### The ResponseFormat Enum Pattern

When agents need both human-readable and technical identifiers (e.g., for chaining tool calls), expose a `response_format` parameter:

```python
enum ResponseFormat {
    DETAILED = "detailed"   # includes IDs, metadata (~206 tokens)
    CONCISE = "concise"     # content only (~72 tokens)
}
```

This is especially valuable for tools like Slack, where `thread_ts` and `channel_id` are needed for downstream calls but shouldn't clutter every response. Concise responses used roughly **one-third the tokens** of detailed ones in Anthropic's testing.

Response structure format (XML, JSON, Markdown) also affects performance — there is no one-size-fits-all. LLMs tend to perform better with formats matching their training data.

### 4. Optimize for Token Efficiency

Quality of context matters, but so does **quantity**. Implement combinations of:

- **Pagination**: Return results in pages rather than all at once
- **Range selection**: Let agents request specific subsets
- **Filtering**: Accept query parameters to narrow results
- **Truncation**: With sensible defaults (Claude Code caps tool responses at 25K tokens)

When truncating, include **helpful instructions** that steer agents toward more efficient strategies (e.g., "use filters or pagination for more results"). Similarly, when tool calls raise errors, provide **actionable error messages** — not opaque error codes or tracebacks.

### 5. Prompt-Engineer Tool Descriptions

Tool descriptions and specs are loaded into the agent's context and collectively shape tool-calling behavior. This is one of the **most effective methods** for improving tool use.

**Think of onboarding a new hire**: What implicit context would they need? Specialized query formats, niche terminology definitions, relationships between resources — make it explicit.

Key guidelines:
- **Unambiguous parameter names**: `user_id` instead of `user`
- **Clear input/output schemas**: Enforced with strict data models
- **Concrete examples**: Show expected usage patterns

Small refinements to tool descriptions can yield dramatic improvements — Claude Sonnet 3.5 achieved state-of-the-art on SWE-bench Verified after precise description refinements that reduced error rates.

## Development Process

### Step 1: Build a Prototype

Stand up a quick prototype and test it hands-on. For MCP servers, connect locally:
```
claude mcp add <name> <command> [args...]
```

Use LLM-friendly documentation (e.g., `llms.txt` files) when building tools with agents like Claude Code. Test yourself to identify rough edges, and collect user feedback to build intuition around expected use cases.

### Step 2: Run an Evaluation

Generate evaluation tasks grounded in **real-world uses** with realistic data sources. Avoid overly simplistic sandbox environments.

**Strong tasks** require multiple tool calls and realistic complexity:
> "Schedule a meeting with Jane next week to discuss our latest Acme Corp project. Attach the notes from our last project planning meeting and reserve a conference room."

**Weak tasks** are too narrow:
> "Schedule a meeting with jane@acme.corp next week."

Run evaluations programmatically with direct LLM API calls in simple agentic loops. Instruct evaluation agents to output reasoning and feedback blocks **before** tool calls to trigger chain-of-thought behaviors. Track metrics including runtime, tool call count, token consumption, and tool errors.

Use **held-out test sets** to prevent overfitting to training evaluations.

### Step 3: Collaborate with Agents to Improve

Let agents analyze evaluation transcripts and refactor tools automatically. Paste concatenated evaluation transcripts into Claude Code — it excels at analyzing transcripts and ensuring tool consistency across changes.

**Read between the lines**: What agents omit in their feedback can be more important than what they include. Observe where agents get confused, review raw transcripts, and analyze tool-calling metrics for patterns (e.g., redundant calls suggest pagination issues, frequent invalid parameters suggest unclear descriptions).

## Comparison: Tool Design for Developers vs. Agents

| Dimension | Traditional API Design | Agent Tool Design |
|---|---|---|
| **Caller behavior** | Deterministic, predictable | Non-deterministic, exploratory |
| **Error handling** | Structured error codes | Actionable natural language messages |
| **Granularity** | Fine-grained (one operation per call) | Coarse-grained (consolidated workflows) |
| **Response format** | Fixed schema | Flexible (detailed vs. concise) |
| **Documentation** | Reference docs for developers | Descriptions that steer agent behavior |
| **Naming** | Developer conventions | Agent-friendly namespaces |
| **Success metric** | Correctness | Token efficiency + task completion |

## Relationship to Context Engineering

Effective tool design is a core component of [[concepts/context-engineering|context engineering]]. Tool definitions consume context budget, tool responses populate the context window, and tool descriptions steer agent reasoning. The principles above — returning meaningful context, optimizing for token efficiency, namespace clarity — all serve the broader goal of curating the optimal set of tokens for each inference step.

The [[concepts/advanced-tool-use|Advanced Tool Use]] features (Tool Search Tool, Programmatic Tool Calling) complement these design principles by addressing the platform-level challenge of managing hundreds of tools at scale.

## See Also

- [[concepts/advanced-tool-use]] — Anthropic platform features for scaling tool use (Tool Search, Programmatic Calling)
- [[concepts/context-engineering]] — Context management strategies for agents
- [[concepts/evals-for-ai-agents]] — Systematic agent evaluation methodology
- [[concepts/agent-skills]] — Open standard for domain-specific agent capabilities
