---
title: "Rahul Sengottuvelu"
tags:
  - ai-agents
  - model
  - prompting
  - entity
  - rag
  - evaluation
  - inference
created: 2026-04-24
updated: 2026-04-24
type: entity
---

# Rahul Sengottuvelu

**URL:** https://rahul.gs/
**Blog:** rahul.gs
**Twitter/X:** @rahulgs
**GitHub:** 1rgs
**Role:** Head of Applied AI at Ramp; Co-founder & former CTO of Cohere.io
**Projects:** Jsonformer, AI agent scaffolding, constrained decoding

## Overview

Rahul Sengottuvelu is the Head of Applied AI at Ramp, where he leads the company's AI engineering strategy and product development. He co-founded and served as CTO of Cohere.io, an AI-powered customer support automation platform acquired by Ramp in June 2023. Before that, he worked on on-device ML at Facebook and product engineering at Superhuman.

Sengottuvelu is best known in the AI engineering community as the creator of Jsonformer, widely credited as the first constrained decoding library for LLMs (4.7K+ GitHub stars). The library pioneered the technique of filling in fixed JSON structure tokens during generation while delegating only content tokens to the language model — an approach that made structured JSON output from LLMs bulletproof rather than brittle.

His thinking on AI agent architecture has been influential in the industry. In his AI Engineer Summit talk "Rethinking how we Scaffold AI Agents" (March 2025, 36K+ views), he argued for embracing what he calls the "bitter lesson" — that systems with expandable computation consistently outperform hand-engineered systems with limited computation. His approach at Ramp involves connecting AI agents to existing frontends rather than rebuilding feature-by-feature, enabling "computer use" agents to leverage full product functionality from day one.

Sengottuvelu studied Statistics, Computer Science, and Math at Duke University. He is an active angel investor with positions in Modal, Cognition, Rutter, Moab, Skio, and others. He has spoken at New York Tech Week, Harvard Business School, Sequoia Capital, and Primary VC on topics ranging from ML commercialization to AI agent strategy.

## Timeline

| Date | Event |
|------|-------|
| ~2018–2020 | Software engineering internships at Facebook (on-device ML) and Superhuman (product engineering, web performance) |
| 2020 | Co-founded Cohere.io (with Yunyu Lin and Jason Wang) — an AI-powered customer support automation platform |
| 2021 | Cohere.io raised $3.5M from Initialized Capital, Y Combinator, and others; Jsonformer project launched on GitHub |
| 2021–2023 | Jsonformer adopted by LangChain ecosystem; Guardrails AI integrated it for constrained JSON decoding |
| 2023 (June) | Cohere.io acquired by Ramp; team of 6 engineers joins Ramp |
| 2023–present | Head of Applied AI at Ramp — leading AI product strategy, agent architecture, and ML engineering |
| 2024 | Featured in TechCrunch, Forbes, Business Insider for Ramp's AI initiatives |
| 2025 (March) | Delivered "Rethinking how we Scaffold AI Agents" at AI Engineer Summit (36K+ YouTube views) |
| 2025 (May) | Presented "How Ramp solved the Fatal Flaw in AI Agent Strategy" at Sequoia Capital's AI Ascent |
| 2025 | Spoke at Harvard Business School (HBS 1509) on "Managing and Innovating in Financial Services" |
| 2025 | Spoke at New York Tech Week on "Bringing ML to Market" |
| 2025 | Forbes 30 Under 30 recognition for Enterprise Technology |
| 2026 | Active angel investor across AI infrastructure, fintech, and developer tooling companies |

## Core Ideas

### The Bitter Lesson Applied to AI Agents

Sengottuvelu's central thesis for AI agent architecture is rooted in Rich Sutton's famous essay "The Bitter Lesson" — the observation that the biggest gains in AI have come from leveraging massive computation through general methods, rather than through human-engineered heuristics. Applied to AI agents, this means building systems where the LLM can access and use computational resources (code interpreters, browser automation, tool chains) rather than trying to encode human reasoning patterns directly into prompts.

> "Limited computation simulating human thought processes doesn't work well. When you scale computation, general methods always tend to outperform tailored engineering."

This philosophy manifests in Ramp's AI products: instead of building hand-crafted tool interfaces for each feature, they connect agents to the existing frontend, letting the agent "computer use" the full product. This gives feature completeness from day one and leverages the engineering work of frontend teams.

### Constrained Decoding as Structural Engineering

Jsonformer emerged from a practical problem: language models are terrible at generating valid JSON reliably. Prompt engineering and post-processing were brittle and error-prone. Sengottuvelu's insight was that in structured data generation, many tokens are fixed and predictable (braces, commas, keys, type markers). By filling in these structural tokens directly and only delegating content token generation to the model, Jsonformer guarantees syntactically correct, schema-conforming output.

This approach became foundational for the Guardrails AI ecosystem and influenced how the industry thinks about LLM output reliability. The key innovation wasn't in model architecture but in the decoding process — a systems-level intervention that made unreliable models produce reliable structured output.

### AI Agent Architecture: Flipping the Stack

