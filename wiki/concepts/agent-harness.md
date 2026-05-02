---
title: "Agent Harness"
created: 2026-04-27
updated: 2026-04-30
tags:
  - harness-engineering
  - architecture
  - ai-agents
aliases: [agent-harness, harness-anatomy, agent-scaffolding]
related: [[concepts/harness-engineering]], [[concepts/deep-agents-runtime]], [[concepts/agent-loop-orchestration]], [[concepts/context-engineering]], [[concepts/bitter-lesson-harnessing]]
sources: [
  "https://x.com/akshay_pachaar/status/2041146899319971922",
  "https://x.com/i/article/2041146899319971922",
  "raw/articles/2026-04-28_the-harness-is-the-backend.md",
  "raw/articles/2041146899319971922_the-anatomy-of-an-agent-harness-.md",
  "raw/articles/2026-the-self-healing-agent-harness.md",
  "raw/articles/2026-the-ai-cake-trade.md",
  "raw/articles/crawl-2026-04-18-token-economics.md",
  "raw/articles/2026-is-s3-faster-than-a-file-system.md"
]
---

# Agent Harness

## Summary

The **agent harness** is the complete software infrastructure wrapping an LLM: orchestration loop, tools, memory, context management, state persistence, error handling, and guardrails. The term was formalized in early 2026. As LangChain's Vivek Trivedy put it: "If you're not the model, you're the harness."

The harness is not the agent itself — it's the machinery that produces agentic behavior. When someone says "I built an agent," they mean they built a harness and pointed it at a model.

## The Von Neumann Analogy

Beren Millidge's 2023 essay "Scaffolded LLMs as Natural Language Computers" made the architecture precise:

| Computer Component | LLM Equivalent | Harness Component |
|---|---|---|
| CPU | Raw LLM | Orchestration loop |
| RAM | Context window | Context management |
| Disk | External databases | Memory system |
| I/O devices | Tool integrations | Tool layer |
| OS | **The harness** | Complete infrastructure |

A raw LLM is a CPU with no RAM, no disk, and no I/O. The harness is the operating system.

## Three Levels of Engineering

Three concentric levels of engineering surround the model:

1. **Prompt Engineering** — Crafts the instructions the model receives
2. **Context Engineering** — Manages what the model sees and when
3. **Harness Engineering** — Encompasses both, plus the entire application infrastructure: tool orchestration, state persistence, error recovery, verification loops, safety enforcement, and lifecycle management

## The 12 Components of a Production Harness

### 1. The Orchestration Loop
The heartbeat. Implements the Thought-Action-Observation (TAO) cycle, also called the ReAct loop. The loop runs: assemble prompt, call LLM, parse output, execute tool calls, feed results back, repeat until done. Mechanically, it's often just a `while` loop. The complexity lives in everything the loop manages, not the loop itself. Anthropic describes their runtime as a "dumb loop" where all intelligence lives in the model.

### 2. Tools
Tools are the agent's hands, defined as schemas (name, description, parameter types) injected into the LLM's context. The tool layer handles registration, schema validation, argument extraction, sandboxed execution, result capture, and formatting results back into LLM-readable observations.

- **Claude Code**: tools across six categories — file operations, search, execution, web access, code intelligence, and subagent spawning
- **OpenAI Agents SDK**: function tools (via `@function_tool`), hosted tools (WebSearch, CodeInterpreter, FileSearch), and MCP server tools

### 3. Memory
Memory operates at multiple timescales:

- **Short-term**: conversation history within a single session
- **Long-term**: persists across sessions — Anthropic uses `CLAUDE.md` project files and auto-generated `MEMORY.md` files; LangGraph uses namespace-organized JSON Stores; OpenAI supports Sessions backed by SQLite or Redis

**Claude Code's three-tier hierarchy**: lightweight index (~150 characters per entry, always loaded), detailed topic files pulled in on demand, and raw transcripts accessed via search only. A critical design principle: the agent treats its own memory as a "hint" and verifies against actual state before acting.

