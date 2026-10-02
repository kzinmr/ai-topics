---
title: "HEXIS: Skills as Executable State Machines"
created: 2026-09-27
updated: 2026-09-27
type: concept
tags: [agent-skills, agent-harness, ai-agents, agent-evaluation]
aliases:
  - HEXIS
  - Skills as State Machines
  - Knowledge-Control Separation
sources:
  - raw/articles/2026-09-27_arxiv_2609.30123_hexis-skills-into-fsm.md
related:
  - concepts/agent-skills.md
  - concepts/skillopt.md
  - concepts/agent-harness-primitives.md
  - concepts/harness-engineering/context-engineering.md
confidence: medium
contested: false
---

# HEXIS: Skills as Executable State Machines

**HEXIS** (arXiv:2609.30123, Vuong & Ngo, 2026) is the concrete instance of
**knowledge–control separation**: compiling an agent *skill* (a markdown instruction
document) into an **extended finite state machine (FSM)** so that *what to do* lives in
state-local instructions, while *what comes next* is decided by explicit transition
conditions and recorded machine state — not by the LLM re-inferring progress from
context every turn.

## The Problem: Native Skill Execution Couples Knowledge and Control

A skill document encodes both **knowledge** (how to perform an operation) and **control
requirements** (order, dependencies, branching, repetition, termination). Native
execution (`Skill + ReAct`) feeds both into context and asks the model to *select the
next operation* each step. That single decision entangles applying task knowledge,
recovering current progress, identifying applicable control rules, and choosing an
action — so the model frequently omits required steps or acts out of order. Supplying
requirements as context *influences* the choice but does not *enforce* it.

## The Mechanism

1. **Incremental compiler** maps skill clauses + tool interfaces into FSM states
   (operations, local instructions, data bindings) and transitions (branch/repeat/
   terminate conditions). It then aligns development *execution traces* to existing
   states to find missing operations/dependencies, adding or reusing states.
2. **Acceptance gate** `A_k = Check(M') ∧ ⋀ Replay(M', r)` — an update is committed only
   after **static checks** (structure, variable dependencies, terminal evidence, declared
   constraints) *and* successful **replay** of the new trace plus *all* previously
   accepted traces. This makes the compiler conservative: it cannot silently break
   behavior it already handled.
3. At runtime the model only does **in-state reasoning/generation**; the machine supplies
   "where am I, what's allowed next", cutting the need to reconstruct state from history.

## Results

- **Success:** +16.1 percentage points over `Skill + ReAct` on average across 4
  benchmarks × 4 executors. Machines compiled from `qwen3.6-flash` executions transfer
  *unchanged* to other backbones — improving in **15 of 16** settings, leading/tie in 11.
- **Cost:** Qwen3.8-27B execution tokens reduced **38.4–88.9%**, because the machine
  (not repeated context re-derivation) supplies the next-step signal.
- **Composition:** HEXIS + [[concepts/skillopt]] (skill optimization) reaches **84.2%**
  on SpreadsheetBench — the two are orthogonal: one optimizes skill *content*, the other
  enforces skill *control flow*.

## Interpretation for This Wiki

HEXIS is a **knowledge/control separation** thesis for agent skills — the same theme
running through [[concepts/agent-harness-primitives]] (harness owns control, model owns
generation) and [[concepts/agent-skills]]. Treating skills as *programs* (FSMs) rather
than prompts converts compliance from a probabilistic hope into a checked artifact:
progress state, static checks, and replay acceptance give a **compile-time guarantee**
for skill adherence. Token savings are a downstream benefit of not re-inferring state.
The knowledge-vs-control split also makes agent behavior more **auditable** — a theme
shared with [[concepts/agent-trace-integrity]].

## Open Questions

- Does trace-guided compilation scale to skills whose control flow is genuinely open-ended
  (creative tasks), or only to procedural ones (spreadsheets, service flows)?
- Where is the boundary between HEXIS-style compiled FSMs and plain
  [[concepts/harness-engineering/context-engineering|context engineering]]? Both manage
  what the model sees per step; HEXIS additionally enforces transition legality.
