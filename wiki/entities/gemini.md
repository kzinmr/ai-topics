---
title: "Gemini"
type: entity
created: 2026-04-25
updated: 2026-04-25
tags: [model, multimodal, text-generation, image-generation, google]
aliases: ["Gemini models", "Google Gemini"]
sources: [raw/newsletters/2026-04-24-chatgpt-images-2-0-is-genuinely-fantastic.md]
---
# Gemini

| | |
|---|---|
| **Type** | Multimodal AI Model Family |
| **Company** | Google / Google DeepMind |
| **Models** | Gemini 1.5, Gemini 2.0, Gemini 3.1 Flash, etc. |
| **Capabilities** | Text, images, audio, video understanding and generation |

## Overview

Gemini is Google's multimodal AI model family, developed by Google DeepMind and Google Research. Gemini models handle text, images, audio, and video as input/output, forming the backbone of Google's AI products and services.

## Model Family

- **Gemini 1.5** — Early version with strong multimodal capabilities and long context windows
- **Gemini 2.0** — Next-generation improvements in reasoning, multimodal understanding, and generation
- **Gemini 3.1 Flash** — Optimized for speed with TTS (text-to-speech) capabilities
- **Gemini Everywhere** — Google's push to integrate Gemini across all products

## Image Generation

Google's Gemini models power image generation through multiple channels:

- **Nano Banana 2 (NB2)** via Google AI Studio — The primary image generation product
  - Resolution: 512px through 4K
  - Aspect ratios: 1:1, 16:9, 9:16, 3:4, 4:5, 4:1, etc.
  - Speed: 20–25 seconds per generation
  - Weaker iteration control (natural language only)
  - Higher hallucination rate in complex layouts

- **Gemini App** — Mobile image generation path
  - Loses aspect-ratio control compared to AI Studio
  - Adds watermark in bottom-right corner

## Competition with OpenAI

Gemini-powered image generation (NB2) competes directly with OpenAI's GPT Image 2 (ChatGPT Images 2.0):

| Dimension | Gemini/NB2 (Google) | GPT Image 2 (OpenAI) |
|-----------|--------------------|---------------------|
| Speed | 20–25s (faster) | 40–60s (slower) |
| Resolution | 512px–4K (flexible) | Not documented |
| Aesthetic | "Cartoonist" default | Professional, clean |
| Iteration | Natural language only | Select lasso + aspect ratio |
| Hallucinations | Higher | Significantly lower |

## Relationships
- [[google]] — Parent company (AI/ML division)
- [[nano-banana-2]] — NB2 image generation model
- [[chatgpt-images-2.0]] — OpenAI's competitor
- [[ai-image-generation]] — AI image generation overview

## Sources
- [Alex Banks, The Signal: "ChatGPT Images 2.0 is genuinely fantastic"](https://thesignal.substack.com/p/chatgpt-images-20-is-genuinely-fantastic) (2026-04-24) — comparative analysis
- [Ben's Bites: Gemini 3.1 Flash TTS](https://substack.com/redirect/417cdc81-3b4b-4bc6-af06-907920a73e36) — TTS model details
