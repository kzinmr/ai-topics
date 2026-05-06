---
title: DeepClaude - Claude Code Agent Loop with DeepSeek V4 Pro
created: 2026-05-06
updated: 2026-05-06
type: concept
tags: [agent, interoperability, deepseek, claude-code, orchestration]
sources:
  - raw/articles/deepclaude-may-2026.md
---

# DeepClaude

**Date**: May 4, 2026

DeepClaude is an open-source tool that enables using **Claude Code**'s agent loop with **DeepSeek V4 Pro**. It demonstrates the emerging pattern of **agent framework interoperability** — where the orchestration layer is decoupled from the underlying model.

## Key Innovation

- **Claude Code → orchestration/agent loop → DeepSeek V4 Pro → execution → back to Claude**
- Allows users to leverage Claude's superior agent planning capabilities while using more cost-effective inference from DeepSeek
- Demonstrates that agent harnesses can be **model-agnostic**

## Significance

This represents a shift in the agentic landscape where:
1. **Orchestration frameworks** (like Claude Code's loop) become reusable across models
2. **Model providers** compete on inference cost/quality, not just agent features
3. **Users** can mix-and-match best-of-breed components

This aligns with the [[concepts/bitter-lesson-agent-harnesses]] thesis: as models improve, more agent functionality moves from harness code into the model itself, but the orchestration layer remains valuable.

## Related

- [[entities/claude-code]] — Claude Code agent framework
- [[entities/deepseek]] — DeepSeek model provider
- [[concepts/agent-harness-primitives]] — Agent harness design patterns
- [[concepts/bitter-lesson-agent-harnesses]] — Bitter lesson applied to agent harnesses
