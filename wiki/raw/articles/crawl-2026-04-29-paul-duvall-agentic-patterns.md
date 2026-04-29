# Agentic AI Patterns Reinforce Engineering Discipline

**Source:** InfoQ
**URL:** https://www.infoq.com/news/2026/03/agentic-engineering-patterns
**Date:** March 2026
**Author:** InfoQ Editorial Team (reporting on Paul Duvall, Paul Stack, Gergely Orosz)
**Type:** News Article / Engineering Report

---

## Summary

Paul Duvall (author of "Continuous Integration"), Paul Stack (System Initiative), and Gergely Orosz discuss how agentic AI is not replacing engineering discipline but rather making core practices like TDD, trunk-based development, and automated validation more critical than ever.

## 1. The Shift in Engineering Discipline

As AI increases the volume and velocity of code generation, traditional manual reviews become impractical. Engineering quality shifts from human inspection to **automated validation and agentic guardrails**.

- **Core Practices:** Trunk-based development, frequent commits, and automated testing are essential to manage the high rate of change
- **Validation over Review:** Duvall: "You're putting in mechanisms... such that the code is reviewed... but it might not be reviewed literally by you every single time"
- **Red, Green, Refactor (XP Revival):** AI workflows are replicating Extreme Programming (XP) patterns — the agent literally follows "red, green, refactor"

## 2. Specification-Driven Development

Vague prompts lead to "random results." To achieve consistency, developers must provide agents structured, high-fidelity intent:

- **Intent Definition:** Structured prompts describing Role, Context, and Constraints
- **Agent-Readable Specs:** Define expected behavior and acceptance criteria upfront so agents can validate their own output
- **Issue-Based Workflows:** Paul Stack suggests moving away from traditional PRs toward collaborative design via issues
- **Plan Mode:** Using Claude's "plan mode" to review intent before execution prevents "AI horror stories"

## 3. Key Agentic Engineering Patterns

Paul Duvall's [repository of patterns](https://github.com/paulDuvall/ai-development-patterns):

| Pattern | Description |
|---------|-------------|
| **Specification-Driven** | Defining behavior and constraints before generation |
| **Codified Rules** | Embedding architectural constraints into agent context |
| **Atomic Decomposition** | Breaking tasks into small parts for parallel agents |
| **Observable Development** | Using automated traceability and production telemetry |
| **Ralph Loops** | Sub-agents iteratively refining until requirements met |

## 4. Shift-Left and Shift-Right Integration

- **Shift-Left:** Provide accurate architectural patterns so agents produce code coherent with existing codebase
- **Shift-Right:** Use AI to analyze production telemetry expansively, identifying issues fed back as new requirements

## 5. The Future of Engineering Role

- **Team Size:** Move toward "one pizza teams" as coordination overhead decreases
- **Identity:** Engineers move "up a level" beyond code itself
- **Taste:** Human "architectural and design taste" remains critical for high-stakes systems
