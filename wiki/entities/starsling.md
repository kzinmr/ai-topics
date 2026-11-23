---
title: "StarSling (Self-Improving CI)"
type: entity
created: 2026-11-23
updated: 2026-11-23
tags:
  - company
  - startup
  - ycombinator
  - ci-cd
  - agentic-engineering
  - devops
  - agent-loop
  - autoresearch
  - developer-tooling
aliases:
  - StarSling
  - starsling.dev
sources:
  - raw/articles/2026-11-23_hn_launch-starsling-self-improving-ci.md
  - https://news.ycombinator.com/item?id=50536468
  - https://starsling.dev
---

# StarSling (Self-Improving CI)

**StarSling** (YC P25, starsling.dev) is a CI platform that combines **fast GitHub Actions runners with an agent loop that ships PRs to continuously optimize your own CI**. Founded by Yonas (previously StackShare, 1.5M developers) and Daniel (ex-Netflix internal developer portal). Launched on HN 2026-11-17 (89 points).

## Pitch: autoresearch applied to CI

Each CI job runs in its own ephemeral sandbox on Zen 5 machines with NVMe disks and unlimited concurrency, so bursts of agent-authored PRs all run at once. On top of the hardware, a **CI harness runs an agent loop** (cf. [[concepts/karpathy-loop]], [[concepts/autonomous-component-optimization]]):

1. Analyze workflows, run logs, and machine telemetry
2. Propose an optimization
3. Run the unchanged workflow side-by-side with the proposed change
4. **Deterministically judge** that the difference is statistically significant
5. Ship the winner as a PR with benchmark evidence

The side-by-side + deterministic-significance gate is the differentiator versus "just prompt an agent to speed up your CI" — StarSling ships the equivalent skills openly (github.com/starslingdev/skills) and sells the saved token/CI compute. The same loop found an **11-month-old performance bottleneck in better-auth** (PR #10762, one test job 5.4× faster) — presented as evidence the loop discovers things humans had stopped looking for.

## Origin: the agent-volume CI wall

The founders' trigger is the [[concepts/code-review-bottleneck]] shifted downstream to infrastructure: their own agents shipped so many PRs that job queues backed up for hours and **"our CI bill got close to our inference bill"** — a new cost-line ratio for agent-volume repos ([[concepts/token-economics]]). They frame it as "shipping code to prod fell way behind agentic coding," the same land-rush pressure [[entities/steve-yegge]] described in [[concepts/land-rush-cicd]].

## Key facts

- **Mastra case study: 1,800+ merged PRs/month**; slowest workflow 29m56s → 5m06s on GitHub-hosted runners (5.87×).
- OSS benchmarks: avg ~10× wall-clock speedup, 70% less runner time (gogs 12.8×, shellcheck 5.5×, chatwoot 3.9×, transfer.sh 11.7×, mirotalksfu 36.4×) — vendor-run, not independently reproduced.
- Per-second billing; **StarSling Disks**: persistent disks, 4.9× faster dependency-ready than actions/cache.
- Infra history: AWS too expensive; no provider offered AWS-comparable machines billed per-minute (microVMs), so they pushed sandbox providers to add Zen 5 and published public benchmarks (starslingdev/hpc-sandbox-benchmarks) — related to [[comparisons/agent-sandboxing]].
- **CI playbooks** (starsling.dev/ci-playbooks) codify CI optimizations attributed to OpenAI, Anthropic, and Linear as agent-consumable playbooks; cf. [[entities/linear]]'s "Linear's CI playbook for agents" (Oct 2026).

## Analysis / Reception

- Concrete instance of the **autoresearch pattern escaping model-training** into DevOps: propose → A/B → statistically-gated merge, with CI cost/speed as the metrics (vs pi-autoresearch's 40+ product metrics).
- The "CI bill ≈ inference bill" data point is one of the first public quantifications of agent-volume CI as a first-order cost line.
- Vendor numbers throughout (Mastra, benchmark multipliers); treat as company-reported.

## Related

- [[concepts/code-review-bottleneck]] — upstream human-side bottleneck; StarSling attacks the compute side
- [[concepts/land-rush-cicd]] — Yegge's megabatch CI pattern for agent volume
- [[concepts/karpathy-loop]] / [[concepts/autonomous-component-optimization]] — the general autonomous optimization loop family (pi-autoresearch is covered there)
- [[entities/mastra]] — flagship customer
- [[concepts/harness-engineering]] — the CI harness that hosts the optimization loop

## Sources

- Launch HN post: raw/articles/2026-11-23_hn_launch-starsling-self-improving-ci.md (full text captured via HN Algolia items API)
