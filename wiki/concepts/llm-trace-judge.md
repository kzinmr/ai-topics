---
title: "LLM Trace Judge"
created: 2026-06-16
updated: 2026-06-16
type: concept
tags:
  - evaluation
  - fine-tuning
  - observability
  - open-source
aliases:
  - perceived error detection
  - trace evaluation
  - llm-as-judge-traces
related:
  - [[concepts/evaluation/ai-evaluation]]
  - [[concepts/evaluation/llm-as-judge]]
  - [[entities/langsmith]]
  - [[entities/fireworks-ai]]
sources:
  - raw/articles/2026-06-15_langchain_building-100x-cheaper-trace-judge-fireworks.md
---

# LLM Trace Judge

**LLM Trace Judge** refers to the practice of using language models to automatically evaluate production traces from AI agent interactions, extracting structured quality signals at scale. A landmark June 2026 study by LangChain and Fireworks AI demonstrated that fine-tuning open models on trace data can match or exceed frontier model performance at 10-100x lower cost.

## Background

As AI agents move into production, they generate billions of tokens daily across traces that record every interaction, tool call, and model response. Manually reviewing these traces is infeasible, but automated evaluation is critical for understanding agent behavior, detecting failure modes, and guiding improvement.

The **Trace Judge** paradigm addresses this by training specialized models to classify traces along meaningful quality dimensions — without requiring ground-truth labels or expensive human annotation.

## Perceived Error Detection

The LangChain x Fireworks study introduced **"Perceived Error"** as a general-purpose trace evaluation metric:

> Perceived error is when the user thinks the assistant made a mistake or produced something that needed correction. It is not about objective correctness or user happiness — an agent could give a correct answer but the user is frustrated by the information (not the agent).

### Signals Used for Detection

Perceived error is inferred from trace signals including:
- **User corrections**: The user restates or fixes the assistant's output
- **Action rejection**: The user rejects an agent's tool invocation or plan
- **Repeated requests**: The user asks the same question again, indicating dissatisfaction
- **Assistant acknowledgments**: The assistant admits an error or apologizes

### Why Perceived Error is General-Purpose

Unlike application-specific evaluators (which require custom logic per use case), perceived error relies on **universal interaction patterns** that appear across any conversational agent. This makes it a strong candidate for a reusable, off-the-shelf judge model.

## Training Methodology

### Dataset Construction

The study used two internal LangChain production tracing datasets:

| Dataset | Description | Total Traces | Train | Holdout |
|---------|-------------|-------------|-------|---------|
| **chat-langchain** | Docs Q&A agent for LangChain libraries | 885 | 707 | 178 |
| **Fleet** | No-code agent creation tool for real work | 911 | 727 | 184 |

Only **multi-turn traces** were selected, because perceived error requires observing a human response to AI output (corrections, rejections, repetitions).

### Label Generation

A two-stage model-assisted labeling pipeline was used:
1. **Panel consensus**: Multiple models independently judge each trace. Agreement = ground truth.
2. **Escalation**: If models disagree, their labels + rationales are passed to a second panel. If still unresolved, human annotation is used.

Error rates: chat-langchain had 24% perceived error traces; Fleet had 18%.

### Input Design

Key design choices for training data preparation:
- **Human + AI messages only**: Tool calls were excluded from the input. The hypothesis was that conversational signals carry most of the perceived-error information.
- **No content trimming**: Full message content was used without length limits.
- Both are active levers for future experimentation.

### Model and Training

- **Base model**: Qwen-3.5-35B (selected for strength + cost balance)
- **Training method**: LoRA SFT via Fireworks managed training
- **Training data**: Only chat-langchain dataset (to test cross-domain transfer)

## Results

### Fine-Tuning Matches Frontier Models

| Model | chat-langchain accuracy | Fleet accuracy |
|-------|------------------------|----------------|
| Base Qwen-3.5-35B | 90.5% | 83.2% |
| **Chat-langchain SFT** | **96.1%** | **90.8%** |
| Fleet SFT | 92.7% | 91.3% |
| Claude Opus | 91.6% | 90.2% |
| GPT-5.5 | 98.9% | 89.1% |

### Cross-Domain Transfer

The model trained **only on chat-langchain** data was tested on the completely unseen Fleet dataset:
- It **outperformed all frontier models** (Opus, GPT-5.5) on Fleet data
- This validates the **generality** of the perceived-error metric across domains

### Cost Efficiency

Fine-tuned open models deliver 10-100x cost savings compared to frontier model alternatives at production trace volumes. The savings scale linearly with trace volume.

## Significance

### For the Eval-as-a-Service Market

This study demonstrates that **open models + fine-tuning infrastructure** can replace expensive frontier models for high-volume evaluation workloads. Key implications:

1. **Specialization beats generalization**: A 35B model fine-tuned on domain-specific traces outperforms a 175B+ frontier model on the same task
2. **Evaluation metrics can be portable**: Perceived error transfers across datasets without retraining
3. **Cost scales favorably**: The fine-tuned model is cheaper to serve and more accurate than smaller frontier alternatives (e.g., Haiku)

### For Production Agent Development

- Trace-level evaluation enables **continuous improvement loops**: detect failures → analyze traces → improve agents → redeploy
- Cost-effective evaluation makes it feasible to judge **every single trace**, not just sampled subsets
- The perceived-error signal connects user-facing quality (not just benchmark accuracy) to agent behavior analysis

### Relationship to LLM-as-Judge

The Trace Judge extends the [[concepts/evaluation/llm-as-judge]] paradigm from single-turn output evaluation to **multi-turn production trace analysis**. Unlike traditional LLM-as-judge (which evaluates generated text against rubrics), trace judges analyze interaction patterns (corrections, rejections, repetitions) to infer quality signals that no rubric can easily capture.

## Related Concepts
- [[concepts/evaluation/ai-evaluation]] — Broader evaluation methodology
- [[concepts/evaluation/llm-as-judge]] — Single-turn judge models
- [[concepts/evaluation/evaluation-flywheel]] — Continuous evaluation improvement
- [[entities/langsmith]] — Platform hosting the trace infrastructure
- [[entities/fireworks-ai]] — Fine-tuning infrastructure partner

## Sources
- [Building a 100x Cheaper Trace Judge with Fireworks](https://www.langchain.com/blog/building-a-100x-cheaper-trace-judge-with-fireworks) — LangChain blog, June 2026
- [[raw/articles/2026-06-15_langchain_building-100x-cheaper-trace-judge-fireworks]] — Raw article (X Article plain_text extraction)
