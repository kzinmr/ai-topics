# Recursive Language Models (RLM)

**Source:** arXiv:2512.24601
**Authors:** Alex L. Zhang, Tim Kraska, Omar Khattab (MIT, Stanford)
**URL:** https://arxiv.org/abs/2512.24601
**Date:** Dec 31, 2025 (v1) → Jan 28, 2026 (v2)

## Abstract

We study allowing large language models (LLMs) to process arbitrarily long prompts through the lens of inference-time scaling. We propose Recursive Language Models (RLMs), a general inference paradigm that treats long prompts as part of an external environment and allows the LLM to programmatically examine, decompose, and recursively call itself over snippets of the prompt.

## Key Findings

- RLMs can successfully process inputs up to **two orders of magnitude beyond model context windows**
- Dramatically outperform vanilla frontier LLMs and common long-context scaffolds across 4 diverse long-context tasks
- Comparable cost to vanilla inference
- Post-trained model RLM-Qwen3-8B outperforms underlying Qwen3-8B by 28.3% on average
- Approaches the quality of vanilla GPT-5 on 3 long-context tasks
- Does not degrade in performance even with 10M+ tokens at inference time

## Core Mechanism

A recursive language model is a thin wrapper around a LM that can spawn recursive LM calls for intermediate computation. The key insight: instead of feeding the entire prompt at once, the LLM recursively decomposes and processes the context in chunks, then combines results.

This takes a **context-centric view** rather than a **problem-centric view** of input decomposition.

## Problem Addressed: Context Rot

Anthropic defines context rot as "when the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases." RLMs directly mitigate this by recursively processing context chunks rather than presenting all at once.

## Code

- Main: https://github.com/alexzhang13/rlm
- Minimal: https://github.com/alexzhang13/rlm-minimal

## Key Insight

RLMs represent the next milestone in general-purpose inference-time scaling after CoT-style reasoning models and ReAct-style agent models. Models trained explicitly to recursively reason are likely the next paradigm shift in long-context processing.
