---
title: "LLM-as-Judge Skills"
type: concept
created: 2026-05-09
updated: 2026-05-09
status: L2
tags: [context-engineering, evaluation, coding-agents]
sources:
  - "[[raw/articles/2026-05-xx_github_llm-as-judge-skills]]"
related:
  - "[[concepts/context-engineering]]"
  - "[[concepts/evaluation]]"
  - "[[concepts/agent-skills]]"
---
# LLM-as-Judge Skills

Part of **Agent-Skills-for-Context-Engineering** (15.5k stars) by [Murat Can Koylan](https://github.com/muratcankoylan). A reusable skill set for having LLMs evaluate their own outputs.

## Overview

LLM-as-Judge is a pattern for automatically evaluating model output quality. From a Context Engineering perspective, it packages evaluation logic as agent skills, making them reusable across coding agents (Claude Code, Cursor, Codex).

## Repository Structure

```
Agent-Skills-for-Context-Engineering/
├── examples/llm-as-judge-skills/
├── agents/        # Agent definitions
├── skills/        # Reusable skills
├── prompts/       # Evaluation prompts
└── src/           # Source code
```

## Relevance

Context Engineering is the concept proposed by Anthropic as "the next step after prompt engineering." It is an engineering discipline that designs the entire agent context — system prompts, tool definitions, skills, memory, and more.

## References

- [Agent-Skills-for-Context-Engineering — GitHub](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)
- [Effective Context Engineering — Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
