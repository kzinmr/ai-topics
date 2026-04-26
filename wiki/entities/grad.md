---
title: Fares Obeid (@Grad62304977)
type: entity
created: 2026-04-10
updated: 2026-04-14
tags:
- ml-researcher
- transformer-architecture
- optimization
- rwkv
- prime-intellect
- eleutherai
- nanogpt-speedrun
aliases:
- '@Grad62304977'
- Grad
- Fares Obeid
- Fareso
- faresobeid
source: x-account
status: enriched
depth: L3
sources: []
---

# Fares Obeid (@Grad62304977)

| | |
|---|---|
| **X/Twitter** | [@Grad62304977](https://x.com/Grad62304977) |
| **GitHub** | [Grad62304977](https://github.com/Grad62304977) |
| **HuggingFace** | [Fareso](https://huggingface.co/Fareso) |
| **LinkedIn** | [Fares Obeid](https://linkedin.com/in/fares-obeid-5461a7253) |
| **Email** | @imperial.ac.uk, @kingsely.org |
| **Role** | Research Engineer at Prime Intellect |
| **Education** | MEng Computing (AI & ML), Imperial College London (2024-2027) |
| **Known for** | NanoGPT speedrun records, Value Residual Learning, INTELLECT-3, GoldFinch RWKV/Transformer hybrid |
| **Organizations** | EleutherAI, Recursal AI, Prime Intellect |

## Overview

**Fares Obeid** (handle **@Grad62304977** on X, **Fareso** on HuggingFace, **faresobeid** on GitHub) is an ML researcher who has made outsized contributions to open-source transformer architecture optimization despite being a student. He is responsible for multiple record-breaking improvements in the **NanoGPT speedrun**, a collaborative effort to train a 124M parameter GPT-2 model to target validation loss on FineWeb as quickly as possible. His work spans **value residual learning**, **attention normalization**, and **linear attention/transformer hybrids**.

Beyond the speedrun, Fares is a co-author on significant papers including **Value Residual Learning** (ACL 2025), **GoldFinch** (RWKV/Transformer hybrid), and **INTELLECT-3** (106B parameter MoE model trained with large-scale RL). He is currently working at Prime Intellect on large-scale distributed training infrastructure.

## Identity Resolution

> @Grad62304977 = Fares Obeid = Fareso (HuggingFace) = faresobeid (GitHub) = Imperial College London student

This was resolved through:
- GitHub commits on [KellerJordan/modded-nanogpt](https://github.com/KellerJordan/modded-nanogpt) explicitly attributing records to `@Grad62304977`
- HuggingFace profile [Fareso](https://hf.co/Fareso) listing 34252.8 TFLOPS, 13 papers, 2 models
- OpenReview profile confirming Fares Obeid at Imperial College London
- LinkedIn showing Fares Obeid, MEng Computing (AI & ML) at Imperial, 2024-2027
- Author lists on GoldFinch (arXiv:2407.12077), Value Residual Learning (ACL 2025), INTELLECT-3

## NanoGPT Speedrun Contributions

The NanoGPT speedrun is a collaborative effort to train a 124M parameter GPT-2 model to 3.28 validation loss on FineWeb as fast as possible. Fares contributed to multiple record-breaking improvements:

| Record | Time | Improvement | Key Changes |
|--------|------|-------------|-------------|
| #5 | 15.2 min | -7.1 min from #4 | Pad embeddings, ReLU², zero-init projections, QK norm |
| #8 | 10.8 min | -4.4 min from #7 | Untied embedding and lm_head |
| #9 | 8.2 min | -2.6 min from #8 | Value & embedding skip connections, momentum warmup, logit softcap |

Combined, these three contributions reduced training time by **~45%** from the previous records. The current record stands at 2.9 minutes (as of 2025).

> "The training has attained this speed due to the contributions of meself, @Grad62304977, @jxbz, @bozavlado, @brendanh0gan, @KoszarskyB, & @fernbear.bsky.social." — [alexjc/nanogpt-speedrun README](https://github.com/alexjc/nanogpt-speedrun)

The speedrun code contains explicit `# @Grad62304977` attribution comments marking Fares's specific contributions:

```python
# @Grad62304977: https://x.com/Grad62304977/status/1849177879059161422
# @Grad62304977: https://x.com/Grad62304977/status/1854295837741809933
```

## Value Residual Learning (ACL 2025)

Fares co-authored the **Value Residual Learning** paper with Zhanchao Zhou, Tianyi Wu, Zhiyun Jiang, and Zhenzhong Lan, published at ACL 2025.

**Paper:** "Value Residual Learning For Alleviating Attention Concentration In Transformers" (arXiv:2410.17897)

> "While Transformer models have achieved remarkable success in various domains, the effectiveness of information propagation through deep networks remains a critical challenge. Standard hidden state residuals often fail to adequately preserve initial token-level information in deeper layers."

Key contributions:
- **ResFormer** architecture: adds value residual connections to standard hidden state residuals
- Achieves equivalent validation loss with **16.11% fewer parameters** and **20.3% less training data**
- **SVFormer** variant: shares first layer's value embedding across all layers, reducing KV cache by ~50%
- Performance influenced by sequence length and cumulative learning rate

This paper directly informed the speedrun's Record #9 improvements (value skip connections).

## GoldFinch: RWKV/Transformer Hybrid

**Paper:** "GoldFinch: High Performance RWKV/Transformer Hybrid with Linear Pre-Fill and Extreme KV-Cache Compression" (arXiv:2407.12077)

> "We introduce GoldFinch, a hybrid Linear Attention/Transformer sequence model that uses a new technique to efficiently generate a highly compressed and reusable KV-Cache in linear time and space with respect to sequence length."

Fares contributed to research discussions and experiments during development. The paper combines:
- **GOLD transformer** stacked on enhanced **Finch (RWKV-6)** architecture
- KV cache **756-2550× smaller** than traditional transformer cache
- Autoregressive generation at O(n) per token, but pre-fill at O(1) per token using RNN
- Trained up to 1.5B parameters on 1.5 trillion tokens of minipile

This work represents Fares's interest in **efficient architectures** that break the quadratic scaling of standard transformers.

## INTELLECT-3 (Prime Intellect)

**Paper:** "INTELLECT-3: Technical Report" (arXiv:2512.16144)

Fares is a co-author on this major paper describing a **106B parameter Mixture-of-Experts model** (12B active) trained with large-scale reinforcement learning:

- Trained on **512×H200 GPUs** with high training efficiency
- Outperforms existing open-source models in its size range across math, code, science, and reasoning benchmarks
- Surpasses frontier open models **6× larger** on reasoning and agentic benchmarks
- Based on **GLM-4.5-Air-Base** model
- Achieves SOTA with only **12B active parameters** (vs 106B total)
- Full infrastructure stack open-sourced: RL frameworks, complete recipe, environments

This represents a significant step in Fares's career trajectory from independent researcher to major lab contributor.

## Core Research Philosophy

### Efficiency Through Architecture

Fares consistently focuses on **architectural efficiency** over brute-force scaling:
- **NanoGPT speedrun**: reducing training time by 45% through architectural modifications (not more compute)
- **Value Residual Learning**: achieving equivalent performance with 16% fewer parameters
- **GoldFinch**: KV cache compression by 756-2550× through hybrid RNN/transformer design
- **INTELLECT-3**: 106B total parameters but only 12B active through MoE

### Collaborative Open Science

All of Fares's major contributions are in **open-source, collaborative projects**:
- NanoGPT speedrun is a public, community-driven benchmark
- Value Residual Learning published at ACL with open access
- GoldFinch released under Apache 2.0 license
- INTELLECT-3 fully open-sourced with infrastructure

### Attention is the Bottleneck

The thread connecting his work is the insight that **attention mechanisms are the bottleneck** in transformer efficiency:
- Value residual learning addresses information flow through attention
- GoldFinch compresses the KV cache to enable longer contexts
- QK normalization in speedrun stabilizes attention computation
- Linear attention hybrids replace quadratic attention entirely

## Timeline

| Date | Event |
|------|-------|
| 2024-2027 | MEng Computing (AI & ML) at Imperial College London |
| Apr 2024 | Eagle and Finch (RWKV-5/6) paper co-author |
| Jul 2024 | GoldFinch paper published (arXiv:2407.12077) |
| Oct 2024 | NanoGPT speedrun Record #5 (15.2 min) |
| Nov 2024 | Records #8 (10.8 min) and #9 (8.2 min) |
| Nov 2024 | INTELLECT-3 paper (106B MoE) |
| 2025 | Value Residual Learning accepted at ACL 2025 |

## Key Quotes & Attributions

From the NanoGPT speedrun README:
> "@Grad62304977: https://x.com/Grad62304977/status/1849177879059161422"

From the Value Residual Learning abstract:
> "This paper introduces ResFormer, a novel architecture that enhances information flow by incorporating value residual connections in addition to hidden state residuals."

From the GoldFinch abstract:
> "Our cache size savings increase linearly with model layer count, ranging from 756-2550 times smaller than the traditional transformer cache for common sizes."

## Related People

- [[andrej-karpathy]] — Karpathy's llm.c was the baseline for the NanoGPT speedrun
- [[concepts/keller-jordan]] — Speedrun organizer and frequent collaborator
- [[concepts/zhanchao-zhou]] — Value Residual Learning co-author
- [[concepts/jxbz]] — Jeremy Bernstein, speedrun contributor (Newton-Schulz iteration)
- [[concepts/bozavlado]] — Speedrun contributor
- [[concepts/brendanh0gan]] — Speedrun contributor (U-net, 2x lr record)
-  — Speedrun contributor
-  — Speedrun contributor (Muon improvements)
-  — Speedrun contributor (Muon improvements)

## Sources

- [NanoGPT Speedrun (KellerJordan/modded-nanogpt)](https://github.com/KellerJordan/modded-nanogpt)
- [alexjc/nanogpt-speedrun](https://github.com/alexjc/nanogpt-speedrun)
- [Value Residual Learning (ACL 2025)](https://aclanthology.org/2025.acl-long.1375/)
- [GoldFinch Paper (arXiv:2407.12077)](https://arxiv.org/abs/2407.12077)
- [INTELLECT-3 Technical Report (arXiv:2512.16144)](https://arxiv.org/abs/2512.16144)
- [PrimeIntellect-ai/prime-rl PR #614](https://github.com/PrimeIntellect-ai/prime-rl/pull/614)
- [Fareso on HuggingFace](https://huggingface.co/Fareso)
- [Fares Obied on csauthors.net](https://www.csauthors.net/fares-obied/)
- [LinkedIn: Fares Obeid](https://linkedin.com/in/fares-obeid-5461a7253)
