---
type: raw_article
title: "Accelerating GPT-5.6 Sol Ultrafast with OpenAI"
source: "cerebras.ai/blog"
source_url: "https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai"
date: 2026-08-13
date_ingested: 2026-08-14
author: "Joyce Er (Cerebras)"
tags: [cerebras, inference, openai, gpt, hardware]
---

# Accelerating GPT-5.6 Sol Ultrafast with OpenAI

Cerebras and OpenAI are sharing an early look at **Ultrafast Mode**, a new service tier launching first in the OpenAI API and powered by Cerebras. Cerebras powers GPT-5.6 Sol on Ultrafast mode, delivering up to **750 output tokens per second** without any quality compromise.

## Speed vs Intelligence Tradeoff

AI builders have always needed to choose between speed and intelligence. GPT-5.6 Sol Ultrafast resolves this tradeoff. Compared with output speeds reported by Artificial Analysis, GPT-5.6 Sol on Ultrafast mode runs **11× faster than Fable 5**, and **5× faster than Opus 4.8 on Fast mode**.

## Humanity's Last Exam Benchmark

Cerebras ran Ultrafast head-to-head on Humanity's Last Exam (HLE; 2,500 PhD-level questions):

- GPT-5.6 Sol on Ultrafast mode answered all 2,500 HLE questions in **11 hours 11 minutes**.
- Claude Fable 5 needed **78 hours 27 minutes** (3+ days) for the same.
- Ultrafast worked through the frontier of human knowledge in a single working day, achieving comparable accuracy nearly **7× faster**.

(Benchmarking: GPT 5.6 Sol Ultrafast with Codex on xhigh reasoning July 10; Claude Fable 5 with Claude Code on xhigh reasoning July 13–15.)

## GDP-Val

On GDP-Val (economically valuable knowledge-work tasks), Ultrafast delivered a **5.6× end-to-end speedup with no quality degradation**. (Benchmarked July 31, 2026, GPT 5.6 Sol vs Sol Ultrafast on medium reasoning within Codex.)

## Architecture: Wafer-Scale Engine

Fast frontier inference is a data movement problem: on GPUs, large-model inference is bottlenecked by memory bandwidth (weights repeatedly transferred between on-chip and off-chip memory). Cerebras packs **44 GB of SRAM on each wafer-sized chip** — weights stay on-chip, tokens flow uninterrupted through model layers pipelined across wafers. This scales smoothly with model size.

## Availability

Limited preview to a select group of customers; access expands as capacity grows.
