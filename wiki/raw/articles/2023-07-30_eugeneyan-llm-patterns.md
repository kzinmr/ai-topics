---
title: "Patterns for Building LLM-based Systems & Products"
source: https://eugeneyan.com/writing/llm-patterns/
author: Eugene Yan (Ziyou Yan)
date: 2023-07-30
tags: [llm, patterns, evals, rag, fine-tuning, caching, guardrails, ux, user-feedback]
---

# Patterns for Building LLM-based Systems & Products

By **Eugene Yan** — Originally published July 2023, one of the most-read posts on eugeneyan.com (62.4K+ views).

This guide outlines seven practical patterns for integrating Large Language Models (LLMs) into production-grade products, moving from data-centric improvements to user-facing design.

---

## 1. Evals: Measuring Performance
Evaluations are the foundation of LLM engineering. Without them, developers are "flying blind."

### Key Metrics
- **BLEU/ROUGE:** Precision/Recall based on n-gram overlaps. Popular but often correlate poorly with human judgment for creative tasks.
- **BERTScore/MoverScore:** Use embeddings to account for synonyms and semantic similarity.
- **LLM-as-a-Judge (G-Eval):** Using a strong model (e.g., GPT-4) to evaluate another model. GPT-4 has shown ~85% agreement with human evaluators.

### Implementation Tips
- **Eval Driven Development (EDD):** Collect task-specific prompts and "gold" references before engineering.
- **Mitigate LLM Bias:** LLMs favor the first response (Position bias), longer responses (Verbosity bias), and their own outputs (Self-enhancement bias). Swap response orders during evaluation to counter position bias.

---

## 2. Retrieval-Augmented Generation (RAG)
RAG grounds models in external, up-to-date data to reduce hallucinations and cost.

### Key Concepts
- **Dense Passage Retrieval (DPR):** Uses dual encoders to map queries and documents into the same vector space.
- **Hybrid Search:** Combining keyword search (BM25) with semantic search (Embeddings) is often superior to either alone.
- **HyDE (Hypothetical Document Embeddings):** Given a query, first prompts an LLM to generate a hypothetical document, then encodes it into an embedding vector.

### Vector Indices for Scale
- **FAISS:** Efficient memory use for billions of vectors.
- **HNSW:** Graph-based structure for fast, hierarchical search.
- **ScaNN:** Google's approach; often provides the best recall-latency trade-off.

---

## 3. Fine-tuning: Task Specialization
Fine-tuning is used for performance, control, and modularization (using smaller, specialized models).

### Techniques
- **LoRA (Low-Rank Adaptation):** Updates only a small subset of parameters by injecting trainable rank decomposition matrices.
- **QLoRA:** Fine-tunes 4-bit quantized models, allowing a 65B model to be tuned on a single 48GB GPU.
- **Instruction Fine-tuning:** Training base models on (instruction, output) pairs to make them helpful assistants.

---

## 4. Caching: Reducing Latency & Cost
Caching stores previously computed LLM responses to serve future identical or similar requests.

### Strategies
- **Semantic Caching:** Keying the cache on the embedding of the input.
- **Safe Caching:** Use Item IDs or constrained inputs (e.g., dropdown selections) rather than just natural language to avoid serving the wrong "similar" answer.
- **Pre-computation:** Generating responses for popular queries offline to shift latency from seconds to milliseconds.

---

## 5. Guardrails: Ensuring Quality
Guardrails validate LLM outputs for syntax, safety, and factuality.

### Tools & Methods
- **Structural Guidance:** Using tools like Microsoft's Guidance to force the model to follow a specific grammar (e.g., valid JSON).
- **Syntactic/Semantic Checks:**
  - *Syntactic:* Checking if SQL code is executable or if a value is in a predefined list.
  - *Semantic:* Using an LLM to check if a summary is consistent with the source text (SelfCheckGPT).
- **Input Guardrails:** Blocking adversarial or NSFW prompts before they reach the model.

---

## 6. Defensive UX: Managing Errors
Anticipate that LLMs will fail and design the interface to handle it gracefully.

### Core Principles
- **Set Expectations:** Disclaimers (e.g., "AI may produce inaccurate info") help users calibrate trust.
- **Efficient Dismissal:** Make it easy to ignore suggestions (e.g., GitHub Copilot's ghost text).
- **Provide Attribution:** Include citations or "social proof" (e.g., "Because you liked X") to help users verify information.
- **Anchor on Familiarity:** Use standard UI elements (buttons, lists) rather than forcing everything into a chat box.

---

## 7. User Feedback: The Data Flywheel
Feedback is the primary "moat" for LLM products, fueling future evals and fine-tuning.

- **Explicit Feedback:** Thumbs up/down, "Regenerate" buttons, or star ratings.
- **Implicit Feedback:**
  - *Copilot:* Did the user hit Tab to accept the code?
  - *Midjourney:* Did the user upscale or download the image?
  - *Search:* Did the user click the result or refine their query?

---

## Summary Table: The LLM Pattern Spectrum

| Pattern | Goal | Focus |
|:---|:---|:---|
| **Evals** | Measure Performance | Data/Internal |
| **RAG** | Add Knowledge | Data/Internal |
| **Fine-tuning** | Task Excellence | Data/Internal |
| **Caching** | Reduce Cost/Latency | Infrastructure |
| **Guardrails** | Ensure Quality | Infrastructure |
| **Defensive UX** | Manage Errors | User-Facing |
| **User Feedback** | Drive Improvement | User-Facing |

The patterns form a spectrum: data-centric → infrastructure → user-facing. Evals underpin all other patterns — without measurement, improvement is impossible.
