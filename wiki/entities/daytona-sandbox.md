---
title: "Daytona Sandbox (Claude Managed Agents)"
created: 2026-05-19
updated: 2026-05-19
type: entity
tags:
  - entity
  - sandbox
  - ai-agents
  - architecture
  - infrastructure
  - developer-tooling
  - orchestration
  - self-hosted
  - daytona
sources:
  - raw/articles/2026-05-19_daytona_claude-managed-agents-sandbox.md
---

# Daytona Sandbox (Claude Managed Agents)

**Daytona Sandbox** is Daytona's self-hosted sandbox environment for [[concepts/anthropic/managed-agents|Claude Managed Agents]] (CMA), launched May 19, 2026. It moves the agent's container layer from Anthropic-operated cloud containers to Daytona-managed sandbox containers running on the user's own infrastructure, while the agent loop, prompt caching, model calls, event stream, and session history all remain on Anthropic's platform.

Daytona was co-founded by [[entities/ivan-burazin|Ivan Burazin]], who coined the term "composable computers for agents." Daytona's platform provisions fast, stateful development environments — popularly called "AI sandboxes" — that give agents full CPU, RAM, disk, and OS access.

## Architecture: Three-Party Split

Daytona's CMA integration explicitly documents a **three-party architecture**:

1. **Anthropic** — Runs the API, agent loop, and a per-environment work queue that signals when an agent has tools to dispatch. Web tools (`web_search`, `web_fetch`) and MCP server calls are dispatched by Anthropic server-side — the sandbox is not involved.

2. **You** — Run an application that creates sessions and talks to end users, plus an **orchestrator** that manages the sandbox lifecycle (create, start, stop, clean up) and launches the agent's tool runner inside each sandbox.

3. **Daytona** — Provides the sandbox containers in which filesystem and shell tools (`bash`, `read`, `write`, `edit`, `glob`, `grep`) execute.

This split means that a self-hosted environment changes **only where filesystem and shell tools run**, and nothing else. Each session gets its own isolated sandbox with persistent filesystem changes across tool calls within the session.

## Key CMA Integration Features

### Orchestrator: Polling and Webhook Variants

Daytona provides two orchestrator reference implementations:

- **Polling (`host_orchestrator_polling.py`)** — Long-polls the environment's work queue. Only needs the environment key. Works against environments behind any kind of NAT or firewall.
- **Webhook (`host_orchestrator_webhook.py`)** — A FastAPI receiver that drains the queue on each `session.status_run_started` delivery. Requires a publicly reachable URL and `ANTHROPIC_WEBHOOK_SECRET`, but avoids continuous polling.

Both share the same sandbox lifecycle logic with deduplication, acknowledgement, retries, locking, and a janitor thread.

### Sandbox Lifecycle Management

Daytona has the most sophisticated lifecycle among [[comparisons/claude-managed-agents-sandbox-providers|CMA sandbox providers]]:

- **Idle stop** — Sandboxes are stopped after a configurable idle threshold. The filesystem survives the pause, so sessions can sit quiet between bursts of activity without keeping a sandbox running.
- **30-day deletion window** — Sandboxes that stay stopped for 30 days are deleted. Activity restarts the timer.
- **Archive on termination** — When a session terminates, the sandbox is archived. The filesystem stays in Daytona's cost-effective object storage until the same 30-day window expires, then is deleted.

### Snapshot-Based Customization

Custom sandbox images are built from a `Dockerfile` via Daytona's snapshot mechanism. The build script uses content-hashing (`byoc-env-default-<sha8>`) for idempotent rebuilds — re-running no-ops if the Dockerfile hasn't changed. A minimal working snapshot (`Dockerfile.minimal`) is just `FROM python:3.12-slim` with basic utilities.

Per-session overrides are possible via `session.metadata` keys:
- `daytona.snapshot_name` — Use a specific named Daytona snapshot instead of the default.
- `daytona.sandbox_id` — Attach an already-prepared sandbox (for pre-seeding state like cloning a repo or loading a dataset).

### In-Sandbox Runner

The orchestrator launches a small Python process inside each sandbox using Anthropic's `EnvironmentWorker`, which composes skill download, tool dispatch, heartbeat management, and force-stop on exit. The environment key (scoped to a single environment) is the only credential the runner needs. For multi-tenant deployments, Daytona recommends giving each tenant its own environment.

### Full Container Ownership

Beyond running the agent's tool runner, developers can shell into the container, mount volumes, pre-install per-customer code, warm caches, run sidecar processes, and attach observability. The runner is one process in a container the developer owns end to end.

## Relationship to Daytona Platform

Daytona provides fast, stateful composable computing environments provisioned in under 60 milliseconds. The company open-sourced Daytona in March 2024, raised a $5M Series A led by Upfront Ventures in June 2024, and surpassed 1M+ sandboxes per day by October 2025.

## Related Pages

- [[concepts/anthropic/managed-agents|Claude Managed Agents]] — The Anthropic platform this integrates with
- [[comparisons/claude-managed-agents-sandbox-providers|CMA Sandbox Providers Comparison]] — Side-by-side comparison of all four providers
- [[entities/ivan-burazin|Ivan Burazin]] — Daytona Co-Founder & CEO
- [[entities/daytona-io|Daytona]] — Daytona platform and company
- [[entities/anthropic|Anthropic]] — Platform partner
- [[concepts/agent-sandboxing|Agent Sandboxing]] — Broader sandboxing patterns
- [[concepts/headless-saas|Headless SaaS]] — Concept coined by Ivan Burazin
