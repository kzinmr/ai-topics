---
title: Bernstein — Deterministic Multi-Agent Orchestrator
created: 2026-05-09
updated: 2026-05-09
type: concept
tags:
  - ai-agents
  - multi-agent
  - orchestration
  - coding-agents
  - claude-code
  - developer-tooling
  - automation
  - open-source
sources: []
---

# Bernstein — Deterministic Multi-Agent Orchestrator

Bernstein is an open-source orchestrator that parallelizes CLI AI coding agents using a **deterministic Python scheduler** — spending **zero LLM tokens on coordination**. Pip install: `pipx install bernstein`.

## Architecture

Four-stage pipeline:

1. **Decompose**: Manager breaks the goal into tasks with roles, owned files, and completion signals (one LLM call)
2. **Spawn**: Agents start in isolated git worktrees, one per task (Claude Code, Codex, Gemini CLI, 37+ others)
3. **Verify**: Janitor checks concrete signals — tests pass, files exist, lint clean, types correct
4. **Merge**: Verified work lands in main; failed tasks get retried or routed to a different model

## Key Differentiators

- **Deterministic scheduling**: Python code for every decision, no LLM calls. Same inputs → same outputs.
- **Zero LLM tokens on coordination**: After initial goal decomposition, scheduling costs nothing
- **Local HTTP task server**: Agents report progress over HTTP; state lives in `.sdd/` directory
- **Git worktree isolation**: Each agent works in a separate branch; main stays clean
- **HMAC-signed audit trail**: Every step is logged and replayable
- **34,000+ monthly PyPI downloads** (as of April 2026)

## Comparison to Alternatives

| Feature | Bernstein | Claude Squad | Composio AO |
|---------|-----------|-------------|-------------|
| Scheduling | Deterministic (Python) | Manual | LLM-based |
| Coordination cost | Zero tokens | Chat tokens | LLM tokens |
| Agent count | 40+ adapters | Claude Code only | 30+ |
| Quality gates | Built-in Janitor | Manual review | CI auto-fix |
| Git isolation | Worktrees | Sessions | Branches |

## Related

- [[concepts/harness-engineering/agent-harness]]
- [[concepts/multi-agents/multi-agent-orchestration]]
- [[entities/bernstein]]
