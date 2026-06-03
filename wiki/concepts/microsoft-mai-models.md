---
title: "Microsoft MAI Models"
created: 2026-05-12
updated: 2026-06-03
type: concept
tags: [microsoft, model, voice-ai, image-generation, openai, reasoning-model, code-model]
sources: 
  - raw/articles/2026-04-02_geekwire-microsoft-mai-models.md
  - raw/articles/simonwillison.net--2026-jun-2-microsofts-new-models--80348929.md
  - raw/newsletters/2026-06-03-ainews-microsoft-build-mai-thinking-1-and-mai-family-models.md
  - raw/articles/2026-06-03_eliebakouch-mai-tech-report-deep-dive.md
---

# Microsoft MAI Models

Microsoft's in-house AI model family (MAI: Microsoft AI), marking the company's strategic independence from its OpenAI partnership.

## Models

### MAI-Transcribe-1
Speech-to-text model released April 2, 2026. Claimed as most accurate available. Designed for noisy real-world conditions (call centers, conference rooms). Runs at half the GPU cost of competing state-of-the-art models. Built by a team of just 10 people. Competing directly with OpenAI's [[entities/openai|Whisper]] and Google Gemini on FLEURS benchmark.

### MAI-Voice-1
Voice generation model, now broadly available for commercial use. Generates natural-sounding speech. Supports custom voice creation from short audio samples.

### MAI-Image-2
Image generation model, top-3 on Arena.ai leaderboard. Deployed in Bing and PowerPoint. Broad commercial use now permitted.

## Build 2026 Updates

At Microsoft Build (June 2, 2026), the company announced five new/updated MAI models along with broader platform announcements for agents and developer tooling.

### MAI-Thinking-1
Microsoft's first dedicated reasoning model. A 1-trillion parameter Mixture-of-Experts model with 35B active parameters (per Simon Willison's correction — initial reports misread the MoE sizes). Trained from scratch with zero distillation and zero synthetic data, using 794 billion pages from a proprietary web crawl plus Common Crawl. Accompanied by a 109-page technical report. Microsoft claims it is "preferred to Sonnet 4.6 in our blind human side-by-side evaluations." Initially available only to select early partners.

**Key benchmarks**: AIME 2025 97.0%, AIME 2026 94.5%, SWE-Bench Pro 52.8%, LiveCodeBench v6 87.7%. Human evals: preferred to Sonnet 4.6 (49% win / 6% tie / 45% loss), loses to Opus 4.6 (43% / 5% / 52%).

> **Technical report deep dive**: See [[concepts/mai-thinking-1-tech-report]] for a detailed analysis of the architecture (interleaved dense/MoE, LatentMoE, global load balancing), the novel scaling ladder methodology, data pipeline transparency, modified GRPO post-training approach, and training infrastructure (8K GB200, 90% goodput, MAIA-200 inference).

### MAI-Code-1-Flash
A code-specialist model with 137B total parameters and 5B active (MoE). Built end-to-end by Microsoft using "appropriately licensed data." Purpose-built for GitHub Copilot and VS Code to deliver high performance at lower cost. Rolling out to GitHub Copilot individual users in Visual Studio Code.

### MAI-Image-2.5
Updated image generation model building on MAI-Image-2. Details on specific improvements were shared at Build.

### MAI-Transcribe-1.5
Updated speech-to-text model following MAI-Transcribe-1 (April 2026). Performance and accuracy improvements.

### MAI-Voice-2
Updated voice generation model following MAI-Voice-1 (April 2026). Improved naturalness and voice customization capabilities.

### Platform Announcements
Alongside the models, Microsoft announced several related initiatives at Build:
- **Windows as an agent runtime** — positioning Windows as the native execution environment for AI agents
- **GitHub Copilot app** — a standalone application expanding Copilot beyond IDE integration
- **Web IQ for agents** — a new capability enabling agents to intelligently browse and extract information from the web

## Strategic Significance

The April 2026 MAI model launch was Microsoft's first major model release since CEO Satya Nadella's March 2026 reorganization, where [[entities/mustafa-suleyman]] shifted from Copilot oversight to focus on frontier model development and superintelligence.

The Build 2026 announcements mark a significant acceleration: with MAI-Thinking-1 and MAI-Code-1-Flash, Microsoft now competes directly with OpenAI on reasoning and code models, while expanding the platform vision with Windows as an agent runtime, GitHub Copilot app, and Web IQ. The MAI model family covers voice, image, code, and reasoning — a full-stack AI strategy that reduces reliance on OpenAI.

Microsoft plans to eventually build a frontier LLM "completely independent" of OpenAI if needed. All MAI models are available on Microsoft Foundry and MAI Playground.

## Related Pages
- [[entities/microsoft]] — Microsoft entity page
- [[entities/mustafa-suleyman]] — Microsoft AI CEO
- [[entities/openai]] — OpenAI partnership context
- [[concepts/ai-services-joint-ventures]] — OpenAI DeployCo and enterprise AI services
