---
title: "Announcing Claude Managed Agents on Cloudflare"
source: "https://blog.cloudflare.com/claude-managed-agents/"
author: "Mike Nomitch"
date: 2026-05-19
source_type: blog
source_domain: blog.cloudflare.com
source_org: Cloudflare
tags: [claude, managed-agents, cloudflare, sandbox, agents, isolates, workers]
---

# Announcing Claude Managed Agents on Cloudflare

**Date:** 2026-05-19 | **Author:** Mike Nomitch | **Reading Time:** 7 min
**Source:** [Cloudflare Blog](https://blog.cloudflare.com/claude-managed-agents/)

---

## Key Highlights

Cloudflare and Anthropic have partnered to integrate **Claude Managed Agents** with **Cloudflare Sandboxes**. This gives developers more control, better security, and deeper observability for agentic workloads.

> *"Anthropic describes this as 'decoupling the brain from the hands.'"*

---

## Overview of Claude Managed Agents

On the Anthropic platform, Claude Managed Agents let developers define and run agents that can:
- Read files
- Run commands
- Browse the web
- Execute code

The harness includes built-in **prompt caching**, **compaction**, and agent-specific performance optimizations.

**Before this integration**, the entire stack had to run on Anthropic-provided infrastructure. Now, **self-managed environments** allow you to move the execution layer anywhere — including Cloudflare.

---

## What You Get Out-of-the-Box

| Capability | Details |
|------------|---------|
| **Enhanced Security** | Run all agent traffic through customizable proxies to inject credentials, prevent data exfiltration, and observe interactions. |
| **Sandbox Control & Observability** | Detailed metrics, logs, SSH access, and the ability to customize sandbox images. |
| **Lightweight Sandboxes** | Choose between full microVMs (Cloudflare Containers) or **isolates** (V8-based) for fast boot (ms), massive scale, and lower cost. |
| **Private Service Connectivity** | Connect agents to internal services without exposing them to the internet. |
| **Browser Control & Observability** | Audit trail of all browser sessions, session recordings, and human-in-the-loop flows. |
| **Email** | Each agent gets its own email address and can send/receive emails. |
| **Custom Tools** | Extend agents by writing functions and deploy — no extra infrastructure needed. |

---

## How It Works

1. **Setup** – Use the onboarding guide, fork the repo to customize.
2. **Agent Session Flow** – When a Claude Agent starts a session, it sends a message to a Cloudflare Workers-based **control plane**. The control plane provisions a sandboxed environment (isolate or microVM) for each session. State persists across session sleeps.
3. **Observation** – Monitor sandboxes in the Cloudflare Dashboard, query logs (or ship them to Datadog/Splunk), SSH into machines.

---

## Scaling to Internet Scale: Isolates vs. MicroVMs

- **MicroVM (Cloudflare Containers):** If the agent needs to act as a developer, build full applications, run Linux-based tools.
- **Isolate (V8):** If you need speed, massive scale, and minimal cost.

> *"If you want to handle bursts of tens of thousands of concurrent agents or more, running with isolates will allow you to scale in a way that no VM-based solution allows."*

---

## Security & Connectivity

- **Outbound proxies** – Inject secrets outside the sandbox so the agent never has them; protect against exfiltration.
- **Cloudflare Mesh & Workers VPC** – Connect to internal services using post-quantum encrypted tunnels.
- **Customizable egress policies** – Allowlist specific endpoints, zero-trust credential injection, custom proxy middleware.

---

## Built-in Developer Tools

All available through the Cloudflare Developer Platform:

### Browser Run
- Tools: `browser_search`, `browser_extract`, `browser_navigate`, `browser_screenshot`
- Full audit trail, session recording, human-in-the-loop

### Email
- Agents send/receive emails via their own address
- Email triggers and responses integrated into agent workflows

### Custom Functions
- Write custom tool handlers in Workers
- Deploy without managing additional infrastructure
