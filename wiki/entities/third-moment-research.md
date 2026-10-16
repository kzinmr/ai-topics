---
title: "Third Moment Research"
type: entity
created: 2026-10-15
updated: 2026-10-15
tags: [company, ai-agents, agent-harness, long-horizon, quantization, frontier-models, case-study]
aliases: [Third Moment, ThirdMoment]
sources:
  - raw/articles/2026-10-14_openai_third-moment-research-10000-agents.md
confidence: medium
related:
  - "[[concepts/outer-harness]]"
  - "[[concepts/long-horizon-agents]]"
  - "[[concepts/token-economics]]"
  - "[[entities/openai]]"
---

# Third Moment Research

## Overview

**Third Moment Research** is an applied AI-research startup that runs very large fleets of autonomous coding agents on hard, measurable problems — most publicly, **quantitative finance**. It is notable as the reference case for OpenAI's October 2026 story on running **~10,000 agents for 36+ hours**, and for its use of an **outer harness** wrapping the Codex harness as a subagent. Co-founders quoted: **Adam Khakhar** and **Jeffrey Yan**.

## What they do

Third Moment builds "specialized AI employees" — agents that internalize a company's tacit workflows, tools, and definitions of success and execute *specialized* work (the "third moment" framing: after ChatGPT made knowledge universally available and agentic tools made execution cheap, the next frontier is encoding *judgment*). Their flagship demonstration is a quantitative-research swarm that improves a baseline trading system.

## How they run agents (Oct 2026)

- **Inner harness:** the default **Codex harness** inside Docker; each agent gets ~1 TB of data, documentation, and a research repo (feature engineering, GPU model training, trading strategies, simulation modules).
- **Outer harness:** GPT-6 Sol / GPT-6.1 Sol supervising Codex-as-subagent — inspecting unfinished trajectories and retrying, terminating, or escalating to humans. See [[concepts/outer-harness]].
- **Models:** GPT-6 Astra, GPT-6 Sol, GPT-6.1 Sol for reasoning; GPT-5.6 Terra for targeted/security checks; GPT-6 Luna under test. GPT-6.1 Sol is their "most-used model given its token efficiency" — matching Astra's performance with the fewest tokens.
- **Token-efficiency wins:** Codex+GPT-5.6 profiled a backtest and shipped a caching + memory-packing fix, cutting it from ~3 hours to ~3–5 minutes, reducing token waste and context pollution.
- **Security at scale:** they use the **Daybreak** platform so agents penetration-test their own sandbox (checking for escape to the wider network) before simulations launch.

## Notable results & roadmap

- Agents improved the baseline trading system; a GPT-6.1 Sol session surfaced an unanticipated finding (large volume share from non-displayed trades on an exchange).
- A latency benchmark (speed up a live scoreboard while preserving outputs) showed GPT-6 Astra delivering the biggest speedup vs. an expert-crafted solution.
- Roadmap: from individual investigations to **hundreds of thousands of collaborating subagents**, trillions of tokens, chains of dozens of dependent experiments, and autonomously improving agents over time.

## Why it matters

Third Moment is the clearest public artifact of the [[concepts/long-horizon-agents]] + [[concepts/agent-swarms]] thesis operating as a *business* rather than a demo, and its token-efficiency-first model selection is a concrete data point for [[concepts/token-economics]].

## Sources

- OpenAI, "How Third Moment Research runs 10,000 agents for 36+ hours" (Oct 14 2026) — `raw/articles/2026-10-14_openai_third-moment-research-10000-agents.md`
