---
title: "Mixture-of-Experts"
type: concept
aliases:
  - mixture-of-experts
created: 2026-04-25
updated: 2026-09-11
tags:
  - concept
  - training
  - fused-kernels
sources:
  - raw/articles/2026-05-10_cursor_kernels.md
  - raw/articles/gilesthomas.com--2026-09-gpt-2-to-moe--d0033616.md

---

# Mixture-of-Experts

> **TODO**: Enrich this page.

## Overview

Stub page for Mixture-of-Experts.

## Kernel-Level Optimization (2025)

Training-infrastructure work shows MoE layers are the primary target for low-precision kernel optimization. Cursor's MXFP8 rebuild (Aug 2025) — the MoE layer was 53% of forward-pass time — achieved a **3.5x MoE layer speedup** on Blackwell via block-scaled MXFP8 grouped GEMM, expert-wise L2 supergrouping, and a 6.2+ TB/s quantization kernel, outperforming DeepSeek's DeepGEMM for grouped Fprop/Dgrad/Wgrad workloads. See [[entities/cursor-ai|Training Infrastructure: MXFP8 MoE Kernels]].

## Single-GPU MoE From-Scratch Replication (Giles Thomas, Sep 2026)

Giles Thomas (author of the *Writing an LLM from scratch* series) ported his fine-tuned GPT-2 Small into a sparse MoE and trained it on a single RTX 3090 — a rare end-to-end record of MoE behavior at hobbyist scale. Series: https://gilesthomas.com/writing/llms/gpt-2-to-moe

**Architecture**: 6 layers, each dense FFN split into 8 equal experts (hidden 768→3072), top-1 routing → ~8× total parameters, but active params per token still ≈ GPT-2 Small's 124M (final model 6% denser than GPT-2 Medium). Trained on TinyStories, 2 days at 12.5k tok/s (6× slower than the dense baseline).

**Load balancing**: aux-loss coefficient α=0 → 7 of 8 experts collapsed to zero usage (one dominant expert absorbed everything). α=0.005 minimized both training and auxiliary loss (6.106 / 25.21); every expert got some traffic, but one remained dominant — **router collapse persisted even at the best-known coefficient**.

**Continued pretraining (5.44B tokens, loss 6.088)**:
- MoE beat fine-tuned GPT-2 Small (epoch 20, loss 6.604) — but **lost to dense GPT-2 Medium** (6.039, reached with 2.5B tokens / 3× less wall time).
- Suspected cause of the Medium gap: MoE was initialized from the *overtrained* GPT-2 Small (1333 epochs), whose degraded weights dragged it down (cf. [[concepts/data-repetition-in-training]], [[concepts/scaling-laws]]).

**SFT / reasoning**: DART-adapted (7400/5200 rows) → **GSM8K 25.6% vs GPT-2 Small's 19.9% (+29% relative)**; MMLU flat (25.56 vs 24.87, ≈ random baseline). MoE lifted math reasoning without lifting broad knowledge.

**Router interpretability probe**: per-token expert-choice sequences embedded → UMAP, colored by GSM8K category. Smooth map, weak clusters — **no strong evidence of expert specialization by reasoning type at 154M scale**. 1B-scale rerun (multi-node) planned.

**Scaling walls documented**: TinyStories (~500M unique tokens) exhausted at 5.44B tokens — the data wall, not compute, binds at this scale; a 1B MoE (GPT-2 Large equivalent) requires multi-node.

^[raw/articles/gilesthomas.com--2026-09-gpt-2-to-moe--d0033616.md]

## Related Pages

- [[entities/_index]]
- [[entities/noumena-network]] — Noumena Network (nmoe, RDEP)
- [[concepts/moe-training-noumena-methodology]] — MoE training methodology synthesis
- [[concepts/rdep]] — RDEP expert parallelism
- [[entities/deepseek]] — DeepSeek (major MoE practitioner)
- [[concepts/moe-train-inference-mismatch]] — aux-loss tradeoffs, DeepSeek's aux-loss-free load balancing
- [[concepts/scaling-laws]] — Chinchilla re-evaluation (same author, same GPU: the 3.2B-token run was Chinchilla-optimal for 163M, not 446M)
- [[concepts/data-repetition-in-training]] — TinyStories data wall at 5.44B tokens
