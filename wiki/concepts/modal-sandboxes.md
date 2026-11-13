---
title: Modal Sandboxes
created: 2026-04-30
updated: 2026-11-13
type: concept
tags: [ai-agents, infrastructure, coding-agents, sandbox, cpu]
sources:
  - raw/articles/2026-04-30_ramp-inspect-background-agent.md
  - raw/articles/modal.com--blog-unpacking-sandbox-startup-latency--b8f065a9.md
  - raw/articles/modal.com--blog-nvidia-vera-sandboxes--1cb9000c.md
  - raw/articles/modal.com--blog-sandbox-bursting--538a1b6f.md
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

## Burst, don't reserve — active-resource pricing (Nov 2026)

Modal's resourcing/pricing thesis for agent sandboxes: **"Across Modal, a typical Sandbox spends more than half its life using less than 6% of its peak CPU."** A coding-agent sandbox sits nearly idle while the model reasons and spikes only when installing dependencies, running tests, or building — the same shape recurs in RL rollouts, evals, and app builders.

**Replayed evidence — Terminal-Bench 2.1 "fix-code-vulnerability"** (bottle.py header-injection fix): a full agent session runs **2 minutes 46 seconds** with CPU **near zero except brief pytest spikes** and memory near **47 MiB**, both under the **0.125-core / 128 MiB default request**; the agent spends 33s waiting on the model plus two 60-second sleeps it asked for. 10 model calls, 367 tests passing at the end.

**Three-tier resource model**:
- **Request** (default 0.125 cores · 128 MiB) — guaranteed, billed even when idle.
- **Burst** — grows past the request into a shared pool of the machine's idle capacity that Modal's scheduler keeps free on every machine; billed per-second for actual use. Default: CPU bursts up to **16 cores** above request; memory unlimited.
- **Limit** (optional) — caps usage; use for evals/RL rollouts needing a consistent environment (set request = limit), or to bound runaway-agent cost. A sandbox **within its request is never evicted**; crossing the memory limit means OOM termination.

**Active-resource pricing math**: cost ≈ runtime × rate × **average** cores/GiB (each second billed at the higher of request and actual use). Estimate from average usage, not peak. Worked example — a 20-minute coding-agent task: average billed use 0.44 CPU · 0.94 GiB vs peak 6.00 CPU · 2.30 GiB; a reservation sized for the busiest minute (1.5 CPU · 3 GiB) costs **20.0¢/Sandbox-hr** vs Modal bursting at **8.4¢** (14.19¢/CPU·hr + 2.40¢/GiB·hr) — **58% savings**. Billing note: Modal prices CPU by **physical core** (1 CPU ≈ 2 vCPU) while most sandbox providers bill per vCPU.

**Why pooling works**: law of averages — co-tenant sandboxes run unrelated workloads and rarely spike simultaneously, so a machine needs room for the *max simultaneous* usage, not the *sum of peaks* ("the same reason a power grid can be much smaller than the sum of every household's peak demand"). On CPU contention bursting sandboxes simply slow down; on memory contention they may be OOM-evicted — Modal backs this with an **SLO: <0.0001% OOM rate per minute for bursting sandboxes under 8 GiB (~1 eviction per 694 Sandbox-days)**. Mitigations: exit snapshots, filesystem snapshots, Volumes, termination-reason SDK for retry-on-eviction.

Source: raw/articles/modal.com--blog-sandbox-bursting--538a1b6f.md

## Related Concepts

- [[concepts/coding-agents/background-coding-agent]] — Modal is the execution layer for background agents
- [[concepts/warm-start-optimization]] — Modal snapshots enable fast warm starts
- [[sandbox/infrastructure]] — Modal is an infrastructure-level sandboxing technology
- [[entities/modal-labs]] — company page with Vera CPU benchmark detail

## Sources

- Ramp Engineering, "Why We Built Our Background Agent", builders.ramp.com, April 2026
- raw/articles/modal.com--blog-nvidia-vera-sandboxes--1cb9000c.md
