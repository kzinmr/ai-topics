---
title: "OpenAI o3 and o4-mini — Test-Time Compute Scaling"
author: OpenAI
source: OpenAI Blog
url: https://openai.com/index/introducing-o3-and-o4-mini/
published: 2025-04-16
updated: 2025-06-10
type: announcement
tags:
  - o3
  - o4-mini
  - test-time-compute
  - reasoning
  - rl-scaling
  - scaling-hypothesis
  - post-pretraining
---

# OpenAI o3 and o4-mini: Next-Generation Reasoning Models

## Core Thesis

o3 and o4-mini demonstrate that **test-time compute scaling** is a viable new axis for AI progress:

> "Large-scale reinforcement learning exhibits the same 'more compute = better performance' trend observed in GPT-series pretraining."

This validates the shift from pretraining scaling to inference-time/reasoning scaling.

## Key Results

- **o3**: 87.7% on GPQA Diamond (expert-level science), ARC-AGI 76% (low compute) → 88% (high compute)
- **o4-mini**: 99.5% pass@1 on AIME 2025 with Python interpreter
- o3 makes **20% fewer major errors** than o1 on difficult real-world tasks
- Performance continues to climb when allowed to "think longer"

## Agentic Capabilities

First reasoning models to integrate tools directly into Chain of Thought:
- Strategic execution: model reasons about *when* and *how* to use tools
- Multimodal: "thinks with images" — diagrams, whiteboard sketches, complex charts
- Can search web, write Python, generate images within reasoning loop

## Connection to Scaling Hypothesis

Validates Daniel Han's "Approach #1" — test-time compute scaling. o3 proves that RL scaling offers a new dimension for improvement beyond pretraining compute, confirming that the Scaling Hypothesis extends beyond the original compute×data×parameters framework.

See: [[concepts/scaling-hypothesis#Test-Time Compute Scaling: OpenAI o3/o4-mini (April 2025)]]
