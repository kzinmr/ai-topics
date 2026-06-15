---
title: "Creating, Curating, and Cleaning Data for LLMs — Conference Talk Transcript"
author: Daniel van Strien, David Berenstein
moderator: Hamel Husain
date: 2024-01-24
date_ingested: 2026-06-15
source: https://maven.com (Full Stack Deep Learning / Hamel Husain course)
type: transcript
tags:
  - synthetic-data
  - datasets
  - fine-tuning
  - reinforcement-learning
  - data-science
  - training
  - transcript
related_article: articles/2024-01-24_hamel-husain_creating-curating-cleaning-data-for-llms
participants:
  - Daniel van Strien (Machine Learning Librarian, Hugging Face)
  - David Berenstein (ML & DevRel, Argilla)
  - Hamel Husain (moderator, Full Stack Deep Learning)
---

# Creating, Curating, and Cleaning Data for LLMs

**Speakers:** Daniel van Strien (Hugging Face), David Berenstein (Argilla)  
**Moderator:** Hamel Husain (Full Stack Deep Learning)  
**Date:** January 24, 2024  
**Context:** Full Stack Deep Learning course session

---

**Key Topics:** **Hugging Face Hub** · **DPO / KTO / ORPO / SPIN** · **synthetic data** · **Alpaca** · **UltraFeedback** · **distilabel** · **Outlines** · **DSPy** · **deduplication** · **rule-based cleaning** · **LLM judges** · **Argilla** · **Lilac** · **ipyannotations** · **Gradio** · **preference data** · **data quality** · **dataset engineer**

---

## Introduction

> "Focusing on this topic of creating, curating, and cleaning data. This has already been discussed quite a lot in the course, but hopefully give you some ideas for how to approach building datasets for fine-tuning large language models." — Daniel van Strien

### Daniel van Strien (Hugging Face)

Daniel works as a machine learning librarian at Hugging Face. His background is in libraries and information science — a discipline centered on organizing, structuring, and curating large volumes of data. He came to machine learning via the fast.ai course roughly a decade ago. He emphasizes that library skills — systematic organization, metadata, taxonomy — translate directly to building high-quality training datasets.

### David Berenstein (Argilla)

David does ML and DevRel at Argilla, a data collaboration platform for engineers and domain experts. His background includes NLP, knowledge graphs, and custom domain models from his master's work. He stresses that data quality and model quality are deeply intertwined, and he covers the synthetic data portion of the talk.

---

## Finding Existing Datasets

Daniel starts from the "ideal case" — finding data that already exists and can be used or adapted for fine-tuning.

### Hugging Face Hub

The Hub hosts a huge diversity of datasets, but the most visible trending ones tend to focus on pre-training (e.g., **FineWeb**). These pre-training-scale corpora are generally not useful for fine-tuning.

However, there is a growing number of community-contributed datasets — "slightly more bespoke and sometimes weird stuff" — that are valuable both for direct use and for understanding how others approach dataset construction.

### Tags and Search

- **Tags feature** — Underused but powerful for filtering by format (e.g., finding all DPO-format datasets).
- **Full-text search** — Useful when datasets are poorly named; searches inside the actual data content.

### Dataset Viewer

> "Once you've found the data, ideally someone would have documented it really well and explained exactly what it's for and what the limitations are and how it was made — but that often doesn't happen." — Daniel van Strien

The Hub's **Dataset Viewer** provides:
- **Metadata previews** — distributions of conversation lengths, field types, etc.
- **Row-level browsing** — lets you do a "vibe check" on whether a dataset fits your use case.

Daniel showed a function-calling dataset example: badly documented, but the viewer revealed that many long "conversations" ended with trivial pleasantries ("oh, thank you" / "oh, you're very welcome"), making those long turns actually uninformative for fine-tuning.

---

## Creating Your Own Data

In practice, you usually need to build your own dataset. Three main approaches:

### Adapting Existing NLP Datasets

Classic NLP datasets can be restructured or reformatted for LLM fine-tuning. Organizations that have been doing NLP for years likely already have data that can be adapted.

### Leveraging User Feedback