### 4. Context Management
The core problem is **context rot**: model performance degrades 30%+ when key content falls in mid-window positions (Chroma research, corroborated by Stanford's "Lost in the Middle" finding).

Production strategies:
- **Compaction**: summarizing conversation history when approaching limits (Claude Code preserves architectural decisions and unresolved bugs while discarding redundant tool outputs)
- **Observation masking**: JetBrains' Junie hides old tool outputs while keeping tool calls visible
- **Just-in-time retrieval**: maintaining lightweight identifiers and loading data dynamically (Claude Code uses `grep`, `glob`, `head`, `tail` rather than loading full files)
- **Sub-agent delegation**: each subagent explores extensively but returns only 1,000 to 2,000 token condensed summaries

### 5. Prompt Construction
Assembles what the model actually sees at each step. Hierarchical: system prompt, tool definitions, memory files, conversation history, current user message.

**OpenAI Codex priority stack**: server-controlled system message (highest priority) → tool definitions → developer instructions → user instructions (cascading `AGENTS.md` files, 32 KiB limit) → conversation history.

### 6. Output Parsing
Modern harnesses rely on native tool calling, where the model returns structured `tool_calls` objects rather than free-text that must be parsed. The harness checks: are there tool calls? Execute them and loop. No tool calls? That's the final answer.

For structured outputs, both OpenAI and LangChain support schema-constrained responses via Pydantic models.

### 7. State Management
- **LangGraph**: models state as typed dictionaries flowing through graph nodes, with reducers merging updates. Checkpointing at super-step boundaries enables resume after interruptions and time-travel debugging
- **OpenAI**: four mutually exclusive strategies — application memory, SDK sessions, server-side Conversations API, or lightweight `previous_response_id` chaining
- **Claude Code**: git commits as checkpoints and progress files as structured scratchpads

### 8. Error Handling
A 10-step process with 99% per-step success still has only ~90.4% end-to-end success. Errors compound fast.

- **LangGraph** distinguishes four error types: transient (retry with backoff), LLM-recoverable (return error as ToolMessage so the model can adjust), user-fixable (interrupt for human input), unexpected (bubble up for debugging)
- **Anthropic**: catches failures within tool handlers and returns them as error results to keep the loop running
- **Stripe's production harness**: caps retry attempts at two

### 9. Guardrails and Safety
- **OpenAI SDK**: three levels — input guardrails (run on first agent), output guardrails (run on final output), tool guardrails (run on every tool invocation). A "tripwire" mechanism halts the agent immediately when triggered
- **Anthropic**: separates permission enforcement from model reasoning architecturally. The model decides what to attempt; the tool system decides what's allowed. Claude Code gates ~40 discrete tool capabilities independently, with three stages: trust establishment at project start, permission check before each tool call, and explicit user confirmation for high-risk operations

### 10. Verification Loops
What separates toy demos from production agents. Anthropic recommends three approaches:

- **Rules-based feedback**: tests, linters, type checkers
- **Visual feedback**: screenshots via Playwright for UI tasks
- **LLM-as-judge**: a separate subagent evaluates output

Boris Cherny (creator of Claude Code) noted that giving the model a way to verify its work improves quality by 2 to 3x.

### 11. Subagent Orchestration
- **Claude Code**: three execution models — Fork (byte-identical copy of parent context), Teammate (separate terminal pane with file-based mailbox communication), Worktree (own git worktree, isolated branch per agent)
- **OpenAI SDK**: agents-as-tools (specialist handles bounded subtask) and handoffs (specialist takes full control)
- **LangGraph**: subagents as nested state graphs

### 12. Termination Conditions
Layered: model produces response with no tool calls, maximum turn limit exceeded, token budget exhausted, guardrail tripwire fires, user interrupts, or safety refusal returned. Simple questions: 1-2 turns. Complex refactoring: dozens of tool calls across many turns.

## The Ralph Loop Pattern

For long-running tasks spanning multiple context windows, Anthropic developed a two-phase pattern:

1. **Initializer Agent**: sets up the environment (init script, progress file, feature list, initial git commit)
2. **Coding Agent**: every subsequent iteration reads git logs and progress files to orient itself, picks the highest-priority incomplete feature, works on it, commits, and writes summaries

The filesystem provides continuity across context windows.

## How Real Frameworks Implement the Pattern

### Anthropic Claude Agent SDK
Exposes the harness through a single `query()` function that creates the agentic loop and returns an async iterator streaming messages. The runtime is a "dumb loop." All intelligence lives in the model. Claude Code uses a **Gather-Act-Verify** cycle: gather context (search files, read code), take action (edit files, run commands), verify results (run tests, check output), repeat.

### OpenAI Agents SDK / Codex
Implements the harness through the `Runner` class with three modes: async, sync, and streamed. The SDK is "code-first": workflow logic is expressed in native Python rather than graph DSLs. The Codex harness extends this with a three-layer architecture: Codex Core (agent code + runtime), App Server (bidirectional JSON-RPC API), and client surfaces (CLI, VS Code, web app). All surfaces share the same harness, which is why "Codex models feel better on Codex surfaces than a generic chat window."

### LangGraph
Models the harness as an explicit state graph. Two nodes (`llm_call` and `tool_node`) connected by a conditional edge: if tool calls present, route to `tool_node`; if absent, route to `END`. LangGraph evolved from LangChain's `AgentExecutor`, which was deprecated in v0.2 because it was hard to extend and lacked multi-agent support. LangChain's Deep Agents explicitly use the term "agent harness": built-in tools, planning (`write_todos` tool), file systems for context management, subagent spawning, and persistent memory.

**TerminalBench evidence**: LangChain changed only the infrastructure wrapping their LLM (same model, same weights) and jumped from outside the top 30 to rank 5 on TerminalBench 2.0. A separate research project hit a 76.4% pass rate by having an LLM optimize the infrastructure itself, surpassing hand-designed systems.

### CrewAI
Implements a role-based multi-agent architecture: Agent (the harness around the LLM, defined by role, goal, backstory, and tools), Task (the unit of work), and Crew (the collection of agents). CrewAI's Flows layer adds a "deterministic backbone with intelligence where it matters," managing routing and validation while Crews handle autonomous collaboration.

### AutoGen / Microsoft Agent Framework
Pioneered conversation-driven orchestration. Three-layer architecture (Core, AgentChat, Extensions) supports five orchestration patterns: sequential, concurrent (fan-out/fan-in), group chat, handoff, and magentic (a manager agent maintains a dynamic task ledger coordinating specialists).

## The Scaffolding Metaphor

Construction scaffolding is temporary infrastructure that enables workers to build a structure they couldn't reach otherwise. It doesn't do the construction. But without it, workers can't reach the upper floors.

**Key insight**: scaffolding is removed when the building is complete. As models improve, harness complexity should decrease. Manus was rebuilt five times in six months, each rewrite removing complexity. Complex tool definitions became general shell execution. "Management agents" became simple structured handoffs.

This points to the **co-evolution principle**: models are now post-trained with specific harnesses in the loop. Claude Code's model learned to use the specific harness it was trained with. Changing tool implementations can degrade performance because of this tight coupling.

**The future-proofing test**: if performance scales up with more powerful models without adding harness complexity, the design is sound.

## Seven Decisions That Define Every Harness

Every harness architect faces seven choices:

| Decision | Options | Trade-offs |
|---|---|---|
| **Single-agent vs. Multi-agent** | Both Anthropic and OpenAI say: maximize a single agent first. Split only when tool overload exceeds ~10 overlapping tools or clearly separate task domains exist | Multi-agent adds overhead (extra LLM calls for routing, context loss during handoffs) |
| **ReAct vs. Plan-and-Execute** | ReAct interleaves reasoning and action at every step. Plan-and-execute separates planning from execution | ReAct: flexible but higher per-step cost. LLMCompiler reports 3.6x speedup over sequential ReAct |
| **Context window management** | Five production approaches: time-based clearing, conversation summarization, observation masking, structured note-taking, sub-agent delegation | ACON research showed 26-54% token reduction while preserving 95%+ accuracy by prioritizing reasoning traces over raw tool outputs |
| **Verification loop design** | Computational (tests, linters) vs. Inferential (LLM-as-judge) | Computational: deterministic ground truth. Inferential: catches semantic issues but adds latency |
| **Permission architecture** | Permissive (fast but risky) vs. Restrictive (safe but slow) | Depends on deployment context |
| **Tool scoping strategy** | More tools often means worse performance. Vercel removed 80% of tools from v0 and got better results. Claude Code achieves 95% context reduction via lazy loading | Principle: expose the minimum tool set needed for the current step |
| **Harness thickness** | Anthropic bets on thin harnesses and model improvement. Graph-based frameworks bet on explicit control | Anthropic regularly deletes planning steps from Claude Code's harness as new model versions internalize that capability |

## The Harness Is the Product

Two products using identical models can have wildly different performance based solely on harness design. The TerminalBench evidence is clear: changing only the harness moved agents by 20+ ranking positions.

The harness is not a solved problem or a commodity layer. It's where the hard engineering lives: managing context as a scarce resource, designing verification loops that catch failures before they compound, building memory systems that provide continuity without hallucination, and making architectural bets about how much scaffolding to build versus how much to leave to the model.

The field is moving toward thinner harnesses as models improve. But the harness itself isn't going away. Even the most capable model needs something to manage its context window, execute its tool calls, persist its state, and verify its work.

> **The next time your agent fails, don't blame the model. Look at the harness.**

## The Harness Is the Backend (iii Paradigm)

A radical alternative view emerged in April 2026 from the [[entities/iii-platform|iii platform]]: the harness should not be separate from the backend — it should **be** the backend.

**Current assumption challenged**: Most architectures treat the harness as "extrinsic to the traditional backend." The agent's loop, tools, and memory live in one layer; queues, state, HTTP routing, and observability live in another. These are connected by HTTP requests with independent retry schedules, timeouts, and traces — creating **agents² × services** stochastic paths to debug.

**The iii solution**: Three primitives — Worker, Function, Trigger — apply universally. An agent is a worker. A queue is a trigger. A sandbox is a worker. "The agent's 'tools' are functions. Its 'memory' is state. Its 'orchestration' is triggers and composition. There is no special agent infrastructure because there doesn't need to be."

**Implications for harness design**:
- Thin vs thick harness becomes a design pattern within the same system, not different architectures
- Removing scaffolding = simplifying a function, not rearchitecting an integration layer
- Categories collapse: "Queues have broker semantics, HTTP has routing semantics, agents have orchestration semantics. In iii, they are all the same thing: a process that registers functions and triggers."

This paradigm connects to the [[concepts/bitter-lesson-harnessing|Bitter Lesson of Harnessing]] — as models improve, infrastructure should collapse categories rather than add new ones. See [[entities/iii-platform]] for full details.

## See Also

- [[concepts/harness-engineering]] — The broader discipline of engineering around LLMs
- [[concepts/deep-agents-runtime]] — Production runtime primitives for deep agents
- [[concepts/agentic-ai-skills]] — Design principles for reusable agent capabilities
- [[concepts/bitter-lesson-harnessing]] — How model intelligence affects harness complexity
- [[concepts/context-engineering]] — Managing what the model sees and when
- [[entities/akshay-pachaar]] — Author of "The Anatomy of an Agent Harness"
