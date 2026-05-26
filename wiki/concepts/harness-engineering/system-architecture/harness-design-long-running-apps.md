---
title: "Harness Design for Long-Running Application Development"
type: concept
aliases:
  - harness-design-long-running-apps
  - generator-evaluator-pattern
  - context-resets
  - frontend-design-harness
created: 2026-04-12
updated: 2026-05-26
tags:
  - concept
  - architecture
  - harness-engineering
  - anthropic
status: draft
sources:
  - "https://www.anthropic.com/engineering/harness-design-long-running-apps"
  - "https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents"
---

# Harness Design for Long-Running Application Development

Anthropic's agent harness pattern for long-running application development, inspired by the Generator-Evaluator loop of GANs (Generative Adversarial Networks).

## Core Insight

> "Context resets—clearing the context window entirely and starting a fresh agent, combined with a structured handoff that carries the previous agent's state and the next steps—addresses both these issues."

> "Separating the agent doing the work from the agent judging it proves to be strong lever to address this issue. The separation doesn't immediately eliminate that leniency on its own... But tuning a standalone evaluator to be skeptical turns out to be far more tractable than making a generator critical of its own work."

> "Every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing."

> "The space of interesting harness combinations doesn't shrink as models improve. Instead, it moves, and the interesting work for AI engineers is to keep finding the next novel combination."

**Every component in a harness encodes an assumption about what the model cannot do on its own, and those assumptions are always worth validating. As models improve, the harness design exploration space doesn't shrink — it shifts.**

## Two Failure Modes for Long-Running Tasks

### 1. Context Degradation and "Context Anxiety"

As context fills up, models suffer from:
- **Loss of coherence**: Decreasing coherence in long tasks
- **Context anxiety**: Tendency to wrap up work early when approaching context limits
- **Compaction limits**: Summary-based compression preserves coherence but cannot eliminate residual anxiety

**Solution**: Context resets (completely restarting the agent) + structured state handoff

### 2. Self-Evaluation Bias

> LLMs are lenient judges of their own work.

- Generator agents tend to evaluate their own work leniently
- Particularly pronounced in subjective tasks (design, etc.)
- When a single agent both generates and evaluates, this bias is amplified

**Solution**: Separate the generator and evaluator agents

## GAN-Inspired Frontend Design Harness

**Inspiration**: Generator-Evaluator loop from Generative Adversarial Networks (GANs)

### Architecture

```
Generator → Evaluator (Playwright MCP for live testing) → Score & Critique → Generator (revise)
```

### 4 Evaluation Criteria

| Criterion | Description |
|---|---|
| **Design Quality** | Coherent whole with consistent mood/identity across colors, typography, layout, images |
| **Originality** | Custom decisions, not template/library defaults. Explicitly penalize "AI slop" (purple gradients on white cards, etc.) |
| **Craft** | Technical execution: typography hierarchy, spacing, contrast ratios |
| **Functionality** | Usability independent of aesthetics (clear primary actions, intuitive navigation) |

### Key Findings

- **Evaluation criteria alone improve output**: Even the first iteration exceeded baseline just by having clear evaluation criteria
- **Prompt wording determines convergence**: Phrases like "museum quality" shape output direction
- **Iteration**: 5-15 cycles where the Generator makes strategic decisions (score rising → refinement, approach failing → pivot)

## 3-Agent Full-Stack Architecture

Scaling the GAN-inspired pattern to autonomous software engineering:

```
Planner → Generator (sprint) → Evaluator/QA (Playwright MCP)
```

### Planner
- Expands 1-4 sentence prompts into ambitious high-level product specs
- Avoids cascading errors by skipping detailed technical specifics
- Weaves AI capabilities into specifications

### Generator
- Works in sprint units (one feature at a time)
- Self-evaluates before QA
- Version-controlled with Git
- Communicates via file-based handoffs

### Evaluator (QA)
- Click-through tests live application with Playwright MCP
- Tests against **sprint contracts** (negotiated before coding) and evaluation criteria
- Triggers failure thresholds and detailed bug reports

### Communication Flow
```
Generator: Propose implementation
  → Evaluator: Review
  → Both: Agree on contract
  → Generator: Build
  → Evaluator: Test
  → Feedback loop
```

## Model Evolution and Harness Design

| Era | Characteristics | Harness Design |
|---|---|---|
| **Opus 4.5** | Pronounced context anxiety | Context resets + strict sprint decomposition required |
| **Opus 4.6** | Better planning, debugging, long task persistence | Context resets and sprints can be removed. SDK auto-compaction enables continuous sessions |

> Opus 4.6 nearly eliminated context anxiety, enabling work in continuous sessions. The Evaluator's role also shifted from per-sprint to single end-of-run pass.

## Effective Harnesses for Long-Running Agents (2-Agent Pattern)

### Problem: Memory Gap

> "The core challenge of long-running agents is that they must work in discrete sessions, and each new session begins with no memory of what came before."

### Solution: Initializer Agent + Coding Agent

The **same agent harness** is used, but with **different initial prompts:**

| Agent | Role |
|---|---|
| **Initializer Agent** | Scaffolds environment, creates tracking artifacts, baseline git commit |
| **Coding Agent** | Incremental single-feature work. Maintains clean mergeable state |

### Key Artifacts

| File | Purpose |
|---|---|
| `feature_list.json` | Comprehensive breakdown of all features. Initial state: all `"passes": false` |
| `claude-progress.txt` | Log of completed work, decisions, and next steps per session |
| `init.sh` | Script for starting the development server and running baseline tests |
| `git` repository | Version control (descriptive commit messages) |

### Session Workflow

1. `pwd` → Confirm working directory
2. Read `claude-progress.txt` and `git log` → Understand recent state
3. Read `feature_list.json` → Select one incomplete highest-priority feature
4. Run `init.sh` → Start development server
5. Run basic end-to-end tests → Verify core functionality is not broken
6. Implement feature → Commit & update progress log

### Failure Modes and Mitigations

| Problem | Initializer Fix | Coding Agent Fix |
|---|---|---|
| Early project completion | Creates `feature_list.json` with all features at `"passes": false` | Reads list, selects one feature per session |
| Buggy/undocumented state | Sets up git repo and `claude-progress.txt` | Reads logs/progress, runs baseline tests, commits with clear messages |
| Unverified features | Sets up feature list | Self-validates end-to-end. Only marks `"passes": true"` after testing |
| Setup time waste | Writes `init.sh` for server startup | Runs `init.sh` immediately at session start |

## Key Lessons

1. **Model improvements don't shrink the harness design exploration space** — it only shifts
2. **Separation of generation and evaluation** is a particularly powerful lever for subjective tasks
3. **Context resets** can be more effective than mere compression
4. **Structured state handoffs** (files, git, progress logs) bridge the gap between sessions
5. **Explicit evaluation criteria alone** significantly improve output quality
6. **Harnesses must be designed for model characteristics** (different approaches for Opus 4.5 vs 4.6)

## Related Concepts

- [[concepts/harness-engineering]] — Top-level index
- [[concepts/building-effective-agents]] — Fundamental principles of agent building
- [[concepts/multi-agent-research-system]] — Multi-agent systems
- [[concepts/context-engineering]] — Context engineering
- [[comparisons/evals-skills]] — Evaluation skills
