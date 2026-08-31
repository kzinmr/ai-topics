---
title: "Pointer AI"
created: 2026-05-31
updated: 2026-08-31
type: entity
tags:
  - company
  - ai-agents
  - open-source
  - computer-use
sources:
  - "[[raw/articles/2026-05-26_pointer-osworld-sota]]"
  - "[[raw/articles/2026-05-31_may-june-trending-topics]]"
  - https://www.pointer.ai/blog/sota
related:
  - concepts/computer-use
  - entities/anthropic
  - concepts/agent-safety
---

# Pointer AI

**Pointer AI** is an AI company focused on [[concepts/computer-use|computer use agents]] — AI systems that operate computers like humans do, across GUIs, terminals, and browsers. In May 2026 it achieved the two highest **verified** scores ever recorded on the OSWorld benchmark, and released its agent system fully open source.

## Key Achievement (May 26, 2026)

- **83.6% on OSWorld** with Claude Opus 4.7 — versus the human baseline of 72.4%
- **81.5% on OSWorld** with Claude Sonnet 4.6 — both runs clear all previously published agents
- Top score in **7 of 10** OSWorld task domains
- **VS Code domain: 95.7%**, **Multi-apps: 74.4%** (the field mean in multi-app is ~10 points lower)
- Fully open source system release (the harness, not the underlying Claude models)

The multi-apps category — orchestrating workflows across several applications — is Pointer's strongest differentiator, and matches the company's stated thesis that cross-application coherence, not raw per-step perception, is the bottleneck for computer use.

## Architecture

A lightweight **task controller** orchestrates three specialized agents, each of which can be backed by a swappable model:

| Agent | Default Model | Role |
|-------|--------------|------|
| **Feasibility Gate** | Sonnet 4.6 | Decides task feasibility *before* work begins — 85.7% recall on impossible tasks, 99.4% specificity |
| **Planner** | Sonnet 4.6 | Breaks goals into state-based milestones |
| **Executor** | Opus 4.7 / Sonnet 4.6 | Does the actual work with unified tools (GUI, code, browser, background execution) |

### Design Principles

- **GUI-first**: prefer pixel-level interaction mirroring human behavior, falling back to code/CLI tools where more reliable
- **"Two strikes then switch"**: after two failed attempts at an approach, the executor must switch modality/strategy rather than retry blindly
- **Feasibility gating as safety + economics**: refusing impossible tasks early avoids wasted compute and hallucinated "success" — an explicit verification-first stance (see [[concepts/agent-safety]])
- **Model-agnostic executor**: different models measurably excel at different domains; the harness is designed so the executor backend can be swapped per-domain

A notable finding from the system's traces: **phantom tool calls** — roughly 5% of tool calls target tools that were never provided to the agent, an artifact ingrained in Claude's post-training. Pointer documents this as a case for harness-level tool-verification rather than prompt fixes.

## Company Profile & Hiring Focus

Pointer presents itself as a small research-heavy team. Its job openings (as of the SOTA post) map directly onto its technical roadmap:

- Computer use agent research
- **Verifying agent work** (evaluation/grounding of agent claims)
- Self-improving systems
- Coherence over long horizons

## Context

Pointer's May 2026 result was one of the standout trending items of the month (recorded in [[raw/articles/2026-05-31_may-june-trending-topics]]), arriving weeks after OpenAI and Anthropic had been trading the OSWorld lead. It is a clean example of the **harness-over-model** pattern: frontier Claude models plus a well-engineered orchestration layer, open-sourced so the result is reproducible.

## Related Pages

- [[concepts/computer-use]] — Computer use agents and the OSWorld benchmark
- [[entities/anthropic]] — Claude models used as Pointer's brain
- [[concepts/agent-safety]] — Verification and feasibility-gating
- [[concepts/harness-engineering]] — Pointer as harness-first engineering

## Sources

- [Pointer — A New State of the Art for Computer Use](https://www.pointer.ai/blog/sota) (2026-05-26) — raw: [[raw/articles/2026-05-26_pointer-osworld-sota]]
- [[raw/articles/2026-05-31_may-june-trending-topics]] — trending survey entry (§6)
