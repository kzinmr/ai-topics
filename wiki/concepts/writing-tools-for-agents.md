---
title: "Designing Tools for Agents"
type: concept
created: 2026-04-12
updated: 2026-06-02
tags:
  - concept
  - architecture
  - harness-engineering
  - anthropic
  - tool-use
  - agent-architecture
  - mcp
  - evaluation
  - agentic-engineering
aliases:
  - writing-tools-for-agents
  - tool-design-principles
  - agent-computer-interface
  - aci-design
  - design-for-agent
related:
  - "[[concepts/building-effective-agents]]"
  - "[[concepts/context-engineering]]"
  - "[[concepts/harness-engineering]]"
  - "[[concepts/mcp]]"
  - "[[concepts/evals-for-ai-agents]]"
  - "[[concepts/advanced-tool-use]]"
sources:
  - "https://www.anthropic.com/engineering/writing-tools-for-agents"
  - "https://www.anthropic.com/engineering/building-effective-agents"
  - "raw/articles/2026-05-08_anthropic-engineering_writing-tools-for-agents.md"
---

# Designing Tools for Agents

**Designing tools for agents** is a software design paradigm where the primary user of an API, tool, or MCP server is an AI agent rather than a human developer. Anthropic's January 2026 article "Writing Effective Tools for AI Agents" is the most complete articulation of this paradigm, but the concept extends beyond any single article — it represents a fundamental shift in how we think about software interfaces.

> "Instead of writing tools and MCP servers the way we'd write functions and APIs for other developers or systems, we need to design them for agents."
> — Anthropic Engineering

## The Paradigm Shift: From HCI to ACI

Traditional software design optimizes for **human-computer interaction (HCI)**. Developers write APIs with human ergonomics in mind: readable documentation, intuitive naming, familiar patterns. The Anthropic team coins the parallel concept of **agent-computer interaction (ACI)** — designing interfaces optimized for LLM agents.

The surprising finding: **tools optimized for agent context limits and reasoning patterns are often more intuitive for human developers as well.** The design disciplines reinforce each other rather than conflict.

### Key Differences from Traditional API Design

| Dimension | Traditional API Design | Agent Tool Design |
|-----------|----------------------|-------------------|
| **User** | Human developer reading docs | LLM processing tool descriptions token-by-token |
| **Constraint** | Cognitive load, documentation quality | Context window (finite attention budget) |
| **Error handling** | Stack traces, error codes | Actionable feedback that steers the agent |
| **Granularity** | Fine-grained CRUD operations | Coarse-grained, workflow-oriented operations |
| **Success metric** | Developer satisfaction, adoption | Task completion rate, token efficiency |
| **Iteration** | Manual testing, user feedback | Evaluation-driven, agent-assisted optimization |

## The Five Principles of Tool Design

### 1. Choose the Right Tools (Not All Tools)

> More tools ≠ better performance.

The fundamental insight: agents have different **affordances** than traditional software. An LLM processes tool responses token-by-token, so returning a list of 10,000 contacts wastes context on irrelevant information.

**Consolidate multi-step workflows into single tools:**

| ❌ Bad (API-style) | ✅ Good (Agent-style) |
|---|---|
| `list_contacts`, `list_users`, `create_event` | `search_contacts`, `schedule_event`, `get_customer_context` |
| `read_logs` (returns everything) | `search_logs` (returns relevant lines + context) |
| `get_customer_by_id`, `list_transactions`, `list_notes` | `get_customer_context` (compiles all recent info) |

Each tool should have a **clear, distinct purpose** that mirrors how a human would subdivide the task — while reducing intermediate context consumption.

### 2. Design Namespaces Strategically

When agents have access to dozens of MCP servers and hundreds of tools, **namespacing prevents tool confusion**:
- Group by service: `asana_search`, `jira_search`
- Group by resource: `asana_projects_search`, `asana_users_search`

**Non-trivial finding**: prefix vs. suffix naming affects LLMs differently. Effects vary by model — test empirically with evaluations.

### 3. Return Meaningful Context

> Resolving cryptic IDs to human-readable formats significantly reduces hallucinations.

| ❌ Low Signal | ✅ High Signal |
|---|---|
| `uuid`, `mime_type`, `256px_image_url` | `name`, `image_url`, `file_type` |

**The `response_format` pattern**: Expose an enum parameter letting agents control verbosity:
- `concise` — essential information only (~⅓ tokens)
- `detailed` — includes technical IDs needed for downstream calls

This is analogous to GraphQL's field selection — the agent chooses the granularity it needs.

### 4. Optimize Token Efficiency

Claude Code defaults to a 25,000-token response cap. Implement:
- **Pagination** with sensible defaults
- **Filtering** to reduce irrelevant results
- **Truncation** with helpful steering messages
- **Error responses** that suggest more efficient strategies

> "Error: Max tokens 500 exceeded, try summarizing first" beats "Error: 400 Bad Request" by an enormous margin.

### 5. Engineer Descriptions as Prompts

> The most effective optimization lever.

Tool descriptions are loaded into the agent's context — they collectively steer tool-calling behavior. Write descriptions as if onboarding a new hire:
- Make implicit context explicit
- Use strict data models with unambiguous parameter names (`user_id` > `user`)
- Include when to use AND when not to use the tool

