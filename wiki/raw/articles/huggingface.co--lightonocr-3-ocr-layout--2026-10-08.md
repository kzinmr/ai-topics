---
title: "LightOnOCR-3: High-Performance OCR and Layout Extraction in One Model"
author: LightOn AI (Said Taghadouini, Adrien Cavaillès, Baptiste Aubertin)
url: https://huggingface.co/blog/lightonai/lightonocr-3
source: huggingface.co/blog
captured: 2026-10-09
date: 2026-10-08
type: raw-article
tags: [ocr, model-releases, open-source]
sources:
  - https://huggingface.co/blog/lightonai/lightonocr-3
  - https://x.com/tomaarsen/status/2108277298743173616
---

# LightOnOCR-3: High-Performance OCR and Layout Extraction in One Model

LightOn released **LightOnOCR-3**, a family of lightweight high-performance OCR models, on
2026-10-08 under Apache 2.0 (research + commercial use OK).

## Key points

- **Three sizes**: LightOnOCR-3-0.8B, -1B, -4B. The 1B model retains the previous generation's
  architecture; 0.8B and 4B adopt the Qwen3.5 vision-language architecture, trading accuracy,
  speed, and compute differently.
- **Unified transcription + layout**: significant speed and transcription-quality improvements
  over the previous generation, plus new visual-understanding capabilities — a single model
  replaces complex document-understanding pipelines (transcription + layout + grounding + chart
  extraction + image description).
- **Two modes**: empty text prompt = plain page transcription (backwards-compatible prompting
  interface); prompt `grounding` = adds labeled bounding boxes (coordinates normalized to 0–1000),
  image descriptions, and chart data extracted as HTML tables.
  - Textual content blocks: transcribed paragraphs/titles
  - Image blocks: bounding box + short description
  - Chart blocks: HTML table of data points extracted from the figure
- **Formatting efficiency**: layout info adds tokens per block; the post addresses token overhead
  design tradeoffs.
- **Training details** described in the post: SFT data mixture; a grounding data pipeline
  (iteratively built bounding-box data, chart data + image description added, document content
  used to guide block segmentation); RL stage with manually verified training data, reward
  shaping, and checkpoint averaging.
- Links: models on HF hub (0.8B/1B/4B), GitHub repo, HF demo space, LightOn website page.

## Context

Tom Aarsen (@tomaarsen, Hugging Face) spotted a small bug in the post's benchmark figure —
LightOnOCR-2 appeared in the legend but not the plotted bars — confirmed with the authors as a
minor plotting bug, not a results issue.

Full text: /tmp archived; see original URL for detailed benchmark tables (OLRB, and the post's
own eval suite), speed numbers, and the grounding/RL pipeline walkthrough.
