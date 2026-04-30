---
title: Modal Sandboxes
created: 2026-04-30
updated: 2026-04-30
type: concept
tags: [ai-agents, infrastructure, coding-agents]
sources: [raw/articles/2026-04-30_ramp-inspect-background-agent.md]
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

## Key Advantages Over Docker/Local

1. **No capacity planning** — serverless means infinite scale
2. **Fast cold starts** — images pre-built and cached
3. **Snapshot/restore** — state persistence across session pauses
4. **Multi-tenant isolation** — each user gets a dedicated sandbox

## Trade-offs

- **Cost**: Serverless pricing can be expensive for long-running sessions
- **Image rebuild cycle**: 30-minute gap means agents may work on slightly stale code
- **Vendor lock-in**: Tightly coupled to Modal's infrastructure APIs

## Related Concepts

- [[background-coding-agent]] — Modal is the execution layer for background agents
- [[warm-start-optimization]] — Modal snapshots enable fast warm starts
- [[sandbox/infrastructure]] — Modal is an infrastructure-level sandboxing technology

## Sources

- Ramp Engineering, "Why We Built Our Background Agent", builders.ramp.com, April 2026
