# STRIDE: Learnable Stepwise Language Feedback for LLM Reasoning

**Source**: https://arxiv.org/html/2605.18851v1
**Date**: May 21, 2026
**Authors**: Junjie Zhang, Guozheng Ma, Shunyu Liu, Zetian Hu, Yongcheng Jing, Ting-En Lin, Yongbin Li, Dacheng Tao
**Affiliations**: Nanyang Technological University, Alibaba Group

## Abstract

STRIDE (language-driven STepwise tRajectory rEDIrection) shifts process supervision from scalar rewards to learnable stepwise language feedback. Co-trains a generator and generative verifier using only outcome-based rewards, eliminating external annotations while delivering sustained policy improvement through jointly aligned verifier training.

## Key Innovation
The verifier's stepwise language critiques explicitly localize and explain failures, enabling the generator to redirect reasoning trajectories at intermediate steps toward alternative decisions. The trajectory redirection design guarantees harmless policy improvement even under noisy or suboptimal verifier feedback.

## Comparison to Existing Methods

| Method | Policy update | Language feedback | Learnable verifier | RL-based training |
|--------|---------------|-------------------|-------------------|-------------------|
| Outcome-based RL | Yes | No | No | Yes |
| Critique-based RL | Yes | Yes (frozen/self) | No | Yes |
| SFT Error-Corrective | Yes (SFT) | Yes (SFT) | No | No |
| TANGO (Co-training w/ Scalar) | Yes | No (scalar) | Yes | Yes |
| **STRIDE** | **Yes** | **Yes (co-trained)** | **Yes** | **Yes** |

STRIDE is the only method satisfying all four properties simultaneously.

## Architecture
- Three-phase interleaved co-training schedule
- Multi-Point Redirection uses verified prefix steps to constrain exploration
- Phase III is only 1/13 of total training schedule but yields decisive gains on previously unsolvable problems

## Results
- Significantly outperforms state-of-the-art baselines on diverse reasoning benchmarks
- Achieves breakthroughs on zero-pass-rate problems where scalar methods yield no learning signal
