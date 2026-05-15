---
title: "Agent Stack Architecture — Closed/Open Harness, Harness Types, Harness vs Framework, PI as Runtime Substrate"
source: "Discord attachment (kzinmr, 2026-05-15)"
author: "kzinmr"
date: 2026-05-15
type: analysis
tags:
  - agent-runtime
  - agent-harness
  - agent-architecture
  - agent-framework
  - orchestration
---

# Agent Stack Architecture & Comparative Analysis

## 5-Layer Agent Stack Definition

```
┌────────────────────────────┐
│ Application / Product Layer │
├────────────────────────────┤
│ Agent Framework / Workflow  │
│ (LangGraph, PydanticAI)     │
├────────────────────────────┤
│ Harness / Runtime           │
│ (ClaudeCode, Codex, OpenClaw)│
├────────────────────────────┤
│ Tool / Environment Layer    │
│ (Browser, Computer, Shell)  │
├────────────────────────────┤
│ Model API                   │
│ (Claude, GPT, Gemini)       │
└────────────────────────────┘
```

This stack definition allows all comparisons to be organized as: runtime comparison, workflow framework comparison, vendor-controlled abstraction vs developer-controlled abstraction.

---

## Part 1: Closed Harness vs Open Harness (Runtime Ownership)

| Axis | Closed Harness | Open Harness |
|---|---|---|
| Examples | ClaudeCode, Codex | OpenClaw, Hermes Agent |
| Control body | Model vendor | Developer/community |
| Runtime visibility | Black box | Visible |
| Extensibility | Limited | High |
| Reliability | High | Implementation-dependent |
| Optimization | Vendor-optimized | Generic |
| Safety | Strong | User responsibility |
| Infra coupling | Strong | Weak |

### Key Thesis 1: Harness ≠ Prompt Wrapper

Harness = context management + tool execution + retries + planning + memory + environment control + streaming + interruption + state persistence.

### Key Thesis 2: Closed Harness Advantage

Closed Harness strength comes from **model-internal priors and runtime being co-optimized**. ClaudeCode is strong because Claude Sonnet has been trained on ClaudeCode trajectories, tool call style is alignment-tuned, and hidden orchestration exists. Model ↔ Harness is co-trained/co-designed.

### Key Thesis 3: Open Harness Advantage

Open Harness essence = **runtime portability**. Any model, any browser, any toolchain, any planner can be swapped in.

---

## Part 2: Harness Type Comparison (Coding vs Browser vs Computer Use vs General)

### Core Axis: "Which World Does the Harness Operate On?"

| Harness Type | Primary Environment | Environment Entropy |
|---|---|---|
| Coding Harness | filesystem/shell/git | Low (symbolic/stable) |
| Browser Harness | DOM/Web | Medium (semi-structured) |
| Computer Use Harness | GUI/OS | High (pixel-level chaotic) |
| General Harness | Mixed environment | Variable |

### System Mapping

| System | Category |
|---|---|
| ClaudeCode | Coding harness |
| Codex CLI | Coding harness |
| OpenClaw | Browser/Computer/General |
| Hermes Agent | General |
| OpenAI Operator | Computer use |
| Browser Use | Browser harness |

### The Environment Entropy Gradient

```
Low Entropy ────────────────────────────── High Entropy
Code CLI  →  Browser DOM  →  Full GUI

Entropy ↑  →  Reliability ↓  →  Autonomy cost ↑  →  Observation cost ↑
```

---

## Part 3: Harness vs Agent SDK/Framework

**Core distinction**:
- **Harness** = "runtime product" → end-user execution, product UX. **Uses** agents.
- **SDK/Framework** = "programmable orchestration layer" → developer composition, library UX. **Builds** agents.

| Axis | Harness | SDK/Framework |
|---|---|---|
| Purpose | End-user execution | Developer composition |
| UX | Product UX | Library UX |
| Primary user | Operator/user | Developer |
| Abstraction | Hidden | Explicit |
| Control | Vendor | Developer |
| Observability | Limited | High |
| Examples | ClaudeCode | LangGraph |

ClaudeCode/Codex = **agent runtime + product**. LangGraph/PydanticAI = **agent construction kit**. The comparison targets are different.

---

## Part 4: OpenClaw/Hermes vs LangGraph/PydanticAI

**Harness (OpenClaw/Hermes) = runtime-centric**:
- Execution loop, tool orchestration, browser/GUI interaction, autonomous control, planning/runtime memory

**Framework (LangGraph/PydanticAI) = workflow-centric**:
- Graph/state machine, structured outputs, deterministic orchestration, business logic integration

| Axis | Harness (runtime-centric) | Framework (workflow-centric) |
|---|---|---|
| Runtime autonomy | High | Medium |
| Determinism | Low | High |
| Environment control | Strong | Weak |
| Workflow modeling | Weak | Strong |
| Production orchestration | Medium | Strong |

---

## Part 5: PI as Runtime Substrate, Not Merely an Agent SDK

PI is doing runtime system work: execution loop, state management, task runtime, tool orchestration, environment mediation, event handling, observability, interruption/recovery. This is closer to "Agent OS".

Contrast with LangGraph/PydanticAI's graph construction, node orchestration, deterministic workflow composition — which is developer-centric orchestration.

| Axis | PI | LangGraph/PydanticAI |
|---|---|---|
| Core abstraction | Runtime | Workflow |
| Primary concern | Execution | Orchestration |
| Control center | Runtime | Developer |
| State model | Runtime-managed | Graph-managed |
| Environment coupling | Strong | Weak |
| Opinionatedness | High | Medium |
| Extensibility | Runtime extension | Workflow composition |
| Mental model | Agent OS | Orchestration library |

PI is not in the Harness↔Framework middle ground — it's firmly on the harness/runtime side. PI is trying to build an application runtime; LangGraph/PydanticAI are closer to agent topology DSLs.

### The Runtime-Centric Family

| System | Nature |
|---|---|
| ClaudeCode | Closed runtime |
| Codex CLI | Closed runtime |
| PI | Programmable runtime substrate |
| OpenClaw | Open runtime |
| Hermes Agent | Open runtime |

LangGraph/PydanticAI are workflow-centric systems.

---

## Historical Arc: Where the Agent Stack's Center of Gravity Moves

```
2023  →  Framework-centric (LangChain)
2024  →  Workflow-centric (LangGraph)
2025- →  Harness-centric (ClaudeCode/Codex/OpenClaw)
```

Agent value is shifting: **Prompt → Workflow → Runtime**.

---

## Core Message

**Model quality alone no longer determines agent capability. Runtime design increasingly dominates real-world performance.**

This frames the entire comparison as: "What is the OS/Runtime of the LLM Agent era?"
