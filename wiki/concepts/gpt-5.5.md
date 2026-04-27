---
title: "GPT-5.5"
type: concept
created: 2026-04-27
updated: 2026-04-27
tags: [model, llm, openai, gpt, frontier-models, agent, benchmark]
aliases: ["GPT-5.5", "OpenAI SPUD"]
sources:
  - raw/articles/openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md
  - entities/openai-spud.md
---

# GPT-5.5

## Overview

**GPT-5.5** is OpenAI's first fully retrained base model since GPT-4.5, announced in April 2026. Designed specifically for multi-step work including planning, tool use, and self-checking, it represents a significant architectural refresh rather than an incremental update.

## Key Specifications

| Metric | Value |
|--------|-------|
| Type | Fully retrained base model (first since GPT-4.5) |
| Design Target | Multi-step work: planning, tool use, self-checking |
| Terminal-Bench 2.0 | **82.7%** |
| Agent Use Case | Can carry tasks through to completion autonomously |

## Significance

GPT-5.5 represents a strategic shift for OpenAI toward **agent-optimized base models**. Unlike GPT-4.5 which was a general-purpose language model, GPT-5.5's architecture prioritizes:

- **Planning and reasoning** — ability to decompose complex tasks into sub-steps
- **Tool use proficiency** — native capability to invoke and integrate external tools
- **Self-checking and error recovery** — can verify its own work and correct mistakes
- **Multi-step task completion** — designed to carry tasks through from start to finish without human intervention

Its 82.7% score on Terminal-Bench 2.0 positions it as one of the top-performing models for agentic coding and terminal-based workflows.

## Relation to SPUD

GPT-5.5 is likely the same model previously discussed under the internal codename **[[entities/openai-spud]]** (OpenAI SPUD), whose pre-training was completed in March 2026.

## Related Pages

- [[concepts/gpt-models]] — The full GPT model family series
- [[entities/openai]] — OpenAI entity page
- [[concepts/openai-workspace-agents]] — Codex-powered shared agents for enterprise
- [[concepts/chatgpt-images-2.0]] — GPT Image 2 announced alongside GPT-5.5
