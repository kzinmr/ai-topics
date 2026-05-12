---
title: "Multipath Reliable Connection (MRC)"
type: concept
created: 2026-05-12
updated: 2026-05-12
tags:
  - concept
  - networking
  - infrastructure
  - training
  - openai
  - nvidia
  - amd
  - inference
sources:
  - raw/newsletters/2026-05-10-spacexai-s-spice-trade-anthropic-targets-the-trillion-and-openai-s-stack-sweep.md
---

# Multipath Reliable Connection (MRC)

An open-source GPU communication protocol co-developed by **OpenAI, NVIDIA, AMD, Broadcom, Intel, and Microsoft**, released through the **Open Compute Project (OCP)** in May 2026. MRC enables GPU traffic to spread across hundreds of network paths and reroute around failures in microseconds, keeping thousands of GPUs in lockstep through congestion that used to stall training runs.

## How It Works

- **Multipath distribution**: GPU-to-GPU traffic is split across hundreds of parallel network paths rather than a single route
- **Microsecond rerouting**: When a path fails or congests, traffic is redirected in microseconds — fast enough that training synchronization is not disrupted
- **Lockstep preservation**: By preventing individual GPU stalls from cascading into cluster-wide training hangs, MRC dramatically improves training reliability at scale

## Strategic Significance

MRC represents a deliberate move by OpenAI to reduce hardware vendor lock-in:

- **Hardware portability**: An open protocol gives OpenAI portability across GPU vendors — NVIDIA, AMD, Broadcom, and Intel all co-developed it
- **Weakening NVIDIA's grip**: While NVIDIA still dominates GPU hardware, MRC ensures no single supplier controls the networking layer that frontier training depends on
- **OCP standardization**: Releasing through the Open Compute Project makes the protocol an industry standard rather than a proprietary solution

## Context: OpenAI's Stack Sweep (May 2026)

MRC was part of OpenAI's unusually busy May 2026 release week, which also included:

- **GPT-5.5 Instant**: Rolled out across ChatGPT with clearer, more concise responses in a warmer tone
- **GPT-Realtime-2**: GPT-5-class reasoning in voice API, with companion models for 70+ language translation and streaming transcription
- **Codex Chrome**: Running directly in Chrome on macOS and Windows via a plugin, working in parallel across tabs

## Related

- [[entities/openai]] — OpenAI's broader infrastructure strategy
- [[concepts/xai-anthropic-colossus-deal]] — GPU compute as strategic resource
- [[entities/nvidia]] — Dominant GPU hardware vendor
- [[concepts/distributed-training]] — Distributed training infrastructure challenges
- [[concepts/mixture-of-experts]] — Related infrastructure scaling