> "You can set about creating preference data very deliberately using human annotations or LLM judges, but quite often you will already have some indications — either very direct like thumbs up/thumbs down, or other ways you can intuit whether a user was satisfied." — Daniel van Strien

Existing thumbs-up/down signals, click-through behavior, or other implicit feedback can serve as preference data without needing to re-gather it.

### Synthetic Data

Synthetic data can jumpstart the dataset-building process and goes hand-in-hand with the other approaches. (Covered in depth below.)

### Format Awareness

There is significant work required to get data into the format needed for LLM training. Importantly, this pre-processing code often overlaps heavily with deployment-time code — so the format you gather data in should be close to how you'll actually use the model in production.

---

## Fine-tuning Data Formats

### Supervised Fine-Tuning (SFT)

The classic format: question-answer or instruction-response pairs.

### Direct Preference Optimization (DPO)

DPO takes an **input**, a **chosen** response, and a **rejected** response. The model is nudged toward the chosen and away from the rejected.

Creative approaches to generating chosen/rejected pairs:
- Use human-written "gold standard" data as chosen; generate a mediocre model response as rejected.
- Use any existing ground-truth as chosen; synthetically generate the rejected alternative.

> "One of the nice things I've seen in the past year is really interesting and creative ways for people to come up with where these chosen and rejected pairs come from." — Daniel van Strien

### KTO (Kahneman-Tversky Optimization)

Unlike DPO (which needs paired chosen/rejected), KTO needs only a **single response** plus a **binary preference** (thumbs up or thumbs down). This is much easier to collect from existing systems.

Creative signal sources: if a user clicked a link, that implies preference; if they didn't, that may imply rejection.

### SPIN (Self-Play Fine-Tuning)

An iterative approach that reduces data requirements. You start with some initial data, synthetically generate new responses, and build the dataset on top of that — without needing a large initial dataset.

### ORPO (Odds Ratio Preference Optimization)

Uses the same data format as DPO (input, chosen, rejected) but **does not require a prior SFT step**. This means:
- No need to duplicate data for both SFT and preference stages.
- Model training is more lightweight (single stage instead of two).

> "You can more quickly go directly from a base model to doing alignment without having to train in two steps, which is often what you have to do with these other approaches." — Daniel van Strien

---

## Synthetic Data Generation

David takes over to cover synthetic data — data generated by LLMs, commonly used for fine-tuning.

### General Approach

Synthetic data involves prompting an LLM with initial context to:
- Generate prompts from scratch
- Generate completions based on prompts
- Rephrase or augment existing data
- Judge/score completions (assign scores with rationales)

A typical prompt template: "Please provide a score for this prompt and its associated response, and also provide a rationale explaining why you gave this score."

### The Alpaca Example

One of the earliest models trained on synthetic data. The **self-instruct** approach:
1. Start with 175 seed instructions.
2. Prompt **text-davinci-003** (OpenAI) to rewrite those into more diverse instructions.
3. End up with 52,000 instructions.
4. Fine-tune **LLaMA 7B** on this data.

> "You might think: amazing, you can use LLM data to train LLMs and everything is solved. But as you might expect, it's not really the case." — David Berenstein

**Problems found:** The resulting model exhibited hallucinations, toxicity, and stereotypes. Example: when asked "Why is 42 the optimal seed?", the model hallucinated that 42 can be used for any neural network training. The issues likely stemmed from biases in both the Meta base model and the OpenAI generation model.

### UltraFeedback

A more sophisticated approach:
1. Source instructions from a pool (both synthetic and human-generated).
2. Prompt **multiple different models** to provide completions for each instruction.
3. Judge each completion with **GPT-4** on 4 criteria: instruction following, honesty, helpfulness, and an overall rating.

**Key finding:** Individual criteria scores highly correlate with the overall rating on average. So if you want to save cost/compute, you can use just the overall rating.

**Data quality issues discovered:** When Argilla's team inspected UltraFeedback data in their UI, they found:
- Responses from benchmark sources that made no sense but received high scores — caused by score scaling bugs (scores meant to be 1–10 were converted incorrectly, so a "10" might have originally been a "1").
- Incomplete ratings due to failed OpenAI API calls.
- Ties (same response, same rating) still being processed as chosen/rejected pairs.

