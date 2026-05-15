---
title: "Agent Harness"
created: 2026-04-27
updated: 2026-05-15
tags:
  - harness-engineering
  - architecture
  - ai-agents
aliases: [agent-harness, harness-anatomy, agent-scaffolding]
sources: [
  "https://x.com/akshay_pachaar/status/2041146899319971922",
  "https://x.com/i/article/2041146899319971922",
  "raw/articles/2026-04-28_the-harness-is-the-backend.md",
  "raw/articles/2041146899319971922_the-anatomy-of-an-agent-harness-.md",
  "raw/articles/2026-the-self-healing-agent-harness.md",
  "raw/articles/2026-the-ai-cake-trade.md",
  "raw/articles/crawl-2026-04-18-token-economics.md",
  "raw/articles/2026-is-s3-faster-than-a-file-system.md",
  "raw/articles/2026-05-02_atalupadhyay-agent-harness.md",
  "raw/articles/2026-05-06_vtrivedy10_strong-opinions-agent-harness-engineering.md",
  "https://x.com/vtrivedy10/status/2052100726608781363",
  "raw/articles/2026-05-02_codekartik-why-everyone-building-agent-harness.md",
  "https://x.com/code_kartik/status/2050631735529095575",
  "raw/articles/2026-05-09_addyosmani-agent-harness-engineering.md",
  "https://x.com/addyosmani/status/2053231239721885918",
  "raw/articles/2026-05-14_kzinmr_open-harness-vs-agent-framework.md",
  "raw/articles/2026-05-15_kzinmr_agent-runtime-execution-semantics.md",
  "raw/articles/2026-05-15_kzinmr_agent-stack-architecture-comparative-analysis.md",
  "raw/articles/2026-05-15_kzinmr_why-runtime-centric-now-control-flow-ownership.md"
]
---


# Agent Harness

## Summary

The **agent harness** is the complete software infrastructure wrapping an LLM: orchestration loop, tools, memory, context management, state persistence, error handling, and guardrails. The term was formalized in early 2026. As LangChain's Vivek Trivedy put it: "If you're not the model, you're the harness."

The harness is not the agent itself — it's the machinery that produces agentic behavior. When someone says "I built an agent," they mean they built a harness and pointed it at a model.

### Harness vs Runtime: The Critical Distinction

A subtle but essential architectural distinction, formalized by kzinmr (2026-05-15): the **harness** and the **runtime** are different layers, though the boundary is often blurred in practice.

| | Harness | Runtime |
|---|---|---|
| **Core question** | *What does the agent attempt?* | *How does execution proceed?* |
| **Primary concern** | Orchestration: tools, prompts, loops, context, memory, verification | Execution control: lifecycle, tool mediation, state continuity, scheduling, events, safety, observability |
| **Owns** | The agent's behavior and capabilities | The agent's continuity and safety as a persistent execution entity |
| **Analogy** | The program logic | The operating system kernel |

The harness decides which tools to call and in what order. The runtime manages whether those calls are allowed, how they execute, what state persists across them, and how execution recovers from failure. In Han Lee's formulation: "The agent is the harness plus the model, running inside the runtime."

**The deeper distinction (kzinmr, 2026-05-15)**: This is not merely a layering question — it's a question of **who owns control flow**. In the workflow-centric era, the developer held control flow authority because models were unreliable primitives (tool misuse, context drift, loop collapse). In the runtime-centric era, models can *maintain execution semantics* — tool continuation, long-horizon tasks, retry adaptation — which means the runtime can shift from "constraining an unreliable model" to "mediating a capable model's execution." The harness still decides *what to attempt*, but the model now safely owns *what happens next*, and the runtime mediates *how it happens safely*. See [[concepts/agent-runtime#why-now-control-flow-ownership-and-the-real-shift]].

> **Workflow framework vs runtime**: LangGraph is closer to a **workflow framework** — it describes *execution topology* (what should happen). Claude Agent SDK and PI are closer to **runtimes** — they maintain *execution continuity* (how execution proceeds). See [[concepts/agent-runtime]] §"Execution Semantics: The Control System Layer" for the full analysis.

