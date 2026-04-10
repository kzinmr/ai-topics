---
title: "Grad (@Grad62304977)"
created: 2026-04-10
updated: 2026-04-10
tags: [person, x-account, ml-researcher, nanogpt-speedrun, smollm2, transformer-architecture, optimization]
aliases: ["@Grad62304977", "Grad"]
source: x-account
---

# Grad (@Grad62304977)

| | |
|---|---|
| **X/Twitter** | [@Grad62304977](https://x.com/Grad62304977) |
| **GitHub** | [github.com/Grad62304977](https://github.com/Grad62304977) |
| **Role** | Independent ML Researcher |
| **Focus** | Transformer architecture optimization, training efficiency, NanoGPT speedrun |
| **Known for** | Value residual learning, QK norm, logit softcap, SmolLM2 co-author |

## Overview

Grad (known online as **@Grad62304977**) is an independent ML researcher who has become one of the most prolific contributors to the **NanoGPT speedrun** — a collaborative/competitive effort to train a GPT-2-scale model (124M parameters) to target validation loss on FineWeb as fast as possible. Starting from Karpathy's 45-minute baseline on 8xH100, the speedrun has been pushed down to **under 3 minutes**, with Grad being responsible for the majority of the key architectural innovations that made this possible.

Beyond the speedrun, Grad is a co-author of the **SmolLM2** paper ("When Smol Goes Big — Data-Centric Training of a Small Language Model", Feb 2025), which documents the training of state-of-the-art small language models (135M, 360M, and 1.7B parameters) through careful data curation and multi-stage training.

Grad embodies the growing movement of **independent researchers** making frontier-level contributions without institutional affiliation — demonstrating that deep technical insight, open collaboration, and public experimentation can rival well-funded lab research.

## Key Architectural Contributions

Grad is credited with introducing or co-developing the following transformer architecture modifications that became central to the NanoGPT speedrun:

| Innovation | Record | Impact |
|------------|--------|--------|
| **Pad embeddings** + **ReLU² activation** + **zero-init projections** + **QK norm** | 15.2 min (from 22.3) | Stabilized training, improved gradient flow |
| **Untied embedding and lm_head** | 10.8 min (from 12.0) | Freed the model from weight tying constraints |
| **Value residual learning** + **embedding skip connections** | 8.2 min (from 10.8) | Allowed information to bypass attention layers |
| **Momentum warmup** | (contributed to) | Stabilized optimizer dynamics early in training |
| **Logit softcap** (tanh scaling) | (contributed to) | Prevented logit explosion, improved stability |
| **FlexAttention window size warmup** | 4.66 min (from 5.03) | Progressive attention window expansion |
| **Long-short sliding window attention** + **attention scale** + **batched Muon** | 2.99 min | Combined multiple optimizations into one record |

### Value Residual Learning

Perhaps Grad's most influential contribution is **value residual learning** — the idea of mixing attention values with a residual path before the output projection. In the modded-nanogpt codebase, this appears as:

```python
# value residual lambda
self.lamb = nn.Parameter(torch.tensor(0.5))  # @Grad62304977
...
v = (1 - self.lamb) * v + self.lamb * vi.view_as(v)  # @Grad62304977
```

This technique allows the model to interpolate between the attention-computed values and an alternative pathway, providing a learnable balance that improves training stability and final performance. The approach was later incorporated into larger models and research.

### QK Norm

Grad suggested applying **normalization to Query and Key vectors** in the attention mechanism, which prevents the dot products from growing too large and destabilizing the softmax. This is now standard practice in modern transformer architectures.

### Zero Initialization of Projections

Grad proposed **zero-initializing the output projection weights** in attention layers (`self.c_proj.weight.data.zero_()`), which ensures that residual connections dominate early in training, providing a stable starting point before the model learns complex transformations.

## NanoGPT Speedrun

The NanoGPT speedrun is a public, collaborative effort to minimize the time required to train a 124M-parameter GPT-2 model to a target validation loss on the FineWeb dataset. The progression shows Grad's outsized impact:

| # | Time | Key Change | Contributors |
|---|------|------------|-------------|
| 1 | 45 min | llm.c baseline | @karpathy |
| 2 | 31.4 min | Tuned learning rate & rotary embeddings | @kellerjordan0 |
| 3 | 24.9 min | Muon optimizer | @kellerjordan0, @jxbz |
| 4 | 22.3 min | Muon improvements | @kellerjordan0, @bozavlado |
| 5 | **15.2 min** | Pad embeddings, ReLU², zero-init, QK norm | **@Grad62304977**, @kellerjordan0 |
| 6 | 13.1 min | Distributed Muon overhead | @kellerjordan0 |
| 7 | 12.0 min | PyTorch 2.5.0 upgrade | @kellerjordan0 |
| 8 | **10.8 min** | Untied embed and lm_head | **@Grad62304977**, @kellerjordan0 |
| 9 | **8.2 min** | Shortcuts & tweaks | **@Grad62304977**, @kellerjordan0 |
| 10 | 7.8 min | Bfloat16 activations | @kellerjordan0 |
| 11 | 7.2 min | U-net & 2x lr | @brendanh0gan |
| 12 | 5.03 min | FlexAttention | @KoszarskyB |
| 13 | **4.66 min** | Attention window warmup | @fernbear.bsky.social |
| ... | ... | ... | ... |
| 20+ | **~2.9 min** | Multiple optimizations | Grad and others |

Grad was directly responsible for **records #5, #8, and #9**, which together accounted for a **~45% reduction** in training time (from 22.3 min to 8.2 min). His contributions are cited in every major fork of the speedrun, including [KellerJordan/modded-nanogpt](https://github.com/KellerJordan/modded-nanogpt), [alexjc/nanogpt-speedrun](https://github.com/alexjc/nanogpt-speedrun), and [4rtemi5/modded-nanogpt](https://github.com/4rtemi5/modded-nanogpt).

## SmolLM2

Grad is a co-author of the **SmolLM2 paper** (arXiv:2502.02737, Feb 2025), which documents the training of small but highly capable language models. The paper's author list includes:

> Loubna Ben Allal, Anton Lozhkov, **Elie Bakouch**, Gabriel Martín Blázquez, Guilherme Penedo, Lewis Tunstall, Andrés Marafioti, Hynek Kydlíček, Agustín Piqueres Lajarín, Vaibhav Srivastav, Joshua Lochner, Caleb Fahlgren, Xuan-Son Nguyen, Clémentine Fourrier, Ben Burtenshaw, Hugo Larcher, Haojun Zhao, Cyril Zakka, Mathieu Morlon, Colin Raffel, Leandro von Werra, Thomas Wolf

SmolLM2-1.7B was trained on **11 trillion tokens** using a multi-stage approach that mixed web text with specialized math, code, and instruction-following data. The model outperforms other recent small LMs including Qwen2.5-1.5B and Llama3.2-1B.

Key innovations in SmolLM2:
- **Multi-stage training strategy** with progressive data mix adjustment
- **New specialized datasets**: FineMath, Stack-Edu, SmolTalk
- **Manual refinement process** based on ablation studies
- **Full open release** of models, datasets, and training code

## Core Ideas

### Architecture Over Scale

Grad's work consistently demonstrates that **architectural improvements can outperform raw scale increases**. While the industry trend has been toward ever-larger models, Grad has shown that careful design choices in attention mechanisms, residual connections, weight initialization, and normalization can dramatically improve training efficiency and final performance at fixed parameter counts.

### Open, Collaborative Research

The NanoGPT speedrun is a model for **open, competitive-collaborative research**. Each improvement is publicly documented with code, commit logs, and attribution. Grad thrives in this environment — rapidly iterating, sharing results, and building on others' contributions. This contrasts sharply with the closed-door research practices of major AI labs.

### The Independent Researcher Paradigm

Grad operates without institutional affiliation, yet produces work that is cited and used by researchers worldwide. This is enabled by:
- **Accessible compute** (cloud GPUs via vast.ai, RunPod, etc.)
- **Open-source frameworks** (PyTorch, Hugging Face Transformers)
- **Public datasets** (FineWeb, The Pile, etc.)
- **Open communication** (X/Twitter, GitHub, Discord)

His success demonstrates that **meaningful contributions to ML research don't require a lab affiliation** — they require insight, rigor, and a willingness to share.

## Community Recognition

Grad's contributions are widely acknowledged in the ML community:
- **Keller Jordan** (@kellerjordan0), the speedrun organizer, regularly credits Grad's innovations in commit messages and READMEs
- The **modded-nanogpt** codebase contains explicit `# @Grad62304977` comments marking his contributions
- His work on value residual learning and QK norm has been adopted by other researchers in the speedrun ecosystem
- Co-authorship on the SmolLM2 paper with Hugging Face researchers validates his contributions to mainstream ML research

## Related

- [[entities/keller-jordan]] — Speedrun organizer, Muon optimizer creator
- [[entities/elie-bakouch]] — SmolLM2 co-author, Hugging Face researcher
- [[entities/andrej-karpathy]] — Created llm.c baseline, inspired the speedrun
- [[concepts/muon-optimizer]] — Second-order optimizer used in the speedrun
- [[concepts/transformer-architecture]] — Grad's primary area of innovation
- [[concepts/smol-lm]] — Small language model family Grad contributed to
- [[concepts/efficient-training]] — Core theme of Grad's work

## Sources

- [NanoGPT speedrun — KellerJordan/modded-nanogpt](https://github.com/KellerJordan/modded-nanogpt)
- [SmolLM2 paper (arXiv:2502.02737)](https://arxiv.org/abs/2502.02737)
- [SmolLM2: When Smol Goes Big — Hugging Face](https://huggingface.co/papers/2502.02737)
- [Inside the family of Smol models — HF blog](https://huggingface.co/blog/Kseniase/insidesmol)
- [Grad's X/Twitter (@Grad62304977)](https://x.com/Grad62304977)
- [Grad's GitHub](https://github.com/Grad62304977)
