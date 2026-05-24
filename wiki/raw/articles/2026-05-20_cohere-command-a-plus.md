# Command A+: Cohere's Open-Source Sovereign Agentic Model

**Source:** [Cohere Blog](https://cohere.com/blog/command-a-plus) | **Date:** May 20, 2026

## Overview
Command A+ is Cohere's fastest and most powerful language model, designed as an open-source enterprise workhorse for complex reasoning, multimodal, multilingual, and agentic tasks. It is Cohere's first fully Apache 2.0-licensed frontier model.

## Key Specifications
- **Architecture:** Sparse Mixture-of-Experts (MoE), 218B total / 25B active parameters
- **Context:** 128K input, 64K max generation
- **Modalities:** Text, image, tool use
- **Languages:** 48 (up from 23)
- **Hardware:** 2× H100 @ W4A4, or 1× Blackwell B200
- **Quantizations:** BF16, FP8, W4A4 (near-lossless)
- **License:** Apache 2.0 (all components — tokenizer, config, training recipes)

## Performance Highlights
- τ²-Bench Telecom: 37% → 85% (agentic task completion)
- Terminal-Bench Hard: 3% → 25%
- Agentic QA (MCP-connected cloud files): +20% accuracy
- Spreadsheet analysis: +32% quality
- Memory (cross-conversation reasoning): 39% → 54%
- Multimodal: MMMU 75.1%, MathVista 80.6%, CharXiv 52.7%
- Japanese tokenization: 18% fewer tokens vs predecessor

## Efficiency
- Output tokens/sec: up to 63% higher vs Command A Reasoning
- W4A4 quantization: additional 47% speed increase
- Speculative decoding: 1.5-1.6× inference speedup for MoE
- Time To First Token: reduced by up to 17%

## Strategic Significance
- Apache 2.0 license enables sovereign AI: enterprises and nations can run, control, and adapt the model without vendor lock-in
- Unifies five previous Command family models (general, reasoning, vision, translation, tool use) into one
- Runs on minimal hardware (2× H100s), making it practical for private deployment
- First Cohere model to support native citation generation (explicit grounding spans)
