# OpenAI Agents SDK — Raw Research Overview

**Fetch date:** 2026-07-25
**Sources:**
- https://openai.github.io/openai-agents-python/ (official docs)
- https://platform.openai.com/docs/guides/agents (OpenAI platform docs)
- https://github.com/openai/openai-agents-python (GitHub repo)
- GitHub API (repo metadata, releases, README)

---

## What It Is

The OpenAI Agents SDK is a lightweight, production-ready Python framework for building multi-agent AI workflows. It provides a small set of powerful primitives — Agents, Handoffs, Guardrails, and Tracing — that enable developers to build complex agentic applications without a steep learning curve.

- **Package:** `openai-agents` (PyPI)
- **Language:** Python 3.10+
- **License:** MIT
- **GitHub:** openai/openai-agents-python (~28,159 stars, ~4,377 forks as of July 2026)
- **JS/TS version:** openai/openai-agents-js
- **Predecessor:** Swarm (experimental educational framework by OpenAI Solutions team, created Feb 2024)

The SDK is described as "a production-ready upgrade of our previous experimentation for agents, Swarm."

---

## Release History

| Milestone | Version | Date |
|-----------|---------|------|
| Repo created | — | 2025-03-11 |
| First public release | v0.0.2 | 2025-03-11 |
| First minor stable | v0.1.0 | 2025-06-27 |
| Feature expansion | v0.2.0 | 2025-07-15 |
| Current latest | v0.18.3 | 2026-07-17 |

**Development pace:** Very active — 100+ releases in ~16 months, averaging multiple releases per week. The SDK has not yet reached v1.0.0.

---

## Design Principles

1. **Enough features to be worth using, but few enough primitives to make it quick to learn**
2. **Works great out of the box, but you can customize exactly what happens**

---

## Key Features

### Agent Loop
Built-in agent loop that handles tool invocation, sends results back to the LLM, and continues until the task is complete.

### Python-First Orchestration
Use built-in language features to orchestrate and chain agents, rather than needing to learn new abstractions.

### Handoffs (Agents as Tools)
Powerful mechanism for coordinating and delegating work across multiple agents. Handoffs are represented as tools to the LLM, enabling dynamic task routing.

### Sandbox Agents
Run specialists inside real isolated workspaces with manifest-defined files, sandbox client choice (Unix local, Docker, hosted), and resumable sandbox sessions.

### Guardrails
Run input validation and safety checks in parallel with agent execution (or blocking). Supports input guardrails (first agent), output guardrails (final output), and tool guardrails (per-tool-call). Tripwire mechanism for fast failure.

### Function Tools
Turn any Python function into a tool with automatic schema generation and Pydantic-powered validation.

### MCP Server Integration
Built-in Model Context Protocol (MCP) server tool integration that works the same way as function tools.

### Sessions
Persistent memory layer for maintaining working context within an agent loop. Supports SQLAlchemy, SQLite, Redis, MongoDB, Dapr, and encrypted backends.

### Human-in-the-Loop
Built-in mechanisms for involving humans across agent runs.

### Tracing
Built-in tracing for visualizing, debugging, and monitoring workflows. Collects LLM generations, tool calls, handoffs, guardrails, and custom events. Integrates with OpenAI's evaluation, fine-tuning, and distillation tools.

### Realtime Agents
Build powerful voice agents with gpt-realtime-2.1, automatic interruption detection, context management, and guardrails over WebSocket connections.

### Provider Agnostic
Supports OpenAI Responses and Chat Completions APIs, plus 100+ other LLMs through multi-provider support.

### Voice Agents
Build voice-enabled agents with speech-to-text and text-to-speech capabilities, with automatic transcription and speech spans in tracing.

---

## Key Concept: Agent

An LLM configured with instructions, tools, guardrails, handoffs, and optional structured output types.

**Key properties:** `name (required)`, `instructions (system prompt)`, `model`, `tools`, `handoffs`, `input_guardrails`, `output_guardrails`, `output_type`, `hooks`, `mcp_servers`

---

## Key Concept: Handoffs

Mechanism allowing an agent to delegate tasks to another specialist agent. Handoffs are represented as tools to the LLM.

Handoff features: Custom tool name and description overrides, on_handoff callback for side effects, input_type for structured data from LLM at handoff time, input_filter for filtering conversation history passed to next agent, Dynamic enable/disable via is_enabled callback, Nested handoff history control

Default tool naming: `transfer_to_<agent_name>`.

---

## Key Concept: Guardrails

Three types of safety/validation checks:
- **Input Guardrails:** Run on the first user input for the agent chain. Supports parallel (default, better latency) and blocking (cost-saving) execution modes.
- **Output Guardrails:** Run on the final agent output. Always runs after agent completes.
- **Tool Guardrails:** Wrap function tools — validate/block tool calls before and after execution. Input checks before execution, output checks after.

