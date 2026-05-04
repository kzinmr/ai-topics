---
title: "With Mobius Labs' Aana models, Dropbox brings deeper multimodal understanding to Dash"
source: "Dropbox Tech Blog"
url: "https://dropbox.tech/machine-learning/mobius-labs-aana-dropbox-multimodal-understanding"
author: "Dropbox"
date: 2026-05-04
tags:
  - dropbox
  - mobius-labs
  - multimodal
  - aana
  - quantization
  - hqq
  - gemlite
---

# Integration of Mobius Labs / Aana into Dropbox Dash

Dropbox has integrated **Mobius Labs** and its **Aana** multimodal models into **Dropbox Dash**, its context-aware AI assistant. This integration provides deeper understanding and searchability across text, images, audio, and video at an "exabyte scale."

## The Core Challenge: Multimodal Fragmentation
Modern teams work across scattered apps and formats. Traditional search fails with rich media because:
- A single video contains scene changes, speaker shifts, on-screen text, and audio cues
- Meaning is derived from how sound, visuals, and language relate
- Processing exabytes of content is traditionally cost-prohibitive

## The Aana Multimodal Engine
Aana treats different media types as an integrated whole rather than separate streams.

### Key Technical Components
- **Audio:** Uses inference-optimized Whisper-like models ([faster-whisper-large-v3-turbo](https://huggingface.co/mobiuslabsgmbh/faster-whisper-large-v3-turbo))
- **Vision & Language:** Transformer-based and **Mixture-of-Experts (MoE)** architectures for off-the-shelf GPUs
- **Shared Vector Space:** Distills all information into a single space; search for specific moments without manual scrubbing

### Efficiency & Optimization Tools
- **[HQQ (Half-Quadratic Quantization)](https://dropbox.tech/machine-learning/halfquadratic-quantization-of-large-machine-learning-models):** Enables low-bit (8-bit and 4-bit) inference
- **[Gemlite](https://github.com/mobiusml/gemlite):** Accelerates core AI operations via custom GPU kernels
- **[Aana SDK](https://github.com/mobiusml/aana_sdk):** Manages batching, model coordination, and GPU utilization

## Key Capabilities
- **Temporal Tracking:** Following object movement and layout changes in video
- **Cross-Modality Insights:** Connecting verbal statements to visual actions
- **Creative Archives:** Surfacing visual motifs across years of assets
- **Meeting Summarization:** Turning client meetings into searchable highlights

## Future: Agentic Workflows
Dropbox intends to use Aana as a foundation for **agentic workflows** that will surface insights and eventually **take action** on behalf of teams.
