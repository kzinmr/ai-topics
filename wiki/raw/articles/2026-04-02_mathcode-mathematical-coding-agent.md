---
type: raw_article
title: "MathCode — A Frontier Mathematical Coding Agent"
source: "math-ai-org.github.io/mathcode"
source_url: "https://math-ai-org.github.io/mathcode/"
date: 2026-04-02
date_ingested: 2026-08-17
author: "math-ai-org"
tags: [coding-agents, autoformalization, formal-methods, mathematics, ai-in-science, cli, terminal, open-source, lean]
note: "Project page + GitHub README (github.com/math-ai-org/mathcode, 657 stars). Repo created 2026-04-02; surfaced on Hacker News 2026-08-16 (95 points)."
---

# MathCode — A Frontier Mathematical Coding Agent

MathCode is a terminal AI coding assistant with a built-in math formalization engine. Give it a math problem in plain language and it automatically converts it into a Lean 4 theorem and attempts a formal proof — with a persistent Lean REPL, reusable theorem and axiom libraries, agentic proving, and an Obsidian knowledge graph.

> **Project page:** https://math-ai-org.github.io/mathcode/
> **Repo:** https://github.com/math-ai-org/mathcode (657 stars, created 2026-04-02, last pushed 2026-06-15, primary language Shell/runtime bundles)

## Quick Start

Requires macOS (arm64) or Linux (x86_64), plus the `codex` CLI for the default backend.

```bash
git clone https://github.com/math-ai-org/mathcode.git
cd mathcode
bash setup.sh
codex auth login
mathcode -p "prove that the square of an even number is even"
```

Outputs are written to `LeanFormalizations/`. A browser UI is available via `./run webui`.

## Features

- **Persistent Lean REPL** — a persistent Lean language server brings compile checks to ~0.4s after a one-time warmup, instead of ~30s.
- **Theorem Library** — every proved theorem is auto-named, stored, and made importable so the prover and planner can reuse it.
- **Axiom Library** — user-managed axioms.
- **Agentic proving** — the agent plans, decomposes, and iterates on proofs rather than emitting a single-shot translation.
- **Obsidian knowledge graph** — proved results are surfaced as a navigable knowledge graph.
- **setup.sh responsibilities** — downloads/verifies (SHA-256) bundled runtime, manages a bundle-local Lean/Lake (`elan`) toolchain, installs a user-local launcher, creates `skills/`, `tools/`, `plugins/` extension directories, ships a bundled `rg` (ripgrep) binary.

## Relationship to Autoformalization

MathCode is a concrete tool in the [[autoformalization]] space: plain-language math → Lean 4 theorem → machine-checked proof. It is complementary to research frameworks such as MathForm (arXiv:2608.14221), which scale *training-data* construction via Mathlib retrieval + verification-guided refinement.
