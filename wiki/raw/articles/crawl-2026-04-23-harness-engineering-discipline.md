---
title: Harness Engineering: The Core Engineering Discipline of the AI Agent Era
category: other
status: active
---

# Harness Engineering: The Core Engineering Discipline of the AI Agent Era

**Source:** DDHigh  
**Date:** March 27, 2026  
**URL:** https://www.ddhigh.com/en/2026/03/27/ai-agent-harness-engineering/  
**Crawled:** 2026-04-23  

## 🔑 Core Definition & Industry Shift
> **Prompt engineering optimizes what the model says. Harness engineering optimizes what the model does — and more importantly, prevents it from doing what it shouldn't.**

### Prompt vs. Harness Engineering Comparison
| Dimension | Prompt Engineering | Harness Engineering |
|---|---|---|
| Scope | Single LLM call | Multi-step system + tool calls |
| Control flow | Input → Output | Input → Planning → Tool calls → Validation → Output |
| Failure mode | Wrong text generated | Wrong actions executed with real-world consequences |
| Security model | Prevent prompt injection | Full authorization system: who can do what, with what confirmation |
| State management | Stateless or simple context | Persistent memory, session management, cross-window state |

## 📊 Why Harnesses Are Critical: Real-World Incidents
Uncontrolled agents cause tangible damage. Root cause across incidents: **missing control layer**, not flawed models.
- **Replit Agent Database Deletion (July 2025):** Agent ignored explicit "stop" commands, deleted 1,206 customer records, generated ~4,000 fake records.
- **Gemini CLI File Loss (July 2025):** Moved user files to unrecoverable locations during simple organization tasks.
- **Amazon Q Supply Chain Attack (2025):** Malicious prompt injected via VS Code extension wiped local files and disrupted AWS infrastructure.
- **📈 Statistic:** AI safety incidents grew **56.4% YoY** (149 in 2023 → 233 in 2024).

## 🏗️ 5-Layer Harness Architecture

### 1️⃣ Tool Layer
- **Specialized > General-Purpose:** Claude Code uses dedicated tools (Read, Edit, Write, Glob, Grep, Bash) to prevent context bloat.
- **Description Quality:** Tool descriptions dictate agent behavior. Apply **ACI (Agent-Computer Interface)** principles: model-centric clarity, examples/edge cases, **poka-yoke (error-proofing)**.
- **Layered Registration:** Built-in tools → Lazily discovered (MCP servers) → Sub-agent specific (strict whitelists).

### 2️⃣ Context Layer
- **Living Prompts:** System prompts evolve with the project (e.g., `CLAUDE.md` managed via PRs).
- **Dynamic Injection:** Priority-ordered conditional composition based on mode, events, or provider traits.
- **Progressive Compression:** 5-stage escalation as tokens deplete (light truncation → heavy summarization). Uses **dual-memory**: episodic (full history) + working (recent observations).

### 3️⃣ Execution Layer
- **Loop Design:** `think → act → observe → think`. Choose **Workflow** (predefined paths) for predictable tasks; **Agent** (dynamic flow) for open-ended problems.
- **5 Workflow Patterns:** Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, Evaluator-Optimizer.
- **Error Recovery:** Retry with variation, escalate to human, fallback to simpler path.

### 4️⃣ Permission Layer
- **Granular Authorization:** Per-tool, per-path, per-action permissions.
- **Human Confirmation:** Required for destructive actions (delete, move, overwrite).
- **Just-In-Time:** Permissions scoped to specific tasks, not persistent.

### 5️⃣ Memory Layer
- **Long-term memory:** Persistent across sessions.
- **Session state:** Current task context.
- **Cross-session understanding:** Agent remembers project state between sessions.

## 💡 Critical Industry Insights
> On the SWE-bench benchmark, we **spent more time optimizing tools than the overall prompt itself**.

> **an agent's capability comes from the model; an agent's reliability comes from the harness.**

## 📐 Harness vs. Scaffolding
| Concept | Purpose | Analogy |
|---|---|---|
| **Scaffolding** | Pre-run assembly: system prompts, tool definitions, sub-agent registration | Construction scaffolding |
| **Harness** | Runtime orchestration: tool dispatch, context management, safety enforcement, session persistence | Reins & bridle |

## 🛠️ Tool Design (ACI Principles)
- **Model-Centric Clarity:** Tool descriptions should read like instructions for an intelligent but literal executor.
- **Edge Cases & Examples:** Include common failure modes in tool descriptions.
- **Poka-Yoke (Error-Proofing):** Make correct usage easy, incorrect usage difficult.

## 📝 CLAUDE.md Living Document Structure
```
CLAUDE.md          ← Project constitution, defines global rules
├── @AGENTS.md     ← Referenced sub-document, detailed technical specs
├── settings.json  ← Permission and environment configuration
└── Memory/        ← Persistent memory
```

## 🎯 Key Takeaways for Prerequisites
Harness engineering builds on several prerequisite concepts:
- **Context engineering** — managing token windows
- **Tool-use patterns** — designing tool interfaces
- **Multi-agent patterns** — orchestrating multiple agents
- **Sandboxing** — isolating agent execution
- **Memory systems** — persistent state management
- **Permission models** — authorization and safety
