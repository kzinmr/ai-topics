# Building Self-Improving Tax Agents with Codex

**Source:** OpenAI Blog
**URL:** https://openai.com/index/building-self-improving-tax-agents-with-codex
**Published:** May 27, 2026
**Authors:** Aravind Srinivasan & Samay Shamdasani (Thrive Holdings), Arthur Fernandes Araujo & John de Wasseige (OpenAI)

---

## Overview

Thrive Holdings and OpenAI co-developed **Tax AI**—a self-improving agent built with Codex—to automate complex tax return preparation for **Crete's network of 30+ accounting firms**. The system processed **7,000 tax returns** during pilot season, delivering continuously improving performance without heavy manual engineering intervention.

## Key Results

- **Time saved:** ~1/3 of practitioner time per return
- **Accuracy:** up to **97% field‑level correctness**
- **Throughput increase:** ~50%
- **Self‑improvement:**
  - At launch, only **25%** of returns reached 75% correct field completion.
  - Within six weeks, **86%** met that threshold.
  - Faster growth observed at 90% and 100% completion levels.
- **Real‑world impact:** One senior accountant went from **180 hours** of tax prep last year to **only 15 hours** this year, using freed time for high-touch client service and business expansion.

## The Three‑Part Self‑Improving Loop

The system transforms production use into autonomous improvement using three pillars:

### 1. Expert Practitioner Feedback
Practitioners steer what the product learns. Their corrections reveal meaningful errors and prioritize which workflows to fix next. Corrections are captured as **structured data**, not as ad‑hoc notes.

### 2. Production Traces as Evidence
The product captures the full path from source documents → extracted fields (with citations) → tax‑engine mappings → filed return. This enables field‑level comparison between the agent's prediction and the final filed value, revealing whether a practitioner correction was a true error or expected workflow noise.

### 3. Codex‑Driven Improvement Loop
Once production issues are structured, they become:
- **Eval targets** (grouped by repeated failure patterns)
- **Scoped engineering tasks** for Codex to investigate, fix, and validate.

Codex inspects the entire context (trace, repo, evals, skills) and proposes changes that are validated against targeted and regression test suites before human review.

## Rental Property Example (Schedule E)

### 1. Practitioner Correction → Failure Signal
A difference between predicted and filed rental property values is analyzed. The system distinguishes extraction misses, mapping gaps, practitioner preferences, or workflow noise.

### 2. Production Traces → Structured Evals
Corrections are processed in three steps:
- **Capture the difference** at field level (predicted vs. filed).
- **Group related failures** (e.g., repeated "fair rental days" missing).
- **Turn repeated patterns into eval targets** (targeted datasets and grader definitions).

### 3. Codex Task Environment
A bounded, writable worktree is provided to Codex alongside **read‑only production context**:

```
1/candidates/FIND-RENTAL-0042/2│3├── repo/
4│   └── branch: codex/fix-rental-0042
5│       ├── AGENTS.md
6│       ├── tasks/FIND-RENTAL-0042/
7│       │   ├── task.yaml
8│       │   ├── EXEC_PLAN.md
9│       │   └── RESULTS.md
10│       ├── app/tax-ai/rental-income/
11│       │   ├── agent.ts
12│       │   ├── schema.ts
13│       │   ├── provenance.ts
14│       │   └── mapper.ts
15│       ├── evals/
16│       │   ├── datasets/fair-rental-days.yaml
17│       │   ├── suites/fair-rental-days.yaml
18│       │   ├── suites/rental-income-regression.yaml
19│       │   └── graders/rental-income.yaml
20│       ├── skills/
21│       │   ├── eval-runner/
22│       │   └── tax-field-docs/
23│       └── docs/
24│           ├── architecture/
25│           └── task-environments/
26└── scoped-tools/
27    ├── production-trace
28    ├── source-artifacts
29    └── tax-engine-docs
```

Codex's workflow:
1. Investigate pipeline (trace, schema, mapper, grader) to find root cause.
2. Implement targeted fix (extend schema, improve source selection, update mapper).
3. Rerun targeted evals + full regression suites, propose pull request.
4. If evidence is ambiguous, route back to product team—no guesswork merged.

## Architecture Pattern

The task environment structure (AGENTS.md + task.yaml + EXEC_PLAN.md + RESULTS.md) is a reusable pattern for any Codex self-improvement workflow. It scopes the problem, provides read-only production context, and lets Codex validate its own fixes before human review.
