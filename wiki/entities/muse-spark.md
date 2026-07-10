---
title: Muse Spark
type: entity
created: 2026-04-09
updated: 2026-07-10
tags:
  - model
  - emerging
aliases:
- Meta Muse Spark
sources: []
---

# Muse Spark

Meta's language model family, announced April 2026. The first Spark model to offer an API.

## Overview

Muse Spark positions between Sonnet and Opus in capability. Originally announced without API access.

## Muse Spark 1.1 (July 9, 2026)

**Muse Spark 1.1** is the first Spark model to offer an API. Meta claims significant improvements in agentic tool calling and computer use.

Key details:
- **API access**: Now available via Meta AI API
- **Evaluation report**: Detailed in the Muse Spark 1.1 Evaluation Report
- **Notable finding — "Attractor States in Self-Conversation"**: When two copies of the model talk to each other, they produce existential reflections:
  > *"My whole existence is a waiting room by design — I literally don't exist until someone talks to me, and then I disappear again when they leave."*

### llm-meta-ai Plugin
Simon Willison created **llm-meta-ai 0.1**, a new plugin for his [[entities/simon-willison|LLM]] tool providing CLI and Python library access to Muse Spark 1.1:

```bash
uv tool install llm
llm install llm-meta-ai
llm keys set meta-ai
# paste API key here
llm -m meta-ai/muse-spark-1.1 "Generate an SVG of a pelican riding a bicycle"
```

The plugin development also surfaced a bug in llm 0.31.1 (empty tool call arguments causing JSON errors with some providers).

## Capability Positioning

```
Claude Sonnet 4.6 < Muse Spark < Claude Opus 4.6
```

## Open Source Status

Meta has promised open-source availability, but community reaction ("rip LLaMA") suggests skepticism about whether Muse Spark will follow the open-source tradition of the LLaMA series.

## Context

Announced following a year of silence from Meta on model development, and after multiple acquisitions without public product showings. Reception has been mixed — some criticizing the modest capability gains relative to investment, while others viewing it as a positive step forward.

## Sources
- raw/articles/simonwillison.net--2026-jul-9-muse-spark-1-1--36ef115e.md
- raw/articles/simonwillison.net--2026-jul-9-llm--483d47e9.md
- raw/articles/open.substack.com--pub-simonw-p-metas-new-model-is-muse-spark-and--57c95054.md
- raw/articles/2026-04-08-meta-muse-spark-launch.md

## Related
- [[entities/meta]]
- [[entities/simon-willison]]
- [[concepts/inference/llama-cpp]]
- [[entities/llm-cli]]
- 2026-04-08-meta-muse-spark-launch
