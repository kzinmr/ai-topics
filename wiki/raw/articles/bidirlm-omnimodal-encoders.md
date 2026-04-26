# BidirLM: Turning Generative LLMs into Omnimodal Encoders

- **Source:** https://huggingface.co/blog/Nicolas-BZRD/bidirlm-release
- **Authors:** Nicolas-BZRD (Théo Deschamps-Berger)
- **Date:** 2026-04-07
- **Domain:** ai-models, multimodal, embedding, open-source
- **Tags:** model, multimodal, encoder, open-source, huggingface

## Summary

BidirLM introduces an open-source recipe to transform any causal decoder LLM into a powerful bidirectional encoder. Through systematic ablations on Gemma3 and Qwen3, they identified the adaptation strategy that works: a two-phase pipeline of Masked Next-Token Prediction (MNTP) followed by contrastive training. They then scaled this without access to original pre-training data, and composed specialized causal models through weight merging to create BidirLM-Omni, a single compact omnimodal model handling text, images, and audio.

## Key Findings

### Adaptation Strategy (Controlled Experiments)
Tested 5 variants on Gemma3 and Qwen3:
1. **Base** — original causal model
2. **Bi+Base** — bidirectional attention enabled
3. **Bi+MNTP** — bidirectional + masked next-token prediction
4. **Bi+Contrastive** — bidirectional + contrastive training
5. **Bi+MNTP+Contrastive** — both phases sequentially

**Finding:** Simply flipping attention mask gives inconsistent results. The model needs to *learn* how to use bidirectional context via MNTP. Then contrastive training builds embedding quality.

### Scaling Without Original Pre-training Data
Problem: Extending MNTP training on different data distribution causes catastrophic forgetting (languages, code, math).
Solutions:
- **Linear weight merging:** 50/50 average of adapted model weights with original base checkpoint (cosine similarity ~0.97)
- **Multi-domain data mixture:** Replace 20% of English training data with multilingual, math, and code samples

Result: +2 points on multilingual benchmarks, up to +11 on code for Gemma.

### Omnimodal Composition
BidirLM-Omni-2.5B is built by composing specialized causal models through weight merging — a single compact model that handles text, images, and audio, beating both omnimodal and unimodal specialists on standard benchmarks.

### Model Family
- Text-only embedding models at 270M, 0.6B, 1B, 1.7B params
- Omnimoal variant at 2.5B
- Full model family, training data, and checkpoints released on HuggingFace Hub

## Models Available
- [BidirLM-Omni-2.5B-Embedding](https://huggingface.co/BidirLM/BidirLM-Omni-2.5B-Embedding)
- [BidirLM-Embedding Collection](https://huggingface.co/collections/BidirLM/bidirlm-embedding)

## Paper
- arxiv.org/abs/2604.02045

## Why This Matters
BidirLM democratizes access to state-of-the-art bidirectional encoders. By providing a recipe to convert any causal decoder LLM into a bidirectional encoder, it opens up a vast universe of open-source models (code specialists, math specialists, vision models, audio models) for representation tasks — previously unused GPU hours become valuable for embeddings and retrieval.
