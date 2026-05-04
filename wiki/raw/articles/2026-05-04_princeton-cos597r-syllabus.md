---
title: "Princeton COS597R: Deep Dive into Large Language Models"
type: raw
created: 2026-05-04
source: https://princeton-cos597r.github.io/
author: Danqi Chen & Sanjeev Arora
tags: [course, syllabus, princeton, llm-research, scaling, alignment, data, reasoning]
---

# Princeton COS597R: Deep Dive into Large Language Models (Fall 2024)

**Instructors:** Danqi Chen & Sanjeev Arora
**TAs:** Adithya Bhaskar, Tyler Zhu
**Focus:** Rigorous survey of LLM research across architecture, data preparation, training (pre/post), alignment, and deployment. Emphasizes conceptual understanding and research over engineering.

## Course Structure
| Component | Weight | Description |
|-----------|--------|-------------|
| Class Participation | 30% | Read 1-2 papers per class, submit pre-lecture form |
| Debate Panels | 15% | Weeks 4-9: Presenter + 2 Critics + 2 Proponents |
| Lecture Scribing | 10% | Groups of 3 scribe using Overleaf template |
| Final Project | 45% | Teams of 2-3: proposal + presentation + paper |

## Key Research Topics

### 1. Pre-training & Scaling
- GPT-3, Llama 3, Transformer architecture
- Scaling Laws: Chinchilla compute-optimal training, data-constrained scaling
- Emergent abilities debate

### 2. Data & Post-Training
- Data Curation: Dolma (3T tokens), data quality vs. quantity (Phi-1.5)
- Instruction Tuning: FLAN, Tulu
- Preference Learning: RLHF, DPO

### 3. Advanced Capabilities
- Alignment: Constitutional AI, weak-to-strong generalization
- Reasoning: process supervision, test-time compute scaling
- Long Context: RoPE, 128K+ token handling
- Agents & RAG

## Schedule & Readings
| Date | Topic | Key Paper |
|------|-------|-----------|
| Sep 9-11 | Pre-training | GPT-3; Llama 3 |
| Sep 16 | Scaling Laws | Chinchilla |
| Sep 23 | Data Curation | Dolma; Phi-1.5 |
| Sep 30 | Preferences | InstructGPT; DPO |
| Oct 7 | Constitutional AI | Harmlessness from AI Feedback |
| Oct 21 | Long Context | Training Long-Context LMs |
| Oct 28-30 | Reasoning | Process Supervision; Test-Time Compute |
| Nov 4 | Small Models | Sheared LLaMA; Gemma 2 |
| Nov 13 | RAG | Retrieval from trillions of tokens |
| Nov 18-20 | Hardware/Vision | FlashAttention; Mamba; Visual Grounding |

## Resources
- Scribe Template: https://www.overleaf.com/read/yjmgcqgyhsyw
- Final Project Template: https://www.overleaf.com/read/smnpdcycbzvg
