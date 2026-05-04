---
title: "Stanford CS336: Language Modeling from Scratch"
type: raw
created: 2026-05-04
source: https://stanford-cs336.github.io/spring2025/
author: Tatsunori Hashimoto & Percy Liang
tags: [course, syllabus, stanford, cs336, llm-training, implementation, triton, alignment]
---

# Stanford CS336: Language Modeling from Scratch (Spring 2025)

**Instructors:** Tatsunori Hashimoto & Percy Liang
**Course Assistants:** Neil Band, Marcel Rød, Rohith Kuditipudi
**Focus:** A comprehensive, implementation-heavy course (5 units) where students build a language model from the ground up, covering data collection, architecture, systems optimization, and alignment.

## Course Philosophy
Inspired by operating systems courses, CS336 requires students to build every component of a language model with minimal scaffolding.

## Prerequisites
- High proficiency in Python; ability to write large-scale codebases
- Familiarity with PyTorch, GPU memory hierarchy, and systems optimization
- College Calculus, Linear Algebra, Probability/Statistics
- Prior deep learning experience (e.g., CS224N, CS229)

## Coursework & Assignments

### Assignment 1: Basics
Implement a tokenizer, Transformer architecture, and optimizer to train a minimal LM.
- Repo: https://github.com/stanford-cs336/assignment1-basics (1.6k ⭐)
- Data: TinyStories (GPT-4 generated stories), OpenWebText sample
- Key learning: full Transformer from scratch, tokenizer implementation

### Assignment 2: Systems
Profile models, implement FlashAttention2 using Triton, build memory-efficient distributed training.
- Repo: https://github.com/stanford-cs336/assignment2-systems (213 ⭐)
- Key learning: Triton kernel authoring, GPU memory optimization, distributed training

### Assignment 3: Scaling
Analyze Transformer components and use training APIs to fit scaling laws.
- Repo: https://github.com/stanford-cs336/assignment3-scaling (56 ⭐)
- Hosted training API at http://hyperturing.stanford.edu:8000
- Key learning: scaling law experiments, compute-optimal training

### Assignment 4: Data
Process raw Common Crawl dumps; implement filtering and deduplication.
- Repo: https://github.com/stanford-cs336/assignment4-data (49 ⭐)
- Key learning: web-scale data processing, deduplication, quality filtering

### Assignment 5: Alignment
Use SFT and RL for math reasoning. Optional: DPO for safety alignment.
- Repo: https://github.com/stanford-cs336/assignment5-alignment (143 ⭐)
- Supplemental: safety alignment, instruction tuning, RLHF (PDF included)
- Key learning: reinforcement learning for math reasoning, preference optimization

## Schedule (Spring 2025)
| Date | Topic | Milestone |
|------|-------|-----------|
| April 1 | Tokenization | Assignment 1 Out |
| April 15 | GPUs | Assignment 1 Due / Assignment 2 Out |
| April 30 | — | Assignment 2 Due |
| May 6 | Scaling Laws | Assignment 3 Due / Assignment 4 Out |
| May 23 | — | Assignment 4 Due / Assignment 5 Out |
| June 6 | — | Assignment 5 Due |

## Infrastructure
- Compute sponsored by Together AI
- GPU recommendation: H100 ($1.99-$3.29/hr via RunPod/Lambda Labs/Paperspace)
- Debug on CPU first; use GPUs only for final training runs

## Honor Code & AI Policy
- LLMs (ChatGPT) permitted for low-level/conceptual questions
- Prohibited: using AI to solve problems directly
- Discouraged: AI autocomplete (Cursor, Copilot)
