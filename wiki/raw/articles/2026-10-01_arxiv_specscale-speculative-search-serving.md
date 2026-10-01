---
source_url: https://arxiv.org/abs/2609.39334
arxiv_id: 2609.39334
ingested: 2026-10-01
sha256: 90ecd6eceac6d5ae040aa86bbfc94030967540f5b221d75ce8f8d9621bd11005
---

# Taming Speculative Search for Test-Time Scaling in LLM Serving (SpecScale)

arXiv:2609.39334v1 (cs.DC, cs.CL, cs.OS), submitted 2026-09-30.
Authors: Jinwoo Jeong, Woohyung Choi, Myeongjae Jeon, Jeongseob Ahn.

## Abstract

Test-time scaling has recently emerged as a powerful approach for improving LLM reasoning by allocating additional computation during inference, substantially enhancing accuracy on challenging tasks such as mathematics and coding. To accelerate the exploration of reasoning paths, recent studies proposed speculative execution. However, we show that supporting speculative execution poses two unique challenges for LLM serving systems: (1) an explosion in the search space of candidate paths and (2) frequent, fine-grained verification tasks for candidates.

To address these challenges, this paper proposes SpecScale, a serving system for efficient speculative execution. We introduce three techniques to reconcile the trade-off between latency and computational overhead: (1) early pruning of low-quality candidate paths, (2) deduplicating computation across redundant candidate paths, and (3) deferring fine-grained verification tasks.

We evaluate SpecScale on challenging reasoning benchmarks, including MATH and Olympiad. Our results show that SpecScale significantly outperforms both non-speculative and recent speculative approaches, delivering substantial improvements in throughput and latency while preserving answer quality.
