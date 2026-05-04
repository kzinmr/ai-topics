---
title: "AI Design Patterns for Information Professionals (Boring AI)"
type: concept
created: 2026-05-04
updated: 2026-05-04
status: Level1
tags:
  - GLAM
  - design-patterns
  - boring-ai
  - structured-extraction
  - cultural-heritage
  - information-professionals
  - huggingface
  - evaluation
aliases:
  - boring-ai
  - ai-patterns-for-glam
  - GLAM AI patterns
sources:
  - https://danielvanstrien.xyz/ai-patterns-for-glam/
  - https://danielvanstrien.xyz/ai-patterns-for-glam/intro.html
  - raw/articles/2026-03-23_ai-patterns-for-glam-welcome.md
---

# AI Design Patterns for Information Professionals (Boring AI)

> **Work in progress** — A practical pattern language for applying AI to information work in Galleries, Libraries, Archives, Museums (GLAM), charities, newsrooms, and any organisation managing large collections without a dedicated ML team.
> **Author:** [[entities/daniel-van-strien]] — Machine Learning Librarian at Hugging Face
> **Published:** March 23, 2026 (early draft)

## Philosophy: The Case for Boring AI

Most discussions about AI focus on chatbots, generative AI, and autonomous agents. But for information professionals, the most impactful uses of AI are **deliberately mundane**:

- Extracting structured data from scanned documents
- Classifying items in a backlog
- Pulling metadata from thousands of PDFs
- Cleaning and standardising legacy records
- OCR correction and quality assessment

These tasks aren't glamorous, but they represent **real bottlenecks** that organisations face every day:
- A library sitting on 250,000 unindexed manuscript cards
- A charity with decades of case files that need categorising
- A newsroom with thousands of leaked documents to sift through

The key insight: AI tools and models change rapidly (a state-of-the-art model may be superseded within months), but the **problems** information professionals face — and the broad strategies for solving them — are far more stable.

## Pattern Language Approach

The book applies Christopher Alexander's concept of **design patterns** (*A Pattern Language*, 1977) to AI in information work. Each pattern documents:

| Element | Description |
|---------|-------------|
| **Problem** | The specific bottleneck or challenge |
| **Worked Example** | Real data from the National Library of Scotland |
| **Evaluation** | How to know if it's working — rigorous measurement without an ML team |
| **Trade-offs** | When to use this pattern vs. alternatives |

Patterns give practitioners a shared vocabulary for discussing solutions without getting lost in implementation details. The specific models and libraries will evolve, but the patterns remain useful.

## The Four-Stage Framework

The book is organised around four key stages of an AI project in information-rich organisations:

### 1. Discovery
How to identify where AI can genuinely help, and how to avoid common pitfalls when scoping projects. Focuses on:
- Bottleneck analysis — is AI actually the right tool?
- Stakeholder mapping — who benefits and who is affected?
- Risk assessment — what happens if the model is wrong?
- Pilot design — starting small, measuring outcomes

### 2. Design Patterns (Structured Extraction)
Reusable approaches to common tasks, starting with structured information extraction — turning unstructured documents into structured, searchable data. Anticipated patterns include:
- **Table extraction** from historical documents
- **Field-level classification** for cataloguing backlogs
- **Entity resolution** across legacy databases
- **Multi-modal extraction** combining text and image analysis

### 3. Evaluation
How to measure whether AI outputs are good enough for your use case, and how to make that judgement rigorously. Emphasises:
- **No ML team required** — evaluation must be feasible for domain experts
- **Task-specific thresholds** — "good enough" depends on the consequence of error
- **Iterative improvement** — evaluation as a feedback loop, not a one-time gate
- **Community evals** over black-box leaderboards (a theme Daniel has advocated widely)

### 4. Infrastructure
Practical guidance on hardware, hosting, and cost, including:
- When to run models locally vs. using cloud APIs
- Cost-efficient OCR (Daniel demonstrated ~$0.002/page using open-source VLMs)
- Disk-free training with Hugging Face Streaming + Unsloth
- Efficient inference with vLLM + UV Scripts on HF Jobs
- Balancing latency, throughput, and budget for collection-scale workloads

## Relationship to Daniel van Strien's Work

This book draws directly on Daniel's practical experience and published tutorials:

| Theme | Related Work |
|-------|-------------|
| Cost-efficient OCR | Re-OCR Your Digitised Collections for ~$0.002/Page (Feb 2026) |
| Synthetic data for extraction | QwQ reasoning datasets for structured data extraction (Mar 2025) |
| Distillation for classification | Distilling DeepSeek reasoning to ModernBERT classifiers (Jan 2025) |
| Efficient inference | vLLM + UV Scripts on HF Jobs (Jul 2025) |
| GLAM AI strategy | Who Benefits? Rethinking Library Data in the Age of AI (Jun 2025) |

## Related Concepts

- [[entities/daniel-van-strien]] — Author, Machine Learning Librarian at Hugging Face
- [[entities/tim-sherratt]] — GLAM hacker, creator of GLAM Workbench (parallel approach to GLAM data access)
- [[concepts/agent-economics]] — Cost analysis for AI at scale (complementary: GLAM budgets are far smaller than tech enterprise)
- [[concepts/synthetic-data]] — Synthetic dataset generation techniques (core enabler for GLAM AI without labeled data)

## TODO: Research Items

- [ ] Track when new chapters are published (Discovery, Structured Extraction, Evaluation, Infrastructure)
- [ ] Enrich with specific pattern implementations as they are documented
- [ ] Compare with Tim Sherratt's GLAM Workbench approach (Jupyter-based vs pattern-language)
- [ ] Add evaluation metrics specific to GLAM use cases (precision requirements for archival work)
- [ ] Monitor Daniel van Strien's blog for related posts that feed into the book
