---
title: "Production-Ready Agent Engineering — Lesson 2: MCP + Production-Grade Agents"
author: Will Brown
date: 2025-06-19
date_ingested: 2026-06-10
source: https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
type: lecture-summary
tags:
  - ai-agents
  - mcp
  - tool-calling
  - async-agents
  - rag
  - security
  - observability
  - education
---

# Production-Ready Agent Engineering — Lesson 2: MCP + Production-Grade Agents

**Instructor:** Will Brown (Research Lead, [[entities/prime-intellect]])
**Co-instructor:** Kyle Corbitt (CTO, OpenPipe)
**Date:** June 19, 2025
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
**Lecture transcript:** [[transcripts/2025-06-19_willbrown_agents-mcp-rl-lesson2-lecture|MCP + Production-Grade Agents (Lecture Transcript)]]
**Notebook:** [ai-agent-engineering repo](https://github.com/willccbb/ai-agent-engineering)

## Summary

The second lecture bridges the gap between agent prototyping and production. It covers **software best practices** (type hints, testing), **async processing** for parallel LLM calls, **RAG patterns** (old-school prefetch vs agentic), **MCP architecture** (when and why), **logging/monitoring**, and **security considerations**. A strong theme is treating tools as software — applying the same testing, typing, and security discipline you would to any production codebase.

## Key Topics

### 1. Type Hints & Strong Typing

The lecture opens with a cautionary demo: an LM returns `"3"` (string) instead of `3` (float). Without type hints, Python's string multiplication silently produces `"333333"` instead of `18`. The code runs without error — but the result is wrong.

**Takeaway:** Type hints + Pydantic structured outputs bridge the gap between LLMs (which operate on tokens) and programs (which operate on typed objects). Use `Literal` types for guaranteed field validation.

### 2. Tools Are Software

- Tools are functions used by LLMs — all software testing/best practices apply
- Calculator tool demo: input filtering + `eval()` for safe code execution
- **Tool vs no-tool:** with calculator → correct answer; without → close but wrong (GPT-4.1 Nano)
- **Model behavior matters:** Codex is terminal-optimized and safe; older Gemini 2.5 Pro churned out scripts chaotically
- **Tool count limits:** a few dozen is fine for big models; 5-10 for small models; 1000+ is impractical

### 3. Async Processing

| Pattern | 12 Requests | Use When |
|---------|-------------|----------|
| Sequential | 19.5s | Never in production |
| `asyncio.gather` (unbounded) | 2.6s | No rate limits |
| Semaphore (max 5) | 4.5s | Rate-limited providers |

- Default programming pattern for production LLM apps
- Also applies to tool calls — parallel sub-agent search
- Timeout patterns: set per-function timeouts, roll with partial results

### 4. RAG Patterns

| Pattern | Search Driver | Retry? | Flexibility |
|---------|--------------|--------|-------------|
| **Prefetch RAG** | Software (embedding search) | No | Low — hand-engineered |
| **Agentic RAG** | Agent (tool calls) | Yes | High — agent adapts |

**Tips:**
- Markdown is the best LLM-readable format
- Expose hyperlinks as navigable tools
- Use existing search APIs as tools (don't reinvent Google)
- LLMs can use terminal commands for file exploration (`show lines 20-47`)

### 5. MCP: Model Context Protocol

MCP = **FastAPI but LM-shaped**. A server with first-class support for exposing prompts and calling tools.

**When to use MCP:**
- Tool portability across apps (Cursor + Claude Code + ChatGPT)
- N data sources × M applications → N+M with MCP (each source = server, each app = client)
- Building a service with an API → add an MCP server

**When NOT to start with MCP:**
- Building from scratch — get logic working with plain functions first, then wrap as MCP tools when needed

**A2A (Agent-to-Agent):**
- Brown is skeptical: "I just don't think we've seen any winning applications"
- Reliable pattern: one primary agent + sub-agents via MCP
- "I'm not gonna tell anyone to go build on A2A right now. But you probably should be building on MCP."

### 6. Logging & Monitoring

| Framework | Best For |
|-----------|----------|
| **Pydantic Logfire** | Pydantic AI users |
| **W&B Weave** | ML researchers already on W&B |
| **MLflow Tracing** | Open-source alternative |
| **Arize Phoenix** | General purpose |

Choose based on ecosystem lock-in — least friction wins. MCP is the closest thing to a "CUDA-like" standard for tools.

### 7. Security & Sandboxing

- **Blacklisting** = whack-a-mole; smart LLMs find workarounds
- **Whitelisting** via code sandboxing (E2B, Docker containers) is safer
- **Codify repeated patterns as tools** — freeze reliable paths, reduce chaos
- LLMs love writing redundant scripts (Claude, Gemini especially) — enforce pathways with tools + docs
- **Auth:** agent = user extension with subset of permissions; human-in-loop approval for risky actions
- **Env vars:** never expose directly to LLMs

### 8. Data Structures for LLMs

- **File systems** — Docker containers as virtual machines; folders as memory
- **Memory is unsolved** — LLMs forget to check memory, hard to trigger right memories dynamically
- **SQL** — LLMs write SQL well; SQLite/Postgres as MCP servers
- **Vector DBs** — commodity; use whatever fits your setup (Chroma for prototyping)

### 9. Eval-Driven Development

- Know your eval before building beyond trivial complexity
- Anthropic/OpenAI do lots of private evals behind the scenes
- **LLM-as-judge** with Pydantic schema → structured evaluation scores
- **Best-of-N sampling**: parallel attempts + eval function selects best
- Compare agentic vs non-agentic at the output level (the report, not the search queries)

### 10. Homework: Build an Agent

Pick a task (code agent, search agent, game player, design agent). Implement:
- State management (in-memory or SQL)
- LLM-as-judge evaluation
- Best-of-N sampling (optional)
- Blog post about the experience (encouraged)

## Q&A Highlights

- **Evals for agentic vs non-agentic:** tool use is OP but that's the point. Eval at the output level. Best benchmarks: Claude Plays Pokemon, MC Bench, ARC 3 (coming soon)
- **Sub-agent spawning:** pick one framework, don't let LLMs mix abstractions
- **Tool count:** dozens OK for big models, 5-10 for small models

## Related

- [[concepts/agents-mcp-rl-course]] — Course portal page
- [[entities/will-brown]] — Instructor profile
- [[concepts/mcp]] — Model Context Protocol
- [[concepts/context-engineering]] — Agent context design
- [[concepts/agentic-search]] — Agentic RAG patterns
- [[concepts/agent-evaluation]] — Evaluation methodology
- [[transcripts/2025-06-17_willbrown_agents-mcp-rl-agent-patterns-lecture]] — Lesson 1 transcript
