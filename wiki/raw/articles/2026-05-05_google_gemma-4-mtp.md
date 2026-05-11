---
title: "Accelerating Gemma 4: faster inference with multi-token prediction drafters"
source: "https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/"
date: 2026-05-05
author: "Google"
tags: [google, model, open-source, optimization, inference]
---

# Gemma 4 Multi-Token Prediction (MTP)

Google released Multi-Token Prediction (MTP) drafters for the Gemma 4 family of open models (May 5, 2026):

- **3x inference speedup** without any degradation in output quality or reasoning logic
- Gemma 4 family downloaded **over 60 million times** since launch (previous month)
- MTP drafters predict multiple tokens at once, reducing the number of inference steps needed
- Efficiency gains benefit both cloud and local deployment

The MTP approach uses a lightweight "drafter" model that proposes multiple tokens, with the main model verifying them — a form of speculative decoding specialized for Gemma 4.
