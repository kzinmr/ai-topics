---
title: "A Visual Guide to Mamba and State Space Models"
source: newsletter.maartengrootendorst.com
author: Maarten Grootendorst
url: https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mamba-and-state
date: 2024
tags: [mamba, ssm, state-space-model, tutorial, visualization]
---

# A Visual Guide to Mamba and State Space Models

Maarten Grootendorst's visual walkthrough of the Mamba architecture, explaining State Space Models from first principles through to Mamba's selective scan algorithm (S6).

## Structure

- **Part 1**: The Problem with Transformers (O(L²) inference scaling)
- **Part 2**: The State Space Model (continuous SSM equations, discretization, three representations, HiPPO)
- **Part 3**: Mamba — A Selective SSM (S6 algorithm, hardware-aware implementation, Mamba block architecture)

## Key Takeaways

- SSMs have three equivalent representations: continuous (theory), recurrent (inference, O(L)), convolutional (training, parallel)
- HiPPO initialization of Matrix A prevents forgetting in long sequences
- Mamba's key innovation: making B, C, and Δ input-dependent (selective) enables content-aware filtering
- The selective scan (S6) uses a parallel associative scan instead of convolution, since parameters are dynamic

Cited as a 🟢 top-tier resource in the [[concepts/genai-handbook|GenAI Handbook]] (Section VII: Sub-Quadratic Context Scaling). Full analysis in [[concepts/ssm-mamba]].
