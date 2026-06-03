---
title: "ar0cket1"
type: entity
created: 2026-06-03
updated: 2026-06-03
tags:
  - person
  - pseudonymous
  - ai-researcher
  - researcher
  - training
  - reasoning
aliases:
  - ar0cket1
  - "@ar0cket1"
sources:
  - raw/articles/2026-05-12_ar0cket1_on-policy-self-distillation.md
  - https://x.com/ar0cket1
  - https://x.com/i/article/2054081238236020736
---

# ar0cket1 (@ar0cket1)

**ar0cket1** is a pseudonymous AI/ML researcher on X/Twitter focusing on **post-training optimization**, specifically On-Policy Self-Distillation (OPSD) and evolutionary prompt engineering. Their work involves hands-on experimentation with training techniques, running multi-hour compute jobs on RTX 6000 Pro GPUs to empirically characterize OPSD behavior and optimize hint-generation strategies.

## Research Focus

### OPSD (On-Policy Self-Distillation)

ar0cket1 conducted extensive token-level analysis of OPSD vs OPD behavior on Olmo 3 7B using math data from Nemotron Math v2. Key contributions:

- **KL Divergence Profiling**: Documented that OPSD has significantly higher max KL (13.249 vs OPD's 3.736), more frequent KL shocks, and disproportionate impact on low-entropy tokens
- **Positive Pressure Asymmetry**: Discovered that OPSD down-weights student-chosen tokens 83% of the time vs OPD's 80% up-weight — a stubborn bias that resisted 40+ hand-written hint variations
- **Token-Level Behavioral Mapping**: Characterized which tokens OPSD and OPD affect — OPD rewards productive search (invariants, rephrasing), while OPSD drives search toward hint suggestions and resurrects skipped paths
- **Continual Learning Economics**: Modeled the cost of OPSD-based continual learning at frontier scale ($10M for 1.55T effective RL-equivalent tokens)

### GEPA-Based Hint Optimization

Applied [[concepts/gepa|GEPA]] (Genetic-Pareto Prompt Evolution) to OPSD hint optimization:
- 20+ hours of optimization on RTX 6000 Pro
- Achieved KL shock reduction to ~1/2 of naive OPSD with 2× mean KL
- Discovered that general hint generation prompts outperform per-problem optimized hints
- Found that OPSD's negative bias appears inherent — even 40 rounds of greedy GEPA mutation couldn't reverse it

## Notable Works

- [**On Policy Self Distillation**](https://x.com/i/article/2054081238236020736) (May 12, 2026) — X Article analyzing OPSD experimental results, KL geometry, hint optimization via GEPA, and the economics of continual learning. 216 bookmarks, 114 likes, ~41K impressions.

## Writing Style & Philosophy

ar0cket1 communicates in a first-person, transparent style — openly sharing experimental results, admitting when approaches fail, and explicitly asking for compute assistance. Their work emphasizes **empirical grounding** (real experiments on real hardware) and **candid assessment of limitations** (noting that the analysis is limited without full training runs).

## Cross-References

- [[concepts/on-policy-self-distillation]] — OPSD: the core technique being analyzed and optimized
- [[concepts/gepa]] — GEPA: the evolutionary algorithm used for hint optimization
- [[entities/will-brown]] — Will Brown (@willccbb): credited for inspiration and suggesting GEPA
- [[entities/nrehiew]] — wh (@nrehiew_): credited for articles and insight
- [[concepts/on-policy-distillation]] — OPD: the baseline compared against
- [[concepts/sdar-self-distilled-agentic-rl]] — SDAR: downstream application of OPSD for agent training

## References

- Raw article: `raw/articles/2026-05-12_ar0cket1_on-policy-self-distillation.md`
