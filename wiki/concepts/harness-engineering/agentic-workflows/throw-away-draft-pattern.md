---
title: "Throw-Away First Draft Pattern"
type: concept
aliases:
  - throw-away-draft
  - throwaway-first-draft
  - draft-compare-iterate
created: 2026-04-12
updated: 2026-05-26
tags:
  - concept
  - agentic-engineering
status: draft
sources:
  - "https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/"
---

# Throw-Away First Draft Pattern

A development pattern where you have the agent **write a throw-away draft first**, compare it with your mental model, then iterate with refined prompts.

## Core Principle

> *"Create branch, let CC build end-to-end, compare vs. mental model, then iterate with refined prompts."*
> — Sankalp

Instead of crafting perfect instructions for a one-shot completion, **first let the agent freely write and learn from its output**.

## Why Write a "Throw-Away Draft"?

### 1. Mental Model Validation

Exposes the **gap** between your intended specification and what the agent understood.

```
Your Mental Model        Agent's Output
       ↓                        ↓
   "How it should be"    ←→    "How it was implemented"
              ↓ Analyze the gap
         Identify "what was different"
              ↓
       Re-implement with corrected instructions
```

### 2. Instruction Precision Improvement

When your initial prompt was imprecise, seeing the agent's output reveals **where the ambiguity was**.

### 3. Unexpected Discoveries

Agents sometimes propose **approaches humans never considered**. The throw-away draft lets you discover new ideas.

## Practice Steps

### Step 1: Clarify Requirements

```bash
# First ask the agent questions to solidify requirements
$ claude "What are the edge cases for this feature?"
```

### Step 2: Create a Branch

```bash
$ git checkout -b draft/feature-x
```

### Step 3: Let It Implement End-to-End

```bash
# Let the agent write freely with minimal instructions
$ claude "Implement feature X based on the requirements we discussed"
```

### Step 4: Compare with Mental Model

```bash
# Review the diff
$ git diff main
# Run tests
$ python -m pytest tests/
```

### Step 5: Iterate with Improved Instructions

```bash
# Analyze the gap and give more precise instructions
$ claude "The date parsing is off. Use ISO 8601 format, not US format. Also, handle null cases explicitly."
```

### Step 6: Discard the Branch if Needed

```bash
# If the agent's approach was completely wrong
$ git checkout main
$ git branch -D draft/feature-x
# Start over on a new branch
$ git checkout -b draft/feature-x-v2
```

## Relationship with Sankalp's Workflow

Sankalp uses tools in the following division of labor:

| Tool | Role | Relationship to Throw-Away Draft |
|--------|------|------------------------|
| **Claude Code** | Main driver | Draft creation & iteration |
| **GPT-5.2-Codex** | Review & bug discovery | Draft validation |
| **Cursor** | Manual editing & reading | Final polish |

## Differences from Traditional Development

| Traditional Development | Throw-Away Draft |
|-----------|-----------------|
| Write perfect specs first | Let the agent write first |
| Aim for one-shot completion | Iteratively improve |
| Humans write code | Humans write instructions |
| Bugs found later | Assume bugs from the start |

## Caveats

### The Draft Must Be "Throw-Away"

- Isolate in a branch
- Don't merge to main (create an improved version)
- Don't take agent output at face value

### Mental Model Comparison is Critical

- Don't assume agent output is "correct"
- Analyze how it differs from your understanding
- Learning from differences makes your next instructions more precise

## Related Concepts

- [[concepts/context-window-management]] — Throw-away drafts consume context
- [[concepts/harness-engineering/agentic-workflows/cli-first-development]] — Writing drafts via CLI speeds up validation
- [[concepts/harness-engineering/agentic-engineering]] — Parent concept

## References

- [[entities/sankalp-sinha]] — Originator of the Throw-Away First Draft pattern
- [A Guide to Claude Code 2.0](https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/)
