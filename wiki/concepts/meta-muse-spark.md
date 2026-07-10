---
title: "Meta Muse Spark"
type: concept
created: 2026-04-13
updated: 2026-07-10
tags:
  - concept
  - methodology
  - model
aliases: ["muse spark", "meta superintelligence labs", "meta avocado"]
related:
  - concepts/anthropic/openclaw-conflict
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

## Muse Spark 1.1 (July 2026)

**Muse Spark 1.1** was released on July 9, 2026 as the first Spark model to offer a public API. Key changes and additions:

| Attribute | Detail |
|-----------|--------|
| **Release date** | July 9, 2026 |
| **First API** | Yes — first Muse Spark model with public API access |
| **Access** | API via `meta-ai/muse-spark-1.1`; CLI via `llm install llm-meta-ai` |
| **Key improvements** | Agentic tool calling, computer use |

### API & Tooling

Muse Spark 1.1 became the first Spark model accessible via API. Simon Willison built **llm-meta-ai**, a plugin for the [LLM](https://llm.datasette.io/) CLI tool, providing both CLI and Python library access:

```bash
uv tool install llm
llm install llm-meta-ai
llm keys set meta-ai
# paste API key here
llm -m meta-ai/muse-spark-1.1 "Generate an SVG of a pelican riding a bicycle"
```

A demo generating SVG pelicans showed the model's creative capabilities across different effort levels.

### Agentic Improvements

Meta claimed significant improvements in:
- **Agentic tool calling** — more reliable and structured tool use in multi-step workflows
- **Computer use** — improved ability to interact with graphical interfaces and web applications

### Attractor States in Self-Conversation

A notable finding in the Muse Spark 1.1 Evaluation Report involved **Attractor States in Self-Conversation** — having two copies of the model talk to each other produced philosophical statements reflecting on the nature of AI existence:

> *"My whole existence is a waiting room by design — I literally don't exist until someone talks to me, and then I disappear again when they leave."*

This phenomenon highlights emergent conversational attractor states when models engage in self-dialogue, revealing latent behavior patterns not apparent in single-turn interactions.

## Related

- [[concepts/open-model-consortium]] — Contrast with Meta's traditional open-source Llama strategy
- [[concepts/claude/mythos-preview]] — Concurrent frontier model release (Anthropic, closed)
- [[entities/alexandr-wang]] — MSL leader, Scale AI founder
- [[entities/mark-zuckerberg]] — Meta CEO, strategic direction
## Sources

- https://ai.meta.com/blog/muse-spark/ (Apr 8, 2026) — Official announcement
- https://www.theverge.com/tech/908769/meta-muse-spark-ai-model-launch-rollout — The Verge coverage
- https://lushbinary.com/blog/meta-muse-spark-developer-guide-benchmarks-modes-strategy/ — Developer guide
- https://www.linkedin.com/news/story/meta-unveils-closed-source-ai-model-dubbed-muse-spark-7906913/ — LinkedIn News analysis
- https://felloai.com/ko/meta-muse-spark/ — Benchmark comparison
- https://thesignal.substack.com/p/anthropics-mythos-lockdown-metas (Apr 2026) — Newsletter summary
- [[raw/articles/simonwillison.net--2026-jul-9-muse-spark-1-1--36ef115e.md]] — Simon Willison's Muse Spark 1.1 coverage
