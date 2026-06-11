---
title: "Modal Sandbox (Claude Managed Agents)"
created: 2026-05-19
updated: 2026-05-19
type: entity
tags:
  - entity
  - modal
  - sandbox
  - ai-agents
  - architecture
  - infrastructure
  - hardware
  - security
sources:
  - raw/articles/2026-05-19_modal_claude-managed-agents-sandbox.md
---

# Modal Sandbox (Claude Managed Agents)

**Modal Sandbox** is Modal's self-hosted sandbox environment for [[concepts/anthropic/managed-agents|Claude Managed Agents]] (CMA), launched May 19, 2026 in collaboration with [[entities/anthropic|Anthropic]]. Modal is a cloud platform built for AI workloads, with a custom container runtime and orchestration layer designed for fast, flexible, isolated compute. The CMA integration lets developers run all tool calls in a self-hosted Modal Sandbox while benefiting from Modal's fast cold-starts, custom images, snapshotting techniques, and cost-efficient bursting — all while maintaining Anthropic's managed agent loop.

Modal was founded with the thesis that separating the agent loop from code execution is the winning architectural pattern, because it makes security boundaries easier to reason about and gives teams more control over observability, failure handling, and scale.

## Key CMA Integration Features

### Fast Startup on Custom Images

Modal's custom container runtime delivers fast cold-starts even on fully customized images. Developers define images declaratively with `modal.Image.debian_slim()`, adding system packages via `apt_install` and Python dependencies via `uv_sync` — the full dependency tree is baked in for rapid iteration:

```python
image = (
    modal.Image.debian_slim(python_version="3.13")
    .apt_install("ffmpeg", "imagemagick", "mediainfo")
    .uv_sync()
)
```

### Rich Persistence Options

Modal offers the richest persistence menu among [[comparisons/claude-managed-agents-sandbox-providers|CMA sandbox providers]]:

- **Volumes** — Durable storage with sub-path mounts per session (`modal.Volume.from_name()` with `with_mount_options(sub_path=f"/sessions/{session_id}")`)
- **Directory snapshots** — Capture and restore specific directory trees
- **Filesystem snapshots** — Full filesystem state preservation
- **Memory snapshots** — Near-instant resume capability

### Scale: 100K+ Concurrent Sandboxes

Modal claims **upwards of 100,000 concurrent sandboxes per customer** — the highest documented concurrency ceiling among all CMA sandbox providers. Resource configuration is fine-grained with CPU (request, limit), memory (request, limit in MiB), and optional GPU access:

```python
sandbox = await modal.Sandbox.create.aio(
    ...,
    cpu=(2, 16),            # (request, limit)
    memory=(8*1024, 64*1024),  # (request, limit) in MiB
    gpu="H100",
)
```

### GPU Support

Modal is the **only CMA sandbox provider offering GPU access** (NVIDIA H100), making it suitable for ML inference, training, or GPU-accelerated workloads within agent sessions. This is a critical differentiator for AI-native workloads.

### Burst Pricing

Modal uses a **serverless burst pricing model**: pay-per-use with no minimums and no idle costs between runs. New users receive $30/month of free compute.

### Security: Short-Lived Connect Tokens

Modal provides **short-lived connect tokens** that give clients authenticated, direct access to running sandbox services without exposing them to the public internet. Credentials are passed via the Modal SDK rather than injected at a network layer.

## Production Adoption and Endorsements

Modal is the only CMA sandbox provider that publicly named specific production customers at launch:

> "Our use cases require secure orchestration of internal tools across a complex product surface. Modal's Sandbox gives us the security boundary our enterprise customers need, and combining it with Claude Managed Agents gave us a powerful harness without hand-rolling extra complexity. We had a working version up in under a week, raising reliability for our customers."
> — **Sai Yandapalli, CTO, Mason AI**

> "As we scale agentic commerce for local businesses, we need a highly efficient path to production with full harness control, scale, and reliability. We're excited to evaluate Claude Managed Agents for this next step, building on our AI infrastructure with Modal."
> — **Andy Fang, Co-founder, DoorDash**

DoorDash is building an intelligence system with a suite of AI agents spanning chat, voice, SMS, browser operation, mobile app, and in-store ordering for its merchant ecosystem. The team already runs production agents powered by Claude models, with Modal as part of their AI infrastructure.

> "Blend sits at the center of hundreds of unique banking environments. When a bug or support request comes in, the answer often lives somewhere in the intersection of code, configuration, and what the customer actually experienced. Having a fully configured environment with the right tooling, context, and credentials already in place is what makes it possible for agents to help engineers reason across all of that faster."
> — **Nima Ghamsari, Co-founder and Head of Blend**

Blend powers digital origination for banks, credit unions, and mortgage lenders, operating across hundreds of unique banking environments with different configurations, workflows, and compliance requirements. The CMA + Modal Sandboxes integration gives Blend a path to make agent-assisted development more secure, consistent, and scalable across its engineering organization.

## Reference Implementations

Modal shipped two reference examples: a CLI agent and a Slack bot, both on the same Modal + Managed Agents backbone. Developers clone, swap in their image and tools, and have the bones of a production deployment.

## Related Pages

- [[concepts/anthropic/managed-agents|Claude Managed Agents]] — The Anthropic platform this integrates with
- [[comparisons/claude-managed-agents-sandbox-providers|CMA Sandbox Providers Comparison]] — Side-by-side comparison of all four providers
- [[entities/anthropic|Anthropic]] — Platform partner
- [[concepts/security-and-governance/agent-sandboxing|Agent Sandboxing]] — Broader sandboxing patterns
- [[concepts/modal-sandboxes|Modal Sandboxes]] — Modal's sandbox technology (pre-dates CMA integration)
