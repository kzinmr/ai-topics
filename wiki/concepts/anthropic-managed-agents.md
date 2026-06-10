---
title: "Anthropic Managed Agents"
type: concept
created: 2026-04-09
updated: 2026-04-26
tags:
  - concept
  - multi-agent
  - anthropic
  - platform
  - ai-agents
related: [agent-team-swarm, harness-engineering, ai-agent-engineering, managed-agents, telegram]
sources:
  - https://claude.com/blog/claude-managed-agents
  - https://www.anthropic.com/engineering/managed-agents
  - https://platform.claude.com/docs/en/managed-agents/quickstart
  - raw/articles/2026-04-09-claude-managed-agents-guide.md
---

# Anthropic Managed Agents

**Source:** Anthropic Claude Blog + Engineering Blog + Platform Docs (April 2026)
**Status:** Public Beta on Claude Platform
**Related:** [[concepts/agent-team-swarm]], [[concepts/harness-engineering]], [[concepts/meta-harness]]

---

## Core Value Proposition

Anthropic Managed Agents is a platform that enables **10x faster AI agent development from prototype to production**. By delegating infrastructure (sandboxes, authentication, permissions, checkpoints, error recovery) to Claude, developers can focus on designing tasks, tools, and guardrails.

---

## Architecture: Brain/Hands/Session Separation

Core thesis from the Anthropic Engineering Blog post "[Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/engineering/managed-agents)":

> Agent harnesses inevitably encode assumptions about current model limitations. As AI capabilities improve, these assumptions become obsolete.

In the initial design, Session, Harness, and Sandbox were coupled in a single container ("pets"). The current design fully decouples these three elements ("cattle"):

| Element | Role | Benefit of Separation |
|---|---|---|
| **Brain** | Claude + Harness | Stateless → horizontally scalable |
| **Hands** | Sandbox/Tools | Provisioned on demand, recreated on failure |
| **Session** | Event Log (persistent) | State management beyond context window |

### Key Interfaces

```
Sandbox Execution:  execute(name, input) → string
Container Lifecycle: provision({resources})
Harness Recovery:   wake(sessionId) → reboot stateless harness
                    getSession(id) → retrieve durable event log
                    emitEvent(id, event) → append to session
Context Query:      getEvents() → fetch positional slices
```

### Meta-Harness Philosophy

> "We're opinionated about the shape of these interfaces, not about what runs behind them."

Managed Agents is designed as a **meta-harness** (see [[concepts/meta-harness]]). It doesn't prescribe specific implementations — it strictly defines interface boundaries.

---

## Security: Credential Isolation

- **Git Integration**: Access tokens are injected directly into the container during sandbox initialization. Claude executes push/pull without touching tokens
- **Custom Tools (MCP)**: OAuth tokens are stored in a secure vault. Called via proxy using session-specific tokens
- **Structural Security Boundary**: Credentials never reach the sandbox

---

## Multi-Agent Coordination → Expanded Features (May 2026)

Four new features of Managed Agents were released as GA/Research Preview. See [[concepts/claude/managed-agents]] for details.

1. **Multi-Agent Orchestration (GA)** — Coordinator agent manages up to 20 specialized sub-agents. Shared filesystem + isolated context windows. Up to 25 parallel threads.
2. **Outcomes Loop (GA)** — Rubric-driven self-improvement cycle. An independent Grader agent evaluates → feedback loop (up to 20 iterations).
3. **Dreams (Research Preview)** — Reviews past sessions to optimize Memory Store (deduplication, conflict resolution, pattern extraction). Non-destructive.
4. **Webhooks (GA)** — Push-based state change notifications. `whsec_` signature verification, lightweight payload (event type + id only).

---

## Session vs Context Window

Long-running tasks can exceed Claude's context window. Traditional solutions (compression, trimming) forced irreversible keep/discard decisions.

By **separating Session as external context**:
- Guarantees persistent, queryable storage
- Harness handles arbitrary context transformations (cache optimization, future context engineering)
- Accommodates future model capability evolution without breaking the storage layer

---

## Performance Impact

| Metric | Improvement | Reason |
|---|---|---|
| TTFT p50 | ~60% reduction | Inference starts immediately, Sandbox on demand |
| TTFT p95 | >90% reduction | Same as above |
| Horizontal Scale | Many Brains | Stateless Harness enables parallel execution |
| Tool Context | Many Hands | Operates across multiple execution contexts |

---

## API Quickstart

**Required header:** `anthropic-beta: managed-agents-2026-04-01`

```python
# 1. Create Agent
agent = client.beta.agents.create(
    name="Coding Assistant",
    model="claude-sonnet-4-20260401",
    system="You are a helpful coding assistant.",
    tools=[{"type": "agent_toolset_20260401"}]
)

# 2. Create Environment
environment = client.beta.environments.create(
    name="prod-env",
    config={"type": "cloud", "networking": {"type": "restricted"}}
)

# 3. Start Session
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id
)

# 4. Stream Events
with client.beta.sessions.events.stream(session.id) as stream:
    for event in stream:
        match event.type:
            case "agent.message": ...
            case "agent.tool_use": ...
            case "session.status_idle": ...
```

---

## Pricing

- Standard Claude Platform token rates
- **+$0.08/session hour** (active runtime)

---

## Enterprise Adoption

| Company | Use Case | Quote |
|---|---|---|
| **Notion** | Custom Agents (private alpha) | "Make open-ended complex tasks delegatable" — Eric Liu, PM |
| **Rakuten** | Enterprise agent for Slack/Teams | "Deploy specialized agents in one week" — Yusuke Kaji, GM AI for Business |
| **Asana** | In-project AI teammate | "Dramatically accelerated development" — Amritansh Raghav, CTO |
| **Sentry** | Seer debugging + Claude patch agent | "Shipped in weeks, not months" — Indragie Karunaratne |
| **Atlassian (Jira)** | Workflow-integrated development agent | "Automated sandboxes, sessions, and permission management" — Sanchan Saxena, SVP Product |

---

## Related

- [[concepts/agent-team-swarm]] — Higher-level concept of multi-agent coordination
- [[concepts/harness-engineering]] — Single-agent execution environment design
- [[concepts/meta-harness]] — Interface-centric design philosophy
- [[concepts/gpt/symphony]] — Competitor's Agent Team orchestrator
- [[concepts/dark-factory-software-factory]] — Cutting-edge fully autonomous development

---

## Sources

- [Claude Blog: Claude Managed Agents](https://claude.com/blog/claude-managed-agents) (2026-04-08)
- [Anthropic Engineering: Scaling Managed Agents](https://www.anthropic.com/engineering/managed-agents) (2026-04)
- [Platform Docs: Get started with Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/quickstart) (2026-04)
- Raw articles: `wiki/raw/articles/claude-managed-agents-20260408.md`