In his AI Engineer Summit talk, Sengottuvelu presented three generations of AI agent architecture:

1. **Classical agents** — pure code execution, no LLM involvement, constrained but limited
2. **Hybrid agents** — LLM partially involved but with heavy hand-engineered scaffolding (the current state of most implementations)
3. **Flipped agents** — LLM decides when it needs computational resources, then accesses them directly

The third approach is what he advocates for at Ramp. Instead of encoding all possible tool paths, you give the LLM access to a code interpreter or browser and let it figure out the path. This scales better because it doesn't require engineering every edge case — the general method handles novel situations.

### The Agent Economy

Sengottuvelu has written and spoken about what he calls the "Agent Economy" — a future where external AI agents interact with products on behalf of users. In this world, companies that only offer chat interfaces to their agents will lose to companies that provide full programmatic access. His advice: "Before letting external agents computer-use your product, learn to computer-use yourself."

This has strategic implications for any company with an existing user base and mature software product. The companies that will win are those that build complete tool interfaces across their entire feature set, not those that create "feature-incomplete, second-class experiences."

### Structured Data from Unstructured Inputs

At Ramp, Sengottuvelu's team uses constrained decoding to extract structured information from contracts, invoices, and receipts — massive volumes of unstructured financial data that need to be parsed for price intelligence and expense management. This is a direct application of Jsonformer's core technique to real business problems, where getting the wrong JSON structure could mean losing money on a contract or misclassifying an expense.

## Key Quotes

> "Limited computation simulating human thought processes doesn't work well. When you scale computation, general methods always tend to outperform tailored engineering."

> "Before letting external agents computer-use your product, learn to computer-use yourself."

> "I want to convey one idea — we'll start off, all of you probably read the essay, bitter lesson, just quickly go through what it is."

> "People are building feature-incomplete, second-class experiences that frustrate their users, and everyone seems to fail in the same way."

> "Don't reinvent the wheel. By building heuristics and scaffolding on top of your frontend, you can give agents complete access."

> "As AI agents become more prevalent in what I call the emerging Agent Economy, having complete tool interfaces across your feature set will become increasingly important."

## Related Wikilinks

- [[concepts/ai-agent-architecture]] — Sengottuvelu's work on agent scaffolding and the "bitter lesson" applied to AI agents
- [[concepts/constrained-decoding]] — The technique pioneered in Jsonformer for reliable structured output
- [[concepts/ramp]] — The fintech company where Sengottuvelu currently leads Applied AI
- [[concepts/cohereio]] — His co-founded startup, acquired by Ramp in 2023
- [[concepts/rich-suttons-bitter-lesson]] — The foundational essay that informs Sengottuvelu's approach to AI agent design
-  — Sengottuvelu's concept of a future where AI agents interact with products programmatically
-  — His position on LLMs as engineering partners, not replacements
-  — The application of constrained decoding to financial document processing

## Influence Metrics

- Jsonformer: 4.7K+ GitHub stars, integrated into the Guardrails AI ecosystem and LangChain documentation
- AI Engineer Summit talk: 36K+ YouTube views, one of the most-watched talks on agent architecture
- Cohere.io: 200+ companies used the platform including Deel, Loom, SecureFrame, and Ramp itself
- Forbes 30 Under 30 for Enterprise Technology (2025)
- Angel investor in Modal, Cognition, Rutter, Moab, Skio, and other AI/infrastructure startups
- Featured in TechCrunch, Forbes, Business Insider for Ramp's AI initiatives
- Regular speaker at premier tech events: Sequoia Capital, HBS, NY Tech Week, AI Engineer Summit

## Sources

- [rahul.gs](https://rahul.gs/) — Personal website
- [gen.rahul.gs](https://gen.rahul.gs/) — Secondary personal site with investments and achievements
- [TechCrunch: "As the generative AI craze rages on, Ramp acquires customer support startup Cohere.io"](https://techcrunch.com/2023/06/26/as-the-generative-ai-craze-rages-on-fintech-ramp-acquires-ai-powered-customer-support-startup-cohere-io/) (June 26, 2023)
- [Crowdfund Insider: "Artificial Intelligence Startup Cohere.io Joins Ramp"](https://www.crowdfundinsider.com/2023/06/209387-artificial-intelligence-startup-cohere-io-joins-ramp-to-bring-generative-ai-to-finance/) (June 2023)
- [AI Engineer Summit: "Rethinking how we Scaffold AI Agents" (YouTube)](https://www.youtube.com/watch?v=-rsTkYgnNzM) (March 2025)
- [Inference by Sequoia: "How Ramp solved the Fatal Flaw in AI Agent Strategy"](https://inferencebysequoia.substack.com/p/how-ramp-solved-the-fatal-flaw-in) (May 2025)
- [The Org: Rahul Sengottuvelu profile](https://theorg.com/org/ramp/org-chart/rahul-sengottuvelu)
- [guardrails-ai/jsonformer](https://github.com/guardrails-ai/jsonformer) — GitHub repository (forked from 1rgs/jsonformer)
- [RahulG-12 GitHub](https://github.com/RahulG-12) — Public activity and projects
