---
title: Stanford CS336 — Language Modeling from Scratch
type: concept
created: 2026-05-04
updated: 2026-05-26
status: Level2
tags:
  - education
  - curriculum
  - training
  - alignment
aliases: [cs336, language-modeling-from-scratch, hashimoto-liang-course]
sources:
  - https://stanford-cs336.github.io/spring2025/
  - raw/articles/2026-05-04_stanford-cs336-syllabus.md
---

# Stanford CS336: Language Modeling from Scratch

> A **Stanford implementation-intensive course (5 units)** by **Tatsunori Hashimoto & Percy Liang**. Inspired by OS courses, students **build a complete language model from scratch**. The curriculum centers on **5 large-scale implementation assignments** rather than lectures. Offered Spring 2025.

---

## Why This Course Is Special

Listed in Yoav Goldberg's guide as the only course given special treatment for being "a tech/ML class that covers the nitty-gritty details of LLM training." Notable points:

1. **Zero-build philosophy** — From tokenizer implementation to Transformer construction, Triton kernel coding, Common Crawl processing, and RL alignment. The "build everything yourself" approach of OS courses
2. **Cutting-edge tech stack** — FlashAttention2 via Triton, uv package management, CI/CD including AGENTS.md/CLAUDE.md. Reflects 2025 best practices
3. **GPU cost guide included** — Practical pricing: RunPod $1.99-2.99/h, Lambda Labs $2.49-3.29/h
4. **Open-source assignments** — All 5 assignments published on GitHub, 1.6k–56 ⭐

---

## Curriculum Details & Wiki Mapping

### Assignment 1: Basics (Transformer from Scratch)

| Implementation Item | What You Learn | Related Wiki Concept |
|---------|-----------|-------------|
| BPE Tokenizer | Full understanding of subword segmentation | `concepts/decoder-only-gpt` (tokenization section) |
| Transformer Architecture | Attention, Feed-Forward, LayerNorm, Positional Encoding | `concepts/decoder-only-gpt`, `concepts/transformer-architecture`, `concepts/attention-mechanism-variants` |
| Optimizer (AdamW) | Learning rate scheduling, weight decay | — |
| Training Loop | Forward/backward, loss calculation, perplexity evaluation | `concepts/llm-core` |
| Data: TinyStories + OpenWebText | Comparing GPT-4-generated data with real web data | `concepts/local-llm` (data-related) |

