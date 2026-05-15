---
title: "Agent Runtime as Execution Control System — Runtime ≠ Event Loop"
source: "Discord attachment (kzinmr, 2026-05-15)"
author: "kzinmr"
date: 2026-05-15
type: analysis
tags:
  - agent-runtime
  - agent-architecture
  - execution-semantics
  - orchestration
---

# Agent Runtime as Execution Control System

## 一言でいうと

この議論での runtime とは：

> **"LLM が environment と相互作用しながら長時間タスクを遂行するための execution control system"**

## 重要：runtime ≠ event loop

多くの人は runtime を asyncio / process / container / VM の意味で使う。しかしここで言っている runtime はもっと上位。近い概念は browser runtime / game engine runtime / actor runtime / distributed execution runtime。

## runtime が持つ8つの責務

### 1. Execution Lifecycle Management
agent run を管理する：start, pause, resume, cancel, retry, checkpoint, terminate

### 2. Tool Mediation
LLM ↔ tool の仲介者。tool schema, validation, execution, timeout, retries, sandboxing, auth, rate limits を管理。

### 3. State Continuity
execution identity を保持：message history, scratchpad, memory, intermediate observations, browser state, filesystem state。Agent は stateless completion ではなく persistent execution entity として扱われる。

### 4. Environment Mediation
browser session, shell session, GUI control, DOM, screenshots, filesystem を mediation する。"world interface" でもある。

### 5. Scheduling
subtask spawning, delegation, concurrency, prioritization, interruption を扱う。かなり OS 的。

### 6. Event System
token stream, tool start, tool end, approval request, delegation, retry, failure, completion を emit する。

### 7. Safety/Policy Enforcement
permissions, approval boundaries, sandboxing, quotas, isolation。

### 8. Observability
traces, spans, event logs, replayability。

## なぜ runtime が必要になったか

旧世界（completion-centric）：LLM call = atomic operation
今（agent-centric）：LLM execution = long-lived process

completion API だけでは state continuity, interruption, environment interaction, delegation, recovery を扱えない。

## Model と Runtime の分離

- **Model** = "what to do"（reasoning）
- **Runtime** = "how execution proceeds safely and continuously"（execution semantics）

Runtime は reasoning itself を持たない。持つのは execution semantics。

## Workflow Framework との違い

- **Workflow framework** は "what should happen"（実行トポロジーの記述）。LangGraph が近い
- **Runtime system** は "how execution continues"（実行継続性の維持）

## OS 比喩

runtime が process lifecycle, scheduling, I/O mediation, permissions, eventing, state management を持つから。

PI/OpenAI Agents SDK/Claude Agent SDK はすべて agent execution substrate を作ろうとしている。LangGraph は orchestration description layer に近い。

## 最も短い定義

> **"Agent を単発 completion ではなく、継続的で状態を持つ execution entity として成立させるための制御システム"**
