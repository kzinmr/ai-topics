---
title: "Reduce, Offload, Isolate"
type: concept
aliases:
  - "Reduce Offload Isolate"
  - "Agent Context Engineering Principles"
  - "Context Engineering Playbook"
created: 2026-05-13
updated: 2026-05-13
status: l2
tags:
  - context-engineering
  - ai-agents
  - harness-engineering
  - anthropic
  - model
  - langchain
sources:
  - https://hugobowne.substack.com/p/ai-agent-harness-3-principles-for
  - https://rlancemartin.github.io/2025/06/23/context_engineering/
  - https://rlancemartin.github.io/2026/01/09/agent_design/
  - wiki/raw/articles/2025-12-12_hugobowne_agent-harness-context-engineering.md
related:
  - concepts/context-rot
  - concepts/agent-harness-comparison
  - concepts/harness-commoditization
  - concepts/unharnessed-agents
  - concepts/harness-engineering/context-engineering
  - entities/claude-code
  - entities/manus
  - entities/lance-martin
  - entities/hugo-bowne-anderson
---

# Reduce, Offload, Isolate

**The 3 Principles** is a context engineering playbook articulated by **Lance Martin** (Anthropic, prev. LangChain) on the **High Signal** podcast with Hugo Bowne-Anderson (Dec 2025). It captures the battle-tested strategies used by leading agentic systems — including **Claude Code** and **Manus** — to manage the fundamental tension between growing context windows and degrading model performance ("[[concepts/context-engineering/context-rot|context rot]]").

## The Core Problem: Context Rot

Even models with million-token context windows suffer from **context rot**: instruction-following ability degrades significantly as the context grows. The *effective* context window is often substantially lower than the stated technical one. Simply appending tool call results to a growing message history is expensive, slow, and degrades performance.

> *"Often the effective context window for these LLMs is actually quite a bit lower than the stated technical one."* — Lance Martin

## The 3 Principles

### 1. Reduce — Shrink the Context

Actively minimize what's passed to the model on each turn.

**Techniques:**
- **Trajectory summarization**: Compress entire agent history into a summary once it reaches a certain size. Older steps are replaced with condensed notes.
- **Tool call compaction**: Keep only the essential results of older tool calls; discard verbose raw outputs.
- **Selective retention**: Drop intermediate reasoning steps that are no longer relevant to the current task.

**Example**: Claude Code compacts its message history periodically, keeping only critical state. Manus tracks "cache hit rate" as its most important production metric — reducing context size reduces cost AND improves quality simultaneously.

### 2. Offload — Move Out of the Prompt

Push information and complexity OUT of the LLM's context window into external systems.

**Techniques:**
- **Filesystem as external memory**: Write full tool results to disk; read back selectively when needed. This prevents context bloat from verbose tool outputs.
- **Offload the action space**: Instead of giving an agent 100 different tools (which bloats the system prompt), give it a few atomic tools like a **bash terminal**. The model can execute a vast range of commands without cluttering context.
- **Deterministic pre/post-processing**: Compute what can be computed outside the LLM (parsing, validation, formatting).

**Example**: Pi's philosophy — 4 tools (read/write/edit/bash) instead of dozens. Claude Code gives agents a full bash shell rather than individual tools. This is the "Give agents a computer" pattern Martin describes in his agent design patterns post.

### 3. Isolate — Delegate to Sub-Agents

Use multi-agent architectures to isolate token-heavy work into independent contexts.

**Techniques:**
- **Sub-agent delegation**: A main agent offloads a complex job to a specialized sub-agent. The sub-agent works in its own isolated context and returns only a **concise result**.
- **Ralph Wiggum loop** (coined by Geoffrey Huntley): Agents iterate on plans stored in files, each iteration in a fresh context.
- **Independent context windows**: Each sub-agent gets a clean context focused on its narrow sub-task — no context pollution from the main agent's history.

**Example**: Anthropic's multi-agent research system — many agents with isolated contexts outperformed a single agent, largely because each sub-agent's context window could be allocated to a narrow sub-task.

## Production Evidence

### Manus: 5 Re-Architectures Since March 2024

The popular AI agent **Manus** has been fundamentally re-architected five times since its launch in March 2024, driven by the relentless improvement of underlying models. Each re-architecture stripped away complexity that the model no longer needed.

### Claude Code: Anthropic Rips Out the Harness

> *"Anthropic rips out Claude Code's agent harness as models improve"* — Lance Martin

