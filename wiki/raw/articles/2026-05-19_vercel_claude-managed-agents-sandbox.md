---
title: "Build a Claude Managed Agent with Vercel Sandbox"
source: "https://vercel.com/kb/guide/run-claude-managed-agent-tools-with-vercel-sandbox"
date: 2026-05-19
source_type: docs
source_domain: vercel.com
source_org: Vercel
tags: [claude, managed-agents, vercel, sandbox, firecracker, microvm]
references:
  - "https://vercel.com/kb/guide/run-claude-managed-agent-tools-with-vercel-sandbox"
---

# Build a Claude Managed Agent with Vercel Sandbox

A step-by-step guide to running Anthropic's Claude Managed Agent (CMA) with **Vercel Sandbox** as the compute plane. Each session runs in an isolated microVM with credential brokering and a webhook-driven control plane.

---

## Architecture

- **Brain (Anthropic)**: Claude agent, tool-calling loop, skills, memory
- **Control plane (Vercel Function)**: receives `session.status_run_started` webhook, polls work items, spawns a sandbox
- **Compute plane (Vercel Sandbox)**: VM that attaches to the session's event stream, executes tools (`run_shell`, `read_file`), sends results back, exits when done

Key security feature: **credential brokering** injects the environment key only on outbound requests scoped to the session/work item. The key never enters the sandbox.

---

## Tool Dispatch

| Tool Type | Where executed |
|-----------|----------------|
| `bash`, `read`, `write`, `edit`, `glob`, `grep` | Inside Vercel Sandbox (runner dispatches) |
| `web_search`, `web_fetch` | Anthropic server-side |
| MCP server tools | Anthropic server-side |

---

## Key Setup Steps

1. **Create Self-Hosted Environment** via Anthropic API (or Console)
2. **Generate Environment Key** from Anthropic Dashboard
3. **Create Agent** with custom tools matching runner implementations
4. **Deploy Vercel Function** as control plane + webhook handler
5. **Define Sandbox Runner** with tool implementations (runs inside each VM)

---

## Security Model

- Credential brokering: environment key NEVER enters sandbox
- OIDC-based auth for Vercel API access (no long-lived tokens)
- Per-session microVM isolation (Firecracker-based)
- Egress control via custom proxy middleware
