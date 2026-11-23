---
title: "Maritime (YC F26)"
type: entity
created: 2026-11-23
updated: 2026-11-23
tags:
  - company
  - startup
  - agent-infrastructure
  - ai-agents
  - microvm
  - ycombinator
  - serverless
  - cost-optimization
aliases:
  - Maritime
  - maritime.sh
sources:
  - raw/articles/2026-11-23_hn_launch-maritime-managed-cloud-for-agents.md
  - https://news.ycombinator.com/item?id=50549188
  - https://maritime.sh
---

# Maritime (YC F26)

**Maritime** is a YC F26 startup (founded March 2026) building a **managed cloud / agent-native cloud for production AI agents**. Founded by Ary (agent coordination protocols research) and Maria (visiting MIT lecturer, agent-infrastructure research), both from the MIT **Project NANDA** agent-infrastructure lab. Launched on HN 2026-11-18 (60 points).

## Core Thesis: "Sandboxes solve maybe 10% of the infrastructure problem"

Maritime's framing directly critiques the 2026 SF sandbox boom ([[entities/e2b]], [[entities/daytona-sandbox]], [[entities/modal-sandbox]]): the common model — buy Hetzner/OVH bare metal, slice it with [[concepts/firecracker]] into VMs, sell low-margin — is a narrow answer to a wider problem. From interviews with ~200 agent-building companies (personal assistants, coding agents, healthcare agents), the recurring pattern was that after picking a sandbox provider, teams still had to build the remaining 90% themselves ([[concepts/managed-agents]], [[concepts/agent-native-cloud]]).

The three friction areas they identified:

1. **Agent lifecycle management** — sleep/wake, persistent storage, triggers, scheduling, per-user routing and spend caps, health monitoring, failure recovery, zero-downtime updates across thousands of VMs.
2. **Custom environments** — Windows apps, Android, browsers with persistent sessions, custom OS images, preinstalled desktop software, private-network/on-prem access, residential IPs, or fully restricted network egress.
3. **Cost optimization** — the "$20/month personal assistant vs $0.04/hour sandbox" problem: a continuously running sandbox (~$29/month) exceeds the product's entire consumer price before inference and storage. Mitigations (auto-snapshotting, event-driven wakes, S3-via-FUSE mounts, cold-tiered snapshots) all mean building more infrastructure.

## Product

Each agent gets its own **isolated, persistent microVM** plus a configurable environment, with composable services on top: provisioning, persistent state, sleep/wake orchestration, triggers, schedules, monitoring, network configuration, updates, rollbacks, recovery, per-agent spend tracking, login handoffs.

**Cost architecture**: scale-to-zero, copy-on-write over shared base images, compressed memory snapshots, hot/warm/cold snapshot and disk tiering — balanced against wake-latency. Headline pricing: **$1/month for a 2 GB-RAM agent with unlimited usage** for that tier, additional resources billed as needed. (Vendor-claimed; the economics depend on snapshot tiering hit rates and wake-latency trade-offs, unverified independently.)

## Analysis / Reception

- Positions Maritime against the "sandbox-as-VM-reseller" model, echoing [[entities/e2b]]'s later "Sandboxes are dead → per-agent private cloud" thesis; the difference is Maritime bundles lifecycle/orchestration as managed services rather than primitives.
- The $1/month unlimited-usage claim is the sharpest cost wedge in the agent-hosting market; it implicitly bets that agents are mostly idle and event-driven (cf. [[concepts/agent-orchestration-runtime]]).
- Founder lineage (Project NANDA) places them in the same research orbit as harness/lifecycle-systems work like [[concepts/harness-engineering]].
- Single-source at creation (Launch HN post, 60 pts); HN Q&A comments not yet mined — enrich on follow-up.

## Related

- [[concepts/managed-agents]] — Anthropic's decoupled session/harness/sandbox architecture
- [[concepts/agent-native-cloud]] — the broader paradigm Maritime claims to implement
- [[comparisons/agent-sandboxing]] — sandbox-provider landscape Maritime critiques
- [[concepts/sandbox]] — isolation primitives (Firecracker, gVisor)
- [[concepts/token-economics]] — the inference-side counterpart of the unit-economics problem

## Sources

- Launch HN post: raw/articles/2026-11-23_hn_launch-maritime-managed-cloud-for-agents.md (full text captured via HN Algolia items API)