### From Dirty to Clean Data

After cleaning UltraFeedback → **Clean UltraFeedback**, the Hugging Face team (via the **Alignment Handbook** and the **Zephyr** model) showed that cleaner data produced a model that performed better on benchmarks and better at predicting human judgment.

---

## Tools for Synthetic Data

### Outlines (Structured Text Generation)

- Produces structured text generation constrained by JSON schema, regex, or Pydantic models.
- Works by modifying token sampling — limits which tokens can be generated.
- Reduces inference time (limited token set) and guarantees valid output.
- Supports function calling.

### DSPy

- "Programming, not prompting" — define a **DSPy signature** specifying expectations for model outputs.
- The optimizer tries to improve prompts and slightly fine-tune model weights for better accuracy.
- **Cost caveat:** Under the hood, DSPy makes hundreds of API calls to OpenAI when optimizing prompts (gathering good few-shot examples), which can be quite expensive.

### distilabel

- A synthetic data generation and AI feedback framework by Argilla.
- Uses a **directed acyclic graph (DAG)** structure for serializable pipelines.
- Features: cache intermediate results, structured generation (via Outlines), parallel execution.
- Positioned as a "dataset engineering" tool — focused on the data pipeline rather than application development.

> "There's an interesting blog post about 'the rise of the dataset engineer' — not really having AI engineers anymore, but people that focus on data and data quality." — David Berenstein

---

## Improving Data Quality

Data improvement is an **iterative process**: original dataset → assess diversity → check quantity/quality → deduplication filtering → human + AI feedback loop.

### Quantity vs. Quality

More isn't always better. It's fine to throw away over-represented data or lower-quality examples.

**Reference points from public reproductions:**
- SFT: great benchmark results with as few as **10K** input samples.
- ORPO/SPIN: as low as **2K** data examples can produce strong results.

### Deduplication

Deduplication pipelines are often poorly documented and hard to reproduce. Hugging Face published their entire FineWeb deduplication pipeline publicly (via the **datatrove** library).

Approaches:
- Use **existing metadata** for filtering (topic, source, relevance).
- Create **custom features** (hashing strings, embedding similarity).
- Topic-wise deduplication: keep the most representative examples per topic.
- **Caution:** Aggressive deduplication doesn't always help — the FineWeb blog post shows subtle heuristics matter.

### Rule-Based Cleaning

Simple, human-readable rules that are highly effective:
- Filter out queries containing "As a large language model..." (LLM self-references).
- Remove responses using the word "DELF" or containing hallucinated URLs/references.
- Detect quotation-mark patterns that indicate the model is fabricating references.
- Flag responses that look like the model hallucinated content.

### Classifiers and Embeddings

- **Zero-shot classifiers** from Hugging Face can predict topics for initial filtering.
- **SetFit models** — train with only a handful of annotated examples.
- Very cheap to run and effective for data triage.

### LLM Judges

For more expensive but powerful assessment:
- LLM-as-judge with scores and rationales.
- **textdescriptives** package — provides out-of-the-box text analysis metrics (readability, complexity, etc.).

---

## Human Annotation Tools

> "All of these methods are intended to be used along with human annotation. This really helps to make human annotation more fun, more engaging, and also more effective." — David Berenstein

The spectrum ranges from simple (Google Sheets) to fully customized tools. For most people, something in between works best.

### Argilla

- Data collaboration platform with dataset overview, semantic search, built-in annotation.
- Open source. Can attach vectors/factors to records.
- Opinionated features — many people can use the out-of-the-box toolkit.
- Better suited for SDK/API-driven workflows (AI engineers).

### Lilac

- Dataset overview with topic clustering visualization.
- Semantic search feature.
- Open source.
- May feel more intuitive for domain experts and labelers (UI/UX).

**Daniel's recommendation:** Use both for different purposes:
- **Lilac** for the initial "vibe check" — quick visualization of data distributions.
- **Argilla** for detailed annotation and iteration.

