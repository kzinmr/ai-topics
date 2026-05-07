---
title: "Byte Latent Transformer: Patches Scale Better Than Tokens"
authors: Artidoro Pagnoni, Ram Pasunuru, Pedro Rodriguez, John Nguyen, Benjamin Muller, Margaret Li, Chunting Zhou, Lili Yu, Jason Weston, Luke Zettlemoyer, Gargi Ghosh, Mike Lewis, Ari Holtzman, Srinivasan Iyer
source: arXiv / ACL 2025
url: https://arxiv.org/abs/2412.09871
published: 2024-12-13
venue: ACL 2025
type: paper
tags:
  - blt
  - byte-level
  - tokenization-free
  - scaling
  - meta
  - architecture
  - post-pretraining
---

# Byte Latent Transformer: Patches Scale Better Than Tokens

## Core Innovation: Entropy-Based Patching

BLT eliminates traditional tokenization and operates directly on raw bytes, grouping them into **dynamically sized patches** based on the entropy of the next byte. Complex regions get fine patches, simple regions get coarse patches.

## Architecture

1. **Byte Encoder** — small high-frequency module converting raw bytes to initial representations
2. **Latent Transformer** — bulk of parameters, processes dynamically formed patches
3. **Byte Decoder** — converts latent representations back to byte-level predictions

## Key Findings

- First byte-level model to match tokenization-based LLM performance at scale (up to 8B params, 4T training bytes)
- **50% fewer inference FLOPs** by using long patches for predictable text
- Unlocks new scaling dimension: growing both patch size and model size simultaneously
- Inherently robust to character-level noise (typos, formatting shifts)
- Shows improvements in reasoning tasks and long-tail generalization

## Connection to Scaling Hypothesis

BLT validates Daniel Han's "Approach #3" — editing the scaling law definition. By changing what "tokens" means, BLT demonstrates that the tokenization bottleneck can be eliminated at scale, offering a new axis for scaling beyond token-based architectures.

See: [[concepts/scaling-hypothesis#Byte Latent Transformer (Meta, ACL 2025)]]
