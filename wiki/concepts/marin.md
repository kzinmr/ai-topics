---
title: Marin
type: concept
created: 2026-06-07
updated: 2026-06-07
aliases: [marin-framework, marin-community]
status: active
description: "Open-source framework for foundation model research and development from Stanford CRFM. Reproducible training pipeline with open development on GitHub."
tags:
  - training
  - open-source
  - foundation-models
  - stanford
  - model-training
  - framework
  - pretraining
  - llm
sources:
  - raw/articles/2026-06-07_eliebakouch_marin.md
---

# Marin

**GitHub:** [marin-community/marin](https://github.com/marin-community/marin) (1.1k ★, 126 forks, Apache 2.0)
**Website:** [marin.community](https://marin.community)
**Documentation:** [marin.readthedocs.io](https://marin.readthedocs.io/en/latest/)
**Discord:** [Join](https://discord.gg/J9CTk7pqcM)

## Overview

Marin is an open-source framework for the research and development of [[concepts/foundation-models|foundation models]], built by the Stanford CRFM (Center for Research on Foundation Models) community. Unlike many training frameworks that only record final artifacts, Marin records **every step** — including failed experiments — making the entire research process transparent and reproducible.

The framework covers the full training pipeline: data curation, transformation, filtering, tokenization, training, and evaluation. It is built on [Levanter](https://github.com/stanford-crfm/levanter), Stanford CRFM's JAX-based training library.

> "I am not afraid of storms, for I am learning how to sail my ship." — Louisa May Alcott (Marin's motto)

Marin has been endorsed by researchers including **[[entities/elie-bakouch|Elie Bakouch]]**, who praised its "scientific approach to training, readiness to take risks, and fully open development."

## Key Features

### Reproducibility by Design
Every step in a Marin experiment — from raw data ingestion to final model checkpoint — is recorded. Failed experiments are preserved alongside successful ones, providing a complete research trail. Experiment specifications are tracked in GitHub issues with linked WandB reports and data browser views.

### Makefile-Style Experiment Definition
Experiments are defined as a directed acyclic graph (DAG) of steps that execute in topological order:

```python
# 1. Choose and tokenize a dataset
tinystories_tokenized = default_tokenize(
    name="roneneldan/TinyStories",
    dataset="roneneldan/TinyStories",
    tokenizer=llama3_tokenizer,
)

# 2. Define training config
nano_train_config = SimpleTrainConfig(
    resources=ResourceConfig.with_cpu(),
    train_batch_size=4,
    num_train_steps=100,
    learning_rate=6e-4,
)

# 3. Train — depends on tokenized data
nano_model = default_train(
    name="marin-nano-tinystories",
    tokenized=tinystories_tokenized,
    model_config=llama_nano,
    train_config=nano_train_config,
)
```

### Full Data Pipeline
Marin includes tools for:
- **HTML-to-text extraction** with format preservation
- **Quality filtering** (cascading classifiers, compression-ratio filters)
- **Deduplication** (minhash, Feistel shuffle for deterministic global shuffling)
- **Tokenization** (supports Llama 3 tokenizer as default)
- **Data mixture scheduling** with curriculum support

### Hardware Flexibility
- **TPU**: Multi-slice TPU v5e, v5p, v4 (including v4-2048)
- **GPU**: Multi-node GPU support (in development)
- **INT8 training** for efficiency

## Models Trained with Marin

| Model | Parameters | Tokens | Key Achievement |
|-------|-----------|--------|-----------------|
| Marin 8B (Tootsie) | 8B | ~12.75T | First open-source 8B to outperform Llama 3.1 8B |
| Marin 32B | 32B | ~6.4T | Successful scale-up with QK-Norm stability fix |
| Marin 13B | 13B | — | Intermediate scale experiment |
| Marin 24B | 24B | — | Intermediate scale experiment |
| Marin 70B | 70B | — | Large-scale experiment |

The Marin 8B run is the most thoroughly documented, with a 5-phase "Tootsie Roll" process that adapted training strategy reactively based on intermediate results. The 32B run encountered loss spikes that were ultimately resolved by adopting Qwen3's QK-Norm architecture, demonstrating Marin's value for diagnosing and fixing training instability.

## Technical Architecture

### Training Stack
- **Backend**: [Levanter](https://github.com/stanford-crfm/levanter) (JAX)
- **Attention**: JAX TPU Splash Attention kernel
- **Precision**: Mixed float32/bfloat16
- **Optimizer**: AdamW (default), Muon (experimental)
- **Schedules**: WSD, WSD-S, Cosine
- **Stability**: Z-loss, grad norm clipping, update norm clipping, skip-bad-steps

### Architecture Configurations Used
| Model | Arch | `hidden_dim` | `num_layers` | `num_heads` | Notes |
|-------|------|-------------|-------------|------------|-------|
| Nano | Llama | 576 | 8 | 8 | Tutorial |
| 8B | Llama 3.1 | 4096 | 32 | 32 | Matches Llama 3.1 8B |
| 32B | Llama/Qwen3 | 5120 | 64 | 40 | QK-Norm added in Phase 3 |

## Key Research Contributions

### The "Tootsie Roll" Training Process
Marin's signature approach: start training with the best available recipe, instrument heavily, and make evidence-driven changes mid-flight. This contrasts with traditional pre-planned training runs and embraces the uncertainty of frontier model development.

### WSD-S Scheduling
Research on cyclic Warmup-Stable-Decay schedules showed that high learning rates can be maintained for extended periods with periodic rapid cooldowns to assess progress, without "wasting" FLOPs.

### The EMA Gap
Marin's 8B run revealed that the gap between EMA model loss and "hot" model loss is surprisingly stable over time (~0.015 bpb for c4en), changing only with learning rate or data distribution changes — not trending up or down.

### Microannealing Methodology
Systematic study of cooldown data mixtures found that:
- Naively oversampling "high-quality" data degrades task performance
- The optimal cooldown mixture is **70% pretraining mix / 15% FLAN / 15% high-quality data**
- FLAN provides crucial few-shot-learning-inducing structure

### Stability at Scale
The 32B run demonstrated that loss spikes at larger scales can be traced to architectural causes (resolved by QK-Norm) and that diagnostic tools (update norm clipping, skip-bad-steps) are essential for production training.

## Comparison with Other Frameworks

| Aspect | Marin | Hugging Face Trainer | Megatron-LM | torchtitan |
|--------|-------|---------------------|-------------|------------|
| Backend | JAX (Levanter) | PyTorch | PyTorch | PyTorch |
| Reproducibility | Full (all steps recorded) | Config-based | Config-based | Config-based |
| Experiment tracking | GitHub issues + WandB | WandB | WandB/TensorBoard | WandB |
| Open development | Yes (public issues, real-time) | No | No | No |
| Data pipeline | Built-in | External | External | External |
| Multi-TPU | First-class | Limited | Yes | No |
| License | Apache 2.0 | Apache 2.0 | Apache 2.0 | BSD-3 |

## Open Development Philosophy

Marin practices radical transparency in AI research:

1. **Public GitHub Issues**: Every experiment, bug, and decision is tracked in public issues
2. **Real-time training logs**: WandB reports are publicly accessible
3. **Data Browser**: Interactive exploration of training data and experiment specifications
4. **Retrospectives**: Detailed post-mortems documenting what worked, what failed, and why
5. **Community Discord**: Direct engagement with the research team

This approach has attracted attention from researchers like Elie Bakouch, who values the ability to "follow everything on GitHub."

## Related Wikilinks

- [[entities/elie-bakouch]] — Researcher who endorsed Marin
- [[concepts/foundation-models]] — What Marin is designed to train
- [[concepts/scaling-laws]] — Marin's research on scaling and scheduling
- [[concepts/pretraining]] — Marin's primary focus
- [[concepts/training]] — Core training techniques used
- [[concepts/levanter]] — JAX training library Marin is built on
- [[concepts/mixture-of-experts]] — MoE experiments run on Marin
- [[concepts/qwen]] — Qwen3 architecture adopted for Marin 32B
- [[entities/stanford]] — Stanford CRFM, Marin's home
- [[concepts/smollm]] — Small model training (contrast with Marin's scale)

## Sources

- [Marin GitHub Repository](https://github.com/marin-community/marin)
- [Marin Documentation](https://marin.readthedocs.io/en/latest/)
- [Marin 8B Retrospective](https://github.com/marin-community/marin/blob/main/docs/reports/marin-8b-retro.md)
- [Marin 32B Retrospective](https://github.com/marin-community/marin/blob/main/docs/reports/marin-32b-retro.md)
- [Marin Community Website](https://marin.community)
- [Elie Bakouch X Post about Marin](https://x.com/eliebakouch)
- [WSD-S Paper (arXiv:2410.05192)](https://arxiv.org/abs/2410.05192)
- [Levanter Repository](https://github.com/stanford-crfm/levanter)
