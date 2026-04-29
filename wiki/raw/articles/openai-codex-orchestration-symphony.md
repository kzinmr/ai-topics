---
title: "An open-source spec for Codex orchestration: Symphony"
url: "https://openai.com/index/open-source-codex-orchestration-symphony/"
date: "2026-04-27"
source: "OpenAI Engineering Blog"
author: "OpenAI Engineering Team"
tags: [codex, agent-orchestration, symphony, openai, linear, coding-agents]
---

# OpenAI Engineering Blog: Open-Source Codex Orchestration — Symphony

## Summary

OpenAI announced Symphony as an open-source specification and reference implementation for orchestrating Codex coding agents at scale. The system transforms project management boards (like Linear) into a control plane for autonomous agents, enabling teams to "manage work instead of supervising agents."

## Key Results

- **500% increase in landed PRs** within three weeks on some teams
- Human attention bottleneck eliminated — engineers manage 3-5 agent sessions before context switching becomes painful
- Symphony acts as a daemon continuously polling issue trackers
- Agents can create sub-tasks, build DAGs of dependencies, and file follow-up issues
- One issue can produce multiple PRs or pure analysis without code changes

## Technical Architecture

### System Components
1. **Workflow Loader** - Reads `WORKFLOW.md` (repo-level contract)
2. **Issue Tracker Client** - Fetches/normalizes tracker data
3. **Orchestrator** - Polling loop, concurrency control, retries
4. **Workspace Manager** - Creates isolated filesystem directories per issue
5. **Agent Runner** - Launches Codex app-server, streams updates

### WORKFLOW.md Contract
Teams define agent policy in-repo with YAML frontmatter + Markdown prompt:
```yaml
tracker:
  kind: linear
  project_slug: my-project
  active_states: ["Todo", "In Progress"]
agent:
  max_concurrent_agents: 10
hooks:
  after_create: "npm install"
```

### Codex App Server Mode
- Headless JSON-RPC API for dynamic tool calls
- Functions like `linear_graphql` exposed without raw API tokens
- Session handshake: initialize → thread/start → turn/start

## The Economic Shift

When implementation cost → near zero:
- **Speculative tasks** become trivial (explore refactors, test hypotheses)
- **Broadened access** — PMs/designers file requests directly, agents provide video walkthroughs
- **From interaction to orchestration** — always-on daemon vs micromanaged sessions

## Lessons Learned

1. **Loss of Nudging** — Can't steer agents mid-flight in ticket-level work
2. **System Hardening over Manual Fixing** — Add skills to harness (e2e tests, Chrome DevTools) so agents self-correct
3. **Objectives over Transitions** — Treating agents as rigid state machine nodes failed; give them objectives and tools, "let them cook"

## Multi-Language Verification

OpenAI verified the spec by having Codex generate implementations in:
- TypeScript
- Go
- Rust
- Java
- Python
- Elixir (reference implementation)

## Repository
- **GitHub:** https://github.com/openai/symphony
- **SPEC.md:** https://github.com/openai/symphony/blob/main/SPEC.md
- **License:** Apache 2.0
