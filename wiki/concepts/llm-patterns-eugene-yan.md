---
title: "LLM Patterns (Eugene Yan)"
type: concept
created: 2026-05-04
updated: 2026-05-26
tags:
  - concept
  - evaluation
  - rag
  - fine-tuning
aliases:
  - "7 patterns for building LLM systems"
  - "yan-llm-patterns"
  - "llm-based-systems-patterns"
sources:
  - https://eugeneyan.com/writing/llm-patterns/
  - https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/
  - https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-ii/
  - https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-iii-strategy/
  - raw/articles/2023-07-30_eugeneyan-llm-patterns.md
  - raw/articles/2024-05-28_oreilly-applied-llms-part1.md
  - raw/articles/2024-05-31_oreilly-applied-llms-part2.md
  - raw/articles/2024-06-06_oreilly-applied-llms-part3.md
status: Level2
---

# LLM Patterns (Eugene Yan's Framework)

Seven practical patterns for integrating LLMs into production systems, proposed by **Eugene Yan**. First systematically organized in the July 2023 article "[Patterns for Building LLM-based Systems & Products](https://eugeneyan.com/writing/llm-patterns/)", later developed and revised in the O'Reilly co-authored work "[What We've Learned From a Year of Building with LLMs](https://oreilly.com)".

This framework is based on the philosophy that "development without evaluation is blind" in LLM application development, covering everything from data-centric improvement to user-facing design.

---

## Framework Overview

The 7 patterns form a spectrum from **data-centric → infrastructure → user-facing**:

```
Data/Internal      Infrastructure        User-Facing
  Evals     RAG     Caching      Guardrails      Defensive UX
  ↓         ↓         ↓             ↓                ↓
  Fine-tuning       (Infrastructure)          User Feedback
```

| Pattern | Goal | Focus | Category |
|---------|------|-------|----------|
| **Evals** | Measuring performance | Data/Internal | 🔵 Evaluation foundation |
| **RAG** | Injecting external knowledge | Data/Internal | 🔵 Knowledge augmentation |
| **Fine-tuning** | Task specialization | Data/Internal | 🔵 Model adaptation |
| **Caching** | Reducing latency and cost | Infrastructure | 🟢 Efficiency |
| **Guardrails** | Ensuring quality and safety | Infrastructure | 🟢 Quality assurance |
| **Defensive UX** | Graceful error handling | User-facing | 🟡 UX design |
| **User Feedback** | Data flywheel for improvement | User-facing | 🟡 Feedback loop |

**Evals is the foundation of everything** — improvement is impossible without measurement.

---

## Detailed Pattern Breakdown

### 1. Evals — Performance Measurement

The foundation of LLM engineering. Without evaluation, you're "flying blind."

**Key Metrics:**
- **BLEU/ROUGE** — n-gram based precision/recall. Poor correlation with human judgment for creative tasks
- **BERTScore/MoverScore** — Uses embeddings to account for synonyms and semantic similarity
- **LLM-as-a-Judge (G-Eval)** — Evaluating other models with a strong model (GPT-4). GPT-4 achieves ~85% agreement with human evaluators

**Implementation Tips:**
- **Eval Driven Development (EDD)** — Collect task-specific prompts and "ground truth" references before engineering
- **Mitigating LLM bias:** LLMs favor first answers (Position bias), longer answers (Verbosity bias), and their own outputs (Self-enhancement bias). Swap answer order during evaluation to counter Position bias

**Related Wiki Pages:**
- [[concepts/evals-for-ai-agents]] — Evaluation for AI agents (needs expansion)
- [[eugene-yan--core-ideas]] — Eugene Yan's EDD philosophy and AlignEval

#### NLI-based Hallucination Detection (OOD Finetuning)

Yan's empirical study ([Out-of-Domain Finetuning to Bootstrap Hallucination Detection](https://eugeneyan.com/writing/finetuning/)) formulates hallucination detection as an **NLI (Natural Language Inference) task**. The BART model is fine-tuned on MNLI to detect contradictions between source text (Premise) and summary (Hypothesis).

**OOD Bootstrapping Method:**
1. **Pre-fine-tuning (out-of-domain):** 3 epochs on Wikipedia dataset (USB). Does not improve scores on its own
2. **Main fine-tuning (target domain):** 10 epochs on News dataset (FIB). Pre-training functions as a "hidden foundation"

**Results (FIB validation set, @0.8 threshold):**

| Training Stage | PR AUC | Recall | Precision |
|----------------|--------|--------|-----------|
| No fine-tuning | 0.56 | Low | Low |
| FIB only (10 epochs) | 0.69 | 0.02 | 0.67 |
| USB (3 epochs) → FIB (10 epochs) | **0.85** | **0.50** | **0.91** |

- **25x Recall improvement:** USB pre-training increased Recall from 0.02 to 0.50
- **Hidden Learning:** Even when out-of-domain data shows no effect on its own, it prepares the model for main training
- **Practical threshold achievable:** Post-bootstrap probability distribution separation becomes clear, enabling a practical classification threshold (0.8)
- **Technology used:** Efficient fine-tuning with QLoRA

> **Lesson:** "Even if you don't have data fully relevant to your target task, pre-training on open-source related datasets can potentially reduce the fine-tuning data you need to collect."

---

### 2. RAG (Retrieval-Augmented Generation) — Injecting External Knowledge

Grounds the model in external, up-to-date data to reduce hallucinations and cost.

**Key Concepts:**
- **Dense Passage Retrieval (DPR)** — Dual encoder mapping queries and documents into the same vector space
- **Hybrid Search** — Combining keyword search (BM25) + semantic search (Embeddings). Outperforms either alone
- **HyDE (Hypothetical Document Embeddings)** — LLM generates hypothetical documents for the query, searches using those embeddings

**Vector Indexes:**
- **FAISS** — Efficient memory usage for billions of vectors
- **HNSW** — Graph structure for fast hierarchical search
- **ScaNN** — Google's approach. Best recall-latency tradeoff

**Related Wiki Pages:**
- [[concepts/agentic-rag]] — Agentic RAG evolution
- [[concepts/modern-retrieval-toolkit]] — Modern retrieval toolkit

---

### 3. Fine-tuning — Task Specialization

For improving performance, control, and modularity (using small specialized models).

**Key Methods:**
- **LoRA (Low-Rank Adaptation)** — Injects trainable low-rank decomposition matrices, updates only a small number of parameters
- **QLoRA** — Fine-tunes 4-bit quantized models. Enables 65B model tuning on a single 48GB GPU
- **Instruction Fine-tuning** — Trains base model on (instruction, output) pairs to create a helpful assistant

**Related Wiki Pages:**
- [[concepts/fine-tuning/peft-lora-qlora]] — LoRA/QLoRA details
- [[concepts/fine-tuning/instruction-fine-tuning]] — Instruction tuning
- [[concepts/fine-tuning/axolotl]] — Fine-tuning framework
- [[concepts/fine-tuning/unsloth]] — Fast fine-tuning

---

### 4. Caching — Reducing Latency and Cost

Caches previously computed LLM responses and reuses them for identical or similar future requests.

**Strategies:**
- **Semantic Caching** — Uses input embeddings as cache keys
- **Safe Caching** — Uses Item IDs or constrained inputs (e.g., dropdown selections) rather than natural language. Prevents incorrect "similar" answers
- **Pre-computation** — Pre-generates responses for popular queries offline. Reduces latency from seconds to milliseconds

---

### 5. Guardrails — Quality Assurance

Validates LLM output from syntactic, safety, and factual accuracy perspectives.

**Tools and Methods:**
- **Structural Guidance** — Uses structured generation (Guidance, Outlines, etc.) to force the model into specific grammars (e.g., JSON)
- **Syntactic/Semantic Checks:**
  - *Syntactic:* Whether SQL code is executable, whether values are in predefined lists
  - *Semantic:* Check if summary contradicts source text using LLM (SelfCheckGPT)
- **Input Guardrails** — Blocks adversarial and NSFW prompts before reaching the model

**Related Wiki Pages:**
- [[concepts/structured-outputs]] — Structured output methods
- [[concepts/coding-agents/ai-coding-reliability]] — AI coding reliability

---

### 6. Defensive UX — Graceful Error Handling

Assume LLMs will fail and design interfaces accordingly.

**Core Principles:**
- **Expectation setting:** "AI may generate inaccurate information" disclaimers calibrate trust
- **Easy dismissal:** Make it easy to ignore suggestions (like GitHub Copilot's ghost text)
- **Provide attribution:** Include citations or "social proof" for user verification
- **Familiar UI:** Use standard UI elements (buttons, lists) instead of cramming everything into a chat box

---

### 7. User Feedback — Data Flywheel

Feedback is the primary "moat" for LLM products, feeding future evaluation and fine-tuning.

- **Explicit feedback:** Thumbs up/down, "regenerate" button, star ratings
- **Implicit feedback:**
  - *Copilot:* Did the user press Tab to accept code?
  - *Midjourney:* Did the user upscale/download the image?
  - *Search:* Did the user click a result, refine the query?

---

## Framework Evolution

Yan's 7 patterns have evolved through co-evolution with the community into multiple versions:

| Version | Source | Patterns | Differences |
|---------|--------|----------|-------------|
| **v1 (2023.07)** | eugeneyan.com | Evals, RAG, Fine-tuning, Caching, Guardrails, Defensive UX, User Feedback | Original version. Includes Caching/Guardrails/Defensive UX/User Feedback |
| **v2 (2024.06)** | O'Reilly co-authored "Applied LLMs" | Part I (Tactical): Prompting, RAG, Flow Engineering, Evals<br>Part II (Operations): Data, Models, Product, Team<br>Part III (Strategy): Resource Allocation, System Moat, Human-Centered AI, Economics | Expanded to 3-part structure. Tactical → Operations → Strategy hierarchy. 6 co-authors. |

**O'Reilly version (Applied LLMs Guide) 3-layer structure:**

```mermaid
Part I: Tactical (How?)
  Prompting Tactics → RAG → Flow Engineering → Evaluation
        ↓
Part II: Operations (Who? With what?)
  Data Ops → Model Management → Product Design → Team/Roles
        ↓
Part III: Strategy (Why? What's next?)
  Resource Allocation → Competitive Advantage → Product Strategy → Economics
```

The O'Reilly guide (commonly known as "Applied LLMs") is available at [applied-llms.org](https://applied-llms.org/), authored by 6 co-authors (Eugene Yan, Bryan Bischof, Charles Frye, Hamel Husain, Jason Liu, Shreya Shankar). It has become the de facto standard reference for the community.

---

## O'Reilly Applied LLMs Guide — Detailed Content

### Part I: Tactical — How to Build

#### 1. Prompting Tactics
- **N-Shot Prompts:** Provide 5+ examples. Select examples representative of the distribution
- **Chain-of-Thought:** Specify concrete steps rather than just "step-by-step" ("1. sketchpad for decision-making, 2. consistency check, 3. integration")
- **Structured I/O:** Instructor (for APIs), Outlines (for self-hosted). Claude prefers XML, GPT prefers Markdown/JSON
- **God Prompt Anti-Pattern:** Avoid 2000-token giant prompts; split into small pipelines
- **Response Pre-filling for Claude:** Pre-write responses in the assistant role to guide direction

#### 2. RAG (Retrieval-Augmented Generation)
- **3 Quality Factors:** Relevance (MRR/NDCG measurement), information density, metadata richness
- **Hybrid Search is Standard:** "Vector embeddings don't magically solve search" — Aravind Srinivas. BM25 (names/acronyms/IDs) + Embeddings (synonyms/multimodal)
- **Why Long Context Doesn't Kill RAG:** Linear cost increase; even with ultra-long context, models are overwhelmed by "distractors"

#### 3. Flow Engineering (Workflow Optimization)
- Moving from single prompt to flow dramatically improves accuracy (AlphaCodium: GPT-4 19%→44%)
- **Determinism First:** Agent generates plan (DAG), executes deterministically for easy debugging
- **Ensuring diversity:** Beyond Temperature, shuffle input order, rephrase prompts, "recent output list" for avoidance instructions
- **Caching:** Cache static content with unique IDs for zero latency/cost

#### 4. Evaluation & Monitoring
- **Intern Test:** If a college intern can't do it in 10 minutes, the LLM will also fail
- **LLM-as-Judge Best Practices:** Pairwise comparison, swap evaluation order (against Position bias), allow tie judgments
- **Assertion-based testing:** Unit tests from real production samples. For code generation, verify up to execution
- **Hallucination Problem:** Baseline 5-10%; even after optimization, under 2% is difficult. Downstream Factual Inconsistency Guardrails

---

### Part II: Operations — Who Builds and With What

#### 1. Data Operations
- **Development-Production Skew:** Structural skew (format mismatch), semantic skew (topic/intent change). Detect via embedding clusters
- **Daily Vibe Check:** Visually inspect I/O samples daily. When finding failures, immediately write code assertions or evaluations
- **Criteria Drift:** The more data you see, the more your "good/bad" judgment criteria shift. Build this into operational processes

#### 2. Working with Models
- **Postel's Law for LLMs:** "Accept free-form natural language on input, return typed machine-readable objects on output"
- **Model Pinning:** Always pin a specific version (e.g., gpt-4-turbo-1106). Expect ~10% performance variation even within-family upgrades
- **Shadow Pipelines:** Run old and new models in parallel, switch after stability confirmation
- **Model Selection:** Use the smallest model that can complete the job. Claude Haiku + 10-shot > GPT-4 zero-shot. For classification, DistilBERT achieves 0.84 ROC-AUC at <5% of LLM cost

#### 3. Product Design
- **Suggestion Pattern:** LLM suggests → human verifies/edits, rather than full automation
- **Implicit Feedback:** Acceptance = strong positive, regeneration = strong negative
- **Hierarchy of Needs:** Prioritize reliability and harmlessness. Don't demand perfection in usefulness and cost from the start

#### 4. Team and Roles
- **Role Evolution:** AI Engineer (prototyping/UX) → Data/Platform Engineer (instrumentation/data) → ML Engineer (optimization). Early adoption of MLE is a waste of resources
- **EvalGen Principle:** Define domain-specific tests, align with human judgment, iterate tests in response to changes
- **Culture:** Teach prompt engineering across the entire team, discover innovative UX through hackathons

---

### Part III: Strategy — Why Build and What's Next

#### 1. Resource Allocation
- **"No GPUs Before PMF":** Don't invest in training infrastructure before achieving Product-Market Fit
- **Training from scratch is a distraction:** Even BloombergGPT was surpassed by GPT-4 within a year
- **Build vs. Buy:** Validate with APIs → self-host only when scale/privacy requires it (BuzzFeed reduced costs 80% via fine-tuning)

#### 2. Competitive Advantage
- **Invest in the "system moat":** Evaluation infrastructure, Guardrails, Caching, data flywheel — these persist after model swaps
- **Strategic deferral:** Don't build features that model providers will solve themselves (e.g., function call validation)

#### 3. Human-Centered AI
- **Centaur Paradigm:** Capable humans + LLM tools in combination, not full replacement
- **Narrow the Scope:** Generic "chat with your data" is shallow. Specialize in domain-specific formats
- **Avoid "Sparkle" Features:** Don't allocate resources to commoditizing vanity features (document chatbots)

#### 4. Economics of "Low-Cost Cognition"
- **Halving every 6 months:** text-davinci-003 equivalent performance went from $20 → $0.20/1M tokens (1/100 in 18 months)
- **Strategic prediction:** Today's high-cost applications ($60/hour game NPCs) will be economically viable in 12-24 months
- **Insight:** "Today's unrealistic demos become premium features in a few years, and commodities after that"

#### 5. From Demos to Products
- "The first neural-network-powered car was in 1988... it took 35 years from prototype to commercial product"
- The shift from 0→1 (demo) to 1→N (scalable product) is the true challenge

---

## Related Wiki Pages

- [[entities/eugene-yan]] — Framework proponent, lead author of Applied LLMs Guide
- [[entities/eugene-yan--core-ideas]] — Yan's core ideas and framework list
- [[entities/bryan-bischof]] — Applied LLMs Guide co-author
- [[entities/charles-frye]] — Applied LLMs Guide co-author
- [[entities/hamel-husain]] — Applied LLMs Guide co-author
- [[entities/jason-liu]] — Applied LLMs Guide co-author (Instructor library author)
- [[entities/shreya-shankar]] — Applied LLMs Guide co-author
- [[concepts/evals-for-ai-agents]] — AI agent evaluation (needs expansion)
- [[concepts/agentic-rag]] — RAG's agentic evolution
- [[concepts/fine-tuning/peft-lora-qlora]] — PEFT/LoRA/QLoRA
- [[concepts/fine-tuning/instruction-fine-tuning]] — Instruction tuning
- [[concepts/structured-outputs]] — Structured outputs
- [[concepts/coding-agents/ai-coding-reliability]] — AI coding reliability and guardrails
