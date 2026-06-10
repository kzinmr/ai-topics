---
title: "Introducing North Mini Code: Cohere's First Model For Developers"
source: https://huggingface.co/blog/CohereLabs/introducing-north-mini-code
date: 2026-06-09
---

# Introducing North Mini Code: Cohere's First Model For Developers

Today, we are releasing North Mini Code, a 30B-parameter Mixture-of-Experts model with 3B active parameters with powerful agentic coding capabilities, available on Hugging Face under the Apache 2.0 license.

North Mini Code is the first model in Cohere's new family of models, and is specifically designed and trained for agentic software engineering tasks.

On Artificial Analysis' Coding Index, North Mini Code achieves a score of 33.4, outperforming Qwen3.5 (35B-A3B), Gemma 4 (26B-A4B), Devstral Small 2 (24B Dense), and even substantially larger models such as Nemotron 3 Super (120B-A12B), Mistral Small 4 (119B-A6B), and Devstral 2 (123B). It ranks among the strongest open-source coding models in its size class.

## Architecture

North Mini Code is a decoder-only Transformer-based sparse Mixture-of-Experts model. It uses efficient attention implementation, interleaved between sliding-window attention with RoPE and global attention with no positional embeddings, in a 3:1 ratio. The feed-forward block is an MoE block with 128 experts, of which 8 are activated per token. Each expert block is an FFN block with SwiGLU activation. The router applies a sigmoid activation function to the logits before the top-k selection. Also uses a single dense layer before the sparse layers.

## Post-Training for Coding Excellence

Two-stage cascaded supervised fine-tuning (SFT) followed by reinforcement learning with verifiable rewards (RLVR).

- First stage SFT: code datasets 70% of trainable tokens, 43% agentic tool-use data, 27% single-turn competitive/scientific programming
- Second stage SFT: 4.5 billion token data mixture, code data 61% of trainable tokens
- Context: 64K (first SFT) → 128K (second SFT) — "long-to-longer" cascade
- Over 70k verifiable tasks across ~5k unique repositories
- Final SFT model: 80.2% pass@10 on SWE-Bench Verified, 55.1% pass@10 on Terminal-Bench v2

## Robustness Across Harnesses

Cross-harness generalization via 6% benchmark harness data in second SFT stage. 10% gain on OpenCode harness while maintaining SWE-Agent performance. 61.0% pass@1 using mini-SWE-Agent.

## Asynchronous RL for Agentic Coding

- Decoupled sampling from learning: trainer + vLLM sidecar
- Windowed FIFO queue for stragglers
- CISPO loss with token-level importance sampling correction
- Single multi-environment RL train: Terminal + SWE tasks, 512 rollouts/batch, 128K context
- RLVR improved: +7.9% Terminal-Bench v2, +3.0% SWE-Bench (absolute pass@1)
- 66.1% win rate in human evaluation vs SFT-only checkpoint

## Availability

- HuggingFace: CohereLabs/North-Mini-Code-1.0 (BF16), CohereLabs/North-Mini-Code-1.0-fp8
- Cohere API
- OpenCode integration
- License: Apache 2.0