### Closed Harness vs Open Harness: Runtime Ownership

The first-order architectural divide in the harness landscape is **who owns the runtime** — the model vendor or the developer community. This distinction (kzinmr, 2026-05-15) cuts across individual harness comparisons and explains fundamental differences in extensibility, reliability, and optimization strategy.

| Axis | Closed Harness | Open Harness |
|---|---|---|
| **Examples** | ClaudeCode, Codex CLI | OpenClaw, Hermes Agent, PI |
| **Control body** | Model vendor | Developer / community |
| **Runtime visibility** | Black box | Fully visible |
| **Extensibility** | Limited (vendor-gated) | High (any model/tool/planner) |
| **Reliability** | High (vendor QA) | Implementation-dependent |
| **Optimization** | Vendor-tuned (model-specific) | Generic (portable) |
| **Safety model** | Strong (vendor-enforced) | User responsibility |
| **Infra coupling** | Strong (vendor cloud) | Weak (BYOK, local, self-hosted) |

#### The Closed Harness Advantage: Co-Training / Co-Design

The closed harness's strength is not merely engineering quality — it's **co-optimization**. ClaudeCode is powerful because:

- Claude Sonnet has been trained on ClaudeCode trajectories — the model has learned the specific tool call patterns, error recovery strategies, and interaction rhythms of its native harness
- Tool call style is alignment-tuned — the model and harness share an implicit contract about how tools should be invoked and how results should be interpreted
- Hidden orchestration exists — the harness can make decisions the developer never sees, informed by model-internal priors

> **Model ↔ Harness is co-trained / co-designed.** This is the closed harness's moat — and its lock-in mechanism.

#### The Open Harness Advantage: Runtime Portability

The open harness's strength is **substitutability**. Any model, any browser, any toolchain, any planner can be swapped in. This means:

- No vendor lock-in on model selection
- Can optimize for cost (local, cheapest provider) without changing workflow
- Can adopt new models immediately without waiting for vendor integration
- The harness asset (AGENTS.md, memory, skills, gateway routing) is portable across infrastructure

> **Open Harness = runtime portability as a first-class property.**

### Harness Type Comparison: Environment Abstraction

Harnesses differ not only in ownership but in **which world they operate on**. This is the environment abstraction dimension (kzinmr, 2026-05-15).

| Harness Type | Primary Environment | Environment Entropy | Key Characteristics |
|---|---|---|---|
| **Coding Harness** | filesystem / shell / git | Low (symbolic, stable) | Deterministic tool outputs, structured data, version-controlled state |
| **Browser Harness** | DOM / Web | Medium (semi-structured) | Dynamic pages, async rendering, CDP protocol, session state |
| **Computer Use Harness** | GUI / OS | High (pixel-level chaotic) | Screenshot-based observation, coordinate-based action, fragile selectors |
| **General Harness** | Mixed environment | Variable | Switches between environments, must handle all entropy levels |

#### System Mapping

| System | Category |
|---|---|
| ClaudeCode | Coding harness |
| Codex CLI | Coding harness |
| PI | Coding harness (with extension to browser/computer via extensions) |
| OpenClaw | Browser / Computer / General |
| Hermes Agent | General (coding + browser + system) |
| OpenAI Operator | Computer use |
| Browser Use | Browser harness |

#### The Environment Entropy Gradient

This is the critical insight for harness design: **as environment entropy increases, reliability decreases, and both autonomy cost and observation cost increase.**

```
Low Entropy ─────────────────────────────────────── High Entropy
Code CLI  →  Browser DOM  →  Full GUI

Entropy ↑  →  Reliability ↓  →  Autonomy cost ↑  →  Observation cost ↑
```

- **Coding harnesses** operate in the lowest-entropy environment: files are deterministic, shell commands have predictable outputs, git provides version history. This is why coding agents consistently score highest on benchmarks — the environment is the most amenable to reliable automation.
- **Browser harnesses** face semi-structured chaos: pages change, selectors break, JavaScript renders asynchronously. Reliability drops but remains manageable with CDP-level control.
- **Computer use harnesses** face the highest entropy: pixel-level observation, coordinate-based action, no symbolic representation of UI state. Every screenshot is a new problem. This is why computer-use agents remain the least reliable category.

