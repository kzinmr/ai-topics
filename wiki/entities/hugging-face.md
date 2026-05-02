---
title: Hugging Face
type: entity
aliases: [HuggingFace, HF]
created: 2026-04-24
updated: 2026-04-24
status: active
tags:
  - company
  - ai-infrastructure
  - open-source
  - model
  - ml-platform
  - nlp
url: https://huggingface.co/
linkedin: https://www.linkedin.com/company/hugging-face
twitter: https://x.com/huggingface
github: https://github.com/huggingface
sources:
  - https://huggingface.co/about
  - https://en.wikipedia.org/wiki/Hugging_Face
  - https://observer.com/2026/02/hugging-face-monetization-chief-jeff-boudier-business-model
  - https://huggingface.co/blog/transformers-v5
  - https://hyperion-consulting.io/en/insights/hugging-face-enterprise-guide-2026
  - https://techcrunch.com/2025/11/18/hugging-face-ceo-says-were-in-an-llm-bubble-not-an-ai-bubble
---

# Hugging Face

**The GitHub of AI** — the central open-source infrastructure layer for machine learning. Platform for sharing, discovering, and deploying ML models, datasets, and demos.

## Overview

Hugging Face (🤗) is the dominant platform for open-source AI development. Founded in 2016 by Clément Delangue, Julien Chaumond, and Thomas Wolf in New York City, the company evolved from a teenage chatbot app into the central hub of the AI ecosystem. By 2025–2026, it hosts over **900,000 models**, **200,000+ datasets**, and **350,000+ Spaces** with over **13 million global users** and **1,500+ enterprise customers** including Meta, Google, Microsoft, Apple, OpenAI, and Anthropic.

Valued at **$4.5 billion** following its Series D ($235M, August 2023, led by Salesforce with participation from Google, Amazon, and Nvidia), Hugging Face has **not raised VC in over two years** and rejected a $500M Nvidia investment to maintain investor independence. Jeff Boudier (joined 2020 as first business-focused hire) runs monetization with a freemium model achieving 3–5% conversion. The company operates at net profitability or strategic investment levels per quarter.

CEO Clément Delangue's stated vision: *"make Artificial Intelligence, robotics and Open Source"* — positioning Hugging Face as open-source infrastructure rather than a closed AI product company.

## Key People

| Name | Role | Background |
|------|------|------------|
| **Clément "Clem" Delangue** | Co-founder & CEO | Former Moodstocks (acquired by Google). Previously attended École 42. Moved from France to NYC. |
| **Julien Chaumond** | Co-founder & CTO | Infrastructure-focused co-founder. Active since 2016 founding. |
| **Thomas Wolf** | Co-founder & CSO | Joined March 2017. Led development of the Transformers library. |
| **Jeff Boudier** | Head of Monetization / Business | Joined 2020 as first business-focused employee. Former GoPro BD exec. |
| **Anthony Moi** | First employee | Joined Jan 2017. Key contributor to ecosystem libraries. |

## Core Products & Libraries

### Platform (Hub)
- **Model Hub**: Central registry for ML models. Nearly every open-weight model (Llama, Mistral, Gemma, etc.) is distributed here first. Each model has a model card with description, uses, training details, eval results, and licensing.
- **Dataset Hub**: 200,000+ datasets for training, fine-tuning, and evaluation.
- **Spaces**: 350,000+ interactive demo applications (Gradio, Streamlit, Docker) — Git-based collaborative development.
- **Inference Endpoints**: Managed model serving infrastructure for enterprise.
- **Inference API**: Free tier for lightweight model inference.

### Libraries (Open Source Tooling)
- **Transformers** (🔥 core product): Unified API for 400+ model architectures. **1.2 billion+ total installs**, >3M installs/day via pip. Released Transformers v5 (Dec 2025) — all-in on PyTorch, continuous batching, paged attention, first-class quantization, `transformers serve` (OpenAI-compatible).
- **Diffusers**: Text-to-image and image generation pipelines.
- **Datasets**: Dataset loading, processing, and streaming library.
- **PEFT** (Parameter-Efficient Fine-Tuning): LoRA, QLoRA, and other parameter-efficient methods.
- **TRL** (Transformer Reinforcement Learning): RLHF/DPO/GRPO training for LLMs.
- **Accelerate**: Easy distributed training setup.
- **Tokenizers**: Fast subword tokenization (Rust-based).
- **Optimum**: Hardware-optimized inference (ONNX, TensorRT, OpenVINO).
- **Gradio**: Acquired Dec 2022 — UI framework for ML demos.
- **LeRobot**: Robotics software library (launched 2024).
- **TGI** (Text Generation Inference): High-performance inference server with continuous batching, tensor parallelism, OpenAI-compatible API.

### Enterprise Products
- **Private Hub**: SaaS or on-premises deployment of the Hub.
- **Enterprise tier**: Scaled usage, collaboration tools, compliance features (EU AI Act alignment).

## Business Model & Strategy

### Financial Stance
- **Last funding**: Series D, $235M (Aug 2023) → $4.5B valuation
- **No new VC**: Has not raised funds in 2+ years; still holding capital from 2023 round
- **Rejected $500M Nvidia offer** to avoid single-investor dominance
- **Revenue**: Freemium model, 3–5% conversion to paid tier
- **Profitability**: Operating at net profitability or strategic investment levels per quarter
- **Funding is not a priority** (per Jeff Boudier, Feb 2026)

