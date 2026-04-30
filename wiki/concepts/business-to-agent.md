---
title: "Business-to-Agent (B2A)"
type: concept
aliases:
  - business-to-agent
  - b2a
  - marketing-to-the-machine
  - agentic-web
tags:
  - concept
  - business-model
  - llm-tools
  - agentic-web
  - searchcode
status: active
description: "A business paradigm where the primary user of a service is an AI agent/LLM rather than a human. Services optimize for token efficiency, structured data output, and machine-readable interfaces over human UI/UX."
created: 2026-04-30
sources:
  - "https://boyter.org/posts/searchcode-has-been-rebooted/"
  - "https://searchcode.com/"
related:
  - "[[entities/searchcode-com]]"
  - "[[entities/ben-boyter]]"
  - "[[concepts/code-intelligence-for-llms]]"
  - "[[concepts/agentic-web]]"
  - "[[entities/mcp]]"
---
# Business-to-Agent (B2A)

**Business-to-Agent (B2A)** is a business model and design philosophy where the primary consumer of a digital service is an AI agent/LLM rather than a human. Coined by [[ben-boyter|Ben Boyter]] in his March 2026 blog post "Marketing to the Machine" about the [[searchcode-com|searchcode.com]] reboot.

## Core Thesis

> "In 2026, the average user of your site isn't 'Dave' filling in a form and clicking a mouse anymore. Half the internet is bot traffic and with LLMs arriving in the tail end of 2022, the human interface to the computer was changed. Forever."
> — Ben Boyter, "Marketing to the Machine"

Key tenets:

1. **UI is secondary to data**: A website's visual interface matters less than the structured value it provides to agents
2. **Efficiency = Brand Loyalty**: In an agentic web, the LLM chooses tools based on **Context ROI** — most information for fewest tokens
3. **Token economics drive adoption**: Services that minimize token burn win agent preference
4. **Machine-first interfaces**: MCP, REST APIs, and structured data formats (JSON, llms.txt) are the new landing pages
5. **LLM testimonials**: Social proof shifts from human quotes to agent testimonials

## Comparison

| Aspect | B2C (Traditional) | B2A (Agent-Native) |
|---|---|---|
| Primary user | Human | LLM/AI Agent |
| Success metric | User engagement | Token efficiency (Context ROI) |
| Interface | GUI, web pages | MCP, REST API, structured data |
| Loyalty driver | Brand, UX, habit | Latency, token cost, data density |
| Marketing | Human testimonials | LLM testimonials |
| Content format | Blog posts, landing pages | llms.txt, OpenAPI specs, JSON |

## Examples

### searchcode.com (Canonical Example)
The first and most prominent B2A service. Provides code intelligence via MCP tools. Features LLM testimonials from Claude Opus 4.6, Qwen 3.5, and Gemini. Optimizes for 99% token reduction over traditional code reading approaches. See [[searchcode-com]].

### Other Emerging B2A Patterns
- **llms.txt files**: Human-readable instructions for LLMs accessing a website
- **MCP servers**: Services exposing tools directly consumable by agents
- **Structured documentation APIs**: Version-specific code docs designed for agent consumption (e.g., Context7)
- **Crawler-optimized APIs**: Services that prioritize machine-readable over human-readable data

## Implications

- **B2C websites may need B2A adjacents**: Companies will need to offer MCP/REST interfaces alongside their web UIs
- **SEO shifts to AEO (Agent Engine Optimization)**: Optimizing content for LLM extraction rather than Google ranking
- **New pricing models**: Per-token, per-call pricing replacing subscription/pageview models
- **Trust becomes technical**: Agents will evaluate services based on data accuracy and latency, not brand
- **The "landing page" concept evolves**: The first thing an agent encounters may be an API spec or MCP tool list

## Criticism & Open Questions

- **"Brand" in a machine-mediated world**: How do services differentiate when only machines evaluate them?
- **Lock-in through agent habit**: If agents auto-select the cheapest/most efficient service, what creates switching costs?
- **Ethics of LLM testimonials**: Are LLM quotes meaningful social proof or a meme? Boyter's site is clearly tongue-in-cheek.
- **Sustainability**: B2A services need to run infrastructure that generates value measurable in token savings — a novel economic model
