---
title: "Interconnects AI tracked-models repository"
author: Interconnects AI (Nathan Lambert et al.)
date: 2026-10-13
type: web_article
source_url: https://github.com/Interconnects-AI/tracked-models
ingested: 2026-10-13
tags: [open-source, hugging-face, model-analytics, interconnects]
---

# Interconnects AI tracked-models repository

> Shared by Nathan Lambert (@natolambert) on X: https://x.com/natolambert/status/2110075913849504240 (2026-10-13): "Our model tracking repo is here and we welcome corrections!"

## What it is

Public list of HuggingFace models tracked by **Interconnects AI** for open model analytics. The project began with private daily download data from HuggingFace covering 7 organizations (1,971 models through July 10, 2025): deepseek-ai, google, meta-llama, microsoft, mistral-community, mistralai, Qwen. It has since expanded to additional frontier model providers, VLM families, and historically significant LLM orgs.

## Scope & inclusion rules

- Post-ChatGPT LLMs and VLMs (released after Nov 30, 2022) with **first-party weights on HuggingFace**.
- Threshold: >100K total downloads for new additions (exceptions for notable recent releases).
- Excluded despite high downloads: guard/shield models (Llama-Guard, ShieldGemma, Qwen3Guard, granite-guardian, wildguard, gpt-oss-safeguard, etc.) — safety classifiers, not generative LLMs.

## Files

- `models.csv` (primary) / `extra_models.csv` (secondary): columns `org`, `model`, `modelId`.
- `arxiv_models.csv`: arXiv model-family list.
- `local-models.csv` (added 2026-10-13): 1,606 conversion-only local copies of models.csv checkpoints, with parent region attribution, plus generator/validator/reviewed overrides. Separate cohort — do not add to main totals.
- `release_date_corrections.csv`: corrections where HuggingFace `created_at` differs from actual release date.
- Public CSV access: `curl -s https://raw.githubusercontent.com/Interconnects-AI/tracked-models/main/models.csv`

## Process

Weekly HuggingFace syncs add models per-org (e.g. 2026-09-28: +9 to models.csv from internlm/LiquidAI/XiaomiMiMo, +4 to extra from apple/llm-jp; 21 candidates rejected, 4 for manual review). Region attribution is explicitly documented (e.g. EleutherAI/BigCode classified as US by institutional attribution; TII as UAE). Corrections workflow via issues/PRs; supporting links live in correction history rather than the CSV. Legacy rows are labeled "Legacy data; not recently reviewed."

## Why it matters

This is the ground-truth denominator behind Interconnects' widely-cited HuggingFace download analytics (open model momentum posts) — now auditable and correction-friendly in public. It anchors claims about open-model adoption trends that Lambert and the open-models community debate frequently.