### Philosophy
- **Contrarian to Silicon Valley growth culture**: Prioritizes financial sustainability and open-source ethos over rapid VC scaling
- **Anti-ad stance**: Rejected ad network proposals for Hugging Chat; considers ads misaligned with company values (contrasts with OpenAI ChatGPT ad rollout)
- **"GitHub of AI"**: Focus on developer infrastructure, not end-user AI products
- **Investor independence**: Deliberately diversified investor base

### Enterprise Clients
Meta, Google, Microsoft, Apple, OpenAI, Anthropic, Salesforce, AMD, Intel, Amazon

## Key Milestones & History

| Date | Event |
|------|-------|
| **2016** | Founded by Delangue, Chaumond, Wolf in NYC. Started as a chatbot app for teenagers. |
| **2016–2017** | Open-sourced chatbot's underlying model; pivoted to ML platform. Thomas Wolf joined (Mar 2017), Anthony Moi joined as first employee (Jan 2017). |
| **2020** | Transformers library released — became the backbone of the open-source ML ecosystem. Jeff Boudier joined as first business-focused hire. |
| **2021** | BigScience Research Workshop launched (Apr 28) — multi-group collaboration for open LLMs. |
| **2022 (May)** | Series C: $235M led by Coatue and Sequoia, $2B valuation. |
| **2022 (Aug)** | AWS partnership announced; Private Hub (enterprise) launched. |
| **2022 (Dec)** | Acquired Gradio (UI framework for ML apps). |
| **2022** | BLOOM released (176B parameters, multilingual LLM from BigScience). |
| **2023 (Aug)** | Series D: $235M led by Salesforce. Valuation: $4.5B. Google, Amazon, Nvidia participated. |
| **2024** | EU AI Accelerator launched with Meta & Scaleway at STATION F (Paris). UNESCO+Meta+NLLB translator for 200+ languages. LeRobot robotics library launched. Reachy Mini desktop robot (>5,000 units sold; featured in Jensen Huang CES keynote). |
| **2024–2025** | Heavy investment in on-device AI and robotics software. |
| **2025 (Apr)** | Acquired Pollen Robotics (French humanoid robotics startup, founded 2016 by Lapeyre & Rouanet) — expanding into open-source AI robotics. |
| **2025 (Nov)** | CEO Delangue: "We're in an LLM bubble, not an AI bubble" (Axios event). Predicted LLM bubble bursting next year but AI application to biology, chemistry, image, audio, video is just beginning. |
| **2025 (Dec)** | Transformers v5 released (Dec 1) — major paradigm shift: all-in on PyTorch, continuous batching, paged attention, `transformers serve`, first-class quantization. |
| **2026 (Feb)** | Observer interview with Jeff Boudier: Company at net profitability or strategic investment levels. Still holding 2023 round capital. Rejected ad integrations. |
| **2026 (early)** | Security breach: hackers hijacked platform to distribute Android-targeted malware. |
| **2026 (Mar)** | Reached 13M global users, 900K+ models, 200K+ datasets, 350K+ Spaces, 1,500+ enterprise customers. |

## Strategic Insights

### Open-Source Leadership
Hugging Face is the single most important open-source ML platform. Nearly every open-weight model from major AI labs (Llama, Mistral, Gemma, etc.) is distributed through the Hub. The Transformers library is the definitive source of truth for model architectures across the field.

### Infrastructure Moat
The ecosystem libraries (Transformers, PEFT, TRL, Datasets, Accelerate, Diffusers, Tokenizers) form a complete pipeline from model selection → fine-tuning → deployment. This creates a strong network effect: the more models and datasets on the platform, the more developers use the libraries, and vice versa.

### Hardware & Cloud Integration
Strategic alliances with AWS (Trainium), Nvidia (CES keynote with Reachy Mini), and hardware vendors (Intel, AMD) ensure scalable deployment. Transformers v5's on-device expansion via executorch & optimum targets edge deployment.

### Robotics Bet
Pollen Robotics acquisition + LeRobot library + Reachy Mini hardware positions Hugging Face as the open-source platform for AI robotics — expanding beyond NLP into physical AI systems.

### LLM Bubble Commentary
Delangue's Nov 2025 statement is notable: he distinguishes between an "LLM bubble" (chatbots getting outsized attention) and broader AI application (biology, chemistry, vision, audio, video). This suggests Hugging Face is positioning for a post-LLM-hype era where AI applications diversify beyond text generation.

## Security Incident (2026)
In early 2026, hackers compromised the Hugging Face platform, distributing Android-targeted malware capable of full system takeover. This is a significant security event for a platform hosting 900K+ models and used by 13M users.

## Related Entities
- [[concepts/transformers-library]]
- [[anthropic]]
- [[openai]]
- 
- [[andrej-karpathy]] (Hugging Face contributor)
- [[simon-willison]] (Hugging Face ecosystem user)
- [[concepts/unsloth]] (fine-tuning on Transformers)
- [[concepts/vllm]] (complementary inference engine)
-  (acquired 2025)
-  (acquired 2022)

## References

- huggingface.co--google-gemma-4-e4b--b37a0ece
