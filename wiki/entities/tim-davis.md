---
title: "Tim Davis"
created: 2026-05-11
updated: 2026-05-11
type: entity
tags: [person, agentic-engineering, software-engineering]
sources: [raw/articles/2026-04-16_timdavis_probabilistic-engineering-24-7-employee.md]
aliases: ["Tim Davis", "timdavis"]
---

# Tim Davis

Tim Davis is a software engineering leader at [Modular](https://www.modular.com/), where he runs the company's operations. He is the creator of **Compound Loop**, a multi-agent system that orchestrates frontier models to autonomously write, review, and merge code, and the author of the influential essay "Probabilistic Engineering and the 24-7 Employee" (April 2026).

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

## Related

- [[concepts/probabilistic-engineering]] — Davis's core concept
- [[concepts/compound-engineering-loop]] — Compound Loop system
- [[concepts/agentic-engineering]] — Agent-centric engineering
- [[entities/modular]] — Modular (employer)
