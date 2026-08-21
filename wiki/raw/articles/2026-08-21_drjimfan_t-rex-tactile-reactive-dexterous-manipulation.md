---
type: x_post
source: https://x.com/drjimfan/status/2090832822525403481
author: "@drjimfan"
date: 2026-08-21
tags: [robotics, embodied-ai, tactile, dexterous-manipulation, vla, nvidia, uc-berkeley]
related: [entities/jim-fan, concepts/robotics, concepts/embodied-ai]
---

# T-Rex: Tactile-Reactive Dexterous Manipulation — @drjimfan tweet

**Tweet (2026-08-21):** "T-Rex: Tactile-Reactive Dexterous Manipulation. Website: https://tactile-reactive-dexterous.github.io/ Open dataset: https://huggingface.co/datasets/zekaiwang/trex_dataset. This work is led by @Dantong_Niu and co-advised by @trevordarrell. Congrats to the team!"

Jim Fan (NVIDIA GEAR Lab) announcing T-Rex, a tactile-reactive dexterous manipulation framework from UC Berkeley + NVIDIA (also Stanford, Panasonic, La Sapienza/ItalAI). Led by Dantong Niu, co-advised by Trevor Darrell; Jim Fan is a co-author.

## Key facts (from project page)

- **Problem:** learning-based Vision-Language-Action (VLA) models for robotic manipulation either ignore the tactile modality or use encoders capturing only *static* cues. Three obstacles: scarce diverse training data + standardized eval, VLA architectural constraints, and static tactile encoders.
- **T-Rex Dataset:** open-source, **100-hour** tactile-synchronized teleoperation corpus for mid-training. Data-efficient recipe prioritizing broad coverage of *elementary motor primitives*. Pairs **207 household objects × 22 motor primitives** → 502 feasible combinations, ~17 demos each. Collected on a bimanual **Dexmate Vega-1** (two 7-DoF arms + two 22-DoF Sharpa Wave dexterous hands, five fingertip tactile sensors per hand). 30 Hz time-aligned bundle: 3 RGB streams + bimanual proprioception + SE(3) wrist poses + per-fingertip tactile.
- **Model — variable-rate Mixture-of-Transformer (MoT):** splits control into a **low-rate action expert** + a **high-rate tactile expert** that provides reactive residual refinements.
- **Temporal tactile VQ-VAE encoder:** compresses high-frequency touch into compact, drift-robust tokens of temporal force/contact patterns.
- **Training recipe:** three-stage — human egocentric pre-training → tactile-rich mid-training → lightweight fine-tuning. First complete recipe for tactile dexterous manipulation.
- **Results:** 12-task real-world benchmark on a 58-DoF bimanual dexterous robot (force control, deformation, bimanual coordination). SOTA — **>30% higher average success rate** than the strongest baseline.

## Sources
- Tweet: https://x.com/drjimfan/status/2090832822525403481
- Project page: https://tactile-reactive-dexterous.github.io/
- Dataset: https://huggingface.co/datasets/zekaiwang/trex_dataset
