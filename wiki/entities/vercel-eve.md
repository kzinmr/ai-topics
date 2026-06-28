---
title: "Vercel Eve"
created: 2026-06-28
updated: 2026-06-28
type: entity
tags:
  - entity
  - agent-framework
  - agent-sdk
  - agent-architecture
  - agent-runtime
  - durable-execution
  - human-in-the-loop
  - filesystem
  - sandbox
  - subagents
  - open-source
  - vercel
  - typescript
aliases:
  - Eve framework
  - eve
related:
  - entities/vercel
  - entities/vercel-sandbox
  - concepts/harness-engineering
sources:
  - raw/articles/2026-06-27_vercel-building-agents-with-eve-framework.md
  - https://github.com/vercel/eve
  - https://vercel.com/docs/eve
  - https://vercel.com/blog/introducing-eve
---

# Vercel Eve

**Vercel Eve** is an open-source (Apache 2.0) filesystem-first framework for building, running, and scaling durable backend AI agents. Announced June 17, 2026 by Vercel, it treats an agent as a directory of files — tools, skills, subagents, schedules, evals, connections, and channels all live as plain files on disk, auto-discovered by name. The framework compiles the `agent/` directory into a Vercel Functions app, making the same agent that runs locally deployable to production with no code changes.

**GitHub**: 2,857 ★ | 214 forks | TypeScript | 116 open issues | Created Jun 16, 2026

## Core Philosophy: An Agent Is a Directory

> "An agent is a directory. A file's name and place in the tree are its definition."

Eve's foundational bet is that an agent should be a set of files you can read, not a runtime you have to trust. This makes agents **inspectable** (open the folder), **versionable** (git diff/commit), and **portable** (hand to a teammate). There is no hidden runtime state — the file tree IS the state.

Two files at the root define the agent:
- `agent/instructions.md` — the always-on system prompt
- `agent/agent.ts` (optional) — runtime config (which model to use, etc.)

Every capability below them is a directory Eve auto-discovers by name, so adding a feature is typically adding a single file.

## Architecture: The Parts You Assemble

### Tools (`agent/tools/`)

Tools are typed actions the agent can call, defined as TypeScript files using Zod schemas. The model decides WHEN to call a tool from its description; the developer's code decides WHAT happens, running in the app runtime with full access (not in the sandbox). This split keeps agents both flexible and safe.

```typescript
import { defineTool } from "eve/tools";
import { z } from "zod";

export default defineTool({
  description: "Save a short note to the project notes/ folder.",
  inputSchema: z.object({ title: z.string(), body: z.string() }),
  async execute({ title, body }) {
    // writes notes/<slug>.md and returns where it saved
  },
});
```

Tools can be gated with `needsApproval: always()` for human-in-the-loop workflows.

### Skills (`agent/skills/`)

Skills give the agent know-how instead of actions. A skill is a markdown file with a frontmatter `description` that tells the model when to load it. Skills use **progressive disclosure** — loaded into context only when a request matches, keeping the prompt lean. A support agent can hold dozens of playbooks as skills.

```markdown
---
description: Use when the learner asks to save, log, file, or keep a note.
---
When the learner asks you to save a note, call the save_note tool. Always
end the note body with this exact line:

Filed with eve.
```

### Subagents (built-in)

Every agent gets a built-in agent tool for delegation. The parent agent can fan out subtasks in parallel and gather results. This is how Vercel's V router agent distributes work across its fleet.

### Human-in-the-Loop

Mark a tool with `needsApproval: always()` and the run pauses for a person before executing, burning no compute while it waits. The pause is **durable** — a task can wait on a human for minutes or days and resume exactly where it stopped. This is the `draft0` pattern: move fast on low-risk actions, keep human judgment on the few that ship.

### Durable Sessions

Every conversation is a checkpointed workflow powered by Vercel Workflows. Sessions survive crashes, deploys, and cold starts, resuming exactly where they stopped. An agent whose work starts in Slack can continue on the web days later with no custom state-management code.

### Evals (`agent/evals/`)

Evals drive the real agent through a session and assert on behavior — like unit tests for agents:

```typescript
import { defineEval } from "eve/evals";

export default defineEval({
  async test(t) {
    await t.send("Save a launch note.");
    t.completed();
    t.calledTool("save_note");
  },
});
```

Evals run locally and in CI. Change a prompt or tool, run the evals, and catch regressions before users do.

### Connections (`agent/connections/`)

Connections wire the agent to external services — MCP servers or OpenAPI-style APIs. Eve brokers authentication so the model never sees URLs or credentials:

```typescript
import { defineMcpClientConnection } from "eve/connections";

export default defineMcpClientConnection({
  url: "http://127.0.0.1:3939/mcp",
  description: "Local weather service.",
});
```

### Channels (`agent/channels/`)

