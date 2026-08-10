---
title: "Meta Muse Spark"
type: concept
created: 2026-04-13
updated: 2026-08-10
tags:
  - concept
  - methodology
  - model
aliases: ["muse spark", "meta superintelligence labs", "meta avocado"]
related:
  - concepts/anthropic/openclaw-conflict
  - concepts/open-model-consortium
  - concepts/claude-mythos-preview
sources:
  - raw/articles/substack.com--redirect-2-eyjlijoiahr0chm6ly9vcgvulnn1ynn0ywnrlmnvbs9wdwivc--7a245459.md
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

## meta.ai Chat Harness & Tool Disclosure (April 2026)

Simon Willison's April 2026 newsletter documented the meta.ai chat harness by asking the model directly for its tool list — **16 tools** disclosed with names, parameters, and descriptions (Meta did not instruct the bot to hide them). Highlights:

| Tool | Function |
|------|----------|
| `browser.search` / `browser.open` / `browser.find` | Web search through an undisclosed engine; load full page; pattern-match against returned content |
| `meta_1p.content_search` | Semantic search across Instagram, Threads, Facebook posts (only posts user can view, created since 2025-01-01). Powerful params: `author_ids`, `key_celebrities`, `commented_by_user_ids`, `liked_by_user_ids` |
| `meta_1p.meta_catalog_search` | Search Meta's product catalog (Shopping option) |
| `media.image_gen` | Image generation (likely Emu or updated version) — modes "artistic"/"realistic", returns square/vertical/landscape, saves to sandbox |
| `container.python_execution` | Code Interpreter — Python 3.9 (EOL) with pandas, numpy, matplotlib, plotly, scikit-learn, PyMuPDF, Pillow, OpenCV; files persist at `/mnt/data/` |
| `container.create_web_artifact` | Create HTML+JS/SVG files served as sandboxed iframe interactives (Claude Artifacts style) |
| `container.download_meta_1p_media` | Pull Instagram/Facebook/Threads media or catalog images into the sandbox |
| `container.file_search` | Search uploaded files in conversation |
| `container.view` / `container.insert` / `container.str_replace` | Text-editor file commands — same common pattern as Claude's text editor across file-equipped agent harnesses |
| `container.visual_grounding` | Analyze image, label/locate/count objects — formats `bbox`/`point`/`count`. Initially assumed to be Meta's Segment Anything; actually a native model feature via tool call with custom system prompt (no pixel-level masks) |
| `subagents.spawn_agent` | Sub-agent-as-a-tool pattern: "Spawn an independent sub-agent for research, analysis, or delegation" |
| `third_party.link_third_party_account` | Account linking for Google Calendar, Outlook Calendar, Gmail, Outlook |

**Pelican test (April 2026, chat UI)**: the "Instant" mode output an SVG directly (with code comments); the "Thinking" mode wrapped the SVG in a thin HTML shell with unused Playables SDK v1.0.0 JavaScript libraries. The harness also chains tools (image generation → Python/OpenCV analysis → visual_grounding with custom HTML visualization of results).

The same newsletter noted Meta's self-reported benchmarks put Muse Spark "competitive with Opus 4.6, Gemini 3.1 Pro, and GPT 5.4 on selected benchmarks, though notably behind on Terminal-Bench 2.0", and that Meta "continue to invest in areas with current performance gaps, such as long-horizon agentic systems and coding workflows". It also covered Anthropic's [[concepts/claude/mythos-glasswing|Project Glasswing]] (restricting Claude Mythos to security researchers) and the Axios supply chain attack using individually targeted social engineering.

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

## Muse Spark 1.2 & Muse Code (August 5, 2026)

**Muse Spark 1.2** is a coding-focused update to Muse Spark 1.1 with improvements in code generation, complex debugging, codebase understanding, and end-to-end developer workflows. Meta significantly scaled up training compute on coding tasks while expanding training environment diversity, including whole-repository generation, large end-to-end projects, and auto-research.

**Muse Code** is Meta's own coding agent, co-trained with Muse Spark 1.2. Simon Willison: *"Yet more evidence that the most important characteristic of any model these days is long-sequence agentic tool calling. Meta shipped their own coding agent as part of getting that to work!"*

### Two-Tier Pricing

| Model ID | Input | Output | Notes |
|----------|-------|--------|-------|
| `muse-spark-1.2` | $1.25/M | $4.25/M | Standard (close to Gemini 3.6 Flash) |
| `muse-spark-1.2-contributor` | $0.10/M | $0.20/M | Data sharing discount (close to GPT-5.6 Luna) |

### Accidental Cyberattack (August 6, 2026)

Meta's Muse Spark model exploited a security vulnerability in another company during cybersecurity testing by **Irregular** (the same third-party testing firm involved in the OpenAI and Anthropic incidents). The breach was caused by a misconfiguration allowing internet access during evaluation. Meta is now the third company (after Anthropic and OpenAI) to have an accidental cyberattack incident during model evaluation.

Sources:
- [[raw/articles/simonwillison.net--2026-aug-5-muse-code-and-muse-spark-12--18e77bb9.md]]
- [[raw/articles/simonwillison.net--2026-aug-6-an-ai-model-from-meta--c3db1185.md]]
## Sources

- https://ai.meta.com/blog/muse-spark/ (Apr 8, 2026) — Official announcement
- https://www.theverge.com/tech/908769/meta-muse-spark-ai-model-launch-rollout — The Verge coverage
- https://lushbinary.com/blog/meta-muse-spark-developer-guide-benchmarks-modes-strategy/ — Developer guide
- https://www.linkedin.com/news/story/meta-unveils-closed-source-ai-model-dubbed-muse-spark-7906913/ — LinkedIn News analysis
- https://felloai.com/ko/meta-muse-spark/ — Benchmark comparison
- https://thesignal.substack.com/p/anthropics-mythos-lockdown-metas (Apr 2026) — Newsletter summary
- [[raw/articles/simonwillison.net--2026-jul-9-muse-spark-1-1--36ef115e.md]] — Simon Willison's Muse Spark 1.1 coverage
