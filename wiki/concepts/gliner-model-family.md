---
title: GLiNER Model Family
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [model, encoder-model, small-language-model, named-entity-recognition, open-source, inference, content-moderation, pii-detection, information-retrieval]
sources:
  - https://pioneer.ai/blog/gliner-modern-named-entity-recognition
  - https://pioneer.ai/blog/gliner2
  - https://pioneer.ai/blog/gliguard-16x-faster-safety-moderation-with-a-small-language-model
  - https://pioneer.ai/blog/gliner2-pii-open-source-privacy-filtering-with-pii-detection
  - https://arxiv.org/abs/2311.08526
  - https://arxiv.org/abs/2507.18546
  - https://arxiv.org/abs/2605.07982
  - https://arxiv.org/abs/2605.09973
---

# GLiNER Model Family

**GLiNER** (Generalist Language model for Named Entity Recognition) is a **bidirectional encoder-based Small Language Model family** developed by [[entities/fastino-labs]]. It began with zero-shot Named Entity Recognition (NER) and has expanded into information extraction, safety moderation, and PII detection.

## Architecture Innovation

GLiNER's core innovation is **redefining NER as a matching task rather than a generation task**.

### Traditional Approach (Decoder Models)

Large generative models such as GPT-5 and Claude process NER as autoregressive token generation:
- Sequential processing of input text one token at a time
- High latency, high cost, API-dependent
- Overhead of solving classification problems through text generation

### GLiNER's Approach (Bidirectional Encoder)

- **Bidirectional Processing**: Builds representations using context from both before and after each token
- **Matching Paradigm**: Projects input text and target labels into a shared latent space and computes similarity scores
- **Zero-shot**: Can recognize new entity classes without additional training
- **Single-pass Processing**: Executes all tasks in parallel in a single forward pass

> "GLiNER's innovation lies in both its return to a bidirectional encoder architecture and its treatment of NER as a matching algorithm."

## Model Family

### GLiNER (v1) — Zero-shot NER

| Property | Description |
|---|---|
| **Paper** | arXiv:2311.08526 (November 2023) |
| **Parameters** | 50M (Small) ~ 205M (Large) |
| **Architecture** | BERT-based bidirectional encoder |
| **Key Function** | Zero-shot NER |
| **GitHub** | https://github.com/urchade/GLiNER |

**Benchmark Results:**
- GLiNER-Medium (90M): Performance comparable to UniNER-13B (**140x smaller**)
- GLiNER-Small (50M): Surpasses ChatGPT, Vicuna, and InstructUIE-11B in zero-shot NER
- Even multilingual adaptation trained only on English outperforms ChatGPT in many languages

**Contradicting Scaling Laws:**
> "GLiNER directly contradicts [scaling laws] by matching and even outperforming models many times larger."

### GLiNER2 — Multi-task Information Extraction

| Property | Description |
|---|---|
| **Paper** | arXiv:2507.18546 (2025) |
| **Parameters** | 205M |
| **Architecture** | Bidirectional encoder + schema-driven interface |
| **Key Function** | NER, Relation Extraction, JSON Extraction, Text Classification (4 tasks in a single pass) |
| **GitHub** | https://github.com/fastinoai/GLiNER2 |

**Extensions from GLiNER:**

While GLiNER v1 handled only NER, GLiNER2 expanded to 4 tasks in response to the demands of the agent era:

1. **NER (Named Entity Recognition)**: Identification and classification of entities such as people, places, and organizations
2. **Relation Extraction**: Identification of semantic connections and dependencies between entities
3. **Structured Data Extraction (JSON Extraction)**: Converting text to JSON format based on a schema
4. **Text Classification**: Assigning categories/labels to text segments

**Architectural Advantages:**
- **Schema-driven**: Executes 4 tasks simultaneously via a declarative schema interface
- **Deterministic Accuracy**: No hallucinations since it is not a generative model
- **Reliable Structured Output**: Output format is predefined by schema
- **CPU-first**: No GPU required, inference under 100ms

**Fine-tuning Characteristics:**
- **Can be fine-tuned within 3 minutes with 10 additional examples**
- Easy domain specialization; data with high privacy requirements can be processed locally

**Use Cases:**
- Prompt hack detection
- Hallucination detection
- Guardrails
- Model routing (model selection based on task complexity)

### GLiGuard — Safety Moderation

| Property | Description |
|---|---|
| **Paper** | arXiv:2605.07982 (May 2026) |
| **Parameters** | 300M |
| **Base** | Full fine-tune of GLiNER2-base-v1 |
| **Key Function** | Simultaneous evaluation of 4 safety tasks in a single pass |
| **License** | Apache 2.0 |
| **HuggingFace** | https://huggingface.co/fastino/gliguard-LLMGuardrails-300M |

**4 Safety Tasks:**

1. **Safety Classification** (safe/unsafe): Applied to both user input and model output
2. **Jailbreak Strategy Detection** (11 strategies): Prompt injection, role-play bypass, instruction override, social engineering, etc.
3. **Harm Category Detection** (14 categories): Violence, sexual content, hate speech, PII exposure, misinformation, child safety, copyright infringement, etc.
4. **Refusal Detection** (compliance/refusal): Tracks whether the model refused or complied with a request (also used for detecting excessive refusal)

**Benchmark Results:**

| Metric | Result |
|---|---|
| Prompt Classification Avg F1 | 87.7 (Best: PolyGuard-Qwen 89.4) |
| Response Classification Avg F1 | 82.7 (Best: Qwen3Guard-8B 84.1) |
| Throughput | **Up to 16.2x faster** than current SOTA (133 vs 8.2 samples/s) |
| Latency | **Up to 16.6x lower latency** than current SOTA (26ms vs 426ms) |

