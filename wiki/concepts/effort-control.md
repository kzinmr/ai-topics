---
title: "Effort Control"
type: concept
created: 2026-05-30
updated: 2026-05-30
tags:
  - concept
  - reasoning
  - optimization
  - claude-code
  - test-time-scaling
sources:
  - https://www.anthropic.com/news/claude-opus-4-8
---

# Effort Control

**Effort Control** is a feature introduced with [[concepts/claude-opus-4-8|Claude Opus 4.8]] (May 28, 2026) in claude.ai and Cowork. It provides users with a UI control to dial the amount of computational effort Claude expends on a task.

## How It Works

A slider or selector alongside the model picker lets users choose:

- **Higher effort settings**: Claude "thinks more frequently and more deeply" — produces better responses but consumes more tokens and takes longer
- **Lower effort settings**: Claude responds faster and uses rate limits more slowly — trades depth for speed and cost efficiency

This gives users **explicit control over the compute-vs-quality tradeoff**, a capability that was previously fixed per model.

## Connection to Test-Time Scaling

Effort Control operationalizes the concept of **test-time compute scaling** — the idea that models can produce better outputs by spending more computation during inference (thinking longer, generating more intermediate reasoning steps). This is related to:

- [[concepts/reasoning|Reasoning models]] (o1, o3, etc.) which use extended chain-of-thought
- **Test-time scaling** research showing that more inference compute improves performance on hard tasks

Unlike reasoning models where the amount of "thinking" is fixed by the model architecture, Effort Control lets the **user decide** how much compute to spend per request.

## Availability

- All Claude plans (free and paid)
- claude.ai web interface and Cowork
- Requires Opus 4.8 or later models

## Related

- [[concepts/claude-opus-4-8]] — model that introduced this feature
- [[concepts/reasoning]] — reasoning models with fixed test-time scaling
- [[concepts/test-time-scaling]] — broader research area
- [[concepts/token-economics]] — cost implications of effort scaling