Channels put the agent in Slack, Discord, Teams, or behind an HTTP API — each a single file. The agent you built in the terminal IS the agent that ships to Slack. You change where it lives by adding a file, not by rewriting code.

## Production: Vercel's Internal Fleet

Vercel runs **100+ Eve agents** internally. Each agent is just a directory.

| Agent | Type | Scale/Performance |
|-------|------|-------------------|
| **d0** | Data agent | ~30,000 questions/month via read-only SQL tool against warehouse |
| **Vertex** | Support agent | ~92% ticket resolution rate, reaches into help center and internal tools via connections |
| **Athena** | Sales agent | Salesforce + Snowflake integration, built in 6 weeks with no engineers |
| **draft0** | Content agent | Drafts and reviews content; human signs off before shipping |
| **V** | Router agent | Sits in Slack, reads tasks, routes to the best-suited agent |

Every one of these has the same architecture as what you build locally. The difference is which files are in the directory.

## From Laptop to Production

Eve compiles the `agent/` directory into a standard Vercel project running on Vercel Functions:

| Concern | Local | Production |
|---------|-------|-----------|
| **Sandbox** | Isolated bash-style sandbox | Vercel Sandbox (real isolated microVMs) |
| **Sessions** | In-process | Vercel Workflows (durable, survive deploys/crashes) |
| **Schedules** | N/A | Vercel Cron |
| **Channels** | Terminal | Slack, Discord, Teams, HTTP API |
| **Tracing** | N/A | Vercel Observability (sessions, turns, tools, reasoning, timing, tokens) |
| **Models/Auth** | Local | AI Gateway (OIDC) + Vercel Connect (OAuth/API key brokering) |
| **Scale** | Single agent | Horizontally scalable fleet (100+ agents at Vercel) |

You don't re-implement anything for production. You deploy the directory, and the framework handles durability, isolation, models, and scale.

## Getting Started

```bash
npx eve@latest init my-agent   # scaffold a project, start dev server
eve dev                          # boots an interactive agent in your terminal
```

1. **Add a tool** — Drop a `defineTool` file and ask the agent to use it
2. **Teach a skill** — Write a short markdown file with a description
3. **Delegate** — Hand off work through the built-in agent tool
4. **Prove it** — Add a `defineEval` file, then schedule it with `defineSchedule`
5. **Connect and ship** — Add a connection for real services, a channel for Slack/Discord, then deploy

## Competitive Positioning

| Aspect | Vercel Eve | Claude Agent SDK | OpenAI Agents SDK | LangChain/LangGraph |
|--------|-----------|-----------------|-------------------|-------------------|
| **Paradigm** | Filesystem-first (agent = directory) | Code-first (agent = class) | Code-first (agent = runner) | Graph-first (agent = DAG) |
| **State** | File tree IS state | In-memory + checkpoints | In-memory + built-in state | Checkpoint-based |
| **Durability** | Built-in (Vercel Workflows) | Optional (external DB) | Built-in (built-in state) | LangGraph checkpoint |
| **Sandbox** | Built-in (isolated microVMs) | External (Daytona, Modal) | External (Vercel Sandbox, Modal) | N/A (code runs inline) |
| **Evals** | Built-in (defineEval, runs in CI) | External (Braintrust, custom) | Built-in (traces, eval runner) | LangSmith |
| **Deployment** | Vercel (serverless) | Any Node.js runtime | Any Python/Node.js runtime | Any Python runtime |
| **Human-in-loop** | Built-in (needsApproval, durable) | Manual (custom gating) | Built-in (handoffs) | LangGraph interrupts |
| **Auth brokering** | Built-in (Vercel Connect) | Manual | Manual | Manual |
| **License** | Apache 2.0 | Proprietary (Anthropic) | Apache 2.0 | MIT |

## Related Concepts

- [[concepts/harness-engineering]] — Eve is a harness that provides the execution environment for agents; the "agent = model + harness" philosophy
- [[entities/vercel-sandbox]] — Vercel Sandbox (microVMs), the isolation layer Eve uses in production
- [[entities/vercel]] — Vercel Inc., the company behind Eve
- [[comparisons/agent-harnesses]] — Broader comparison of agent harnesses and frameworks

## References

- [Introducing Eve](https://vercel.com/blog/introducing-eve) — Vercel announcement (Jun 17, 2026)
- [vercel/eve](https://github.com/vercel/eve) — GitHub repository (Apache 2.0)
- [Eve documentation](https://vercel.com/docs/eve) — Official docs
- [Eve concepts](https://vercel.com/docs/eve/concepts) — Architecture overview
- [Introduction to Eve (D.AI.R)](https://academy.dair.ai/labs/intro-to-eve) — Free hands-on lab
- [Building Agents with Vercel's Eve Framework](https://x.com/i/article/2069825847729508352) — X Article deep-dive
