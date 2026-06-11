---
title: Perplexity Comet
type: entity
aliases:
- comet-browser
- perplexity-ai-browser
- perplexity-computer
created: 2026-04-13
updated: 2026-04-13
tags:
- entity
- product
- browser-agent
status: active
sources:
- https://en.wikipedia.org/wiki/Perplexity_Comet
- https://www.infoworld.com/article/4081396/when-will-browser-agents-do-real-work.html
- https://till-freitag.com/en/blog/perplexity-comet-ai-browser
---

# Perplexity Comet

**Perplexity Comet** is an AI-native browser developed by Perplexity AI. Released for Windows/macOS in July 2025, with Android support in November 2025 and iOS in March 2026. It is at the forefront of the "turn the browser into an AI agent" strategy.

## Overview

| Field | Details |
|---|---|
| Developer | Perplexity AI |
| Initial release | July 9, 2025 (Windows/macOS) |
| Android | November 20, 2025 |
| iOS | March 18, 2026 |
| Engine | Blink (Chromium-based) |
| License | Proprietary (OSS-based) |
| AI engine | Perplexity search API integration |
| Pricing | Free browser, AI features via Perplexity Pro ($20/month) |

## Architecture: Search-First Browser

Comet's core is a **search-first architecture**. While traditional browsers follow a "type URL → render page → user reads" flow, Comet **directly understands user intent and delegates tasks to agents on the web**.

### Agentic Browsing Features
1. **Natural language tasks**: "Find the cheapest flight to Berlin next week" → Comet searches, compares, presents results
2. **Context AI**: Highlight any text and ask questions → understands page context to answer
3. **Multi-tab synthesis**: Collects and summarizes information across multiple tabs
4. **Auto form fill**: Completes purchases, bookings, applications

### Perplexity Product Ecosystem
```
┌─────────────────┐
│ Perplexity Search│ ← Core AI search engine (brain)
├─────────────────┤
│  Comet Browser  │ ← AI-native browser (interface)
├─────────────────┤
│ Perplexity Computer│ ← Autonomous task execution (agent)
└─────────────────┘
```

## Competitive Advantage

| Strength | Details |
|---|---|
| Search integration | Integrates Perplexity answer-first search at the browser level |
| Speed | Compresses 5 steps (terminal→search→results) into 1 step |
| Multi-platform | Supports Windows, Mac, Android, iOS |
| Cost | Browser is free, AI features $20/month |

## Challenges and Risks

1. **Security**: LayerX Security discovered the "CometJacking" attack vector (August 2025). Malicious web pages can inject instructions into the AI agent
2. **Privacy**: AI monitors all browsing, creating data leak risk
3. **Ecosystem lock-in**: Heavy dependence on Perplexity services
4. **Automation reliability**: Errors on complex tasks

## Security Incident: CometJacking

In 2025, LayerX Security discovered a Comet-specific attack vector:
- Malicious web pages inject instructions into the AI agent
- Data leaks and unintended actions possible
- Perplexity released a fix patch in August 2025

## Market Position

| Competitor | Feature | Difference from Comet |
|---|---|---|
| ChatGPT Atlas | OpenAI AI browser | GPT integration vs Perplexity integration |
| Arc | UI innovation | Design-focused vs search-focused |
| Brave | Privacy-focused | Local AI vs cloud AI |
| Kahana Oasis | Enterprise AI browser | Consumer vs enterprise |

## Related Entities

- [[concepts/browser-agent/death-of-browser]] — The de-humanization of the browser
- [[entities/anthropic-computer-use]] — Anthropic Computer Use
- [[entities/openai-cua]] — OpenAI Computer-Using Agent
- [[entities/webmcp]] — Standardization protocol
- [[entities/manus]] — Local browser integration agent

## Sources

- [Wikipedia: Perplexity Comet](https://en.wikipedia.org/wiki/Perplexity_Comet)
- [Perplexity Comet Official Site](https://comet.perplexity.ai/)
- [When will browser agents do real work? (InfoWorld)](https://www.infoworld.com/article/4081396/when-will-browser-agents-do-real-work.html)
- [Perplexity Comet Analysis (Till Freitag)](https://till-freitag.com/en/blog/perplexity-comet-ai-browser)
