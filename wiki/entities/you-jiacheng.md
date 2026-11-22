---
title: "You Jiacheng (YouJiacheng)"
type: entity
created: 2026-11-22
updated: 2026-11-22
tags:
  - person
  - nanogpt-speedrun
  - open-source
  - optimization
aliases:
  - '@YouJiacheng'
  - You Jiacheng
sources:
  - https://github.com/YouJiacheng
  - https://github.com/KellerJordan/modded-nanogpt
---

# You Jiacheng (`@YouJiacheng`)

| | |
|---|---|
| **GitHub** | [YouJiacheng](https://github.com/YouJiacheng) |
| **Bio** | IIIS, Tsinghua University. |
| **Blog** | — |
| **Location** | Beijing, China |
| **Known for** | nanoGPT speedrun record contributions; Muon optimizer co-authorship |

> Created by the skeleton-enrichment run (2026-11-22) from GitHub API + modded-nanogpt
> README records. Sparse profile — enrichment deliberately conservative, no fabrication.

## nanoGPT speedrun contributions

You Jiacheng is credited in the official [modded-nanogpt](https://github.com/KellerJordan/modded-nanogpt)
record table (train a 124M GPT-2 to 3.28 val loss on FineWeb, 8xH100):

| Record | Time | Change | Date | Credits |
|--------|------|--------|------|---------|
| #15 | 3.95 min | U-net pattern value embeddings | 2024-12-08 | @leloykun, @YouJiacheng |
| #16 | 3.80 min | Split value embeddings, block sliding window | 2024-12-10 | @YouJiacheng |
| #17 | 3.57 min | Sparsify value embeddings, rotary improvements | 2024-12-17 | @YouJiacheng |
| #19 | 3.142 min | FP8 head, offset logits, lr-decay floor | 2025-01-13 | @YouJiacheng |
| #20 | 2.992 min (first sub-3-minute) | batched Muon et al. | 2025-01-16 | 6 credits incl. @YouJiacheng |

The #15-#17 streak established the **value-embedding family** (U-net-pattern, split,
sparsified) that became a signature technique of the run.

## Muon co-author

Listed as **Jiacheng You** among Muon's co-authors in
[Deriving Muon](https://jeremybernste.in/writing/deriving-muon). See [[concepts/jxbz]].

## Related Pages

- [[concepts/jxbz]] — Muon theory author
- [[entities/grad]] — fellow speedrun contributor
