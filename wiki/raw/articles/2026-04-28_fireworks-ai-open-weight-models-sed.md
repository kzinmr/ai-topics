---
title: "Fireworks AI – Serving and Customizing Open-Weight Models (Software Engineering Daily, Episode 1919)"
source: "Software Engineering Daily"
url: "https://softwareengineeringdaily.com/2026/04/28/open-weight-ai-models/"
transcript_url: "https://softwareengineeringdaily.com/wp-content/uploads/2026/03/SED1919-FireworksAI.txt"
date: 2026-04-28
host: "Gregor Vand"
guest: "Benny Chen, Co-Founder of Fireworks AI"
tags: [fireworks-ai, open-weight-models, inference, rft, speculative-decoding, fine-tuning]
---

# Fireworks AI – Serving and Customizing Open-Weight Models

Software Engineering Daily, Episode 1919. Hosted by Gregor Vand, featuring Benny Chen (Co-Founder of Fireworks AI).

## Executive Summary

Fireworks AI is a platform dedicated to serving and customizing **open-weight models** at scale. Founded roughly six months before the launch of ChatGPT, the company focuses on providing optimized inference infrastructure, multi-hardware support (NVIDIA and AMD), and advanced reinforcement fine-tuning (RFT) capabilities. The platform currently processes over **13 trillion tokens per day**, rivaling the scale of major closed-source providers like OpenAI and Google.

## Key Technical Insights

### Open-Weight Models Definition
> "Open-weight models are AI systems whose trained parameters are publicly released, which allows developers to run, fine-tune and deploy them independently rather than accessing them only through a hosted API... they've become credible alternatives for production workloads with advantages in customization and data privacy."

### Multi-Hardware Strategy (NVIDIA vs. AMD)
> "We have a very, I would say, expensive but important commitment to do multi-hardware... Practically speaking, it's all about supply chain reliability. Making sure that you can actually buy the cards when you have the money... having more than one [supplier] is very, very helpful."

### The Shift to Reinforcement Learning
> "Reinforcement learning is a new lever that the industry found while the pretraining sort of free-riding slowed down... you need sort of exponential amount of compute to get the straight line going. And at some point, the money aspect will kick in... reinforcement learning was a new paradigm that the industry found to keep the scaling going."

## Fireworks AI Technology Stack

### FireAttention
In-house kernels developed to ensure numerical consistency between training and inference. Critical for reinforcement learning, where slight discrepancies can cause training to fail.

### Speculative Decoding
Fireworks helps customers train **custom speculators** specifically for their fine-tuned models to maximize speed. A small "draft" model predicts tokens and a large "target" model verifies them — but the key insight is that custom speculators trained on the fine-tuned model's distribution achieve much higher acceptance rates.

### 3D FireOptimizer
Internal database and automation tool that predicts the best deployment trade-offs (hardware type, cache hit rate, workload patterns) for a specific customer use case.

### Multi-Hardware Support
Unlike many providers locked into NVIDIA, Fireworks has invested heavily in AMD support for supply chain resilience and price competitiveness.

## Model Customization & Evaluation

### The "Eval Protocol"
Fireworks open-sourced the **Eval Protocol**, a framework focused on authoring evaluations for reinforcement learning. Chen argues that **"Traces are all you need"** — if a product manager can articulate what a "good" or "bad" output looks like, they can use production traces to rank models and bootstrap RL without needing a massive team of MLEs. Once a company owns its evaluation suite, it gains the power to switch between model providers without losing quality.

### RFT vs. SFT

| Aspect | SFT | RFT |
|--------|-----|-----|
| Data requirements | Expensive, human-labeled datasets | Production traces + LLM-as-Judge |
| Personnel | MLEs for quality control | Software engineers |
| Loop | Human-in-the-loop labeling | Automated "LM as Judge" |
| Scalability | Linear with labeling budget | Sub-linear with compute |

### Vercel Case Study
Vercel used RFT with Fireworks to achieve **40x faster code fixing** with improved output quality.

## Market Trends

- **Open-weight competitiveness**: Models like Llama 3, DeepSeek, Mistral, and Qwen are now price-competitive and performance-competitive with closed-source frontier models for specific tasks like coding and function calling.
- **The "Alpha" is shrinking**: Few secrets left in AI; data sets and recipes are converging.
- **ROI barriers**: The biggest barrier to AI ROI isn't compute cost — it's the inability of organizations to **"define good"** through robust evaluations.
