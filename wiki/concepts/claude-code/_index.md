---
title: "Claude Code"
type: concept
created: 2026-06-11
updated: 2026-11-08
tags:
  - coding-agents
  - claude-code
  - anthropic
  - developer-tooling
sources: []
status: active
---

# Claude Code

Anthropic's CLI-based coding agent. Sub-index of all Claude Code concept pages.

See also: [[entities/claude-code]] (entity page), [[concepts/claude|Claude]] (model family)

---

## Core

- [[entities/claude-code]] — Claude Code overview
- [[concepts/claude-code/claude-code-best-practices]] — Best practices
- [[concepts/claude-code/claude-code-tips]] — Tips and tricks
- [[concepts/claude-code/claude-code-routines]] — Workflow routines

## Configuration and Rules

- [[concepts/claude-code/claude-md-rules]] — CLAUDE.md rules and conventions
- [[concepts/claude-code/claude-code-skills]] — Skill system
- [[concepts/claude-code/claude-code-source-patterns]] — Source code patterns

## Advanced Features

- [[concepts/claude-code/claude-code-auto-mode]] — Auto mode
- [[concepts/claude-code/claude-code-goal]] — /goal command and delegation
- [[concepts/claude-code/claude-code-artifacts]] — Artifacts feature (shareable HTML pages)
- [[concepts/claude-code/claude-code-sandboxing]] — Sandboxing and isolation

## Known Issues

- [[concepts/claude-code/claude-code-leak]] — Known leak issues
- [[concepts/claude-code/claude-code-agent-summary-polling]] — `agent_summary` background transcript polling — hidden ~30s interval transcript re-summarization for every background agent (status line only, no off switch since 2.1.232)

## Secrets Exposure via "Don't Ask Again" (Nov 2026)

Apiiro reported (HN 434pts — https://news.ycombinator.com/item?id=50407882) that Claude Code's "Don't Ask Again" permission option writes approved commands — including commands containing inline passwords/keys — into project-local `.claude/settings.local.json` / `.claude/settings.json`. Committing the `.claude/` directory then leaks those secrets: 1,122 such files were found in public GitHub repos, and the file spreads with every clone/fork even in private repos until the repo goes public. Remediation per the authors: search your org for `.claude/settings.local.json` and `.claude/settings.json` and audit for embedded credentials. Raw: `raw/articles/2026-11-07_apiiro_claude-code-dont-ask-again-secrets.md`. See [[concepts/claude-code/claude-code-sandboxing]] for the permission-model context.
