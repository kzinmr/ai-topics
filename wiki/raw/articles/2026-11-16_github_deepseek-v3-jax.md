---
title: "DeepSeek-V3 in ~200 lines of pure JAX (Show HN + README)"
source: https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax
collected: 2026-11-16
hn_item: https://news.ycombinator.com/item?id=50497589
sha256: 74e51aab04b35d57893f046cc6fd3f8036e70e4ccad442db7ed4902563ec59cc
---

# Show HN: DeepSeek V3 in ~200 lines of pure Jax

Vaibhaav Tiwari, Show HN 2026-11-15 (273 points / 29 comments,
https://news.ycombinator.com/item?id=50497589). Per the repo tagline: "DeepSeek V3 (MLA,
DeepSeekMoE, aux-loss-free balancing, MTP) in 190 lines of pure JAX, trained on a MacBook Air."
Write-up: vaibhaav.in/writing/deepseek-v3-jax. The implementation covers the four signature
DeepSeek-V3 mechanisms — Multi-head Latent Attention (MLA), DeepSeekMoE sparse experts,
auxiliary-loss-free load balancing, and Multi-Token Prediction (MTP) — in a single ~190-line JAX
file, and the author reports completing training on a MacBook Air.

Positioning alongside this wiki's other from-scratch reference implementations:
[[concepts/flashattention-pytorch-educational]], [[concepts/flashattention-pytorch-educational-implementation]],
and the [[concepts/ai-benchmarks/nanogpt-speedrun]] lineage. The canonical DeepSeek-V3 architecture
description lives at [[concepts/deepseek-v3]].

## HN thread

Top comments (item 50497589) focused on correctness of the MLA implementation vs the paper, whether
the 200-line count includes the training loop, and comparisons to the PyTorch nanogpt-style
teaching repos. (See the Show HN thread for the full discussion.)
