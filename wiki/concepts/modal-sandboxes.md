---
title: Modal Sandboxes
created: 2026-04-30
updated: 2026-10-20
type: concept
tags: [ai-agents, infrastructure, coding-agents, sandbox, cpu]
sources:
  - raw/articles/2026-04-30_ramp-inspect-background-agent.md
  - raw/articles/modal.com--blog-unpacking-sandbox-startup-latency--b8f065a9.md
  - raw/articles/modal.com--blog-nvidia-vera-sandboxes--1cb9000c.md
---

# Modal Sandboxes

## Definition

**Modal Sandboxes** are isolated, cloud-hosted virtual machines provided by the [[modal-serverless-gpu]] platform, used as execution environments for AI coding agents. They offer near-instant startup, filesystem snapshots, and serverless scaling — making them ideal for background agent workflows.

## How Ramp Inspect Uses Modal

| Feature | Implementation |
|---------|---------------|
| **Isolated VMs** | Each agent session runs in its own sandboxed Modal VM |
| **Image Registry** | Per-repository images rebuilt every 30 minutes (clone + install deps + initial build) |
| **Filesystem Snapshots** | Modal's snapshot feature freezes and restores state, keeping repos < 30 min out of date |
| **Warm Starts** | Sandboxes pre-warm as users type, finishing before the user hits Enter |
| **Serverless Scaling** | Unlimited concurrency — sessions scale with demand, no capacity planning needed |

## Architecture Flow

```
User types prompt → Modal sandbox warms up (pre-cloned image)
  → Git sync completes (≤ 30 min)
    → Agent starts reading files immediately
      → Edits allowed after sync
        → Tests run in sandbox
          → PR opened via user's GitHub token
```

### Sandbox Startup Lifecycle

Modal defines a 5-stage lifecycle for sandbox startup:

1. **Created** — Sandbox requested, no resources allocated yet. `Sandbox.create()` is asynchronous.
2. **Scheduled** — Assigned to a worker provisioning CPU/memory/GPU/volumes.
3. **Started** — Container live, entrypoint running, tunnels active. `exec(...)` available.
4. **Ready** — Application-level initialization complete (git clone, npm install, server boot). This gap is the largest real-world latency factor.
5. **In use** — Sandbox handling real work.

**Readiness Probes** (GA Jun 2026): Shell command (exit 0) or TCP port check. `sandbox.wait_until_ready()` blocks until ready. Dashboard shows 'ready' event alongside scheduled/started/terminated events.

**Optimizations**:
- **Warm Pools**: Pre-initialized sandboxes in modal.Queue, background producer maintains fullness, perceived latency drops to fetch-from-pool time.
- **Directory Snapshots**: Instant per-project state mount into generic warm sandboxes, avoiding per-user rebuilds.

Source: raw/articles/modal.com--blog-unpacking-sandbox-startup-latency--b8f065a9.md

## Key Advantages Over Docker/Local

1. **No capacity planning** — serverless means infinite scale
2. **Fast cold starts** — images pre-built and cached
3. **Snapshot/restore** — state persistence across session pauses
4. **Multi-tenant isolation** — each user gets a dedicated sandbox

## Trade-offs

- **Cost**: Serverless pricing can be expensive for long-running sessions
- **Image rebuild cycle**: 30-minute gap means agents may work on slightly stale code
- **Vendor lock-in**: Tightly coupled to Modal's infrastructure APIs

## Host CPU Choice (Oct 2026)

Modal published its first Arm-based benchmark: **NVIDIA Vera** CPUs (Arm-compatible, from the Vera Rubin platform, also sold standalone) deliver **up to 2x task throughput** vs an equivalent x86 Granite Rapids machine for sandbox workloads — while matching or beating it on single-task latency.

The result only appears under load. Modal's **Agentless Agent Bench** (50 Terminal-Bench oracle solutions/verifiers, network calls stripped, prewarmed in concurrent Docker containers) isolates the CPU work agents and RL actually do: compilation, grepping, git operations, device emulation. Straightline latency on a quiet host showed Vera marginally ahead; at 50/100/150 concurrent containers, Vera kept scaling while alternatives plateaued — attributed to high memory bandwidth enabling denser packing per core without throttling.

Why sandbox CPU characteristics differ from typical server workloads: workload shape is unknown until runtime (an LLM chooses what to run), usage is spiky (idle awaiting the LLM, then 10x bursts), and Modal's burst-above-reservation pricing model trades noisy-neighbor safety for user cost savings. Scheduler tension: higher packing density extracts more from each host and raises absolute scale, but cluster-wide demand is itself spiky, so overpacking is a standing risk.

Full methodology and benchmark detail: [[entities/modal-labs]] — "NVIDIA Vera CPUs for Sandboxes".

## Related Concepts

- [[concepts/coding-agents/background-coding-agent]] — Modal is the execution layer for background agents
- [[concepts/warm-start-optimization]] — Modal snapshots enable fast warm starts
- [[sandbox/infrastructure]] — Modal is an infrastructure-level sandboxing technology
- [[entities/modal-labs]] — company page with Vera CPU benchmark detail

## Sources

- Ramp Engineering, "Why We Built Our Background Agent", builders.ramp.com, April 2026
- raw/articles/modal.com--blog-nvidia-vera-sandboxes--1cb9000c.md
