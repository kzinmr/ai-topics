---
title: "LLM-Assisted Development"
type: concept
aliases:
  - llm-assisted-development
created: 2026-04-25
updated: 2026-06-07
tags:
sources: []
  - concept
status: live
---

# LLM-Assisted Development

LLM-Assisted Development refers to the practice of using large language model coding agents (Claude Code, Codex, Cursor, etc.) to write, refactor, and maintain software under human direction and review. The field has rapidly matured from early experiments to practical methodology, with experienced practitioners documenting specific workflows, heuristics, and pitfalls.

## Core Paradigms

### Greenfield Projects vs. Rewrites

A critical distinction drawn by experienced practitioners is the difference between using LLMs for **greenfield projects** (new from-scratch development) vs. **rewrites** (restructuring existing codebases). These two paradigms demand different workflows:

- **Rewrites** benefit from existing test suites as safety nets — the LLM can be given a conformance suite and asked to produce code that passes all tests. The human defines the contract via tests; the LLM fills in the implementation.
- **Greenfield projects** require upfront design documentation, deliberate CL (change list) size discipline, and a test suite built from scratch as the first task. Without existing tests, the human must design the test strategy before the LLM writes any production code.

### Design Docs in Markdown

For greenfield projects, committing a Markdown design document into the repository is a recommended practice. The human iterates on the design with the agent using this document, which serves as a persistent reference for both human and AI throughout the project lifespan. This creates a shared understanding that survives context window resets.

### CL Size Discipline

Keeping change lists small and reviewable is critical when working with agents. The temptation to sprint ahead submitting thousands of lines daily must be resisted — coding with an agent is like speed-reading: more progress is made, but comprehension suffers the faster one goes. A disciplined workflow:

1. Ask the agent to write CLs in a logical order, keeping them small
2. Commit a CL, then go back and ask the agent to modify/refactor in separate CLs
3. Use source control branches as safety nets for complex scenarios
4. Accept that sometimes a single CL is a huge step forward requiring hours of cleanup

### Human-in-the-Loop: Two Categories

Projects should be split into two categories with different workflows:

1. **Low-importance / prototype / throwaway**: Can be "vibe-coded" — submitting agent code without review
2. **High-importance / maintainable**: Requires full review and guidance of all agent-written code before submission

For category (2), a reliable workflow is running a CLI agent locally in the repository while keeping a VSCode window open for real-time diff review. The human makes their own tweaks alongside the agent's changes, then manually commits.

### Testing Strategy

A solid test suite is the single most important success factor for LLM-assisted development:

- For rewrites: leverage existing conformance suites (pycparser had 2500+ lines of test code)
- For greenfield: build the test suite FIRST — adapt existing spec suites or build from scratch
- **Beware of self-reinforcing loops**: trusting agents for both tests AND implementation creates a dangerous feedback cycle

### Language Choice

Go is particularly well-suited for LLM-assisted development because:

- It changes infrequently — no need to wonder about "modern/idiomatic" approaches
- Few ways to accomplish the same thing, lowering mental burden
- Rich standard library reduces dependency churn
- Designed for readability with mild-but-strong typing and explicit error propagation
- When working with agents, the human spends ~99% reading vs 1% writing, so readability is paramount

### Junior vs. Senior Guidance

- **Senior engineers** benefit most from agents — it eliminates the "potential well" of mental overhead that prevents tackling known projects. Agents increase productivity, avoid boredom, and overcome procrastination.
- **Junior engineers** should exercise extreme caution. Learning a new subject requires working through it from scratch. Agents cannot learn for the user. There is no replacement for hard-won experience.

## Key Principles

- **Comprehensive test suites enable safe delegation**: The more exhaustive the tests, the more safely implementation can be delegated to an LLM
- **Strong typing aids LLM agents**: Static type information helps coding agents produce correct code (Go, TypeScript, Rust particularly benefit)
- **Boring technology gets better AI augmentation**: Tools with decades of accumulated training data (LaTeX, C, Python, SQL) benefit more from LLMs than new technologies with sparse training coverage
- **Maintaining code is more than writing it**: Even if writing costs go down, maintenance (bug triage, design thinking, code health) remains human-intensive

## Sources

- eli.thegreenplace.net--2026-thoughts-on-starting-new-projects-with-llm-agents--7d421bbe
- eli.thegreenplace.net--rewriting-pycparser-with-llm--source
