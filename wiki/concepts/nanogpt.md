---
title: "nanoGPT"
type: concept
aliases:
  - nanogpt
created: 2026-04-25
updated: 2026-10-26
tags:
  - concept
  - education
  - model-training
  - open-source
  - transformer
  - gpt-2
related:
  - "[[entities/andrej-karpathy]]"
  - "[[entities/karpathy-projects]]"
  - "[[concepts/micrograd]]"
  - "[[concepts/ai-benchmarks/nanogpt-speedrun]]"
sources:
  - https://github.com/karpathy/nanoGPT
---

# nanoGPT

**nanoGPT** is Andrej Karpathy's minimal, readable PyTorch reimplementation of GPT-2 pretraining and finetuning — ~300 lines in `train.py` plus a small `model.py`. Released October 2022, it became the de-facto reference implementation for "how a transformer LM is actually trained," and the default substrate for fast training research, education, and speedrun competitions.

## What It Is

- **Goal**: reproduce GPT-2 (124M/350M/774M/1.6B) on OpenWebText in a codebase small enough to read in one sitting — no libraries beyond PyTorch.
- **The Karpathy education stack**: [micrograd](https://github.com/karpathy/micrograd) (autograd in ~100 lines) → makemore (bigrams→MLP) → **nanoGPT** (full transformer) → llm.c (C/CUDA) → [microgpt](https://github.com/karpathy/microgpt) (200 lines, no-framework). Each step removes a layer of abstraction; see [[entities/karpathy-projects]].
- One command trains: `python train.py --config train_shakespeare_char` (character-level, cheap) up to GPT-2 124M pretraining (~4 days on 8×A100, roughly $75 at 2022 cloud prices — the figure Karpathy publicized to demystify "you need a lab" thinking).

## Why It Matters

1. **Democratized pretraining.** The "$100 GPT-2 reproduction" framing turned transformer pretraining from lab-only lore into a weekend-scale experiment.
2. **Research substrate.** Its clean single-file model made it the standard target for optimizer/kernel/precision experiments — Cerebras-GPT-style ablations, speedrun competitions, and quantization/attention research all fork nanoGPT.
3. **Benchmark lineage.** [[concepts/ai-benchmarks/nanogpt-speedrun]] (Prime Intellect, 2026) grew directly out of the "Kaggle nanoGPT speedrun" meme — training nanoGPT to 0.85 val loss as fast as possible — which in 2026 became a frontier-model autonomy benchmark (harness×model leaderboard, 153 runs across 18 models).
4. **Pedagogical canon.** "Read nanoGPT" is standard advice for anyone moving from using LLMs to training them; Karpathy's videos walk through it line by line.

## Notable Forks & Descendants

- **llm.c** (Karpathy, 2024) — same algorithm in C/CUDA/MPI, matches GPT-2 124M at ~2× the speed.
- **modded-nanoGPT** (Keller Jordan et al.) — speedrun-oriented fork where many efficiency tricks (e.g. Muon optimizer lineage) were prototyped.
- Countless "nanoGPT from scratch" implementations (JAX, tinygrad, Mojo) serve as cross-framework translation exercises.

## Related Concepts

- [[entities/andrej-karpathy]] — author
- [[entities/karpathy-projects]] — project timeline page
- [[concepts/micrograd]] — the autograd teaching tool that precedes it
- [[concepts/ai-benchmarks/nanogpt-speedrun]] — the autonomy benchmark derived from nanoGPT speedrunning
- [[concepts/tinygrad]] — George Hotz's framework often used for nanoGPT reimplementations

## Sources

- [karpathy/nanoGPT on GitHub](https://github.com/karpathy/nanoGPT)
- [Karpathy's nanoGPT announcement & GPT-2 reproduction cost thread](https://x.com/karpathy/status/1578377177384833024)
