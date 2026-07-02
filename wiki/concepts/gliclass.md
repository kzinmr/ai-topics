---
title: "GLiClass"
type: concept
created: 2026-05-01
updated: 2026-07-02
tags:
  - optimization
  - open-source
  - model
aliases: ["GLiClass-V3", "GLiClass-Instruct", "GLiClass-Multilang", "gliclass"]
sources:
  - https://arxiv.org/abs/2508.07662
  - https://huggingface.co/collections/knowledgator/gliclass-v3
  - https://huggingface.co/collections/knowledgator/gliclass-instruct
  - https://huggingface.co/collections/knowledgator/gliclass-multilang
  - https://github.com/Knowledgator/GLiClass
  - https://medium.com/@knowledgrator/pushing-zero-shot-classification-to-the-limit-696a2403032f
status: L3
---

# GLiClass

**GLiClass** (Generalist Lightweight Model for Sequence Classification) is an encoder-only zero-shot text classification model family developed by [Knowledgator](https://knowledgator.com) Engineering. It adapts the GLiNER (Generalist Lightweight Named Entity Recognition) architecture for classification tasks, achieving **up to 50x faster** inference while maintaining accuracy comparable to or exceeding Cross-Encoders.

Foundation paper: [arXiv:2508.07662](https://arxiv.org/abs/2508.07662) (published August 2025), License: Apache-2.0.

## Architecture Core

### Single Forward-Pass Classification

Traditional Cross-Encoder (NLI-based) classification requires N forward passes for N labels. GLiClass handles this in a **single forward pass**:

1. Mark labels with `<<LABEL>>` special tokens and concatenate with input text
2. Process inter-label and text-label interactions simultaneously using a bidirectional Transformer (DeBERTa / ModernBERT / Ettin)
3. Compute scores for each label via a pooling mechanism (CLS / average / max, etc.)
4. Evaluate text-label alignment using a dot-product or neural network-based scorer

### Three Architecture Types

- **uni-encoder** (default): Processes text and labels with the same encoder, maximum efficiency
- **bi-encoder**: Processes text and labels with separate encoders
- **bi-encoder-fused**: bi-encoder with label embeddings fused into the text side
- **encoder-decoder**: For sequence transformation tasks

### Scorer & Pooling Strategies

| Component | Options |
|---|---|
| Scorer | `simple` (dot product), `weighted-dot`, `mlp`, `hopfield` |
| Pooling | `first` (CLS), `avg`, `max`, `last`, `sum`, `rms`, `abs_max`, `abs_avg` |
| Flash Attention | FlashDeBERTa (DeBERTa v2), TurboT5 (T5/mT5) support |

## Model Family Overview

GLiClass consists of three sub-families:

### 1. GLiClass-V3 (V3.0 Series)

The core variant. Specialized for zero-shot classification with DeBERTa-v3 / ModernBERT / Ettin backbones. **Released August 2025**.

| Model | Parameters | Size | Avg F1 | Inference Speed (ex/s) | Backbone |
|---|---|---|---|---|---|
| **gliclass-edge-v3.0** | 32.7M | 131 MB | 0.4873 | 97.29 | Ettin |
| gliclass-modern-base-v3.0 | 151M | 606 MB | 0.5571 | 54.46 | ModernBERT |
| gliclass-modern-large-v3.0 | 399M | 1.6 GB | 0.6082 | 43.80 | ModernBERT |
| **gliclass-base-v3.0** | 187M | 746 MB | **0.6556** | 51.61 | DeBERTa-v3 |
| **gliclass-large-v3.0** | 439M | 1.75 GB | **0.7001** | 25.22 | DeBERTa-v3 |
| gliclass-x-base | 0.3B | — | 0.5778 (EN) / 0.418 (multilingual) | — | mDeBERTa-v3 |

**Inference Speed Characteristics**: While Cross-Encoder slows linearly with increasing label count (DeBERTa-v3-Large: 0.25 ex/s at 128 labels), GLiClass-V3 maintains nearly constant speed regardless of label count (base-v3.0: 45.94 ex/s at 128 labels).

### 2. GLiClass-Instruct (V1.0 Series)

A variant specialized for multi-task instruction following. **Released February 2026**. Features the same advanced capabilities as V3 (hierarchical labels, few-shot examples, label descriptions, task prompts), optimized for instruction-following.

| Model | Parameters | Avg F1 | Features |
|---|---|---|---|
| gliclass-instruct-edge-v1.0 | 32.7M | 0.4922 | Lightest for edge |
| gliclass-instruct-base-v1.0 | 0.2B | 0.6525 | Balance of speed and accuracy |
| **gliclass-instruct-large-v1.0** | **0.4B** | **0.7199** | Highest accuracy |

**Key Benchmarks (large-v1.0, zero-shot F1)**:
| Dataset | large-v1.0 | base-v1.0 | edge-v1.0 |
|---|---|---|---|
| IMDB | 0.9397 | 0.9364 | 0.8159 |
| SST2 | 0.9154 | 0.9198 | 0.7577 |
| CR | 0.9066 | 0.8922 | 0.7933 |
| Spam | 0.9790 | 0.9380 | 0.7609 |
| Snips | 0.8509 | 0.6515 | 0.5461 |
| **AVERAGE** | **0.7199** | **0.6525** | **0.4922** |

### 3. GLiClass-Multilang (Multilingual Series)

A multilingual variant with native support for **20 languages**. **Released April 2026**. Features a newly developed **CrossAttn Scorer** (efficient per-label pooling via Flash-Attention + unpadding). Supports **cross-lingual classification** (e.g., classifying French text with English labels).

| Model | Parameters | English Avg F1 | Multilingual Avg F1 | Throughput (samp/s) |
|---|---|---|---|---|
| gliclass-multilang-edge | ~140M | 0.6196 | 0.3959 | 553.6 |
| **gliclass-multilang-mini** | **~288M** | **0.6827** | **0.5378** | **513.4** |
| **gliclass-multilang-ultra** | **~720M** | **0.7212** | **0.5599** | **200.7** |

**Supported Languages**: Swedish, Norwegian, Czech, Polish, Spanish, German, French, Ukrainian, Hindi, Chinese, Arabic, Hebrew, and more.

**Cross-Encoder Comparison** (throughput vs label count):
| Model | 1 Labels | 8 Labels | 64 Labels | 256 Labels |
|---|---|---|---|---|
| multilang-ultra | 308.2 | 266.3 | 125.2 | 31.5 |
| bge-m3-zeroshot | 940.0 | 112.9 | 14.4 | 3.7 |

## V3 New Features (Common Across All Families)

Advanced control features introduced in the GLiClass V3 generation:

### Hierarchical Labels
```python
hierarchical_labels = {
    "science": ["space", "biology", "physics"],
    "society": ["politics", "economics", "culture"]
}
# → results: science.space => 0.95
```

### Few-Shot Learning
```python
examples = [
    {"text": "Wake me up at 6:30.", "labels": ["set_alarm"]},
    {"text": "Play some jazz.", "labels": ["play_music"]},
]
results = pipeline(text, labels, examples=examples, threshold=0.5)[0]
```

### Label Descriptions
Define label meanings in natural language to improve accuracy. Example: `"spam": "Unsolicited commercial messages"`.

### Task Prompts
Custom instructions prepended to the input. Example: `"Classify the sentiment of this review:"`.

### Long Document Chunking
Automatically chunk long documents up to 8K tokens with `ZeroShotClassificationWithChunkingPipeline`.

## Training Methods

### LoRA Fine-Tuning
- **V3 Base/Large**: LoRA r=384, α=768, target modules = query_proj, key_proj, value_proj, dense, linear_1, linear_2, mlp layers
- **Modern Large V3.0**: LoRA r=768, α=1536
- **Focus Loss**: α=0.7

### Training Datasets
- `tau/commonsense_qa`
- `knowledgator/gliclass-v3-logic-dataset`
- `BioMike/formal-logic-reasoning-gliclass-2k`

### Multi-Label PPO
One of the paper's key contributions: the first adaptation of **Proximal Policy Optimization (PPO)** for multi-label text classification. Enables effective training under data scarcity and allows incorporation of human preferences / logical constraints.

## Retrieval-Augmented Classification (RAC)

An inference-time augmentation technique inspired by RAG. An **optional feature** of the GLiClass pipeline:

### How It Works
1. Encode the `gliclass-v2.0` dataset with Sentence Transformer (paraphrase-MiniLM-L6-v2)
2. Index into an HNSW database
3. At inference, retrieve 1–3 similar examples with cosine similarity > 0.5
4. Format with `<<EXAMPLE>>` / `<<TRUE_LABEL>>` / `<<FALSE_LABEL>>` tokens
5. During training, inject 30% noise (replace with irrelevant text) for robustness

### Impact
- **With 1 example: F1 0.3090 → 0.4275** (+38%), extreme cases 0.2594 → 0.6249 (+141%)
- **With 2 examples: F1 0.4707** (approaching 0.4838 of 8-shot Few-Shot)
- Achieves near-Few-Shot performance without labeled data

## Comparison: GLiClass vs Traditional Methods

| Aspect | GLiClass | Cross-Encoders | LLM | Embedding Models |
|---|---|---|---|---|
| **Label Count Scaling** | Sub-linear (7-20% drop 1→128 labels) | Linear decay (50x slowdown) | Prompt length increase | Constant time (fast) |
| **Zero-Shot Ability** | Strong (F1 0.49–0.72) | Strong | Strong but unstable | Moderate |
| **Single Pass** | ✅ 1 pass | ❌ N passes | ❌ Generative | ✅ Encoding only |
| **Inference Cost** | Low (GPU optional) | Medium-High | High | Low |
| **Hierarchical Labels** | ✅ Native | ❌ | Prompt-dependent | ❌ |

Evaluations in the GLiNER2 (July 2025 paper) also show GLiClass demonstrating competitive accuracy as an open-source model, outpacing DeBERTa-v3 particularly in tasks like Banking77 (intent classification).

## Use Cases

1. **RAG Pipeline Re-ranker**: Reduce latency as an alternative to Cross-Encoders
2. **Content Filtering**: Primary filtering of large text corpora (topic, sentiment, spam)
3. **Intent Classification**: Routing for chatbots and agents
4. **NLI**: Entailment relationship judgment
5. **Hallucination Detection**: Classify hallucinated/correct by inputting context+question+answer concatenation
6. **LLM Safety Classification**: Detect prompt injection, jailbreaks, and harmful content
7. **Compliance Verification**: Auto-check adherence to guidelines
8. **Edge Devices / On-Device NLP**: Privacy-safe with 32.7M parameter edge model

## Related Resources

- **GitHub**: [Knowledgator/GLiClass](https://github.com/Knowledgator/GLiClass)
- **Docs**: [docs.knowledgator.com/docs/frameworks/gliclass/](https://docs.knowledgator.com/docs/frameworks/gliclass/)
- **Demo**: [GLiClass SandBox](https://huggingface.co/spaces/knowledgator/GLiClass_SandBox)
- **Discord**: [knowledgator Discord](https://discord.gg/dkyeAgs9DG)
- **Blog**: [Pushing Zero-Shot Classification to the Limit](https://medium.com/@knowledgrator/pushing-zero-shot-classification-to-the-limit-696a2403032f)
- **Colab**: [Fine-tuning Notebook](https://colab.research.google.com/github/Knowledgator/GLiClass/blob/main/finetuning.ipynb)
- **Install**: `pip install gliclass`

## Related Concepts
- [[concepts/gliner-model-family]] — GLiNER/GLiNER2/GLiGuard/GLiNER2-PII; GLiClassはGLiNERアーキテクチャの分類特化派生
- [[concepts/rag-retrieval-augmented-generation]]
- [[entities/gm8xx8]] — Curator
- [[entities/knowledgator]] — GLiClass開発元
