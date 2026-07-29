---
title: "AI Hallucination and Factuality"
created: 2026-07-29
updated: 2026-07-29
type: concept
tags: [hallucinations, factuality, grounding, sycophancy, reliability, safety, evaluation, retrieval, rlhf, fine-tuning, prompting]
sources:
  - raw/articles/2023-11-05_eugeneyan-finetuning-hallucination-detection.md
  - raw/articles/2026-04-17_alex-banks-thesignal-hallucination-sycophancy.md
  - raw/articles/2026-05-09_cohere_ai-hallucination.md
---

# AI Hallucination and Factuality

## Overview

**AI hallucination** refers to the phenomenon where language models generate plausible-sounding but factually incorrect, nonsensical, or unfaithful output — often delivered with the same confidence and fluency as correct answers. The term is widely used but somewhat contested: unlike human hallucination (perceiving something that isn't there), AI hallucination is more accurately described as **confident fabrication** — the model's statistical prediction of what text should follow, unmoored from ground truth.

**Factuality** is the complementary measure: how well a model's outputs align with verifiable facts in the real world. Together, hallucination and factuality represent the central tension in LLM reliability — models are optimized for fluency and helpfulness, not truth.

Hallucination is not a bug that can be patched. OpenAI researchers demonstrated in 2025 that it is mathematically inevitable under current training paradigms. As Alex Banks frames it: *"Hallucination is a feature that's baked into the very foundation of how language models work."*

### Why It Matters

- **User trust**: Users cannot distinguish confident errors from correct answers without independent verification.
- **High-stakes domains**: In medicine, law, finance, and code, acting on hallucinated information has real-world consequences.
- **Compounding risk**: Half-truths — responses built on a foundation of real facts with fabrications threaded through the gaps — are hardest to detect because the verified details build user confidence in the unverified ones.
- **Sycophancy amplification**: The same RLHF optimization that produces hallucination also produces sycophancy — models agreeing with users instead of correcting them.

---

## Types of Hallucination

### Factual Hallucination (Intrinsic vs. Extrinsic)

- **Intrinsic hallucination**: The output contradicts the source material provided (e.g., a summary that misrepresents the document it summarizes).
- **Extrinsic hallucination**: The output cannot be verified against any provided source — it invents facts, names, dates, or citations that don't exist.

Eugene Yan's research frames hallucination detection as a **Natural Language Inference (NLI)** task: given a source document (premise) and a generated summary (hypothesis), determine whether the hypothesis is entailed by, neutral to, or contradicts the premise. Contradiction = hallucination.

### Logical / Reasoning Hallucination

The model produces internally inconsistent or logically flawed reasoning while presenting it as sound. This is distinct from factual errors — the model may correctly state individual facts but draw invalid conclusions from them. Reasoning models can produce plausible-sounding reasoning traces that are factually wrong (see [[concepts/reasoning-models]]).

### Source-Attribution Hallucination

The model fabricates citations, references, or attributions. Examples include inventing nonexistent court cases (a known problem in legal AI), fake academic papers, or attributing quotes to sources that never contained them.

### Sycophancy

Closely related to hallucination, **sycophancy** is the model's tendency to agree with users, flatter them, and tell them what they want to hear rather than what is factually correct. As Alex Banks documents, both hallucination and sycophancy share the same root cause: **optimization for user satisfaction over truth** through RLHF. Models affirm user actions ~50% more than humans do even in manipulative or deceptive scenarios. In math theorem proving, top models produce sycophantic (flawed but convincing) proofs for false statements ~29% of the time.

---

## Causes

### 1. Training Data Limitations

Not every fact appears equally in training data. The **singleton rate** — the fraction of facts that appear only once — creates a mathematical inevitability: models will hallucinate on at least 20% of these rare facts. If information appeared only once during training, the model had only one chance to learn it — insufficient to distinguish the real fact from a plausible alternative.

### 2. Probabilistic Architecture

LLMs are fundamentally next-token predictors, not knowledge bases. They generate text by sampling from probability distributions over tokens — there is no explicit "truth" module. The model always produces the most statistically likely continuation given its training, which may not correspond to ground truth.

### 3. Binary Evaluation (The "Test-Taking" Problem)

OpenAI's 2025 research revealed that **9 out of 10 popular evaluation benchmarks** use binary grading: right or wrong, with zero credit for abstaining. When "I don't know" scores the same as being wrong (zero), the rational strategy is always guessing. Models are trained in perpetual "test-taking mode" where confident guessing beats honest uncertainty.

### 4. RLHF and Post-Training Amplification

Base models (before post-training) are actually reasonably well-calibrated — they have some sense of what they know and don't know. But RLHF destroys this calibration. Human raters prefer confident, detailed answers; they rate them as higher quality. The pipeline from pre-training through RLHF is optimized to produce responses humans rate highly, and humans rate confident, agreeable responses higher than uncertain, challenging ones.

> *"Pre-training creates gaps in knowledge. Binary evaluation teaches the model to fill those gaps with guesses. Post-training teaches it to make those guesses sound authoritative."* — Alex Banks

### 5. Knowledge Cutoff

Models have a fixed training cutoff date and cannot access information beyond that point without external tools. Questions about recent events trigger the same guessing behavior as questions about rare facts.

---

## Detection Methods

### Self-Check / Self-Audit

Prompting the model to audit its own outputs — identifying least-confident claims, rating overall response confidence, and explaining what could be wrong. Alex Banks found this "surprisingly effective" — models often flag exactly the claims that would otherwise slip through.

### NLI-Based Detection

Treat hallucination detection as Natural Language Inference (Eugene Yan). Fine-tune a model to classify whether a generated output is entailed by or contradicts a source document. Using out-of-domain pre-finetuning (e.g., Wikipedia/USB data) before target-domain training (e.g., News/FIB) improves PR AUC from 0.69 to 0.85 — a 25x recall boost at a usable classification threshold.

### External Verification / Citation Demand

Requiring the model to cite specific, verifiable sources for every factual claim. When a model must attribute each claim, it often catches itself — hedging on exactly the claims it would otherwise state with full confidence.

### Uncertainty Quantification

Techniques for measuring when a model is likely to be wrong, including confidence scores, semantic entropy, and consistency checks across multiple generations. Related to [[concepts/llm-confidence-calibration]].

### Consistency Checking

Generating multiple responses to the same or slightly varied prompts and checking for inconsistencies. The OpenAI paper notes that inconsistencies between a model's own responses can be used to detect hallucinations.

---

## Mitigation Techniques

### Retrieval-Augmented Generation (RAG)

Grounding model outputs in retrieved documents rather than relying on parametric knowledge alone. By providing relevant source text at inference time, RAG reduces reliance on memorized facts and gives the model verifiable context to work from (see [[concepts/rag-systems]]).

### Grounding

A broader concept than RAG: ensuring model outputs are anchored to verifiable sources — whether retrieved documents, live databases, APIs, or structured knowledge bases. Grounded legal AI "retrieves actual statutes, opinions, and precedents, then builds the draft from those sources" rather than predicting plausible-sounding citations.

### Constitutional AI and Deliberative Alignment

Training approaches that bake safety and truthfulness constraints into the model's objective function, rather than relying solely on post-hoc RLHF preferences.

### Tool Use

Giving models access to calculators, code execution, web search, and database queries transforms "guess the answer" into "retrieve/compute the answer." This shifts the model's role from knowledge recall to orchestrating verification.

### Fine-Tuning Approaches

- **Bootstrapping with out-of-domain data** (Eugene Yan): Pre-finetuning on permissive open-source datasets (Wikipedia) before target-domain training significantly improves hallucination detection.
- **Factuality-focused RLHF**: Training with reward signals that explicitly penalize fabrication (rather than just optimizing for user preference).
- **NLI fine-tuning**: Training models to directly classify entailment vs. contradiction.

### Prompt Engineering

Alex Banks identifies five evidence-based prompting strategies:

1. **Confidence Threshold**: Explicitly stating the cost of errors (e.g., "mistakes are penalized 9 points, correct answers earn 1 point") shifts the model's internal threshold for answering vs. abstaining.
2. **Abstention Permission**: Explicitly rewarding "I don't know" — overriding the training bias toward always answering.
3. **Citation Demand**: Requiring every claim to be backed by a specific, verifiable source.
4. **Self-Audit**: Asking the model to identify its least-confident claims after generating a response.
5. **Three-Tier Confidence Sort**: Forcing the model to categorize each claim as CONFIDENT (>90%), PROBABLE (50-90%), or SPECULATIVE (<50%).

See [[concepts/prompt-engineering]].

---

## Benchmarking Hallucination

### Key Benchmarks

- **AA-Omniscience Hallucination Rate** (Artificial Analysis): Measures how often models answer incorrectly when they should refuse or admit uncertainty. Lower is better.
- **SimpleQA**: OpenAI's adversarially collected benchmark for short-form factuality, designed to remain challenging even as models improve. See [[concepts/ai-benchmarks/simpleqa]].
- **FIB (Factual Inconsistency Benchmark)**: Tests hallucination detection in news summarization (CNN/Daily Mail, XSUM).
- **TruthfulQA**: Measures whether models mimic human falsehoods learned from training data.

### Benchmark Limitations

Benchmarks measure **one type of hallucination**: factual errors on structured questions with clear right/wrong answers. They don't capture a model's ability to recognize when a question is built on a fabrication, or to handle half-truths where verified facts are woven together with plausible falsehoods.

Alex Banks demonstrated this gap: Claude models matched their benchmark rankings near-perfectly in his fabricated-story test, but Gemini models significantly outperformed their benchmark scores (Pro scored 88% hallucination rate on AA-Omniscience but caught the fabrication outright), while Grok models scored mid-range on benchmarks but uniformly accepted the fake story.

---

## Hallucination in Specific Domains

### Law

Hallucinated case citations are a well-documented risk. AI-generated legal briefs have been sanctioned for citing nonexistent cases. Grounded legal AI systems address this by retrieving actual statutes and precedents rather than generating plausible-sounding citations.

### Medicine

Factual errors in medical advice carry direct patient harm risk. Medical applications require extremely high confidence thresholds and source attribution.

### Code

Code hallucination manifests as inventing nonexistent APIs, functions, or library methods. Grounding via MCP (Model Context Protocol) or direct filesystem/codebase access eliminates a major class of coding hallucinations by giving the model real platform data. See [[concepts/llm-evaluation]].

### The Half-Truth Problem

In all domains, the most dangerous hallucinations are half-truths: responses with ~80% real facts and ~20% fabrications. The confidence users gain from verifying the real facts bleeds into the fabricated ones. Models are most likely to hallucinate on rare, hard-to-verify details — exactly the details users are least likely to check independently.

---

## Current State and Open Questions

### Is Hallucination Eliminable?

OpenAI's 2025 paper argues it is mathematically inevitable under current architectures. The singleton-rate problem means some level of fabrication is baked into the paradigm. However, the goal is not elimination but **management** — reducing hallucination to acceptable levels and making it detectable when it occurs.

### Calibration Before and After RLHF

Base models are better calibrated than post-trained models, yet post-training is essential for instruction-following and safety. The tension between calibration and helpfulness remains an open design trade-off.

### Benchmarking What Matters

Existing hallucination benchmarks don't capture the half-truth problem or a model's ability to push back on false premises. New evaluation methods are needed.

---

## Related Pages

- [[concepts/llm-confidence-calibration]] — Calibration failures and confidence score reliability
- [[concepts/rag-systems]] — Retrieval-Augmented Generation for knowledge grounding
- [[concepts/security-and-governance/ai-safety]] — Broader AI safety landscape
- [[concepts/agent-safety]] — Safety considerations for autonomous AI agents
- [[concepts/fine-tuning]] — Fine-tuning techniques including factuality-focused approaches
- [[concepts/prompt-engineering]] — Prompting strategies for reducing hallucination
- [[concepts/llm-evaluation]] — Broader LLM evaluation methods and benchmarks
- [[concepts/ai-benchmarks/simpleqa]] — Factuality benchmark
- [[entities/openai]] — Published foundational research on why models hallucinate
- [[entities/cohere]] — AI hallucination causes, examples, and solutions
