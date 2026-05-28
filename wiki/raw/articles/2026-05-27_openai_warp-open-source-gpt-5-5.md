# Warp's Big Bet on Building Open Source with GPT-5.5

**Source:** OpenAI Blog (Customer Story)
**URL:** https://openai.com/index/warp
**Published:** May 27, 2026
**Company:** Warp (Startup, Technology)
**CEO:** Zach Lloyd

---

## Overview

Warp began as a modern terminal beloved by developers for its speed, collaboration features, and AI-native interface. As coding agents moved into everyday engineering, Warp saw the terminal as the natural hub where commands, context, collaboration, and review converge. Now, Warp is betting big on **Open Agentic Development** — a model where humans define objectives and supervise outcomes, while agents plan, write code, test changes, and open pull requests.

This year, Warp **open-sourced its terminal client** with OpenAI as the founding sponsor of the repo, signaling a commitment to building in public and shaping the future of agent-driven development.

## Key Metrics & Achievements

- **Nearly 1 million developers** use Warp; **56% of the Fortune 500** are customers.
- **90%** of Warp's internal pull requests are now co-created by agents.
- **GPT‑5.5** uses **30% fewer tokens** per agentic coding task compared to GPT‑5.4 in internal benchmarks.
- **ARR grew 35x** in the last year; **enterprise revenue up >500%** since Q4 2025.

## Open Agentic Development

Warp's **Open Agentic Development** reimagines software creation:

- **Agents write the code**; developers **specify intent, verify outputs, and decide what ships**.
- Decisions become **reusable context** for future agents, improving the system over time.
- With sufficient orchestration, agents can produce **more consistent code than a loosely coordinated group of humans**.
- Open source transforms from individual contribution to **collective product judgment and shared vision**.

## Oz — The Agent Orchestration Platform

Warp built **Oz**, a cloud orchestration platform that acts as a **control plane for deploying and coordinating agents** across local and cloud environments.

**Features:**
- **Web interface** to launch agents, select skills/environments, choose models, and configure hosting.
- **Live session monitoring** — inspect execution state, review artifacts, hand off workflows between cloud and local without losing context.
- **Recurring workflows** — agents can run like scheduled cron jobs.
- **State management** — context compaction, persistent memory, and dedicated subagents (for code search, file analysis) keep agents reliable over long-running tasks.

## Model Usage & Efficiency

- **GPT‑5.5** is used for complex, long‑horizon agentic coding tasks requiring reasoning across large problem spaces.
- Warp also uses **OpenAI models as LLM‑as‑a‑judge** in its evaluation pipelines.
- The model mix routes tasks by difficulty, sending the toughest reasoning and coding work to GPT‑5.5.

## CEO Quotes

> "We think we can ship a better Warp, more quickly, by working with our community to supervise a fleet of agents. OpenAI models help make that sustainable for the long‑horizon coding work these systems require."
> — **Zach Lloyd, CEO**

> "We've found that OpenAI models regularly provide frontier‑level intelligence while taking fewer tokens and turns to complete the same tasks. The models are especially strong for coding tasks that require reasoning across large problem spaces."
> — **Zach Lloyd, CEO**

> "No one knows exactly what the future of agentic development will look like. We think the community ought to be able to participate in shaping it."
> — **Zach Lloyd, CEO**

## Looking Ahead

Warp's combination of an open‑source terminal + Oz orchestration is a long‑term bet that development will shift from individual assistants to **coordinating persistent, parallelized agents**. The workflows are still experimental, but by building in public, Warp invites the community to shape the supervision, verification, and orchestration layers that will define autonomous coding.

## Related OpenAI Customer Stories

- [Parloa](https://openai.com/index/parloa)
- [Gradient Labs](https://openai.com/index/gradient-labs)
- [Descript](https://openai.com/index/descript)
