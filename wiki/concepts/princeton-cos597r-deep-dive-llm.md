---
title: Princeton COS597R — Deep Dive into Large Language Models
type: concept
created: 2026-05-04
updated: 2026-05-04
status: Level2
tags:
  - education
  - curriculum
  - lab
  - optimization
  - alignment
  - reasoning
  - interpretability
aliases: [cos597r, princeton-llm, deep-dive-llm]
sources:
  - https://princeton-cos597r.github.io/
  - raw/articles/2026-05-04_princeton-cos597r-syllabus.md
---

# Princeton COS597R: Deep Dive into Large Language Models

> A **paper-based LLM research survey course** by **Danqi Chen & Sanjeev Arora (Princeton)**. Covers the full spectrum of LLM research: scaling laws, data curation, alignment, reasoning, RAG, and hardware. Research-oriented, emphasizing **conceptual understanding and critical thinking** over implementation. Offered Fall 2024.

---

## Why This Course Is Special

1. **Renowned Instructors** — Chen (long-context & knowledge editing specialist) + Arora (theorist) cover both theory and practice
2. **Paper-based deep dives** — 1-2 key papers per session. Lectureship system (students write lecture notes) documents discussions
3. **Debate Panel Format** — Presenter + 2 Critics + 2 Proponents structure trains critical evaluation of papers
4. **Best Snapshot of Fall 2024** — Provides the full picture of LLM research post-GPT-4, post-Llama 3, post-DPO

---

## Curriculum Details & Wiki Mapping

### Phase 1: Pre-training & Scaling (September)

| Week | Topic | Key Paper | Related Wiki Concepts |
|----|---------|-------------|-------------|
| 1-2 | Pre-training | GPT-3 (*Language Models are Few-Shot Learners*), Llama 3 | `concepts/decoder-only-gpt`, `concepts/transformer-architecture` |
| 3 | Scaling Laws | Chinchilla (*Training Compute-Optimal LLMs*) | — (scaling laws concept page not yet created) |
| 4 | Emergent Abilities | *Are Emergent Abilities a Mirage?* | — (not yet covered) |

> **Relation to CS336:** Both cover scaling laws, but COS597R focuses on **reading papers to understand concepts**, while CS336 focuses on **experimentally verifying** them. Doing both is most effective.

### Phase 2: Data & Post-Training (Late September - October)

| Week | Topic | Key Paper | Related Wiki Concepts |
|----|---------|-------------|-------------|
| 4 | Data Curation | Dolma (3T tokens), Phi-1.5 (data quality vs. quantity) | — (data curation concept page not yet created) |
| 5 | Instruction Tuning | FLAN, Tulu | `concepts/fine-tuning/instruction-fine-tuning` |
| 6 | Preference Learning | InstructGPT, DPO | `concepts/fine-tuning/rlhf-dpo-preference` |
| 7 | Constitutional AI | *Harmlessness from AI Feedback* | `concepts/ai-safety` |
| 7 | Weak-to-Strong | Weak-to-Strong Generalization | `concepts/ai-safety` (related) |

> **Unique Value:** The strength of this course is the **paper-level comparison of DPO and RLHF**. Reading InstructGPT (the origin of RLHF) and DPO (its simplification) in the same week and debating them in the Panel.

### Phase 3: Advanced Capabilities (October - November)

| Week | Topic | Key Paper | Related Wiki Concepts |
|----|---------|-------------|-------------|
| 8 | Long Context | RoPE, Long-context training | `concepts/attention-mechanism-variants`, `concepts/kv-cache` |
| 9 | Reasoning | *Let's Verify Step by Step*, Test-Time Compute Scaling | `concepts/grpo-rl-training` (indirect), `concepts/exec-plans` |
| 10 | Small Models | Sheared LLaMA, Gemma 2 | `concepts/model-quantization`, `concepts/fine-tuning/quantization-overview` |
| 11 | RAG | *Retrieval from trillions of tokens* | `concepts/agentic-rag` |
| 12 | Agents | LLM → Autonomous Agents evolution | `concepts/agent-harness`, `concepts/agent-orchestration-frameworks` |

> **Unique Value:** Includes **Test-Time Compute Scaling** (the foundational paper for OpenAI o1) in the curriculum. One of the few courses to cover this groundbreaking paper as of Fall 2024.

### Phase 4: Special Topics (November)

| Week | Topic | Key Paper | Related Wiki Concepts |
|----|---------|-------------|-------------|
| 13 | Hardware | FlashAttention, Mamba | `concepts/flashattention-pytorch-educational`, `concepts/local-llm/gguf` (indirect) |
| 14 | Multimodal | Visual Grounding (Saining Xie) | `concepts/ai-image-generation` |
| 14 | Pruning/Distillation | — | — |

---

## Limitations of This Course

- **Zero implementation** — No coding at all. Focuses on conceptual understanding; unsuitable for those who want hands-on practice.
- **Frozen as of Fall 2024** — GRPO, test-time compute scaling (post-o1), RLM, Agent Harness, Claude Mythos, etc. are not covered.
- **Paper reading proficiency required** — Load of 1-2 papers per week. Prerequisite knowledge equivalent to COS484 (Deep Learning) is needed.
- **Active participation assumed** — Pre-lecture form submission + Debate Panel + Lecture Scribing. Self-study is limited to using Scribe notes + paper lists.

---

## Position Within Learning Priorities

| Aspect | COS597R | Alternative Course |
|------|---------|-----------|
| Research Skills | 🟢 **Best. Paper close-reading + critical discussion** | CS336: Focus on implementation skills |
| LLM Knowledge Breadth | 🟢 Full range from pre-training to deployment | CMU LLMs: Application-focused, theory is light |
| Implementation Experience | ⚪ None | CS336: Full implementation |
| Participation Barrier | 🔵 Paper reading proficiency required | CMU LLMs: Most beginner-friendly |
| Accessibility | 🟢 All materials public, rich Scribe notes | — |

---

## Related Wiki Pages

- [[concepts/learning-llms-in-2025]] — Yoav Goldberg's comprehensive guide
- [[concepts/stanford-cs336-language-modeling-from-scratch]] — The implementation-focused counterpart
- [[concepts/decoder-only-gpt]] — The underlying architecture for the entire course
- [[concepts/fine-tuning/rlhf-dpo-preference]] — Preference optimization (Week 6)
- [[concepts/grpo-rl-training]] — Follow-up on test-time compute (extension of Week 9)
- [[concepts/flashattention-pytorch-educational]] — FlashAttention (Week 13)
- [[concepts/agentic-rag]] — RAG (Week 11)
- [[concepts/ai-safety]] — Constitutional AI (Week 7)
- [[concepts/kv-cache]] — Long context (Week 8)
- [[concepts/attention-mechanism-variants]] — RoPE (Week 8)

---

> **This page is meta-knowledge (a knowledge map).** It maps the Princeton COS597R curriculum structure and paper roadmap onto Wiki concepts. For actual lecture notes and papers, please refer to princeton-cos597r.github.io.
