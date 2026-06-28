---
title: "Building Agents with Vercel's Eve Framework"
fetched: 2026-06-28
source: X Article (x.com/i/article/2069825847729508352)
source_url: https://x.com/i/article/2069825847729508352
author: Unknown (X Article)
type: raw_article
tags: [vercel, eve, agent-framework, filesystem, durable-execution]
canonical_urls:
  - https://vercel.com/blog/introducing-eve
  - https://vercel.com/docs/eve
  - https://github.com/vercel/eve
  - https://academy.dair.ai/labs/intro-to-eve
---

# Building Agents with Vercel's Eve Framework

Vercel recently shipped Eve, an open-source framework for building, running, and scaling agents. The core idea is that you stop hand-rolling the same agent plumbing every time, and start treating an agent as something you can read off disk.

This is the practical version of what Eve is, why it matters, and what building with it actually looks like, drawn from the free hands-on lab we just built around it.

If you want to try Eve without any setup, we built a free hands-on lab where you drive the real eve CLI in a live terminal with no API key of your own required. You can try it at Introduction to Eve.

## Where Eve comes from

Eve comes from a team at Vercel and is open source under the Apache 2.0 license. The official Vercel documentation describes it as a filesystem-first framework for durable backend AI agents, and it is currently in beta, so the APIs can still change before general availability.

"Agents today are where the web was before frameworks, with everyone hand-rolling the same plumbing and nothing carrying over to the next one." — The Eve team, Vercel. Introducing Eve, June 17 2026.

That is the whole motivation. Durable sessions, a sandbox to run code, approvals, tracing, evals. Every team rebuilds these before their agent does anything useful, and none of it transfers to the next project. Eve ships that infrastructure as the framework, so production is built in from the first run instead of bolted on at the end.

## An agent is just a directory of files

The core idea, and the one the lab keeps returning to, is that an agent is not a graph you wire together in code. It is a folder.

"An agent is a directory. A file's name and place in the tree are its definition."

The tools an agent can call, the skills it knows, the subagents it delegates to, its schedules, and its evals all live on disk as plain files. You can open the folder and see exactly what your agent is, diff it, commit it, and hand it to a teammate. There is no hidden runtime state to reason about, because the file tree is the state.

Two files at the root define the agent itself. agent/instructions.md holds the always-on system prompt, and the optional agent/agent.ts sets the runtime config such as which model to use. Every capability below them, the tools, skills, subagents, connections, channels, and sandbox, is a directory eve auto-discovers by name, so adding one is usually just adding a file.

## The parts you assemble

In the lab, each capability is one file you drop into the project, and Eve wires it up with no registration step.

### Tools

Tools are the agent's hands. A tool is a typed action the agent can call, defined in a file under agent/tools/. The lab ships save_note.ts.

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

The model decides when to call a tool from its description. Your code decides what happens, and it runs in your app runtime with full access, not in the sandbox. That split is what keeps an agent both flexible and safe.

### Skills

Skills give the agent know-how instead of actions. A skill is a markdown file under agent/skills/, advertised by a one-line description and loaded into context only when a request matches.

```markdown
---
description: Use when the learner asks to save, log, file, or keep a note.
---

When the learner asks you to save a note, call the save_note tool. Always
end the note body with this exact line on its own:

Filed with eve.
```

Ask the agent to "log" a note and it loads this skill, files the note, and signs it off with "Filed with eve." This is progressive disclosure. A support agent can hold dozens of playbooks as skills and pull in only the one the ticket needs, so the prompt stays lean.

### Subagents

Subagents let one agent delegate. Every agent gets a built-in agent tool, so the parent can fan three subtasks out at once and gather the results. This is exactly how V routes work across Vercel's fleet of Eve agents.

### Human-in-the-loop

Human-in-the-loop gates the actions that need judgment. Mark a tool needsApproval: always() and the run pauses for a person before it executes, burning no compute while it waits.

```typescript
export default defineTool({
  description: "Publish a saved note so it goes live.",
  inputSchema: z.object({ slug: z.string() }),
  needsApproval: always(),
  async execute({ slug }) { /* copies notes/<slug>.md into published/ */ },
});
```

The pause is durable, so a task can wait on a human for minutes or days and resume right where it stopped. That is the draft0 pattern. Move fast on everything low-risk, and keep a hand on the few actions that ship.

### Durable sessions

Durable sessions are why all of this survives the real world. Every conversation is a checkpointed workflow, so it survives a crash or a deploy and resumes exactly where it stopped. In the lab the agent simply remembers a fact you gave it three messages ago. In production it is an agent whose work starts in Slack and continues on the web days later, with no state-management code that you wrote.

### Evals

Evals prove it still works. An eval drives the real agent through a session and asserts on what happened.

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

Change a prompt or a tool, run the evals, and you catch the regression before your users do. They run locally and in CI, the same way unit tests do.

### Connections and Channels

