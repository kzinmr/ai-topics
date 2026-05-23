---
title: "Run Claude Managed Agents on Daytona"
source: "https://www.daytona.io/docs/en/guides/claude/claude-managed-agents/"
date: 2026-05-19
source_type: docs
source_domain: daytona.io
source_org: Daytona
tags: [claude, managed-agents, daytona, sandbox, self-hosted]
references:
  - "https://www.daytona.io/docs/en/guides/claude/claude-managed-agents/"
---

# Run Claude Managed Agents on Daytona

A guide to running Claude Managed Agents inside your own Daytona sandboxes, as a self-hosted environment.

---

## How the Pieces Fit Together

Three parties are involved in any session:

- **Anthropic** – runs the API, the agent loop, and a per-environment work queue.
- **You** – run an application that creates sessions and an orchestrator that manages sandbox lifecycle and runs the agent's tool runner inside each sandbox.
- **Daytona** – provides sandbox containers where filesystem and shell tools execute.

---

## Tool Dispatch Split

| Tool Type | Where executed |
|-----------|----------------|
| `bash`, `read`, `write`, `edit`, `glob`, `grep` | Inside your Daytona sandbox |
| `web_search`, `web_fetch` | Anthropic server-side |
| MCP server tools | Anthropic server-side (uses Anthropic-managed vaults) |

Each session gets its own **isolated sandbox**; filesystem changes persist across tool calls, and the bash shell keeps its working directory, environment, and background processes between calls.

---

## Orchestrator Process

A long-lived process with these responsibilities:

- Watch the environment's work queue (polling or webhooks)
- For each work item, ensure a Daytona sandbox is running and start the agent's tool runner inside it
- Stop idle sandboxes after a configurable threshold
- Archive sandboxes when their session terminates; files remain in Daytona's object storage for 30 days

Two reference orchestrator variants:
- **Polling** – long-polls the work queue; only needs the environment key
- **Webhook** – FastAPI receiver triggered by `session.status_run_started` webhook deliveries; needs a public URL

---

## Anthropic Skills CLI Integration

The runner can download and install Anthropic Skills packages from the API, creating a drop-in experience for agent skills in self-hosted environments.
