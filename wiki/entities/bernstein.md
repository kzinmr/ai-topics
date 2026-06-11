---
title: Bernstein
created: 2026-05-09
updated: 2026-05-10
type: entity
tags:
  - tool
  - open-source
  - multi-agent
  - orchestration
  - coding-agents
  - developer-tooling
  - automation
aliases:
  - bernstein-orchestrator
  - bernstein-run
sources:
  - https://bernstein.run/
  - https://github.com/sipyourdrink-ltd/bernstein
  - https://bernstein.readthedocs.io/
  - https://pypi.org/project/bernstein/
  - https://alexchernysh.com/
related:
  - "[[concepts/coding-agents/bernstein]]"
  - "[[concepts/multi-agents/multi-agent-orchestration]]"
  - "[[concepts/harness-engineering/agent-harness]]"
---

# Bernstein

**Bernstein** is an open-source deterministic multi-agent orchestrator for CLI coding agents. It parallelizes 40+ CLI AI agents (Claude Code, Codex CLI, Gemini CLI, Aider, and more) using a pure-Python scheduler that spends **zero LLM tokens on coordination**. Named for Leonard Bernstein, "the original orchestrator."

Created by **Alex Chernysh** ([[entities/alex-chernysh]]), Bernstein runs locally or on-prem with Apache 2.0 licensing and no SaaS dependency.

## Getting Started

```bash
pipx install bernstein
bernstein init
bernstein run -g "fix the failing test in tests/test_foo.py"
```

Also available via: `pip install bernstein`, `uv tool install bernstein`, `brew tap chernistry/tap && brew install bernstein`, Docker, and GitHub Actions.

## Key Features

### Deterministic Python Scheduler (Core Innovation)
The core scheduling loop is pure Python — zero LLM tokens spent on coordination. After one initial LLM call for goal decomposition, all decisions (who runs, what merges) are deterministic and replayable. Same inputs → same outputs.

### Four-Stage Pipeline
1. **Decompose**: Manager breaks goal into tasks with roles, owned files, and completion signals (one LLM call)
2. **Spawn**: Agents start in isolated git worktrees, one per task
3. **Verify**: Janitor checks concrete signals — tests pass, files exist, lint clean, types correct
4. **Merge**: Verified work lands in main; failed tasks get retried or routed to a different model

### HMAC-SHA256 Audit Chain
Every scheduling decision writes an HMAC-SHA256-signed entry (RFC 2104) to `.bernstein/audit.log`. Each entry references the previous hash — tampering breaks verification. Per-artefact lineage records every file write linked back to producer, inputs, prompt SHA, model, and cost.

### Git Worktree Isolation
Each agent works in an isolated git worktree on its own branch. The main branch stays clean until verified diffs merge. No race conditions, no merge conflicts from parallel agents.

### 44 CLI Adapters (v1.10.x)
Supports Claude Code, Codex CLI, OpenAI Agents SDK v2, GitHub Copilot CLI, Gemini CLI, Aider, Letta Code, Cursor, and 37+ more. Any CLI with `--prompt` works via the generic adapter.

### MCP Server Mode
Bernstein can run as an MCP server over stdio/HTTP/SSE, allowing integration with Claude Code and other MCP-compatible agents.

## Supported Agents

| Agent | Models | Install |
|-------|--------|---------|
| Claude Code | Opus 4, Sonnet 4.6, Haiku 4.5 | `npm install -g @anthropic-ai/claude-code` |
| Codex CLI | GPT-5, GPT-5 mini | `npm install -g @openai/codex` |
| OpenAI Agents SDK v2 | GPT-5, GPT-5 mini, o4 | `pip install 'bernstein[openai]'` |
| GitHub Copilot CLI | Copilot-managed | `npm install -g @github/copilot` |
| Gemini CLI | Gemini 2.5 Pro | npm install |
| Generic | Any CLI with `--prompt` | Built-in |

## Architecture

```
┌──────────────────────────────────────────────┐
│              Goal (user input)                │
└──────────────────┬───────────────────────────┘
                   │
     ┌─────────────▼─────────────┐
     │   Manager (1 LLM call)    │
     │  Decompose → Tasks,Roles  │
     └─────────────┬─────────────┘
                   │
     ┌─────────────▼─────────────┐
     │  Deterministic Scheduler  │
     │  (Pure Python, No LLM)    │
     └──┬──────────┬──────────┬──┘
        ▼          ▼          ▼
  ┌────────┐ ┌────────┐ ┌────────┐
  │Agent A │ │Agent B │ │Agent C │
  │Worktree│ │Worktree│ │Worktree│
  └───┬────┘ └───┬────┘ └───┬────┘
      │          │          │
      ▼          ▼          ▼
   ┌───────────────────────────┐
   │  Janitor (Verify)         │
   │  Test · Lint · Type · Sig │
   └───────────┬───────────────┘
               │
               ▼
        ┌───────────┐
        │   Merge   │ → Main
        └───────────┘
```

## Comparison

| Feature | Bernstein | Cursor BG | Devin | Copilot WS |
|---------|-----------|-----------|-------|------------|
| Apache 2.0 source | Yes | No | No | No |
| Runs on-prem / air-gapped | Yes | No | No | No |
| Multi-agent in parallel | Yes (40+) | Limited | No | No |
| Deterministic scheduler | Yes | No | No | No |
| HMAC-signed audit log | Yes | No | No | No |
| Cost to install | $0 | $20+/mo | $500+/mo | $10+/mo |

## Community

- **Website**: https://bernstein.run
- **Docs**: https://bernstein.readthedocs.io/
- **GitHub**: https://github.com/sipyourdrink-ltd/bernstein
- **PyPI**: https://pypi.org/project/bernstein/
- **Sponsor**: https://github.com/sponsors/chernistry
- **VS Extension**: VS Marketplace / Open VSX

## Metrics (as of May 2026)

- 296+ GitHub stars, 36 forks
- 44 CLI adapters shipping
- 462 closed PRs, 18 contributors
- ~54,000 monthly PyPI installs
- 30+ awesome lists and newsletter features
- ~$4k out-of-pocket operating cost (solo maintained, no funding)

## Creator

Built by **Alex Chernysh** (@alex_chernysh on X, chernistry on GitHub), an Applied AI Systems & Platform Engineer based in Tel Aviv. See [[entities/alex-chernysh]] for full background.

## Sources
- [Bernstein.run](https://bernstein.run/)
- [GitHub Repository](https://github.com/sipyourdrink-ltd/bernstein)
- [PyPI](https://pypi.org/project/bernstein/)
- [Alex Chernysh](https://alexchernysh.com/)