Tripwire mechanism: Guardrail function → `GuardrailFunctionOutput` → check `tripwire_triggered` → raise exception if triggered.

---

## Key Concept: Tracing

Built-in observability system collecting comprehensive records of agent runs.

**Hierarchy:** Trace (end-to-end workflow) → Spans (operations with start/end times)

**Span types:** `agent_span`, `generation_span`, `function_span`, `guardrail_span`, `handoff_span`, `transcription_span`, `speech_span`, `speech_group_span`, `custom spans`

**Default behavior:** Enabled by default. Can disable globally (env var), per-run, or via ZDR policy.

---

## OpenAI API Relationship

The SDK uses the **Responses API** by default for OpenAI models but adds a higher-level runtime around model calls.

**Use the SDK when:**
- You want the runtime to manage turns, tool execution, guardrails, handoffs, or sessions
- Your agent should produce artifacts or operate across multiple coordinated steps
- You need a real workspace or resumable execution through Sandbox agents

**Use the Responses API directly when:**
- You want the runtime to manage turns, tool execution, guardrails, handoffs, or sessions
- Your agent should produce artifacts or operate across multiple coordinated steps
- You need a real workspace or resumable execution through Sandbox agents

---

## Comparison to Alternatives

### vs Langgraph
- **Langgraph:** General-purpose graph-based agent framework by LangChain. Uses StateGraph with nodes and edges for complex, branching workflows.
- **Agents Sdk:** Simpler, fewer abstractions. Agent-centric (not graph-centric). Opinionated about the agent loop. Easier to learn but less flexible for arbitrary graph topologies.
- **Key Difference:** Philosophy: Agents SDK prioritizes simplicity and quick learning curve; LangGraph prioritizes maximum control and composability.

### vs Crewai
- **Crewai:** Role-based multi-agent framework where agents have defined roles, goals, and backstories. Focuses on collaborative task execution with sequential or hierarchical processes.
- **Agents Sdk:** Lighter weight with fewer abstractions. No built-in role/backstory concepts. Handoffs provide similar multi-agent coordination but more programmatic.
- **Key Difference:** CrewAI is more opinionated about agent roles and collaboration patterns; Agents SDK is more flexible and lower-level.

### vs Autogen
- **Autogen:** Microsoft's multi-agent conversation framework supporting diverse conversation patterns, code execution, and human-in-the-loop. Originally multi-backend (now more OpenAI-focused).
- **Agents Sdk:** More OpenAI-native. Simpler API surface. Built-in tracing and guardrails that AutoGen provides through separate mechanisms.
- **Key Difference:** AutoGen provides richer conversation patterns (group chat, nested chat); Agents SDK is more streamlined with a focus on handoffs and a cleaner API.

### vs Swarm Predecessor
- **Swarm:** Experimental educational framework. Lightweight but not production-hardened. No built-in tracing, guardrails, or session management.
- **Agents Sdk:** Production-ready upgrade. Adds tracing, guardrails, sessions, sandbox agents, realtime agents, MCP support, and multi-provider support.

---

## Installation

```bash
pip install openai-agents

# Optional extras:
pip install 'openai-agents[voice]'     # Voice/realtime support
pip install 'openai-agents[redis]'     # Redis session support
pip install 'openai-agents[docker]'    # Docker sandbox support
```

---

## Ecosystem & Extensions

**Session backends:** SQLAlchemySession, AsyncSQLiteSession, RedisSession, MongoDBSession, DaprSession, EncryptedSession, AdvancedSQLiteSession, Tool output trimmer

**Tool types:** Function tools, MCP server tools, Hosted tools, Agents as tools

**Model providers:** OpenAI (Responses API, Chat Completions API), Multi-provider (100+ LLMs via any-llm / LiteLLM)

**Companion tools:** Agent visualization, REPL utility, Traces dashboard

---

## Raw Data Files Saved

The following raw files were saved during research for reference:
- `raw/platform.openai.com_raw.html`
- `raw/openai.github.io_raw.html`
- `raw/sdk_agents_raw.html / sdk_agents_text.txt`
- `raw/sdk_handoffs_raw.html / sdk_handoffs_text.txt`
- `raw/sdk_guardrails_raw.html / sdk_guardrails_text.txt`
- `raw/sdk_tracing_raw.html / sdk_tracing_text.txt`
- `raw/sdk_tools_raw.html / sdk_tools_text.txt`
- `raw/sdk_quickstart_raw.html / sdk_quickstart_text.txt`
- `raw/sdk_github_repo.json`
- `raw/sdk_latest_release.json`
- `raw/sdk_readme.md`
- `raw/scrape_metadata.json`
- `raw/openai_agents_sdk_structured_facts.json`