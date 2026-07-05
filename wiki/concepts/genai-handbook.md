---
title: "GenAI Handbook (William Brown)"
type: concept
created: 2026-05-04
updated: 2026-05-04
status: Level2
tags:
  - curriculum
  - methodology
  - education
  - model
aliases: [willccbb-handbook, genai-roadmap]
sources:
  - https://genai-handbook.github.io
  - https://github.com/genai-handbook/genai-handbook.github.io
  - raw/articles/2026-05-04_genai-handbook.md
---

# GenAI Handbook (William Brown)

**William Brown ([@willccbb](https://x.com/willccbb))** created this **knowledge map** for GenAI learning resources in June 2024. It is not a standalone technical concept, but rather a **resource roadmap** for learning Generative AI as a whole, organizing scattered excellent explanatory resources (blogs, videos, papers) into a textbook-style structure.

> **This is meta-knowledge (a knowledge map).** The handbook itself is not the source of knowledge, but a navigation tool that guides you to "where to find what." Refer directly to the linked resources for the actual content.
>
> **Note:** This handbook dates from June 2024 and is approximately 2 years old. In particular, Section V (Agents, DSPy) and Section VI (vLLM, llama.cpp) have evolved significantly, so cross-referencing with the latest information is necessary.

---

## 🛠️ Overall Structure

The GenAI Handbook consists of 9 sections:

```text
Section I:   Foundations of Sequential Prediction (prerequisites)
    ↓
Section II:  Neural Sequential Prediction (Neural Networks → Transformers)
    ↓
Section III: Foundations for Modern LM (Tokenization, MoE, Scaling Laws)
    ↓
Section IV:  Finetuning Methods (LoRA, RLHF, DPO)
    ↓
Section V:   Evaluations & Applications (Benchmarks, RAG, Agents)
    ↓
Section VI:  Performance Optimization (Quantization, FlashAttention, vLLM)
    ↓
Section VII: Sub-Quadratic Context Scaling (SSM, Mamba, RWKV)
    ↓
Section VIII: Generative Modeling Beyond Text (GANs, Diffusion Models)
    ↓
Section IX:  Multimodal Models (VLM, VQ-VAE)
```

**Bloggers/educators featured in the handbook:**
- **Andrej Karpathy** (GPT from scratch, tokenization, backpropagation)
- **Lilian Weng** (RL, agents, diffusion, prompting, GANs)
- **3Blue1Brown** (calculus, linear algebra, neural network visualizations)
- **Chip Huyen** (RLHF, LLM engineering, multimodal)
- **Sebastian Raschka** (practical LoRA, model evaluation)
- **Tim Dettmers** (quantization, LLM.int8())
- **Neel Nanda** (introduction to mechanistic interpretability)
- **Jay Alammar** (Transformer, Word2Vec visualizations)
- **StatQuest** (basic stats/ML video series)
- **Maxime Labonne** (LLM Course companion)

---

## 🧩 Wiki Coverage Mapping

### Section I: Foundations of Sequential Prediction

**Coverage rate:** ~5% (prerequisite knowledge that is outside Wiki scope)

| Topic | Wiki Coverage | Notes |
|-------|-------------|------|
| Calculus/Linear Algebra (3Blue1Brown) | — | Outside Wiki scope (programming/engineering prerequisites) |
| Supervised Learning | — | Same as above |
| Time Series Analysis / ARIMA | — | Same as above |
| Online Learning / Regret Minimization | — | Same as above |
| Reinforcement Learning (MDP, Policy) | [[concepts/post-training/reinforcement-learning]] | "Classic" RL fundamentals (Sutton & Barto) are covered, but in a different context from LLM alignment RL |
| Markov Models | — | Same as above |

**Resource Evaluation:** This section aims to organize prerequisite knowledge. Lilian Weng's [RL Overview](https://lilianweng.github.io/posts/2018-02-19-rl-overview/) remains an excellent introductory article. Sutton & Barto's textbook is a classic but doesn't directly connect to LLM alignment.

---

### Section II: Neural Sequential Prediction

**Coverage rate:** ~20%

| Topic | Wiki Coverage | Notes |
|-------|-------------|------|
| Neural Network Basics | [[concepts/deep-learning]] | High-level coverage only |
| RNNs | — | Missing |
| LSTMs / GRUs | — | Missing |
| Embeddings / Word2Vec | [[entities/embeddings]] | Entity page has an overview of embeddings |
| Transformer (Encoder-Decoder) | [[concepts/transformer-architecture]] | Covered |
| Decoder-Only Transformers | [[concepts/gpt/decoder-only]] | Covered |

**Resource Evaluation:**
- 🟢 **Karpathy "Let's build GPT"** — The best resource for grasping the full Transformer picture in 2 hours. Its value remains unchanged as of 2026.
- 🟢 **3Blue1Brown "But what is a GPT?"** — Visually beautiful. Ideal for solidifying foundations.
- 🟢 **Jay Alammar "The Illustrated Transformer"** — A classic with excellent intuitive understanding. Must-read.
- 🟡 **d2l.ai** — A textbook with code. Good balance of theory and practice, but doesn't cover recent LLM techniques (RLHF, vLLM).
- ⚪ **Goodfellow "Deep Learning"** — A classic but published in 2016. No Transformer coverage. Historical value only.

---

### Section III: Foundations for Modern Language Modeling

**Coverage rate:** ~50%

| Topic | Wiki Coverage | Notes |
|-------|-------------|------|
| Tokenization (BPE) | [[concepts/claude/tokenizer-47]] | Focused on Claude 4.7 tokenizer changes. General BPE explanation is insufficient |
| Positional Encoding (RoPE) | [[concepts/transformer-architecture]] | Partially covered within the Transformer architecture page |
| Mixture-of-Experts | [[concepts/mixture-of-experts]] | Covered |
| Scaling Laws | [[concepts/scaling-laws]] | Covered |
| Pretraining Recipes | [[concepts/llm-training-fundamentals]] | Covered |
| Distributed Training / FSDP | [[concepts/post-training/pytorch-fsdp]], [[concepts/post-training/fsdp-qlora]] | Both are well-covered |

**Resource Evaluation:**
- 🟢 **Karpathy "Tokenization" video** — A must-watch for deep understanding of tokenization. Provides a unique thought framework.
- 🟢 **Eleuther AI "Rotary Embeddings" blog** — Still the best explanation of RoPE.
- 🟢 **Hugging Face "Mixture of Experts Explained"** — Sufficient as a conceptual explanation.
- 🟢 **Answer.AI "FSDP + QLoRA Deep Dive"** — Practical FSDP explanation. Already incorporated into wiki [[concepts/post-training/fsdp-qlora]].
- 🟡 **Meta's official FSDP blog** — A bit dated but good for understanding the basics.
- 🟡 **Chinchilla Scaling Laws blog series** — Good for basic concepts, but doesn't cover post-2024 Scaling Laws discussions (shift toward smaller models).
- ⚪ **"The Novice's LLM Training Guide"** — Unofficial guide on rental servers. Content is useful but source provenance is unclear.

---

### Section IV: Finetuning Methods for LLMs

**Coverage rate:** ~80% (Wiki's most comprehensive section)

| Topic | Wiki Coverage | Notes |
|-------|-------------|------|
| Instruct Fine-Tuning | [[concepts/fine-tuning]], [[concepts/post-training/post-training]] | Both covered |
| LoRA | [[concepts/peft-lora-and-qlora]], [[concepts/qlora]], [[entities/lora-fine-tuning]] | Well-covered with 3 pages |
| RLHF | [[concepts/post-training/rlhf]], [[concepts/security-and-governance/ai-safety-alignment-rlhf-scalable-oversight-interpretability]] | Covered |
| DPO | [[concepts/post-training/rlhf-dpo-orpo-kto-preference-optimization]] | Covered (including KTO/ORPO) |
| Context Scaling (YaRN) | — | Missing |
| Distillation | [[concepts/model-distillation]] | Covered |
| Model Merging | — | Missing (SLERP merging not covered) |

**Resource Evaluation:**
- 🟢 **Sebastian Raschka "Practical Tips for Finetuning LLMs Using LoRA"** — Rich with practical insights. Valuable hyperparameter selection guidelines.
- 🟢 **Hugging Face "Illustrating RLHF"** — The classic RLHF introduction. The fundamentals remain unchanged as of 2026.
- 🟢 **Hugging Face "DPO with TRL"** — Practical with code.
- 🟡 **Chip Huyen "RLHF"** — Good balance of theory and practice.
- 🟡 **Maxime Labonne "Merge Large Language Models with mergekit"** — The de facto standard guide for model merging. Not yet incorporated into the wiki.

---

### Section V: LLM Evaluations and Applications

**Coverage rate:** ~80%

| Topic | Wiki Coverage | Notes |
|-------|-------------|------|
| Benchmarking / Evals | [[concepts/evaluation/ai-evals]], [[concepts/evaluation/ai-evaluation]], [[concepts/evaluation/open-llm-leaderboard]] | Covered |
| Sampling / Structured Outputs | [[concepts/sampling-strategies]], [[concepts/structured-outputs]] | Covered |
| Prompting | [[concepts/prompt-engineering]] | Covered |
| Vector Databases | [[concepts/vector-search]], [[concepts/rag-systems]] | Covered |
| RAG | [[concepts/rag-systems]], [[concepts/retrieval-augmented-generation]], [[concepts/agentic-rag]] | Covered |
| Agents / Tool Use | Multiple pages | Most comprehensive section |
| DSPy | [[entities/dspy]], [[concepts/dspy-architecture]] | Covered |
| Synthetic Data | [[concepts/synthetic-data]] | Covered |
| Representation Engineering | — | Missing |
| Mechanistic Interpretability | [[concepts/mechanistic-interpretability]] | Covered |

**Resource Evaluation:**
- 🟢 **Lilian Weng "LLM Powered Autonomous Agents"** — Comprehensive agent survey. Still one of the most cited articles as of 2026. However, the implementation dates from 2023.
- 🟢 **Chip Huyen "Building LLM Applications for Production"** — A 2023 article, but the system design principles remain timeless.
- 🟢 **Neel Nanda's MI resources** — The best introduction to mechanistic interpretability. Especially the Glossary and Quickstart Guide are must-reads.
- 🟢 **Anthropic "Scaling Monosemanticity"** — Feature extraction from Claude 3 Sonnet. Important as a real-world application of MI.
- 🟡 **LangChain "Deconstructing RAG"** — Good basics, but diverges from current RAG practice as of 2026.
- 🟡 **Pinecone Learning Series** — Excellent conceptual explanation of vector DBs. Still applicable in 2026.
- ⚪ **Microsoft "Generative AI for Beginners"** — Fine as an introductory level, but too shallow for the handbook's target audience (engineers).

---

### Section VI: Performance Optimizations for Efficient Inference

**Coverage rate:** ~85%

| Topic | Wiki Coverage | Notes |
|-------|-------------|------|
| Quantization | [[concepts/model-quantization]], [[concepts/gguf-quantization]], [[concepts/gguf]] | Covered |
| Speculative Decoding | [[concepts/speculative-decoding]] | Covered |
| FlashAttention | [[concepts/flashattention-pytorch-educational]] | Covered |
| KV Caching | [[concepts/kv-cache]], [[concepts/attention-mechanism-variants]] | Covered |
| vLLM / PagedAttention | [[concepts/vllm]], [[concepts/serving-llms-vllm]] | Covered |
| CPU Offloading / llama.cpp | [[concepts/llama-cpp]], [[concepts/ollama]] | Covered |

**Resource Evaluation:**
- 🟢 **Tim Dettmers "LLM.int8()" blog** — Still the best foundational theory for quantization. The concept of emergent features is essential knowledge.
- 🟢 **Tri Dao's FlashAttention talk** — Explanation by the creator. Ideal for understanding tiling and recomputation.
- 🟢 **NVIDIA "Mastering LLM Techniques: Inference Optimization"** — Short blog that's great for an overview.
- 🟡 **Jay Mody "Speculative Sampling"** — Good as a theoretical walkthrough. However, implementation status in vLLM etc. needs updating.
- 🟡 **vLLM original blog** — From 2023, but PagedAttention fundamentals haven't changed.
- ⚪ **Datacamp "llama.cpp Tutorial"** — Introductory level. Insufficient for deep understanding.

---

### Section VII: Sub-Quadratic Context Scaling

**Coverage rate:** ~5%

| Topic | Wiki Coverage | Notes |
|-------|-------------|------|
| Sliding Window Attention | — | Missing |
| Ring Attention | — | Missing |
| Linear Attention / RWKV | — | Missing |
| SSMs / Mamba | — | Missing. The S4→Mamba history is not covered |
| HyperAttention | — | Missing |

**Resource Evaluation:**
- 🟢 **"The Annotated S4"** — The best SSM explanation. Bridges code and theory.
- 🟢 **Maarten Grootendorst "Visual Guide to Mamba"** — Visually easy to understand. Ideal for Mamba introduction.
- 🟢 **Tri Dao "Mamba-2 State Space Duality" series** — The complete 4-part Mamba-2 series. An important contribution that theoretically demonstrates the relationship between SSMs and Linear Attention.
- 🟡 **RWKV blogs (Hugging Face, Johan Wind)** — Conceptual explanation of RWKV. Practical utility is limited but useful for understanding architectural diversity.

**⚠️ This section is the biggest gap in the Wiki. In particular, Mamba-family SSMs are still actively researched, and creating concept pages is recommended.**

---

### Section VIII: Generative Modeling Beyond Sequences

**Coverage rate:** ~5%

| Topic | Wiki Coverage | Notes |
|-------|-------------|------|
| VAEs | — | Missing |
| GANs | — | Missing (only occasional mentions) |
| Conditional GANs / VQGAN-CLIP | — | Missing |
| Diffusion Models | [[concepts/ai-image-generation]], [[skills/stable-diffusion-image-generation]] | Exists as skills. Missing as concept pages |
| Normalizing Flows | — | Missing |

**Resource Evaluation:**
- 🟡 **Lilian Weng "What are Diffusion Models?"** — Still good as a theoretical introduction to diffusion models. However, many more resources have emerged in the 2 years since.
- 🟡 **Hugging Face "The Annotated Diffusion Model"** — Code-annotated explanation. For those who want to learn through implementation.
- ⚪ **GANs-related (Paperspace, Analytics Vidhya)** — Even in 2024, the handbook itself acknowledged that GANs are "somewhat outdated." In 2026, they're even older — focus should be on Diffusion and VAEs.

---

### Section IX: Multimodal Models

**Coverage rate:** ~15%

| Topic | Wiki Coverage | Notes |
|-------|-------------|------|
| VQ-VAE | — | Missing |
| Vision Transformers | [[concepts/vision-models]] | Covered |
| Multimodal (general) | [[concepts/multimodal]] | Covered |

**Resource Evaluation:**
- 🟢 **Chip Huyen "Multimodality and LMMs"** — Best for an overview of multimodal LLMs.
- 🟢 **Lilian Weng "Generalized Visual Language Models"** — Organizes various VLM approaches.
- 🟡 **Distill "Multimodal Neurons"** — Visually appealing. Useful for conceptual understanding but limited academic depth.
- ⚪ **Apple MM1 paper** — Large-scale experiment from 2024. Practical but somewhat dated in 2026.

---

## 📊 Overall Coverage

| Section | Wiki Coverage | Notes |
|---------|-------------|------|
| I. Foundations | **~5%** | Outside Wiki scope (prerequisites). Referenced resources are useful. |
| II. Neural Sequential | **~20%** | Missing RNN/LSTM concept pages |
| III. Modern LM | **~50%** | General tokenization page is insufficient. FSDP/MoE are well-covered. |
| IV. Finetuning | **~80%** | Wiki's most comprehensive section. Context Scaling (YaRN) and Model Merging are missing. |
| V. Evaluations & Apps | **~80%** | Agents/RAG are well-covered. Representation Engineering is missing. |
| VI. Inference Optimization | **~85%** | Most comprehensive section. Everything covered. |
| VII. Context Scaling | **~5%** | Biggest gap. SSM/Mamba/RWKV concept pages completely absent. |
| VIII. Beyond Text | **~5%** | Diffusion/VAE/GANs not covered. However, close to Wiki scope boundary. |
| IX. Multimodal | **~15%** | VQ-VAE missing. VLMs are covered. |

---

## 🏆 Recommended Priorities

### 🅰️ Engineers / Practitioners — For LLM application developers

Focus on Section V (Evals & Applications) and Section VI (Inference Optimization). VII (Context Scaling) only if you want to understand Mamba.

```text
1. Section V: Agents / RAG / DSPy — Directly connected to practice
2. Section VI: vLLM / Quantization — Essential for deployment
3. Section IV: LoRA / RLHF / DPO — Practical finetuning
```

### 🅱️ Researchers / Deep divers

Start from Section III (Modern LM), then move to Section VII (SSM/Mamba) and the latter half of Section V (MI, RepE).

```text
1. Section III: Scaling Laws / MoE — Foundational theory
2. Section VII: Mamba / SSM — Cutting-edge architecture
3. Section V: MI / RepE — Interpretability
4. Section I: Time-Series / RL — Theoretical foundations
```

### 🅲️ Beginners — Learning GenAI for the first time

Following the handbook structure as-is is optimal. Section II up through Transformer is mandatory. Section III onward — choose based on interest.

```text
1. Section I: Math (3Blue1Brown) + RL basics
2. Section II: Karpathy "Let's build GPT" (highest priority)
3. Section III: Tokenization + Scaling Laws
4. Section IV: LoRA (start from practice)
5. Section V: Prompting → RAG
```

---

## 🗺️ Gap Analysis — Concepts to Add to Wiki

| Priority | Missing Concept | Section | Reason |
|--------|---------|------------|------|
| 🔴 | **SSM / Mamba** | VII | Important alternative architecture paradigm. Still an active research area. |
| 🔴 | **Representation Engineering** | V | New paradigm for AI safety and model control. High practical value. |
| 🟡 | **Model Merging (mergekit / SLERP)** | IV | Widespread as a practical approach to open-source model utilization. |
| 🟡 | **Context Scaling (YaRN / RoPE extension)** | IV | Important as an implementation technique for long-context processing. |
| 🟢 | **RNN / LSTM** | II | Historical value. However, low priority (in the Transformer-centric era). |
| 🟢 | **FlashAttention (detailed concept page)** | VI | Currently exists as a skill. Worth creating as a concept page. |
| 🟢 | **Diffusion Models (concept page)** | VIII | Foundation of image generation. Skills exist but no concept page. |

---

## 🔗 Related Wiki Pages

- [[entities/will-brown]] — Handbook creator
- [[concepts/llm-course-roadmap]] — Maxime Labonne (similar meta knowledge map)
- [[concepts/learning-llms-in-2025]] — Yoav Goldberg (similar meta knowledge map)
- [[concepts/transformer-architecture]] — Core Transformer concepts
- [[concepts/scaling-laws]] — Scaling Laws
- [[concepts/post-training/rlhf-dpo-orpo-kto-preference-optimization]] — Preference optimization
- [[concepts/rag-systems]] — Retrieval-augmented generation
- [[concepts/model-quantization]] — Quantization
- [[concepts/mechanistic-interpretability]] — Mechanistic interpretability
- [[entities/andrej-karpathy]] — Most cited educator in the handbook
- [[entities/lilian-weng]] — Second most cited blogger
- [[entities/maxime-labonne]] — Creator of companion resource (LLM Course)

---

> **This page is meta-knowledge (a knowledge map) that evaluates the resources referenced by William Brown's GenAI Handbook and maps them to existing Wiki concepts. Refer to each linked page for explanations of individual technical concepts.**
