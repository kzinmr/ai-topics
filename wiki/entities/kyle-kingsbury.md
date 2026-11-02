---
title: "Kyle Kingsbury"
type: entity
aliases: [jepsen, aphyr]
created: 2026-11-02
updated: 2026-11-02
tags:
  - person
  - distributed-systems
  - ai-skeptic
  - developer-tooling
sources:
  - raw/articles/simonwillison.net--2026-nov-1-kyle-kingsbury--e4fc43e0.md
---

# Kyle Kingsbury

**Known for:** Creator and maintainer of **Jepsen** — the open-source framework for fault-injection testing of distributed databases (network partitions, clock skew, process crashes) that has repeatedly exposed data-loss and correctness bugs in mainstream systems: Redis losing 56% of writes during a partition, MongoDB "dropping a phenomenal amount of data," RabbitMQ ~35% acknowledged-write loss, Elasticsearch reporting green during split-brain. His reports routinely force vendors to change methodology and have made independent adversarial verification the reference standard for distributed-systems claims (catalogued in [[entities/dan-luu]]'s "Measurement, benchmarking, and data analysis are underrated," which holds up Jepsen as the canonical high-ROI measurement project).

Blog: [[https://aphyr.dev|aphyr.dev]] · X: @aphyr

## LLM-Era Documentation Trust Collapse (November 2026)

In a widely-amplified passage from "Jepsen results for ParticleDB 1.1.4" (quoted by [[entities/simon-willison]] on Nov 1, 2026), Kingsbury extends the Jepsen ethos — *never trust a system's claims about itself; test its failure behavior* — to the software ecosystem as poisoned by LLM generation:

> "More broadly, the use of LLMs erodes trust in documentation, in software, and in the organizations which produce them. Perhaps engineers will begin to treat any new software project with suspicion—**the signals we used to rely on as markers of a mature system are now easier to counterfeit.** [...] In the age of LLMs, what can maintainers do to ensure correct software and accurate documentation? Having done that work, how can they demonstrate its quality to users?"

The argument parallels the trust-erosion observations in [[concepts/ai-slop]] (Sean Goedecke's "workslop" effort-asymmetry, Simon Willison's evaluation-first doctrine), but Kingsbury's angle is distinct: the problem is **counterfeitability of provenance signals** (star counts, polish, docs coverage, release cadence), not slop quality. The open question he poses — how maintainers can *demonstrate* verified quality when verification signals are forgeable — maps directly onto distributed-systems practice: adversarial fault-injection testing (the Jepsen pattern) as a candidate answer for documentation/software claims, analogous to how independent benchmark suites counter lab self-reporting ([[concepts/ai-benchmarks]]).

## Context

- **Jepsen**: https://jepsen.io — the framework, and Kingsbury's consultancy running contract audits (e.g., ParticleDB, whose 1.1.4 round produced the above quote).
- Prior wiki footprint before Nov 2026: a single mention in [[entities/dan-luu]] (Jepsen as measurement exemplar). This page created from the Nov 1 quote-post; future Jepsen reports and LLM-era commentary should be filed here.

## References

- [A quote from Kyle Kingsbury — simonwillison.net](https://simonwillison.net/2026/Nov/1/kyle-kingsbury/)
- [Jepsen results for ParticleDB 1.1.4 — original](https://aphyr.dev/)
