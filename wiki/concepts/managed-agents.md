---
title: "Managed Agents (Anthropic)"
type: concept
created: 2026-04-25
updated: 2026-05-15
tags:
  - architecture
  - anthropic
  - infrastructure
aliases:
  - Claude Managed Agents
  - decoupled agent architecture
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_managed-agents.md
  - https://www.anthropic.com/engineering/managed-agents
  - raw/articles/martinalderson.com--posts-managed-agents-are-the-new-lambda--f9db9fb9.md
  - https://martinalderson.com/posts/managed-agents-are-the-new-lambda/
related:
  - building-effective-agents
  - effective-harnesses-for-long-running-agents
  - multi-agent-research-system
  - agent-team-swarm
---
# Managed Agents (Anthropic)

Anthropic's hosted service for long-running agents. Architecture of **separating the brain from the hands**.

## Design Philosophy

> "How to design a system for 'programs as yet unthought of.'"

Just as an OS virtualizes hardware into `process` / `file`, Managed Agents virtualize the building blocks of agents:
- **Session** — An append-only log of all events that occurred
- **Harness** — The loop that calls Claude and routes tool calls
- **Sandbox** — The execution environment where Claude runs code and edits files

Each interface is independent of implementation → implementations can be freely swapped.

## Pets vs Cattle

### Coupled Architecture (Pet)
- Session, harness, and sandbox co-located in one container
- Container failure → session loss
- Debugging requires shell access → conflicts with user data access
- Harness assumes "resources are inside the container" → walls hit during VPC connection

### Decoupled Architecture (Cattle)

```
execute(name, input) -> string
provision({resources})
wake(sessionId)
getSession(id)
emitEvent(id, event)
getEvents()
```

- Container death → detected as tool call error, Claude decides whether to retry
- Harness crash → restarted via `wake(sessionId)`, resumes from event log
- Credentials stored in Vault outside sandbox (inaccessible from Claude's generated code)

## Session ≠ Context Window

- Session is a persistent context object **outside** the context window
- `getEvents()` for position-based slice retrieval (resume, rewind, reload)
- Retrieved events are transformable within the harness (prompt caching optimization, context engineering)

## Performance Improvements

- **p50 TTFT**: ~60% reduction
- **p95 TTFT**: 90%+ reduction
- When the brain doesn't need a container, inference starts without waiting for provisioning

## Many Brains, Many Hands

- **Many brains**: Launch multiple stateless harnesses, connecting to hands only when needed
- **Many hands**: Each hand is an `execute(name, input) -> string` tool. Harness doesn't care about the hand's physical form (container/phone/Pokemon emulator)
- Hands can be passed between brains

## Meta-Harness

Managed Agents is a **meta-harness** — not tied to a specific harness implementation, capable of accommodating both general-purpose harnesses like Claude Code and task-specific harnesses.

> "We're opinionated about the shape of these interfaces, not about what runs behind them."


## Vendor Lock-in and Self-Hosting Strategy (Martin Alderson, May 2026)

[[entities/martin-alderson|Martin Alderson]] analyzes managed agents through the **AWS Lambda analogy**. Just as Lambda sparked a serverless revolution, managed agents are powerful but warns they are "sticky (hard to migrate from)."

### Agent Harness Interchangeability

All agent harnesses (Claude Code, Codex, OpenCode, Pi) share the same primitives:
- Prompt + Context + Tools → Output + Log

This fundamental structural commonality makes switching between harnesses relatively easy. But when data and workflows become embedded in a managed agent product, that ease is lost.

### Impact of Anthropic Pricing Changes (May 2026)

In May 2026, Anthropic **excluded non-interactive** Claude Code usage (including Managed Agents and CI/CD pipelines) from subscription token allocations. Effectively a **5-20x price increase**, resulting in:
- **Migration pressure toward OpenAI Codex** (OpenAI currently permits subscription allocation for all tools and modes)
- Notable pattern of developer price sensitivity cascading into enterprise purchasing decisions

### Self-Hosting in Practice

```bash
# Essentially just running a harness in a Docker container
docker run ... opencode --model <any-provider> --prompt "..."
```

Advantages:
- **Model provider independence**: Switch Anthropic → OpenAI → Google → DeepSeek in minutes
- **Secure within existing infrastructure**: Runs within your own VPC, IAM, audit logs
- **Building organizational competence**: Don't outsource knowledge of agent primitives

### Frontier Lab Monopoly Strategy Risk

> *"I have a strong gut feeling the frontier labs are going to start introducing new models and capabilities that are ONLY available on their managed agent platforms."*

If new models and capabilities start being offered exclusively on managed agent platforms, the self-hosting strategy is fundamentally undermined. For now, a wait-and-see approach is prudent, but trends must be closely monitored.

## See Also


- [[concepts/building-effective-agents]] — Building effective agents
- [[concepts/effective-harnesses-for-long-running-agents]] — Long-running agent harnesses
- [[concepts/multi-agents/multi-agent-research-system]] — Multi-agent research system
- [[concepts/multi-agents/agent-team-swarm]] — Agent team/swarm architecture
- [[concepts/carlini-c-compiler-agents]] — Carlini's parallel agent experiment