For even cruder quick analysis: get data into a DataFrame (even in Google Colab), compute basic features (string length, token counts), and use built-in plot suggestions to spot outliers.

### ipyannotations

- Notebook-based annotation tool.
- Fully customizable with callbacks for post-processing.
- Supports active learning — train a classifier on the fly and use it for inference within the same notebook.

### Gradio / Streamlit / Shiny

- Build custom annotation web apps quickly using their components.
- Example: a hackathon submission where annotators could mark translations as correct/incorrect, or do KTO-style thumbs-up/thumbs-down per record.
- Fully customizable.

---

## Example Datasets

### Writing Improvement (DPO)

A creative approach to building preference data for writing quality:
1. Take existing books written by humans.
2. Prompt an LLM to **summarize** chapters.
3. Prompt another model to **rewrite** based on that summary.
4. Set the **original human text** as chosen; the **model-generated rewrite** as rejected.

> "This might not apply to your use case, but it's an example of how you can get at these things without having to rely on either human data or purely model data." — Daniel van Strien

### Preference Flywheel (Vision Model)

A vision model example focused on collecting thumbs-up/thumbs-down ratings in a continuous feedback loop — generating data as users interact with the system.

### Annotation Ergonomics

> "It's worth thinking about not just the tool, but also what the task is that you're actually doing when you're annotating, and how does that work better." — Daniel van Strien

For preference data:
- Sometimes it's easy to say "that's good" or "that's bad" for a single response.
- Other times, placing **two generations side-by-side** and asking "which is better?" produces more reliable judgments.
- Task design likely influences annotation quality significantly.

### Daniel's Summarization Project

Building a small LLM summarizer (for the course) that takes a Hugging Face dataset card (long markdown) and produces a TL;DR summary.

Pipeline:
1. Load dataset cards from the Hub.
2. Filter and format the markdown (remove formatting noise).
3. Generate summaries with multiple open models.
4. Compare summaries using **UltraFeedback** (LLM-as-judge, using LLaMA 3).
5. Send results to **Argilla** for human review.

Key insights:
- Start small (100 samples), inspect results, iterate on prompts.
- Look for **simple heuristics** that correlate with your preferences (e.g., "I always prefer shorter summaries" → just cap tokens and skip the LLM judge).
- Use heuristics as a check on the LLM judge's continued reliability.

---

## Q&A and Closing

**Q: How would you recommend generating synthetic data when fine-tuning on proprietary datasets and human annotation is expensive?**

> "It's about data ownership — if you value privacy, if you need these things in your company, and if you really want to be the owner of your data and your model. Those are the main takeaways for this trade-off." — David Berenstein

The considerations are the same as choosing between proprietary and open models: data ownership, privacy requirements, licensing, and whether you need full control.

**Hugging Face course credits** can be used for Spaces *and* inference endpoints — enough to generate quite a lot of synthetic data.

Daniel and David both offered to continue the conversation in the course Discord, with Daniel noting:

> "I'm overly excited about people building datasets. I'm happy to try and help out — I might not have the answer but I'm up to brainstorm with people if they're interested." — Daniel van Strien

---

## Companion Resources

- [Hugging Face Hub Datasets](https://huggingface.co/datasets) — Browse and search datasets
- [Argilla](https://github.com/argilla-io/argilla) — Open-source data collaboration platform
- [Lilac](https://github.com/lilacai/lilac) — Dataset exploration and annotation tool
- [distilabel](https://github.com/argilla-io/distilabel) — Synthetic data generation framework
- [Outlines](https://github.com/outlines-dev/outlines) — Structured text generation
- [DSPy](https://github.com/stanfordnlp/dspy) — Programming (not prompting) framework
- [Alignment Handbook](https://github.com/huggingface/alignment-handbook) — Hugging Face's reproducible alignment recipes
- [FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb) — Pre-training dataset with documented deduplication pipeline
- [datatrove](https://github.com/huggingface/datatrove) — Hugging Face's data processing library
- [textdescriptives](https://github.com/HLasse/TextDescriptives) — Text analysis metrics
- [ipyannotations](https://github.com/janfreyberg/ipyannotations) — Notebook-based annotation