This entropy gradient explains why **coding harnesses reach production first** — not because the problems are easier, but because the environment is more tractable. The same harness engineering principles apply across the gradient, but the cost of reliability scales with entropy.

**Source**: kzinmr, "Agent Stack Architecture & Comparative Analysis" (2026-05-15), [[raw/articles/2026-05-15_kzinmr_agent-stack-architecture-comparative-analysis]].

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

## Atal Upadhyay's 9-Component Framework (May 2026)

[[entities/atal-upadhyay|Atal Upadhyay]] proposed a canonical decomposition of an agent harness into 9 core components in his guide "The Agent Harness: What It Is, Why It Matters, and How to Build One from Scratch":

| # | Component | Role |
|---|-----------|------|
| 1 | **The `while` Loop** | Heartbeat managing Decide→Act→Observe cycle; requires `max_iterations` |
| 2 | **Context Management** | Token budgeting with compaction (summarizing old turns, keeping recent verbatim) |
| 3 | **Tools & Skills Registry** | Map of capabilities with schemas and permission levels |
| 4 | **Sub-Agent Management** | Isolated sessions for parallel/complex tasks to prevent single-thread choking |
| 5 | **Built-In Skills** | OOTB capabilities: file ops, code navigation |
| 6 | **Session Persistence** | Append-only logs (JSON/Markdown) for crash recovery |
| 7 | **System Prompt Assembly** | Dynamic injection of project-specific rules into static core prompt |
| 8 | **Lifecycle Hooks** | Pre/post-tool hooks for auditing, modifying, or blocking actions |
| 9 | **Permissions & Safety** | Hierarchy (read/workspace/full) requiring human approval for destructive actions |

Upadhyay's framework complements the industry analysis above by providing a **build-from-scratch** reference architecture, including a minimal Python implementation demonstrating each component. His distinction between frameworks (building blocks) and harnesses (working agents out of the box) reinforces the central theme: the harness determines agency, not the model.

Key implementation insights from the framework:
- **Prefix Caching**: Always place the static core prompt first — changing dynamic content order invalidates cache, causing 3-5x latency spikes
- **Semantic Compaction**: Use a smaller LLM to summarize history while preserving function signatures and error traces
- **Command Classification**: Parse shell commands via AST/shlex (not string matching) to prevent permission bypass

> "Don't just prompt the model. Engineer the loop. The harness is where agency becomes reliable." — Atal Upadhyay

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

### Viv Trivedy's Synthesis (May 2026)

[[entities/vtrivedy10|Viv Trivedy]]'s 8-point "Strong Opinions" ([source](https://x.com/vtrivedy10/status/2052100726608781363)) reframes the harness landscape with three key extensions:

1. **No general purpose agent exists** (Point 2-3) — What's called "general purpose" is just "decently good at many tasks out of the box," which ultimately converges on a good coding agent with the right tool set.

2. **Convergence on Skills** (Point 4) — As models improve at in-context learning, task-specific harness optimization packages into discrete Skills (prompt + tool design), reducing harness complexity while preserving task performance.

3. **Subagents as Tools** (Point 8) — The harness becomes a configurable box populated with specialist subagent-tools (WarpGrep, Chroma Context, Nemotron) rather than a monolithic runtime. See [[concepts/unbundled-agents]].

These points extend the framework's core argument: the harness determines agency, not the model. As harnesses evolve toward skill-based composition and subagent-as-tool architectures, the design challenge shifts from "how do I run this agent" to "what tools/subagents do I configure for this task."

## The Seven-Plane Production Harness (Kartik, May 2026)

[[entities/kartik-labhshetwar|Kartik Labhshetwar]] proposed an alternative decomposition of a production harness into seven architectural planes in his essay "[Why Everyone Is Suddenly Building Their Own Agent Harness](https://x.com/code_kartik/status/2050631735529095575)":

