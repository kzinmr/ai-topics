---
title: "Anthropics Skills Repository"
type: entity
created: 2026-09-29
updated: 2026-09-29
aliases:
  - anthropics/skills
  - Anthropic Agent Skills repo
tags:
  - ai-agents
  - agent-skills
  - claude-code
  - evals
  - developer-tooling
sources:
  - https://github.com/anthropics/skills
  - raw/articles/claude.dev--automating-eval-design-and-hillclimbing--2026-09-28.md
related:
  - "[[entities/anthropic]]"
  - "[[entities/rlancemartin]]"
  - "[[concepts/evals-skills]]"
  - "[[concepts/agent-skills-skillmd]]"
---

# Anthropic Skills Repository

**anthropics/skills** ([github.com/anthropics/skills](https://github.com/anthropics/skills)) is Anthropic's official, open-source repository of agent skills — packaged procedures (SKILL.md + supporting files/scripts) that coding agents like Claude Code load on demand. It is the canonical distribution channel for first-party skills and the reference implementation of the [[concepts/agent-skills-skillmd|SKILL.md]] format.

## The `claude-api` Skill

The flagship skill, maintained publicly by [[entities/rlancemartin|Lance Martin]], provides SDK patterns for the Claude API in Python, TypeScript, Go, Java, Ruby, PHP, C#, and curl, plus orchestration patterns for Claude Managed Agents self-hosted sandboxes.

As of September 2026 it ships two eval-related commands (see [[concepts/evals-skills]]):

- **`build-eval`** — builds an evaluation inside your codebase via a guided interview workflow (task sourcing, grader design, calibration).
- **`hillclimb`** — iteratively improves an application against the eval, one patch at a time, with a held-out test set and revert-on-overfitting guardrails.

The evals implementation lives in [`skills/claude-api/shared/evals`](https://github.com/anthropics/skills/tree/main/skills/claude-api/shared/evals).

## Significance

- Converts Anthropic's internal engineering blog guidance ("Demystifying evals for AI agents", "Effective Context Engineering") into **executable agent procedures** — the skill *is* the doc.
- A feedback loop with practitioners is visible in the open: Hamel Husain critiqued the evals skill on X (Sep 29, 2026), and Lance Martin committed publicly to updating it (his critique centered on the skill's handling of internal/proprietary evals datasets).

## Sources

- Repo: https://github.com/anthropics/skills
- Article: [[raw/articles/claude.dev--automating-eval-design-and-hillclimbing--2026-09-28]]
