---
title: "Machine Studying — Agents Developing Expertise from Corpora"
created: 2026-06-17
updated: 2026-06-17
type: concept
tags:
  - training
  - evaluation
  - ai-agents
  - inference
  - rag
  - context-engineering
  - fine-tuning
  - memory-systems
sources:
  - https://jacobxli.com/blog/2026/machine-studying/
  - https://huggingface.co/datasets/jacobli/studybench
---

# Machine Studying

**Machine Studying** is a problem formulation introduced by Jacob Xiaochen Li, Rick Battle, and Omar Khattab (MIT CSAIL / Broadcom, June 2026): given nothing but a corpus **D = (d₁, …, dₙ)**, can AI systems autonomously develop **expertise** in the underlying domain?

> *"Humans can turn reading a textbook and actively thinking about the material into deep knowledge and even expertise. Why can't agents yet?"*

## Core Definitions

### Expertise
An expert in a domain D is **an agent that can *efficiently* turn inference compute into accurate work**. Measured as the *weighted area* under the agent's performance curve as inference compute grows. A sharp novice might brute-force an open-book exam, but only an expert produces high-quality answers with ease.

### Studying Algorithm
Whatever the agent does **to itself** using D before anything is known about downstream evaluation. May update weights or anything in the agent's [[concepts/context-engineering|harness]]. Critically, the agent **retains full access to the corpus at test time** — the question is how much expertise it develops, not whether it memorizes the corpus.

### Studying Intelligence
The efficiency with which an agent can develop expertise in a new subject. By this measure, current agents are not very intelligent yet.

## Three Paradigms for Studying

### 1. Self-Supervised Objectives
Compress the corpus into weights via ML objectives (next-token prediction, test-time training, KV cache compaction).

**Approach tested:** Continual pre-training (CPT) — LoRA adapters trained on raw corpus text. CPT(code) on DSPy codebase (459k tokens), CPT(doc) on documentation (160k tokens). Risk: degrades post-training abilities (instruction following), mitigated by mixing in self-sampled coding traces.

**Limitation:** Encodes limited domain biases; NTP objective tries to teach every part of the corpus but doesn't necessarily build *expertise*.

### 2. Synthetic Data & Environments
Models synthesize their own training data — entity-rich retellings, synthetic Q&A, active reading strategies, self-edits.

**Approach tested:** Synthetic fine-tuning (SFT) — larger model (DeepSeek-V4-Flash) generates Q&A pairs from codebase, smaller model trains on them. On-policy distillation (OPSD) recovers general behavior.

**Extension:** On-policy RL with self-synthesized environments. [[entities/omar-khattab|Pedagogical RL]] guides sampling with privileged information.

**Limitation:** Serious difficulty scaling; synthesized environments may not align with unseen tasks.

### 3. Amortized Context Management
Skip weight updates — agents manage notes in prompts or environment. Related to [[concepts/knowledge-storage-spectrum|Knowledge Storage Spectrum]].

**Approach tested:** Cheatsheet — agent explores repository for dozens of steps, writes itself a note prepended to every future question.

**Connection to our wiki:** This paradigm is essentially what [[concepts/llm-wiki|Karpathy's LLM Wiki]] pattern does — compiling documents into a maintained wiki. Also maps to `skill.md` files and context engineering practices.

## StudyBench Benchmark

Two tasks measuring agent expertise acquisition:
- **Studying-DSPy**: Expertise in the [[concepts/dspy|DSPy]] library (small API surface, deliberately minimal)
- **Studying-OpenClaw**: Expertise in the OpenClaw domain

Evaluation across inference budgets (0, 5, 20, forced full) with strict and lenient grading.

## Key Findings (Qwen3.5-9B)

| Approach | DSPy (lenient) | DSPy (strict) | Notes |
|---|---|---|---|
| Original (no study) | 3.3 → 11.6% | 0 → 2.0% | Baseline |
| CPT(code) | 5.1 → 7.0% | 0.8 → 1.0% | Modest gains, degrades at high budget |
| CPT(doc) | 3.8 → 6.2% | 0% | Doc-only less effective than code |
| SFT + OPSD | 9.4 → 8.5% | 1.1 → 0% | Strong at low budget, degrades |

**Core insight:** Memorization ≠ expertise. Retrieval ≠ expertise. Weight updates alone don't reliably produce expertise. The bottleneck is not "getting knowledge into the model" but developing the *efficiency* of using that knowledge.

## Stale Knowledge Problem

GPT-5.1 calls DSPy APIs that existed in 2024 but were since deprecated. Stronger model, worse expertise on a domain that evolved between training cutoffs. This is the **stale knowledge** problem that machine studying aims to solve.

## Relationship to Existing Concepts

| Concept | Relationship to Machine Studying |
|---|---|
| [[concepts/rag-systems\|RAG]] | Studying ≠ retrieval. RAG treats knowledge as lookup; studying builds understanding |
| [[concepts/dspy\|DSPy]] | Both task and tool — DSPy is used as StudyBench domain; DSPy optimizers could be studying algorithms |
| [[concepts/knowledge-storage-spectrum\|Knowledge Storage Spectrum]] | Studying spans the spectrum: weights (CPT), context (cheatsheets), retrieval (search) |
| Continual Learning | Machine studying is a *subset* — focused on expertise from new corpora, not just avoiding forgetting |
| [[entities/omar-khattab\|Omar Khattab]] | Co-author; studying connects to his work on programmatic LM control |
| Context Engineering | Cheatsheet approach = automated context engineering for expertise |

## Why This Matters

Machine studying is described as "a central and unrecognized bottleneck for downstream AI success." Current agents engage with new domains in shallow, hand-engineered ways. If solved, it enables:
- **Cheap custom experts**: Point a studying agent at any corpus
- **Auditable expertise**: Study notes are human-readable (unlike fine-tuned weights)
- **Updatable knowledge**: New paper → another iteration, no retraining
- **Bottleneck shift**: From "get knowledge into model" to "curate corpus and validate synthesis"

## Open Questions

- Can on-policy RL teach *knowledge* (not just *skills*) at reasonable efficiency?
- Will synthesized environments align with unseen downstream tasks?
- Can weight updates and context management be combined effectively?
- How to measure expertise efficiency independent of model scale?
