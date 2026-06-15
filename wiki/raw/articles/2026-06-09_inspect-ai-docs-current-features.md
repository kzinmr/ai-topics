---
title: "Inspect AI Documentation — Current Feature Overview (v0.3.239)"
date: 2026-06-09
date_ingested: 2026-06-15
source: https://inspect.aisi.org.uk/
type: article
tags: [evaluation, evals, framework, open-source, agent-evaluation, sandbox, ai-safety, documentation]
---

# Inspect AI Documentation — Current Feature Overview

> Captured from https://inspect.aisi.org.uk/ (v0.3.239, June 9, 2026) and https://inspect.aisi.org.uk/llms-full.txt

## Summary

Inspect AI is a framework for frontier AI evaluations developed by the UK AI Security Institute and Meridian Labs. Used for coding, agentic tasks, reasoning, knowledge, behavior, and multi-modal understanding evaluations.

## Core Features (as of June 2026)

1. **Composable building blocks** — datasets, agents, tools, and scorers
2. **200+ pre-built evaluations** ready to run on any model
3. **Web-based Inspect View** for monitoring/visualizing evaluations + VS Code Extension
4. **Flexible tool calling** — custom and MCP tools, built-in bash, python, text editing, web search, web browsing, computer tools
5. **Agent evaluations** — built-in agents, multi-agent primitives, external agent support (Claude Code, Codex CLI, Gemini CLI)
6. **Sandboxing** — Docker, Kubernetes, Modal, Proxmox, and extension API

## Agent System

### Built-in Agents
- **react()**: ReAct agent — reason-act-observe loop with tool calling, retry, submit
- **Deep Agent**: Long-horizon tasks with subagent delegation, memory, planning
- **Human Agent**: Human baselining of computing tasks

### Agent Bridge
Bridges external agents into Inspect:
- **Python bridge** (`agent_bridge()`): OpenAI Agents SDK, Pydantic AI, LangChain — same process
- **Sandbox bridge** (`sandbox_agent_bridge()`): Claude Code, Codex CLI, Gemini CLI — runs in Docker
- Intercepts API calls with `model="inspect"`, routes to Inspect model provider
- Works with OpenAI Completions, Responses, Anthropic, Google APIs
- `BridgedToolsSpec` exposes host tools as MCP to sandboxed agents

### Multi-Agent
- `handoff()`: Forwards entire conversation history between agents
- `as_tool()`: String-in/string-out interface to agents
- Agents can be used as solvers, standalone, delegated to, or as tools

## Tools (6 built-in)
- `bash()` — shell commands in sandbox
- `python()` — Python code in sandbox
- `text_editor()` — file editing
- `web_search()` — web search
- `web_browser()` — headless Chromium
- `computer()` — desktop via screenshots
- `think()` — explicit reasoning
- `todo_write()` — task tracking
- `submit()` — agent signals completion

## Scoring
- Standard: `match()`, `includes()`, `choice()`
- Model-graded: `model_graded_fact()`, `model_graded_qa()`
- Custom: `@scorer` decorator with metrics (`accuracy()`, `stderr()`)
- Perplexity scoring
- Multiple scorers per task
- Scoring workflow customization

## Models
- 20+ built-in providers
- `provider/model-name` convention
- Concurrency: `max_connections`, `max_subprocesses`
- Caching, compaction, fallbacks
- Batch mode, multimodal, reasoning controls
- Structured output (JSON schema)
- `reasoning_effort`, `reasoning_tokens`, `effort` controls

## Production
- **eval_set()**: Multi-task, multi-model with retries and resumption
- **Parallelism**: Async architecture, massive scale
- **Limits**: Message, token, time, cost
- **Error handling**: Failure thresholds, crash recovery
- **Control Channel**: `inspect ctl` for live run observation

## Logging
- Structured EvalLog (Python object + JSON + TypeScript types)
- Web-based log viewer (`inspect view`)
- `inspect view bundle` — static website for sharing
- Pandas DataFrames: `samples_df()`, `evals_df()`
- VS Code Extension integration

## Scanning (inspect-scout)
- `@scanner` decorator for transcript review
- `llm_scanner()` — model-powered analysis
- Supports boolean, numeric, string, classification answers
- Run with `--scanner` flag

## Extensions
- Custom model APIs, components, sandboxes, approvers, hooks, filesystems
- Extensions gallery of community packages
- MCP tool integration

## Ecosystem
- `inspect-ai` — core framework
- `inspect-swe` — coding agents (Claude Code, Codex CLI, Gemini CLI)
- `inspect-scout` — transcript scanning
- `inspect_evals` — 200+ pre-built benchmarks
- VS Code Extension
- Community extensions

## Release History
- First release: v0.3.2 (April 21, 2024)
- Current: v0.3.239 (June 9, 2026)
- 239 releases in ~2 years — near-daily cadence
