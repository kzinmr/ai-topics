---
title: "Launch HN: Maritime (YC F26) – A managed cloud for production AI agents"
url: "https://news.ycombinator.com/item?id=50549188"
source: active-crawl
date: 2026-11-18
type: hn-launch
fetch_method: hn-algolia-items-api
---

# Launch HN: Maritime (YC F26) – A managed cloud for production AI agents

Source: https://news.ycombinator.com/item?id=50549188 (60 points, 2026-11-18)
Founders: Ary and Maria, maritime.sh, YC F26. Demo: https://www.youtube.com/watch?v=lCWMdBQ96rY

## Full Launch Post (from HN Algolia items API)

Hi HN, we're Ary and Maria, co-founders of Maritime (https://maritime.sh). We're building an agent-native cloud that handles everything from custom environments to lifecycle management for AI agents.

There's been an explosion of sandbox companies coming out of SF, but sandboxes solve maybe 10% of the infrastructure problem for AI agents. The approach that most sandboxing companies take is: You buy Hetzner/OVH Cloud bare metal servers, use Firecracker to slice the servers up into VMs, sell those VMs with low margins. It's a bit of an oversimplification, but the point is it's a narrow solution to a fairly difficult problem.

We talked to a couple hundred companies that are building AI agents. From personal assistants and coding agents to specialized healthcare agents, and the main pattern we saw was that even after choosing a sandbox provider, you still have to build additional infrastructure just to get things working. These were the primary points of friction:

1. **Agent lifecycle management.** There's a lot that you have to build in order to properly give your agents VMs: things like sleep/wake, persistent storage, triggers, scheduling, per-user routing and spend caps, health monitoring, failure recovery, and deploying updates across thousands of VMs without downtime. There are so many of these small sandbox management tasks that companies have to build and maintain themselves, and they add up.

2. **Custom environments.** Production agents have varying needs. Some agents need Windows applications. Others need Android, browsers with persistent sessions, custom operating system images, preinstalled desktop software and applications, or specific dependencies. Some agents need access to private networks to interact with customer-specific things on prem, or residential IPs, or the ability to restrict network access completely.

3. **Cost optimization.** If you're selling a personal assistant for $20/month, a sandbox that costs $0.04/hour comes out to roughly $29/month if you keep it running continuously, not including LLM inference, storage, etc. There is a way to combat this though, which is to optimize sandbox usage with auto-snapshotting, making things event-driven, mounting S3 buckets to agent environments via FUSE for cheap storage, cold-tiering snapshots, etc. All roads lead to… building more infrastructure.

So what did we build differently? We give each agent its own isolated, persistent microVM and a configurable environment. On top of the compute, we built a lot of composable services: provisioning, persistent state, sleep/wake orchestration, triggers, schedule creation, monitoring, network configuration, updates, rollbacks, recovery, per-agent spend tracking, login handoffs, all the things you'd need for production agents.

We also spent a huge amount of time optimizing cost. A lot of thought was put into things such as scale-to-zero, copy-on-write over shared base images, compressed memory snapshots, hot/warm/cold snapshot and disk tiering, and other optimizations while balancing these with performance metrics like latency. As a result, Maritime costs $1 for a 2gb RAM agent per month (unlimited usage for that $1), with additional resources available as needed.

Maria was a visiting lecturer at MIT and did research at Project NANDA on agent infrastructure. Ary did research on agent coordination protocols at the same lab. We started Maritime together this March because of all the issues we faced with trying to deploy agents to the cloud during our research.