**Comparison Models (all 23-90x larger than GLiGuard):**
- LlamaGuard4 (12B)
- WildGuard (7B)
- ShieldGemma (27B)
- NemoGuard (8B)
- PolyGuard (7B)
- Qwen3Guard (8B)

**Training Data:**
- WildGuardTrain (87,000 annotated examples)
- Label generation via GPT-4.1 (unsafe samples)
- Synthetic data complement for edge cases by Pioneer

### GLiNER2-PII — PII Detection & Privacy Filtering

| Property | Description |
|---|---|
| **Paper** | arXiv:2605.09973 (May 2026) |
| **Parameters** | 300M |
| **Base** | Fine-tune of GLiNER2 |
| **Key Function** | Detection and masking of 42 PII entity types |
| **License** | Apache 2.0 |
| **HuggingFace** | https://huggingface.co/fastino/gliner2-privacy-filter-PII-multi |

**42 PII Entity Types (7 Categories):**

| Category | Entity Examples |
|---|---|
| Personal Identification | person, full name, date of birth |
| Contact / Location | email, phone, address, postal code |
| Government / Tax ID | passport number, driver's license, tax ID |
| Banking / Payment | bank account, IBAN, card number, CVV |
| Digital ID | username, IP address, account ID |
| Secrets / Credentials | password, API key, access token |
| Sensitive Dates | sensitive date, expiration date |

**SPY Benchmark Results:**

| Model | Avg F1 | Recall (Legal) | Recall (Medical) |
|---|---|---|---|
| **GLiNER2-PII** | **0.471** | **0.722** | **0.681** |
| NVIDIA GLiNER PII | 0.391 | — | — |
| urchade | 0.384 | — | — |
| OpenAI Privacy Filter | 0.373 | 0.640 | 0.671 |
| Knowledgator | 0.368 | — | — |

**Comparison with OpenAI Privacy Filter:**
- OpenAI: 1.5B parameter decoder, 8 fixed entity types, schema not modifiable
- GLiNER2-PII: 300M parameter encoder, 42 types, schema customizable at inference time
- **5x+ label coverage** achieved with a fraction of the memory footprint

**Training Data Innovation:**
- Real PII data is inherently impossible to collect, share, and annotate
- Pioneer's synthetic data generation pipeline produced **4,910 high-quality annotated examples**
- 7 languages, diverse document formats (chat logs, support tickets, CRM notes, KYC forms, invoices, medical records)
- Despite training solely on synthetic data, generalizes to unseen natural text

## GLiNER Ecosystem

The GLiNER architecture has influenced others beyond Fastino Labs, with several derivative models being developed:

### GLiClass (Knowledgator) — Classification-specialized Derivative
→ See [[concepts/gliclass]] for details

A model family developed by **Knowledgator** by adapting the GLiNER architecture to classification tasks. It applies NER's "matching" paradigm to text classification, achieving inference up to 50x faster than Cross-Encoders.

| Model | Parameters | Primary Use |
|---|---|---|
| GLiClass-V3 | 32M-439M | Zero-shot classification (DeBERTa/ModernBERT/Ettin) |
| GLiClass-Instruct | 32M-400M | Multi-task instruction-following classification |
| GLiClass-Multilang | 140M-720M | 20-language support, cross-lingual classification |

**Relationship with GLiNER2**: GLiClass and GLiNER2 represent **parallel evolution** from GLiNER (v1). While GLiNER2 aimed for integration of NER+Relation Extraction+JSON+Classification by Fastino, GLiClass was developed by Knowledgator specializing in classification tasks, deepening hierarchical labels, few-shot learning, and multilingual support. Both share the philosophy of "solving classification problems with bidirectional encoders" while evolving in different optimization directions.

### Other Community Derivatives

| Project | Developer | Use Case |
|---|---|---|
| [GLiNER-PII](https://huggingface.co/nvidia/gliner-PII) | NVIDIA | PII Detection |
| [Gretel GLiNER](https://huggingface.co/gretelai/gretel-gliner-bi-large-v1.0) | Gretel AI | PII Detection |
| [GLiNER-BioMed](https://huggingface.co/collections/knowledgator/gliner-biomed) | Knowledgator | Biomedical entity extraction |
| GLiNER-Multi-PII | urchade | Multilingual PII detection |

## Production Usage Patterns

GLiNER models can be inferred via the [[entities/pioneer-ai]] platform. They are designed for use in agent architectures such as:

```
User Input
    ↓
[GLiGuard] ── Safety check (safe/unsafe, jailbreak detection)
    ↓
[GLiNER2-PII] ── PII detection & masking
    ↓
[GLiNER2] ── Intent classification & routing
    ↓
[Frontier LLM] ── Complex reasoning & planning (only when needed)
    ↓
[GLiNER2] ── Output structuring & validation
```

## Technical Significance

The GLiNER family embodies the following trends in the AI industry:

1. **Relativization of Scaling Laws**: Performance comparable to models hundreds of times larger through specialized architecture + task specialization
2. **The Era of SLM Advantage**: The primary building blocks of production AI are specialized SLMs, not frontier LLMs
3. **Revival of Encoders**: Bidirectional encoders specialized for understanding and classification tasks, as a counter to generative model universalism
4. **Utility of Synthetic Data**: Use of synthetic data in domains where real data is constrained (PII, safety)

## Related Pages

- [[entities/fastino-labs]] — Developer
- [[entities/pioneer-ai]] — Fine-tuning & inference platform
- [[concepts/gliclass]] — Classification-specialized derivative of GLiNER architecture (developed by Knowledgator)
- [[concepts/continual-learning]] — Continual learning (theoretical foundation of Adaptive Inference)
