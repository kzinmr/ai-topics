---
title: "MathCode"
created: 2026-08-17
updated: 2026-08-17
type: concept
tags: [coding-agents, agents, autoformalization, formal-methods, mathematics, ai-in-science, cli, terminal, open-source]
sources:
  - raw/articles/2026-04-02_mathcode-mathematical-coding-agent.md
---

# MathCode

**MathCode** is a terminal AI coding assistant with a built-in math formalization engine. Given a math problem in plain language, it automatically converts it into a **Lean 4** theorem and attempts a formal proof. It is a concrete [[concepts/autoformalization|autoformalization]] tool, pairing an LLM backend (the `codex` CLI by default) with a persistent Lean proof environment.

## What It Does

The core loop: plain-language problem → Lean 4 theorem statement → agentic proof attempt → machine-checked result, written to a `LeanFormalizations/` directory.

Key components:

- **Persistent Lean REPL** — a persistent Lean language server cuts compile-check latency to ~0.4s after warmup (vs ~30s cold).
- **Theorem Library** — every proved theorem is auto-named, stored, and made importable so the prover and planner can reuse prior results.
- **Axiom Library** — user-managed assumptions.
- **Agentic proving** — planning, decomposition, and iteration rather than single-shot translation.
- **Obsidian knowledge graph** — proved results surface as a navigable graph.

## Positioning

MathCode is an *agent* in the [[concepts/coding-agents/coding-agents|coding agent]] family, specialized for mathematical formalization rather than general software engineering. Unlike research frameworks that focus on training data (e.g., [[concepts/autoformalization|MathForm]]'s FormalVerse dataset), MathCode is an end-user tool: it runs locally (macOS arm64 / Linux x86_64), downloads a bundle-local Lean/Lake toolchain, and drives proving interactively.

This mirrors a broader pattern of domain-specialized coding agents — the same way general agents have been specialized for competitive programming and theorem proving, MathCode specializes the harness for [[concepts/ai-mathematics-theorem-proving|mathematical theorem proving]].

## Release and Reception

The repository was created 2026-04-02 (657 GitHub stars) and surfaced on Hacker News on 2026-08-16 (95 points). It is distributed as bundled runtime binaries with SHA-256 verification, and exposes a browser UI via `./run webui`.

## Related

- [[concepts/autoformalization]] — the technique MathCode operationalizes
- [[concepts/ai-mathematics-theorem-proving]] — AI theorem proving and TCS
- [[concepts/alphaproof-nexus]] — theorem-proving model lineage
- [[concepts/coding-agents/coding-agents]] — coding agent landscape
