---
title: "Dylan Patel"
tags: [- person]
created: 2026-04-24
updated: 2026-04-24
---

tags:
  - person
---
title: "Dylan Patel"
date: 2026-04-10
sources:
  - "https://www.dwarkesh.com/p/dylan-patel"
  - "https://semianalysis.com/dylan-patel/"
  - "https://www.youtube.com/watch?v=mDG_Hx3BSUE"
tags: [person, analyst, semiconductors, ai-infrastructure, semi-analysis]
aliases: ["dylan-patel-semianalysis"]
related:
  - "[[compute-scaling-bottlenecks]]"
  - "[[dwarkesh-patel]]"
  - ""
---

# Dylan Patel

| | |
|---|---|
| **Role** | Founder, CEO, and Chief Analyst at SemiAnalysis |
| **Organization** | SemiAnalysis — boutique AI & semiconductor research firm |
| **Location** | San Francisco Bay Area |
| **Years Active** | 2020 – Present |
| **X/Twitter** | [@dylan522p](https://x.com/dylan522p) |
| **LinkedIn** | [dylan-patel-90ba03126](https://linkedin.com/in/dylan-patel-90ba03126) |
| **Known for** | Deep technical analysis of semiconductor supply chains, AI compute economics, and hardware bottlenecks |

## Overview

Dylan Patel is the **Founder, CEO, and Chief Analyst** of SemiAnalysis, which he started in 2020 as a solo research blog and grew into a 12-person global team. SemiAnalysis has become one of the most respected independent research firms covering the intersection of semiconductors, AI hardware, and cloud infrastructure.

Patel is known for his **data-driven, contrarian takes** on AI infrastructure economics, supply chain dynamics, and the real-world constraints on compute scaling. Unlike many commentators who focus on model capabilities, Patel grounds his analysis in the **physical and economic realities** of chip manufacturing, packaging, memory, and power.

He is a regular guest on the **Dwarkesh Podcast**, where his March 2026 episode on compute bottlenecks became one of the most cited analyses in the AI infrastructure discourse.

## SemiAnalysis

Patel founded SemiAnalysis in 2020 as a one-person blog analyzing semiconductor trends. His writing quickly gained attention for its accuracy, technical depth, and willingness to challenge industry narratives. The firm now offers:

- **Core Research**: Subscription-based deep-dive reports for the finance industry on semiconductor supply chains, AI compute, and hardware economics
- **Breaking News**: Real-time analysis of developments across the chip ecosystem
- **Consulting**: Advisory work for Silicon Valley investors, chipmakers, and cloud providers

SemiAnalysis covers NVIDIA, AMD, Intel, TSMC, ASML, SK Hynix, Micron, and the full spectrum of AI cloud providers. Patel's reports are known for their granular supply chain tracking — from lithography equipment to packaging to data center deployment.

## The Three Bottlenecks to AI Compute Scaling

Patel's most influential framework identifies **three physical bottlenecks** that constrain AI compute scaling, each operating on different timelines:

### 1. Logic — The Immediate Constraint (2026)

In the near term, the bottleneck is **access to advanced logic chips** — primarily NVIDIA's GPU lineup and competing accelerators. Patel documented how Nvidia secured TSMC CoWoS packaging allocation years ahead of competitors, creating asymmetric advantages. Google missed the window, and despite $30B in funding, Anthropic struggled to secure compute because they were conservative on long-term contracts while OpenAI signed aggressive five-year deals.

### 2. Memory — The Incoming Crunch (2026–2028)

High Bandwidth Memory (HBM) represents the **immediate crisis**. HBM production requires approximately 4x more wafer area than standard DRAM, creating a supply shock that forces trade-offs across the industry. As HBM demand from AI accelerators grows, consumer electronics face volume reductions — potentially halving smartphone production volumes and adding ~$250 to iPhone costs. Patel flagged that Micron's CEO sold 1.17 million shares in November 2025 while publicly stating all HBM capacity was sold out.

### 3. ASML EUV Lithography — The Ultimate Constraint (2028–2030)

The **fundamental bottleneck** by the end of the decade is ASML's EUV (Extreme Ultraviolet) lithography tools. The math is stark:

- **3.5 EUV tools** are required per gigawatt of AI compute capacity
- ASML currently produces ~70 EUV tools per year, scaling to ~80 in 2026 and ~100 by 2030 under aggressive expansion
- TSMC and the broader ecosystem already have ~250–300 EUV tools deployed
- By end of decade: **~700 total EUV tools** → **~200 gigawatts of AI compute capacity**
- Sam Altman's stated target: **52 gigawatts per year**

> *"Three and a half EUV tools satisfies a gigawatt... 700 EUV tools by the end of the decade gets you to 200 gigawatts worth of AI chips."*
> — Dylan Patel, Dwarkesh Podcast (March 2026)

Each EUV tool costs **$300–400 million**, and ASML is the **world's only manufacturer**. The tools are described as "the world's most complicated machine." ASML's Q4 2025 backlog reached **€38.8 billion** (65% EUV-weighted), with record bookings of €7.4 billion in EUV alone that quarter.

> *"To scale compute further, there are different bottlenecks this year and next year, but ultimately by 2028 or 2029, the bottleneck falls to the lowest rung on the supply chain, which is ASML."*
> — Dylan Patel

## On HBM Economics and Memory Wall

Patel's analysis of the memory bottleneck goes beyond supply constraints to the fundamental economics of chip design. Key insights include:

- HBM stacks require advanced packaging (CoWoS, SoIC) that adds significant cost and complexity
- Memory bandwidth, not compute throughput, is the limiting factor for most AI workloads
- The "memory wall" — the growing gap between processor speed and memory speed — is the most pressing hardware challenge for AI scaling
- Alternative architectures (Cerebras wafer-scale, custom ASICs, optical interconnects) may partially address but not eliminate the constraint

## On China's Semiconductor Ambitions

Patel has published analysis on China's attempts to build indigenous semiconductor capacity:

- China may achieve fully indigenized DUV lithography by 2030
- Working EUV tools are possible but unlikely to reach production scale before 2030
- The West's export controls create a meaningful gap, but China's state-directed investment model should not be underestimated
- Huawei's Ascend production ramp (despite constraints) demonstrates China's ability to achieve "good enough" AI compute domestically

## On the AI Demand/Supply Chain Asymmetry

One of Patel's recurring themes is the **fundamental asymmetry** between AI demand and supply chain capacity:

- **AI demand is effectively infinite** — every lab, startup, and enterprise wants more compute
- **Supply chains scale linearly** — ASML can only produce so many EUV tools, TSMC can only build so many fabs
- **Each tier of the supply chain applies a "minus one"** heuristic — underinvesting relative to projected demand because no one believes the most aggressive forecasts
- This creates a **structural shortage** that persists regardless of capital availability

> *"The semiconductor supply chain hasn't embraced AGI-level demand scaling, with each tier applying a 'minus one' or conservative assumption about the scale of coming demand."*
> — StackAlpha analysis of Patel's framework

## On Power: "Scaling Power in the US Will Not Be a Problem"

Contrarian to the dominant narrative that power is the AI bottleneck, Patel argues that **US power scaling is solvable** through behind-the-meter generation, nuclear (SMRs), and grid infrastructure investment. The real constraint is not power generation but **semiconductor manufacturing capacity** — you can't use power you don't have chips to run.

This puts Patel at odds with the "power is the bottleneck" consensus of 2024–2025 and aligns with his broader thesis that the bottleneck always shifts to the **most constrained physical layer** in the supply chain.

## Key Quotes

> *"No sloppy seconds for Dwarkesh."* — Opening line of his Dwarkesh Podcast appearance

> *"There's having it work, and then there's production hell. ASML had EUV working in the [2010s]."* — On the gap between prototype and production scale

> *"What will be the thing that is constraining us from deploying the singularity? The biggest bottleneck is compute."*

## Related

- [[compute-scaling-bottlenecks]] — Patel's three-bottleneck framework
- [[dwarkesh-patel]] — Host of the podcast where Patel delivered his landmark analysis
-  — The broader domain Patel operates in
- [[concepts/space-gpus.md]] — Orbital compute as a potential workaround to terrestrial constraints

## Sources

- [Dylan Patel — Deep dive on the 3 big bottlenecks to scaling AI compute](https://www.dwarkesh.com/p/dylan-patel) — Dwarkesh Podcast (Mar 13, 2026)
- [Dylan Patel: Founder, CEO, and Chief Analyst](https://semianalysis.com/dylan-patel/) — SemiAnalysis
- [ASML Bottleneck: EUV Tool Shortage Will Cap AI Compute at 200 Gigawatts by 2030](https://stackalpha.io/reports/asml-bottleneck-euv-tool-shortage-will-cap-ai-compute-at-200-gigawatts-by-2030-2026-03-13-0700e4) — StackAlpha (Mar 13, 2026)
- [Exclusive: ASML plots future of chipmaking tools for AI beyond EUV](https://www.reuters.com/world/asia-pacific/asml-plots-future-chipmaking-tools-ai-beyond-euv-2026-03-02/) — Reuters (Mar 2, 2026)
