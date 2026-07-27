---
title: Screenpipe
created: 2026-07-26
updated: 2026-07-26
type: entity
tags:
  - ai-agents
  - open-source
  - developer-tooling
  - product
  - ycombinator
  - privacy
  - mcp
  - desktop-automation
  - screen-recording
  - quantified-self
sources:
  - raw/articles/2026-07-23_screenpipe-yc-s26-screen-to-agent.md
  - https://github.com/screenpipe/screenpipe
  - https://screenpipe.com
  - https://news.ycombinator.com/item?id=49024620
related:
  - "[[concepts/coding-agents/coding-agents]]"
  - "[[concepts/ai-agent-memory]]"
  - "[[concepts/local-llm/local-ai]]"
  - "[[entities/hermes-agent]]"
  - "[[entities/openclaw]]"
  - "[[concepts/mcp]]"
---

# Screenpipe

**Screenpipe** is a 24/7 local AI screen and microphone recording tool that captures everything you do on your computer and turns it into agent-accessible, searchable data. Think of it as "Rewind.ai but open source and agent-oriented." Built by Louis Beaumont as part of YC S26.

## Overview

Screenpipe continuously records your screen and audio locally, indexing everything into a searchable timeline. It captures screenshots paired with accessibility tree data on meaningful events (app switches, clicks, typing pauses, scrolling), runs OCR when structured data is unavailable, and transcribes audio via local Whisper/Parakeet models. The result is an AI-friendly API (port 3030) with MCP and skills support, letting agents query your digital history.

It integrates with Claude, ChatGPT, Hermes Agent, OpenClaw, and 100+ other apps.

## Key Features

- **Local-first & private**: All data stored locally. PII redaction model runs on-device (Apple MLX, Windows DirectML). Supports confidential cloud inference for low-end devices. Target: <1% CPU, <400 MB RAM.
- **Open source (source-available)**: Screenpipe Commercial License — free for personal, nonprofit, educational, research. Commercial use requires a license. Pre-license versions remain MIT.
- **Screen + audio capture**: Accessibility tree + screenshot on meaningful events; continuous audio with speaker ID and transcription.
- **OCR pipeline**: Falls back to OCR when structured accessibility data is unavailable.
- **Searchable timeline**: Indexed in local SQLite database, mp4, and markdown files.
- **MCP integration**: Agents can query Screenpipe via MCP or direct API.
- **Recording schedules & filtering**: Exclude specific apps, windows, URLs. Incognito-aware. Schedule-based recording (e.g., no weekends).
- **Agent use cases**: Personal wikis, meeting transcripts, CRM automation, productivity tracking, automated documentation.

## Technology

- **Core**: Rust, with MLX, ONNX for ML inference
- **Apple APIs**: cidre, direct C calls
- **Windows APIs**: windows-rs
- **Experimental Linux support**
- **AI models**: Local OCR, local Whisper/Parakeet for transcription, local PII redaction
- **Storage**: SQLite, mp4, markdown files
- **Agent interface**: REST API on port 3030, MCP, skills system

## Use Cases

1. **Agent memory**: Give AI agents persistent, searchable memory of everything you've seen, said, and heard.
2. **Productivity tracking**: "Retrieve the tasks I was working on from 8 am to 4 pm."
3. **Personal wiki / second brain**: "Every hour, organize everything I do into projects, people, tasks in my Obsidian vault."
4. **Meeting transcripts**: Continuous audio capture with transcription and speaker identification.
5. **Automated documentation**: Turn repetitive tasks into SOPs by observing workflows.
6. **CRM automation**: "Whenever I visit someone's LinkedIn profile, update my CRM."
7. **Automation discovery**: Analyze team activity to surface automation opportunities.

## Background

Louis Beaumont had been building "second brain" tools since 2020. He built Ava, the first Obsidian AI plugin (thousands of users), then Embedbase (RAG API). The core insight: models need deep context about what you're doing on your computer to truly automate your work.

Screenpipe started as a CLI in 2024. An HN post (https://news.ycombinator.com/item?id=41695840) shaped the product with feedback on recording consent, local security, CPU usage, and signal-to-noise.

## GitHub Stats

| Metric | Value |
|--------|-------|
| Stars | 20,538 |
| Forks | 2,028 |
| Language | Rust |
| Open Issues | 101 |
| License | Screenpipe Commercial License (source-available) |
| Created | June 2024 |

## YC S26 Launch

Launched on HN as part of Y Combinator Summer 2026 batch on July 23, 2026. The Launch HN post received 84 points and 23 comments. Key discussion topics included privacy, local vs. cloud AI, license changes (MIT → source-available), and the "email harvesting from GitHub stars" controversy (founder apologized, practice discontinued).

## Privacy & Controversy

- **Privacy concerns**: 24/7 recording raises questions about segregating personal and professional use. Screenpipe addresses this with app/URL filtering, recording schedules, incognito awareness, and local-only storage.
- **Email harvesting incident**: Screenpipe was criticized for collecting GitHub stargazer emails for marketing (via [skerritt.blog post](https://skerritt.blog/screenpipe-ai-company-will-harvest-your-email-against-your-permission/)). Louis Beaumont apologized on HN: "it's been a while ago, we didn't know that emails on GitHub were not allowed to be used... We apologized to our users and never did this again."
- **License change**: Originally MIT, switched to Screenpipe Commercial License for sustainability. Pre-change versions remain MIT.
