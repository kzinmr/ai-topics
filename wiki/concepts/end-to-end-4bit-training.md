---
title: "End-to-End 4-Bit Training (Thinking Machines, Inkling 2 Small)"
created: 2026-11-15
updated: 2026-11-15
type: concept
tags: [training, quantization, inference, hardware, moe]
sources:
  - raw/articles/2026-11-13_thinkingmachines_end-to-end-4-bit-training.md
  - https://thinkingmachines.ai/blog/end-to-end-4-bit-training/
confidence: medium
---

# End-to-End 4-Bit Training

On November 13, 2026, [[entities/thinking-machines-lab|Thinking Machines Lab]] published its recipe for **end-to-end NVFP4 training** of [[concepts/inkling-2-small|Inkling 2 Small]] — the largest model known to be trained with a **native 4-bit forward pass from the start of pretraining through the final RL rollout** (no post-hoc quantization, no calibration step at delivery).

## The three-format numerical recipe

Training uses three numerical formats, chosen per stage according to the speed-vs-error tradeoff:

| Format | Bits/value | GB300 PFLOPS | Role |
|---|---|---|---|
| NVFP4 | 4.5 (4×16+8 packed /16) | 15 | Expert-layer **forward** passes (3.6× fewer bits than BF16, up to 6× faster) |
| MXFP8 | 8.25 | 5 | **Backward** passes, with re-quantization + stochastic rounding |
| BF16 | 16 | 2.5 | Non-expert layers / sensitive paths |

Hardware target: NVIDIA **Grace Blackwell Ultra (GB300)**, whose tensor cores are optimized for NVFP4 matmuls.

## Why MoE expert layers are the quantization target

- Speed matters most in high-volume steps: pretraining (trillions of tokens) and RL sampling (tens of thousands of tokens per rollout), where weight loading from global memory scales with bits stored.
- Backward passes average rounding error over large batches, but are highly sensitive to **quantization bias**, which compounds across layers, samples, and steps instead of averaging out — hence MXFP8 + **stochastic rounding** for gradients.
- MoE layers are computationally dominant and empirically tolerate quantization better than attention/dense layers. Full-NVFP4 training of *all* layers degraded compute efficiency (CE) unacceptably in early experiments.

## Technical core: the block-scaled transpose problem

NVFP4 scales each **1×16 block** by its largest value (E4M3 scale factor, unlike MX formats' E8M0-over-32). Backward passes transpose activations/weights, so each value gets grouped with 15 *different* neighbors — different scales, different quantized values, and a forward/backward mismatch that corrupts gradients. NVIDIA's answer (used in *Pretraining LLMs with NVFP4*, 2025) is 16×16 tile scaling for bitwise transpose identity, but TML found it too outlier-sensitive (one large value among 256 zeroes the rest), hurting CE.

TML's solution: only the **expectation** needs to match between passes — `E[w_q] = E[(w_q^T)^T]` — so they de-quantize forward tensors, transpose in high precision, and **re-quantize with stochastic rounding (SR)**, which rounds probabilistically in inverse proportion to distance from neighbors, preserving values in expectation. SR is hardware-accelerated on Blackwell. Final recipe: NVFP4 forwards, stochastically re-quantized **MXFP8** gradients/GEMMs. Inspiration: TetraJet-v2 (Chen et al., 2025) and Quartet II (Panferov et al., 2026).

## Results (company-reported)

- **8% wall-clock speedup in pretraining** and **20% speedup in RL** vs full MXFP8 training on the largest jobs.
- Same numerics configuration from pretraining start to final RL rollout → simpler training pipeline and no calibration when shipping a quantized checkpoint.
- A dedicated NVFP4 kernel was written for expert-layer forwards; GPU-communication quantization was added to relieve the bottleneck that emerged once compute sped up.

## Significance

- Progresses TML's 2025 MXFP8 pretraining work ("Recipes for Pre-training LLMs with MXFP8", Mishra et al.) one precision notch down, matching the [[concepts/nvfp4-4bit-floating-point|NVFP4]] format NVIDIA has pushed for inference (see [[events/2026-10-30-nvidia-deepseek-v4.1-flash-nvfp4]]).
- Collapses the train/inference precision gap: if the model trains natively in FP4, the deployment quantization step disappears — relevant to [[concepts/model-quantization]] and [[concepts/inference/vllm|vLLM serving economics]].
- Counterpoint to the "compute gets 10x more expensive" thesis: precision reduction is a compute-multiplier of the kind Tom Brown's "physical × multipliers" framing predicts (see [[events/anthropic-ipo-roadshow-2026]]).

## Related

- [[concepts/inkling-2-small]] — the model trained with this recipe
- [[concepts/nvfp4-4bit-floating-point]] — the NVFP4 format itself
- [[concepts/mixture-of-experts]] — why MoE layers absorb low precision
- [[concepts/post-training/quantization-overview]] — quantization beyond training time
- [[concepts/distributed-training]] — communication-quantization bottleneck
