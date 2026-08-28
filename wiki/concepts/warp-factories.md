---
title: "Warp Factories (Cloud Software Factory Infrastructure)"
created: 2026-08-19
updated: 2026-08-28
type: concept
tags:
  - coding-agents
  - agent-infrastructure
  - agent-observability
  - self-improving
  - developer-tooling
  - self-driving-codebases
aliases:
  - Warp Factories
  - cloud software factory infrastructure
related:
  - concepts/dark-factory-software-factory
  - entities/warp-terminal
  - concepts/agentic-engineering
  - concepts/interaction-centric-agent-failure-taxonomy
sources:
  - raw/articles/2026-08-19_warp_open-infrastructure-for-building-a-software-factory.md
  - raw/articles/2026-08-28_warp_agent-self-improving-software-factories.md
  - https://www.warp.dev/blog/open-infrastructure-for-building-a-software-factory
---

# Warp Factories (Cloud Software Factory Infrastructure)

**Warp Factories** (announced Aug 18 2026, closed beta) is Warp's productization of its internal cloud software factory into deployable, **open, flexible infrastructure**: engineering orgs deploy their own cloud factories that triage → spec → implement → review → verify work items, with any model and any harness, on codebases where the org owns the data, inference, and compute. Warp's own claim: ~30% of internal tasks currently automated through factories. The strategic move: position the software factory as *infrastructure you build on* (like CI/CD), not a SaaS product or "AI teammate."

## Why: the two problems interactive agents don't solve

Per Warp's framing (echoes of their June 2026 "factory engineers" memo):

1. **Measuring & improving coding-agent ROI over time** — usage grows, cost unclear, open-weight models should be in the mix; teams want throughput/cost/quality that improve over time, not frontier-only lock-in
2. **Governance & control** — every dev installing a bespoke agent on their laptop with access to all logged-in systems is a security hole; no standardization of skills/MCPs; all data exhaust lost, making standards and measurement impossible

## Architecture (what's actually new vs. prior Warp factory series)

| Component | What it does |
|---|---|
| **Foreman agent** | Orchestrator triggered by Slack/Jira/GitHub/Linear events; splits work into subagents, picks model+harness+context per subtask to optimize cost/quality |
| **Assembly-line agents** | Default: Triage, Spec, Implement, Review — each with its own skills/MCPs/permissions + computer-use on Linux & Mac (implementation agent click-verifies its own UI changes end-to-end; video saved to PR descriptions) |
| **Factory-as-code** | Factories are version-controlled definitions (Terraform-style): roll back, canary, test; and *agentic changes to the factory itself* |
| **Metrics/evals** | Queryable cost/velocity/quality/ROI metrics (control room + API + Factory MCP); built-in scorers (tokens spent, code quality, defect rate) + custom scorers |
| **Self-improvement loops** | "Observer" agents score a % of runs and open **PRs that modify the factory's own definitions** (model/harness choice, context, skill contents) |
| **Benchmarks** | Repeatable cross-configuration comparisons on curated tasks (e.g. "GLM 5.2 in Warp harness vs. Claude Code running Opus" on frontend tasks) |
| **Factory MCP** | Interop: any coding agent (Claude Code, Codex, Cursor) can push work in, pull work down, or guide sessions |
| **AI sovereignty** | BYO inference / BYO hosting / host all data exhaust (conversations, evals, memories) / zero-data-retention option |

## Closed-Loop Spec (Aug 27, 2026 follow-up: "Closing the loop with self-improving cloud software factories")

Warp's Aug 27 follow-up formalizes the self-improvement loop as an engineering discipline ("meta-engineering"), with five acceptance criteria for evaluating any factory platform:

| Criterion | Detail |
|---|---|
| Factory-as-code | `factory.yaml` manifest + directory hierarchy of agent definitions, skills, MCPs, model routing rules — version-controlled, **editable by agents via diffs** (the basis of self-improvement) |
| Cloud-resident | Local-first ≠ factory: agents must run 24/7 in cloud dev environments; all traces/telemetry stored centrally as "raw material of improvement"; team-tool (Slack/Jira/GitHub) integration |
| API-first runtime | Launch/steer/retrieve-history/telemetry APIs — makes the factory *observable by other agents*; CLIs and MCPs are built on top, AWS/GCloud-style |
| Built-in metrics | DORA-adjacent but inner-loop: **PR throughput, avg cost per PR, automation percent (human touchpoints per PR), savings vs human work**; shipped-product acceleration is the hard-to-measure fifth |
| Multi-model/multi-agent | Model routing must be swappable so model/harness improvements flow through automatically |

**Scorers**: grade functions (human / code / LLM-as-judge) over agent run traces + human-interaction data from integrated tools; Warp ships defaults for correctness, cost efficiency, verbosity. Sampling strategy matters — scorers cost money.

**The 4-step loop**: (1) factory agents build → (2) scorer agents grade runs every ~2h → (3) self-improvement agents review graded runs and open diff PRs against the factory definition → (4) humans review & merge.

**Benchmarks vs self-improvement loops**: the loop is "an intelligent person suggesting changes from past results"; true A/B confidence needs the benchmark system — pick 5–10 reference tasks, run configurations (e.g. model mixtures for frontend work, incl. open-weight viability) in parallel, score with the same scorers, output a results matrix; an agent synthesizes the winner into a factory-definition diff. Closes the loop again.

^ [raw/articles/2026-08-28_warp_agent-self-improving-software-factories.md]

## Positioning in the wiki's thread

- This is the infrastructure layer of the [[concepts/dark-factory-software-factory|dark factory]] trajectory: StrongDM's dark factory (no human code review) and Vercel's 35%-factory-PRs are *practices*; Warp Factories is the *platform* bet that factories become as ubiquitous as CI/CD
- The self-improving factory (observer agents PR-ing into factory definitions) is a concrete instance of the [[concepts/self-evolving-agents|self-evolving agent]] pattern applied to the SDLC loop itself
- Contrast with Harvey II's vertical context-lock-in (spaces + matter memory) and the general context-portability debate: Warp's counter is multi-model/multi-harness openness + org-owned data exhaust, i.e. anti-lock-in by keeping the whole factory stack in your VCS
- Open question: with factories as code and self-modifying observers, failure localization becomes a first-class ops problem — see [[concepts/interaction-centric-agent-failure-taxonomy]] (Scale AI, Jul 2026) for where to attribute a bad factory PR

## Caveats

- Closed beta; $10k usage credit for early orgs; all throughput/ROI figures are Warp's own
- "Factory as CI/CD ubiquity" is a prediction, not a measured adoption rate

## Related

- [[concepts/dark-factory-software-factory]] — the L5 autonomy level Warp Factories is infrastructure for
- [[entities/warp-terminal]] — parent company; "factory engineers" memo; prior 4-part factory series
- [[concepts/agentic-engineering]] — the broader discipline
- [[concepts/self-evolving-agents]] — observer agents improving the factory

## Sources

- [Warp blog: "Introducing Warp Factories — open, flexible infrastructure for building your software factory"](https://www.warp.dev/blog/open-infrastructure-for-building-a-software-factory) (Aug 18 2026, Zach Lloyd)
- [[raw/articles/2026-08-19_warp_open-infrastructure-for-building-a-software-factory]]