| # | Plane | Function | Key Insight |
|---|-------|----------|-------------|
| 1 | **Agent Loop** | ReAct, plan-execute, generate-test-repair | The heartbeat; all intelligence lives in the model |
| 2 | **Tool Layer** | Purpose-built for LLMs, not humans | Replit switched from function calling to a restricted Python DSL → 90%+ valid call rate |
| 3 | **Context & Memory** | Progressive disclosure with multi-timescale memory | Cursor spends weeks tuning per-model context behavior |
| 4 | **Sandbox** | Permission-gated execution | Strict enforcement at the tool boundary |
| 5 | **Multi-Agent** | Coordination and sub-agent orchestration | Each subagent returns condensed 1-2K token summaries |
| 6 | **Evals & Tracing** | Product-specific evaluation and observability | Generic benchmarks (SWE-bench) miss product-specific failures |
| 7 | **Prompt & Model Routing** | Dynamic model selection and prompt assembly | Frontier labs have structural conflict with efficiency optimizations |

**The shared design pattern**: trust the LLM at the reasoning layer, enforce strictly at the tool boundary.

This seven-plane view complements Upadhyay's 9-component framework (above) by focusing on the **production deployment** concerns — sandboxing, multi-agent coordination, and model routing — that become critical at scale but are often absent in reference implementations.

### Scale Evidence

When Claude Code's source map briefly leaked in March 2026, the harness (everything around the model) came to **~513,000 lines of TypeScript**. The actual model API call: a few lines. This 500,000:1 ratio of harness to model invocation is the clearest evidence that the harness — not the model — is where the engineering weight lives.

The term "agent harness" was coined by [[entities/mitchell-hashimoto|Mitchell Hashimoto]] in early 2026. His definition: "Anytime an agent makes a mistake, you engineer a solution so it never makes that mistake again. That fix lives in the harness." See [[concepts/why-harness-development-boom]] for a synthesis of the structural forces driving harness development.

## The Harness Is the Backend (iii Paradigm)

A radical alternative view emerged in April 2026 from the [[entities/iii-platform|iii platform]]: the harness should not be separate from the backend — it should **be** the backend.

**Current assumption challenged**: Most architectures treat the harness as "extrinsic to the traditional backend." The agent's loop, tools, and memory live in one layer; queues, state, HTTP routing, and observability live in another. These are connected by HTTP requests with independent retry schedules, timeouts, and traces — creating **agents² × services** stochastic paths to debug.

**The iii solution**: Three primitives — Worker, Function, Trigger — apply universally. An agent is a worker. A queue is a trigger. A sandbox is a worker. "The agent's 'tools' are functions. Its 'memory' is state. Its 'orchestration' is triggers and composition. There is no special agent infrastructure because there doesn't need to be."

**Implications for harness design**:
- Thin vs thick harness becomes a design pattern within the same system, not different architectures
- Removing scaffolding = simplifying a function, not rearchitecting an integration layer
- Categories collapse: "Queues have broker semantics, HTTP has routing semantics, agents have orchestration semantics. In iii, they are all the same thing: a process that registers functions and triggers."

This paradigm connects to the [[concepts/bitter-lesson-harnessing|Bitter Lesson of Harnessing]] — as models improve, infrastructure should collapse categories rather than add new ones. See [[entities/iii-platform]] for full details.

## The Ratchet: Every Mistake Becomes a Rule (*Addy Osmani, May 2026*)

The most vital habit in harness engineering, as articulated by [[entities/addy-osmani|Addy Osmani]] in "[Agent Harness Engineering](https://addyosmani.com/blog/agent-harness-engineering/)" (April 2026), is treating agent mistakes as **permanent signals** — not one-off flukes to retry and forget. This is the **Ratchet pattern**:

> If an agent ships a PR with a commented-out test that gets merged by accident, that is an input. The next iteration of AGENTS.md must state: "Never comment out tests; delete or fix them." The next pre-commit hook should automatically flag `.skip(` in the diff. The reviewer subagent must be updated to block commented-out tests.

**Core principles**:
- Constraints are only added when you observe a **real failure** — never preemptively
- Constraints are removed only when a **capable model renders them redundant**
- Every line in a good system prompt should trace back to a **specific, historical failure**
- Harness engineering is a **discipline**, not a one-size-fits-all framework — the right harness for a specific codebase is shaped by its **unique failure history**

