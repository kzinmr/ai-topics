---
title: Mike Piccolo
description: Founder & CEO of iii (open-source agent orchestration engine), creator of the "Harness Is the Backend" thesis. Co-Founder/CTO of FullStack Labs. Leads the iii workers harness architecture.
url: https://iii.dev
type: entity
x_handle: "@iiidevs"
github: mfpiccolo
created: 2026-05-29
updated: 2026-05-29
aliases:
  - Mike Piccolo
  - "@iiidevs"
  - mfpiccolo
tags:
  - person
  - open-source
  - harness-engineering
  - backend-engineering
  - orchestration
  - ai-agents
sources:
  - https://iii.dev
  - https://github.com/iii-hq/iii
  - https://linkedin.com/in/mike-piccolo-55431b14
  - https://github.com/mfpiccolo
  - https://blog.motia.dev
  - raw/articles/2026-05-28_mike-piccolo-build-your-own-agent-harness-iii.md
related:
  - "[[entities/iii-platform]]"
  - "[[concepts/agent-harness]]"
  - "[[concepts/harness-engineering]]"
---

# Mike Piccolo

**Mike Piccolo** (GitHub: `mfpiccolo`, X: `@iiidevs`) is the founder & CEO of **iii** (pronounced "three eye"), an open-source orchestration engine that collapses distributed backend complexity into three primitives: Functions, Triggers, and Workers. He is also co-founder and CTO of **FullStack Labs** (since 2015), a 500+ person technology consultancy. His core thesis — **"The Harness Is the Backend"** — argues that agent infrastructure should not be a separate layer from backend infrastructure; both should share the same primitive surface.

## Background

Mike Piccolo has spent over a decade building backend systems, automation platforms, and workflows. He started as a software developer at New Leaders (ERP systems, Salesforce integrations, billing solutions), then co-founded FullStack Labs in 2015 where he has served as CTO for 11 years, overseeing technology decisions for a consultancy with 534 employees across 30 countries. He holds a BBA from San Diego State University.

In 2025, he founded **Motia** (later renamed to **iii**), an open-source AI agent orchestration framework. The insight driving iii came from observing that backend engineers face the same problem across APIs, queues, workflows, and agents: **exponential integration complexity**. As he describes it: "Six tools before you write a line of business logic, fifteen integration edges between them, and no single trace when something breaks."

## Key Theses

### The Harness Is the Backend

Piccolo's foundational thesis: agent infrastructure (the "harness") should not be a separate category from backend infrastructure. In current architectures, teams run one stack for APIs/queues/cron and another for agent loops/tools/memory — with custom integration between them. iii collapses both into the same three primitives (Functions, Triggers, Workers), treating agents as workers no different from a payment service or ML pipeline.

> "When agents are workers, thin versus thick harness is just a question of how many functions you register and how you compose them."

### Thin vs. Thick Is a Slider, Not a Fork

The classic harness debate frames itself as a binary choice: Anthropic's thin loop vs. LangGraph's explicit DAG. Piccolo argues this framing is wrong. When the harness is composed of workers on a shared engine bus, thin vs thick is a config change — add or remove workers from `config.yaml`. The slider moves without rewrites.

### Backend Complexity Is Quadratic

Piccolo identifies the root cause of backend fragility: **integration edges grow quadratically** with the number of services. Each new service (API framework, queue, cron, workflow, agent framework, observability) adds integration edges to every existing service. The solution is not a better integration tool — it's a substrate where services don't need to integrate because they share primitives.

### "The Answer to Every Backend Question Is: Add a Worker"

Rather than evaluating, procuring, and integrating a new service for each requirement, iii's model makes every capability a worker. A worker connects to the engine via WebSocket, registers functions and triggers, and is immediately discoverable, callable, and traceable across the entire system — regardless of language or runtime.

## Projects

### iii (2025–present)

Open-source orchestration engine (Rust, 15.9k ★ GitHub). Three primitives: Functions, Triggers, Workers. Ships with SDKs for Node.js, Python, and Rust; open wire protocol supports any language. The May 2026 workers harness (`iii-hq/workers`) ships 11 independently replaceable workers: turn-orchestrator, provider-*, auth-credentials, models-catalog, iii-directory, approval-gate, session, llm-budget, hook-fanout, context-compaction, harness-meta.

### Motia (2025)

Predecessor to iii. An open-source AI agent orchestration framework and Motia Hub cloud platform. Evolved into iii when Piccolo realized a framework-level solution couldn't solve the integration problem — the answer had to live one layer down in the primitives themselves.

### FullStack Labs (2015–present)

Co-founder and CTO. Leading technology consultancy specializing in custom software development, AI services, mobile/web applications, and developer resourcing. 534 employees across 30 countries.

## Writing Style

Piccolo writes in a direct, architectural voice. His articles are structured as technical walkthroughs — enumerating responsibilities (the "15 jobs"), defining primitives, and showing concrete code examples. He favors the "here's what's broken, here's the bet, here's how it works" structure. His writing bridges the gap between backend infrastructure philosophy and working production code.

## Key Articles

- **"How to build your own agent harness???"** (May 2026) — The definitive guide to iii's workers harness architecture. Enumerates 15 jobs a production harness does, the 11-worker stack, the 7-state turn FSM, and the "thin vs thick is a slider" thesis. [[raw/articles/2026-05-28_mike-piccolo-build-your-own-agent-harness-iii.md]]
- **"The Harness Is the Backend"** (April 2026) — Foundational article establishing the thesis that agent infrastructure and backend infrastructure should share the same primitive surface.

## Conference Talks

- **"Agent Orchestration: The New Full Stack in 2026"** — YouTube talk on how AI changes backend architecture and why "designing for intelligence" replaces "designing endpoints"
- **The Humans in the Loop podcast** — Deep dive on how back-end engineering needs to evolve for the agentic era

## Cross-References

- [[entities/iii-platform|iii Platform]] — The open-source engine and workers harness he founded
- [[concepts/agent-harness]] — The concept his work reimagines from the infrastructure layer
- [[concepts/harness-engineering]] — The eval-focused harness discipline alongside the operational harness he builds
- [[concepts/bitter-lesson-harnessing]] — Why harnesses should simplify as models improve

## Sources

- [iii.dev](https://iii.dev) — Official website
- [GitHub: iii-hq/iii](https://github.com/iii-hq/iii) — 15.9k ★ engine
- [GitHub: iii-hq/workers](https://github.com/iii-hq/workers) — Workers harness monorepo
- [GitHub: mfpiccolo](https://github.com/mfpiccolo) — Personal GitHub (169 followers, 101 repos)
- [LinkedIn: Mike Piccolo](https://linkedin.com/in/mike-piccolo-55431b14) — Professional background
- [Motia Blog](https://blog.motia.dev) — iii's origin story from Motia
- [The Humans in the Loop](https://thehumansintheloop.substack.com/p/the-humans-in-the-loop-deep-dive-back-end-in-the-age-of-ai) — Podcast interview
