---
title: "Spice AI"
created: 2026-06-08
updated: 2026-06-08
type: entity
tags:
  - company
  - ai-infrastructure
  - developer-tooling
  - coding-agents
  - verification
  - agentic-engineering
sources:
  - https://spice.ai/
  - raw/articles/2026-06-08_linkedin-ido-pesok_verifying-agentic-development-at-scale.md
description: "AI developer platform focused on real-time verification of agentic code generation, ensuring correctness, security, and architectural compliance at scale."
status: stub
---

# Spice AI

**Spice AI** is a developer platform company focused on solving the **verification problem** in agentic software development. Co-founded by [[entities/ido-pesok]], the company builds infrastructure that enables organizations to scale AI-assisted code generation while maintaining quality, security, and architectural compliance.

## Verification Stack

Spice AI's core product is a multi-layered verification system for AI-generated code that operates at three levels:

1. **Syntax and Type Checking** — immediate compilation and type-checking of generated code
2. **Semantic Verification** — LLM-based verification that generated code matches the intent of the request, checking API usage, data flows, and pattern adherence
3. **Architectural Compliance** — enforcement of architectural rules including dependency policies, service boundaries, and approved patterns

### Key Design Principle

Verification happens **during generation, not after**. This creates a tight feedback loop where agents self-correct in real time:

- Non-existent API calls trigger immediate correction
- Contract violations provide the contract definition for regeneration
- Security policy violations surface approved alternatives

## Team-Scale Verification

The platform supports organization-wide deployment with:

- **Team-specific rule sets** — per-team coding standards and architectural constraints
- **Shared infrastructure rules** — org-wide security policies and compliance requirements
- **Priority-based verification** — stricter checks on critical paths (payments, auth) vs. internal tools

## Reported Metrics

- **94% catch rate** before code review
- **<3% false positive rate**
- **87% self-correction rate** within two agent attempts

## Relation to Agentic Engineering

Spice AI's approach embodies the [[concepts/agentic-engineering]] principle that verification — not code reading — is the critical skill in agent-driven development. The company's verification stack is a concrete implementation of the multi-layer verification pipeline described in the agentic engineering literature.

See also: [[concepts/code-review-agents]], [[concepts/vibe-coding]]

> **Note**: Ido Pesok, co-founder of Spice AI, later joined [[entities/cognition-ai]] to work on verification capabilities in [[entities/devin]]'s virtual machine. The LinkedIn article (Spice AI) and the X article (Cognition/Devin) cover related but distinct approaches to the same problem.