> **Unique value:** By implementing the tokenizer yourself, you can **experience firsthand** how BPE operation and vocabulary choices affect model quality. Training on both TinyStories (GPT-4-generated children's stories) and OpenWebText (real web scrapes) allows comparison of data distribution effects.

### Assignment 2: Systems (GPU Optimization & Distributed Training)

| Implementation Item | What You Learn | Related Wiki Concept |
|---------|-----------|-------------|
| GPU Profiling | Diagnosing memory bandwidth and compute bounds | `concepts/ai-infrastructure-engineering/gpu-vram-fundamentals` |
| **Triton FlashAttention2** | Custom CUDA kernel authoring | `concepts/flashattention-pytorch-educational` |
| Memory-Efficient Transformer | Activation checkpointing, recomputation | `concepts/context-compression` |
| Distributed Data Parallel (DDP) | Multi-GPU training fundamentals | `concepts/ai-infrastructure-engineering/distributed-training` |

> **Unique value:** You actually **write custom Triton kernels**. Rather than using FlashAttention as a black box, implementing it yourself in Triton — a skill very few engineers have — is the **single biggest differentiator**.

### Assignment 3: Scaling (Experimental Validation of Scaling Laws)

| Implementation Item | What You Learn | Related Wiki Concept |
|---------|-----------|-------------|
| Scaling Law Fitting | Empirical validation of Chinchilla Optimal Model Size | — (concept page not yet created) |
| API Training Runner | Calling distributed training APIs and collecting results | — |
| Loss Prediction Model | IsoFLOP contours, parameter prediction | — |

> **Unique value:** You can **empirically validate** scaling laws (Chinchilla, Kaplan et al.) — which you know as theory — with your own training runs. Using Stanford's training API (hyperturing.stanford.edu), you measure loss across different model size × data amount combinations.

### Assignment 4: Data (Common Crawl Processing)

| Implementation Item | What You Learn | Related Wiki Concept |
|---------|-----------|-------------|
| Common Crawl Download & Parsing | WARC format, large-scale data pipelines | — |
| Filtering (Quality, Dedup, PII) | Automated data quality assessment | `concepts/fine-tuning/quantization-overview` (data quality related) |
| Deduplication (MinHash, exact dedup) | Large-scale data dedup algorithms | — |
| Training on Filtered Data | Measuring data quality's impact on final model performance | — |

> **Unique value:** You get hands-on experience with Common Crawl processing — **the most important element** of LLM training that most courses skip. Uniquely, you can **quantitatively compare** how different filtering strategies affect final model performance.

### Assignment 5: Alignment (SFT + RL + DPO)

| Implementation Item | What You Learn | Related Wiki Concept |
|---------|-----------|-------------|
| SFT (Supervised Fine-Tuning) | Supervised tuning on math reasoning datasets | `concepts/fine-tuning/instruction-fine-tuning`, `concepts/fine-tuning/trl` |
| RL for Math Reasoning | GRPO-style reinforcement learning | `concepts/grpo-rl-training`, `concepts/fine-tuning/rlhf-dpo-preference` |
| DPO (Optional) | Direct Preference Optimization | `concepts/fine-tuning/rlhf-dpo-preference` |
| Safety Alignment (Supplementary) | Instruction tuning, RLHF safety assurance | `concepts/ai-safety` |

> **Unique value:** You can implement **RL for math reasoning** — a cutting-edge topic as of 2025 — as a course assignment. Understand the difference between GRPO/PPO at the code level, and experience the improvement in reasoning capabilities that SFT alone cannot achieve. A supplementary Safety Alignment PDF is also provided.

---

## Limitations of This Course

- **Minimal lectures** — Assignments are the primary curriculum. Theoretical background must be self-studied
- **GPU costs** — Expect $50–200 in total GPU costs across all assignments
- **Coverage bias** — RAG, agents, evaluation, and multimodal are not covered. Focused on "how to build and train LLMs"
- **Spring 2025 snapshot** — Does not include cutting-edge topics from 2026 (RLM, Mythos, Agent Harness, etc.)

---

## Position in Learning Priority

| Aspect | CS336 | Alternative Courses |
|------|-------|-----------|
| Implementation depth | 🟢 **Highest. Build every component yourself** | Princeton COS597R: Paper-based, no implementation |
| Theoretical depth | 🔵 Learn through implementation (discovery-based) | Princeton COS597R: Paper-based, systematic |
| Application scope | ⚪ LLM training specialization | CMU LLMs: General applications |
| Cost | 🟡 GPU $50–200 | Free (paper reading only) |
| Prerequisites | 🔵 Python proficiency required | COS597R: DL basics, CMU: Light |

---

## Related Wiki Pages

- [[concepts/llm-course-roadmap]] — Similarities with Maxime Labonne's LLM Course (overlaps with Part 2: The Scientist)
- [[concepts/learning-llms-in-2025]] — Yoav Goldberg's comprehensive guide
- [[concepts/gpt/decoder-only]] — Architecture implemented in Assignment 1
- [[concepts/flashattention-pytorch-educational]] — FlashAttention implemented in Assignment 2
- [[concepts/grpo-rl-training]] — RL method implemented in Assignment 5
- [[concepts/fine-tuning/rlhf-dpo-preference]] — Preference optimization covered in Assignment 5
- [[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]] — Prerequisite knowledge for Assignment 2
- [[concepts/fine-tuning/trl]] — HuggingFace TRL used in Assignment 5

---

> **This page is meta-knowledge (knowledge map).** It maps the Stanford CS336 curriculum structure to Wiki concepts, showing the correspondence between each Assignment's learning content and existing Wiki pages. For actual assignment content, refer to each GitHub repository.
