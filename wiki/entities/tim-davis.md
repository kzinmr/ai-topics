---
title: "Tim Davis"
created: 2026-05-11
updated: 2026-09-27
type: entity
tags: [person, agentic-engineering, software-engineering, ai-infrastructure, entrepreneur]
sources: [raw/articles/2026-04-16_timdavis_probabilistic-engineering-24-7-employee.md, raw/articles/2026-09-27_timdavis_timdavis-com-homepage-and-token-curve.md, https://www.timdavis.com/, https://www.qualcomm.com/news/releases/2026/07/qualcomm-completes-acquisition-of-modular]
aliases: ["Tim Davis", "timdavis", "@tdavis"]
related: ["entities/modular", "concepts/probabilistic-engineering", "events/2026-06-24-qualcomm-acquires-modular"]
---

# Tim Davis

**Tim Davis** (X: `@tdavis`, blog: [timdavis.com](https://www.timdavis.com/)) co-founded [Modular](https://www.modular.com/) with Chris Lattner, whose mission is to create an AI hardware abstraction layer for the world. Modular was **acquired by Qualcomm in July 2026** (~$4B); Davis is now **SVP & GM of Modular at Qualcomm**. Previously he was a PM at Google, helping to create and scale AI systems inside Google Brain — infrastructure like TensorFlow, on-device AI, and large-model infrastructure. He studied Engineering, Finance and Law in Australia and the US, resides in California, and is an active angel investor in AI startups.

Within the AI-engineering community he is known as the creator of **Compound Loop**, a multi-agent system that orchestrates frontier models to autonomously write, review, and merge code, and as the author of the influential essay "Probabilistic Engineering and the 24-7 Employee" (April 2026).

## Career

### Google Brain (Product Manager)
Helped create & scale AI systems inside Google Brain: TensorFlow, on-device AI, and large-model infrastructure. Wrote about MLIR as "Open Source Infrastructure for the world" (Aug 2020) — the compiler lineage that later fed Modular.

### Modular (2022–2026, co-founder)
Co-founded [[entities/modular|Modular]] in January 2022 with Chris Lattner. Public funding arc (from his own blog posts): **$30M** seed (Jan 2022) → **$100M** "to fix AI infrastructure" (Aug 2023) → **$250M** "to scale AI's Unified Compute Layer" (Sep 2025). Products: the **Mojo** programming language and **MAX** inference platform.

### Qualcomm (July 2026–present)
Modular was acquired by Qualcomm (announced June 2026, ~$4B; completed July 2026 — see [[events/2026-06-24-qualcomm-acquires-modular]]). Davis is now SVP & GM of Modular at Qualcomm. Coverage: EE Times "Why Qualcomm Bought An Open AI Software Stack" (Jul 2026); Australian press: "Australian entrepreneur sells AI start-up Modular for $4B+" (Jun 2026); earlier profile "The Aussie conquering Silicon Valley" (Sep 2023). Press framing: "the Android moment for AI."

## Key Contributions

### Probabilistic Engineering
Davis articulated the paradigm shift from deterministic to probabilistic software engineering — the observation that as AI agents generate increasingly large portions of codebases, the confidence interval around correctness widens. His core insight: **generation has become cheap, but validation has not**. Review scales worse than generation, and past a certain throughput, correctness becomes something you _believe_ rather than _know_.

### The 24-7 Employee
Davis coined the "24-7 employee" concept — not a person working 24 hours, but a person whose agent fleet works with enormous parallelization while they sleep. He lived this through Compound Loop: setting it on real problems before bed and waking up to triage PRs that hadn't existed hours before.

### Compound Loop
A multi-agent harness that orchestrates frontier models against each other to write, review, and merge code autonomously. Features continuous log monitoring loops, self-healing test suites, and autonomous experimentation. Represents the "agentic fleet" paradigm Davis advocates.

### Role Fragmentation Analysis
Davis identified that AI-native teams are splitting, not just leveling up: top-tercile operators become architects and market thinkers with unprecedented leverage, while the middle tier becomes spec writers and agent babysitters in what he calls "the 2026 equivalent of data entry."

## Philosophy

- **Jevons Paradox applied to code**: As the unit cost of code approaches zero, we write _vastly more_ — but selection becomes the new leverage point. Direction, filtering, and coherence matter more than production.
- **Build for the model you don't have yet**: Organizations should build scaffolding now (spec writing, review culture, observability, agent fleet direction) for 2027-2028 capability jumps.
- **Know your tier**: Teams must honestly assess whether they're in the deterministic tier (formal verification, human sign-off) or probabilistic tier (ship, measure, correct), and get precise about where the boundary sits.

## Token Economics & GPU Financing Essays (2026)

Davis's post-acquisition essays apply his Engineering+Finance+Law background to AI capital markets. Shared thesis: **the binding constraints on AI are software portability and capital structure, not silicon.**

### The Token Curve (Aug 2026)
Financing terms set the cost floor for every token served; heterogeneous compute will materially reprice the long-contracted GPU market. Portability does not create heterogeneous compute — it turns existing heterogeneous capacity into supply the market can actually use. Distinguishes the **market token curve** (price of a standardized task, moved most by open-model competition) from the **portable cost curve** (break-even cost of a fixed checkpoint across the cheapest qualified hardware); "the Token Curve is the gap between what the market pays and what it costs to produce."
Key data: Google's tokens served went 9.7T/month (May 2024) → ~480T (May 2025) → 3.2 quadrillion+ (May 2026), so Alphabet's capex per million tokens served fell ~$451 → $16 → ~$5 (a ~90x fall in capex intensity) even as capex nearly quadrupled ($52.5B → $91.4B → ~$200B guided). Constant-capability price envelope anchored at GPT-4-class ~$60/M tokens (Mar 2023), falling ~10x/year.

### Every GPU loan is really a software loan (Jul 2026)
What a lender repossesses is worth far less than the silicon unless software portability lets a new operator put the cluster back to work. Three senses of portability: **workload portability** (models move across silicon at bounded cost), **operational transferability** (a qualified third party can keep a running cluster earning), and **asset liquidity** (hardware finds a new buyer at an observable price). Debt-market underwriting of AI hardware reveals the real fungibility of compute — "it's mostly software, not silicon."

## Essay Bibliography (timdavis.com)

| Date | Title | Theme |
|------|-------|-------|
| 2026-08-17 | The Token Curve | token economics, GPU repricing |
| 2026-07-26 | Every GPU loan is really a software loan | compute financeability, portability |
| 2026-04-16 | Probabilistic engineering and the 24-7 employee | [[concepts/probabilistic-engineering]] |
| 2025-10-13 | What we owe the minds we create | AI ethics |
| 2025-06-06 | Scale or Surrender: When watts determine freedom | energy constraints |
| 2023-09-26 | AI Regulation: step with care, and great tact | policy |
| 2019-10-12 | The career opportunity matrix | career strategy |

## Token Economics & GPU Financing Essays (2026)

Davis's post-acquisition essays apply his Engineering+Finance+Law background to AI capital markets. Shared thesis: **the binding constraints on AI are software portability and capital structure, not silicon.**

### The Token Curve (Aug 2026)
Financing terms set the cost floor for every token served; heterogeneous compute will materially reprice the long-contracted GPU market. Portability does not create heterogeneous compute -- it turns existing heterogeneous capacity into supply the market can actually use. Distinguishes the **market token curve** (price of a standardized task, moved most by open-model competition) from the **portable cost curve** (break-even cost of a fixed checkpoint across the cheapest qualified hardware); "the Token Curve is the gap between what the market pays and what it costs to produce."
Key data: Google's tokens served went 9.7T/month (May 2024) -> ~480T (May 2025) -> 3.2 quadrillion+ (May 2026), so Alphabet's capex per million tokens served fell ~$451 -> $16 -> ~$5 (a ~90x fall in capex intensity) even as capex nearly quadrupled ($52.5B -> $91.4B -> ~$200B guided). Constant-capability price envelope anchored at GPT-4-class ~$60/M tokens (Mar 2023), falling ~10x/year.

### Every GPU loan is really a software loan (Jul 2026)
What a lender repossesses is worth far less than the silicon unless software portability lets a new operator put the cluster back to work. Three senses of portability: **workload portability** (models move across silicon at bounded cost), **operational transferability** (a qualified third party can keep a running cluster earning), and **asset liquidity** (hardware finds a new buyer at an observable price). Debt-market underwriting of AI hardware reveals the real fungibility of compute -- "it's mostly software, not silicon."

## Essay Bibliography (timdavis.com)

| Date | Title | Theme |
|------|-------|-------|
| 2026-08-17 | The Token Curve | token economics, GPU repricing |
| 2026-07-26 | Every GPU loan is really a software loan | compute financeability, portability |
| 2026-04-16 | Probabilistic engineering and the 24-7 employee | [[concepts/probabilistic-engineering]] |
| 2025-10-13 | What we owe the minds we create | AI ethics |
| 2025-06-06 | Scale or Surrender: When watts determine freedom | energy constraints |
| 2023-09-26 | AI Regulation: step with care, and great tact | policy |
| 2019-10-12 | The career opportunity matrix | career strategy |

## Related

- [[concepts/probabilistic-engineering]] — Davis's core concept
- [[concepts/compound-engineering-loop]] — Compound Loop system
- [[concepts/agentic-engineering]] — Agent-centric engineering
- [[entities/modular]] — Modular (co-founded; now Qualcomm-owned)
- [[events/2026-06-24-qualcomm-acquires-modular]] — the acquisition
- Chris Lattner — Modular co-founder (LLVM/MLIR/Swift; see [[concepts/llvm]])
