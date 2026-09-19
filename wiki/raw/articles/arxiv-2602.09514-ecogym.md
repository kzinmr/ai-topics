---
source_url: https://arxiv.org/abs/2602.09514
ingested: 2026-09-19
sha256: 431f7429b5fc0c4d531b232659bb3a474b2d41f3c2938589d3b6aca813bf8f20
---

# EcoGym: Evaluating LLMs for Long-Horizon Plan-and-Execute in Interactive Economies

**arXiv**: https://arxiv.org/abs/2602.09514 | **Published**: 2026-02-10

**Authors**: Xavier Hu, Jinxiang Xia, Shengze Xu, Kangqi Song, Yishuo Yuan, Guibin Zhang, JinCheng Ren, Boyu Feng et al.

## Abstract

Long-horizon planning is widely recognized as a core capability of autonomous LLM-based agents; however, current evaluation frameworks suffer from being largely episodic, domain-specific, or insufficiently grounded in persistent economic dynamics. We introduce EcoGym, a generalizable benchmark for continuous plan-and-execute decision making in interactive economies. EcoGym comprises three diverse environments: Vending (adapted from the closed-source Vending-Bench, with full open-source release), Freelance (new), and Operation (new), implemented in a unified decision-making process with standardized interfaces, and budgeted actions over an effectively unbounded horizon (1000+ steps if 365 day-loops for evaluation). The evaluation of EcoGym is based on business-relevant outcomes (e.g., net worth, income, and DAU), targeting long-term strategic coherence and robustness under partial observability and stochasticity. Experiments across eleven leading LLMs expose a systematic tension: no single model dominates across all three scenarios. Critically, we find that models exhibit significant suboptimality in either high-level strategies or efficient actions executions. EcoGym is released as an open, extensible testbed for transparent long-horizon agent evaluation and for studying controllability utility trade-offs in economic settings.
