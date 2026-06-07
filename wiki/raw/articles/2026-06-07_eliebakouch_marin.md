# Marin — Open-Source Foundation Model Training Framework

**Source:** Elie Bakouch (@eliebakouch) X post
**Scraped from:** https://github.com/marin-community/marin
**Date scraped:** 2026-06-07
**Context:** X accounts scan found Elie Bakouch post about Marin: "one of my favorite projects is Marin from the stanford folks, they have a scientific approach to training, are ready to take risks and are fully open (even open development where you can follow everything on github!)"

---

## GitHub Repo Overview

- **Repository:** [marin-community/marin](https://github.com/marin-community/marin)
- **Organization:** marin-community (created 2024-03-22)
- **Stars:** 1,057 (1.1k)
- **Forks:** 126
- **Watchers:** 19
- **Open Issues:** 561
- **License:** Apache 2.0
- **Primary Language:** Python (55.7%), HTML (39.5%), Rust (1.9%), Vue (1.3%), TypeScript (0.6%)
- **Website:** https://marin.community
- **Documentation:** https://marin.readthedocs.io/en/latest/

## Description (from repo)

> "I am not afraid of storms, for I am learning how to sail my ship." — Louisa May Alcott

Marin is an open-source framework for the research and development of foundation models.

A key feature of Marin is **reproducibility**: every step, from raw data to the final model are recorded, not just the end result. This includes failed experiments, so the entire research process is transparent.

Marin's primary use case is training language models like Llama, DeepSeek, Qwen, etc. Notably, this includes data curation, transformation, filtering, tokenization, training, and evaluation.

The team used Marin to train the first open-source 8B parameter model to outperform Llama 3.1 8B. They have also trained Marin 13B, 24B, 32B, and 70B models.

## Key Experiments

- **Marin 8B (Tootsie):** First open-source 8B to outperform Llama 3.1 8B. Trained in 5 phases using a "Tootsie Roll" adaptive approach: Kestrel (DCLM WSD-S), Ocelot (DCLM EMA), Jellyfish (first cooldown), Phoenix (reheated), Starling (second cooldown). Used TPU v5e-256 and v4-2048 hardware.
- **Marin 32B:** Scale-up of 8B recipe. Hit loss spikes resolved by switching to Qwen3 backbone with QK-Norm. Trained ~6.4T tokens total. Base checkpoint on Hugging Face.
- **Marin 13B, 24B, 70B:** Additional scale experiments.

## Architecture & Design

Marin experiments are defined as a set of steps that can depend on each other and executed in topological order (like a Makefile). Steps include:

1. **Data Curation**: HTML-to-text extraction, quality filtering, deduplication
2. **Tokenization**: Configurable tokenizers (Llama 3 default)
3. **Training**: Levanter-based JAX training with AdamW, WSD schedules
4. **Evaluation**: lm-evaluation-harness integration, Paloma perplexity

## Technical Details

- Built on [Levanter](https://github.com/stanford-crfm/levanter) (Stanford CRFM's JAX training library)
- Uses JAX's TPU Splash Attention kernel
- Mixed float32/bfloat16 precision
- AdamW optimizer with WSD (Warmup-Stable-Decay) schedules
- EMA (Exponential Moving Average) for eval monitoring
- Supports multi-slice TPU and multi-node GPU
- Z-loss default for stability
- INT8 training support

## Key Research Findings

- **WSD-S scheduling** works for long-running training
- **EMA gap** (difference between EMA model loss and hot model loss) is stable over time
- **Microannealing** experiments: 70% PT / 15% FLAN / 15% HQ is the best cooldown mixture
- **QK-Norm** essential for stability at 32B scale
- **Muon optimizer** explored as alternative to AdamW
- **Data quality over quantity** for cooldown phases

## Community & Open Development

- Open development tracked via GitHub issues with detailed experiment reports
- Marin Discord community
- Data Browser for experiment transparency
- WandB reports for all runs
- Agent skills in `.agents/skills/` for guided workflows

## Quote from Elie Bakouch

> "one of my favorite projects is Marin from the stanford folks, they have a scientific approach to training, are ready to take risks and are fully open (even open development where you can follow everything on github!)"
