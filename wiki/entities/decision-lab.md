---
title: Decision Lab
created: 2026-06-01
updated: 2026-06-01
type: entity
tags:
  - company
  - open-source
  - data-science
  - bayesian
  - ai-agents
sources:
  - raw/newsletters/2026-06-01-the-agentic-data-science-research-lab.md
---

# Decision Lab

**Decision Lab** is an open-source tool for causal and Bayesian analysis built by [[entities/thomas-wiecki|PyMC Labs]]. It enforces a **"garden of forking paths"** architecture for robust, principled data analysis — systematically exploring multiple analytical paths to avoid confirmation bias and p-hacking.

## Overview

Decision Lab addresses a core challenge in data science: given the same dataset, different analysts can reach different conclusions depending on arbitrary choices in data cleaning, model specification, and analysis strategy. Decision Lab makes these forking paths explicit, systematic, and auditable.

## Garden of Forking Paths Architecture

The "garden of forking paths" is a structured approach where:

- Every analytical decision point is tracked as a branching path
- Multiple plausible analyses are run in parallel
- Results are aggregated across all paths to assess robustness
- Sensitivity to analytical choices is quantified rather than hidden
- Bayesian methods provide principled uncertainty quantification across forks

This approach is inspired by Gelman & Loken's (2013) work on the garden of forking paths and the replication crisis in science. Decision Lab operationalizes the solution via automated causal/Bayesian workflows.

## Relationship to Agentic Data Science

Decision Lab fits into the broader [[concepts/agentic-data-science|agentic data science]] stack as an orchestrated analysis engine — AI agents can spawn multiple Decision Lab analyses in parallel as part of a larger research workflow, with the garden of forking paths providing natural verification and robustness checking.

## Related Concepts

- [[concepts/agentic-data-science]] — The broader paradigm of AI agents doing data science work
- [[concepts/bayesian-methods]] — Bayesian statistical approaches
- [[concepts/causal-reasoning]] — Causal inference frameworks

## Related Entities

- [[entities/thomas-wiecki]] — CEO of PyMC Labs, creator
- [[entities/decision-lens]] — Agentic dashboard companion for stakeholder interaction
- [[entities/pymc-labs]] — The Bayesian consulting firm behind Decision Lab

## Links

- [PyMC Labs](https://www.pymc-labs.com) — Bayesian consulting firm
- [PyMC](https://www.pymc.io) — Probabilistic programming framework
