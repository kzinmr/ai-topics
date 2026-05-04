---
title: Maxime Labonne
type: entity
aliases: [mlabonne, maximelabonne]
created: 2026-05-04
updated: 2026-05-04
tags: [person, opinion-leader, open-source, llm-post-training]
sources:
  - https://mlabonne.github.io/blog/
  - https://github.com/mlabonne
  - https://huggingface.co/mlabonne
  - https://twitter.com/maximelabonne
  - https://www.linkedin.com/in/maxime-labonne/
---

# Maxime Labonne

**Role:** Head of Post-Training @ [Liquid AI](https://www.liquid.ai/)
**Location:** London, United Kingdom
**Blog:** https://mlabonne.github.io/blog/
**X/Twitter:** [@maximelabonne](https://twitter.com/maximelabonne)
**GitHub:** [mlabonne](https://github.com/mlabonne) (6.8k+ followers)
**Hugging Face:** [mlabonne](https://huggingface.co/mlabonne) (178 models)
**Google Scholar:** [Maxime Labonne](https://scholar.google.com/citations?user=r4PsgrcAAAAJ)

## Overview

Maxime Labonne is one of the most prolific and influential open-source educators in the LLM post-training space. He is the creator of the **LLM Course** (78.9k ⭐ on GitHub), the most widely referenced curated guide to getting started with Large Language Models. He holds a Ph.D. in Machine Learning from the Polytechnic Institute of Paris and is recognized as a **Google Developer Expert in AI/ML**.

His work spans the full post-training stack — supervised fine-tuning (SFT), preference alignment (DPO, ORPO, GRPO), model merging (mergekit), quantization (GPTQ, GGUF, AWQ), and model editing (abliteration). He is the author of two best-selling technical books and leads post-training at Liquid AI, where he works on efficient model architectures like LFM2.

## Career Timeline

| Date | Event |
|------|-------|
| ~2019 | Ph.D. in Machine Learning, Polytechnic Institute of Paris — applied ML to cybersecurity (intrusion detection, protocol identification) |
| 2020 | **Airbus** AI Lab — developed CyBERT, domain-specific LLMs (RoBERTa, GPT-2) for network protocol understanding |
| 2022 | Joined **JPMorgan Chase** — developed internal code copilots, fine-tuned IndexGPT for domain-specific use cases, created Spam-T5 (published at IJCAI 2023 — first open-sourced AI project at JPMorgan) |
| 2023 | Published "Hands-On Graph Neural Networks Using Python" (Packt) — best-selling book |
| 2024 | Joined **Liquid AI** as Head of Post-Training; published "LLM Engineer's Handbook" (Packt) |
| 2024 | Published abliteration technique — removing refusal mechanisms from LLMs without retraining (845+ upvotes on Hugging Face, became a widely-used community technique) |
| 2024 | Created NeuralHermes-2.5-Mistral-7B, NeuralDaredevil-8B — top-ranked open models |
| 2025 | LLM Course reaches 70k+ ⭐ on GitHub, becoming the de facto entry point for LLM education |
| 2026 | Contributed to Liquid AI LFM2 series — MoE models designed for edge deployment (8.3B params, 1.5B active/token) |
| 2026 | LLM Datasets repository reaches 4.5k ⭐ — curated datasets for post-training |

## Key Contributions

### LLM Course ([mlabonne/llm-course](https://github.com/mlabonne/llm-course))
> 78.9k ⭐ — the largest open LLM curriculum on GitHub

A structured roadmap with Colab notebooks covering the complete LLM pipeline: quantization, supervised fine-tuning, preference alignment (DPO, ORPO, GRPO), model merging, and evaluation. Includes:
- **[The LLM Scientist](https://github.com/mlabonne/llm-course)** — hands-on track with coding exercises
- **[The LLM Engineer](https://github.com/mlabonne/llm-course)** — production-focused track (RAG, deployment, LLMOps)
- All tutorials come with executable Colab notebooks — zero-config learning

### Abliteration
> Technique to remove model refusal mechanisms without retraining

The **abliteration** technique (June 2024) uses activation analysis on harmless vs. harmful prompts to calculate a "refusal direction" vector. By subtracting this direction from the model's weights, the model stops outputting refusals. Key properties:
- Zero retraining required — single forward pass to compute the direction
- Can be "healed" with DPO after abliteration to restore quality (e.g., NeuralDaredevil-8B)
- Demonstrated the fragility of safety fine-tuning — raised important ethical considerations
- Inspired derivative work: norm-preserving biprojected abliteration, MopeyMule (style transfer via same technique)

### Model Merging & MergeKit
Labonne's tutorials ([Merge LLMs with mergekit](https://mlabonne.github.io/blog/posts/2024-01-08_Merge_LLMs_with_mergekit.html)) were among the most influential in popularizing **model merging** — combining multiple fine-tuned models into a single stronger model without additional training. He created **LazyMergekit**, a one-click Colab for model merging, and documented techniques for creating **Mixture of Experts (MoE)** models from merged dense models.

### Quantization Education
Authored the most-read tutorials on LLM quantization:
- [Introduction to Weight Quantization](https://mlabonne.github.io/blog/posts/Introduction_to_Weight_Quantization.html) — conceptual overview with code
- [Quantize with llama.cpp](https://mlabonne.github.io/blog/posts/Quantize_Llama_2_models_using_ggml.html) — GGUF quantization workflow
- [4-bit Quantization with GPTQ](https://mlabonne.github.io/blog/posts/4_bit_Quantization_with_GPTQ.html) — AutoGPTQ implementation
- Created **AutoQuant** — one-click quantization Colab

### Fine-Tuning Tools
Created a suite of automation tools for LLM fine-tuning pipelines:
- **LLM AutoEval** ([mlabonne/llm-autoeval](https://github.com/mlabonne/llm-autoeval)) — automated evaluation pipeline
- **LazyAxolotl** — one-click Axolotl fine-tuning Colab
- **LazyMergekit** — one-click model merging Colab
- Tutorial on fine-tuning Llama 3.1 with Unsloth (ultra-efficient SFT)

### Post-Training at Liquid AI
As Head of Post-Training at Liquid AI, Labonne works on the **LFM2** model series — a Mixture of Experts (MoE) architecture with:
- 8.3B total parameters, only 1.5B active per token
- Designed for edge deployment (phones, laptops)
- Uses llama.cpp and vLLM for inference
- Quality comparable to 3-4B dense models, speed faster than Qwen3-1.7B
- Pre-trained on 12T tokens with strong math/code/instruction-following capabilities

## Books

| Title | Publisher | Year | Description |
|-------|-----------|------|-------------|
| **Hands-On Graph Neural Networks Using Python** | Packt | 2023 | Practical guide to GNN architectures (GCN, GAT, GraphSAGE, GIN) with Python implementations |
| **LLM Engineer's Handbook** | Packt | 2024 | From fundamentals to deploying advanced LLM and RAG apps on AWS using LLMOps best practices. Code: [PacktPublishing/LLM-Engineers-Handbook](https://github.com/PacktPublishing/LLM-Engineers-Handbook) (5k ⭐) |

## Notable Models (Hugging Face)

Labonne has released **178 models** on Hugging Face, including:
- **NeuralDaredevil-8B-abliterated** — abliterated + DPO-healed 8B model
- **NeuralHermes-2.5-Mistral-7B** — DPO fine-tune of Mistral-7B
- **TwinLlama-3.1-8B-DPO** — from the LLM Engineer's Handbook
- **LFM2 series** (at LiquidAI) — 8B-A1B, 2.6B, 1.2B, 700M
- Various abliterated variants: Gemma-3-12B, Phi-4, etc.

## Relationship to Wiki Topics

- **[[concepts/model-quantization]]** — Core educational resource; his quantization tutorials are among the most widely referenced
- **[[concepts/abliteration]]** — Created and popularized this technique for model editing
- **[[concepts/mergekit-model-merging]]** — Popularized model merging through tutorials and LazyMergekit
- **[[concepts/dpo-preference-tuning]]** — His DPO tutorial for Mistral-7b is canonical
- **[[entities/liquid-ai]]** — Currently employed as Head of Post-Training
- **[[concepts/local-llm]]** — Tutorials cover GGUF quantization for local inference
- **[[concepts/small-language-models]]** — LFM2 MoE work on efficient edge models
- **[[concepts/llm-fine-tuning]]** — Comprehensive fine-tuning guides with Axolotl and Unsloth

## Online Presence

- **Blog:** https://mlabonne.github.io/blog/ (Quarto-based, posts on LLMs, GNNs, optimization)
- **Substack:** https://maximelabonne.substack.com/
- **Medium:** https://medium.com/@mlabonne (9.1k followers)
- **Hugging Face Spaces:** 19 spaces including Model Family Tree, Yet Another LLM Leaderboard, AutoMerger, Chess LLM
- **Speaker:** Regular conference speaker; profiled on Learning from Machine Learning podcast (Seth Levine)

## Notes

- RSS feed at `https://mlabonne.github.io/blog/index.xml` is configured in Quarto (`feed: true`) but currently returns 404 from GitHub Pages — feed may need a build/deployment fix
- His LLM Course has been forked by thousands and is used as the curriculum for multiple university courses in LLM engineering
- The abliteration technique inspired a broader community movement in model editing and safety mechanism analysis
