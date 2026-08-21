---
title: "DeepSeek Vision — Multimodal Capabilities"
created: 2026-06-19
updated: 2026-08-21
type: concept
tags:
  - deepseek
  - multimodal
  - vlm
  - model
  - product
  - announcement
sources:
  - raw/articles/2026-06-18_deepseek_vision-launch.md
  - raw/articles/2026-08-21_deepseek-v4-flash-vision-exp-api.md
  - https://chat.deepseek.com/
  - https://news.ycombinator.com/item?id=48588409
---

# DeepSeek Vision

DeepSeek Vision is the multimodal capability launched by DeepSeek in June 2026, adding image understanding to the chat.deepseek.com interface. This marks DeepSeek's expansion from text-only models into vision-language model (VLM) territory, positioning it alongside GPT-4V, Claude Vision, and Google Gemini in the multimodal frontier.

## Overview

On June 18, 2026, DeepSeek introduced Vision on their chat platform. Users can now upload images and have the model analyze, describe, and reason about visual content alongside text conversations. The launch was received with high engagement on Hacker News (473 points, 194 comments), reflecting strong community interest in open-weight model capabilities catching up to closed-source multimodal offerings.

## Key Details

- **Launch date**: June 18, 2026
- **Platform**: chat.deepseek.com
- **Capability**: Image input + text output (vision-language)
- **Model**: Integrated with DeepSeek's existing chat models
- **Positioning**: Open-weight alternative to GPT-4V, Claude Vision, Gemini

## Significance

- **Open-source multimodal milestone**: DeepSeek is one of the few labs offering vision capabilities with open-weight models
- **Competitive pressure**: Puts pressure on other open-source labs (Meta LLaMA, Mistral) to ship multimodal
- **Ecosystem impact**: Enables open-source vision applications (image analysis, visual QA, document understanding) without API dependency
- **Catch-up narrative**: Demonstrates that open-weight models are rapidly closing the gap with proprietary multimodal systems

## Community Reception

The HN discussion highlighted several themes:
- Excitement about open-weight multimodal capabilities
- Comparisons to closed-source vision models
- Interest in API availability and self-hosting options
- Questions about the underlying model architecture
- Practical applications for document analysis and visual understanding

## V4-Flash Vision Experimental API (August 2026)

On August 21, 2026, DeepSeek published an API docs guide for **`deepseek-v4-flash-vision-exp`** — an **experimental** vision model in the DeepSeek V4-Flash line (the 284B-total / 13B-active MoE; see [[concepts/deepseek-v4]]). This moves DeepSeek vision from the chat.deepseek.com consumer surface into the paid API, with these characteristics:

- **Model**: `deepseek-v4-flash-vision-exp` (the `-exp` suffix marks it experimental; images in system/assistant messages return 400).
- **Formats**: JPEG, PNG, GIF, WebP — detected from file content, not MIME type.
- **Three input paths**: base64 data URL (48 MiB request body limit), external http(s) URL (8192-char URLs, 32 MiB images, 60s download budget), or **Files API file_id** (64 MiB per image, reusable across requests).
- **Token billing**: images are auto-resized to ~800×800-equivalent pixel counts (small images scaled up from ~384×384), capping usage at **384 tokens per image**.
- **Limits**: up to 600 images per request; 8192 px max dimension (4096 px when 15+ images in a request).
- **Triple API compatibility**: the same model is served via the OpenAI-compatible Chat Completions endpoint, the **Anthropic-compatible `/messages` endpoint** (`https://api.deepseek.com/anthropic`), and the OpenAI **Responses API** — a notable multi-vendor compatibility move that lets existing OpenAI- or Anthropic-shaped client code call DeepSeek vision unchanged.
- **Detail levels**: `low` (downscale to 512×512) vs `original`/`high`/`auto` (keep original resolution).

No per-token vision pricing was listed on the guide as of retrieval; image tokens bill alongside V4-Flash text tokens.

Source: [[raw/articles/2026-08-21_deepseek-v4-flash-vision-exp-api]] — [DeepSeek API docs, Vision guide](https://api-docs.deepseek.com/guides/vision/) (discovered via HN, 61 pts, Aug 21 2026).

## See Also

- [[entities/deepseek]] — DeepSeek entity page
- [[concepts/multimodal]] — multimodal AI capabilities
- [[concepts/multimodal-vision-audio-cross-modal]] — cross-modal AI
- [[concepts/open-source-ai]] — open-source AI ecosystem
- [[concepts/frontier-models-comparison-april-2026]] — frontier model competitive landscape
- [[concepts/deepseek-v4]] — DeepSeek V4 model

## Sources

- [DeepSeek Vision Launch Announcement](https://chat.deepseek.com/) — June 18, 2026
- [HN Discussion (473 pts, 194 comments)](https://news.ycombinator.com/item?id=48588409)
- [Raw research note](raw/articles/2026-06-18_deepseek_vision-launch.md)