This sharpens Mitchell Hashimoto's original definition ("Anytime an agent makes a mistake, you engineer a solution") by specifying that **removal is as important as addition** — outdated scaffolding must be pruned when models internalize the capability it addressed.

## Working Backwards from Behavior

Osmani proposes a design methodology: **start with the desired behavior and build the component that delivers it**.

> Behavior we want → Harness design to achieve it.

Every piece of the harness must have a distinct, nameable job. If you cannot articulate the specific behavior a component exists to deliver, it should be removed. This cleanly connects to the thick vs thin harness debate: the question isn't absolute thickness, but whether each component traces to a real behavioral requirement.

## Hooks as the Enforcement Layer

Hooks bridge the gap between **requesting** an action and **enforcing** it. They operate at specific lifecycles:

| Hook Point | What It Enforces | Example |
|------------|-----------------|---------|
| **Before tool call** | Destructive command blocking | Block `rm -rf /` in sandbox |
| **After file edit** | Auto-formatting, lint-on-save | Run `prettier` after every `.ts` edit |
| **Before commit** | Test suite gate, type checking | Block commit if `tsc --noEmit` fails |

**Design principle**: Success is silent, failures are verbose. If a typecheck passes, the agent hears nothing. If it fails, the error is injected directly back into the loop for self-correction.

## Tool Discipline: Ten Focused Beats Fifty Overlapping

- **Ten highly focused tools always outperform fifty overlapping ones**
- Tool descriptions populate the agent's prompt — **malicious or sloppy external integrations** (unverified MCP servers) can inject bad prompts before the agent even starts working
- Every tool must have a distinct job that traces back to a behavioral requirement

## Harness-as-a-Service (HaaS)

Osmani identifies a fundamental industry transition: from building on **LLM APIs** (completions) to building on **Harness APIs** (runtimes).

SDKs now offer the loop, tools, context management, hooks, and sandboxes out of the box. The modern default:
1. **Select** a harness framework (Claude Code, Codex, OpenCode, Flue)
2. **Configure** its core pillars (prompts, hooks, tools)
3. **Focus** purely on domain-specific prompt and tool design

This makes troubleshooting scalable: tuning a well-factored configuration surface rather than reinventing the entire agent architecture. Frameworks like [[entities/fred-schott|Flue]] (TypeScript-native harness framework) and LangChain's Deep Agents CLI exemplify the HaaS transition.

## The Convergence Dynamic

Top coding agents look **more like each other than their underlying models do**. The models differ significantly, but harness patterns converge on load-bearing scaffolding: loops with self-verification, filesystem-as-state, sandboxed execution, subagent delegation, context compaction, hook-based enforcement.

Osmani predicts the next phase: harnesses stop being static configuration files and start acting like **compilers**. Open problems:
- **Multi-agent orchestration** in parallel
- **Self-analytic agents** that inspect their own traces to fix harness-level failures
- **Just-in-time tool assembly** — dynamically composing tools based on task requirements

