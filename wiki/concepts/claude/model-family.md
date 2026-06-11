---
title: "Build with Claude — Developer Guide"
type: concept
aliases:
  - claude
  - Claude AI
  - anthropic-claude
  - claude-models
  - build-with-claude
  - claude-developer-guide
created: 2026-05-08
updated: 2026-05-26
tags:
  - concept
  - anthropic
  - model
  - ai-agents
  - developer-tooling
status: complete
sources:
  - url: "https://www.anthropic.com/learn/build-with-claude"
    title: "Build with Claude — Anthropic Developer Guide"
  - url: "https://www.anthropic.com/news/claude-3-family"
    title: "Claude 3 Family Announcement"
  - url: "https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking"
    title: "Extended Thinking Guide"
  - url: "https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching"
    title: "Prompt Caching Guide"
  - url: "https://github.com/anthropics/anthropic-cookbook"
    title: "Anthropic Cookbook"
  - url: "https://www.anthropic.com/research/building-effective-agents"
    title: "Building Effective Agents — Anthropic"
  - url: "https://www.anthropic.com/engineering/harness-design-long-running-apps"
    title: "Harness Design for Long-Running Application Development"
related:
  - "[[entities/anthropic]]"
  - "[[entities/claude-code]]"
  - "[[concepts/claude/design]]"
  - "[[claude-managed-agents]]"
  - "[[concepts/mcp]]"
  - "[[claude-opus-4-7]]"
  - "[[concepts/anthropic-computer-use]]"
  - "[[concepts/claude/memory-tool]]"
  - "[[concepts/extended-thinking]]"
  - "[[concepts/prompt-caching]]"
  - "[[concepts/anthropic/agent-sdk-sre-patterns]]"
  - "[[concepts/ai-safety-military-governance-claude]]"
  - "[[concepts/coding-agents]]"
---

# Build with Claude — Developer Guide

