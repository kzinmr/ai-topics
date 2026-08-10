---
title: Dan Luu
description: Software reliability engineer and data analyst known for systematic incident analysis and empirical studies of tech company failure modes.
type: entity
created: 2026-06-08
updated: 2026-08-10
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
  - raw/articles/danluu.com--cocktail-ideas--305e725e.md
  - raw/articles/danluu.com--latency-mitigation--06d7b2ea.md
  - raw/articles/danluu.com--overwatch-gender--17650033.md
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
- **[Cocktail party ideas](https://danluu.com/cocktail-ideas/)** (site undated; references Hillel Wayne's trad-engineering crossover project, ~2021) — Essay on the **illusion of explanatory depth** in tech circles: people with cocktail-party-level knowledge of a field propose confident fixes while missing the field's hidden complexity. Key cases: programmers' misconceptions about civil engineering (bridge-building predictability myths debunked via Hillel Wayne's crossover interviews; geotechnical engineering/preload as invisible sub-field), the "building a plane while flying" trope, Rebecca Lawson's bicycle-drawing study (60/94 participants drew non-working bikes), the jam-experiment / paradox-of-choice folktale (Manzi's *Uncontrolled*: 35 jars, one store, two Saturdays), and the dual-core chip anecdote ("why don't you just staple two cores together") with Intel's twice-failed SMT verification. Luu's own corrective: the gap between stated ideas and knowledge of sub-problems is the real signal; "mathematical maturity"-style tacit thinking is the unnameable equivalent in other fields.
- **[Latency mitigation strategies (by John Carmack)](https://danluu.com/latency-mitigation/)** (archive page undated; classic VR-era essay from the early-2010s Oculus period, archived by Luu after Carmack's original disappeared from the internet) — Carmack's canonical motion-to-photons latency treatise for head-mounted displays: ~20ms absolute latency as the threshold for imperceptibility; latency budget breakdown across sensors (analog filtering, USB sampling jitter up to 8ms at 125Hz HID), displays (LCD switching ~10ms, consumer multi-frame buffering up to 50ms, incremental scanout causing "waggle" shear on fast OLED HMDs), and host processing (vsync floor of 16ms, GPU command buffering, pipelined CPU/GPU/VID architectures costing 32-64ms); measurement via high-speed video frame counting; reduction strategy hierarchy (true latency reduction over extrapolation, prevent GPU buffering with SwapBuffers→tiny draw→fence→block, aggressive sensor prediction only to smooth jitter).
- **[Randomized trial on gender in Overwatch](https://danluu.com/overwatch-gender/)** (2018) — Self-run randomized experiment (339 games, ~half with masculine / half with feminine username) measuring gendered treatment in Overwatch: sexual/gendered comments were not observably different between conditions, but being told how to play was sharply higher with a feminine name (F comp 19% vs M comp 6%; F QP 4% vs M QP 1%, 50% intervals), with qualitatively harsher tone in the feminine condition. Notable for its methodology discussion: non-pre-registration, threats to validity, manual comment coding (state-of-the-art sentiment analysis "often return[s] nonsensical results"), and uncertainty-interval presentation. Non-AI content, catalogued for author completeness.

## References

- [danluu.com](https://danluu.com/) — Personal blog and research archive
- [A decade of major cache incidents at Twitter](https://danluu.com/cache-incidents/) — Co-authored with Yao Yue. Documents 6 SEV-0 and 6 SEV-1 cache incidents at Twitter (2012–2022).
