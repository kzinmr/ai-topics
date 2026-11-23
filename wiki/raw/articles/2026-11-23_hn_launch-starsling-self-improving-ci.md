---
title: "Launch HN: StarSling (YC P25) – Self-improving CI for agent-volume repos"
url: "https://news.ycombinator.com/item?id=50536468"
source: active-crawl
date: 2026-11-17
type: hn-launch
fetch_method: hn-algolia-items-api
---

# Launch HN: StarSling (YC P25) – Self-improving CI for agent-volume repos

Source: https://news.ycombinator.com/item?id=50536468 (89 points, 2026-11-17)
Founders: Yonas (previously founded StackShare, 1.5M devs) and Daniel (ex-Netflix internal developer portal), starsling.dev, YC P25.

## Full Launch Post (from HN Algolia items API)

We're Yonas and Daniel and we're building StarSling (https://starsling.dev), fast GitHub Actions runners with AI agents that ship PRs to continuously improve your tests and workflows. Every CI job gets its own ephemeral sandbox on the fastest Zen 5 machines and NVMe Disk with unlimited concurrency so a burst of agent PRs all run at once.

We're different from other runners because ours come with agents that cut down your CI bill over time. PRs are generated through our CI harness, which runs an agent loop that's tuned to improve your CI speed and reduce cost.

**Mastra now merges over 1,800 PRs a month** and we got their slowest workflow from 29m 56s on GitHub-hosted runners down to 5m 06s (5.87x) on StarSling.

We realized the true value of having an agent loop running on top of fast runners when our agents found an 11-month-old performance bottleneck in better-auth. The fix made one of their test jobs 5.4x faster: https://github.com/better-auth/better-auth/pull/10762

I previously founded StackShare, which grew to over 1.5M developers. Daniel helped build Netflix's internal developer portal. Last year we started building AI agents for DevOps because shipping code to prod fell way behind agentic coding. We hit the CI bottleneck ourselves as we were building agents. Our own agents shipped so many PRs that at peak our job queues were backed up for hours and **our CI bill got close to our inference bill**.

We now support per-second billing, and just shipped StarSling Disks - persistent disks that give you a 4.9x speedup in dependencies ready over actions/cache. Demo: https://www.youtube.com/watch?v=2JrrpRm9Mww

Our CI harness runs a loop that has agents:
- Analyze your workflows, run logs, and machine telemetry
- Propose an optimization
- Test your unchanged workflow side by side the proposed change
- Deterministically judge that the difference is statistically significant
- Ship the winner to you as a PR with benchmarks evidence

We benchmarked open source repos on our runners and average 10x speedup in wall clock time with 70% less runner time:
- starsling-demo-org/benchmark-gogs (12.8x)
- starsling-demo-org/benchmark-shellcheck (5.5x)
- starsling-demo-org/benchmark-chatwoot (3.9x)
- starsling-demo-org/benchmark-transfer.sh (11.7x)
- starsling-demo-org/benchmark-mirotalksfu (36.4x)

Yes, you can do these optimizations yourself with prompts so we've released skills for this: https://github.com/starslingdev/skills. The benefit of using our agents is that you don't need to spend tokens and CI compute finding optimizations yourself.

We started building our runners on AWS at the beginning of the year and realized that was too expensive. But at that time there weren't any cloud providers that could give us the same machines we were getting on AWS, billed per minute (microVMs). So we convinced a handful of sandbox providers to get Zen 5s and started benchmarking them publicly (https://github.com/starslingdev/hpc-sandbox-benchmarks).

We've learned that fast infrastructure is table stakes for CI, but it's not sufficient on its own. To get fast and cost effective CI you need a process that continues making improvements. We turned CI optimizations from OpenAI, Anthropic, Linear and others into playbooks for your agent: https://starsling.dev/ci-playbooks