> **Claude** is an LLM family developed by [[entities/anthropic]], built on Constitutional AI as its safety design philosophy, and offered in **3 tiers: Haiku / Sonnet / Opus.**
> This page follows the structure of [Anthropic's Build with Claude guide](https://www.anthropic.com/learn/build-with-claude), compiling practical guidance for developers integrating Claude into their applications.
> See the respective sub-pages for details on individual products and models.

---

## 🚀 1. Quick Start — First Steps in Development

Get your API key from the [Anthropic Console](https://console.anthropic.com). Make your first API request with the [Quickstart Guide](https://docs.anthropic.com/en/docs/get-started). Via CLI: `npm install -g @anthropic-ai/claude-code`. See [Developer Docs](https://docs.anthropic.com/en/home) and [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) for more.

---

## 🧠 2. Advanced Model Capabilities

### 2.1 Extended Thinking

Claude's ability to execute internal reasoning steps before responding. First introduced in Claude 3.7 Sonnet (February 2025).

- **Ideal tasks**: Complex logic, math, coding, multi-step reasoning
- **API usage**: Specify the `thinking` parameter
- **Pricing**: Reasoning tokens are billed at output token prices
- **In Claude Code**: Internally used via Ultraplan and Subagent delegation
- Details: [Extended Thinking Guide](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)

### 2.2 Vision & Multimodal

Image input support since Claude 3. Opus 4.7 achieves state-of-the-art visual recognition.

- **Supported media**: Images (JPEG/PNG/GIF/WebP), PDF (text + images)
- **Use cases**: Screenshot analysis, chart reading, PowerPoint slide analysis, technical diagram understanding
- **Techniques**: Multi-image comparison, text transcription from embedded images
- Details: [[concepts/multimodal]]

### 2.3 Computer Use (Beta)

Claude's ability to see screenshots and directly operate desktop GUIs.

- **Operations**: Click, type, scroll (equivalent to human operations)
- **History**: October 2024 research preview → February 2026 Vercept acquisition enhanced capabilities
- **Use cases**: Browser operations, desktop app operations, data entry automation
- **Limitations**: Beta, room for improvement in latency and accuracy
- Details: [[entities/anthropic-computer-use]]

---

## 🛠️ 3. Architectural Patterns and Tools

> **Design principles (from [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)):**
> 1. **Simple is best** — Small composable patterns over complex frameworks
> 2. **Context is all you need** — Rich context environments are more effective than explicit planners
> 3. **Deterministic infrastructure over decision scaffolding** — 98.4% of agent execution infrastructure can be deterministic
> 4. **Unix philosophy** — Minimal components should be "useful, understandable, and extensible"

### 3.1 Tool Use (Function Calling)

Standard functionality for Claude to interact with external APIs and local tools. Beta in November 2023, GA in March 2024.

- **Standard tools**: Bash execution, file editing, text editor, code execution, web search
- **Custom tools**: Define any external API via JSON schema
- **MCP integration**: Connect via [[concepts/mcp]]-compatible tool servers
- **Parallel calls**: Multiple tools can be executed simultaneously
- Learning resources: [Tool Use Course](https://github.com/anthropics/courses/blob/master/tool_use/README.md)

### 3.2 Agents & Skills — Building Autonomous Agents

Three-layer approach for building autonomous agents with Claude:

| Layer | Description | Examples |
|---|---|---|
| **Skills** | Task-specific instruction blocks | Code review skills, test generation skills |
| **MCP** | Open standard for tool connectivity | Filesystem MCP, DB MCP, Slack MCP |
| **Agent SDK** | Agent lifecycle management | Hooks, Subagents, Plan Mode |

Claude Agent SDK (`@anthropic-ai/claude-agent-sdk`) key features:
- **Hooks**: Lifecycle hooks such as `before_tool`, `after_tool`, `on_error`
- **Subagents**: Spawn child agents and collect results
- **Plan Mode**: Generate and approve plans before execution
- **Output Styles**: Structured output style specifications
- **MCP integration**: Built-in MCP server support

### 3.3 RAG — Integrating External Data

Combine external data with Claude to improve answer accuracy:

- **Contextual Retrieval**: High-precision RAG technique developed by Anthropic
- **Supported embeddings**: Integrated with Voyage AI
- **Supported frameworks**: LlamaIndex, MongoDB
- **Techniques**: Reduce reference document costs with prompt caching

### 3.4 Structured Output

Function to reliably ensure model output conforms to a JSON schema.

- JSON mode guarantees schema compliance via validation
- Improves reliability of agent control, eliminates need for subsequent parsing
- Reference: [[concepts/claude-code/claude-code]]

---

## 📈 4. Optimization & Performance

### 4.1 Prompt Engineering

Prompt design to maximize Claude's performance:

- **[Prompt Generator](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-generator)** — Automated prompt generation tool
- **[Interactive Tutorial](https://github.com/anthropics/courses/blob/master/prompt_engineering_interactive_tutorial/README.md)** — Interactive learning course
- **Key points**: Clear instructions, examples (few-shot), role setting, output format specification
- **System prompts**: Set persistent instructions as system messages

### 4.2 Prompt Caching

Reduce cost and latency by reusing frequently-sent large context:

- **Cache write cost**: 1.25x standard input
- **Cache read cost**: **10%** of standard input (valid for 5 minutes)
- **Effect**: Significant cost reduction for workloads repeatedly sending long system prompts or reference documents
- **Example**: For Sonnet 4.6 with 50K token system prompt, normal $0.15 → cached $0.015

| Model | Cache Write ($/MTok) | Cache Read ($/MTok) |
|---|---|---|
| Opus 4.7 | $6.25 | $0.50 |
| Sonnet 4.6 | $3.75 | $0.30 |
| Haiku 4.5 | $1.25 | $0.10 |

- Details: [Prompt Caching Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)

### 4.3 Evaluations (Evals)

Improve prompts and architecture through systematic performance measurement:

- **Anthropic Console**: Create, run, and compare Evals in browser
- **Automation pipelines**: [Cookbook Notebook](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building_evals.ipynb) for CI/CD integration
- **Batch processing**: Run large-scale Evals at 50% off all token costs
- **Measured metrics**: Accuracy, latency, cost, consistency

---

## Appendix A: Model Reference

### A.1 Quick Overview of the 3 Tiers

| Tier | Price (input) | Optimal Workload | Recommended For |
|---|---|---|---|
| **Haiku 4.5** 🏎️ | $1/MTok | Classification, extraction, routing, chat | Cost-conscious, high throughput |
| **Sonnet 4.6** ⚖️ | $3/MTok | Coding, agents, knowledge work, RAG | First choice for production workloads |
| **Opus 4.7** 🧠 | $5/MTok | High-difficulty reasoning, long-term planning, complex coding | Frontier tasks where quality is paramount |

### A.2 Simplified Timeline

| Period | Milestone |
|---|---|
| 2023 | Claude 1 → 2.1. Tool Use beta, 200K context. Constitutional AI established |
| 2024 | Claude 3 (Haiku/Sonnet/Opus). 3 tiers + multimodal introduced. 3.5 Sonnet delivers Opus-class performance at Sonnet pricing |
| Early 2025 | 3.7 Sonnet adds Extended Thinking. Claude Code released. Competes with GPT-4o |
| Late 2025 | Claude 4 → 4.5 generation. Achieves SWE-bench 77.2%. Computer Use improvements. Bun acquisition |
| H1 2026 | Opus 4.6 (Feb)→ Sonnet 4.6 (Feb)→ Opus 4.7 (Apr). Managed Agents GA. Claude Design announced |

For model-specific details, see sub-pages: [[claude-opus-4-7]], [[claude-sonnet-4.6]], [[claude-opus-4-6]]

---

## Appendix B: Ecosystem Overview

| Product | Description | Details |
|---|---|---|
| **Claude.ai** | Official Web/Mobile chat. Subscription-based. | Projects, file attachments, 200K context |
| **[[entities/claude-code]]** | Autonomous coding agent (CLI/IDE/Web/Mobile/Slack) | SWE-bench 72.7%, 7.6x deployment improvement |
| **[[concepts/claude/design]]** | Visual design collaboration tool (April 2026 research preview) | Powered by Opus 4.7 vision model |
| **[[claude-managed-agents]]** | Enterprise managed agent platform | Memory store, multi-agent, Outcomes Loop |
| **[[concepts/mcp]]** | Model Context Protocol — open standard for tool connectivity | Adopted by OpenAI/Google/Microsoft/Red Hat |
| **Claude Agent SDK** | Node.js SDK (`@anthropic-ai/claude-agent-sdk`) | Hooks, Subagents, Plan Mode |

---

## Appendix C: Subscription Pricing

| Plan | Price | Target Audience |
|---|---|---|
| Free | Free | Trial |
| Pro | $20/month | Individual developer |
| Max (5x) | $100/month | Heavy users (up to 36x value vs API) |
| Max (20x) | $200/month | High-frequency use (~2x the weekly limit of 5x) |
| Team | $25/seat/month | Teams |
| Enterprise | Custom | Large enterprises (SSO, audit logs, separate API billing for usage) |

> See [Anthropic Console](https://console.anthropic.com) or [[concepts/claude-opus-4-7]] for API pricing.

---

## Related Pages

- **[[entities/anthropic]]** — The company behind Claude
- **[[entities/claude-code]]** — AI coding agent
- **[[claude-code--capabilities]]** — Claude Code capabilities detail
- **[[concepts/claude/design]]** — Visual design tool
- **[[claude-managed-agents]]** — Enterprise agent platform
- **[[claude-opus-4-7]]** — Latest Opus model details
- **[[concepts/anthropic-computer-use]]** — GUI operation capability
- **[[concepts/mcp]]** — Model Context Protocol
- **[[concepts/ai-safety-military-governance-claude]]** — Safety and governance
- **[[concepts/coding-agents]]** — AI coding agent ecosystem
- **[[concepts/anthropic/agent-sdk-sre-patterns]]** — Agent SDK
- **[[concepts/claude/memory-tool]]** — Memory tool
