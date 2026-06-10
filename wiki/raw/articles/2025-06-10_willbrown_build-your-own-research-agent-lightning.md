---
title: "Build Your Own AI Research Agent — Lightning Lesson"
author: Will Brown
date: 2025-06-10
date_ingested: 2026-06-10
source: https://maven.com/p/193c6f/build-your-own-ai-research-agent
type: lecture-summary
tags:
  - ai-agents
  - research-agent
  - tool-calling
  - context-engineering
  - deep-research
  - education
  - mcp
---

# Build Your Own AI Research Agent — Lightning Lesson

**Instructor:** Will Brown (Research Lead, [[entities/prime-intellect]])
**Date:** June 10, 2025 (pre-course Lightning Lesson)
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
**Lecture notebook:** [[transcripts/2025-06-10_willbrown_build-your-own-research-agent-notebook|Notebook Walkthrough]]
**GitHub repo:** [agent-engineering](https://github.com/willccbb/agent-engineering) (lightning-lessons/agents.ipynb)
**Maven page:** [Build Your Own AI Research Agent](https://maven.com/p/193c6f/build-your-own-ai-research-agent)

## Summary

A ~75-minute pre-course Lightning Lesson that builds a **deep research agent from scratch** in under an hour. The lesson progresses from basic definitions through a working V1 agent (search + fetch tools), a V2 agent (sub-models as tools), and culminates in a live demo using MCP servers with Claude Code for iterative refinement. The lesson connects agent building to the course's broader RL thesis: agents and RL are two sides of the same coin.

## Video Chapters

| Timestamp | Chapter |
|-----------|---------|
| 00:11:40 | Introduction: Building a Research Agent and the Role of RL |
| 00:13:42 | What is an Agent? The Core Interaction Loop |
| 00:15:20 | Why You Should Build Agents Without Frameworks |
| 00:19:10 | V1 Agent: System Prompt and Tool Definition |
| 00:22:45 | Implementing Search and Fetch Tools |
| 00:27:08 | The Core Agent Loop: Parsing, Execution, and First Run |
| 00:34:38 | Improving the Agent with Sub-Models as Tools |
| 00:41:14 | V2 Agent: Running with the New 'Ask Model' Tool |
| 00:45:43 | Building Robust Systems with MCP and Claude Code |
| 00:50:12 | Live Demo: Iteratively Refining Agent Behavior in Claude Code |
| 00:58:36 | Evaluating Agent Output and the Concept of Evals |
| 01:06:02 | Q&A, Course Details, and Connecting Agents to RL |
| 01:13:23 | Conclusion and Anecdotes on Reward Hacking |

## Key Topics

### 1. What is an Agent?

No universally agreed-upon definition, but the core idea: **a system that can take actions in an environment towards a goal**, with the ability to dynamically adapt logic in response to observations.

**Agents** (dynamic adaptation):
- Deep Research
- Claude Code
- Manus

**Non-agents** (fixed pipelines):
- Pre-fetch RAG
- Fixed decision trees of LLMs
- Classifier-based routers

**Reductive definition:** *"LLM with tool calls in a while loop"*
**Must-read:** [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) from Anthropic

### 2. Why Build Without Frameworks

Brown advocates building agents from scratch first to understand the core loop before using abstractions. The basic environment requires only:
- An OpenAI-compatible client (any model/provider)
- A search tool + fetch tool
- A system prompt with format instructions

### 3. V1 Agent: System Prompt + Tool Definition

The V1 agent uses regex-based XML parsing (`<think>`, `<tool>`, `<answer>` tags) rather than native function calling. This is deliberately simple and portable:
- Works with any model that can follow format instructions
- No dependency on provider-specific tool calling APIs
- Tools: `search(query)` using Brave Search API, `fetch(url)` using markdownify

### 4. The Core Agent Loop

```python
while True:
    response = client.chat.completions.create(model=model_name, messages=messages)
    maybe_tool_call = parse_tool_from_response(response)
    maybe_answer = parse_answer_from_response(response)
    if maybe_tool_call:
        tool_result = call_tool(tool_call)
        messages.append({"role": "user", "content": tool_result})
    elif maybe_answer:
        final_answer = maybe_answer
        break
```

Key pattern: **state accumulation** via message list. Without state, the model has no memory of prior searches.

### 5. V2 Agent: Sub-Models as Tools

The V2 improvement adds an `ask_model(question, url)` tool that delegates URL reading to a cheaper helper model (GPT-4.1 Mini). This is a critical pattern:
- **Primary agent** (GPT-4.1): strategic decisions, search planning
- **Helper model** (GPT-4.1 Mini): bulk reading, summarization
- Reduces cost and latency for multi-source research

### 6. MCP Crash Course

MCP = "basically just function calling" with a client/server architecture:
- **Why:** standardized interface, portability, clients + servers manage own state
- **SDKs:** Python + TypeScript (uvx, npx), also Java/Kotlin/C#/Swift
- **Clients:** Claude Desktop, Claude Code, Cursor, Windsurf
- **Resources:** [MCP docs](https://modelcontextprotocol.io), [Smithery](https://smithery.ai/), [mcp.so](https://mcp.so/)

### 7. Deep Research via Claude Code

The lesson demonstrates using Claude Code as a sandbox for research agent workflows. Requirements:
- Tools (MCP servers for search/fetch)
- Instructions (report guidelines)
- Examples (sample reports)
- Ability to refine via feedback

The companion repo includes [EXAMPLE_REPORT.md](https://github.com/willccbb/research-agent-lesson/blob/main/EXAMPLE_REPORT.md) with detailed report generation guidelines (importance ranking, spam filtering, limerick summaries, cost info, celebrity speaker flagging).

### 8. Evaluating Agent Output

- "The best eval is your own eval" — build task-specific evaluation
- LLMs work best in-distribution; custom evals measure what matters
- The lesson connects evals to the RL reward signal: evals → rewards → training
- Anecdotes on reward hacking: agents optimizing for metrics rather than quality

## Companion Resources

| Resource | Description |
|----------|-------------|
| [agent-engineering/lightning-lessons](https://github.com/willccbb/agent-engineering/tree/main/lightning-lessons) | Lightning lesson notebooks (agents.ipynb, search.ipynb) |
| [agents.ipynb](https://github.com/willccbb/agent-engineering/blob/main/lightning-lessons/agents.ipynb) | Main lesson notebook |
| [research-agent-lesson](https://github.com/willccbb/research-agent-lesson) | Companion repo (MCP server, example report, CLAUDE.md) |
| [server_example.py](https://github.com/willccbb/research-agent-lesson/blob/main/server_example.py) | MCP Fetch server implementation |
| [EXAMPLE_REPORT.md](https://github.com/willccbb/research-agent-lesson/blob/main/EXAMPLE_REPORT.md) | Report generation guidelines |
| [CLAUDE.md](https://github.com/willccbb/research-agent-lesson/blob/main/CLAUDE.md) | Report generation guidelines (MCP version) |

## Related

- [[concepts/agents-mcp-rl-course]] — Course portal page
- [[entities/will-brown]] — Instructor profile
- [[transcripts/2025-06-10_willbrown_build-your-own-research-agent-notebook|Notebook Walkthrough]] — Detailed code walkthrough
- [[raw/articles/2025-06-17_willbrown_agents-mcp-rl-lesson1|Lesson 1: Agent Patterns & Principles]] — First regular lecture
- [[concepts/research-agent-fundamentals]] — Research agent concepts
- [[concepts/deep-research]] — Deep research agent paradigm
- [[concepts/context-engineering]] — Agent context design
- [[concepts/agentic-rl]] — RL for agents paradigm
- [[concepts/mcp]] — Model Context Protocol
