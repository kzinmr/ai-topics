---
title: ZAYA1-8B
created: 2026-05-16
updated: 2026-05-16
type: concept
tags: [model, open-source, amd, mixture-of-experts, reasoning, inference, training]
sources: [raw/articles/zyphra.com--zaya1-8b-moe-amd-reasoning--2026-05-16.md]
---

# ZAYA1-8B

**ZAYA1-8B** is a reasoning-focused mixture-of-experts (MoE) language model by [[entities/zyphra]], released May 6, 2026. With 8.4B total parameters and only 760M active parameters per inference pass, it achieves frontier-competitive performance at a fraction of the compute cost. Trained end-to-end on AMD Instinct MI300X hardware.

## Performance

With under 1 billion active parameters, ZAYA1-8B punches far above its weight class:

| Benchmark | ZAYA1-8B | Comparison |
|-----------|----------|------------|
| HMMT'25 (w/ Markovian-RSA) | 89.6 | GPT-5-High: 88.3 |
| Mathematics (AIME) | Competitive | Close to DeepSeek-R1-0528 |
| Coding (LiveCodeBench) | Strong | Exceeds Mistral-Small-4-119B |
| GPQA-Diamond | Competitive | Near Gemini-2.5-Pro |
| IFEval / IFBench | Strong | Competitive instruction following |

Matches or exceeds: Nemotron-3-Nano-30B-A3B, Mistral-Small-4-119B. Competitive with: DeepSeek-R1-0528, Gemini-2.5-Pro, Claude 4.5 Sonnet.

## Architecture

- **MoE++**: Zyphra's proprietary mixture-of-experts design
- **Active/total**: 760M / 8.4B parameters
- **Training hardware**: 1,024 AMD Instinct MI300X nodes with AMD Pensando Pollara interconnect, on IBM Cloud
- **First**: First MoE model pretrained, midtrained, and SFT'd entirely on AMD hardware

## Technical Innovations

### Reasoning from Scratch
Reasoning data included from pretraining onward using answer-preserving trimming — the model learns reasoning patterns natively rather than via post-training only.

### Markovian-RSA
A novel test-time compute methodology. At inference time, this technique achieves additional performance gains — exceeding GPT-5-High on HMMT'25 (89.6 vs 88.3).

### AMD-Native Training Stack
The full training pipeline ran on AMD hardware, demonstrating that non-NVIDIA infrastructure can train competitive frontier models. This has significant implications for the GPU supply chain and hardware diversity in AI.

## Availability

- **License**: Apache 2.0
- **Weights**: Hugging Face (zyphra/ZAYA1-8B)
- **API**: Free serverless endpoint on Zyphra Cloud
- **arXiv**: 2605.05365

## ZAYA1-VL-8B (May 14, 2026)

Zyphra subsequently released a vision-language variant with 700M active parameters, outperforming Deepseek-VL2, Qwen3-VL, and MolmoE on visual understanding tasks. Uses bidirectional attention for image tokens and vision-specific LoRA parameters. Apache 2.0 license.

## See Also

- [[entities/zyphra]]
- [[concepts/mixture-of-experts]]
- [[entities/amd]]
- [[concepts/inference]]
- [[concepts/intelligence-density]]