Connections are the way out, and channels are the way in, each a single file. A connection points the agent at an external service, an MCP server or an OpenAPI-style API, and Eve brokers the auth so the model never sees the URL or credentials.

```typescript
import { defineMcpClientConnection } from "eve/connections";

export default defineMcpClientConnection({
  url: "http://127.0.0.1:3939/mcp",
  description: "Local weather service.",
});
```

A channel puts that same agent in Slack, Discord, Teams, or behind an HTTP API. The agent you built in the terminal is the agent that ships to Slack. You change where it lives by adding a file, not by rewriting it.

The pattern is always the same. Drop a file, the agent reads it, behavior changes, and you commit the file alongside your code.

## What this looks like in production

This is not a toy. The examples below come straight from Vercel's Eve announcement, where the team describes the fleet of more than a hundred agents they run internally.

| Agent | Type | Details |
|-------|------|---------|
| **d0** | Data agent | Answers ~30,000 questions/month through a single read-only SQL tool against the warehouse |
| **Vertex** | Support agent | Resolves ~92% of tickets on its own by reaching into the help center and internal tools through connections |
| **Athena** | Sales agent | Wired to Salesforce and Snowflake, built in six weeks with no engineers |
| **draft0** | Content agent | Drafts and reviews content, but a human signs off before anything ships |
| **V** | Router agent | Sits in Slack, reads each incoming task, and routes it to the agent best suited to answer |

Every one of these is the same shape you build in the lab. The difference between the agent in your terminal and the one resolving real support tickets is mostly which files are in the directory.

## A concrete first session

You do not start from a blank page. In the lab you launch a working agent in a real terminal and talk to it in plain English.

```bash
eve dev      # boots an interactive agent in your terminal
```

You ask it to build something, say a small welcome.html, and watch it call its write_file tool and save the result to its sandbox, never touching your real machine. Then you hand it the save_note tool above, ask it to file a note, and see it pick the tool on its own from the description. From there the lab layers on a skill, a subagent, an approval gate, an eval, and a connection, one file at a time, until you have walked the whole framework.

## From your laptop to production

This is where the filesystem-first bet pays off.

"The same directory runs in production exactly as it ran on your laptop."

It is a normal Vercel project. Eve compiles the agent/ directory into an app that runs on Vercel Functions, so the agent you built and tested locally is the agent that deploys. What changes is not your code but the infrastructure underneath it, and each piece maps to a documented Vercel service.

- **The sandbox graduates.** Locally the agent runs in an isolated, bash-style sandbox. In production each agent gets a real isolated Vercel Sandbox, so it can run shell commands and write files without ever touching your application runtime.
- **Sessions become durable workflows.** Eve persists session state on Vercel Workflows, so a run survives a deploy, recovers from a cold start, and can pause on a human approval for minutes or days, then resume exactly where it stopped.
- **Schedules and channels go live.** Your defineSchedule files start firing on cron, and the channels you added put the same agent in Slack, Discord, Teams, or behind an HTTP API.
- **Every run is traced.** Vercel Observability shows each agent run with its sessions, turns, tools, reasoning, timing, and token usage, with no setup.
- **Models and auth are handled.** Model strings route through AI Gateway with OIDC, so you never manage provider keys, and Vercel Connect brokers OAuth and API keys for your connections.
- **One agent becomes a fleet.** The same shape scales horizontally, which is how Vercel runs more than a hundred of these agents at once, each one just a directory.

You do not re-implement anything for production. You deploy the directory, and the framework handles durability, isolation, models, and scale.

## How to get started

1. **Scaffold a project.** Run `npx eve@latest init my-agent` to create the project, install dependencies, and start the dev server. You get an interactive agent in your terminal in seconds.
2. **Give it a tool.** Add a defineTool file like save_note, ask the agent to use it, and watch it call your code.
3. **Teach it a skill.** Write a short markdown file with a description that says when to use a procedure.
4. **Delegate with a subagent.** Hand off a focused job through the built-in agent tool so your main agent stays clean.
5. **Prove it with an eval, then schedule it.** Add a defineEval file and a defineSchedule file with a cron line.
6. **Connect and ship.** Add a connection to reach a real service, a channel to put the agent in Slack, then deploy the same directory to Vercel.

## Takeaway

Eve's bet is that an agent should be a set of files you can read, not a runtime you have to trust. That makes agents inspectable, versionable, and portable, and it moves the hard production concerns into the framework where they belong.

## References

- [Eve documentation](https://vercel.com/docs/eve) — the official docs
- [Eve concepts](https://vercel.com/docs/eve/concepts) — how agents, sessions, tools, skills, connections, and sandboxes fit together
- [Introducing Eve](https://vercel.com/blog/introducing-eve) — the Vercel announcement
- [vercel/eve](https://github.com/vercel/eve) — the open-source framework on GitHub
- [Introduction to Eve](https://academy.dair.ai/labs/intro-to-eve) — free hands-on lab by D.AI.R
