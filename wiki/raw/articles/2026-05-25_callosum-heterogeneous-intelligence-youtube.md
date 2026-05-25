---
title: "Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum"
url: "https://www.youtube.com/watch?v=WRBNDpUhsJQ"
fetched_at: 2026-05-25T07:01:33+00:00
source: "AI Engineer (YouTube)"
tags: [youtube, raw, talk]
---

# Scaling the Next Paradigm of Heterogeneous Intelligence

**Speaker:** Adrian Bertagnoli, Founding Engineer at Callosum
**Source:** AI Engineer Conference (YouTube), Duration: 15:13

## The Shift from Homogeneous to Heterogeneous Intelligence

### Homogeneous Intelligence (Prevailing Paradigm)
- Single large models trained on identical hardware fleets
- Driven by neural scaling laws (more data + parameters → better models)
- Primarily designed for the training domain, not inference

### Toward Full Heterogeneity
Three evolutionary phases:
1. **Mild heterogeneity** – same clusters, but varied prompts, agents, or MoE layers
2. **Increased heterogeneity** – different chip types per model, state-space models, diffusion models interacting
3. **Co-evolution** – hardware and software designed together, unified interface for all intelligence

## Why Heterogeneity? Mathematical Formalization

- Real-world problems decompose into sub-problems requiring **different types of intelligence**
- **Principle of Maximum Heterogeneity**: Under reasonable constraints, heterogeneous systems consistently outperform homogeneous ones (formal proof across neuroscience, economics, ecology)

## Practical Results

### Heterogeneous Recursion for Context-Heavy Tasks (ULong Benchmark)
| Configuration | Cost Saving | Speed Improvement |
|---|---|---|
| vs GPT-5.2 (Cerebras) | 7× cheaper | 5× faster |
| vs GPT-5.2 (SambaNova) | 12× cheaper | 3× faster |

### Visual Web Navigation (Video Web Arena)
- Heterogeneous Mixture: Qwen 3 VL8B-Instruct + Kimi K2.5
- Beat GPT-5.2 by 18%, Gemini 2.5 by 25%
- 3× faster and 3.7× cheaper than GPT-5.2 alone
- Key insight: "You don't need GPT to zoom for you" — offload simple subtasks to small models

## Three Eras of Compute Scaling
1. **CPU era** – faster single-threaded performance
2. **Massively parallel era** – dominated by NVIDIA GPUs
3. **Heterogeneous era** – multi-agent intelligence mapped to diverse chips, software/hardware co-designed

## Collaboration
- £3 million grant with Aria Institute (UK) for first heterogeneous collocated compute environment
