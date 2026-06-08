---
title: Llama 3
created: 2026-05-19
updated: 2026-05-19
type: entity
tags:
  - model
  - text-generation
  - open-source
  - methodology
  - training
  - alignment
  - multimodal
  - vlm
  - voice-ai
  - optimization
  - fine-tuning
  - benchmark
  - evaluation
  - agent-safety
  - tool
aliases: [Llama 3.1, Llama 3 Herd of Models]
sources:
  - raw/papers/2024-07-23_2407.21783_llama-3-herd-of-models.md
related:
  - concepts/llm-development-paradigm.md
---

# Llama 3

**Llama 3** is an open-source foundational language model family developed by Meta. The 8B/70B models launched in April 2024, with the full version (Llama 3.1) released in July 2024 offering **8B / 70B / 405B** sizes with multilingual support, long context (128K), and tool-use Instruct models.

Its defining feature is achieving GPT-4-comparable performance with a **dense Transformer** at 405B parameters (no MoE), while establishing the two-phase development paradigm of **Pre-training -> Post-training (SFT + Rejection Sampling + DPO)**, becoming a landmark in 2024 LLM development.

## Model Family

| Model | Parameters | Multilingual | 128K Context | Tool Use | Release |
|--------|-----------|---------------|-------------------|-----------|----------|
| Llama 3 8B | 8B | — | — | — | 2024-04 |
| Llama 3 8B Instruct | 8B | — | — | — | 2024-04 |
| Llama 3 70B | 70B | — | — | — | 2024-04 |
| Llama 3 70B Instruct | 70B | — | — | — | 2024-04 |
| **Llama 3.1 8B** | 8B | ✓ | ✓ | ✓ (Instruct) | 2024-07 |
| **Llama 3.1 70B** | 70B | ✓ | ✓ | ✓ (Instruct) | 2024-07 |
| **Llama 3.1 405B** | 405B | ✓ | ✓ | ✓ (Instruct) | 2024-07 |

All paper references refer to Llama 3.1. The April release is primarily English-only; the July release is the full version.

## Key Benchmarks

| Category | Benchmark | Llama 3 405B | GPT-4 (0125) | GPT-4o | Claude 3.5 Sonnet |
|----------|-------------|-------------|-------------|--------|-------------------|
| General Knowledge | MMLU (5-shot) | **87.3** | 85.1 | 89.1 | 89.9 |
| Code | HumanEval (0-shot) | 89.0 | 86.6 | 90.2 | 92.0 |
| Math | GSM8K (8-shot, CoT) | **96.8** | 94.2 | 96.1 | 96.4 |
| Reasoning | ARC Challenge (0-shot) | **96.9** | 96.4 | 96.7 | 96.7 |
| Tool Use | BFCL | 88.5 | 86.5 | 80.5 | 90.2 |
| Long Context | ZeroSCROLLS/QuALITY | **95.2** | 95.2 | 90.5 | 90.5 |
| Multilingual | MGSM (0-shot, CoT) | **91.6** | 85.9 | 90.5 | 91.6 |

**First open-source model to surpass GPT-4**. It exceeded GPT-4 (0125) on MMLU, GSM8K, ARC Challenge, and MGSM.

## Development Paradigm

Llama 3 established the **two-phase development paradigm** (-> [[concepts/llm-development-paradigm]]):

### Phase 1: Pre-training
- **Data**: 15.6T tokens (8.7x Llama 2 at 1.8T). Multilingual web data
- **Data Mix**: General knowledge ~50%, Math/Reasoning 25%, Code 17%, Multilingual 8% - optimized via scaling laws
- **Architecture**: Dense Transformer (no MoE). GQA (8 KV-heads), RoPE (theta=500,000), vocabulary 128K
- **Compute**: 3.8 x 10^25 FLOPs (~50x Llama 2)
- **Infrastructure**: Up to 16K H100 GPUs, 4D parallelism. 466 job interruptions in 54 days (78% hardware-related)
- **Effective Training Time**: 38.5 days

### Phase 2: Post-training
1. **Reward Model**: Trained on human preference data (with safety pre-training)
2. **SFT**: Supervised fine-tuning on high-quality human and synthetic data
3. **Rejection Sampling (RS)**: Generate K outputs per prompt, select best via RM for training
4. **DPO**: Direct Preference Optimization from preference pairs
5. **Final Averaging**: Weight averaging of RM-selected checkpoint ensembles

**Design Philosophy**: No online RL like PPO - only SFT + DPO. Prioritizing simplicity.

### Phase 3 (Experimental, Unreleased): Multimodal Expansion
- Image encoder (ViT-H/14) + cross-attention adapter for vision
- Video adapter (temporal aggregator + cross-attention)
- Audio encoder + adapter for speech input
- Language model frozen; only adapters trained

## Data Pipeline Innovations

### Web Data Curation
- **PII & Safety Filtering**: Remove harmful domains
- **Deduplication**: URL-level, document-level (MinHash), line-level (remove lines appearing 6+ times in 30M documents)
- **Heuristic Filtering**: n-gram overlap rate, dirty word count, token distribution KL divergence
- **Model-based Quality Filtering**: fasttext + DistilRoberta (trained on Llama 2 judgments)
- **Code & Reasoning Data**: Dedicated pipeline to identify math/STEM/code pages

### Annealing Data
- Annealing with small-scale high-quality code & math data is effective
- 8B: GSM8K +24%, MATH +6.4% improvement
- 405B: smaller effect (already has strong in-context learning)

## Safety

- **Llama Guard 3**: Safeguard LLM for input/output safety (public)
- **Llama Code Shield**: Safety filter for generated code
- **Red Teaming**: CBRN, cyber, child safety experts + automated testing
- **CyberSecEval 2**: Cybersecurity risk evaluation suite
- Safety fine-tuning integrated into post-training pipeline (SFT + DPO)

## Key Findings

1. **Frontier performance with dense Transformer**: Surpassing GPT-4 with 405B dense model (no MoE)
2. **Data quality > quantity in post-training**: Quality matters for SFT; quantity also helps for DPO
3. **Synthetic data effectiveness**: Especially effective for code & reasoning tasks; limited for knowledge-intensive tasks
4. **Data mix optimization via scaling laws**: Evaluated trade-offs between general knowledge, math, code, and multilingual on small models, then extrapolated to large scale
5. **Frontier training reliability**: 466 interruptions over 54 days - valuable data on large-scale training operations

## Historical Significance

Why the Llama 3 paper is a 2024 landmark in LLM development:

- **Open-source frontier achieved**: Demonstrated that open models can match GPT-4 quality
- **Standardized development paradigm**: Two-phase pipeline of pre-training -> SFT + RS + DPO established as industry standard
- **Data engineering importance**: Systematically showed that data quality and composition matters more than model architecture
- **Multimodal expansion blueprint**: Demonstrated adding modalities via adapters while freezing the language model

## References

- [[concepts/llm-development-paradigm]] - Two-phase development paradigm
- [[concepts/scaling-laws]] - Scaling laws
- [[entities/meta]] — Meta AI
- Paper: [arXiv:2407.21783](https://arxiv.org/abs/2407.21783)
- License: Llama 3 Community License (updated)
