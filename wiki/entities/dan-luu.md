---
title: Dan Luu
description: Software reliability engineer and data analyst known for systematic incident analysis and empirical studies of tech company failure modes.
type: entity
created: 2026-06-08
updated: 2026-08-08
aliases:
  - danluu
  - daniel-luu
tags:
  - person
  - infrastructure
sources:
  - raw/articles/danluu.com--cache-incidents--1d05e743.md
  - raw/articles/danluu.com--startup-options--a3b4b12e.md
  - raw/articles/danluu.com--ballmer--7af5f7cf.md
  - raw/articles/danluu.com--julialang--efa2d4b6.md
  - https://danluu.com/cache-incidents/
  - https://danluu.com/
---

# Dan Luu

**Dan Luu** is a software reliability engineer and data analyst known for systematic incident analysis, empirical studies of tech company failure modes, and data-driven critiques of industry practices. His work focuses on understanding how large-scale distributed systems fail and why organizational knowledge about failures is lost over time.

## Overview

Luu's research methodology is characterized by thorough data collection, historical incident analysis, and systematic pattern identification. Unlike typical post-mortems that focus on a single incident, Luu's work aggregates failures across years to identify recurring patterns and systemic weaknesses. This approach has been applied to Twitter cache reliability, failover testing, cloud service outages, and other infrastructure domains.

## Notable Work

### Twitter Cache Incident Analysis (2012–2022)

In "[A decade of major cache incidents at Twitter](https://danluu.com/cache-incidents/)" (co-authored with Yao Yue), Luu documented 6 SEV-0 and 6 SEV-1 cache-related incidents at Twitter over a decade, along with 38 less severe incidents. The analysis revealed several key patterns:

**Cache as a Failure Amplifier:**
- **Cascading failures**: Cache outages caused total site outages because architectures designed around cache performance lacked backing DB capacity to handle failover
- **Positive feedback loops**: High-volume, low-latency SLOs worsened "death spiral" failure modes when cache degradation triggered increased load on remaining nodes
- **Hardware-level failure modes**: Cache servers were sensitive to kernel, firmware, and hardware anomalies — including a BMC health check that caused packet drops every 20 hours 40 minutes
- **Host ejection inconsistency**: Different workers making independent routing decisions led to cache key duplication and stale data serving
- **memcached as a critical path**: The vast majority of Twitter's cache was a fork of memcached, making the findings broadly applicable to distributed systems

**Knowledge Loss in Tech Organizations:**
- Document links rot within 2–3 years (90%+ link failure rate for pre-2012 incidents)
- Human memory provides inconsistent accounts of the same events
- Viral stories about incidents are frequently wrong due to exaggeration and self-aggrandizing narratives
- "Gresham's law of stories" — incorrect stories tend to win out over correct ones in public memory

**Organizational Patterns:**
- Fixes for earlier incidents were often incompletely applied, causing repeat failures
- Issues identified by engineers as serious were frequently deprioritized until they caused major incidents
- Operational knowledge was concentrated in individual engineers rather than institutionalized

### AI Infrastructure Relevance

The cache failure modes documented by Luu are highly relevant to modern AI infrastructure:
- **KV cache management**: LLM inference serving relies on massive key-value caches with similar failure mode risks (positive feedback loops, death spirals during high-load inference)
- **Distributed inference**: Multi-node AI serving architectures face the same cache consistency and host ejection challenges documented in Twitter's memcached infrastructure
- **Prompt caching**: AI systems increasingly cache prompts and intermediate results, introducing similar staleness and inconsistency risks
- **Capacity planning**: The gap between announced and operational capacity that Luu documented in Twitter's infrastructure parallels current debates about AI data center buildout claims

## Notable Essays (Non-AI)

Luu's blog spans topics beyond reliability engineering. These essays are general-interest (compensation, tech leadership, programming languages) — catalogued here for author completeness; they are NOT AI/LLM-focused content and were triaged as non-takes by the raw-backlog pipeline.

- **[Startup options v. cash](https://danluu.com/startup-options/)** (2013, updated 2020) — Argues startup equity packages rarely beat cash+public-equity comp. Covers the risk-reward proportionality fallacy (only undiversifiable risk earns a premium; VCs diversify, employees don't), preferred vs common stock (liquidation preferences, anti-dilution — Mayhar dilution example), Black-Scholes inapplicability to startup options, strike-price/public-valuation misrepresentations, ~5% exercise rates, ISO/AMT/QSBS tax treatment, and debunks retention/incentive-alignment rationales (Netflix/Headlands cash-pay counterexamples). 2020 update: investing ~$25k/yr in seed rounds is strictly superior to early-employee equity on risk-adjusted return.
- **[Steve Ballmer was an underrated CEO](https://danluu.com/ballmer/)** (2024) — Revisionist analysis of Microsoft under Ballmer: revenue $14–22B → $83B, $27B profit on exit, and deep long-term bets (Azure, Office 365, Bing, Xbox, enterprise sales org) that set up Nadella's success. Documents the antitrust-constrained context (Microsoft chose not to kill Google for PR reasons) and internal-politics cleanup. Appendix covers TypeScript, vscode, LINQ, and Sumit Gulwani's program-synthesis work behind Excel autocomplete.
- **[A review of the Julia language](https://danluu.com/julialang/)** (2015, updated 2022) — Critique of Julia's correctness culture: 4 core-language bugs in a half-hour script, plotting regressions, non-deterministic exception handling, weak testing (FactCheck barely used; coverage tool only counted functions with non-zero coverage), slow git-backed package manager, benchmark gaming, and contributor barriers. The 2022 update documents a continued stream of silent-wrong-result bugs — including incorrect gradients in Zygote/ReverseDiff.jl AD (users switching to PyTorch/JAX) — and co-creator dismissal patterns ("illegitimate / fixed soon / already fixed").

## References

- [danluu.com](https://danluu.com/) — Personal blog and research archive
- [A decade of major cache incidents at Twitter](https://danluu.com/cache-incidents/) — Co-authored with Yao Yue. Documents 6 SEV-0 and 6 SEV-1 cache incidents at Twitter (2012–2022).
