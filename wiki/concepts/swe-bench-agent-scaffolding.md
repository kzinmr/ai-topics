---
title: "SWE-bench Agent Scaffolding (Claude 3.5 Sonnet)"
type: concept
created: 2026-05-08
updated: 2026-05-26
tags:
  - benchmark
  - architecture
  - anthropic
  - evaluation
  - coding-agents
aliases:
  - SWE-bench Sonnet agent
  - minimal agent scaffold
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_swe-bench-sonnet.md
  - https://www.anthropic.com/engineering/swe-bench-sonnet
related:
  - swe-bench
  - agent-harnesses
  - coding-agents
  - building-effective-agents
---

# SWE-bench Agent Scaffolding (Claude 3.5 Sonnet)

The agent design used by Claude 3.5 Sonnet to achieve 49% on SWE-bench Verified (beating the then-SOTA of 45%). Its design philosophy: **Delegate as much control as possible to the model itself, keeping scaffolding minimal.**

## Agent Architecture

### Components
- **Prompt**: Suggests approaches but is not excessively long or detailed
- **Bash Tool**: Shell command execution (simple schema, heavy on description)
- **Edit Tool**: File and directory viewing and editing
- **Loop**: Continues until the model decides it is "done" or exceeds the 200K context window

### Design Philosophy

> Rather than forcing it to follow hardcoded patterns or workflows, let the model choose its own problem-solving approach.

### Prompt

```
<uploaded_files>{location}</uploaded_files>
I've uploaded a python code repository in the directory {location}.
Consider the following PR description:
<pr_description>{pr_description}</pr_description>

Follow these steps to resolve the issue:
1. Explore the repo to familiarize yourself with its structure.
2. Create a script to reproduce the error and execute it
3. Edit the sourcecode of the repo to resolve the issue
4. Rerun your reproduce script and confirm that the error is fixed!
5. Think about edgecases and make sure your fix handles them as well

Your thinking should be thorough and so it's fine if it's very long.
```

### Bash Tool Design

Simple schema (command string only), but detailed instructions in the description:
- Input escaping
- Explicit no internet connection
- Background execution method
- Handling long-running commands

## Key Insights

> SWE-bench evaluates not just the model, but the **entire agent system**. The same model performance varies dramatically depending on the scaffolding.

Open-source developers and startups have achieved significant improvements by optimizing scaffolding around the same model ([[agent-harnesses|Harness Effect]]).

## SWE-bench vs SWE-bench Verified

| | SWE-bench | SWE-bench Verified |
|---|---|---|
| Problem Count | 2,294 | 500 |
| Quality | Includes problems needing context outside GitHub issues | Human-reviewed, solvable problems only |
| Purpose | Broad evaluation | Clear coding agent performance measurement |

## Results

- Claude 3.5 Sonnet (upgraded): **49%** on SWE-bench Verified
- Previous SOTA: 45%
- Closing in on breaking the barrier: "no model has yet exceeded 50%"

## See Also

- [[concepts/swe-bench]] — SWE-bench benchmark overview
- [[concepts/frontier-swe-benchmark]] — Frontier SWE benchmark
- [[agent-harnesses]] — Agent harness comparison
- [[concepts/building-effective-agents]] — Building effective agents (Anthropic)
- [[concepts/coding-agents]] — Coding agents overview
