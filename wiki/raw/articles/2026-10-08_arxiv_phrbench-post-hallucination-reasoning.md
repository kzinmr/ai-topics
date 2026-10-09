---
source_url: https://arxiv.org/abs/2610.10455
ingested: 2026-10-08
sha256: ae83694942c9dd015f58cc64aaeca72d27f4fed1e6e2d214edae71c091885c15
---

# PHRBench: A Behavioral Evaluation of Post-Hallucination Reasoning in LLMs

- **arXiv:** arXiv:2610.10455
- **Authors:** Linghao Meng, Feng He, Xuan Yang, Junyuan Mao, Pinze Ren, Deqing Mu, et al.
- **Published:** 2026-10-07
- **Source URL:** https://arxiv.org/abs/2610.10455

## Abstract

Hallucinated information can propagate through multi-stage LLM systems and become part of the context for subsequent reasoning. Existing studies of post-hallucination reasoning (PHR) mainly characterize changes in final outcomes and aggregate reasoning dynamics, leaving how models resolve hallucinated premises at the response level insufficiently understood. In this work, we introduce PHRBench, a controlled benchmark for behaviorally structured PHR across four domains and 18 large language models. PHRBench characterizes each reasoning trajectory independently of final-answer correctness through Hallucination Compliance, Hallucination Avoidance, and Heuristic Correction, and defines an insightful trajectory as successful correction that ultimately reaches the correct answer. Across 4820 controlled instances, we find that successful recovery remains relatively rare and is associated with more frequent belief updates along the reasoning trajectory. We further find that properties of the hallucinated prompt contain substantial predictive signal for successful recovery, with a lightweight predictor achieving an AUROC of 0.847. These findings provide a behavioral view of post-hallucination reasoning, characterizing how LLMs resolve erroneous context and when successful recovery is likely to occur.