Fareed Khan's ([estimated] breakdown of Claude Code's architecture)[https://levelup.gitconnected.com/building-claude-code-with-harness-engineering-d2e8c0da85f0] maps every concept to a named architectural component: context injection = knowledge layer, loop state = memory store + worktree isolator, hooks = permission gate, subagent firewalls = multi-agent layer, tool dispatch = MCP + bash registry.

## Agent Harness と Agent Framework/SDK の本質的差異

> このセクションは kzinmr による包括的分析（[[comparisons/open-harness-vs-agent-framework]]、2026-05-14）に基づく。Open Harness（OpenClaw, Hermes Agent, OpenCode, Pi）と Agent Framework/SDK（Claude Agent SDK, OpenAI Agents SDK, Google ADK, Strands Agents, LangGraph, Pydantic AI）の差異を概念レベルで整理する。

### 2つの投資対象

| | Open Harness | Agent Framework / Runtime |
|---|---|---|
| **投資先** | 人間がAI Agentを**使う**操作環境・作業面 | AI Agentを**システムに組み込む**制御基盤 |
| **柔軟性** | **広い柔軟性**: モデル切替、CLI/チャット選択、MCP追加、プロンプト変更 | **深い柔軟性**: 型付き状態管理、graph遷移、checkpoint、副作用制御、tenant境界 |
| **Securityの質** | **Operator Safety** — 信頼された人間の操作安全性 | **Product/Tenant Safety** — 不特定ユーザー・複数tenantの安全性 |

### Operator Workbench と Product Runtime の2軸評価

Harness系とFramework系の評価は、単一の「Security/Control/Opsスコア」ではなく、**用途に応じた2軸**で行う必要がある:

1. **Operator Workbench Readiness** — 信頼された人間がAI Agentを安全に使う作業環境としての成熟度
   - この軸では OpenClaw（gateway/control plane）、Hermes Agent（persistent ops agent）、OpenCode（coding workbench）は高評価
2. **Untrusted Product Runtime Readiness** — 不特定ユーザー・複数tenant・顧客向けSaaS・本番業務ワークフローに耐えるruntimeとしての成熟度
   - この軸では LangGraph（stateful durable execution）、Pydantic AI（typed application framework）、OpenAI Agents SDK が有利

**結論**: Harnessを本番agent backendとして低めに見るのは妥当だが、operator workbenchとして低めに見るのは不当。

### 4種類のロックイン

| ロックイン種別 | 例 | 対策 |
|---|---|---|
| **モデルロックイン** | Claude Agent SDK（Claude依存）、OpenAI Agents SDK（Responses API依存） | model routing layer分離 |
| **SDKロックイン** | Frameworkの抽象（handoff, guardrail, graph state） | 良い抽象へのロックインは許容。state, eval dataはSDK外 |
| **Harnessロックイン** | Open Harnessの設定資産（AGENTS.md, extension, memory, skills, gateway routing） | 中核業務ロジック・状態はharness外に保持 |
| **クラウドロックイン** | Google ADK（GCP）、Strands（AWS/Bedrock） | agent state, tool API, audit logをクラウド固有機能に閉じ込めない |

### 推奨分離アーキテクチャ

```
Human Interface / Harness Layer  (OpenClaw / Hermes / OpenCode / Pi)
        ↓
Tool Boundary  (MCP / HTTP APIs / typed function tools)
        ↓
Agent Control Layer  (LangGraph / Pydantic AI / OpenAI Agents SDK / etc.)
        ↓
State & Governance Layer  (DB / audit logs / eval datasets / approval records)
        ↓
Execution Layer  (containers / sandbox / serverless / Kubernetes)
```

**設計原則**: **Harnessを捨てても業務ロジックが残る**ようにする。

### 選定指針

- **Open Harness優先**: AI Agentを人間の作業環境に入れたい場合（開発者生産性、CLI/チャット操作、モデル試行錯誤）
- **Framework / Runtime優先**: AI Agentをプロダクト/業務システムに組み込みたい場合（顧客向け機能、監査、状態管理、本番SLA）
- **ツール別最適シナリオ**: 詳細は [[comparisons/open-harness-vs-agent-framework]] の §7 を参照

## See Also

- [[concepts/harness-engineering]] — The broader discipline of engineering around LLMs
- [[concepts/deep-agents-runtime]] — Production runtime primitives for deep agents
- [[concepts/agent-runtime]] — The execution environment where harness + model operate: isolation primitives, sandbox landscape, runtime shift, runtime debt
- [[concepts/agentic-ai-skills]] — Design principles for reusable agent capabilities
- [[concepts/bitter-lesson-harnessing]] — How model intelligence affects harness complexity
- [[concepts/context-engineering]] — Managing what the model sees and when
- [[concepts/why-harness-development-boom]] — Why harness engineering is accelerating (five structural forces)
- [[entities/kartik-labhshetwar]] — Author of "Why Everyone Is Suddenly Building Their Own Agent Harness"
- [[entities/mitchell-hashimoto]] — Coined the term "agent harness"
- [[concepts/unbundled-agents]] — Viv Trivedy's subagents-as-Tools pattern
- [[entities/akshay-pachaar]] — Author of "The Anatomy of an Agent Harness"
