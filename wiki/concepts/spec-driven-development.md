---
title: "Spec-Driven Development"
type: concept
aliases:
  - spec-driven-development
  - spec-first-development
  - spec-first
created: 2026-04-25
updated: 2026-08-06
tags:
  - concept
  - software-engineering
  - ai-coding
  - workflow
  - documentation
  - verification
related:
  - concepts/ai-assisted-development
  - concepts/agentic-engineering
  - entities/eleanor-berger
  - entities/hugo-bowne-anderson
sources:
  - raw/articles/2026-03-31_hugobowne_top-questions-about-ai-assisted-software.md
---

# Spec-Driven Development

## Overview

**Spec-driven development** is the practice of writing an explicit specification — goal, scope, constraints, success criteria, and expected output artefacts — *before* asking an AI model to implement a task. It is the discipline of defining success up front rather than letting the model improvise a solution. The format can vary (a careful prompt, a plan, a PRD, an implementation brief); what matters is that the spec exists, is reviewable, and precedes the code.

The practice gained renewed prominence with AI-assisted coding: a good spec is what turns an AI from an improviser into a collaborator with a map (Eleanor Berger, "Top Questions About AI-Assisted Software Development", Mar 2026).

## The Spec as Contract

A good spec answers the same basic questions:

- What are we trying to achieve, and why?
- What is in scope, and what is explicitly **not** in scope (non-goals)?
- Which files, systems, or inputs matter?
- Which constraints must be respected (conventions, architecture, security)?
- What tests or checks must pass?
- What output should the agent produce — code changes, docs, a PR, an issue comment, a report?

For a small task the contract may just be a careful prompt. For larger work it should become a proper Markdown artefact — a plan, PRD, or implementation brief. The format matters less than clarity and reviewability.

## Precise Incompleteness

Specs must be **calibrated, not maximal**:

- **Under-specified** tasks give the model too much freedom and invite misalignment (ambiguous scope → the agent changes more than intended).
- **Over-specified** tasks trap the agent inside irrelevant implementation detail and stop it from finding simpler solutions.

The sweet spot is *precise incompleteness*: enough detail to define the target and the boundaries, enough freedom to let the model solve the problem.

### Common specification bugs

- **Ambiguous scope** — the agent changes more than intended
- **Implicit assumptions** — domain knowledge obvious to the human but written nowhere
- **Under-constrained style** — output works but does not fit the project conventions
- **Missing exit conditions** — the agent keeps going past the intended stopping point
- **Insufficient context** — the agent reinvents things that already exist

## A Practical Spec Template

1. **Goal** and why it matters
2. **Scope** and explicit non-goals
3. Relevant **inputs, files, or references**
4. **Constraints** and acceptance criteria
5. **Tests and checks** to run
6. Expected **output artefacts**

## Agent-Written Specs (Spec-First Loop)

AI lowers the cost of spec-driven development in a distinctive way: you can use an **interactive agent to write the specification for a background agent**. Ask the first agent to analyse the codebase, identify affected files, draft a plan, and sharpen the constraints; then hand that refined spec to a second agent to execute.

This hints at a broader trajectory: as agents improve, the durable artefact may increasingly be the specification and the recorded intent around it, with code generated or regenerated just-in-time for a task. Good specs become *more* valuable, not less.

## Relationship to Other Concepts

- **[[concepts/ai-assisted-development]]** — Spec-driven development is one of the core practice patterns of AI-assisted development (Q4 of the ten-question playbook).
- **[[concepts/agentic-engineering]]** — Spec-first workflows are a central agentic-engineering pattern; the spec is the primary human control surface for agent delegation.
- **[[entities/dspy]]** — DSPy's declarative signature/module approach is a programmatic cousin of spec-first development (specifying inputs/outputs/constraints instead of prompt text).

## Sources

- Eleanor Berger, "Top Questions About AI-Assisted Software Development" (Vanishing Gradients, Mar 31, 2026). [[raw/articles/2026-03-31_hugobowne_top-questions-about-ai-assisted-software.md]]
