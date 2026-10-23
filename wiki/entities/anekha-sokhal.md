---
title: "Anekha Sokhal"
type: entity
created: 2026-10-23
updated: 2026-10-23
tags:
  - person
  - founder
  - ai-agents
  - vertical-agent
  - ai-native
  - fintech
  - startup
  - domain-expertise
aliases: ["Anekha Sokhal", "Moshi"]
sources:
  - raw/newsletters/2026-10-22-the-recommendation-engine-for-commodity-traders-anekha-sokhal-moshi.md
  - https://www.latent.space/p/you-are-the-team
---

# Anekha Sokhal

**Anekha Sokhal** is the founder & CEO of **Moshi** ([hellomoshi.ai](https://hellomoshi.ai)), a recommendation engine for **commodity traders**. She spoke about building Moshi at **AI Engineer NYC 2026** (Latent Space episode "You are the Team"). A former energy-derivatives trader, she is building the tool she wished she had on the desk — an AI system that connects market information to what actually matters for an individual trader's book.

> Note: distinct from **Moshi**, the speech-text model by Kyutai. This is the commodity-trading startup at hellomoshi.ai.

## Background

- **JPMorgan energy derivatives trader** before founding Moshi.
- Academic background in **mathematics, operations research, statistics, and economics** at the **University of Warwick**.
- The founding motivation: as a trader, staying on top of the market meant tracking more information than any single person could read. Moshi is the recommendation engine she wanted.

## Moshi — a recommendation engine for commodity traders

Sokhal describes Moshi as **"what might happen if Bloomberg, Claude and Netflix had a baby"** — market data (Bloomberg) + an AI interface (Claude) + a Netflix-style recommendation layer that surfaces what matters for a specific trader's book.

Key framing on data volume and processing:

- **"It takes me four seconds to say a sentence, but in that time Moshi has learned 300 new pieces of information"** — a vivid order-of-magnitude for the throughput the system sustains.
- The data it processes is organized in **three layers**, fed through a **cleaning → statistical/ML → tagging** pipeline:
  1. **Constantly-updated news**
  2. **Time-series fundamentals**
  3. **Unstructured data** (X/posts, voice, alternative data) plus **user-private data** — e.g., a trader's own view of "how many LNG ships are transiting the Strait of Hormuz."
- The recommendation layer's job is to connect that firehose to what is *decision-relevant for the individual trader's book*, rather than a generic news feed.

## "You are the team" — lessons on building

The episode title captures her hardest-won lesson about building an AI-native startup as a domain expert:

- **The "you are the team" pressure**: AI engineers are pushed to do everything themselves — the tools make solo building possible but also create pressure to never delegate or hire.
- **Talk to customers before you hire.** Her learned discipline is that customer conversations come *first*; building/hiring is secondary to validating against real traders' workflows.

## Why it matters

Moshi is a clean example of **AI agents × a vertical domain (commodities / financial trading)** — a domain-expert founder encoding proprietary workflow knowledge into a recommendation + retrieval agent, rather than a general-purpose assistant. It illustrates the "vertical agent" pattern: deep domain data + tailored interface + recommendation logic beats a horizontal chatbot for expert users.

## See also

- [[concepts/agentic-search]]
- [[concepts/agent-economics]]

*(The "vertical agent" / vertical-AI pattern and the Latent Space podcast do not yet have dedicated wiki pages.)*

## References

- Latent Space / AI Engineer NYC — "You are the Team — Anekha Sokhal, Moshi" (Oct 2026). Source: raw/newsletters/2026-10-22-the-recommendation-engine-for-commodity-traders-anekha-sokhal-moshi.md
