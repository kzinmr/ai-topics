---
title: "Mixture-of-Experts"
type: concept
aliases:
  - mixture-of-experts
created: 2026-04-25
updated: 2026-08-16
tags:
  - concept
  - training
  - fused-kernels
sources:
  - raw/articles/2026-05-10_cursor_kernels.md

---

# Mixture-of-Experts

> **TODO**: Enrich this page.

## Overview

Stub page for Mixture-of-Experts.

## Kernel-Level Optimization (2025)

Training-infrastructure work shows MoE layers are the primary target for low-precision kernel optimization. Cursor's MXFP8 rebuild (Aug 2025) — the MoE layer was 53% of forward-pass time — achieved a **3.5x MoE layer speedup** on Blackwell via block-scaled MXFP8 grouped GEMM, expert-wise L2 supergrouping, and a 6.2+ TB/s quantization kernel, outperforming DeepSeek's DeepGEMM for grouped Fprop/Dgrad/Wgrad workloads. See [[entities/cursor-ai|Training Infrastructure: MXFP8 MoE Kernels]].

## Related Pages

- [[entities/_index]]
- [[entities/noumena-network]] — Noumena Network (nmoe, RDEP)
- [[concepts/moe-training-noumena-methodology]] — MoE training methodology synthesis
- [[concepts/rdep]] — RDEP expert parallelism
- [[entities/deepseek]] — DeepSeek (major MoE practitioner)
