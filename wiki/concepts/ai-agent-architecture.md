---
title: "AI Agent Architecture"
type: concept
aliases:
  - ai-agent-architecture
created: 2026-04-25
updated: 2026-07-18
tags:
  - ai-agents
  - agent-architecture
  - enterprise-ai
  - agent-evaluation
sources:
  - raw/articles/2026-07-17-hugobowne-enterprise-ai-agent-healthcare.md
---

# AI Agent Architecture

## Overview

The architecture of production AI agents spans multiple design dimensions: how agents are structured (monolithic vs. specialist decomposition), how they are evaluated (deterministic checks, LLM judges, human calibration), how they are released (gating by consequence severity), and how they are constrained (guardrails, tool access boundaries).

## Lead Agent + Specialist Pattern

One proven architecture for enterprise AI agents is the **lead agent + specialist** pattern, where a stronger lead agent routes requests to narrower specialists rather than giving one model access to hundreds of tools. This was demonstrated by Maven Clinic's Maven Assistant for women's and family healthcare.

### Maven Clinic Case Study (2026-07-17)

William Horton, Staff AI Engineer at Maven Clinic, described the architecture on the Vanishing Gradients podcast:

**Agent Structure:**
- A lead agent routes requests to four sub-specialists:
  - Appointments
  - Provider search
  - Health questions
  - Maven support
- Only 15-20 tools total, divided across specialists
- Hard guardrails execute before dynamic routing decisions — safety checks run before routing
- Existing APIs become safer agent tools by injecting user identity and application state

**Evaluation Methodology:**
- **Failure → cheapest reliable eval escalation:** String checks for simple classifications, deterministic tool call verification, LLM judges for clinical accuracy
- **Human labels calibrate LLM judges** — consequence severity determines release threshold
- **Pragmatic release gating:** "9 out of 10 passes is acceptable for cheap failures"
- Every capability has its own evidence standard and release bar — model-provider slip, wrong tool call, and wrong health answer are treated as distinct failure modes

**Significance:**
This case study demonstrates real-world application of principles from [[concepts/agentic-engineering/]] (developer workflow decisions like tool count discipline) and [[concepts/ai-agent-engineering/]] (execution architecture like routing and guardrails). It is especially notable for its concrete evaluation methodology, which bridges the gap between theoretical agent evaluation frameworks and practical deployment requirements.

## Related Patterns

### Hard Guardrails
Safety-critical agents require guardrails that execute **before** dynamic routing. Maven Clinic runs safety checks as a pre-routing layer rather than post-hoc validation. This is related to [[concepts/harness-engineering/]]'s constraint-layer concept.

### Tool Count Discipline
Limiting tools to 15-20 total across all specialists is a deliberate architectural choice that reduces decision surface area and improves reliability. This contrasts with approaches that give one agent hundreds of tool options — see [[concepts/agentic-engineering/]] for tool-selection patterns in developer workflows.

### Consequence-Based Release Gating
Release thresholds should vary by consequence severity: cheap failures tolerate lower accuracy, while clinical errors require near-perfect performance. This is an operational instantiation of principles from [[concepts/ai-safety/]].

## See Also

- [[concepts/ai-agent-engineering/]] — Agent execution platform architecture
- [[concepts/agentic-engineering/]] — Developer workflow patterns with agents
- [[concepts/harness-engineering/]] — Execution environment design
- [[entities/william-horton]] — Staff AI Engineer at Maven Clinic (Maven Assistant architecture)
