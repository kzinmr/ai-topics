---
title: "Creating, Curating, and Cleaning Data for LLMs — Conference Talk Summary"
author: Hamel Husain (host)
speaker: Daniel van Strien, David Berenstein
date: 2024-01-24
date_ingested: 2026-06-15
source: https://maven.com (Full Stack Deep Learning course)
type: article
tags:
  - synthetic-data
  - datasets
  - fine-tuning
  - training
  - data-science
---

# Creating, Curating, and Cleaning Data for LLMs

**Summary:** A conference talk from Hamel Husain's Full Stack Deep Learning course covering practical approaches to building datasets for fine-tuning large language models. Daniel van Strien (Hugging Face) covers finding and evaluating existing datasets, fine-tuning data formats (SFT, DPO, KTO, SPIN, ORPO), and building a dataset summarizer pipeline. David Berenstein (Argilla) covers synthetic data generation, the UltraFeedback case study, quality improvement techniques, and annotation tooling.

**Speakers:**
- **Daniel van Strien** (@vanstriendaniel) — Machine Learning Librarian, [[entities/daniel-van-stien|Hugging Face]]. Background in libraries; expertise in data organization and systematic structure.
- **David Berenstein** — ML & DevRel, Argilla. Background in NLP, knowledge graphs, custom domain models.
- **Hamel Husain** ([[entities/hamel-husain]]) — moderator

## Key Topics

- **Finding Existing Datasets**: Hugging Face Hub tags, full-text search, Dataset Viewer for quick vibe checks
- **Adapting Classic NLP Data**: Restructuring existing datasets for LLM fine-tuning
- **User Feedback as Training Signal**: Thumbs up/down → KTO format, implicit signals (click behavior)
- **Fine-tuning Data Formats**:
  - **SFT** (Supervised Fine-Tuning): question-answer pairs
  - **DPO** (Direct Preference Optimization): input + chosen/rejected pairs
  - **KTO** (Kahneman-Tversky Optimization): input + binary preference (simpler than DPO)
  - **SPIN**: Iterative self-play, reduces initial data requirements
  - **ORPO**: DPO format but skips SFT step, single-stage alignment
- **Synthetic Data Generation**:
  - Alpaca model: 175 seed instructions → 52K via self-instruct (text-davinci-003 + LLaMA 7B)
  - Problems: hallucinations, toxicity, stereotypes from source model bias
  - UltraFeedback: multi-model completions scored by GPT-4 on 4 criteria → found coding errors (1→10 score inversion), incomplete ratings, ties treated as preferences
  - Cleaned UltraFeedback → better Zephyr reproduction (Argilla + HF collaboration)
- **Synthetic Data Tools**:
  - **Outlines**: Structured text generation (JSON, regex, Pydantic models, function calling). Token sampling modification reduces inference time.
  - **DSPy**: Programming (not prompting) — define signatures, optimize prompts/fine-tune weights. Can be costly (hundreds of API calls for optimization).
  - **distilabel**: Synthetic data generation and AI feedback framework. DAG-based pipeline, serializable, parallelizable, includes structured generation via Outlines.
- **Data Quality Improvement**:
  - Quantity: more isn't always better. Public reproductions: SFT 10K, ORPO 7K, DPO 3K, SPIN 2K samples sufficient
  - Deduplication: topic-wise dedup, custom metadata, hashing, embedding similarity. FineWeb pipeline (HuggingFace) is a good reference.
  - Rule-based cleaning: regex for LLM artifacts ('as a large language model', 'DELF', hallucinated URLs/references)
  - Classifiers: zero-shot models, SetFit (few-shot), LLM-as-judge with rationale
  - text-descriptives: simple out-of-the-box data analysis
- **Annotation Tooling**:
  - **Argilla**: Dataset overview, semantic search, bulk annotation. Open source.
  - **Lilac**: Topic clustering, semantic search, dataset visualization. Open source.
  - **ipyannotations**: Notebook-based annotation with active learning callbacks
  - **Gradio/Streamlit/Shiny**: Custom web app annotation UIs
  - Custom tools: Kinaesthetic Warmer's Bokeh+Pandas+JS embedding explorer
- **Daniel's Dataset Summarizer Project**: Fine-tune a small LLM to generate TL;DR summaries of HuggingFace dataset cards. Pipeline: markdown processing → multi-model summarization → UltraFeedback judging (Llama 3) → preference dataset via distilabel. Key insight: validate LLM judge by measuring agreement with human ratings and look for simple heuristics (e.g., always prefer shorter → cap max tokens).
- **Annotation Ergonomics**: Task design matters — pairwise comparison vs. absolute rating affects annotation quality and experience

## Key Insights

1. DPO datasets became popular because chosen/rejected pairs can be generated creatively (human gold standard + model generation as rejected)
2. KTO is simpler than DPO — binary thumbs up/down is easier to collect from existing systems
3. ORPO enables single-stage alignment (skip SFT), reducing data duplication and training time
4. Synthetic data quality depends heavily on source model bias — always inspect generated data
5. UltraFeedback had serious bugs (score inversion, ties as preferences) — manual data inspection caught them
6. Aggressive deduplication doesn't always improve results (FineWeb lesson)
7. Simple heuristics can replace expensive LLM judges for quality filtering
8. Dataset engineering is becoming a specialized role distinct from AI engineering

## Companion Resources

- Companion transcript: [[transcripts/2024-01-24_hamel-husain_creating-curating-cleaning-data-for-llms|Full Transcript]]
- Related concept: [[concepts/dataset-engineering]]
- Related entity: [[entities/daniel-van-strien]]
- Related entity: [[entities/hamel-husain]]
- Tools mentioned: [Argilla](https://argilla.io/), [Lilac](https://lilacml.com/), [distilabel](https://distilabel.argilla.io/), [Outlines](https://github.com/outlines-dev/outlines), [DSPy](https://github.com/stanfordnlp/dspy)
