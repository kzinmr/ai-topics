---
title: LightOn
created: 2026-05-28
updated: 2026-10-09
type: entity
tags:
  - company
  - open-source
  - model
  - search
  - late-interaction
  - france
sources:
  - raw/articles/2026-04-21_antoine-chaffin_denseon-lateon-open-sota-retrieval.md
  - raw/articles/2025-04-30_lighton_gte-moderncolbert-pylate.md
  - https://lighton.ai/about-us
  - https://nextomoro.com/lighton/
status: active
---

# LightOn

LightOn is a French enterprise AI company founded in 2016 by **Igor Carron** and **Laurent Daudet**, headquartered in Paris. Originally an optical-computing hardware company (Optical Processing Units), LightOn pivoted around 2022 to enterprise LLM deployment and is now a leading open-source player in information retrieval and late interaction models. It became the **first generative AI company to IPO on Euronext Growth Paris** (November 2024, ticker: ALTAI-FR).

## Company Facts

| Field | Detail |
|-------|--------|
| **Founded** | 2016 |
| **Founders** | Igor Carron (CEO), Laurent Daudet (co-CEO) |
| **HQ** | Paris, France |
| **IPO** | Euronext Growth Paris, Nov 2024 (~€11M raised, ~€60M valuation) |
| **Employees** | ~40 (10+ nationalities) |
| **Focus** | Enterprise GenAI, retrieval models, late interaction |
| **Positioning** | European data-sovereignty alternative to US API providers |

## Key Products & Models

### Retrieval Models (Open Source, Apache 2.0)

- **[[entities/denseon-lateon|LateOn]]** (Apr 2026): Multi-vector ColBERT-style retriever, BEIR 57.22 — first ColBERT to break 57
- **[[entities/denseon-lateon|DenseOn]]** (Apr 2026): Single-vector dense retriever, BEIR 56.20 — first <150M model past 56
- **ColBERT-Zero**: Unsupervised ColBERT model, prior SOTA at 55.32
- **[[concepts/gte-moderncolbert|GTE-ModernColBERT-v1]]**: First SOTA late interaction model trained on PyLate, 8K context, BEIR 54.75 (2025)

### OCR (Open Source, Apache 2.0)

- **LightOnOCR-3** (Oct 8, 2026): family of lightweight high-performance OCR models in three
  sizes (0.8B / 1B / 4B; the 1B keeps the previous architecture, 0.8B and 4B adopt the Qwen3.5
  vision-language architecture). A single model outputs page transcription *and* — via a
  `grounding` prompt mode — labeled bounding boxes (coords normalized 0–1000), image
  descriptions, and chart data extracted as HTML tables, positioning itself as a ready-to-use
  replacement for complex document-understanding pipelines. The release post details the SFT
  data mixture, an iteratively built grounding/bounding-box data pipeline, and an RL stage with
  manually verified data and checkpoint averaging.
  Sources: [HF blog](https://huggingface.co/blog/lightonai/lightonocr-3),
  [[raw/articles/huggingface.co--lightonocr-3-ocr-layout--2026-10-08.md]]

### Tools & Libraries

- **PyLate**: Flexible training and retrieval library for late interaction models (CIKM 2025). Train SOTA retrieval on MS MARCO in <2 hours with ~80 lines of code.
- **Paradigm**: Enterprise GenAI platform for deploying foundation models behind the firewall

### LLMs

- **Alfred**: Flagship commercial LLM
- 12+ LLMs developed, including open-sourced foundation models with 100B+ parameters

## Research Contributions

- Pioneer in **late interaction retrieval** — PyLate is the first peer-reviewed (CIKM 2025) library for ColBERT-style training
- **Late Interaction Workshop (LIR) @ ECIR 2026** co-organizer (via Antoine Chaffin)
- Full pipeline release philosophy: models + training data + curation + mixture recipes all open

## Relationships

- **Key researchers**: Antoine Chaffin, Benjamin Clavié (Mixedbread AI collaborator)
- **Peers**: [[entities/mistral-ai|Mistral AI]], Aleph Alpha (European data-sovereignty AI)
- **Related concepts**: [[concepts/colbert|ColBERT]], [[entities/late-interaction|Late Interaction Workshop]], [[concepts/evaluation/longembed|LongEmbed]], [[entities/embeddings|Embeddings]]
