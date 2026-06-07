---

## Related Entities

- [[entities/scott-wu]]
title: "Akira (@realmcore_) / Random Labs"
type: entity
handle: "@realmcore_"
name: Akira (Random Labs)
created: 2026-04-13
updated: 2026-06-07
status: complete
tags:
  - person
  - coding-agents
  - rlm
sources: []
---


# Akira (@realmcore_) — Random Labs / Slate

| | |
|---|---|
| **X** | [@realmcore_](https://x.com/realmcore_) |
| **GitHub** | [github.com/random-labs](https://github.com/random-labs) |
| **Blog** | [randomlabs.ai/blog](https://randomlabs.ai/blog) |
| **Company** | Random Labs (YC S24, founded 2024 by Kiran & Mihir Chintawar) |
| **Known for** | Slate: Thread Weaving, Episodic Memory, Swarm Orchestration, Skill Chaining |
| **Bio** | AI engineering team at Random Labs. Leads Slate development. Advocates for "RLM for coding," building a third architecture beyond ReAct and RLM. |

## Overview

Akira (@realmcore_) is a key voice on the AI engineering team at **Random Labs**. The company was founded in 2024 as a YC S24 startup by **Kiran** and **Mihir Chintawar**.

Random Labs' mission is "to bring the next 20 million engineers online for software development" and is building Slate as the platform to achieve this.

## Core Ideas

### 1. Thread Weaving — A Swarm Architecture with Episodic Memory

The core of Slate is **Thread Weaving**. Just as an OS kernel manages processes, an LLM orchestrator manages threads.

> "Instead of letting RAM fill until the process crashes, each thread return is a natural opportunity to decide what gets retained, what gets compressed, and what gets discarded."

**Threads**: General-purpose workers executing one action at a time. Unlike persistent sub-agents, threads can pause and return control to the orchestrator. Context is **shared and composable**, not isolated via message passing.

**Episodes**: Compressed representations of a thread's completed action sequences. They function as **true episodic memory** and serve as natural compression boundaries.

**Thread Weaving**: The orchestrator dispatches threads → threads execute → episodes are returned → episodes become input for subsequent threads. This enables **implicit, adaptive task decomposition** rather than static planning.

### 2. RLM for Coding — Practical Application and Critical Refinement

Akira applies Alex Zhang's RLM (Recursive Language Models) to coding agents while also recognizing its limitations.

> "We built RLM for coding. And it F*cking rocks. Swarm native agents are here to stay."

**RLM's recognized limitations**:
- RLM: "Blind N-step execution" — commits full sequences without intermediate feedback
- Slate: Thread Weaving provides **intermediate state preservation**

**Random Labs' critical stance** (Agent Wars 2026-03-13):
> "Random Labs says coding agents are patching over a problem they should be solving... both paradigms [RLM and ReAct] treat context management as an afterthought. RLMs externalize data into a Python REPL and hand analysis off to sub-LLMs. ReAct agents interleave reasoning traces with action steps. Random Labs argues that neither was built for the multi-hour, multi-file sessions that real software engineering demands."

### 3. Three Foundational Problems

Random Labs has identified three fundamental problems with modern agents:

| Problem | Description | Insight |
|---|---|---|
| **Long-Horizon Tasks** | Path-dependent tasks (e.g., changes spanning multiple files) | Requires dynamic working memory, strategic planning, and intermediate adaptation |
| **Working Memory & "Dumb Zone"** | As the context window fills, LLM attention degrades non-uniformly | "The dumb zone at the right edge — attention quality degrades as the window fills." All frontier models suffer from this |
| **Strategy vs. Tactics** | Strategy = open-ended planning vs Tactics = local execution sequences | Software engineering spans this entire spectrum: `bash command execution` (tactics) vs `backward-compatible schema design` (strategy) |

### 4. Prior Approaches & Critical Failure Modes

| Approach | Mechanism | Critical Failure Mode |
|---|---|---|
| **Compaction** | Periodically drop/summarize context | **Lossy & unpredictable.** Risk of dropping critical state (Claude Code, Ralph Wiggum loop, Amp handoffs) |
| **Subagents** | Isolate context in separate agent instances | **Poor cross-context transfer.** Returns only response messages; fails to share intermediate state |
| **Markdown Planning** | Enforce pre-planned structure via files | **3 failure modes:** under-specified plans, incomplete execution, failure to adapt/update. Limited by "knowledge overhang" |
| **Task Trees (Direct Decomposition)** | Rigid gated step execution graph | **Low expressiveness & inflexibility.** Cannot adapt to new information; trades natural language flexibility for structural rigidity |
| **RLM (Recursive LM)** | Iterative/recursive execution in Python REPL | **Blind N-step execution.** No intermediate feedback; model commits full sequence upfront |
| **Multi-Agent (Devin/Manus/Altera/Codex)** | Strategize → Delegate → Compress → Synchronize | **Synchronization bottleneck.** Sync = slow; Async = coordination issues. Compression boundaries drop critical state |

### 5. Knowledge Overhang — Unlocking Latent Knowledge

> "The gap between what an LLM *knows* and what it *chooses* to do."

An approach that draws out the model's latent intelligence through proper context management and routing. Skills are activated/deactivated via **progressive disclosure** to protect the limited context space (under 200k tokens).

### 6. Skill Chaining — Dynamic Skill Definition

Critiques the traditional approach of skills as "static prompts":
> "A skill should be something the agent does not something the agent reads."

**Orchestration Skills**: User-activated skills that reference other skills to define conditional activation sequences. Enables programmatic automation workflows.

**Context Forking**:
- Interactive skills → **Fork** (blocking, UI hijack)
- Autonomous skills → **Thread** (background execution, isolated context)

⚠️ **Status**: As of April 1, 2026, forking is in **ALPHA** (delayed for reliability)

## Slate Architecture: OS Analogy (Karpathy's LLM OS Framing)

| OS Component | Slate Equivalent |
|---|---|
| Kernel | Orchestration LLM |
| RAM | Context Window (scarce, actively managed) |
| Processes | Threads |
| Return Values | Episodes (compressed state) |
| Peripherals | Files, Terminal, Web, APIs |

## Architecture Comparison

| Aspect | ReAct | Markdown Plan | Task Trees | RLM | Multi-Agent (Devin/Codex) | **Slate** |
|---|---|---|---|---|---|---|
| **Planning** | Implicit | File-based | Explicit | REPL-driven | Planning Agent | **Implicit** |
| **Decomposition** | None | None | Direct Tree | REPL Functions | Task-based | **Implicit** |
| **Synchronization** | Single-thread | Single-thread | Gated Steps | REPL Return | Reduce/Message | **Episodes** |
| **Context** | Lossy | Static | Rigid | REPL Externalized | Compressed | **Episodic** |
| **Memory** | None | None | None | None | Lossy compaction | **True episodic** |

## Key Work

### Slate V1 (March 12, 2026)
- **Terminal Bench**: 2/3 tests passed on make-mips-interpreter task (demonstrated stability in changing environments)
- **Real-world task**: TypeScript port of open-source library completed for $58.32
- **Install**: `npm i -g @randomlabs/slate`
- **Config**: `slate.json` defines model slots, permissions, MCP servers, and custom commands

### RLM for Coding
- Applied and refined Alex Zhang's RLM architecture for coding agents
- Thread Weaving solves RLM's lack of intermediate feedback

### Skill Chaining (April 1, 2026)
- Dynamically chain skills to define conditional execution sequences
- Automation workflows via Orchestration Skills
- Context Forking (Alpha)

## Connection to Harness Engineering & Agentic Engineering

Akira's Slate occupies an important position in the context of [[concepts/harness-engineering]]:

1. **Slate as a Meta-Harness**: Slate itself is a large-scale harness — integrating model routing, context management, and permission control
2. **Thread Weaving as Harness Pattern**: Each thread operates as an independent harness instance, synthesizing results via episodes
3. **Skill Chaining as Dynamic Harness**: A dynamic approach that chains skills conditionally, rather than static harness definitions
4. **Knowledge Overhang as Harness Insight**: The harness's role is to bridge the gap between "what the model knows" and "what the model actually uses"

> "Slate is not merely a wrapper or a chatbot with file access; it is an implementation of a 'hive mind' philosophy designed to scale agentic work with the complexity of a human organization."

Slate is a pioneering implementation of the "swarm orchestration" paradigm in [[concepts/agentic-engineering]], embodying the shift from single-agent models (like Devin or Codex) to parallel collaboration across multiple models.

## Related People

| Person | Relationship | Wiki Link |
|---|---|---|
| [[concepts/kiran-random-labs]] | Random Labs co-founder | — |
|  | Random Labs co-founder, CTO | — |
| (@a1zhang) | RLM developer. Slate adapts and improves RLM | [[entities/alex-zhang]] |
| [[entities/andrej-karpathy]] | LLM OS concept — origin of Slate's OS analogy | [[entities/andrej-karpathy]] |
| [[entities/peter-steinberger]](@steipete) | OpenClaw developer; related via parallel agent approach | [[entities/peter-steinberger]] |
| [[entities/nader-dabit]](@dabit3) | Cloud agents / agent fleet; related in long-running agent context | — |

## Related

- [[entities/steve-blank]] — Lean Startup methodologist; shared focus on agentic-engineering and harness-engineering patterns
- [[entities/drmaciver]] — Hypothesis creator; PBT and AI evaluation methodology
- [[entities/mitchell-hashimoto]] — HashiCorp co-founder; harness engineering pioneer
- [[entities/daniel-de-laney]] — Designer/PM; structured AI development critique

## X Activity Themes

| Theme | Content |
|---|---|
| **Thread Weaving** | Slate architecture explanations, OS analogy, episodic memory |
| **RLM for Coding** | Practical application and recognition of RLM's limitations |
| **Swarm Orchestration** | Multi-model parallel execution, hive mind philosophy |
| **Knowledge Overhang** | Unlocking latent model knowledge, importance of context management |
| **Skill Chaining** | Dynamic skill definition, Orchestration Skills |
| **Critique of Existing Agents** | ReAct/RLM limitations, importance of context management |

## Sources

- [Random Labs Blog: Slate](https://randomlabs.ai/blog/slate)
- [Random Labs Blog: Skill Chaining](https://randomlabs.ai/blog/skill-chaining)
- [Agent Wars: Moving Beyond RLM and ReAct](https://agent-wars.com/news/2026-03-13-moving-beyond-rlm-and-react-based-coding-agents)
- [VentureBeat: YC-backed Random Labs launches Slate V1](https://venturebeat.com/orchestration/y-combinator-backed-random-labs-launches-slate-v1-claiming-the-first-swarm)
- [Podcast: Slate: An Agent Architecture - Vinh Nguyen](https://www.youtube.com/watch?v=zTXWPdsiv9c)
- [Slate Documentation](https://docs.randomlabs.ai/)
