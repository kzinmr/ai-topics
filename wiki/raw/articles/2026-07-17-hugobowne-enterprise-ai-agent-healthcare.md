---
title: "Building an Enterprise AI Agent for Healthcare"
author: "Hugo Bowne-Anderson"
date: 2026-07-17
source_url: "https://hugobowne.substack.com/p/building-an-enterprise-ai-agent-for"
podcast: "Vanishing Gradients"
tags: [ai-agents, enterprise-ai, healthcare, agent-architecture, evals, agent-evaluation, maven-clinic]
---

# Building an Enterprise AI Agent for Healthcare

**Author:** Hugo Bowne-Anderson (Vanishing Gradients podcast)
**Date:** 2026-07-17
**Source:** https://hugobowne.substack.com/p/building-an-enterprise-ai-agent-for

## Summary

Interview with William Horton, Staff AI Engineer at Maven Clinic, about building Maven Assistant — an AI agent for women's and family healthcare. Covers agent architecture, evaluation methodology, release gating, and trust in healthcare AI.

## Key Architectural Decisions

1. **Lead agent + specialist pattern:** A stronger lead agent routes requests to four narrower specialists:
   - Appointments
   - Provider search
   - Health questions
   - Maven support
2. **Hard guardrails before dynamic routing** — safety checks run before routing decisions
3. **Only 15-20 tools total** — divided across specialists rather than one model with hundreds of choices
4. **Existing APIs become safer agent tools** — user identity and application state injected by code

## Evaluation & Release Strategy

- **Failure → cheapest reliable eval:** A response claiming "made by Google" became a string check; tool calls verified deterministically; LLM judges for clinical accuracy
- **Human labels calibrate judges** — consequence of wrong answer determines release threshold
- **"9 out of 10 passes is acceptable for cheap failures"** — pragmatic release gating
- Every capability needs its own evidence and release bar (model-provider slip ≠ wrong tool call ≠ wrong health answer)

## Significance for Wiki

This is a high-quality, concrete case study of:
- Enterprise AI agent deployment patterns (lead/specialist routing)
- Healthcare-specific agent constraints (trust, safety, regulatory)
- Agent evaluation methodology (deterministic checks + LLM judges + human calibration)
- Practical release gating by consequence severity