**Small adjustments yield dramatic results**: Claude Sonnet 3.5 achieved SOTA on SWE-bench Verified after precise refinements to tool descriptions alone.

## Evaluation-Driven Development Workflow

The article proposes a three-stage iterative workflow that uses agents to improve their own tools:

### Stage 1: Build Prototypes
- Wrap tools in a local MCP server or Desktop Extension (DXT)
- Provide LLM-friendly documentation via `llms.txt`
- Test manually to identify rough edges

### Stage 2: Run Evaluations
- Generate tasks grounded in **real-world complexity** (not superficial sandboxes)
- Strong tasks require dozens of tool calls
- Use simple agentic loops (`while`-loops alternating LLM API + tool calls)
- Collect metrics: accuracy, runtime, tool call count, token consumption, error rate

### Stage 3: Agent-Assisted Optimization
- Paste evaluation transcripts into Claude Code for automatic refactoring
- Validate on **held-out test sets** (prevent overfitting to training evaluations)
- Iterate until performance plateaus

> "Most of the advice in this post came from repeatedly optimizing our internal tool implementations with Claude Code."

## The Broader "Design for Agent" Concept

Anthropic's article focuses on MCP tool design, but the "design for agent" paradigm extends further:

### Agent-Legible Software
[[concepts/harness-engineering|Harness Engineering]] (Ryan Lopopolo, OpenAI) generalizes this: optimize entire codebases, workflows, and organizations for agent readability. The AGENTS.md pattern, `llms.txt` files, and structured documentation are all instances of designing for agent users.

### Progressive Disclosure for Agents
Don't dump all information into the context window. Provide lightweight references; let agents load details on demand:
- **Tool definitions**: Index descriptions, retrieve on demand
- **CLI utilities**: Provide command list; agent uses `--help` for specifics
- **Skills**: YAML frontmatter in instructions; full content read only when needed

### Context Engineering as Tool Design
[[concepts/context-engineering|Context engineering]] and tool design are deeply intertwined:
- Tool definitions tax the attention budget
- Every tool description is a prompt engineering decision
- Tool responses are context that shapes future agent behavior

### Agent-Computer Interface (ACI) Design Pattern
The concept of ACI design parallels decades of HCI research but for a new user class:

```
HCI (Human-Computer Interface)          ACI (Agent-Computer Interface)
├── UX research                          ├── Evaluation-driven iteration
├── Usability testing                    ├── Agent behavior analysis
├── Progressive disclosure               ├── Token-efficient responses
├── Error messages for humans            ├── Actionable error steering
├── Documentation / tutorials            ├── Tool descriptions as prompts
└── A/B testing                          └── Held-out test set validation
```

## Relationship to the Agent Engineering Stack

```
Design for Agent (paradigm)
│
├── Tool Design for Agents (this article)
│   ├── MCP tool descriptions
│   ├── Response format design
│   └── Evaluation-driven iteration
│
├── Agent-Legible Software
│   ├── AGENTS.md pattern
│   ├── llms.txt documentation
│   └── Structured codebases
│
├── Context Engineering
│   ├── Tool definitions as context budget
│   ├── Progressive disclosure
│   └── Token efficiency
│
└── Harness Engineering
    ├── Environment design for agents
    ├── CLI design for agents
    └── Workflow design for agents
```

## Graph Structure Query

```
[writing-tools-for-agents] ──author──→ [anthropic]
[writing-tools-for-agents] ──extends──→ [building-effective-agents]
[writing-tools-for-agents] ──extends──→ [harness-engineering]
[writing-tools-for-agents] ──relates-to──→ [context-engineering]
[writing-tools-for-agents] ──relates-to──→ [mcp]
[writing-tools-for-agents] ──teaches──→ [evals-for-ai-agents]
[writing-tools-for-agents] ──embodies──→ [design-for-agent]
```

Authored by Anthropic (Ken Aizawa). Extends [[concepts/building-effective-agents]]'s ACI appendix into a full methodology. Embodies the broader "design for agent" paradigm alongside [[concepts/harness-engineering]]'s agent-legible software.

## Related Concepts

- [[concepts/building-effective-agents]] — Foundational agent patterns (ACI concept introduced here)
- [[concepts/context-engineering]] — Context window optimization (tool definitions as context budget)
- [[concepts/harness-engineering]] — Environment design philosophy (agent-legible software)
- [[concepts/mcp]] — Model Context Protocol (the tool integration standard)
- [[concepts/evals-for-ai-agents]] — Agent evaluation methodology (drives tool iteration)
- [[concepts/advanced-tool-use]] — Advanced tool use patterns
- [[concepts/code-execution-with-mcp]] — Code execution via MCP
- [[concepts/progressive-disclosure]] — Progressive disclosure pattern for agents

## Sources

- [Writing Effective Tools for AI Agents — Anthropic Engineering](https://www.anthropic.com/engineering/writing-tools-for-agents)
- [Building Effective Agents — Anthropic Engineering](https://www.anthropic.com/engineering/building-effective-agents)
- [[raw/articles/2026-05-08_anthropic-engineering_writing-tools-for-agents.md]]
