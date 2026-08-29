---
title: "Datalog"
type: concept
aliases:
  - datalog
created: 2026-04-25
updated: 2026-08-29
tags:
  - concept
  - formal-methods
  - agent-memory
  - memory-systems
sources:
  - raw/articles/2026-08-28_pwning-systems_llm-memory-as-program-analysis.md
status: complete
---

# Datalog

## Overview

Datalog is a **declarative logic programming language**: instead of writing instructions for *how* to compute, you declare **facts** and **rules** from which new facts are derived, then compute a **fixed point** containing everything derivable. A key property exploited by program analysts: when an input fact changes, incremental techniques update only the affected results instead of recomputing from scratch.

## Datalog as an LLM Memory Substrate

Pseudonymous security researcher **pwning.systems** (Aug 28, 2026, HN 164 pts) built a **Datalog engine for LLMs** after hours-long vulnerability-research sessions kept revealing the failure mode of transcript/RAG-style agent memory: the model keeps reasoning from retracted observations. Storing facts, conclusions, and later corrections in a vector store leaves the LLM to "hope" retrieval surfaces the right subset and that it correctly figures out which conclusions are still valid.

The insight: this is exactly the **program-analysis** setting. Facts like `calls(foo, bar)` + a transitivity rule derive new facts; invalidating an input fact invalidates dependents automatically. Applied to agent memory: `attacker controls object_a` + `object_a points to object_b` derive `attacker can control a kernel object` — and when LLDB later shows `object_a` doesn't point to `object_b`, a **dependency-tracking materialization** engine marks every derived conclusion invalid without the LLM reconstructing the investigation. See [[concepts/materialized-agent-memory]] for the full pattern.

## Related Pages

- [[concepts/materialized-agent-memory]] — the agent-memory pattern built on Datalog
- [[concepts/formal-methods]] — formal methods in AI/agent engineering
- [[concepts/ai-agent-memory-middleware]] — agent memory middleware landscape
