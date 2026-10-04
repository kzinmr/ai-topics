---
source_url: https://arxiv.org/abs/2610.01508
ingested: 2026-10-04
sha256: 0fa4022aa4628744536f298fe4de5468b6b14b3ed60f67e79ecbe377bc02d388
---

# OverAct: Measuring and Mitigating Proactive Over-Authorization in LLM Tool-Calling Agents

Authors: Taolin Zhang, Jiuheng Wan, Hanyu Wang, Tingyuan Hu, Chengyu Wang.
arXiv:2610.01508, submitted 2026-10-01.

## Abstract
LLM agents with tool-calling capabilities can access external services and private user data, but they may retrieve more information than a user's request explicitly requires. We study this behavior in structured tool-calling agents and term it proactive over-authorization. This setting differs from filesystem-level coding agents because the main risk is unnecessary access to private data. We introduce OverAct, a controlled benchmark spanning eight privacy-sensitive domains with deterministic, judge-free scoring, together with an interpretive decision-theoretic framework that yields three testable predictions. Across seven models from four families, all models significantly exceed authorized scope. Request specificity is the strongest predictor of severity, over-authorization grows sublinearly with tool-pool size, and decoding temperature has little effect. These patterns are consistent with a cost-asymmetry account, suggesting that over-authorization arises more from structural decision tendencies than from decoding randomness. We also propose SelfAudit, a zero-shot inference-time method that generates request-grounded justifications and filters unjustified calls before execution. Ablation shows that explicit filtering is the main driver of scope reduction. SelfAudit reduces privacy-oriented excess by 43% without oracle knowledge.
