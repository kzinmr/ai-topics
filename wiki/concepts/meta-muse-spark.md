---
title: "Meta Muse Spark"
type: concept
created: 2026-04-13
updated: 2026-04-24
tags: [concept, meta, frontier-models, closed-source, muse, alexandr-wang]
aliases: ["muse spark", "meta superintelligence labs", "meta avocado"]
related:
  - concepts/anthropic-openclaw-conflict
  - concepts/open-model-consortium
  - concepts/claude-mythos-preview
sources: []
---

# Meta Muse Spark

## Overview

**Muse Spark** is Meta's first model from **Meta Superintelligence Labs (MSL)**, announced on **April 8, 2026**. Internally codenamed "Avocado", it was built over nine months after a complete ground-up rebuild of Meta's AI stack. It marks a strategic shift from Meta's open-source Llama strategy to a closed-source, consumer-facing model designed to power Meta AI across Facebook, Instagram, WhatsApp, Messenger, and smart glasses.

## Key Facts

| Attribute | Detail |
|-----------|--------|
| **Developer** | Meta Superintelligence Labs (MSL) |
| **Lab Leader** | Alexandr Wang (Scale AI founder, $14.3B investment) |
| **Internal Codename** | "Avocado" |
| **Launch Date** | April 8, 2026 |
| **License** | Closed-source (open weights planned, no timeline) |
| **Access** | Free via meta.ai and Meta AI app |
| **API** | Private preview for select partners |
| **Input** | Text, image, voice |
| **Output** | Text-only (currently) |

## Architecture & Capabilities

- **Natively multimodal reasoning** — visual chain of thought, tool-use, multi-agent orchestration
- **Three reasoning modes**: Instant (fast default), Thinking (deeper reasoning), Contemplating (most powerful, rolling out gradually)
- **Training efficiency**: 10x less compute than Llama 4 for comparable results (per Meta)
- **Benchmarks**:
  - **52** on Artificial Analysis Intelligence Index v4.0 (top 5 overall: behind Gemini 3.1 Pro, GPT-5.4, Claude Opus 4.6)
  - **86.4** on CharXiv Reasoning (ahead of Claude Opus 4.6)
  - **#2** on Finance Agent v1.1
  - **#3** on overall Vals Index
  - **#1** on visual reasoning, embodied reasoning, multimodal understanding

## Strategic Significance

### Shift from Open to Closed

Muse Spark represents a **major strategic pivot** for Meta. The company built its AI reputation on open-source Llama models. Muse Spark is closed-source, with no open weights, no local deployment, and no fine-tuning access. Meta says it "hopes to open-source future versions" but no timeline has been announced.

> *"This is the first model from a new series of large language models built by Meta Superintelligence Labs. We are on our way to personal superintelligence."*
> — Meta blog post, Apr 8, 2026

### Competition Context

| Model | Developer | Open? | Key Strength |
|-------|-----------|-------|-------------|
| GPT-5.4 | OpenAI | ❌ | Coding (75.1), agentic tasks |
| Claude Opus 4.6 | Anthropic | ❌ | Safety, reasoning |
| Gemini 3.1 Pro | Google | ❌ | Multimodal, ecosystem |
| **Muse Spark** | **Meta** | ❌ | **Visual reasoning, multimodal understanding** |
| Llama 4 Maverick | Meta | ✅ | Developer ecosystem |

Muse Spark closes the gap to frontier models on multimodal tasks but still trails significantly on coding (59.0 vs GPT-5.4's 75.1). Meta acknowledges this as a "priority area for improvement."

### "Personal Superintelligence" Thesis

Meta's vision extends beyond chatbot responses. Muse Spark is designed as the core of a "personal superintelligence" — an assistant that:
1. Understands what you're seeing (camera glasses, phone camera)
2. Remembers what matters to you
3. Pulls in relevant creator/community context from Instagram, Facebook, Threads
4. Eventually takes action across Meta's products

### Distribution & Strategy
- **Now**: Meta AI app, meta.ai (US)
- **Coming weeks**: WhatsApp, Instagram, Facebook, Messenger, smart glasses
- **Developers**: Private API preview (no public pricing/docs yet)

### Distribution Advantage

Muse Spark has a unique distribution advantage over ChatGPT or Claude: **3 billion people already inside Meta's apps** (WhatsApp, Instagram, Facebook, Messenger). If this model meaningfully improves the AI inside these applications, users will no longer need external applications for AI interactions. The convenience of calling your AI in WhatsApp or exchanging voice notes "feels" more intuitive in the space where you message friends and family, especially as we move to voice-first modalities ([Alex Banks, Apr 2026](https://thesignal.substack.com/p/anthropics-mythos-lockdown-metas)).

This positions Muse Spark not just as a model, but as a **distribution moat** — the value isn't just in capability but in being the default AI layer inside the social graph.

## Related

- [[concepts/open-model-consortium]] — Contrast with Meta's traditional open-source Llama strategy
- [[concepts/claude-mythos-preview]] — Concurrent frontier model release (Anthropic, closed)
-  — MSL leader, Scale AI founder
-  — Meta CEO, strategic direction

## Sources

- https://ai.meta.com/blog/muse-spark/ (Apr 8, 2026) — Official announcement
- https://www.theverge.com/tech/908769/meta-muse-spark-ai-model-launch-rollout — The Verge coverage
- https://lushbinary.com/blog/meta-muse-spark-developer-guide-benchmarks-modes-strategy/ — Developer guide
- https://www.linkedin.com/news/story/meta-unveils-closed-source-ai-model-dubbed-muse-spark-7906913/ — LinkedIn News analysis
- https://felloai.com/ko/meta-muse-spark/ — Benchmark comparison
- https://thesignal.substack.com/p/anthropics-mythos-lockdown-metas (Apr 2026) — Newsletter summary
