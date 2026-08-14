---
title: Dan Luu
description: Software reliability engineer and data analyst known for systematic incident analysis and empirical studies of tech company failure modes.
type: entity
created: 2026-06-08
updated: 2026-08-14
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
  - raw/articles/danluu.com--programming-books--e046e92b.md
  - raw/articles/danluu.com--why-benchmark--b53029a8.md
  - raw/articles/danluu.com--branch-prediction--2971bd41.md
  - raw/articles/danluu.com--talent--62694a87.md
  - raw/articles/danluu.com--essential-complexity--83af4861.md
  - https://danluu.com/cache-incidents/
  - https://danluu.com/why-benchmark/
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
- **[Programming book recommendations and anti-recommendations](https://danluu.com/programming-books/)** (site undated; fetched 2026-05) — Luu's field-by-field reading list built on the premise that universal "N books every programmer must read" lists are nonsense: the field is too broad and learning preferences differ too much for any single book to be required for everyone. Recommendations by topic: algorithms (Dasgupta as best intro, Skiena for the practical/math-averse, CLRS and Kleinberg & Tardos as class textbooks that fail as standalone intros, randomized-algorithms book as the most practically useful), operating systems (xv6/Remzi-style book as the great implementation-first intro, Love's Linux Kernel Development, Russinovich's Windows Internals as the most comprehensive), computer architecture (Hennessy & Patterson's Quantitative Approach for constraint tradeoff reasoning, incl. data-center design chapter), auction theory/mechanism design (Krishna as the comprehensive modern text, FCC spectrum auction book on real-world mechanism bugs costing billions), misc (critique of Google SRE book's "only SRE model" assumption, Refactoring's mainstreamed code smells, Peopleware skepticism — meta-evidence that its prescriptions don't correlate with company success, Microsoft/Twitter culture books, Galenson on productivity and age), math (Apostol over the edition-mill Stewart), hardware (nand2tetris, CMOS texts, solid-state devices). Anti-recommendation patterns: textbooks that crank out money-driven editions, and classics recommended as intros that don't work as intros. Non-AI content, catalogued for author completeness.
- **[Measurement, benchmarking, and data analysis are underrated](https://danluu.com/why-benchmark/)** (site undated; ~2019, one of Luu's most-cited essays) — The canonical statement of Luu's measurement philosophy: because almost nothing is rigorously measured, measurement projects are higher-ROI than building projects ("if anything, because measurement is, like writing, not generally valued, it's much easier to find high ROI measurement projects than high ROI building projects"). Central case study: Kyle Kingsbury's Jepsen distributed-systems correctness testing (Redis losing 56% of writes during a partition, MongoDB "drop a phenomenal amount of data", RabbitMQ ~35% acknowledged-write loss, Elasticsearch health endpoint reporting green during split-brain, etc.) — the rare measurement effort that forced an entire industry to change methodology. Other impact examples: his keyboard-latency post led major gaming-device manufacturers to start optimizing input latency; Consumer Reports' headlight/ABS testing gave engineers internal ammunition (Tesla's brake fix after CR/Car and Driver measured 152 ft. stops). Also covers why most published reviews can't be trusted (manufacturer hand-picked review units for cars, lenses, SSDs; Wirecutter's poor methodology; the only reliable model is an independent purchaser like Consumer Reports), and an appendix cataloguing ~25 of his own measurement projects (keyboard-vs-mouse, terminal latency, web bloat, filesystem errors, etc.). Non-AI content, catalogued for author completeness — but directly relevant to AI eval culture ([[concepts/ai-benchmarks]]): the Jepsen pattern is the closest analogue to how independent benchmark suites force frontier labs to fix real capability gaps, and "reviewers must buy their own units" maps onto eval contamination/overfitting debates.
- **[Branch prediction](https://danluu.com/branch-prediction/)** (2017) — Pseudo-transcript of the talk he gave at Two Sigma on 8/22/2017 to kick off RC's "localhost" series. Explains why CPUs do branch prediction (pipelining makes branches a serialization point; prediction is what allows deep pipelines) and walks through the algorithm progression: static schemes (always-taken, BTFNT — backwards-taken-forwards-not-taken, ~80%), one-bit dynamic predictors (85%), two-bit saturating counters (~90%), global-history + correlated-branch schemes (93%), and how to read a modern branch-prediction paper. Non-AI content, catalogued for author completeness — useful background for evaluating inference-hardware performance claims.
- **[Misidentifying talent](https://danluu.com/talent/)** (site undated; fetched 2026-05) — Essay on how even the most measurable fields systematically misidentify talent, using baseball scouting reports as the running case (scouts rated Derek Jeter/Jim Abbott by body type and "good face"; Adam Eaton got glowing reports and flopped; Albert Pujols was dinged for weight). Argues height/appearance-based halo effects are *stronger* in consulting/programming career success than in baseball (where height actually conveys advantage) — evidenced by chess/go/shogi top players clustering at average height, and by the weak height-IQ-performance correlations. Documents resume-name bias studies (Bertrand & Mullainathan; white- vs Asian-sounding names), informal polling of engineers showing evaluation clusters (output-based vs height/confidence-based vs credential-based), and the promotion-system catch-22 (junior staff can't get high-impact work because they're too junior to be trusted with it). Ends optimistically: companies that ignored pedigree/whiteboarding/cultural-fit criteria had "by far" the best engineering teams he's worked with. Non-AI content, catalogued for author completeness — relevant background for AI hiring/eval bias debates.
- **[Against essential and accidental complexity](https://danluu.com/essential-complexity/)** (site undated; ~2020 with a 2022 update) — Systematic dismantling of Fred Brooks' *No Silver Bullet* (1986) claim that ≥1/2 of programming complexity is essential, bounding total tech-enabled productivity gains to ~2x. Counter-arguments: the bound is uncomputable (requires anticipating all future tools); Brooks wrote off categories that then exploded (scripting languages, GC languages, fuzzers, static analysis, CI/CD, version control — Win2k's 5000-person team could merge only 100 changes/day pre-modern VCS); Brooks dismissed AI right before neural nets unified speech/image recognition; his 2010 *Design of Design* reused the same stale examples. Concrete appendix: modern log-scraping and Presto/ggplot metrics tasks are "nearly entirely accidental complexity" — essential fraction arguably <1%, with 1986→2020 speedups of many orders of magnitude. 2022 update rebuts "Brooks obviously meant X" readers as self-refuting. Non-AI content, catalogued for author completeness — relevant framing for agentic-coding productivity claims ([[concepts/agentic-engineering]]).

## References

- [danluu.com](https://danluu.com/) — Personal blog and research archive
- [A decade of major cache incidents at Twitter](https://danluu.com/cache-incidents/) — Co-authored with Yao Yue. Documents 6 SEV-0 and 6 SEV-1 cache incidents at Twitter (2012–2022).
