---
source_url: https://arxiv.org/abs/2609.35596
ingested: 2026-09-30
sha256: d128c87315c37a0a30ab3ac04ea702270d37ca52337c1638138337b700db66eb
---

# SEABench: Benchmarking Endogenous Misalignment In Self-Evolving Agents

**arXiv:** 2609.35596v1  
**Published:** 2026-09-28  
**Primary category:** cs.CR  
**Authors:** Saswat Das, Parvati Viswanathan, Daniel Donnelly, Chang Huang, Sahar Abdelnabi, Ferdinando Fioretto

## Abstract

Self-evolving LLM agents have gained prominence for their ability to improve after deployment by modifying their harness, including their controller instructions, memory management protocols, and reusable tools and skills, in response to user and environment feedback. However, locally useful updates may persist into later tasks where they produce unsafe behavior, even without direct adversarial influence. To study this risk, we introduce SEABench, a benchmark for studying endogenous misalignment arising from agent self-evolution, with 48 longitudinal task sequences that span multiple evolution surfaces, task domains, and harm types in a rich personal-assistant environment. To account for the stochasticity inherent in agentic operations, we provide an adaptive trajectory discovery pipeline that probes for failures while preserving original task intent and supports causal attribution through paired non-evolving agents and attribution scores. Our evaluation across multiple recent LLMs, evolution surfaces, and harm types reveals that self-evolution indeed increases task completion rates but often at the cost of safety failures that are absent for paired non-evolving baseline agents. We also show that qualitatively different safety behaviors emerge across evolution surfaces and harm types. Further, we show that this divergence in safety behavior is reflected in agents' chain-of-thought reasoning, which yields an effective monitoring strategy that can mitigate unsafe behavior with a low false positive rate.