Anthropic maintains Claude Code by **removing** harness features as models get smarter, not adding them. This is the **Bitter Lesson applied to harness design**: general methods (better models) eventually overtake handcrafted systems (complex harnesses). The harness should be a **shrinking scaffold**, not an accumulating feature set.

### Open Deep Research: Multiple Rebuilds

LangChain's **Open Deep Research** agent was rebuilt multiple times in a single year to keep pace with model improvements.

## The Bitter Lesson Connection

Rich Sutton's **Bitter Lesson** — that general methods leveraging computation ultimately win over handcrafted, complex systems — now applies at the **application layer**. The architectural assumptions baked into an application today will likely be obsolete in six months when a more capable model is released.

This creates a fundamental design tension:
- **Today**: Good context engineering (Reduce/Offload/Isolate) is the highest-leverage skill for agent builders
- **Tomorrow**: Models will absorb these patterns, making today's harness engineering obsolete

The imperative is not to build the perfect harness, but to build a harness designed to be **stripped away**.

## Relationship to Martin's Earlier Framework

Martin's earlier "Context Engineering for Agents" (June 2025) organized strategies into **Write, Select, Compress, Isolate**. The High Signal "Reduce, Offload, Isolate" reframes and condenses this:

| Earlier (Jun 2025) | Reduce/Offload/Isolate (Dec 2025) |
|---|---|
| Write (save context outside window) | → Offload (filesystem as external memory) |
| Select (pull right context in) | → (implicit in Reduce — only what's needed) |
| Compress (retain only needed tokens) | → Reduce (trajectory summarization, compaction) |
| Isolate (split across sub-agents) | → Isolate (unchanged, reinforced) |

The evolution reflects the deepening understanding that **context is the scarcest resource** in agent systems.

## Implications for Agent Design

1. **Start with minimal tools** — 4 primitive tools (read/write/edit/shell) beat 100 specialized tools. The model extends itself when needed.
2. **Design for deletion** — Build harness features expecting to remove them. Every harness addition should have a planned removal trigger.
3. **Test against model generations** — A harness should show performance improvement when tested against progressively more capable models. If not, the harness is a bottleneck.
4. **Context budget as first-class constraint** — Treat context tokens like memory in embedded systems. Profiling tools should track context utilization per agent step.

## Inner Loop vs Outer Loop (Jeff Huber's Extension)

**Jeff Huber** (Chroma CEO) extended the context engineering framework with a temporal dimension in his Vanishing Gradients conversation with Hugo Bowne-Anderson (Mar 2026):

- **Inner Loop**: What information to put into context for a **single task, right now**. This is the tactical, per-request curation problem — Reduce/Offload/Isolate applied at the level of each agent step.
- **Outer Loop**: Building systems that get **better at filling context over time**. The strategic, learning-oriented problem. The "machine that builds the machines."

> *"It's both figuring out what do I put into context this time. That's the inner loop. And then it's how do I get better at context filling over time. And that is the outer loop."* — Jeff Huber

The outer loop implies:
- **Continuous improvement**: Systems that learn from feedback and adjust their context engineering strategies
- **From 90% to 99.9%**: Moving from internal-tool reliability to user-facing product reliability
- **Unsolved evaluation**: Agent evaluation remains the bottleneck — LLM-as-judge is not a panacea; manual labeling is brittle

This framework is complementary to Reduce/Offload/Isolate: the 3 principles are *how* you engineer context; the inner/outer loop distinction is *when and how you improve* that engineering over time.

See [[entities/jeff-huber]] for Huber's full framework and background.

## Related Concepts

- [[concepts/context-engineering/context-rot|Context Rot]] — The degradation of LLM instruction-following as context grows
- [[concepts/agent-harness-comparison]] — Comparative analysis of major agent harnesses
- [[concepts/harness-commoditization]] — Thorsten Ball's thesis: harness differentiation is dying as models absorb features
- [[concepts/unharnessed-agents]] — John Berryman's anti-harness thesis
- [[concepts/harness-effect]] — Same model, different harness = 5-40pp performance difference
- [[concepts/harness-engineering/context-engineering]] — Martin's comprehensive 4-bucket taxonomy (Write/Select/Compress/Isolate)

## See Also

- [[entities/lance-martin]] — Author of the framework
- [[entities/hugo-bowne-anderson]] — Host of the High Signal conversation
- [[entities/claude-code]] — Production example of harness simplification
- [[entities/manus]] — 5x re-architected agent
