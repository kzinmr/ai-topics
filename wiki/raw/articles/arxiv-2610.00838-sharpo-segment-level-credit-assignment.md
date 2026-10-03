---
source_url: https://arxiv.org/abs/2610.00838
arxiv_id: 2610.00838
ingested: 2026-10-03
sha256: 2a57748e6d395c323d2c7db97295a754b9a86b007b30b4961941a188ed5e8f16
---

# SHARPO: Segment-Level Credit Assignment for Agentic Reinforcement Learning

**arXiv:** 2610.00838  |  **Submitted:** 2026-09-30
**Authors:** Xinchen Du, Zhengze Zhou, Wenhui Zhu, Han Yu, Sen Na, Rohit Jain, Alborz Geramifard
**URL:** https://arxiv.org/abs/2610.00838

## Abstract

Agentic reinforcement learning (RL) trains a large language model (LLM) to act over long, multi-step interactions. However, a single localized error can cause task failure, while trajectory-level rewards provide limited guidance for assigning credit to individual decisions. To address this limitation, we introduce Segment-level Hindsight Advantage Reweighting for Policy Optimization (SHARPO), a credit-assignment mechanism that refines Group Relative Policy Optimization (GRPO) at the level of environment-facing segments. Inspired by the existing on-policy self-distillation (OPSD) method, SHARPO computes teacher-student log-probability gaps within each segment and uses the resulting signal to compute a bounded multiplier on the GRPO advantage. This multiplier is shared by all tokens within the segment, allowing credit to vary across different segments. With Qwen2.5-7B-Instruct, SHARPO outperforms existing baselines on the ALFWorld and WebShop benchmarks, including GRPO, SDAR, RLSD, and StepOPSD.
