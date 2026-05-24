---
title: Command A+
created: 2026-05-24
updated: 2026-05-24
type: entity
tags: [model, multimodal, moe, open-source, company, cohere, inference, quantization, enterprise-ai, agentic-engineering]
sources: [raw/articles/2026-05-20_cohere-command-a-plus.md]
---

# Command A+

Command A+ is Cohere's most powerful language model, released May 20, 2026 as the company's first fully Apache 2.0-licensed frontier model. It is a 218B-parameter Sparse Mixture-of-Experts (MoE) model with 25B active parameters, designed for complex reasoning, multimodal document processing, multilingual tasks, and agentic workflows.

## Key Specifications

| Feature | Detail |
|---------|--------|
| Architecture | Sparse MoE, 218B total / 25B active |
| Context | 128K input, 64K max generation |
| Modalities | Text, image, tool use |
| Languages | 48 (up from 23 in Command A) |
| Minimum Hardware | 2× H100 @ W4A4, or 1× Blackwell B200 |
| Quantizations | BF16, FP8, W4A4 (near-lossless) |
| License | Apache 2.0 (all components) |

## Performance

Command A+ consolidates five previous Command family models (general, reasoning, vision, translation, tool use) into a single unified system, delivering significant gains:

- **τ²-Bench Telecom:** 37% → 85% (agentic task completion)
- **Terminal-Bench Hard:** 3% → 25%
- **Agentic QA (MCP-connected):** +20% accuracy
- **Spreadsheet analysis:** +32% quality
- **Cross-conversation memory:** 39% → 54%
- **MMMU (multimodal):** 75.1% (vs 65.3% for dedicated vision model)
- **MathVista:** 80.6%

## Efficiency

- Output tokens/sec: up to 63% higher vs Command A Reasoning
- W4A4 quantization: additional 47% speed increase
- Speculative decoding: 1.5-1.6× for MoE architecture
- Tokenizer improvements: 18% fewer tokens for Japanese, 20% for Arabic, 16% for Korean

## Sovereign AI Thesis

Command A+ embodies Cohere's "sovereign AI" strategy: enterprises and nations can run, control, and adapt a frontier-grade model entirely within their own infrastructure. The full Apache 2.0 license covers not just weights but all components (tokenizer, config, training recipes), enabling unrestricted commercial and government use.

## Related Pages

- [[entities/cohere]] — Cohere company
- [[concepts/mixture-of-experts]] — MoE architecture
- [[concepts/quantization]] — W4A4 quantization techniques
- [[entities/command-a]] — predecessor Command A family
- [[concepts/sovereign-ai]] — sovereign AI concept
