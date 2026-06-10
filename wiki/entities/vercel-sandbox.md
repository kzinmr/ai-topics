---
title: "Vercel Sandbox (Claude Managed Agents)"
created: 2026-05-19
updated: 2026-05-19
type: entity
tags:
  - entity
  - company
  - sandbox
  - ai-agents
  - architecture
  - agent-safety
  - infrastructure
  - developer-tooling
  - security
  - web-development
  - orchestration
sources:
  - raw/articles/2026-05-19_vercel_claude-managed-agents-sandbox.md
---

# Vercel Sandbox (Claude Managed Agents)

**Vercel Sandbox** is Vercel's self-hosted sandbox environment for [[concepts/claude/managed-agents|Claude Managed Agents]] (CMA), launched May 19, 2026. It uses a Next.js-based control plane and Vercel Sandbox microVMs to provide a TypeScript-native execution layer for CMA tool calls, with a standout security model based on firewall-level credential brokering.

## Architecture: Two-Plane Design

Vercel's CMA integration uses a clean **two-plane architecture**:

1. **Control plane (Vercel Function)** — A Next.js API route that receives `session.status_run_started` webhooks from Anthropic, polls and acknowledges work items, and spawns one Vercel Sandbox per session.

2. **Compute plane (Vercel Sandbox)** — A fresh isolated microVM per session that attaches to the session's event stream, executes tool calls (`run_shell`, `read_file`, etc.), posts results back, and exits when the session ends.

The full implementation — control plane webhook, UI, and setup scripts — lives in a single Next.js application. Tool implementations are written in `sandbox/runner.ts` and run via `tsx`.

## Key CMA Integration Features

### Credential Brokering: Firewall-Level Security (Standout Feature)

Vercel's credential brokering is the most security-hardened among all [[comparisons/claude-managed-agents-sandbox-providers|CMA sandbox providers]]. The Anthropic environment key **never enters the sandbox VM**. Instead:

- The control plane configures a `networkPolicy` on each sandbox that injects the `Authorization: Bearer` header at the **firewall level**.
- The sandbox runner uses a placeholder `authToken: "_brokered_"` — the real key is never exposed.
- Injection is **scoped by path and method**: only outbound calls to `/v1/sessions/<thisSessionId>/...` and `/v1/environments/<envId>/work/<thisWorkId>/...` receive authentication. A malicious request to `work/poll` or another session ID gets no auth and is rejected by Anthropic.
- `process.env.ANTHROPIC_ENVIRONMENT_KEY` is `undefined` inside the spawned VM. Even if an agent jailbreak or compromised tool ran `console.log(process.env)`, there is no key to leak.

This is fundamentally different from passing tokens as environment variables, which any code running in the sandbox can read.

### Egress Control: Domain Allowlist with Deny-All Default

`networkPolicy.allow` defines a domain allowlist. The default mode is **deny-all** once a policy is set — anything not explicitly allowed is blocked at the firewall. Policies can be updated on running sandboxes without restarting. A useful pattern: start with allow-all to install dependencies, then tighten the policy before running agent-generated code or processing sensitive data.

Matchers support path-prefix and HTTP method scoping for fine-grained egress:

```typescript
inject: [{
  match: {
    path: { startsWith: "/v1/write" },
    method: ["POST", "PUT", "PATCH"],
  },
  requestHeaders: { Authorization: `Bearer ${writeToken}` },
}]
```

### Snapshot-Based Fast Boot

Sandboxes boot from prebuilt snapshots. The build process creates a sandbox, installs dependencies (`npm install @anthropic-ai/sdk tsx`), copies in the runner script, snapshots the state, and uses that snapshot for all future spawns. This eliminates SDK installation and file copying on every session, reducing boot latency.

### OIDC Token Authentication

Vercel Sandbox authenticates via `VERCEL_OIDC_TOKEN` — a short-lived OIDC token pulled from the Vercel project environment. No long-lived Vercel tokens are used. The `@vercel/sandbox` SDK handles authentication automatically.

### TypeScript-Native Developer Experience

The entire integration is TypeScript/Next.js, following the same DX principles as the Vercel AI SDK, Next.js, and Turborepo. `tsx` auto-loads `.env.local`, eliminating the need for `dotenv` imports in scripts. The control plane, runner, UI, and all setup scripts share a single project.

### Webhook-Driven Orchestration

The control plane receives webhooks from Anthropic (`session.status_run_started`), verifies HMAC signatures using `client.beta.webhooks.unwrap()`, polls and acks the work queue, then spawns a sandbox. `waitUntil` from `@vercel/functions` hands the spawn off so the function returns `200` immediately while `Sandbox.create` finishes in the background.

### Durable Streaming with Vercel Workflow

For long-running sessions that exceed serverless function timeouts, Vercel offers integration with **Vercel Workflow** for durable polling, multi-turn conversations, and full event replay. The workflow run serves as both execution engine and event log.

## Battle-Tested Infrastructure

Vercel Sandbox runs on the same microVM infrastructure that has powered Vercel's build system for **10 years**, handling over a billion deployments. This infrastructure has hardened defenses against attacks agent code can encounter, including cryptominer abuse and container escapes. Sandboxes have direct, low-latency egress to AWS workloads with low data transfer costs — significant when agent tools need to reach private services.

## Related Pages

- [[concepts/claude/managed-agents|Claude Managed Agents]] — The Anthropic platform this integrates with
- [[comparisons/claude-managed-agents-sandbox-providers|CMA Sandbox Providers Comparison]] — Side-by-side comparison of all four providers
- [[entities/anthropic|Anthropic]] — Platform partner
- [[concepts/agent-sandboxing|Agent Sandboxing]] — Broader sandboxing patterns
- [[entities/vercel-labs|Vercel Labs]] — Vercel's experimental projects
- [[concepts/agent-security|AI Agent Security]] — Security patterns for agent infrastructure
